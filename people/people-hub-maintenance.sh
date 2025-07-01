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

# Function to generate people index
generate_index() {
    echo "📋 Generating people index..."
    
    # Create a temporary file for the index
    local temp_file=$(mktemp)
    
    echo "# People Index" > "$temp_file"
    echo "" >> "$temp_file"
    echo "## Alphabetical List" >> "$temp_file"
    echo "" >> "$temp_file"
    
    # Sort people files alphabetically
    for file in "$PEOPLE_DIR"/*.md; do
        if [[ "$file" == *"README.md" ]] || [[ "$file" == *"_template.md" ]]; then
            continue
        fi
        
        filename=$(basename "$file" .md)
        title=$(head -1 "$file" | sed 's/# //')
        
        echo "- [$title](./$filename.md)" >> "$temp_file"
    done
    
    echo "" >> "$temp_file"
    echo "---" >> "$temp_file"
    echo "*Generated on: $(date)*" >> "$temp_file"
    
    # Move to people directory
    mv "$temp_file" "$PEOPLE_DIR/INDEX.md"
    echo "✅ Index generated: $PEOPLE_DIR/INDEX.md"
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
        echo "  index        - Generate people index"
        echo "  links        - Check links"
        echo "  help         - Show this help"
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo "Use '$0 help' for usage information"
        exit 1
        ;;
esac
