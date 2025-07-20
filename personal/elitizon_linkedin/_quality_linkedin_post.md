# LinkedIn Post Quality Guidelines

**Version:** 1.0  
**Last Updated:** July 20, 2025  
**Purpose:** Ensure consistent quality and compliance for LinkedIn content

---

## 📏 Character Count Requirements

### Primary Rule: 1800 Characters Maximum

- **Hard Limit:** 1800 characters between the ruler markers (`---`)
- **Optimal Range:** 1500-1800 characters for maximum engagement
- **Minimum Viable:** 1200 characters to provide sufficient value

### Content Measurement Rules

- Count only content between the **first** and **last** ruler (`---`)
- Exclude metadata, headers, and footer content
- Markdown formatting is automatically excluded from count
- Quoted text examples don't count toward character limit
- Link text counts, but URLs don't

‼️ **CRITICAL REQUIREMENT:** The content between rulers MUST start with the post title as a `## [Title]` header (WITHOUT 👉 emoji). This title is counted as part of the character count.

---

## 📝 Content Structure Requirements

### Required Elements
1. **Header Section** (Above first ruler)
   - Title with clear value proposition
   - Date, type, target audience
   - Business impact statement
   - Academic reference (when applicable)

2. **Main Content** (Between rulers)
   - Problem statement
   - Solution overview
   - Practical examples
   - Actionable insights
   - Call to action

3. **Footer Section** (Below last ruler)
   - Series continuation
   - Context about content series

### Formatting Standards

#### Quoted Text Examples

- **Maximum:** 1 quoted text example per post
- **Purpose:** Show before/after examples or practical implementations
- **Format:** Use blockquotes (>) for examples
- **Content:** Keep examples concise and relevant

#### Headers and Structure

- Use `## 👉` for main sections with emoji prefix
- **MANDATORY:** Content between rulers MUST start with post title as `## [Title]` (WITHOUT 👉 emoji)
- Use `### 👉` for subsections
- Use `**bold**` for emphasis, not headers
- Maintain consistent hierarchy
- All level 2 headers (##) must include 👉 emoji EXCEPT the opening title
- Format: `## 👉 Section Title`

#### Lists and Bullets

- Surround lists with blank lines
- Use `-` for unordered lists
- Keep bullet points concise
- Limit to 5-7 items per list


- Don't use codeblocks or inline code in main content
- Avoid excessive formatting that distracts from content 
- Use simple, clear language

---

## 🎯 Content Quality Standards

### Engagement Optimization

- **Hook:** Start with compelling problem statement
- **Value:** Provide actionable insights within first 100 words
- **Specificity:** Use concrete numbers and percentages
- **Social Proof:** Include research citations and data

### Professional Standards

- **Tone:** Professional yet approachable
- **Expertise:** Position as industry expert
- **Credibility:** Reference academic sources
- **Actionability:** Every post must include practical steps

### Readability Requirements

- **Paragraphs:** Maximum 3 sentences each
- **Sections:** Break content into digestible chunks
- **Flow:** Logical progression from problem to solution
- **Clarity:** Avoid jargon, explain technical terms

---

## 🔧 Technical Validation

### Character Count Verification

```bash
# Quick check
python3 check_post.py "personal/elitizon_linkedin/[post_name].md"

# Detailed analysis
python3 linkedin_character_counter.py "personal/elitizon_linkedin/[post_name].md" --verbose
```

### Pre-Publication Checklist

- [ ] Character count ≤ 1800 characters
- [ ] Content between rulers only
- [ ] Single quoted example maximum
- [ ] All required elements present
- [ ] No markdown linting errors
- [ ] Engaging hook in first paragraph
- [ ] Clear call to action
- [ ] Academic reference included
- [ ] Series context provided

---

## 📊 Quality Metrics

### Engagement Targets

- **Character Count:** 1500-1800 characters (optimal range)
- **Reading Time:** 45-60 seconds
- **Paragraph Length:** 2-3 sentences maximum
- **Quoted Examples:** 1 per post maximum
- **Call to Action:** 1 clear, specific action

### Content Effectiveness

- **Problem Clarity:** Issue identified within first 100 characters
- **Solution Specificity:** Concrete steps provided
- **Value Density:** High insight-to-character ratio
- **Actionability:** Immediate implementable advice
- **Credibility:** Research-backed claims

---

## 🚨 Common Violations

### Character Count Issues

- ❌ Exceeding 1800-character limit
- ❌ Counting metadata in character count
- ❌ Including multiple quoted examples
- ❌ Verbose explanations without value

### Structure Problems

- ❌ Missing ruler markers
- ❌ Content outside rulers
- ❌ Inconsistent header hierarchy
- ❌ Lists without blank lines

### Content Quality Issues

- ❌ Vague problem statements
- ❌ Generic advice without specifics
- ❌ Missing call to action
- ❌ No research backing
- ❌ Poor readability

---

## 🔄 Review Process

### Self-Review Steps

1. **Content Check:** Verify all required elements
2. **Word Count:** Run validation tools
3. **Readability:** Read aloud for flow
4. **Value Test:** Can reader implement immediately?
5. **Engagement:** Compelling hook and CTA?

### Final Validation

```bash
# Run comprehensive check
python3 linkedin_character_counter.py "path/to/post.md" --verbose

# Verify structure and formatting
# Check for markdown linting errors
# Confirm all guidelines met
```

---

## 📈 Success Indicators

### Post Performance

- High engagement in first 2 hours
- Comments asking follow-up questions
- Shares by industry professionals
- Profile visits from post viewers

### Content Quality

- ✅ Passes all technical validations
- ✅ Provides immediate actionable value
- ✅ Maintains professional credibility
- ✅ Advances series narrative
- ✅ Encourages meaningful discussion

---

## 🔧 Tools and Resources

### Validation Tools

- `linkedin_character_counter.py` - Comprehensive analysis
- `check_post.py` - Quick validation
- Markdown linters for formatting

### Reference Materials

- "The Prompt Report" academic survey
- LinkedIn engagement best practices
- Professional writing standards
- Series content planning

### Workflow Integration

- Pre-commit validation hooks
- VS Code task integration
- Automated quality checks
- Performance tracking systems
