## About this repository

Digital Palace is a personal knowledge base and engineering handbook for building AI agents, RAG systems, and agent frontends. Content is stored as Markdown under categorized folders (for example `concepts/`, `guides/`, `reference/`, `community/`). The repo includes tools and generated artifacts under `.archive/` and a small Node toolchain (`package.json`) used for tasks like slide generation with Marp.

## What I (the assistant) should know first

- Primary content locations:
  - `concepts/` — canonical concept pages and short explainers
  - `guides/` — longer how-tos and SOPs (agent development, deployment)
  - `reference/` — deep technical articles and curated resources
  - `.archive/` — generated artifacts and presentation drafts
  - `prompts/` and `.github/prompts/` — recorded prompt workflows

- Local dev helpers and tasks are defined in `.vscode/` and the repository `tasks` view (see VS Code tasks such as "Start Chroma MCP Server").
- Slides are authored as Marp markdown in `.archive/pres/` and rendered via the Marp CLI (note: Marp uses a headless browser and can time out on some systems).

## How I should behave as a code assistant

- Prefer small, safe edits: create or update Markdown, small scripts, tests, and documentation. Avoid large refactors unless requested.
- Respect repository style: markdown files use standard heading spacing and single trailing newline. Keep existing link structure and relative paths.
- When adding new concept pages, add a single-line entry to `concepts/README.md` near related topics.
- Run quick validation when possible (spellcheck, markdown linting, or running lightweight Node scripts). Report any lint/type failures and propose fixes.

## Common tasks and where to start

- Add or update a concept page: edit or create `concepts/*.md`. After adding content, update `concepts/README.md` with a one-line index entry.
- Create presentations: put Marp slides under `.archive/pres/`. To export, use the project's Marp CLI (requires Node). If Marp PPTX export fails with a Puppeteer timeout, try increasing timeout, export HTML first, or run the command on a desktop environment with a GUI.
- Working with MCP or Chroma: VS Code tasks exist to start/stop an MCP server and initialize the Chroma DB. Use those tasks or run the commands in the workspace root.

## Useful commands (zsh / macOS)

- Run Marp (example):
  - marp .archive/pres/adk-ag-ui-integration-presentation.md --pptx --theme gaia
  - If timeout occurs, try: marp --debug --html .archive/pres/... then convert or open the HTML in a browser.
- Start Chroma MCP server (via tasks): run the VS Code task "Start Chroma MCP Server" or execute the task command from the workspace tasks.
- Run the project's Node scripts or linters via package.json (see `package.json`).

## Format, PRs and code style

- Keep changes focused and atomic. Edit only the files necessary for the task.
- For Markdown: ensure headings have blank lines above and below lists and subheadings, use relative links within the repo, and keep a single trailing newline at EOF.
- When adding code examples, prefer typed or small runnable snippets and include minimal usage instructions.

## Examples: prompts an AI agent can use in this repo

- "Add a summary section and link to `concepts/ai-engineer-book-resources.md` from `concepts/README.md` about foundation models." — Good: small doc edit and index update.
- "Create a Marp slide from `concepts/adk-ag-ui-integration.md` and save it to `.archive/pres/` as a Marp markdown file." — Good: create presentation; note export may require manual run.
- "Verify external links in `concepts/*.md` and report unreachable URLs." — Good: run link-checker script or propose one if missing.

## Edge cases & constraints

- Large binary or media changes: avoid committing large binaries to the repo; prefer adding references in `.archive/` and storing originals elsewhere.
- Headless browser tasks (Marp/Puppeteer) may fail in CI or headless macOS environments. If rendering fails, document the error and propose alternatives (increase timeout, use --no-sandbox, render HTML then convert).
- Do not run network calls that exfiltrate secrets or require external credentials without explicit user consent.

## Where to leave notes for humans

- When in doubt, create a short PR description that explains intent, commands run, and a short verification checklist (build, lint, smoke-test).

---

If you want, I can open a PR with this file, or adjust tone/length. Mark this task completed when added to the repo.
