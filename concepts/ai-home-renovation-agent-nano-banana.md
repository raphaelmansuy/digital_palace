
# AI Home Renovation Planner Agent (Nano Banana)

**Source:** [Build an AI Home Renovation Planner Agent using Nano Banana](https://www.theunwindai.com/p/build-an-ai-home-renovation-planner-agent-using-nano-banana)

**Authors:** [Shubham Saboo](https://www.theunwindai.com/authors/6d38748c-8860-4670-b547-9204c5a5afdb), [Gargi Gupta](https://www.theunwindai.com/authors/9f437733-2dfa-4cc0-bccf-09166ca8f60b)

---

## Overview

A hands-on tutorial for building a fully local, production-ready multi-agent home renovation planner using Google ADK and Gemini 2.5 Flash Image (Nano Banana). The system analyzes room photos, understands style preferences, generates photorealistic renovation renderings, and provides budget/timeline recommendations—all orchestrated by a multi-agent pipeline.

## Key Features

- **Smart Image Analysis:** Upload room and inspiration photos for automatic analysis using Gemini's vision capabilities.
- **Photorealistic Rendering:** Generate high-quality images of renovated spaces with Nano Banana.
- **Budget-Aware Planning:** Get recommendations that respect your financial constraints.
- **Complete Roadmap:** Timeline estimation, budget breakdown, contractor lists, and actionable checklists.
- **Iterative Refinement:** Edit generated renderings with natural language instructions.
- **Multi-Agent Orchestration:** Demonstrates Coordinator/Dispatcher and Sequential Pipeline patterns.
- **Versioned Artifacts:** Automatic version tracking for all generated renderings.

## How It Works

1. **User uploads photos or describes needs.**
2. **Coordinator agent** routes requests to specialist agents (visual assessment, design planning, project coordination).
3. **VisualAssessor** analyzes images and provides detailed assessment.
4. **DesignPlanner** creates actionable design recommendations.
5. **ProjectCoordinator** generates renderings, budget, and timeline.
6. **RenderingEditor** allows iterative edits to generated images.

## Tech Stack & Prerequisites

- Python 3.10+
- Google ADK (Agent Development Kit)
- Gemini 2.5 Flash Image (Nano Banana)
- [Gemini API key](https://aistudio.google.com/api-keys?utm_source=www.theunwindai.com&utm_medium=referral&utm_campaign=build-an-ai-home-renovation-planner-agent-using-nano-banana)
- Streamlit for UI

## Code & Setup

- **GitHub Repo:** [awesome-llm-apps/ai_home_renovation_agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent)
- Install dependencies: `pip install -r requirements.txt`
- Start app: `adk web` in the project directory
- Example prompts and usage provided in the tutorial

## Why It Matters

This project is a practical demonstration of:

- Real-world agentic design patterns (Coordinator/Dispatcher, Sequential Pipeline)
- Local, privacy-preserving AI applications
- Advanced multimodal capabilities (vision + language)
- Extensible architecture for home, interior, or other planning agents

## Further Reading & Related Links

- [Awesome LLM Apps (GitHub)](https://github.com/Shubhamsaboo/awesome-llm-apps)
- [Unwind AI](https://www.theunwindai.com/)

---

*For more agentic AI tutorials, visit [Unwind AI](https://www.theunwindai.com/).*
