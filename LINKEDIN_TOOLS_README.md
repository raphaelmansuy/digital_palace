# LinkedIn Post Character Counter Tools

This directory contains Python tools to verify that LinkedIn posts meet the 3000-character limit requirement.

## Files

- `linkedin_character_counter.py` - Comprehensive character counting tool with detailed analysis
- `check_post.py` - Simple checker script for quick validation
- `linkedin_word_counter.py` - Legacy word counter (deprecated)

## Usage

### Quick Check
```bash
python3 check_post.py "path/to/your/post.md"
```

### Detailed Analysis
```bash
python3 linkedin_character_counter.py "path/to/your/post.md" --verbose
```

### Custom Character Limit
```bash
python3 linkedin_character_counter.py "path/to/your/post.md" --limit 2500
```

## How It Works

The tools automatically:
1. Extract content between the first and last ruler markers (`---`)
2. Remove markdown formatting (code blocks, links, emphasis)
3. Count actual characters in the content
4. Provide pass/fail status with detailed metrics

## Example Output

```
File: personal/elitizon_linkedin/post_02_95_percent_fail_ai_collaboration.md
Character count: 2347
Character limit: 2500
✅ PASS: Post is within 2500 character limit
Remaining characters: 153 (6.1% available)
🎉 Your LinkedIn post is ready to publish!
```

## Integration

You can integrate these tools into your workflow:
- Add as VS Code tasks
- Use in CI/CD pipelines
- Create git pre-commit hooks

## Migration from Word Count

Previous versions used a 400-word limit. The new 3000-character limit provides more accurate control over LinkedIn post length, as LinkedIn's actual limit is character-based.
- Add to your content creation process

## Content Rules

The tools count content between ruler markers (`---`) and exclude:
- Markdown formatting
- Code blocks
- Inline code
- Link URLs (but count link text)
- Headers and metadata above the first ruler
