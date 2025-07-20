#!/usr/bin/env python3
"""
Example usage of the Markdown to DOCX converter

This script demonstrates how to use the converter programmatically.
"""

import os
import sys
from pathlib import Path

# Add the current directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from markdown_to_docx_converter import MarkdownToDocxConverter


def convert_example():
    """Convert the AI collaboration post to DOCX"""
    # Input and output paths
    input_file = "../../personal/elitizon_linkedin/post_02_95_percent_fail_ai_collaboration.md"
    output_file = "../../tmp/ai_collaboration_post.docx"
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        print("Converting markdown to DOCX...")
        converter = MarkdownToDocxConverter(input_file, output_file)
        converter.convert()
        print(f"✅ Successfully converted to: {output_file}")
        
        # Check if the file was created
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"📄 Output file size: {file_size} bytes")
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return 1
    
    return 0


def convert_custom_file(input_path: str, output_path: str):
    """Convert any markdown file to DOCX"""
    try:
        print(f"Converting {input_path} to DOCX...")
        converter = MarkdownToDocxConverter(input_path, output_path)
        converter.convert()
        print(f"✅ Successfully converted to: {output_path}")
        return 0
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return 1


if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Custom file conversion
        exit(convert_custom_file(sys.argv[1], sys.argv[2]))
    else:
        # Default example
        exit(convert_example())
