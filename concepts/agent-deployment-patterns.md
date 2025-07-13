# Agent Deployment Patterns 🚀

> Production deployment strategies for LLM agents inspired by 12-factor methodology

## Core Principles

### 1. Codebase Isolation
- **One agent per repository**: Each agent maintains its own versioned codebase
- **Shared libraries**: Common functionality extracted to separate packages
- **Configuration separation**: Environment-specific configs kept separate from code

```python
# Agent structure example
agent-service/
├── src/
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── handlers/
│   ├── config/
│   │   └── settings.py
│   └── requirements.txt
├── deployment/
│   ├── docker/
│   ├── k8s/
│   └── terraform/
└── tests/
```

### 2. Dependency Declaration
- **Explicit dependencies**: All agent dependencies declared in manifest files
- **Isolation**: No implicit dependencies on system packages
- **Vendoring**: Critical dependencies vendored for reliability

```python
# requirements.txt with pinned versions
langchain==0.1.0
openai==1.0.0
fastapi==0.104.1
pydantic==2.5.0
redis==5.0.1
```

### 3. Configuration Management
- **Environment variables**: All config through env vars
- **Secrets management**: Sensitive data through secure vaults
- **Configuration validation**: Validate config at startup

```python
from pydantic import BaseSettings

class AgentConfig(BaseSettings):
    """Agent configuration from environment variables."""
    
    # Model configuration
    model_name: str = "gpt-4"
    temperature: float = 0.1
    max_tokens: int = 1000
    
    # Infrastructure
    redis_url: str
    database_url: str
    
    # Security
    api_key: str
    auth_secret: str
    
    class Config:
        env_file = ".env"
```

## Deployment Strategies

### Stateless Deployment
- **No local state**: All state externalized to backing services
- **Horizontal scaling**: Multiple identical instances
- **Load balancing**: Traffic distributed across instances

```python
class StatelessAgent:
    """Stateless agent implementation."""
    
    def __init__(self, config: AgentConfig):
        self.llm = self._init_llm(config)
        self.memory = RedisMemory(config.redis_url)
        self.storage = DatabaseStorage(config.database_url)
    
    async def process_request(self, request: AgentRequest) -> AgentResponse:
        """Process request without local state."""
        # Retrieve context from external storage
        context = await self.memory.get_context(request.session_id)
        
        # Process with LLM
        response = await self.llm.agenerate(
            messages=context + [request.message]
        )
        
        # Update external state
        await self.memory.update_context(
            request.session_id, 
            context + [request.message, response]
        )
        
        return AgentResponse(content=response.content)
```

### Microservice Architecture
- **Single responsibility**: Each service handles one aspect
- **API communication**: Services communicate via well-defined APIs
- **Independent deployment**: Services deployed and scaled independently

```python
# Agent orchestrator service
class AgentOrchestrator:
    """Coordinates multiple specialized agents."""
    
    def __init__(self):
        self.router = AgentRouter()
        self.tools = ToolRegistry()
        self.monitor = MonitoringService()
    
    async def handle_request(self, request: UserRequest) -> AgentResponse:
        """Route request to appropriate agent."""
        agent_type = await self.router.determine_agent(request)
        
        if agent_type == "code":
            return await self.tools.code_agent.process(request)
        elif agent_type == "search":
            return await self.tools.search_agent.process(request)
        else:
            return await self.tools.general_agent.process(request)
```

### Container Deployment
- **Docker containers**: Agents packaged as containers
- **Kubernetes orchestration**: Container orchestration and scaling
- **Health checks**: Built-in health monitoring

```dockerfile
# Dockerfile for agent service
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY config/ ./config/

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Scaling Patterns

### Horizontal Scaling
- **Load balancing**: Distribute requests across instances
- **Auto-scaling**: Scale based on metrics
- **Resource limits**: Set appropriate CPU/memory limits

```yaml
# Kubernetes deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: agent-service
  template:
    metadata:
      labels:
        app: agent-service
    spec:
      containers:
      - name: agent
        image: agent-service:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "512Mi"
            cpu: "0.5"
          limits:
            memory: "1Gi"
            cpu: "1"
        env:
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: agent-secrets
              key: redis-url
---
apiVersion: v1
kind: Service
metadata:
  name: agent-service
spec:
  selector:
    app: agent-service
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
```

### Vertical Scaling
- **Resource optimization**: Optimize memory and CPU usage
- **Model efficiency**: Use efficient model variants
- **Caching strategies**: Cache frequent responses

```python
class OptimizedAgent:
    """Agent optimized for resource usage."""
    
    def __init__(self, config: AgentConfig):
        # Use efficient model variants
        self.llm = ChatOpenAI(
            model=config.model_name,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            streaming=True  # Enable streaming for better UX
        )
        
        # Response caching
        self.cache = TTLCache(maxsize=1000, ttl=3600)
        
        # Memory optimization
        self.memory = ConversationSummaryMemory(
            llm=self.llm,
            max_token_limit=2000
        )
    
    async def process_with_caching(self, request: str) -> str:
        """Process request with response caching."""
        cache_key = hashlib.md5(request.encode()).hexdigest()
        
        # Check cache first
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Process and cache result
        response = await self.llm.agenerate([request])
        self.cache[cache_key] = response.content
        
        return response.content
```

## Environment Management

### Development Environment
- **Local development**: Docker Compose for local services
- **Hot reloading**: Automatic code reloading during development
- **Debug mode**: Enhanced logging and debugging

```yaml
# docker-compose.dev.yml
version: '3.8'
services:
  agent:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=true
      - LOG_LEVEL=debug
    depends_on:
      - redis
      - postgres
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
  
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: agent_db
      POSTGRES_USER: agent
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
```

### Staging Environment
- **Production replica**: Mirror production configuration
- **Integration testing**: End-to-end testing environment
- **Performance testing**: Load and stress testing

```python
# staging configuration
class StagingConfig(AgentConfig):
    """Staging environment configuration."""
    
    environment: str = "staging"
    debug: bool = False
    log_level: str = "info"
    
    # Use smaller models for cost efficiency
    model_name: str = "gpt-3.5-turbo"
    
    # Reduced scaling for staging
    max_workers: int = 2
    timeout: int = 30
```

### Production Environment
- **High availability**: Multi-region deployment
- **Monitoring**: Comprehensive observability
- **Security**: Enhanced security measures

```python
class ProductionConfig(AgentConfig):
    """Production environment configuration."""
    
    environment: str = "production"
    debug: bool = False
    log_level: str = "warning"
    
    # Production-grade models
    model_name: str = "gpt-4"
    
    # Production scaling
    max_workers: int = 10
    timeout: int = 60
    
    # Security settings
    rate_limit: int = 100  # requests per minute
    require_auth: bool = True
```

## Monitoring and Observability

### Health Checks
- **Readiness probes**: Check if agent is ready to serve
- **Liveness probes**: Check if agent is healthy
- **Custom metrics**: Agent-specific health indicators

```python
from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, Histogram, generate_latest

app = FastAPI()

# Metrics
request_count = Counter("agent_requests_total", "Total agent requests")
request_duration = Histogram("agent_request_duration_seconds", "Request duration")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        # Check dependencies
        await redis_client.ping()
        await db_client.execute("SELECT 1")
        
        # Check model availability
        test_response = await llm.agenerate(["test"])
        
        return {"status": "healthy", "timestamp": datetime.utcnow()}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Unhealthy: {str(e)}")

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint."""
    return Response(generate_latest(), media_type="text/plain")
```

### Logging Strategy
- **Structured logging**: JSON format for machine processing
- **Request tracing**: Track requests across services
- **Error tracking**: Detailed error reporting

```python
import structlog
from typing import Any, Dict

logger = structlog.get_logger()

class AgentLogger:
    """Structured logging for agents."""
    
    @staticmethod
    def log_request(request_id: str, user_id: str, message: str) -> None:
        """Log incoming request."""
        logger.info(
            "agent_request",
            request_id=request_id,
            user_id=user_id,
            message_length=len(message),
            timestamp=datetime.utcnow().isoformat()
        )
    
    @staticmethod
    def log_response(request_id: str, response: str, duration: float) -> None:
        """Log agent response."""
        logger.info(
            "agent_response",
            request_id=request_id,
            response_length=len(response),
            duration_seconds=duration,
            timestamp=datetime.utcnow().isoformat()
        )
    
    @staticmethod
    def log_error(request_id: str, error: Exception) -> None:
        """Log agent error."""
        logger.error(
            "agent_error",
            request_id=request_id,
            error_type=type(error).__name__,
            error_message=str(error),
            timestamp=datetime.utcnow().isoformat()
        )
```

## Security Patterns

### Authentication and Authorization
- **API keys**: Secure API key management
- **JWT tokens**: Token-based authentication
- **Role-based access**: Different access levels

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Verify JWT token."""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/agent/chat")
async def chat_endpoint(
    request: ChatRequest,
    user_id: str = Depends(verify_token)
) -> ChatResponse:
    """Authenticated chat endpoint."""
    return await agent.process_chat(request, user_id)
```

### Rate Limiting
- **Request throttling**: Limit requests per user/IP
- **Resource protection**: Prevent abuse
- **Fair usage**: Ensure equitable access

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/agent/chat")
@limiter.limit("10/minute")
async def chat_endpoint(request: Request, chat_request: ChatRequest):
    """Rate-limited chat endpoint."""
    return await agent.process_chat(chat_request)
```

## Best Practices

### Configuration Management
1. **Never commit secrets** to version control
2. **Use environment variables** for all configuration
3. **Validate configuration** at startup
4. **Provide sensible defaults** where possible

### Deployment Safety
1. **Blue-green deployments** for zero downtime
2. **Canary releases** for gradual rollouts
3. **Rollback procedures** for quick recovery
4. **Health checks** before traffic routing

### Performance Optimization
1. **Connection pooling** for external services
2. **Response caching** for repeated queries
3. **Async operations** for I/O bound tasks
4. **Resource monitoring** and optimization

### Error Handling
1. **Graceful degradation** when services fail
2. **Circuit breakers** for external dependencies
3. **Retry mechanisms** with exponential backoff
4. **Comprehensive error logging**

## Related Concepts

- [[12-factor-agents]] - Core methodology overview
- [[human-in-the-loop]] - Human oversight patterns
- [[stateless-agent-design]] - Stateless architecture principles
- [[pause-resume-workflows]] - Workflow interruption handling
- [[production-deployment]] - General deployment strategies
- [[observability]] - Monitoring and debugging
- [[mlops]] - ML operations practices

## Tools and Platforms

- **Container Orchestration**: Kubernetes, Docker Swarm, ECS
- **Service Mesh**: Istio, Linkerd, Consul Connect
- **Monitoring**: Prometheus, Grafana, DataDog, New Relic
- **Logging**: ELK Stack, Fluentd, Splunk
- **Secrets Management**: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins, ArgoCD

## Implementation Guide

### Phase 1: Basic Deployment
1. Containerize your agent application
2. Set up basic health checks
3. Configure environment-based settings
4. Implement basic logging

### Phase 2: Production Readiness
1. Add comprehensive monitoring
2. Implement security measures
3. Set up CI/CD pipelines
4. Configure auto-scaling

### Phase 3: Advanced Patterns
1. Implement blue-green deployments
2. Add circuit breakers and retries
3. Set up distributed tracing
4. Optimize for performance

---

*Agent deployment patterns ensure reliable, scalable, and maintainable LLM agent applications in production environments.*
