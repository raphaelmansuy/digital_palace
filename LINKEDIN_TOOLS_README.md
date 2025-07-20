# LinkedIn Post Word Counter Tools

This directory contains Python tools to verify that LinkedIn posts meet the 400-word limit requirement.

## Files

- `linkedin_word_counter.py` - Comprehensive word counting tool with detailed analysis
- `check_post.py` - Simple checker script for quick validation

## Usage

### Quick Check
```bash
python3 check_post.py "path/to/your/post.md"
```

### Detailed Analysis
```bash
python3 linkedin_word_counter.py "path/to/your/post.md" --verbose
```

### Custom Word Limit
```bash
python3 linkedin_word_counter.py "path/to/your/post.md" --limit 500
```

## How It Works

The tools automatically:
1. Extract content between the first and last ruler markers (`---`)
2. Remove markdown formatting (code blocks, links, emphasis)
3. Count actual words in the content
4. Provide pass/fail status with detailed metrics

## Example Output

```
File: personal/elitizon_linkedin/post_02_95_percent_fail_ai_collaboration.md
Word count: 386
Word limit: 400
✅ PASS: Post is within 400 word limit
🎉 Your LinkedIn post is ready to publish!
```

## Integration

You can integrate these tools into your workflow:
- Add as VS Code tasks
- Use in CI/CD pipelines
- Create git pre-commit hooks
- Add to your content creation process

## Content Rules

The tools count content between ruler markers (`---`) and exclude:
- Markdown formatting
- Code blocks
- Inline code
- Link URLs (but count link text)
- Headers and metadata above the first ruler
