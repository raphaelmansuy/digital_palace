#!/bin/bash

# Quick status check for LinkedIn posts conversion
echo "LinkedIn Posts Conversion Status"
echo "================================"

total_posts=$(find personal/elitizon_linkedin -name "post_*.md" | wc -l | tr -d ' ')
converted_posts=$(ls output/*.docx 2>/dev/null | wc -l | tr -d ' ')
image_files=$(ls output/*.png 2>/dev/null | wc -l | tr -d ' ')

echo "Total LinkedIn posts found: $total_posts"
echo "Posts converted to DOCX: $converted_posts"
echo "Code block images generated: $image_files"
echo ""

if [ $converted_posts -gt 0 ]; then
    echo "Progress: $(( converted_posts * 100 / total_posts ))% complete"
    echo ""
    echo "Latest converted files:"
    ls -lt output/*.docx | head -3 | awk '{print "  " $9 " (" $6 " " $7 " " $8 ")"}'
else
    echo "No conversions completed yet."
fi

echo ""
echo "Output directory size: $(du -sh output 2>/dev/null | cut -f1)"
