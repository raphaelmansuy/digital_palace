# LinkedIn Post Quality Checklist

Use this checklist before publishing any LinkedIn post.

## Pre-Publication Validation

### Word Count
- [ ] Run: `python3 check_post.py "path/to/post.md"`
- [ ] Verify: Word count ≤ 400 words
- [ ] Check: Content measured between rulers only

### Structure Requirements
- [ ] Header metadata above first ruler (`---`)
- [ ] Main content between first and last ruler
- [ ] Footer/series info below last ruler
- [ ] Maximum 1 code block in entire post
- [ ] Clear problem → solution → action flow

### Content Quality
- [ ] Engaging hook in first 50 words
- [ ] Specific data/percentages included
- [ ] Academic reference cited
- [ ] Clear, actionable call to action
- [ ] Professional yet approachable tone

### Technical Validation
- [ ] No markdown linting errors
- [ ] Proper heading hierarchy (## ###)
- [ ] Lists surrounded by blank lines
- [ ] Code blocks properly formatted

### Final Check
- [ ] Provides immediate actionable value
- [ ] Maintains professional credibility
- [ ] Advances series narrative
- [ ] Encourages meaningful discussion

## Validation Commands

```bash
# Quick validation
python3 check_post.py "personal/elitizon_linkedin/post_name.md"

# Detailed analysis  
python3 linkedin_word_counter.py "personal/elitizon_linkedin/post_name.md" --verbose
```

## Success Criteria
✅ All checklist items completed
✅ Automated validation passes
✅ Ready for LinkedIn publication
