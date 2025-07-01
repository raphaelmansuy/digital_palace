# 🤖 VSCode Copilot Integration Guide

This guide shows how to integrate the Digital Palace link checking tools with VSCode Copilot for automated link maintenance and issue resolution.

## 🔧 Available Commands

### Internal Link Checker
```bash
# Basic usage
python check_internal_links.py [files/directories]

# With specific format
python check_internal_links.py README.md --format json
python check_internal_links.py guides/ --format markdown
python check_internal_links.py --all --format text

# Save report to file
python check_internal_links.py README.md --format json --output internal_report.json
```

### External Link Checker
```bash
# Basic usage
python check_external_links.py [files/directories]

# With timeout
python check_external_links.py README.md --timeout 15

# Batch processing
python check_external_links.py guides/ tools/ --format json --timeout 20

# Save report
python check_external_links.py --all --format markdown --output external_report.md
```

## 📋 VSCode Copilot Integration Patterns

### 1. Automated Issue Detection

Use JSON output for programmatic processing:

```bash
# Get issues as JSON for processing
python check_internal_links.py README.md --format json > issues.json

# Process with jq (if available)
python check_internal_links.py README.md --format json | jq '.issues[] | select(.severity == "error")'
```

### 2. Quick Fix Generation

The tools provide `suggested_fix` fields in JSON output:

```json
{
  "line_number": 27,
  "link_text": "Best AI Tools →",
  "link_target": "./tools/ai-tools-master-directory.md#-beginner-friendly-tools",
  "issue_type": "missing_anchor",
  "description": "Anchor '-beginner-friendly-tools' not found",
  "severity": "error",
  "suggested_fix": "#beginner-friendly-tools"
}
```

### 3. Batch Processing

Check multiple directories:
```bash
python check_internal_links.py guides/ tools/ reference/ learning/ --format json
```

### 4. CI/CD Integration

Exit codes indicate success/failure:
- `0`: No issues found
- `1`: Issues found

```bash
# Check all files and fail if issues found
python check_internal_links.py --all && echo "All internal links OK!"
python check_external_links.py --all --timeout 10 && echo "All external links OK!"
```

## 🎯 Common Use Cases

### Fix Broken Internal Links

1. **Identify Issues**:
   ```bash
   python check_internal_links.py README.md --format json
   ```

2. **Common Issues & Solutions**:
   - **Missing Anchor**: Update anchor format (remove emoji characters)
   - **Wrong File Path**: Fix relative path
   - **Missing File**: Create file or update link

3. **Bulk Fix Strategy**:
   ```bash
   # Get all error-level issues
   python check_internal_links.py --all --format json | jq '.issues[] | select(.severity == "error")'
   ```

### Validate External Links

1. **Check Status**:
   ```bash
   python check_external_links.py README.md --timeout 10
   ```

2. **Common Issues & Solutions**:
   - **403 Forbidden**: May need authentication or is restricted
   - **404 Not Found**: URL incorrect or page moved
   - **Redirects**: Consider updating to final URL
   - **Timeout**: Increase timeout or check network

### Pre-commit Validation

Create a validation script:
```bash
#!/bin/bash
# validate_links.sh

echo "🔍 Checking internal links..."
python .digital_palace_toolbox/check_internal_links.py --all --format text

echo "🌐 Checking external links..."
python .digital_palace_toolbox/check_external_links.py --all --timeout 15 --format text

echo "✅ Link validation complete!"
```

## 📊 Report Formats

### JSON Format (Best for Automation)
- Machine-readable
- Structured error information
- Includes suggested fixes
- Perfect for CI/CD integration

### Markdown Format (Best for Reports)
- Human-readable
- GitHub-compatible
- Great for issue tracking
- Includes summary tables

### Text Format (Best for Terminal)
- Quick overview
- Console-friendly
- Good for development workflow

## 🛠️ Advanced Usage

### Filter by Severity
```bash
# Only show errors (JSON)
python check_internal_links.py README.md --format json | jq '.issues[] | select(.severity == "error")'

# Count issues by severity
python check_internal_links.py --all --format json | jq '.issues | group_by(.severity) | .[] | {severity: .[0].severity, count: length}'
```

### Performance Monitoring
```bash
# External links with performance data
python check_external_links.py guides/ --format json | jq '.issues[] | select(.response_time > 2.0)'
```

### Custom Reporting
```bash
# Create custom summary
python check_internal_links.py --all --format json | jq '{
  total_files: .total_files_checked,
  total_links: .total_links_found,
  errors: [.issues[] | select(.severity == "error")] | length,
  files_with_issues: [.issues[] | .file_path] | unique | length
}'
```

## 🔄 Workflow Integration

### 1. Development Workflow
```bash
# Before committing
python check_internal_links.py $(git diff --name-only --cached | grep '\.md$')
```

### 2. Documentation Review
```bash
# Check specific guide
python check_internal_links.py guides/ai-agents.md --format markdown
python check_external_links.py guides/ai-agents.md --timeout 15
```

### 3. Maintenance Tasks
```bash
# Weekly external link check
python check_external_links.py --all --format json --output weekly_external_report.json

# Monthly full validation
python check_internal_links.py --all --format markdown --output monthly_internal_report.md
```

## 🚨 Error Handling

### Common Exit Codes
- `0`: Success (no issues)
- `1`: Issues found
- `2`: Script error (file not found, etc.)

### Error Types
- **Internal Links**: `missing_file`, `missing_anchor`, `invalid_path`
- **External Links**: `timeout`, `connection_error`, `http_error`, `ssl_error`

### Debugging
```bash
# Verbose output (if issues occur)
python check_internal_links.py README.md --format text --verbose

# Check specific file thoroughly
python check_internal_links.py guides/mcp-servers.md --format json | jq '.issues'
```

## 💡 Tips for VSCode Copilot

1. **Use JSON for automation**: Easier to parse programmatically
2. **Save reports**: Keep track of improvements over time
3. **Set appropriate timeouts**: Balance speed vs. accuracy for external links
4. **Check before committing**: Prevent broken links from entering the repository
5. **Regular maintenance**: Run weekly/monthly checks for large repositories
6. **Focus on errors first**: Fix high-severity issues before warnings

## 🔗 Integration Examples

### VS Code Tasks
Add to `.vscode/tasks.json`:
```json
{
  "label": "Check Internal Links",
  "type": "shell",
  "command": "python",
  "args": [".digital_palace_toolbox/check_internal_links.py", "${file}", "--format", "text"],
  "group": "test",
  "presentation": {
    "reveal": "always",
    "panel": "new"
  }
}
```

### GitHub Actions
```yaml
name: Link Validation
on: [push, pull_request]
jobs:
  validate-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check Internal Links
        run: python .digital_palace_toolbox/check_internal_links.py --all
      - name: Check External Links
        run: python .digital_palace_toolbox/check_external_links.py --all --timeout 30
```

This comprehensive toolbox helps maintain link integrity and provides actionable feedback for VSCode Copilot to automatically identify and suggest fixes for broken links!
