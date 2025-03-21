#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import logging
import os

logger = logging.getLogger(__name__)

class DBManager:
    def __init__(self, db_path):
        """Initialize database manager
        
        Args:
            db_path (str): Path to SQLite database file
        """
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize the database and create tables if they don't exist"""
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create visited_urls table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS visited_urls (
                        url_hash TEXT PRIMARY KEY,
                        url TEXT NOT NULL,
                        file_path TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                
                # Create index on url for faster lookups
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_url ON visited_urls(url)
                """)
                
                conn.commit()
        except Exception as e:
            logger.error(f"Error initializing database: {str(e)}")
            raise
    
    def add_visited_url(self, url_hash, url, file_path):
        """Add a visited URL to the database
        
        Args:
            url_hash (str): MD5 hash of the URL
            url (str): The visited URL
            file_path (str): Path where the content is saved
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO visited_urls (url_hash, url, file_path)
                    VALUES (?, ?, ?)
                """, (url_hash, url, file_path))
                conn.commit()
        except Exception as e:
            logger.error(f"Error adding visited URL: {str(e)}")
            raise
    
    def get_visited_urls(self):
        """Get all visited URLs from the database
        
        Returns:
            set: Set of visited URLs
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT url FROM visited_urls")
                return {row[0] for row in cursor.fetchall()}
        except Exception as e:
            logger.error(f"Error getting visited URLs: {str(e)}")
            return set()
    
    def get_file_path(self, url):
        """Get file path for a visited URL
        
        Args:
            url (str): The URL to look up
            
        Returns:
            str: File path if found, None otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT file_path FROM visited_urls
                    WHERE url = ?
                """, (url,))
                result = cursor.fetchone()
                return result[0] if result else None
        except Exception as e:
            logger.error(f"Error getting file path: {str(e)}")
            return None