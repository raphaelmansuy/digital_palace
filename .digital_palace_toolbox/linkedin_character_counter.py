#!/usr/bin/env python3
"""
LinkedIn Post Character Counter Tool
Verifies that LinkedIn post content is under 1800 characters.
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

def count_characters(text):
    """Count characters in text, excluding markdown formatting."""
    if not text:
        return 0
    
    # Remove markdown code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # Remove inline code
    text = re.sub(r'`[^`]*`', '', text)
    
    # Remove markdown links [text](url) - keep only the link text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove markdown formatting characters (* ** _ __ # etc.) but keep the content
    text = re.sub(r'[*_#`>-]', '', text)
    
    # Remove extra whitespace but keep single spaces and newlines
    text = re.sub(r'[ \t]+', ' ', text)  # Multiple spaces/tabs to single space
    text = re.sub(r'\n+', '\n', text)    # Multiple newlines to single newline
    
    # Count characters (including spaces and newlines for readability)
    return len(text.strip())

def analyze_post(file_path, char_limit=1800):
    """Analyze a LinkedIn post file for character count compliance and title requirement."""
    content, title = extract_linkedin_content(file_path)
    if content is None:
        return False
    
    char_count = count_characters(content)
    
    print(f"File: {file_path}")
    print(f"Character count: {char_count}")
    print(f"Character limit: {char_limit}")
    
    # Check character count
    char_count_ok = char_count <= char_limit
    if char_count_ok:
        print(f"✅ PASS: Post is within {char_limit} character limit")
        remaining = char_limit - char_count
        print(f"Remaining characters: {remaining} ({remaining/char_limit*100:.1f}% available)")
    else:
        excess = char_count - char_limit
        print(f"❌ FAIL: Post exceeds limit by {excess} characters")
        print(f"Reduction needed: {excess} characters ({excess/char_count*100:.1f}%)")
    
    # Check title requirement
    title_ok, title_message = check_title_requirement(content, title)
    if title_ok:
        print(f"✅ PASS: {title_message}")
    else:
        print(f"❌ FAIL: {title_message}")
    
    return char_count_ok and title_ok

def main():
    parser = argparse.ArgumentParser(description='Check LinkedIn post character count')
    parser.add_argument('file', help='Path to the markdown file')
    parser.add_argument('--limit', type=int, default=1800, help='Character limit (default: 1800)')
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
            
            # Show character distribution
            print("\n--- Character Analysis ---")
            raw_chars = len(content)
            cleaned_chars = count_characters(content)
            print(f"Raw content characters: {raw_chars}")
            print(f"Cleaned content characters: {cleaned_chars}")
            print(f"Formatting overhead: {raw_chars - cleaned_chars} characters")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
