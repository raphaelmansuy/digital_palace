# 📋 People Page Format Specification

This document defines the actionable format for a "People" profile page in this repository. Use this template for consistency, clarity, and discoverability.

---

## 1. Frontmatter (YAML)

- Add a YAML block at the top for metadata and searchability.

```yaml
---
name: "Full Name"
slug: "url-friendly-slug"
photo_url: "https://..."
birth_year: 19XX
nationality: "Country"
current_role:
  title: "Role"
  organization: "Org Name"
  location: "City, Country"
  start_date: "YYYY"
links:
  website: "https://..."
  twitter: "https://..."
  github: "https://..."
  linkedin: "https://..."
  scholar: "https://..."
  personal: "https://..."
expertise_areas:
  - "Area 1"
  - "Area 2"
categories:
  - "category1"
  - "category2"
position: "Role"
organization: "Org Name"
tags: [tag1, tag2, ...]
last_updated: "YYYY-MM-DD"
priority: "high|medium|low"
status: "active|inactive"
---
```

---

## 2. Main Content Structure

- The first heading (H1) should be the person's name.

- Use clear section headings (H2 or H3) for each concept

- Recommended sections:

  - Photo
  - Current Role
  - Biography
  - Key Contributions
  - Notable Publications/Work
  - Social Media & Links
  - Notable Quotes
  - Areas of Expertise
  - Recent News/Updates
  - Notable Collaborations
  - Companies & Investments
  - Background
  - Global Impact
  - Tags

---

## 3. Code & Media

- Use fenced code blocks for YAML frontmatter

- Use markdown image syntax for profile photos

```markdown
![Full Name](https://...)
```

---

## 4. Lists & Tips

- Use bullet points for contributions, expertise, collaborations, and companies

- Keep lists concise and focused on practical facts

---

## 5. Footer & Maintenance

- End with last updated and next review dates

```markdown
---
_Last updated: YYYY-MM-DD_  
_Next review: YYYY-MM-DD_
```

---

## 6. Example

See [`sam-altman.md`](./sam-altman.md) for a complete, actionable example.
