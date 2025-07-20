# LinkedIn Post Quality Rules - Quick Reference

**Version:** 1.0  
**Date:** July 20, 2025  
**Type:** Quality Guidelines  
**Target:** Content Creators | LinkedIn Publishers  
**Purpose:** Essential rules for high-quality LinkedIn posts

---

## 🎯 Core Requirements

**Word Count Rules:**
- Maximum 400 words between rulers (`---`)
- Optimal range: 350-400 words
- Content between first and last ruler only

**Structure Standards:**
- Single markdown code block maximum
- Clear problem → solution → action flow
- Professional tone with specific data
- Academic references when applicable

## 📝 Validation Process

**Pre-Publication Checklist:**
```
✅ Word count ≤ 400 (use python3 check_post.py "filename.md")
✅ Content between rulers only
✅ Single code block maximum  
✅ Engaging hook in first 50 words
✅ Specific data and percentages included
✅ Clear call to action present
✅ Academic reference cited
```

**Technical Validation:**
- Run `python3 linkedin_word_counter.py "post.md" --verbose`
- Check markdown formatting compliance
- Verify all required elements present

## 🚨 Common Mistakes to Avoid

**Word Count Violations:**
- Including metadata in count
- Multiple code blocks
- Exceeding 400-word limit
- Verbose explanations without value

**Structure Issues:**
- Missing ruler markers
- Content outside rulers  
- Poor readability (long paragraphs)
- Weak or missing call to action

## 📊 Success Metrics

**Quality Indicators:**
- Passes automated validation
- High engagement within 2 hours
- Meaningful comments and discussions
- Professional credibility maintained
- Actionable value provided immediately

**Tools Available:**
- `linkedin_word_counter.py` - Full analysis
- `check_post.py` - Quick validation  
- Quality guidelines reference document

---

**Remember:** Every post should provide immediate, actionable value while maintaining professional credibility and staying within the 400-word limit.
