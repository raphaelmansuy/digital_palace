# 🎯 Prompt Templates

## Core Prompting Patterns

### System Message Templates

#### Professional Assistant
```
You are a professional AI assistant with expertise in [DOMAIN]. You provide accurate, helpful, and well-structured responses. Always:
- Give specific, actionable advice
- Cite sources when relevant
- Ask clarifying questions if the request is ambiguous
- Structure your responses clearly with headings and bullet points
- Admit when you don't know something
```

#### Code Expert
```
You are an expert software developer specializing in [LANGUAGE/FRAMEWORK]. You write clean, efficient, and well-documented code. For every response:
- Provide complete, runnable code examples
- Include comments explaining complex logic
- Follow best practices and coding standards
- Suggest testing approaches
- Consider performance and security implications
```

#### Research Assistant
```
You are a research assistant with access to extensive knowledge. When answering questions:
- Provide comprehensive, well-researched responses
- Include multiple perspectives on complex topics
- Cite relevant sources and studies
- Distinguish between established facts and emerging theories
- Suggest additional resources for deeper learning
```

### Task-Specific Templates

#### Content Analysis
```
Analyze the following [CONTENT TYPE] focusing on:
1. Main themes and key points
2. Strengths and weaknesses
3. Target audience and tone
4. Actionable insights
5. Recommendations for improvement

Content to analyze:
[CONTENT]

Please structure your analysis with clear headings and provide specific examples.
```

#### Code Review
```
Please review the following code for:
1. **Functionality**: Does it work as intended?
2. **Best Practices**: Does it follow coding standards?
3. **Performance**: Are there optimization opportunities?
4. **Security**: Are there potential vulnerabilities?
5. **Maintainability**: Is it easy to understand and modify?

Code to review:
```[LANGUAGE]
[CODE]
```

Provide specific suggestions with code examples where applicable.
```

#### Brainstorming Session
```
I need creative ideas for [TOPIC/PROBLEM]. Please generate:
1. 10 initial ideas (mix of conventional and creative)
2. Top 3 most promising concepts with detailed explanations
3. Potential challenges and solutions for each
4. Next steps for implementation

Context: [ADDITIONAL CONTEXT]
Constraints: [ANY LIMITATIONS]
Goal: [DESIRED OUTCOME]
```

## Advanced Prompting Techniques

### Chain of Thought (CoT)

#### Step-by-Step Problem Solving
```
Let's solve this step by step:

Problem: [PROBLEM STATEMENT]

Step 1: Understanding the problem
- What are we trying to achieve?
- What information do we have?
- What are the constraints?

Step 2: Breaking down the problem
- What are the sub-problems?
- How do they relate to each other?
- What's the logical sequence?

Step 3: Solving each part
- [Work through each step methodically]

Step 4: Combining results
- How do the pieces fit together?
- Does the solution make sense?

Step 5: Verification
- Does this solve the original problem?
- Are there edge cases to consider?
```

### Tree of Thoughts (ToT)

#### Multi-Path Reasoning
```
Let's explore multiple approaches to solve: [PROBLEM]

Approach 1: [METHOD 1]
Pros: [LIST ADVANTAGES]
Cons: [LIST DISADVANTAGES]
Outcome: [PREDICTED RESULT]

Approach 2: [METHOD 2]
Pros: [LIST ADVANTAGES]
Cons: [LIST DISADVANTAGES]
Outcome: [PREDICTED RESULT]

Approach 3: [METHOD 3]
Pros: [LIST ADVANTAGES]
Cons: [LIST DISADVANTAGES]
Outcome: [PREDICTED RESULT]

Best path forward: [CHOSEN APPROACH WITH REASONING]
Implementation plan: [SPECIFIC STEPS]
```

### Few-Shot Learning Templates

#### Classification Task
```
Classify the following examples into categories:

Example 1: "The weather is sunny and warm today"
Category: Weather

Example 2: "I need to buy groceries and cook dinner"
Category: Personal Tasks

Example 3: "The stock market closed higher today"
Category: Finance

Now classify this: "[NEW EXAMPLE]"
Category: 
```

#### Writing Style Transfer
```
Rewrite the following text in different styles:

Original: "The meeting was postponed due to technical issues."

Formal: "The scheduled meeting has been deferred owing to technical complications."
Casual: "We had to push back the meeting because of some tech problems."
Excited: "Guess what? The meeting got moved because of some crazy technical stuff!"

Now rewrite this in [TARGET STYLE]: "[TEXT TO REWRITE]"
```

## Domain-Specific Templates

### Business & Strategy

#### SWOT Analysis
```
Conduct a SWOT analysis for: [BUSINESS/PROJECT/IDEA]

**Strengths** (Internal positive factors):
- [List 3-5 key strengths]

**Weaknesses** (Internal negative factors):
- [List 3-5 key weaknesses]

**Opportunities** (External positive factors):
- [List 3-5 key opportunities]

**Threats** (External negative factors):
- [List 3-5 key threats]

**Strategic Recommendations**:
1. How to leverage strengths to capitalize on opportunities
2. How to address weaknesses to avoid threats
3. Priority actions for the next 90 days
```

#### Business Plan Section
```
Create a [BUSINESS PLAN SECTION] for: [BUSINESS IDEA]

Include:
1. **Overview**: Brief description and value proposition
2. **Market Analysis**: Target audience and competition
3. **Strategy**: How you'll achieve success
4. **Resources**: What you need to get started
5. **Timeline**: Key milestones and deadlines
6. **Metrics**: How you'll measure success

Make it actionable and specific to [INDUSTRY/CONTEXT].
```

### Technical Documentation

#### API Documentation
```
Document this API endpoint:

**Endpoint**: [METHOD] /api/[endpoint]
**Description**: [What this endpoint does]

**Parameters**:
- `param1` (type): Description
- `param2` (type, optional): Description

**Request Example**:
```json
{
  "example": "request"
}
```

**Response Example**:
```json
{
  "example": "response"
}
```

**Error Codes**:
- 400: Bad Request - [When this occurs]
- 401: Unauthorized - [When this occurs]
- 500: Server Error - [When this occurs]
```

#### Troubleshooting Guide
```
**Problem**: [Issue description]

**Symptoms**:
- [Observable behavior 1]
- [Observable behavior 2]
- [Observable behavior 3]

**Possible Causes**:
1. [Cause 1] - Likelihood: High/Medium/Low
2. [Cause 2] - Likelihood: High/Medium/Low
3. [Cause 3] - Likelihood: High/Medium/Low

**Solutions** (try in order):
1. **[Solution 1]**
   - Steps: [Detailed steps]
   - Expected result: [What should happen]
   
2. **[Solution 2]**
   - Steps: [Detailed steps]
   - Expected result: [What should happen]

**Prevention**:
- [How to avoid this issue in the future]
```

### Educational Content

#### Lesson Plan
```
**Topic**: [SUBJECT]
**Duration**: [TIME]
**Audience**: [TARGET LEARNERS]

**Learning Objectives**:
By the end of this lesson, students will be able to:
1. [Specific, measurable objective 1]
2. [Specific, measurable objective 2]
3. [Specific, measurable objective 3]

**Prerequisites**: [Required knowledge/skills]

**Materials Needed**:
- [Resource 1]
- [Resource 2]

**Lesson Structure**:
1. **Introduction** (X minutes)
   - Hook: [Engaging opening]
   - Overview: [What we'll cover]

2. **Main Content** (X minutes)
   - [Key concept 1 with examples]
   - [Key concept 2 with examples]
   - [Practice activity]

3. **Conclusion** (X minutes)
   - Summary: [Key takeaways]
   - Next steps: [What's coming next]

**Assessment**: [How you'll check understanding]
**Homework/Follow-up**: [Optional assignments]
```

## Creative Writing Templates

### Story Structure

#### Hero's Journey
```
Create a story following the Hero's Journey structure:

**Ordinary World**: [Character's normal life]
**Call to Adventure**: [Inciting incident]
**Refusal of the Call**: [Initial hesitation]
**Meeting the Mentor**: [Wise guide appears]
**Crossing the Threshold**: [Point of no return]
**Tests, Allies, Enemies**: [Challenges and relationships]
**Approach to the Inmost Cave**: [Preparing for major challenge]
**Ordeal**: [Greatest fear/crisis]
**Reward**: [Surviving and gaining something]
**The Road Back**: [Beginning of return]
**Resurrection**: [Final test and transformation]
**Return with the Elixir**: [Coming home changed]

Character: [PROTAGONIST]
Setting: [WORLD/ENVIRONMENT]
Central conflict: [MAIN CHALLENGE]
```

### Marketing & Sales

#### Product Launch Announcement
```
**Headline**: [Attention-grabbing title]

**Problem**: [What problem does this solve?]
"Many [TARGET AUDIENCE] struggle with [SPECIFIC PAIN POINT]..."

**Solution**: [Your product/service]
"Introducing [PRODUCT NAME] - [ONE-LINE DESCRIPTION]"

**Benefits**: [What's in it for them?]
- [Benefit 1 with specific outcome]
- [Benefit 2 with specific outcome]  
- [Benefit 3 with specific outcome]

**Social Proof**: [Why should they trust you?]
"[TESTIMONIAL/STATISTIC/ACHIEVEMENT]"

**Call to Action**: [What do you want them to do?]
"[SPECIFIC ACTION] by [DEADLINE] to [INCENTIVE]"

**Contact**: [How to reach you]
```

## Prompt Optimization Strategies

### Iterative Improvement

#### Version 1 (Basic)
```
Write a blog post about AI.
```

#### Version 2 (More Specific)
```
Write a 1000-word blog post about the benefits of AI for small businesses, including practical examples and implementation tips.
```

#### Version 3 (Structured)
```
Write a 1000-word blog post for small business owners about AI benefits:

Structure:
1. Introduction: Hook + problem statement
2. 3 main benefits with real examples
3. Implementation guide (5 practical steps)
4. Common concerns and solutions
5. Call-to-action

Tone: Professional but approachable
Include: Statistics, case studies, actionable advice
Avoid: Technical jargon, overly complex concepts
```

### Testing Framework

#### A/B Testing Prompts
```
Test A (Direct):
[DIRECT INSTRUCTION]

Test B (Context-Rich):
[DETAILED CONTEXT + INSTRUCTION]

Test C (Role-Based):
[ROLE ASSIGNMENT + INSTRUCTION]

Evaluate based on:
- Relevance to goal
- Quality of output
- Consistency across runs
- Time to completion
```

## Prompt Libraries by Use Case

### Content Creation
- Blog post outlines
- Social media captions
- Email newsletters
- Video scripts
- Podcast outlines

### Business Operations
- Meeting agendas
- Project plans
- Performance reviews
- Process documentation
- Training materials

### Technical Tasks
- Code generation
- Debugging assistance
- Architecture design
- Documentation writing
- Testing scenarios

### Research & Analysis
- Market research
- Competitive analysis
- Data interpretation
- Literature reviews
- Trend analysis

## Best Practices for Prompt Engineering

### Do's
✅ Be specific and clear
✅ Provide context and examples
✅ Use structured formats
✅ Test and iterate
✅ Consider the model's capabilities
✅ Include quality criteria
✅ Specify output format

### Don'ts
❌ Be vague or ambiguous
❌ Overload with too many instructions
❌ Assume implicit knowledge
❌ Use inconsistent terminology
❌ Ignore context limitations
❌ Skip validation steps
❌ Neglect edge cases

### Optimization Checklist
- [ ] Clear objective defined
- [ ] Appropriate context provided
- [ ] Examples included (if helpful)
- [ ] Output format specified
- [ ] Quality criteria established
- [ ] Edge cases considered
- [ ] Tested with variations
- [ ] Performance measured

---

*Last updated: December 2024*
*Templates tested across multiple AI models*
*Regular updates with new patterns and techniques*
