# Stateless Agent Design 🎯

> Building scalable, reliable LLM agents through stateless architecture patterns

## Overview

Stateless agent design is a fundamental principle for building production-ready LLM agents that can scale horizontally, recover from failures gracefully, and maintain consistency across distributed deployments. By externalizing all state and maintaining no server-side session data, agents become inherently more reliable and scalable.

## Core Principles

### 1. No Server-Side State
- **Stateless execution**: Each request is self-contained
- **External state storage**: All state stored in external systems
- **Session independence**: No dependency on previous requests

### 2. Idempotent Operations
- **Repeatable requests**: Same input produces same output
- **Safe retries**: Operations can be retried without side effects
- **Consistency guarantees**: Predictable behavior across instances

### 3. Horizontal Scalability
- **Load distribution**: Requests routed to any available instance
- **Auto-scaling**: Scale based on demand without state concerns
- **Fault tolerance**: Instance failures don't lose user state

## Architecture Patterns

### 1. External State Management

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from datetime import datetime
import json
import asyncio

@dataclass
class ConversationTurn:
    """Represents a single conversation turn."""
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime
    metadata: Dict[str, Any] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata or {}
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ConversationTurn":
        return cls(
            role=data["role"],
            content=data["content"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            metadata=data.get("metadata", {})
        )

class StateStorage(ABC):
    """Abstract interface for external state storage."""
    
    @abstractmethod
    async def get_conversation_history(self, session_id: str) -> List[ConversationTurn]:
        """Retrieve conversation history for a session."""
        pass
    
    @abstractmethod
    async def append_conversation_turn(self, session_id: str, turn: ConversationTurn) -> None:
        """Append a new turn to the conversation."""
        pass
    
    @abstractmethod
    async def get_user_context(self, user_id: str) -> Dict[str, Any]:
        """Retrieve user context and preferences."""
        pass
    
    @abstractmethod
    async def update_user_context(self, user_id: str, context: Dict[str, Any]) -> None:
        """Update user context."""
        pass
    
    @abstractmethod
    async def get_session_metadata(self, session_id: str) -> Dict[str, Any]:
        """Retrieve session metadata."""
        pass
    
    @abstractmethod
    async def update_session_metadata(self, session_id: str, metadata: Dict[str, Any]) -> None:
        """Update session metadata."""
        pass

class RedisStateStorage(StateStorage):
    """Redis implementation of state storage."""
    
    def __init__(self, redis_client):
        self.redis = redis_client
    
    async def get_conversation_history(self, session_id: str) -> List[ConversationTurn]:
        """Get conversation history from Redis."""
        key = f"conversation:{session_id}"
        history_data = await self.redis.lrange(key, 0, -1)
        
        history = []
        for turn_data in history_data:
            turn_dict = json.loads(turn_data)
            history.append(ConversationTurn.from_dict(turn_dict))
        
        return history
    
    async def append_conversation_turn(self, session_id: str, turn: ConversationTurn) -> None:
        """Append turn to conversation history."""
        key = f"conversation:{session_id}"
        turn_data = json.dumps(turn.to_dict())
        
        await self.redis.lpush(key, turn_data)
        
        # Keep only last 100 turns
        await self.redis.ltrim(key, 0, 99)
        
        # Set expiration (7 days)
        await self.redis.expire(key, 604800)
    
    async def get_user_context(self, user_id: str) -> Dict[str, Any]:
        """Get user context from Redis."""
        key = f"user_context:{user_id}"
        context_data = await self.redis.get(key)
        
        if context_data:
            return json.loads(context_data)
        return {}
    
    async def update_user_context(self, user_id: str, context: Dict[str, Any]) -> None:
        """Update user context in Redis."""
        key = f"user_context:{user_id}"
        context_data = json.dumps(context)
        await self.redis.set(key, context_data, ex=2592000)  # 30 days
    
    async def get_session_metadata(self, session_id: str) -> Dict[str, Any]:
        """Get session metadata from Redis."""
        key = f"session_metadata:{session_id}"
        metadata_data = await self.redis.get(key)
        
        if metadata_data:
            return json.loads(metadata_data)
        return {}
    
    async def update_session_metadata(self, session_id: str, metadata: Dict[str, Any]) -> None:
        """Update session metadata in Redis."""
        key = f"session_metadata:{session_id}"
        metadata_data = json.dumps(metadata)
        await self.redis.set(key, metadata_data, ex=86400)  # 24 hours
```

### 2. Stateless Agent Implementation

```python
from langchain.llms import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from typing import List, Dict, Any

class StatelessAgent:
    """Completely stateless LLM agent."""
    
    def __init__(self, model_name: str, state_storage: StateStorage):
        self.llm = ChatOpenAI(model=model_name, temperature=0.1)
        self.state_storage = state_storage
    
    async def process_message(self, 
                            user_id: str, 
                            session_id: str, 
                            message: str,
                            context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process a user message in a stateless manner."""
        
        # 1. Retrieve all necessary state from external storage
        conversation_history = await self.state_storage.get_conversation_history(session_id)
        user_context = await self.state_storage.get_user_context(user_id)
        session_metadata = await self.state_storage.get_session_metadata(session_id)
        
        # 2. Build complete context for this request
        request_context = {
            "user_context": user_context,
            "session_metadata": session_metadata,
            "conversation_history": conversation_history,
            "current_message": message,
            "additional_context": context or {}
        }
        
        # 3. Process the request using complete context
        response = await self._generate_response(request_context)
        
        # 4. Store the new conversation turn
        user_turn = ConversationTurn(
            role="user",
            content=message,
            timestamp=datetime.utcnow(),
            metadata={"user_id": user_id}
        )
        
        assistant_turn = ConversationTurn(
            role="assistant", 
            content=response["content"],
            timestamp=datetime.utcnow(),
            metadata=response.get("metadata", {})
        )
        
        await self.state_storage.append_conversation_turn(session_id, user_turn)
        await self.state_storage.append_conversation_turn(session_id, assistant_turn)
        
        # 5. Update any derived state
        await self._update_derived_state(user_id, session_id, request_context, response)
        
        return {
            "response": response["content"],
            "session_id": session_id,
            "metadata": response.get("metadata", {}),
            "timestamp": datetime.utcnow().isoformat()
        }
    
    async def _generate_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate response using complete context."""
        
        # Build message history for LLM
        messages = []
        
        # Add system message with user context
        system_prompt = self._build_system_prompt(context["user_context"])
        messages.append(SystemMessage(content=system_prompt))
        
        # Add conversation history
        for turn in context["conversation_history"][-10:]:  # Last 10 turns
            if turn.role == "user":
                messages.append(HumanMessage(content=turn.content))
            else:
                messages.append(AIMessage(content=turn.content))
        
        # Add current message
        messages.append(HumanMessage(content=context["current_message"]))
        
        # Generate response
        response = await self.llm.agenerate([messages])
        
        return {
            "content": response.generations[0][0].text,
            "metadata": {
                "model": self.llm.model_name,
                "tokens_used": response.llm_output.get("token_usage", {}),
                "processing_time": datetime.utcnow().isoformat()
            }
        }
    
    def _build_system_prompt(self, user_context: Dict[str, Any]) -> str:
        """Build system prompt based on user context."""
        base_prompt = "You are a helpful AI assistant."
        
        # Customize based on user preferences
        if user_context.get("expertise_level") == "expert":
            base_prompt += " Provide detailed, technical responses."
        elif user_context.get("expertise_level") == "beginner":
            base_prompt += " Provide simple, easy-to-understand explanations."
        
        if user_context.get("preferred_style") == "concise":
            base_prompt += " Keep responses brief and to the point."
        elif user_context.get("preferred_style") == "detailed":
            base_prompt += " Provide comprehensive, detailed responses."
        
        return base_prompt
    
    async def _update_derived_state(self, 
                                  user_id: str, 
                                  session_id: str, 
                                  context: Dict[str, Any], 
                                  response: Dict[str, Any]) -> None:
        """Update derived state based on interaction."""
        
        # Update session metadata
        session_metadata = context["session_metadata"]
        session_metadata["last_activity"] = datetime.utcnow().isoformat()
        session_metadata["message_count"] = session_metadata.get("message_count", 0) + 1
        
        await self.state_storage.update_session_metadata(session_id, session_metadata)
        
        # Update user context if needed
        user_context = context["user_context"]
        user_context["last_seen"] = datetime.utcnow().isoformat()
        user_context["total_interactions"] = user_context.get("total_interactions", 0) + 1
        
        await self.state_storage.update_user_context(user_id, user_context)
```

### 3. Request Context Pattern

```python
from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class AgentRequest:
    """Complete request context for stateless processing."""
    user_id: str
    session_id: str
    message: str
    timestamp: datetime
    user_context: Dict[str, Any]
    session_context: Dict[str, Any]
    conversation_history: List[ConversationTurn]
    additional_context: Dict[str, Any] = None
    
    def to_prompt_context(self) -> Dict[str, Any]:
        """Convert to context suitable for prompt generation."""
        return {
            "user_preferences": self.user_context,
            "session_info": self.session_context,
            "recent_messages": self.conversation_history[-5:],  # Last 5 messages
            "current_message": self.message,
            "metadata": self.additional_context or {}
        }

class RequestContextBuilder:
    """Builds complete request context for stateless processing."""
    
    def __init__(self, state_storage: StateStorage):
        self.state_storage = state_storage
    
    async def build_context(self, 
                          user_id: str, 
                          session_id: str, 
                          message: str,
                          additional_context: Dict[str, Any] = None) -> AgentRequest:
        """Build complete request context."""
        
        # Fetch all required state in parallel
        user_context_task = self.state_storage.get_user_context(user_id)
        session_context_task = self.state_storage.get_session_metadata(session_id)
        history_task = self.state_storage.get_conversation_history(session_id)
        
        user_context, session_context, conversation_history = await asyncio.gather(
            user_context_task,
            session_context_task,
            history_task
        )
        
        return AgentRequest(
            user_id=user_id,
            session_id=session_id,
            message=message,
            timestamp=datetime.utcnow(),
            user_context=user_context,
            session_context=session_context,
            conversation_history=conversation_history,
            additional_context=additional_context
        )
```

### 4. Stateless Tool Integration

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, List

class StatelessTool(ABC):
    """Abstract base for stateless tools."""
    
    @abstractmethod
    async def execute(self, 
                     context: AgentRequest, 
                     parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute tool with complete context."""
        pass
    
    @abstractmethod
    def get_tool_schema(self) -> Dict[str, Any]:
        """Get tool schema for LLM function calling."""
        pass

class SearchTool(StatelessTool):
    """Stateless search tool."""
    
    def __init__(self, search_service):
        self.search_service = search_service
    
    async def execute(self, 
                     context: AgentRequest, 
                     parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute search with user context."""
        query = parameters.get("query", "")
        
        # Customize search based on user context
        search_params = {
            "query": query,
            "user_id": context.user_id,
            "language": context.user_context.get("language", "en"),
            "expertise_level": context.user_context.get("expertise_level", "general")
        }
        
        results = await self.search_service.search(**search_params)
        
        return {
            "results": results,
            "query": query,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def get_tool_schema(self) -> Dict[str, Any]:
        """Get search tool schema."""
        return {
            "name": "search",
            "description": "Search for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["query"]
            }
        }

class StatelessToolAgent(StatelessAgent):
    """Stateless agent with tool capabilities."""
    
    def __init__(self, model_name: str, state_storage: StateStorage, tools: List[StatelessTool]):
        super().__init__(model_name, state_storage)
        self.tools = {tool.get_tool_schema()["name"]: tool for tool in tools}
    
    async def _generate_response(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate response with tool support."""
        
        # Check if tools are needed
        tool_schemas = [tool.get_tool_schema() for tool in self.tools.values()]
        
        # Build messages with tool definitions
        messages = self._build_messages_with_tools(context, tool_schemas)
        
        # Generate response with function calling
        response = await self.llm.agenerate([messages])
        
        # Check if tools were called
        if response.function_call:
            tool_result = await self._execute_tool(context, response.function_call)
            
            # Generate final response with tool results
            final_response = await self._generate_with_tool_results(context, tool_result)
            return final_response
        
        return {
            "content": response.generations[0][0].text,
            "metadata": {"tools_used": []}
        }
    
    async def _execute_tool(self, 
                          context: Dict[str, Any], 
                          function_call: Dict[str, Any]) -> Dict[str, Any]:
        """Execute tool in stateless manner."""
        tool_name = function_call["name"]
        parameters = function_call["arguments"]
        
        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")
        
        tool = self.tools[tool_name]
        
        # Build request context for tool
        request_context = AgentRequest(
            user_id=context["user_context"].get("user_id", ""),
            session_id=context["session_metadata"].get("session_id", ""),
            message=context["current_message"],
            timestamp=datetime.utcnow(),
            user_context=context["user_context"],
            session_context=context["session_metadata"],
            conversation_history=context["conversation_history"]
        )
        
        return await tool.execute(request_context, parameters)
```

## Scaling Patterns

### 1. Horizontal Scaling

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Stateless Agent API")

class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    message: str
    context: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    metadata: Dict[str, Any]
    timestamp: str

# Global agent instance (stateless, safe to share)
agent = None

@app.on_event("startup")
async def startup_event():
    """Initialize agent on startup."""
    global agent
    
    # Initialize state storage
    redis_client = Redis.from_url(os.getenv("REDIS_URL"))
    state_storage = RedisStateStorage(redis_client)
    
    # Initialize agent
    agent = StatelessAgent(
        model_name=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
        state_storage=state_storage
    )

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    """Stateless chat endpoint."""
    try:
        result = await agent.process_message(
            user_id=request.user_id,
            session_id=request.session_id,
            message=request.message,
            context=request.context
        )
        
        return ChatResponse(**result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

# Run with multiple workers for horizontal scaling
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=4  # Multiple workers, each handling requests independently
    )
```

### 2. Load Balancing Configuration

```yaml
# nginx.conf for load balancing
upstream agent_backend {
    server agent-1:8000;
    server agent-2:8000;
    server agent-3:8000;
    
    # Least connections for optimal distribution
    least_conn;
}

server {
    listen 80;
    
    location /chat {
        proxy_pass http://agent_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # No session affinity needed - stateless!
    }
    
    location /health {
        proxy_pass http://agent_backend;
    }
}
```

### 3. Auto-Scaling Configuration

```yaml
# Kubernetes HPA for auto-scaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: stateless-agent-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: stateless-agent
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
```

## Performance Optimization

### 1. State Caching

```python
from functools import wraps
from typing import Callable, Any
import hashlib

class StateCache:
    """Cache for frequently accessed state."""
    
    def __init__(self, cache_client, ttl: int = 300):
        self.cache = cache_client
        self.ttl = ttl
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        value = await self.cache.get(f"cache:{key}")
        if value:
            return json.loads(value)
        return None
    
    async def set(self, key: str, value: Any) -> None:
        """Set value in cache."""
        await self.cache.set(
            f"cache:{key}", 
            json.dumps(value), 
            ex=self.ttl
        )

def cache_state(cache: StateCache, key_func: Callable = None):
    """Decorator for caching state operations."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate cache key
            if key_func:
                cache_key = key_func(*args, **kwargs)
            else:
                cache_key = hashlib.md5(
                    f"{func.__name__}:{str(args)}:{str(kwargs)}".encode()
                ).hexdigest()
            
            # Try cache first
            cached_result = await cache.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Execute function and cache result
            result = await func(*args, **kwargs)
            await cache.set(cache_key, result)
            
            return result
        return wrapper
    return decorator

class CachedStateStorage(StateStorage):
    """State storage with caching layer."""
    
    def __init__(self, storage: StateStorage, cache: StateCache):
        self.storage = storage
        self.cache = cache
    
    @cache_state(cache, lambda self, user_id: f"user_context:{user_id}")
    async def get_user_context(self, user_id: str) -> Dict[str, Any]:
        """Get user context with caching."""
        return await self.storage.get_user_context(user_id)
    
    async def update_user_context(self, user_id: str, context: Dict[str, Any]) -> None:
        """Update user context and invalidate cache."""
        await self.storage.update_user_context(user_id, context)
        # Invalidate cache
        await self.cache.cache.delete(f"cache:user_context:{user_id}")
```

### 2. Connection Pooling

```python
import aioredis
import asyncpg
from sqlalchemy.ext.asyncio import create_async_engine

class PooledStateStorage(StateStorage):
    """State storage with connection pooling."""
    
    def __init__(self, redis_url: str, postgres_url: str):
        self.redis_pool = None
        self.postgres_pool = None
        self.redis_url = redis_url
        self.postgres_url = postgres_url
    
    async def initialize_pools(self):
        """Initialize connection pools."""
        # Redis pool
        self.redis_pool = aioredis.ConnectionPool.from_url(
            self.redis_url,
            max_connections=20,
            retry_on_timeout=True
        )
        
        # PostgreSQL pool
        self.postgres_pool = asyncpg.create_pool(
            self.postgres_url,
            min_size=5,
            max_size=20,
            command_timeout=60
        )
    
    async def get_conversation_history(self, session_id: str) -> List[ConversationTurn]:
        """Get conversation history using pooled connections."""
        async with aioredis.Redis(connection_pool=self.redis_pool) as redis:
            # Implementation using pooled Redis connection
            pass
    
    async def close_pools(self):
        """Close connection pools."""
        if self.redis_pool:
            await self.redis_pool.disconnect()
        if self.postgres_pool:
            await self.postgres_pool.close()
```

## Best Practices

### 1. State Design
- **Minimize state size**: Keep state lean and focused
- **Immutable state**: Treat state as immutable where possible
- **State validation**: Validate state integrity on retrieval

### 2. Error Handling
- **Graceful degradation**: Handle missing state gracefully
- **Retry mechanisms**: Implement exponential backoff for state operations
- **Circuit breakers**: Protect against state storage failures

### 3. Security
- **State encryption**: Encrypt sensitive state data
- **Access controls**: Implement proper authorization
- **Audit logging**: Log state access and modifications

### 4. Monitoring
- **State metrics**: Monitor state storage performance
- **Cache hit rates**: Track caching effectiveness
- **Error rates**: Monitor state operation failures

## Testing Stateless Agents

### 1. Unit Testing

```python
import pytest
from unittest.mock import AsyncMock, MagicMock

@pytest.fixture
async def mock_state_storage():
    """Mock state storage for testing."""
    storage = AsyncMock(spec=StateStorage)
    storage.get_conversation_history.return_value = []
    storage.get_user_context.return_value = {}
    storage.get_session_metadata.return_value = {}
    return storage

@pytest.fixture
async def stateless_agent(mock_state_storage):
    """Create agent for testing."""
    return StatelessAgent("gpt-3.5-turbo", mock_state_storage)

@pytest.mark.asyncio
async def test_process_message_stateless(stateless_agent, mock_state_storage):
    """Test that agent processes messages without internal state."""
    # Given
    user_id = "user123"
    session_id = "session456"
    message = "Hello, world!"
    
    # When
    result1 = await stateless_agent.process_message(user_id, session_id, message)
    result2 = await stateless_agent.process_message(user_id, session_id, message)
    
    # Then
    assert result1["session_id"] == session_id
    assert result2["session_id"] == session_id
    
    # Verify state storage was called for each request
    assert mock_state_storage.get_conversation_history.call_count == 2
    assert mock_state_storage.get_user_context.call_count == 2
```

### 2. Integration Testing

```python
@pytest.mark.asyncio
async def test_multiple_instances_consistency():
    """Test that multiple agent instances behave consistently."""
    # Create two separate agent instances
    storage = RedisStateStorage(redis_client)
    agent1 = StatelessAgent("gpt-3.5-turbo", storage)
    agent2 = StatelessAgent("gpt-3.5-turbo", storage)
    
    user_id = "user123"
    session_id = "session456"
    
    # Send message to first agent
    await agent1.process_message(user_id, session_id, "Hello")
    
    # Send follow-up message to second agent
    result = await agent2.process_message(user_id, session_id, "How are you?")
    
    # Verify second agent has access to conversation history
    assert result is not None
    # Additional assertions based on expected behavior
```

## Related Concepts

- [[agent-deployment-patterns]] - Production deployment strategies
- [[pause-resume-workflows]] - Workflow state management
- [[human-in-the-loop]] - External state integration
- [[12-factor-agents]] - Foundational principles
- [[production-deployment]] - Deployment considerations
- [[observability]] - Monitoring stateless systems
- [[mlops]] - ML operations practices

## Tools and Technologies

- **State Storage**: Redis, PostgreSQL, DynamoDB, MongoDB
- **Caching**: Redis, Memcached, ElastiCache
- **Load Balancing**: Nginx, HAProxy, AWS ALB, GCP Load Balancer
- **Auto-scaling**: Kubernetes HPA, AWS Auto Scaling, GCP Autoscaler
- **Monitoring**: Prometheus, Grafana, DataDog, New Relic

---

*Stateless agent design enables building scalable, reliable, and maintainable LLM applications that can handle production workloads effectively.*
