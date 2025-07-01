#!/bin/bash

# People Hub Maintenance Script
# Usage: ./people-hub-maintenance.sh

set -e

echo "🏛️ Digital Palace - People Hub Maintenance"
echo "========================================"

PEOPLE_DIR="."
CURRENT_DATE=$(date "+%B %Y")

# Function to count people files
count_people() {
    find "$PEOPLE_DIR" -name "*.md" -not -name "README.md" -not -name "_template.md" | wc -l
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

# Function to validate person pages
validate_pages() {
    echo "✅ Validating person pages..."
    
    for file in "$PEOPLE_DIR"/*.md; do
        if [[ "$file" == *"README.md" ]] || [[ "$file" == *"_template.md" ]]; then
            continue
        fi
        
        filename=$(basename "$file")
        
        # Check if file has required sections
        if ! grep -q "## 🎯 Current Role" "$file"; then
            echo "⚠️  $filename missing Current Role section"
        fi
        
        if ! grep -q "## 📖 Biography" "$file"; then
            echo "⚠️  $filename missing Biography section"
        fi
        
        if ! grep -q "## 🏆 Key Contributions" "$file"; then
            echo "⚠️  $filename missing Key Contributions section"
        fi
        
        if ! grep -q "## 🔗 Social Media & Links" "$file"; then
            echo "⚠️  $filename missing Social Media & Links section"
        fi
        
        if ! grep -q "**Tags**:" "$file"; then
            echo "⚠️  $filename missing tags"
        fi
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
        if [[ "$file" == *"README.md" ]] || [[ "$file" == *"_template.md" ]] || [[ "$file" == *"DATA-SCHEMA.md" ]]; then
            continue
        fi
        
        if [ $count -ge 4 ]; then
            break
        fi
        
        filename=$(basename "$file" .md)
        title=$(head -1 "$file" | sed 's/# //')
        
        # Extract role/organization from current role section
        local role=$(grep -A 3 "## 🎯 Current Role" "$file" | grep "Position" | sed 's/.*Position\*\*: //' | head -1)
        local org=$(grep -A 5 "## 🎯 Current Role" "$file" | grep "Organization" | sed 's/.*Organization\*\*: //' | head -1)
        
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
        if [[ "$file" == *"README.md" ]] || [[ "$file" == *"_template.md" ]] || [[ "$file" == *"DATA-SCHEMA.md" ]]; then
            continue
        fi
        
        filename=$(basename "$file" .md)
        title=$(head -1 "$file" | sed 's/# //')
        
        # Extract role and organization
        local role=$(grep -A 3 "## 🎯 Current Role" "$file" | grep "Position" | sed 's/.*Position\*\*: //' | head -1)
        local org=$(grep -A 5 "## 🎯 Current Role" "$file" | grep "Organization" | sed 's/.*Organization\*\*: //' | head -1)
        
        # Extract first few tags
        local tags=$(grep "**Tags**:" "$file" | sed 's/.*Tags\*\*: //' | sed 's/#//g' | awk '{print $1 "," $2 "," $3}' | sed 's/,$//g')
        
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
    
    # List researchers (files with #researcher tag)
    for file in "$PEOPLE_DIR"/*.md; do
        if [[ "$file" == *"README.md" ]] || [[ "$file" == *"_template.md" ]] || [[ "$file" == *"DATA-SCHEMA.md" ]]; then
            continue
        fi
        
        if grep -q "#researcher\|#academia" "$file" 2>/dev/null; then
            filename=$(basename "$file" .md)
            title=$(head -1 "$file" | sed 's/# //')
            echo "- 🎓 [$title](./$filename.md)" >> "$temp_file"
        fi
    done
    
    cat << EOF >> "$temp_file"

### 🏢 Industry & CEOs
*Industry leaders and executives driving AI adoption*

EOF
    
    # List industry leaders
    for file in "$PEOPLE_DIR"/*.md; do
        if [[ "$file" == *"README.md" ]] || [[ "$file" == *"_template.md" ]] || [[ "$file" == *"DATA-SCHEMA.md" ]]; then
            continue
        fi
        
        if grep -q "#ceo\|#entrepreneur\|#industry" "$file" 2>/dev/null; then
            filename=$(basename "$file" .md)
            title=$(head -1 "$file" | sed 's/# //')
            echo "- 🏢 [$title](./$filename.md)" >> "$temp_file"
        fi
    done
    
    cat << EOF >> "$temp_file"

### 🛡️ AI Safety & Ethics
*Researchers focused on responsible AI development*

EOF
    
    # List AI safety experts
    for file in "$PEOPLE_DIR"/*.md; do
        if [[ "$file" == *"README.md" ]] || [[ "$file" == *"_template.md" ]] || [[ "$file" == *"DATA-SCHEMA.md" ]]; then
            continue
        fi
        
        if grep -q "#ai-safety\|#ai-ethics\|#ethics\|#fairness" "$file" 2>/dev/null; then
            filename=$(basename "$file" .md)
            title=$(head -1 "$file" | sed 's/# //')
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
    local recent_files=$(ls -t "$PEOPLE_DIR"/*.md | grep -v "README.md\|_template.md\|DATA-SCHEMA.md" | head -3)
    
    for file in $recent_files; do
        filename=$(basename "$file" .md)
        title=$(head -1 "$file" | sed 's/# //')
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
