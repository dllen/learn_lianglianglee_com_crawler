#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
from urllib.parse import unquote

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("rename.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def rename_files_and_dirs(directory):
    """Recursively rename files and directories with URL-encoded names"""
    try:
        # Get all items in the directory
        items = os.listdir(directory)
        
        # Sort items to process directories first (in reverse order to handle nested dirs)
        items.sort(reverse=True)
        
        for item in items:
            old_path = os.path.join(directory, item)
            
            # Skip if the item is not URL encoded
            if '%' not in item:
                continue
            
            try:
                # Decode the URL-encoded name
                decoded_name = unquote(item)
                new_path = os.path.join(directory, decoded_name)
                
                # Skip if the decoded name is the same as the original
                if old_path == new_path:
                    continue
                
                # If the new path exists, we'll replace it
                if os.path.exists(new_path):
                    logger.info(f"Target path {new_path} exists, will be replaced")
                    # If it's a directory, we need to handle it differently
                    if os.path.isdir(new_path):
                        # First process the contents of the old directory
                        rename_files_and_dirs(old_path)
                        # Then remove the target directory and rename
                        import shutil
                        shutil.rmtree(new_path)
                        os.rename(old_path, new_path)
                        logger.info(f"Replaced directory: {old_path} -> {new_path}")
                    else:
                        # For files, simply remove the target and rename
                        os.remove(new_path)
                        os.rename(old_path, new_path)
                        logger.info(f"Replaced file: {old_path} -> {new_path}")
                else:
                    # If target doesn't exist, simply rename
                    os.rename(old_path, new_path)
                    logger.info(f"Renamed: {old_path} -> {new_path}")
                
                # If it's a directory, process its contents
                if os.path.isdir(new_path):
                    rename_files_and_dirs(new_path)
                    
            except Exception as e:
                logger.error(f"Error processing {old_path}: {str(e)}")
                
    except Exception as e:
        logger.error(f"Error accessing directory {directory}: {str(e)}")

def main():
    # Get the output directory path
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    
    if not os.path.exists(output_dir):
        logger.error(f"Output directory does not exist: {output_dir}")
        sys.exit(1)
    
    logger.info(f"Starting rename process in: {output_dir}")
    rename_files_and_dirs(output_dir)
    logger.info("Rename process completed")

if __name__ == "__main__":
    main()