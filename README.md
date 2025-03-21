# Learn.LiangLiangLee.com Crawler

A Python web crawler designed to backup the entire content of learn.lianglianglee.com in Markdown format.

## Features

- Crawls all pages on learn.lianglianglee.com
- Converts HTML content to Markdown format
- Maintains the original site structure in the output directory
- Respects rate limits to avoid overloading the server
- Supports concurrent crawling for faster backup
- Comprehensive logging for monitoring the crawling process

## Requirements

- Python 3.6+
- Required packages listed in `requirements.txt` or `pyproject.toml`

## Installation

1. Clone this repository
2. Install the required packages:

### Using pip

```bash
pip install -r requirements.txt
```

### Using uv (Recommended)

```bash
# Install uv if you don't have it yet
pip install uv

# Create and activate a virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .
```

## Usage

Run the crawler with default settings:

```bash
python crawler.py
```

The crawler will:
- Start from the base URL (https://learn.lianglianglee.com)
- Save all content to the `output` directory
- Maintain a 1-second delay between requests
- Use 3 concurrent threads for crawling

## Configuration

You can modify the following parameters in the `main()` function of `crawler.py`:

- `base_url`: The starting URL for crawling
- `output_dir`: Directory to save the crawled content
- `delay`: Delay between requests in seconds
- `max_pages`: Maximum number of pages to crawl (None for unlimited)
- `concurrency`: Number of concurrent crawling threads

## Output

The crawler saves content in the following structure:

```
output/
  ├── index.md
  ├── category1/
  │   ├── page1.md
  │   └── page2.md
  └── category2/
      └── page3.md
```

Each Markdown file contains:
- The page title as a heading
- The source URL as a reference
- The main content converted to Markdown

## Logging

The crawler logs its activity to both the console and a `crawler.log` file.