#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import time
import requests
import logging
import hashlib
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
from markdownify import markdownify as md
from concurrent.futures import ThreadPoolExecutor
import random
from db_manager import DBManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("crawler.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LiangLiangLeeCrawler:
    def __init__(self, base_url="https://learn.lianglianglee.com", output_dir="output", delay=1):
        """
        Initialize the crawler
        
        Args:
            base_url (str): The base URL of the website to crawl
            output_dir (str): Directory to save the crawled content
            delay (int): Delay between requests in seconds to avoid overloading the server
        """
        self.base_url = base_url
        self.output_dir = output_dir
        self.delay = delay
        self.visited_urls = set()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        })
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Initialize database manager
        self.db_manager = DBManager(os.path.join(output_dir, 'visited_urls.db'))
        self.visited_urls = self.db_manager.get_visited_urls()
    
    def is_valid_url(self, url):
        """
        Check if the URL is valid and belongs to the target domain
        
        Args:
            url (str): URL to check
            
        Returns:
            bool: True if the URL is valid, False otherwise
        """
        parsed_url = urlparse(url)
        parsed_base = urlparse(self.base_url)
        
        # Check if the URL belongs to the target domain
        if parsed_url.netloc != parsed_base.netloc:
            return False
        
        # Check for allowed file extensions
        has_valid_extension = url.endswith('.md') or url.endswith('.jpg') or url.endswith('.png') or url.endswith('.pdf')
        
        # Check for specific strings in URL path that indicate valid content
        path = unquote(parsed_url.path.lower())
        valid_strings = ['/专栏/', '/文章/', '/极客时间/']
        contains_valid_string = any(s.lower() in path for s in valid_strings)
        
        return has_valid_extension or contains_valid_string
    
    def get_page_content(self, url):
        """
        Get the content of a page
        
        Args:
            url (str): URL to fetch
            
        Returns:
            tuple: (soup, response.text) or (None, None) if failed
        """
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup, response.text
            else:
                logger.error(f"Failed to fetch {url}, status code: {response.status_code}")
                return None, None
        except Exception as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None, None
    
    def extract_links(self, soup, current_url):
        """
        Extract all links from a page
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            current_url (str): Current URL for resolving relative URLs
            
        Returns:
            list: List of absolute URLs
        """
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            absolute_url = urljoin(current_url, href)
            
            # Only add URLs that belong to the target domain
            if self.is_valid_url(absolute_url) and absolute_url not in self.visited_urls:
                links.append(absolute_url)
        
        return links
    
    def convert_to_markdown(self, soup, url):
        """
        Convert HTML content to Markdown
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            url (str): URL of the page
            
        Returns:
            str: Markdown content
        """
        # Find the book content container
        main_content = soup.find('div', class_='book-content')
        
        if not main_content:
            logger.warning(f"No 'book-content' div found in {url}")
            return None
        
        # URL decode all links and convert to relative paths
        for link in main_content.find_all('a', href=True):
            href = unquote(link['href'])
            # Convert absolute URLs to relative paths if they match base URL
            if href.startswith(self.base_url):
                href = href[len(self.base_url):]
                if not href.startswith('/'):
                    href = '/' + href
            link['href'] = href
        
        # Add title
        title = soup.title.string if soup.title else "Untitled"
        markdown_content = f"# {title}\n\n"
        
        # Add source URL as reference
        markdown_content += f"Source: {unquote(url)}\n\n"
        
        # Convert HTML to Markdown
        markdown_content += md(str(main_content), heading_style="ATX")
        
        return markdown_content
    
    def get_save_to_file_path(self, url):
        """Generate a file path from a URL
        
        Args:
            url (str): The URL to generate a file path from
            
        Returns:
            str: The generated file path
        """
        # Parse URL to create a file path
        parsed_url = urlparse(url)
        path_parts = [unquote(part) for part in parsed_url.path.strip('/').split('/')]
        
        # Create directory structure
        if path_parts and path_parts[0]:
            dir_path = os.path.join(self.output_dir, *path_parts[:-1]) if len(path_parts) > 1 else self.output_dir
        else:
            dir_path = self.output_dir
        
        # Create filename
        if path_parts and path_parts[-1]:
            # URL decode the filename to convert %xx sequences to their original characters
            filename = unquote(path_parts[-1])
        else:
            filename = 'index'
        
        # Handle file extensions
        if url.endswith('.pdf'):
            if not filename.endswith('.pdf'):
                filename += '.pdf'
        else:
            if not filename.endswith('.md'):
                filename += '.md'
        
        # Ensure directory exists
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        
        return os.path.join(dir_path, filename)

    def save_to_file(self, url, content):
        file_path = self.get_save_to_file_path(url)
        
        # Handle PDF files differently
        if url.endswith('.pdf'):
            # Save PDF content in binary mode
            with open(file_path, 'wb') as f:
                f.write(content)
        else:
            # Save markdown content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return file_path
    
    def get_url_hash(self, url):
        """Generate MD5 hash for a URL"""
        return hashlib.md5(url.encode('utf-8')).hexdigest()

    def save_visited_url(self, url, file_path):
        """Save visited URL and its file path to database"""
        try:
            url_hash = self.get_url_hash(url)
            self.db_manager.add_visited_url(url_hash, url, file_path)
        except Exception as e:
            logger.error(f"Error saving visited URL: {str(e)}")
    
    def crawl_page(self, url):
        # Check if URL is already visited and file exists
        try:
            file_path = self.db_manager.get_file_path(url)
            if file_path and os.path.exists(file_path):
                logger.info(f"Skipping {url}, already downloaded to {file_path}")
                if url not in self.visited_urls:
                    self.visited_urls.add(url)
                return []
        except Exception as e:
            logger.error(f"Error checking visited URL: {str(e)}")
        
        # Check if file_path exists
        file_path = self.get_save_to_file_path(url)
        if os.path.exists(file_path):
            logger.info(f"Skipping {url}, already downloaded to {file_path}")
            if url not in self.visited_urls:
                self.visited_urls.add(url)
            return []

        self.visited_urls.add(url)
        logger.info(f"Crawling: {url}")
        
        # Add delay to avoid overloading the server
        time.sleep(self.delay)
        
        # For PDF files, download directly without parsing
        if url.endswith('.pdf'):
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    file_path = self.save_to_file(url, response.content)
                    logger.info(f"Saved PDF: {url} -> {file_path}")
                    self.save_visited_url(url, file_path)
                    return []
                else:
                    logger.error(f"Failed to fetch PDF {url}, status code: {response.status_code}")
                    return []
            except Exception as e:
                logger.error(f"Error fetching PDF {url}: {str(e)}")
                return []
        
        # For non-PDF files, continue with normal HTML processing
        soup, html_content = self.get_page_content(url)
        if not soup:
            return []
        
        # Extract links
        links = self.extract_links(soup, url)
        
        # Convert to markdown and save
        markdown_content = self.convert_to_markdown(soup, url)
        file_path = self.save_to_file(url, markdown_content)
        logger.info(f"Saved: {url} -> {file_path}")
        self.save_visited_url(url, file_path)
        
        # Add random sleep between 5 and 60 seconds after each page crawl
        random_sleep = random.randint(5, 60)
        logger.info(f"Sleeping for {random_sleep} seconds...")
        time.sleep(random_sleep)
        
        return links
    
    def crawl(self, max_pages=None, concurrency=4):
        """
        Start crawling from the base URL
        
        Args:
            max_pages (int, optional): Maximum number of pages to crawl
            concurrency (int): Number of concurrent crawling threads
        """
        to_visit = [self.base_url]
        crawled_count = 0
        
        with ThreadPoolExecutor(max_workers=concurrency) as executor:
            while to_visit and (max_pages is None or crawled_count < max_pages):
                # Take a batch of URLs to process concurrently
                batch = []
                while to_visit and len(batch) < concurrency:
                    batch.append(to_visit.pop(0))
                
                # Process the batch
                future_to_url = {executor.submit(self.crawl_page, url): url for url in batch}
                
                for future in future_to_url:
                    url = future_to_url[future]
                    try:
                        new_links = future.result()
                        # Add new links to the queue
                        for link in new_links:
                            if link not in self.visited_urls and link not in to_visit:
                                to_visit.append(link)
                        
                        crawled_count += 1
                        if max_pages and crawled_count >= max_pages:
                            break
                    except Exception as e:
                        logger.error(f"Error processing {url}: {str(e)}")
        
        logger.info(f"Crawling completed. Visited {len(self.visited_urls)} pages.")


def main():
    # Create and run the crawler
    crawler1 = LiangLiangLeeCrawler(
        base_url="https://learn.lianglianglee.com/%e4%b8%93%e6%a0%8f",
        output_dir="output",
        delay=10  # 1 second delay between requests
    )
    
    # Start crawling
    crawler1.crawl(max_pages=None, concurrency=3)


    # Create and run the crawler
    crawler2 = LiangLiangLeeCrawler(
        base_url="https://learn.lianglianglee.com/%e4%b8%93%e6%a0%8f",
        output_dir="output",
        delay=10  # 1 second delay between requests
    )
    
    # Start crawling
    crawler2.crawl(max_pages=None, concurrency=3)

    # Create and run the crawler
    crawler3 = LiangLiangLeeCrawler(
        base_url="https://learn.lianglianglee.com/%e6%9e%81%e5%ae%a2%e6%97%b6%e9%97%b4",
        output_dir="output",
        delay=10  # 1 second delay between requests
    )
    
    # Start crawling
    crawler3.crawl(max_pages=None, concurrency=3)

if __name__ == "__main__":
    main()