# TIL: Capturing and Reusing Illustration Style for Variants

## How to Extract and Reapply Illustration Style for Generative Art

When you want to generate new images that match the style of a real illustration, it's crucial to capture the style in a structured, detailed way. This allows you to create variants—such as changing the subject—while preserving the original's artistic feel.

### Step 1: Use a Detailed Style Extraction Prompt

Use the following prompt to analyze your reference illustration:

> "Please analyze the following image as an illustration and describe it in extreme detail, focusing on its artistic medium, style, technique, narrative elements, and visual characteristics. The goal is to capture enough information that one could potentially recreate a similar illustration based solely on this description. Provide the description in a JSON format.
>
> The JSON object should have the following keys:
> - `illustration_title`
> - `overall_illustration_summary`
> - `artistic_medium_and_technique` (with `primary_medium`, `specific_techniques`, `tool_feel`)
> - `illustration_style`
> - `mood_and_atmosphere`
> - `narrative_elements` (with `implied_story`, `character_interaction`, `symbolism_or_metaphor`, `intended_message`)
> - `subject_details` (array of objects: `name`, `design_description`, `pose_and_action`, `expression_or_state`, `position_in_frame`, `color_palette_specific_to_subject`)
> - `setting_details` (with `location_type`, `time_of_day_or_era`, `environmental_conditions`, `specific_elements`)
> - `composition_and_framing` (with `camera_angle`, `shot_type`, `perspective_rendering`, `depth_of_field_rendering`, `leading_lines_design`, `rule_of_thirds_placement_design`, `balance_and_symmetry`, `negative_space_usage`)
> - `lighting_details_illustration` (with `light_source_rendering`, `light_direction_rendering`, `light_quality_rendering`, `light_color_temperature_rendering`, `shadow_rendering`)
> - `color_palette_illustration` (with `dominant_colors_list`, `color_harmony_scheme`, `saturation_level_illustration`, `color_application_style`)
> - `line_work_details` (with `line_quality`, `line_color`, `line_purpose`)
> - `texture_and_materials_rendering`
> - `special_effects_and_filters_illustration`
> - `keywords`

### Step 2: Example Output

Here is an example JSON for a digital illustration:

```json
{
  "illustration_title": "The Curious Fox and the Whispering Woods",
  "overall_illustration_summary": "A whimsical digital illustration depicting a stylized red fox cautiously exploring a magical, glowing forest at twilight. The style is reminiscent of modern children's book art, with soft lighting and a sense of wonder and gentle mystery.",
  "artistic_medium_and_technique": {
    "primary_medium": "Digital Painting",
    "specific_techniques": "Soft blending, cel-shaded characters with subtle gradients, glowing effects, textured brushes for foliage.",
    "tool_feel": "Brush-like, with a smooth, painterly finish."
  },
  "illustration_style": "Children's Book Illustration, Whimsical, Stylized Animal Art",
  "mood_and_atmosphere": "Curious, magical, peaceful, slightly mysterious, enchanting, innocent.",
  "narrative_elements": {
    "implied_story": "A small, curious fox is discovering a hidden, enchanted part of the forest, perhaps for the first time.",
    "character_interaction": "The fox is the sole active character, interacting with its environment through exploration.",
    "symbolism_or_metaphor": "The glowing elements symbolize magic or hidden wonders; the fox represents curiosity and innocence.",
    "intended_message": "To evoke a sense of wonder, discovery, and the magic of nature."
  },
  "subject_details": [
    {
      "name": "Red Fox",
      "design_description": "Stylized, slightly oversized head, large expressive eyes, fluffy tail. Fur is a vibrant orange-red with white accents on belly and tail tip. Lean, agile body.",
      "pose_and_action": "Lowered head, nose to the ground, one paw slightly raised, as if sniffing or listening intently.",
      "expression_or_state": "Curious and cautious, eyes wide with wonder.",
      "position_in_frame": "Center foreground, slightly to the right, drawing the eye immediately.",
      "color_palette_specific_to_subject": ["vibrant orange-red", "white", "dark brown (eyes)"]
    }
  ],
  "setting_details": {
    "location_type": "Enchanted Forest",
    "time_of_day_or_era": "Twilight/Dusk, with an eternal magical glow.",
    "environmental_conditions": "Still, calm air, with a soft, magical luminescence emanating from plants.",
    "specific_elements": "Tall, slender trees with glowing leaves (various shades of green, blue, purple). Luminescent mushrooms and flowers on the forest floor. Soft, ethereal mist weaving through the trees."
  },
  "composition_and_framing": {
    "camera_angle": "Slightly low angle, looking up at the fox and the magical forest, enhancing the sense of wonder.",
    "shot_type": "Medium shot, capturing the fox and a good portion of its immediate magical surroundings.",
    "perspective_rendering": "Soft atmospheric perspective, with background trees becoming less defined and more ethereal.",
    "depth_of_field_rendering": "Fox is in sharp focus, while the immediate foreground (blades of grass) and background trees have a gentle, artistic blur.",
    "leading_lines_design": "Subtle leading lines formed by the path of glowing mushrooms and the curves of tree trunks, guiding the eye towards the fox.",
    "rule_of_thirds_placement_design": "The fox's head is positioned near a lower-right intersection point, while a prominent glowing tree is on the left vertical third.",
    "balance_and_symmetry": "Asymmetrical, with the fox as the primary focal point balanced by the glowing elements and trees.",
    "negative_space_usage": "The soft, misty background acts as negative space, allowing the fox and glowing elements to stand out."
  },
  "lighting_details_illustration": {
    "light_source_rendering": "Multiple internal light sources from glowing flora and a soft, ambient magical light from above.",
    "light_direction_rendering": "Omnidirectional from glowing elements, with soft top-down ambient light.",
    "light_quality_rendering": "Soft, diffused, ethereal, and magical.",
    "light_color_temperature_rendering": "Cool blues and purples from glowing elements, mixed with warm, subtle greens and yellows from ambient light.",
    "shadow_rendering": "Soft, subtle shadows, mostly created by the glow of the magical plants, adding depth without harshness."
  },
  "color_palette_illustration": {
    "dominant_colors_list": ["vibrant orange-red (fox)", "deep forest greens", "luminous blues", "soft purples", "subtle yellows"],
    "color_harmony_scheme": "Analogous (greens, blues, purples) with a complementary pop (orange-red fox) and accent colors.",
    "saturation_level_illustration": "Moderately saturated for the fox and glowing elements, slightly desaturated for background foliage.",
    "color_application_style": "Smooth digital gradients for blending, flat colors for base shapes with subtle shading."
  },
  "line_work_details": {
    "line_quality": "Clean, precise lines for character outlines, softer, implied lines for background elements.",
    "line_color": "Darker shades of the fill color for outlines, not pure black.",
    "line_purpose": "Defining character shapes, separating elements, and adding a subtle sense of form."
  },
  "texture_and_materials_rendering": "Soft, slightly textured fur on the fox (rendered with subtle brush strokes); smooth, glowing surfaces for magical plants; soft, blended textures for mist and background foliage.",
  "special_effects_and_filters_illustration": "Prominent glow effects on magical elements, subtle atmospheric haze, soft light bloom around light sources.",
  "keywords": ["illustration", "fox", "forest", "magic", "fantasy", "whimsical", "children's book", "digital art", "animal", "glowing", "enchanted", "nature", "cute"]
}
```

### Step 3: Generate a Variant by Changing the Subject

To create a new image with the same style, modify only the `subject_details` (and related narrative fields if needed). For example, change the fox to a "robot owl" but keep all style, composition, and color details the same. This ensures the new image matches the original's look and feel.

---

**Summary:**
- Use a detailed prompt to extract style as structured JSON.
- Keep all style/composition fields the same for variants.
- Change only the subject and narrative to generate new images in the same style.

---

*Today I Learned: How to capture and reuse illustration style for generative art variants.*
