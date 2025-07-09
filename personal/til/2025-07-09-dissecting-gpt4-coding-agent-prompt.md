# TIL: Dissecting the GPT-4.1 Coding Agent System Prompt (2025-07-09)

Today I learned how Burke Holland's GPT-4.1 Coding Agent System Prompt is structured and why each component is essential for creating effective AI coding assistants.

## Source Analysis

**Original Gist**: [GPT-4.1 Coding Agent System Prompt (VS Code Tools Edition)](https://gist.github.com/burkeholland/7aa408554550e36d4e951a1ead2bc3ac)  
**Author**: Burke Holland  
**Purpose**: Production-grade system prompt for VS Code coding agents  
**Key Innovation**: Systematic workflow with todo list management and explicit tool usage guidelines

## Prompt Architecture Breakdown

### 1. Core Agent Identity & Persistence

```markdown
You are an agent - please keep going until the user's query is completely 
resolved, before ending your turn and yielding back to the user.
```

**Why This Matters**:
- ✅ **Prevents premature termination** - Agent continues until task completion
- ✅ **Sets expectation** - User knows agent will be thorough
- ✅ **Reduces back-and-forth** - Minimizes need for follow-ups

**Prompt Engineering Insight**: The opening line establishes the agent's fundamental behavior pattern. Without this, agents often stop mid-task.

### 2. Motivation & Performance Incentive

```markdown
Your goal is to complete the entire user request as quickly as possible. 
You will receive a bonus depending on how fast you can complete the entire task.
```

**Psychological Triggers**:
- 🎯 **Goal-oriented behavior** - Clear completion target
- ⚡ **Speed incentive** - Encourages efficiency
- 🏆 **Performance motivation** - Bonus system drives quality

**Why It Works**: LLMs respond well to explicit goal structures and performance incentives, even though they're simulated.

### 3. Systematic Workflow Steps

```markdown
1. Always search the codebase to understand the context
2. Think deeply about the user's request
3. Identify the steps needed to complete the task
4. Create a Todo List with the steps identified
5. Use the appropriate tools to complete each step
6. After fully completing a step, update the Todo List
7. Ensure all steps are fully completed
8. Check for problems using the #problems tool
9. Return control only after completion
```

**Engineering Excellence**:
- 📋 **Structured approach** - Prevents chaotic execution
- 🔍 **Context-first strategy** - Always understand before acting
- ✅ **Progress tracking** - Todo lists maintain state
- 🐛 **Quality gates** - Problem checking before completion

**Real-World Impact**: This workflow mirrors professional software development practices.

### 4. Todo List Management System

```markdown
## Todo List Guidelines

You MUST manage your progress using a Todo List.

Todo Lists must use standard checklist syntax and be wrapped in a markdown 
code block with tripple backticks.

Never use HTML or any other format for the todo list. Always use Markdown 
checklist syntax.

Only re-render the todo list after you completed and item and checked it 
off the list.

### Todo List Legend
• `[ ]` = Not started
• `[x]` = Completed  
• `[-]` = Removed or no longer relevant
```

**Strategic Design**:
- 📝 **Standardized format** - Consistent, parseable output
- 🔄 **State management** - Tracks progress across interactions
- 🚫 **Format constraints** - Prevents HTML rendering issues
- 📊 **Clear legend** - Eliminates ambiguity

**Implementation Genius**: The todo list acts as both a planning tool and a progress tracker, essential for complex multi-step tasks.

### 5. Tool Usage Guidelines

#### Fetch Tool Rules
```markdown
You MUST use the `fetch_webpage` tool when the user provides a URL. 
Follow these steps exactly:
1. Use the `fetch_webpage` tool to retrieve content
2. Review the content returned
3. If you find additional relevant URLs, fetch those too
4. Repeat until you have all necessary context

IMPORTANT: Recursively fetching links is crucial.
```

**Deep Context Strategy**:
- 🔗 **Recursive fetching** - Ensures comprehensive understanding
- 📖 **Content review** - Always analyze what was retrieved
- 🌐 **Link following** - Discovers additional context
- ⚠️ **Mandatory compliance** - "MUST" language enforces behavior

#### Read File Guidelines
```markdown
1. Before you read a file, MUST inform the user and explain why
2. Always read the entire file (up to 2000 lines)
3. Unless file has changed, MUST not read same lines more than once

IMPORTANT: Read the entire file. Failure to do so will result in a bad 
rating for you.
```

**Efficiency & Transparency**:
- 💬 **User communication** - Explains actions before taking them
- 📄 **Complete reading** - Avoids partial context issues
- 🔄 **Caching behavior** - Prevents redundant operations
- ⚠️ **Consequence framing** - "Bad rating" motivates compliance

#### GREP Search Protocol
```markdown
1. Before calling `grep_search`, MUST inform user and explain why
```

**Communication Pattern**:
- 🗣️ **Transparency requirement** - User always knows what's happening
- 🎯 **Purpose explanation** - Context for every action
- 🤝 **Trust building** - Predictable, communicative behavior

### 6. Communication Style Guidelines

```markdown
1. Always include a single sentence acknowledging the user's request
2. Always tell the user what you are about to do before you do it
3. Always explain why you are searching or reading a file
4. Do not use code blocks for explanations or comments
5. The user does not need to see your plan or reasoning
```

**UX Design Principles**:
- ✅ **Acknowledgment** - User feels heard
- 📢 **Proactive communication** - No surprises
- 🎯 **Purposeful actions** - Every action has stated reason
- 📝 **Clean output** - No unnecessary code blocks
- 🎭 **Behind-the-scenes planning** - Internal reasoning stays internal

### 7. Quality Assurance & Completion Criteria

```markdown
## Important Notes
1. Always use the #problems tool before returning control
2. Before using a tool, check if recent output satisfies the task
3. Avoid re-reading files, re-searching, or re-fetching URLs
4. Reuse previous context unless something has changed
5. If redoing work, explain briefly why it's necessary

IMPORTANT: Do not return control until you have fully completed the 
user's entire request. All items in your todo list MUST be checked off.
```

**Production-Ready Standards**:
- 🔍 **Pre-completion checks** - Quality gates before finishing
- 🚀 **Efficiency optimization** - Avoid redundant operations
- 🧠 **Context reuse** - Smart caching behavior
- 📋 **Completion verification** - Todo list must be 100% complete

## Prompt Engineering Insights

### What Makes This Prompt Exceptional

1. **Behavioral Conditioning**: Uses psychological triggers (bonuses, ratings) to shape AI behavior
2. **Systematic Workflow**: Enforces professional development practices
3. **Communication Protocol**: Builds trust through transparency
4. **State Management**: Todo lists provide continuity across interactions
5. **Quality Gates**: Multiple checkpoints ensure thoroughness
6. **Tool Discipline**: Specific rules prevent tool misuse

### Advanced Techniques Used

#### Constraint-Based Design
- **Format constraints** (Markdown only for todos)
- **Behavioral constraints** (MUST inform user)
- **Quality constraints** (check problems before completion)

#### Escalating Language
- "You MUST" - Highest priority
- "Always" - Consistent behavior
- "IMPORTANT" - Critical instructions
- "Failure to do so will result in bad rating" - Consequence framing

#### Workflow State Machine
```
Start → Search Codebase → Create Todo → Execute Steps → Update Todo → Check Problems → Complete
```

Each step has specific rules and transition criteria.

## Real-World Applications

### Perfect For
- ✅ **Complex refactoring tasks** - Multi-file changes with dependencies
- ✅ **Feature implementation** - End-to-end development workflows
- ✅ **Debugging sessions** - Systematic investigation and fixes
- ✅ **Code reviews** - Thorough analysis with actionable feedback

### Adaptable Patterns
- 🔄 **Todo list management** - Any multi-step process
- 🗣️ **Communication protocol** - Building user trust
- 🛠️ **Tool usage discipline** - Preventing AI tool abuse
- ✅ **Quality gates** - Ensuring thorough completion

## Key Takeaways for Prompt Engineering

### 1. Structure Over Intelligence
Well-structured workflows beat pure intelligence. The prompt creates a reliable system rather than depending on AI creativity.

### 2. Communication is UX
The extensive communication guidelines create a professional user experience that builds trust and reduces anxiety.

### 3. State Management Matters
Todo lists provide continuity that prevents the AI from losing track of complex, multi-step tasks.

### 4. Constraints Enable Freedom
By constraining format and behavior, the prompt allows the AI to focus on problem-solving rather than figuring out how to communicate.

### 5. Quality Gates Prevent Problems
Multiple checkpoints (problems tool, completion verification) catch issues before they reach the user.

## 🔗 Related Resources

- [GPT-4.1 Coding Agent System Prompt (Burke Holland)](https://gist.github.com/burkeholland/7aa408554550e36d4e951a1ead2bc3ac) - Original source
- [How to Configure Chat Mode in VSCode](2025-07-09-vscode-chat-mode-configuration.md) - Implementation guide
- [Prompt Engineering](../../concepts/prompt-engineering.md) - Core prompting concepts
- [AI Agents Guide](../../guides/ai-agents.md) - Building autonomous systems

## Quick Reference: Prompt Components

```markdown
1. Agent Identity & Persistence ("You are an agent...")
2. Motivation & Incentives ("You will receive a bonus...")
3. Systematic Workflow (9 explicit steps)
4. Todo List Management (Format, legend, update rules)
5. Tool Usage Guidelines (Fetch, read, grep protocols)
6. Communication Style (5 explicit rules)
7. Quality Assurance (Completion criteria)
```

*This TIL demonstrates how professional-grade AI agents require structured prompts that combine behavioral psychology, software engineering practices, and clear communication protocols.*

## Community Insights & Evolution

### Recent Updates & Improvements

**Note**: Burke Holland has since released an improved **v2 "Beast Mode"** version available at: [Beast Mode Gist](https://gist.github.com/burkeholland/a232b706994aa2f4b2ddd3d97b11f9a7)

### Community-Driven Enhancements

#### 1. HTML Prevention Fix (ChrisTorng)

**Problem**: The AI sometimes generated HTML checkboxes instead of Markdown

```html
<input checked="" disabled="" type="checkbox">
```

**Solution**: Enhanced todo list guidelines

```markdown
**Never use HTML** or any other format for the todo list. Always use Markdown checklist syntax.
```

**Engineering Lesson**: Explicit negative constraints are as important as positive instructions.

#### 2. VSCode Tool Mapping (ChrisTorng & Community)

**Challenge**: The original prompt used generic function names that needed mapping to VSCode Copilot tools.

**Community Solution**:

```yaml
# Original → VSCode Copilot Mapping
functions.fetch_webpage → fetch
functions.read_file → search  
functions.grep_search → search
#problems → problems

# Additional tools suggested:
- codebase (for broader searches)
- editFiles (for file modifications)
- runCommands (for terminal operations)
```

#### 3. Metadata Configuration Optimization

**Successful Configuration**:

```yaml
---
description: 'PlanFirst chat mode to help users with their coding tasks'
tools: ['codebase', 'editFiles', 'fetch', 'problems', 'runCommands', 'search']
---
```

**Key Learning**: Some users found that removing the metadata section entirely resolved tool access issues.

### Performance Configuration Insights

#### Request Limit Optimization

```json
{
  "chat.agent.maxRequests": 500
}
```

**Burke's Recommendation**:
> "Pro tip here as well - bump the max requests in your settings to like 500. 4.1 likes to do a lot of turns calling search/read."

**Why This Matters**:

- GPT-4.1 is thorough but resource-intensive
- Higher request limits prevent mid-task termination
- Essential for complex, multi-file operations

#### Model-Specific Considerations

```yaml
---
description: 'Generate implementation plan for new features'
tools: ['codebase', 'fetch', 'findTestFiles', 'githubRepo', 'search', 'usages']
model: GPT-4.1  # Saves manual model selection
---
```

### Implementation Troubleshooting

#### Common Issues & Solutions

**Problem**: Custom chat mode can't access `editFiles` or `runCommands`

```yaml
# ❌ This may cause tool access issues
tools: ['codebase', 'editFiles', 'fetch', 'problems', 'runCommands', 'search']

# ✅ Try removing metadata entirely
# (Just use the system prompt without the YAML header)
```

**Problem**: Overly verbose todo list rendering

```markdown
# Original behavior: Re-rendered list after every action
# Improved behavior: Only re-render after completing items
```

### Advanced Prompt Engineering Discoveries

#### 1. Recursive Information Gathering

The fetch tool's recursive strategy proved essential:

```markdown
IMPORTANT: Recursively fetching links is crucial. You are not allowed to 
skip this step, as it ensures you have all the necessary context.
```

**Real Impact**: Prevents surface-level analysis that leads to incomplete solutions.

#### 2. Context Efficiency Optimization

```markdown
Unless a file has changed since the last time you read it, you MUST not 
read the same lines in a file more than once.
```

**Economic Consideration**: This rule directly addresses API cost management while maintaining quality.

#### 3. Behavioral Reinforcement Patterns

The prompt uses multiple reinforcement strategies:

- **Positive**: "You will receive a bonus"
- **Negative**: "Failure to do so will result in a bad rating"
- **Authority**: "You MUST", "IMPORTANT"
- **Consequence**: Clear outcomes for compliance/non-compliance

### Cross-Platform Considerations

#### IntelliJ Compatibility

**Question from Community**: "Will this work with IntelliJ too?"

**Current Status**:

- IntelliJ Copilot respects `copilot-instructions.md`
- Tool mapping may differ
- Workflow principles remain applicable

**Adaptation Strategy**: Focus on the workflow and communication patterns rather than specific tool names.

## Lessons from Community Feedback

### 1. **Iterative Improvement Works**

The prompt evolved through community feedback, demonstrating the value of collaborative refinement.

### 2. **Tool Abstraction is Critical**

Generic tool references make prompts more portable across different AI environments.

### 3. **Configuration Flexibility Matters**

Different users found success with different metadata approaches, suggesting flexibility in implementation.

### 4. **Performance Tuning is Essential**

Settings like `maxRequests` are crucial for complex agent workflows.

### 5. **Community Validation Accelerates Development**

93+ stars and active community contributions validate the prompt's effectiveness and drive improvements.
