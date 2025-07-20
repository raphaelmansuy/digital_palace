#!/usr/bin/env python3
"""
LinkedIn Post Word Counter Tool (DEPRECATED)
This tool has been superseded by linkedin_character_counter.py
LinkedIn posts are now limited by character count (1800 chars) rather than word count (400 words).

For new projects, use linkedin_character_counter.py instead.
"""

import re
import sys
import argparse
from pathlib import Path

print("⚠️  DEPRECATION WARNING: This tool uses word count (400 words max)")
print("LinkedIn posts are now limited to 1800 characters.")
print("Please use linkedin_character_counter.py for accurate validation.")
print("=" * 60)

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
            return content, None
        
        # Extract content between first and last ruler
        start_idx = ruler_indices[0] + 1
        end_idx = ruler_indices[-1]
        
        linkedin_content = '\n'.join(lines[start_idx:end_idx])
        
        # Extract title from main header (first line before rulers)
        title = None
        for line in lines[:ruler_indices[0]]:
            if line.startswith('# '):
                title = line[2:].strip()
                break
        
        return linkedin_content, title
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None

def check_title_requirement(content, title):
    """Check if content starts with the required title format."""
    if not content or not title:
        return False, "Could not extract title or content"
    
    # Check if content starts with ## followed by the title (WITHOUT 👉 emoji)
    lines = content.strip().split('\n')
    if not lines:
        return False, "Content is empty"
    
    first_line = lines[0].strip()
    expected_format = f"## {title}"
    
    if first_line == expected_format:
        return True, "Title requirement met"
    else:
        return False, f"Expected: '{expected_format}', Found: '{first_line}'"

def count_words(text):
    """Count words in text, excluding markdown formatting."""
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
    """Analyze a LinkedIn post file for word count compliance and title requirement."""
    content, title = extract_linkedin_content(file_path)
    if content is None:
        return False
    
    word_count = count_words(content)
    
    print(f"File: {file_path}")
    print(f"Word count: {word_count}")
    print(f"Word limit: {word_limit}")
    
    # Check word count
    word_count_ok = word_count <= word_limit
    if word_count_ok:
        print(f"✅ PASS: Post is within {word_limit} word limit")
    else:
        excess = word_count - word_limit
        print(f"❌ FAIL: Post exceeds limit by {excess} words")
        print(f"Reduction needed: {excess} words ({excess/word_count*100:.1f}%)")
    
    # Check title requirement
    title_ok, title_message = check_title_requirement(content, title)
    if title_ok:
        print(f"✅ PASS: {title_message}")
    else:
        print(f"❌ FAIL: {title_message}")
    
    return word_count_ok and title_ok

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
        content, title = extract_linkedin_content(file_path)
        if content:
            print("\n--- Content Preview ---")
            print(content[:500] + "..." if len(content) > 500 else content)
            if title:
                print("\n--- Extracted Title ---")
                print(f"'{title}'")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
