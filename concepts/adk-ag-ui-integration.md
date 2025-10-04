# ADK + AG-UI Integration: Fancy Frontends for ADK Agents

Combining Google's Agent Development Kit (ADK) with AG-UI protocol to create production-ready, interactive AI agent interfaces with rich user experiences.

---

**[Delight users by combining ADK Agents with Fancy Frontends using AG-UI (Google Developer Blog)](https://developers.googleblog.com/en/delight-users-by-combining-adk-agents-with-fancy-frontends-using-ag-ui/)** 🎨 — *Official Google guide demonstrating ADK + AG-UI integration for building sophisticated AI applications. Shows how to connect ADK's powerful agent backend with AG-UI's flexible frontend protocol using CopilotKit, enabling generative UI, shared state, human-in-the-loop workflows, and frontend tool interactions.*

---

## 🏗️ Integration Architecture

### Core Components

- **ADK Backend**: Agent Development Kit providing multi-step planning, tool use, and state management
- **AG-UI Protocol**: Open protocol for standardized agent-frontend communication
- **CopilotKit**: React components and hooks implementing AG-UI for seamless frontend integration
- **Frontend Application**: Next.js/React app with CopilotKit components

### Data Flow

1. User interacts with CopilotKit-powered frontend interface
2. AG-UI protocol handles communication between frontend and ADK backend
3. ADK agent processes requests, uses tools, and generates responses
4. Results flow back through AG-UI to update frontend with rich UI elements

## ✨ Key Features Unlocked

### Generative UI

- Agents can generate and render UI components directly in chat
- Contextual information display beyond text responses
- Dynamic interface elements based on agent reasoning

### Shared State Management

- Frontend and backend maintain synchronized application state
- Agent actions can update UI state and vice versa
- Consistent user experience across interactions

### Human-in-the-Loop Workflows

- Users can supervise, approve, or correct agent actions
- Safety controls and intervention capabilities
- Collaborative decision-making between AI and human

### Frontend Tool Integration

- Agents can directly interact with frontend elements
- Form filling, page navigation, document annotation
- Seamless agent control of user interface

## 🚀 Quick Start Implementation

### 1. Create ADK + AG-UI Project

```bash
npx copilotkit@latest create -f adk
```

### 2. Configure ADK Backend Agent

```typescript
// backend/agent.ts
import { adk } from "@copilotkit/adk";

adk.setSystemMessage("You are a helpful assistant that can fetch stock prices.");

// Define tools the agent can use
adk.addTool("getStockPrice", {
  description: "Get the current stock price for a given ticker symbol.",
  parameters: {
    type: "object",
    properties: {
      ticker: {
        type: "string",
        description: "The stock ticker symbol (e.g., GOOGL).",
      },
    },
    required: ["ticker"],
  },
  handler: async ({ ticker }) => {
    // Implementation here
    return `The current price of ${ticker} is $${price}.`;
  },
});

export default adk;
```

### 3. Setup Frontend with CopilotKit

```tsx
// frontend/src/app/page.tsx
"use client";

import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

export default function Home() {
  return (
    <CopilotKit url="http://localhost:5001/api/adk">
      <main>
        <h1>Welcome to Your ADK + AG-UI App!</h1>
        <p>Ask me to get a stock price.</p>
      </main>
      <CopilotChat />
    </CopilotKit>
  );
}
```

## 📦 Key Resources

- **[CopilotKit Documentation](https://docs.copilotkit.ai/adk)** — Complete ADK integration guide
- **[AG-UI Protocol Documentation](https://docs.ag-ui.com/)** — Protocol specification and concepts
- **[Starter Repository](https://github.com/copilotkit/with-adk)** — Pre-configured ADK + AG-UI project
- **[AG-UI Dojo Tutorial](https://dojo.ag-ui.com/adk-middleware/feature/shared_state)** — Interactive learning platform

## 🎯 Use Cases & Applications

- **Conversational Commerce**: AI shopping assistants with rich product displays
- **Data Analysis Tools**: Interactive dashboards with agent-driven insights
- **Content Creation**: Collaborative writing with real-time UI generation
- **Workflow Automation**: Human-supervised business process automation
- **Educational Platforms**: Interactive learning experiences with agent guidance

## 🔄 Comparison with Other Approaches

| Feature | ADK Only | ADK + AG-UI |
|---------|----------|-------------|
| UI Quality | Basic developer UI | Production-ready interfaces |
| User Experience | Limited | Rich, interactive |
| State Management | Backend only | Shared frontend/backend |
| Human Oversight | Limited | Full intervention capabilities |
| Tool Integration | Backend tools | Frontend + backend tools |

## 📈 Benefits & Impact

- **Faster Development**: One-command setup for full-stack agent applications
- **Better UX**: Professional interfaces that delight users
- **Enhanced Safety**: Human-in-the-loop controls for critical operations
- **Scalability**: Standardized protocol enables ecosystem growth
- **Innovation**: Enables new interaction patterns between AI and humans

---

*See also: [AG-UI (Agent Graphical User Interface)](./ag-ui.md), [AI Agents](./ai-agents.md), [Agent Protocols](./agent-protocols.md)*
