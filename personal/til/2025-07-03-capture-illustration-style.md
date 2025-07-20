# TIL: Capture and Reuse Illustration Style for Generative Art Variants (2025-07-03)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Extract and reuse illustration style for consistent generative art** – Use structured prompts and JSON to capture style, then generate new variants by changing only the subject.

---

## The Pain Point

Generating art variants that match the style of a real illustration is difficult without a structured approach. Most models lose consistency when the subject changes.

---

## Step-by-Step Guide

### 1. Use a Detailed Style Extraction Prompt

Analyze your reference illustration with a prompt that requests extreme detail and outputs a structured JSON. Example:

```text
"Please analyze the following image as an illustration and describe it in extreme detail, focusing on its artistic medium, style, technique, narrative elements, and visual characteristics. The goal is to capture enough information that one could potentially recreate a similar illustration based solely on this description. Provide the description in a JSON format."
```

Include keys for title, summary, medium, style, mood, narrative, subject, setting, composition, lighting, color palette, line work, texture, effects, and keywords.

### 2. Example Output

```json
{
  "illustration_title": "The Curious Fox and the Whispering Woods",
  "overall_illustration_summary": "A whimsical digital illustration depicting a stylized red fox cautiously exploring a magical, glowing forest at twilight. The style is reminiscent of modern children's book art, with soft lighting and a sense of wonder and gentle mystery.",
  ...
}
```

### 3. Generate a Variant by Changing the Subject

Modify only the `subject_details` (and related narrative fields if needed). For example, change the fox to a "robot owl" but keep all style, composition, and color details the same. This ensures the new image matches the original's look and feel.

---

## Troubleshooting

- If the style is not preserved, check that all style/composition fields remain unchanged except for the subject.
- Keep the JSON under 400 tokens for best results with most models.

---

## Security Considerations

- Do not include copyrighted or sensitive reference images in prompts or outputs.
- Avoid sharing style JSONs that contain proprietary or private visual information.
- Audit generated images for compliance with platform and copyright rules.

---

## Related Resources

- [Prompt Engineering for Art](https://www.promptingguide.ai/)
- [Generative Art Consistency](https://aiartists.org/generative-art)

---

*⚡ Pro tip: Use structured JSON prompts to lock in style and composition for consistent generative art variants!*
