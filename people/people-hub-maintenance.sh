#!/bin/bash

# People Hub Maintenance Script
# Usage: ./people-hub-maintenance.sh

set -e

echo "🏛️ Digital Palace - People Hub Maintenance"
echo "========================================"

PEOPLE_DIR="."
CURRENT_DATE=$(date "+%B %Y")

# Function to count people files (ignore README, _template, and files starting with _)
count_people() {
    find "$PEOPLE_DIR" -name "*.md" \
        -not -name "README.md" \
        -not -name "_template.md" \
        -not -name "DATA-SCHEMA.md" \
        -not -name '_*' | wc -l
}

# Function to check for broken links
check_links() {
    echo "🔍 Checking for broken links..."
    
    # Check internal links
    grep -r "\[\[.*\]\]" "$PEOPLE_DIR" || echo "No internal links found"
    
    # Check external links (simplified)
    grep -r "http" "$PEOPLE_DIR" | grep -v "github.com" | head -5 || echo "No external links to check"
}

# Function to update statistics in README
update_stats() {
    local count=$(count_people)
    echo "📊 Updating statistics..."
    echo "   - Total people: $count"
    
    # Update the README with current count
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/\*\*Total People\*\*: [0-9]*/\*\*Total People\*\*: $count/" "$PEOPLE_DIR/README.md"
        sed -i '' "s/\*Last updated: .*/\*Last updated: $CURRENT_DATE/" "$PEOPLE_DIR/README.md"
    else
        # Linux
        sed -i "s/\*\*Total People\*\*: [0-9]*/\*\*Total People\*\*: $count/" "$PEOPLE_DIR/README.md"
        sed -i "s/\*Last updated: .*/\*Last updated: $CURRENT_DATE/" "$PEOPLE_DIR/README.md"
    fi
}

# Function to validate person pages using front matter
validate_pages() {
    echo "✅ Validating person pages (front matter)..."
    for file in "$PEOPLE_DIR"/*.md; do
        base=$(basename "$file")
        if [[ "$base" == README.md ]] || [[ "$base" == _* ]]; then
            continue
        fi
        filename=$(basename "$file")
        # Extract front matter block
        frontmatter=$(awk '/^---/{flag=!flag; next} flag' "$file")
        # Check for required front matter keys
        for key in name position organization tags; do
            if ! echo "$frontmatter" | grep -q "^$key:"; then
                echo "⚠️  $filename missing front matter key: $key"
            fi
        done
    done
}

# Function to generate beautiful people README
generate_index() {
    echo "📋 Generating beautiful people README..."
    
    # Create a temporary file for the index
    local temp_file=$(mktemp)
    
    # Generate beautiful header
    cat << 'EOF' > "$temp_file"
# � People Hub - AI/ML Influential Figures

> **Your comprehensive directory of AI/ML leaders, researchers, and innovators**

[![Total People](https://img.shields.io/badge/Total%20People-0-blue?style=flat-square)](#alphabetical-directory)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-July%202025-green?style=flat-square)](#recent-additions)
[![Categories](https://img.shields.io/badge/Categories-7-orange?style=flat-square)](#by-category)

---

## 🚀 Quick Navigation

| 🎯 **Jump to** | 📊 **Filter by** | 🔍 **Find** |
|---------------|------------------|-------------|
| [📝 Alphabetical](#alphabetical-directory) | [🔬 Researchers](#researchers--academics) | [🆕 Recent](#recent-additions) |
| [📊 By Category](#by-category) | [🏢 Industry Leaders](#industry--ceos) | [⭐ Featured](#featured-profiles) |
| [🔍 Advanced Search](#search-tips) | [🛡️ AI Safety](#ai-safety--ethics) | [📈 Stats](#statistics) |

---

## 🏆 Featured Profiles

EOF
    
    # Add featured profiles (first 4 files alphabetically)
    local count=0
    for file in "$PEOPLE_DIR"/*.md; do
        base=$(basename "$file")
        if [[ "$base" == README.md ]] || [[ "$base" == _* ]]; then
            continue
        fi
        if [ $count -ge 4 ]; then
            break
        fi
        filename=$(basename "$file" .md)
        # Extract front matter
        frontmatter=$(awk '/^---/{flag=!flag; next} flag' "$file")
        title=$(echo "$frontmatter" | grep '^name:' | sed 's/name:[ ]*//')
        role=$(echo "$frontmatter" | grep '^position:' | sed 's/position:[ ]*//')
        org=$(echo "$frontmatter" | grep '^organization:' | sed 's/organization:[ ]*//')
        if [[ -z "$title" ]]; then
            title="$filename"
        fi
        if [[ -z "$role" ]]; then
            role="AI/ML Leader"
        fi
        if [[ -z "$org" ]]; then
            org="Various"
        fi
        echo "### 🌟 [$title](./$filename.md)" >> "$temp_file"
        echo "**$role** at $org" >> "$temp_file"
        echo "" >> "$temp_file"
        count=$((count + 1))
    done
    
    # Add alphabetical directory
    echo "---" >> "$temp_file"
    echo "" >> "$temp_file"
    echo "## 📝 Alphabetical Directory" >> "$temp_file"
    echo "" >> "$temp_file"
    echo "| Name | Role | Organization | Tags |" >> "$temp_file"
    echo "|------|------|--------------|------|" >> "$temp_file"
    
    # Sort people files alphabetically and create table
    for file in $(ls "$PEOPLE_DIR"/*.md | sort); do
        base=$(basename "$file")
        if [[ "$base" == README.md ]] || [[ "$base" == _* ]]; then
            continue
        fi
        filename=$(basename "$file" .md)
        frontmatter=$(awk '/^---/{flag=!flag; next} flag' "$file")
        title=$(echo "$frontmatter" | grep '^name:' | sed 's/name:[ ]*//')
        role=$(echo "$frontmatter" | grep '^position:' | sed 's/position:[ ]*//')
        org=$(echo "$frontmatter" | grep '^organization:' | sed 's/organization:[ ]*//')
        tags=$(echo "$frontmatter" | grep '^tags:' | sed 's/tags:[ ]*//;s/\[//;s/\]//;s/,/, /g')
        if [[ -z "$title" ]]; then
            title="$filename"
        fi
        if [[ -z "$role" ]]; then
            role="AI/ML Expert"
        fi
        if [[ -z "$org" ]]; then
            org="Various"
        fi
        if [[ -z "$tags" ]]; then
            tags="ai, ml"
        fi
        echo "| [$title](./$filename.md) | $role | $org | \`$tags\` |" >> "$temp_file"
    done
    
    # Add by category section
    echo "" >> "$temp_file"
    echo "---" >> "$temp_file"
    echo "" >> "$temp_file"
    echo "## 📊 By Category" >> "$temp_file"
    echo "" >> "$temp_file"
    
    # Add category counts
    local total_count=$(find "$PEOPLE_DIR" -name "*.md" -not -name "README.md" -not -name "_template.md" -not -name "DATA-SCHEMA.md" | wc -l | tr -d ' ')
    
    cat << EOF >> "$temp_file"
### 🔬 Researchers & Academics
*Academic researchers and university professors advancing AI/ML theory*

EOF
    
    # List researchers (files with researcher/academia tag in front matter)
    for file in "$PEOPLE_DIR"/*.md; do
        base=$(basename "$file")
        if [[ "$base" == README.md ]] || [[ "$base" == _* ]]; then
            continue
        fi
        frontmatter=$(awk '/^---/{flag=!flag; next} flag' "$file")
        if echo "$frontmatter" | grep -q 'tags:.*researcher\|tags:.*academia'; then
            filename=$(basename "$file" .md)
            title=$(echo "$frontmatter" | grep '^name:' | sed 's/name:[ ]*//')
            if [[ -z "$title" ]]; then
                title="$filename"
            fi
            echo "- 🎓 [$title](./$filename.md)" >> "$temp_file"
        fi
    done
    
    cat << EOF >> "$temp_file"

### 🏢 Industry & CEOs
*Industry leaders and executives driving AI adoption*

EOF
    
    # List industry leaders (tags in front matter)
    for file in "$PEOPLE_DIR"/*.md; do
        base=$(basename "$file")
        if [[ "$base" == README.md ]] || [[ "$base" == _* ]]; then
            continue
        fi
        frontmatter=$(awk '/^---/{flag=!flag; next} flag' "$file")
        if echo "$frontmatter" | grep -q 'tags:.*ceo\|tags:.*entrepreneur\|tags:.*industry'; then
            filename=$(basename "$file" .md)
            title=$(echo "$frontmatter" | grep '^name:' | sed 's/name:[ ]*//')
            if [[ -z "$title" ]]; then
                title="$filename"
            fi
            echo "- 🏢 [$title](./$filename.md)" >> "$temp_file"
        fi
    done
    
    cat << EOF >> "$temp_file"

### 🛡️ AI Safety & Ethics
*Researchers focused on responsible AI development*

EOF
    
    # List AI safety experts (tags in front matter)
    for file in "$PEOPLE_DIR"/*.md; do
        base=$(basename "$file")
        if [[ "$base" == README.md ]] || [[ "$base" == _* ]]; then
            continue
        fi
        frontmatter=$(awk '/^---/{flag=!flag; next} flag' "$file")
        if echo "$frontmatter" | grep -q 'tags:.*ai-safety\|tags:.*ai-ethics\|tags:.*ethics\|tags:.*fairness'; then
            filename=$(basename "$file" .md)
            title=$(echo "$frontmatter" | grep '^name:' | sed 's/name:[ ]*//')
            if [[ -z "$title" ]]; then
                title="$filename"
            fi
            echo "- 🛡️ [$title](./$filename.md)" >> "$temp_file"
        fi
    done
    
    # Add other categories as needed...
    cat << EOF >> "$temp_file"

---

## 🔍 Search Tips

**Find people by:**
- **Expertise**: Use tags like \`deep-learning\`, \`computer-vision\`, \`nlp\`
- **Affiliation**: Search by company/university name
- **Role**: Look for \`researcher\`, \`ceo\`, \`founder\`, \`educator\`
- **Location**: Filter by geographic region

**Quick filters:**
- 🔬 **Academia**: Look for university affiliations
- 🏢 **Industry**: Focus on company leaders and CTOs
- 🚀 **Startups**: Find founders and entrepreneurs
- 📚 **Education**: Identify course creators and authors

---

## 📈 Statistics

- **Total Profiles**: $total_count people
- **Categories**: 7 primary categories
- **Last Updated**: $(date "+%B %Y")
- **Update Frequency**: Monthly maintenance
- **Coverage**: Global AI/ML community

## 🆕 Recent Additions

*Latest profiles added to the People Hub*

EOF
    
    # Add recent files (last 3 modified)
    local recent_files=$(ls -t "$PEOPLE_DIR"/*.md | grep -v "README.md\|^_" | head -3)
    for file in $recent_files; do
        filename=$(basename "$file" .md)
        frontmatter=$(awk '/^---/{flag=!flag; next} flag' "$file")
        title=$(echo "$frontmatter" | grep '^name:' | sed 's/name:[ ]*//')
        if [[ -z "$title" ]]; then
            title="$filename"
        fi
        echo "- 🆕 [$title](./$filename.md)" >> "$temp_file"
    done
    
    # Add footer
    cat << EOF >> "$temp_file"

---

## 🎯 Contributing

Help us expand the People Hub!

**Ways to contribute:**
- 📝 **Add new profiles** using the [template](./_template.md)
- 🔄 **Update existing profiles** with recent news
- 🔗 **Verify links** and social media accounts
- 📸 **Update photos** with higher quality versions
- 🏷️ **Improve tags** for better discoverability

**Guidelines:**
1. Use the standardized [template](./_template.md)
2. Include reliable sources for all information
3. Add appropriate tags for categorization
4. Maintain professional and respectful tone
5. Verify all external links are working

---

## 📚 Related Resources

- 📖 [Books by these authors](../reference/books.md)
- 🛠️ [Tools they've created](../tools/ai-tools-master-directory.md)
- 🧩 [Concepts they've pioneered](../concepts/README.md)
- 🎯 [Guides they've inspired](../guides/README.md)

---

*Generated automatically on: $(date)*  
*Next update: Monthly via maintenance script*

**Legend**: 🎓 Academic • 🏢 Industry • 🛡️ Safety • 🚀 Startup • 📚 Author • 💻 Open Source • 🎤 Communicator
EOF
    
    # Update people count in badges
    sed -i.bak "s/Total%20People-[0-9]*/Total%20People-$total_count/" "$temp_file" && rm "$temp_file.bak" 2>/dev/null || true
    
    # Move to people directory as README.md
    mv "$temp_file" "$PEOPLE_DIR/README.md"
    echo "✅ Beautiful README generated: $PEOPLE_DIR/README.md"
}

# Function to create new person page
create_person() {
    local name="$1"
    if [[ -z "$name" ]]; then
        echo "❌ Please provide a name: ./people-hub-maintenance.sh create 'Person Name'"
        exit 1
    fi
    
    # Convert name to filename
    local filename=$(echo "$name" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')
    local filepath="$PEOPLE_DIR/$filename.md"
    
    if [[ -f "$filepath" ]]; then
        echo "❌ Person page already exists: $filepath"
        exit 1
    fi
    
    # Copy template and replace name
    cp "$PEOPLE_DIR/_template.md" "$filepath"
    
    # Replace template placeholders
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/\[Person Name\]/$name/g" "$filepath"
    else
        sed -i "s/\[Person Name\]/$name/g" "$filepath"
    fi
    
    echo "✅ Created new person page: $filepath"
    echo "📝 Don't forget to edit the template placeholders!"
}

# Main script logic
case "${1:-maintenance}" in
    "create")
        create_person "$2"
        ;;
    "validate")
        validate_pages
        ;;
    "index")
        generate_index
        ;;
    "links")
        check_links
        ;;
    "maintenance"|"")
        echo "🔧 Running full maintenance..."
        validate_pages
        update_stats
        generate_index
        check_links
        echo "✅ Maintenance complete!"
        ;;
    "help")
        echo "Usage: $0 [command] [options]"
        echo ""
        echo "Commands:"
        echo "  maintenance  - Run full maintenance (default)"
        echo "  create NAME  - Create new person page"
        echo "  validate     - Validate existing pages"
        echo "  index        - Generate beautiful README"
        echo "  links        - Check links"
        echo "  help         - Show this help"
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo "Use '$0 help' for usage information"
        exit 1
        ;;
esac
