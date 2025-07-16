# Notes on Context Engineering with Walden Yan

These are notes from a discussion with Walden Yan on the challenges and principles of context engineering for AI agent systems.

1. **The telephone game kills agent systems**: When multiple agents pass information between each other, crucial context gets lost in translation, leading to misaligned outputs and conflicting decisions.

2. **Context is king, not prompts**: Models are already smart. What limits them now isn't clever prompting but how much context they have about your task and their previous actions.

3. **We're in the HTML era of agent design**: Current frameworks are premature because we're still discovering the fundamental principles of building reliable agent systems, similar to web development before React.

4. **Implicit decisions create conflicts**: When multiple agents work in parallel, they make countless implicit decisions (from coding style to API choices) that inevitably clash when combined.

5. **Linear agents beat parallel ones**: The most reliable system is often a single agent working through tasks sequentially, maintaining full awareness of everything that's happened before.

6. **Read-only sub-agents reduce risk**: If you must use multiple agents, constrain them to information gathering rather than decision-making to minimize conflicts.

7. **Context compression is necessary but dangerous**: As tasks grow, you'll hit token limits and need to compress context, but this introduces new failure points if important details get lost.

8. **Good systems feel like one consciousness**: Even with complex underlying components, a well-engineered agent should present itself to users as a single, coherent entity with continuous decision-making.

9. **Confidence and escalation are critical skills**: The best agents know when to say "I don't know" and when to escalate decisions to humans rather than guessing incorrectly.

10. **Universal tools beat specialized ones**: Give your agent powerful general-purpose tools like shell access rather than narrow integrations. A bash command with an API key can do almost anything.

> Source: improvingrag.com
