---

# People Page Frontmatter Format

This document describes the recommended YAML frontmatter and section structure for all files in the `people/` directory. Use this as a reference when creating or updating a person profile.

---

## 0. YAML Frontmatter Block (Required)

Each person profile should begin with a YAML frontmatter block, enclosed by triple dashes (`---`). This block provides structured metadata for the person and is used for indexing, search, and automation.

**Example:**

```yaml
---
name: "[Full Name]"
slug: "[url-friendly-slug]"
photo_url: "[https://link-to-photo.jpg]"
birth_year: [YYYY]
nationality: "[Country or Countries]"
current_role:
  title: "[Current Title/Role]"
  organization: "[Current Company/Institution]"
  location: "[City, Country]"
  start_date: "[YYYY or YYYY-MM]"
links:
  website: "[https://website]"
  twitter: "[https://twitter]"
  github: "[https://github]"
  linkedin: "[https://linkedin]"
  scholar: "[https://scholar]"
expertise_areas:
  - "[Area 1]"
  - "[Area 2]"
categories:
  - "[researcher|educator|entrepreneur|etc]"
last_updated: "[YYYY-MM-DD]"
priority: "[high|medium|low]"
status: "[active|inactive|retired]"
---
```

**Recommended fields:**
- `name`, `slug`, `photo_url`, `birth_year`, `nationality`, `current_role` (with subfields), `links` (with subfields), `expertise_areas`, `categories`, `last_updated`, `priority`, `status`
- Add or remove fields as needed for your use case.

---

### 1. Title & Photo
- `# [Person Name]`
- `![Profile Photo](link_to_photo_or_placeholder)`

### 2. Current Role
- **Position**: [Current Title/Role]
- **Organization**: [Current Company/Institution]
- **Location**: [City, Country]
- **Previous**: [Previous notable positions]
- **Additional Roles**: [Other relevant roles]

### 3. Biography
- 2-3 paragraph summary: background, education, career, achievements, current focus

### 4. Key Contributions
- Bulleted list of major achievements and impact

### 5. Notable Publications/Work
- List of books, papers, patents, software, courses, etc.

### 6. Social Media & Links
- Website, Twitter/X, LinkedIn, GitHub, Google Scholar, YouTube, etc.

### 7. Notable Quotes
- Up to 3 impactful or characteristic quotes

### 8. Areas of Expertise
- List of primary and secondary expertise areas

### 9. Recent News/Updates
- Dated list of recent achievements, announcements, ongoing projects

### 10. Notable Collaborations
- List of collaborators, institutions, and nature of collaboration

### 11. Awards & Recognition
- List of awards, honors, recognitions

### 12. Academic/Professional Background
- Education, advisors, thesis, early career, career progression

### 13. Special Sections (as applicable)
- Companies & Investments (for entrepreneurs/investors)
- Educational Impact (for educators)
- Research Philosophy (for researchers)
- Global Impact (for leaders)

---

### Footer
- Last updated: [Date]
- Next review: [Date]
- **Tags**: #[tag1] #[tag2] #[tag3] #[area] #[location] #[role-type]

---

#### Template Instructions
1. Replace all bracketed placeholders with actual information
2. Remove unused sections
3. Add relevant tags
4. Include high-quality photo with attribution
5. Verify all links
6. Set review date
7. Use consistent formatting

#### Photo Guidelines
- Use official or open-licensed photos, ~256px width, alt text, credit source

#### Tag Guidelines
- Use role, area, location, and affiliation tags (e.g. #founder, #ai-safety, #stanford)

#### Update Schedule
- Monthly: News/updates
- Quarterly: Link check
- Annually: Full review
