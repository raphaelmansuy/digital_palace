#!/usr/bin/env python3
"""
LinkedIn Post Word Counter Tool
Verifies that LinkedIn post content is under 400 words.
Counts only the content between the rulers (---).
"""

import re
import sys
import argparse
from pathlib import Path

def extract_linkedin_content(file_path):
    """Extract content between the first and last rulers (---) in a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find content between first and last ruler
        ruler_pattern = r'^---\s*$'
        lines = content.split('\n')
        
        ruler_indices = []
        for i, line in enumerate(lines):
            if re.match(ruler_pattern, line.strip()):
                ruler_indices.append(i)
        
        if len(ruler_indices) < 2:
            print(f"Warning: Could not find two rulers (---) in {file_path}")
            return content
        
        # Extract content between first and last ruler
        start_idx = ruler_indices[0] + 1
        end_idx = ruler_indices[-1]
        
        linkedin_content = '\n'.join(lines[start_idx:end_idx])
        return linkedin_content
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def count_words(text):
    """Count words in text, excluding markdown formatting."""
    if not text:
        return 0
    
    # Remove markdown code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # Remove inline code
    text = re.sub(r'`[^`]*`', '', text)
    
    # Remove markdown links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove markdown formatting (* ** _ __ # etc.)
    text = re.sub(r'[*_#`>-]', '', text)
    
    # Remove extra whitespace and split into words
    words = text.split()
    
    # Filter out empty strings and count
    return len([word for word in words if word.strip()])

def analyze_post(file_path, word_limit=400):
    """Analyze a LinkedIn post file for word count compliance."""
    content = extract_linkedin_content(file_path)
    if content is None:
        return False
    
    word_count = count_words(content)
    
    print(f"File: {file_path}")
    print(f"Word count: {word_count}")
    print(f"Word limit: {word_limit}")
    
    if word_count <= word_limit:
        print(f"✅ PASS: Post is within {word_limit} word limit")
        return True
    else:
        excess = word_count - word_limit
        print(f"❌ FAIL: Post exceeds limit by {excess} words")
        print(f"Reduction needed: {excess} words ({excess/word_count*100:.1f}%)")
        return False

def main():
    parser = argparse.ArgumentParser(description='Check LinkedIn post word count')
    parser.add_argument('file', help='Path to the markdown file')
    parser.add_argument('--limit', type=int, default=400, help='Word limit (default: 400)')
    parser.add_argument('--verbose', action='store_true', help='Show detailed analysis')
    
    args = parser.parse_args()
    
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    success = analyze_post(file_path, args.limit)
    
    if args.verbose and not success:
        content = extract_linkedin_content(file_path)
        if content:
            print("\n--- Content Preview ---")
            print(content[:500] + "..." if len(content) > 500 else content)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
