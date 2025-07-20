#!/bin/bash

# Script to convert all LinkedIn posts to DOCX format
# Usage: ./process_linkedin_posts.sh

echo "🚀 Starting LinkedIn posts conversion to DOCX..."
echo "==============================================="

# Create output directory if it doesn't exist
mkdir -p ./output

# Find all LinkedIn post files (excluding helper files)
posts=$(find personal/elitizon_linkedin -name "post_*.md" | sort)

# Count total posts
total_posts=$(echo "$posts" | wc -l | tr -d ' ')
current=0

echo "Found $total_posts LinkedIn posts to convert"
echo ""

# Process each post
for post in $posts; do
    current=$((current + 1))
    filename=$(basename "$post")
    echo "[$current/$total_posts] Processing: $filename"
    
    # Run the converter
    ./.digital_palace_toolbox/markdown_to_docx/markdown_to_docx_converter.py "$post" --output-dir ./output
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully converted: $filename"
    else
        echo "❌ Failed to convert: $filename"
    fi
    echo ""
done

echo "🎉 Conversion completed!"
echo "Check the ./output directory for all converted DOCX files and images."
echo ""
echo "Summary:"
echo "- Total posts processed: $total_posts"
echo "- Output directory: ./output"
echo "- Each post generates: 1 DOCX file + code block images (PNG files)"
