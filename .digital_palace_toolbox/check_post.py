#!/usr/bin/env python3
"""
Simple LinkedIn Character Counter Script
Quick check for character count compliance on LinkedIn posts.
"""

import sys
from pathlib import Path

# Add the current directory to the path so we can import our tool
sys.path.append(str(Path(__file__).parent))

from linkedin_character_counter import analyze_post

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check_post.py <markdown_file>")
        print("Example: python3 check_post.py personal/elitizon_linkedin/post_02.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    success = analyze_post(file_path)
    
    if success:
        print("\n🎉 Your LinkedIn post is ready to publish!")
    else:
        print("\n⚠️  Please reduce character count before publishing.")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
