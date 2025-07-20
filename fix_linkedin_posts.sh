#!/bin/bash

# LinkedIn Posts Quality Fix Script
# Fixes title and emoji formatting for all posts

echo "LinkedIn Posts Quality Fix Script"
echo "================================="

# Function to fix a single post
fix_post() {
    local file="$1"
    local basename=$(basename "$file")
    
    echo "Processing: $basename"
    
    # Extract the title from the first line starting with #
    title=$(grep -m1 '^# ' "$file" | sed 's/^# //')
    
    if [ -z "$title" ]; then
        echo "  ❌ No title found"
        return 1
    fi
    
    # Check if content already starts with title
    if grep -q "^## $title$" "$file"; then
        echo "  ✅ Title already present"
        # Add emoji to other headers but not the title
        sed -i '' '/^## '"$title"'$/!s/^## \([^👉]\)/## 👉 \1/g' "$file"
    else
        echo "  🔧 Adding title and fixing headers"
        # Find the first --- and add title after it
        awk -v title="$title" '
        /^---$/ && !found_first_ruler {
            print $0
            print ""
            print "## " title
            print ""
            found_first_ruler = 1
            next
        }
        /^## / && found_first_ruler {
            if ($0 !~ /^## 👉/ && $0 !~ title) {
                gsub(/^## /, "## 👉 ")
            }
        }
        { print }
        ' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi
    
    # Check compliance
    if python3 check_post.py "$file" >/dev/null 2>&1; then
        echo "  ✅ Post is now compliant"
        return 0
    else
        echo "  ⚠️  Post needs manual review"
        return 1
    fi
}

# Process posts based on arguments
if [ $# -eq 0 ]; then
    # Process all posts
    echo "Processing all posts..."
    fixed=0
    total=0
    
    for file in personal/elitizon_linkedin/post_*.md; do
        if [ -f "$file" ]; then
            total=$((total + 1))
            if fix_post "$file"; then
                fixed=$((fixed + 1))
            fi
            echo
        fi
    done
    
    echo "Summary: $fixed/$total posts fixed"
else
    # Process specific posts
    for post in "$@"; do
        file="personal/elitizon_linkedin/post_${post}_*.md"
        if ls $file 1> /dev/null 2>&1; then
            fix_post $file
        else
            echo "Post $post not found"
        fi
        echo
    done
fi
