# People File Frontmatter Format

All people profiles must begin with a YAML frontmatter block using the following structure:

```yaml
---
name: "Full Name"
slug: "unique-slug"
photo_url: "https://..."
birth_year: 1980
nationality: "Country or Countries"
current_role:
  title: "Current Title or Position"
  organization: "Current Organization"
  location: "Location (City, Country or Remote)"
  start_date: "YYYY" # or null if unknown
links:
  website: "https://..." # Official or org website
  twitter: "https://..." # Twitter/X profile
  github: "https://..." # GitHub profile (optional)
  linkedin: "https://..." # LinkedIn profile (optional)
  scholar: "https://..." # Google Scholar (optional)
  personal: "https://..." # Personal website (optional)
expertise_areas:
  - "Area 1"
  - "Area 2"
categories:
  - "researcher" # e.g., researcher, educator, entrepreneur
  - "educator"
last_updated: "YYYY-MM-DD"
priority: "high" # or "medium", "low"
status: "active" # or "inactive"
---
```

**Rules:**

- The YAML frontmatter must be at the very top of the page.
- The frontmatter block must start with `---` (three dashes).
- The frontmatter block must be finished by a line with only `---` (three dashes).

VERY IMPORTANT: Ensure that the frontmatter is valid YAML. Use a YAML validator if necessary.
FRONT MATTER MUST NOT INCLUDE ANY EXTRA WHITESPACE OR INDENTATION.
FRONT MATTER MUST BE AT THE TOP OF THE FILE, IMMEDIATELY FOLLOWING THE `---` START AND END MARKERS.

**Notes:**

- All string values must be quoted with double quotes.
- List values must be quoted and use YAML list syntax.
- The `links` section may include empty strings for missing links, but all keys should be present for consistency.
- The `current_role.start_date` can be a year as a string (e.g., "2021") or null if unknown.
- Add or update fields as needed for new requirements, but keep the structure consistent across all people files.
