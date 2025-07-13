# Pause and Resume Workflows 🔄

> Implementing stateful workflow interruption and continuation patterns for LLM agents

## Overview

Pause and resume workflows enable LLM agents to handle long-running tasks that may require interruption, human intervention, or resource optimization. This pattern is essential for production agents that need to manage complex, multi-step processes reliably.

## Core Concepts

### Workflow State Management
- **Checkpointing**: Save workflow state at strategic points
- **State serialization**: Persist workflow context and progress
- **Recovery mechanisms**: Resume from saved checkpoints

### Interruption Patterns
- **Graceful pausing**: Clean workflow suspension
- **External triggers**: Human or system-initiated pauses
- **Resource management**: Optimal resource usage during pauses

## Implementation Patterns

### 1. Checkpoint-Based Workflows

```python
from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from enum import Enum
import json
import asyncio
from datetime import datetime

class WorkflowStatus(Enum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class WorkflowCheckpoint:
    """Workflow state checkpoint."""
    workflow_id: str
    step_index: int
    step_name: str
    state: Dict[str, Any]
    timestamp: datetime
    status: WorkflowStatus
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize checkpoint to dictionary."""
        return {
            "workflow_id": self.workflow_id,
            "step_index": self.step_index,
            "step_name": self.step_name,
            "state": self.state,
            "timestamp": self.timestamp.isoformat(),
            "status": self.status.value
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WorkflowCheckpoint":
        """Deserialize checkpoint from dictionary."""
        return cls(
            workflow_id=data["workflow_id"],
            step_index=data["step_index"],
            step_name=data["step_name"],
            state=data["state"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            status=WorkflowStatus(data["status"])
        )

class PausableWorkflow:
    """Base class for pausable workflows."""
    
    def __init__(self, workflow_id: str, storage: WorkflowStorage):
        self.workflow_id = workflow_id
        self.storage = storage
        self.current_step = 0
        self.state = {}
        self.status = WorkflowStatus.CREATED
        self.pause_requested = False
    
    async def save_checkpoint(self, step_name: str) -> None:
        """Save workflow checkpoint."""
        checkpoint = WorkflowCheckpoint(
            workflow_id=self.workflow_id,
            step_index=self.current_step,
            step_name=step_name,
            state=self.state.copy(),
            timestamp=datetime.utcnow(),
            status=self.status
        )
        await self.storage.save_checkpoint(checkpoint)
    
    async def load_checkpoint(self) -> Optional[WorkflowCheckpoint]:
        """Load latest workflow checkpoint."""
        return await self.storage.load_latest_checkpoint(self.workflow_id)
    
    async def pause(self) -> None:
        """Request workflow pause."""
        self.pause_requested = True
        self.status = WorkflowStatus.PAUSED
        await self.save_checkpoint("paused")
    
    async def resume(self) -> None:
        """Resume paused workflow."""
        checkpoint = await self.load_checkpoint()
        if checkpoint and checkpoint.status == WorkflowStatus.PAUSED:
            self.current_step = checkpoint.step_index
            self.state = checkpoint.state
            self.status = WorkflowStatus.RUNNING
            self.pause_requested = False
            await self.execute_from_checkpoint()
    
    async def execute_from_checkpoint(self) -> None:
        """Execute workflow from current checkpoint."""
        steps = self.get_workflow_steps()
        
        while self.current_step < len(steps) and not self.pause_requested:
            step = steps[self.current_step]
            
            try:
                # Execute step
                await self.execute_step(step)
                
                # Save checkpoint after successful step
                await self.save_checkpoint(step.name)
                
                self.current_step += 1
                
            except Exception as e:
                self.status = WorkflowStatus.FAILED
                await self.save_checkpoint(f"failed_at_{step.name}")
                raise
        
        if not self.pause_requested:
            self.status = WorkflowStatus.COMPLETED
            await self.save_checkpoint("completed")
    
    def get_workflow_steps(self) -> List[WorkflowStep]:
        """Define workflow steps - to be implemented by subclasses."""
        raise NotImplementedError
    
    async def execute_step(self, step: 'WorkflowStep') -> None:
        """Execute a single workflow step."""
        raise NotImplementedError
```

### 2. Step-Based Workflow Engine

```python
from abc import ABC, abstractmethod
from typing import Callable, Any

class WorkflowStep(ABC):
    """Abstract workflow step."""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
    
    @abstractmethod
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the workflow step."""
        pass
    
    async def can_pause_after(self) -> bool:
        """Check if workflow can be paused after this step."""
        return True

class ResearchWorkflowStep(WorkflowStep):
    """Research step in a workflow."""
    
    def __init__(self, query: str, sources: List[str]):
        super().__init__("research", f"Research: {query}")
        self.query = query
        self.sources = sources
    
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute research step."""
        # Simulate research operation
        research_results = await self.perform_research(self.query, self.sources)
        
        context["research_results"] = research_results
        context["research_query"] = self.query
        
        return context
    
    async def perform_research(self, query: str, sources: List[str]) -> Dict[str, Any]:
        """Perform research operation."""
        # Implementation details...
        return {"findings": f"Research results for: {query}"}

class AnalysisWorkflowStep(WorkflowStep):
    """Analysis step in a workflow."""
    
    def __init__(self, analysis_type: str):
        super().__init__("analysis", f"Analysis: {analysis_type}")
        self.analysis_type = analysis_type
    
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute analysis step."""
        research_results = context.get("research_results", {})
        
        # Simulate analysis operation
        analysis_results = await self.perform_analysis(research_results)
        
        context["analysis_results"] = analysis_results
        context["analysis_type"] = self.analysis_type
        
        return context
    
    async def perform_analysis(self, research_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform analysis operation."""
        # Implementation details...
        return {"insights": "Key insights from analysis"}

class ContentGenerationWorkflowStep(WorkflowStep):
    """Content generation step."""
    
    def __init__(self, content_type: str, template: str):
        super().__init__("content_generation", f"Generate: {content_type}")
        self.content_type = content_type
        self.template = template
    
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute content generation step."""
        analysis_results = context.get("analysis_results", {})
        
        # Generate content based on analysis
        content = await self.generate_content(analysis_results, self.template)
        
        context["generated_content"] = content
        context["content_type"] = self.content_type
        
        return context
    
    async def generate_content(self, analysis: Dict[str, Any], template: str) -> str:
        """Generate content using LLM."""
        # Implementation details...
        return f"Generated content based on {analysis}"
```

### 3. Research Agent Workflow Example

```python
class ResearchAgentWorkflow(PausableWorkflow):
    """Multi-step research agent workflow."""
    
    def __init__(self, workflow_id: str, storage: WorkflowStorage, 
                 research_query: str, output_format: str):
        super().__init__(workflow_id, storage)
        self.research_query = research_query
        self.output_format = output_format
        self.state = {
            "research_query": research_query,
            "output_format": output_format,
            "start_time": datetime.utcnow().isoformat()
        }
    
    def get_workflow_steps(self) -> List[WorkflowStep]:
        """Define research workflow steps."""
        return [
            ResearchWorkflowStep(
                query=self.research_query,
                sources=["web", "academic", "internal_docs"]
            ),
            AnalysisWorkflowStep("comprehensive_analysis"),
            WorkflowStep("human_review", "Human review checkpoint"),
            ContentGenerationWorkflowStep(
                content_type=self.output_format,
                template="research_report_template"
            ),
            WorkflowStep("quality_check", "Final quality check"),
            WorkflowStep("delivery", "Deliver final results")
        ]
    
    async def execute_step(self, step: WorkflowStep) -> None:
        """Execute workflow step with pause checks."""
        print(f"Executing step: {step.name}")
        
        # Check for pause request before execution
        if self.pause_requested:
            return
        
        # Execute step based on type
        if isinstance(step, (ResearchWorkflowStep, AnalysisWorkflowStep, ContentGenerationWorkflowStep)):
            self.state = await step.execute(self.state)
        elif step.name == "human_review":
            await self.handle_human_review_step()
        elif step.name == "quality_check":
            await self.handle_quality_check_step()
        elif step.name == "delivery":
            await self.handle_delivery_step()
        
        # Simulate processing time
        await asyncio.sleep(1)
    
    async def handle_human_review_step(self) -> None:
        """Handle human review checkpoint."""
        # Pause for human review
        self.state["review_requested"] = True
        self.state["review_content"] = self.state.get("analysis_results", {})
        
        # Automatically pause workflow for human intervention
        await self.pause()
        print("Workflow paused for human review")
    
    async def handle_quality_check_step(self) -> None:
        """Handle quality check step."""
        content = self.state.get("generated_content", "")
        
        # Simulate quality metrics
        quality_score = len(content) / 100  # Simple metric
        self.state["quality_score"] = quality_score
        
        if quality_score < 0.8:
            # Pause for quality improvement
            self.state["quality_issue"] = True
            await self.pause()
            print("Workflow paused for quality improvement")
    
    async def handle_delivery_step(self) -> None:
        """Handle final delivery step."""
        self.state["delivery_time"] = datetime.utcnow().isoformat()
        self.state["final_output"] = self.state.get("generated_content", "")
        print("Research workflow completed successfully")
```

### 4. Workflow Storage Interface

```python
from abc import ABC, abstractmethod

class WorkflowStorage(ABC):
    """Abstract workflow storage interface."""
    
    @abstractmethod
    async def save_checkpoint(self, checkpoint: WorkflowCheckpoint) -> None:
        """Save workflow checkpoint."""
        pass
    
    @abstractmethod
    async def load_latest_checkpoint(self, workflow_id: str) -> Optional[WorkflowCheckpoint]:
        """Load latest checkpoint for workflow."""
        pass
    
    @abstractmethod
    async def load_checkpoint_history(self, workflow_id: str) -> List[WorkflowCheckpoint]:
        """Load checkpoint history for workflow."""
        pass

class RedisWorkflowStorage(WorkflowStorage):
    """Redis-based workflow storage."""
    
    def __init__(self, redis_client):
        self.redis = redis_client
    
    async def save_checkpoint(self, checkpoint: WorkflowCheckpoint) -> None:
        """Save checkpoint to Redis."""
        key = f"workflow:{checkpoint.workflow_id}:checkpoints"
        value = json.dumps(checkpoint.to_dict())
        
        # Save latest checkpoint
        await self.redis.set(f"workflow:{checkpoint.workflow_id}:latest", value)
        
        # Add to checkpoint history
        await self.redis.lpush(key, value)
        
        # Keep only last 100 checkpoints
        await self.redis.ltrim(key, 0, 99)
    
    async def load_latest_checkpoint(self, workflow_id: str) -> Optional[WorkflowCheckpoint]:
        """Load latest checkpoint from Redis."""
        value = await self.redis.get(f"workflow:{workflow_id}:latest")
        if value:
            data = json.loads(value)
            return WorkflowCheckpoint.from_dict(data)
        return None
    
    async def load_checkpoint_history(self, workflow_id: str) -> List[WorkflowCheckpoint]:
        """Load checkpoint history from Redis."""
        values = await self.redis.lrange(f"workflow:{workflow_id}:checkpoints", 0, -1)
        checkpoints = []
        for value in values:
            data = json.loads(value)
            checkpoints.append(WorkflowCheckpoint.from_dict(data))
        return checkpoints
```

## Advanced Patterns

### 1. Conditional Pause Points

```python
class ConditionalPauseWorkflow(PausableWorkflow):
    """Workflow with conditional pause points."""
    
    def __init__(self, workflow_id: str, storage: WorkflowStorage, pause_conditions: Dict[str, Callable]):
        super().__init__(workflow_id, storage)
        self.pause_conditions = pause_conditions
    
    async def execute_step(self, step: WorkflowStep) -> None:
        """Execute step with conditional pausing."""
        # Execute the step
        await super().execute_step(step)
        
        # Check pause conditions
        for condition_name, condition_func in self.pause_conditions.items():
            if await condition_func(self.state, step):
                self.state["pause_reason"] = condition_name
                await self.pause()
                break

# Example usage
async def cost_threshold_condition(state: Dict[str, Any], step: WorkflowStep) -> bool:
    """Pause if cost threshold exceeded."""
    total_cost = state.get("total_cost", 0)
    return total_cost > 10.0

async def time_limit_condition(state: Dict[str, Any], step: WorkflowStep) -> bool:
    """Pause if time limit exceeded."""
    start_time = datetime.fromisoformat(state.get("start_time", datetime.utcnow().isoformat()))
    elapsed = datetime.utcnow() - start_time
    return elapsed.total_seconds() > 3600  # 1 hour limit

workflow = ConditionalPauseWorkflow(
    workflow_id="conditional_research",
    storage=redis_storage,
    pause_conditions={
        "cost_threshold": cost_threshold_condition,
        "time_limit": time_limit_condition
    }
)
```

### 2. Parallel Workflow Branches

```python
class ParallelBranchWorkflow(PausableWorkflow):
    """Workflow with parallel execution branches."""
    
    def __init__(self, workflow_id: str, storage: WorkflowStorage):
        super().__init__(workflow_id, storage)
        self.branch_states = {}
    
    async def execute_parallel_branches(self, branches: Dict[str, List[WorkflowStep]]) -> None:
        """Execute multiple workflow branches in parallel."""
        tasks = []
        
        for branch_name, branch_steps in branches.items():
            task = asyncio.create_task(
                self.execute_branch(branch_name, branch_steps)
            )
            tasks.append(task)
        
        # Wait for all branches to complete or pause
        await asyncio.gather(*tasks, return_exceptions=True)
    
    async def execute_branch(self, branch_name: str, steps: List[WorkflowStep]) -> None:
        """Execute a single workflow branch."""
        self.branch_states[branch_name] = {"current_step": 0, "status": "running"}
        
        for i, step in enumerate(steps):
            if self.pause_requested:
                self.branch_states[branch_name]["status"] = "paused"
                break
            
            try:
                # Execute step with branch-specific state
                branch_state = self.state.get(f"branch_{branch_name}", {})
                updated_state = await step.execute(branch_state)
                self.state[f"branch_{branch_name}"] = updated_state
                
                self.branch_states[branch_name]["current_step"] = i + 1
                
                # Save checkpoint after each step
                await self.save_checkpoint(f"{branch_name}_{step.name}")
                
            except Exception as e:
                self.branch_states[branch_name]["status"] = "failed"
                self.branch_states[branch_name]["error"] = str(e)
                break
        
        if not self.pause_requested:
            self.branch_states[branch_name]["status"] = "completed"
```

### 3. Workflow Orchestration

```python
class WorkflowOrchestrator:
    """Orchestrates multiple pausable workflows."""
    
    def __init__(self, storage: WorkflowStorage):
        self.storage = storage
        self.active_workflows: Dict[str, PausableWorkflow] = {}
    
    async def start_workflow(self, workflow: PausableWorkflow) -> None:
        """Start a new workflow."""
        self.active_workflows[workflow.workflow_id] = workflow
        workflow.status = WorkflowStatus.RUNNING
        await workflow.save_checkpoint("started")
        
        # Execute workflow in background
        asyncio.create_task(workflow.execute_from_checkpoint())
    
    async def pause_workflow(self, workflow_id: str) -> bool:
        """Pause a running workflow."""
        if workflow_id in self.active_workflows:
            workflow = self.active_workflows[workflow_id]
            await workflow.pause()
            return True
        return False
    
    async def resume_workflow(self, workflow_id: str) -> bool:
        """Resume a paused workflow."""
        # Load workflow from storage
        checkpoint = await self.storage.load_latest_checkpoint(workflow_id)
        if checkpoint and checkpoint.status == WorkflowStatus.PAUSED:
            # Recreate and resume workflow
            workflow = await self.recreate_workflow(checkpoint)
            self.active_workflows[workflow_id] = workflow
            await workflow.resume()
            return True
        return False
    
    async def get_workflow_status(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """Get current workflow status."""
        if workflow_id in self.active_workflows:
            workflow = self.active_workflows[workflow_id]
            return {
                "workflow_id": workflow_id,
                "status": workflow.status.value,
                "current_step": workflow.current_step,
                "state": workflow.state
            }
        
        # Check storage for stopped workflows
        checkpoint = await self.storage.load_latest_checkpoint(workflow_id)
        if checkpoint:
            return {
                "workflow_id": workflow_id,
                "status": checkpoint.status.value,
                "current_step": checkpoint.step_index,
                "last_updated": checkpoint.timestamp.isoformat()
            }
        
        return None
    
    async def recreate_workflow(self, checkpoint: WorkflowCheckpoint) -> PausableWorkflow:
        """Recreate workflow from checkpoint."""
        # This would typically involve workflow factory pattern
        # For demonstration, assuming ResearchAgentWorkflow
        workflow = ResearchAgentWorkflow(
            workflow_id=checkpoint.workflow_id,
            storage=self.storage,
            research_query=checkpoint.state.get("research_query", ""),
            output_format=checkpoint.state.get("output_format", "report")
        )
        
        # Restore state
        workflow.current_step = checkpoint.step_index
        workflow.state = checkpoint.state
        workflow.status = checkpoint.status
        
        return workflow
```

## Best Practices

### 1. Checkpoint Strategy
- **Frequent checkpoints**: Save state after each significant operation
- **Atomic operations**: Ensure checkpoint consistency
- **Cleanup policies**: Remove old checkpoints to manage storage

### 2. Resource Management
- **Resource cleanup**: Clean up resources during pause
- **Connection management**: Close database/API connections properly
- **Memory optimization**: Minimize state size in checkpoints

### 3. Error Handling
- **Graceful failures**: Handle errors during pause/resume operations
- **Rollback mechanisms**: Ability to rollback to previous checkpoints
- **Notification systems**: Alert operators of workflow failures

### 4. Monitoring
- **Workflow metrics**: Track execution times, pause frequency
- **Health checks**: Monitor workflow health and progress
- **Logging**: Comprehensive logging for debugging

## Use Cases

### Long-Running Research Tasks
- Multi-step data collection and analysis
- Human review checkpoints
- Cost-aware processing

### Content Generation Pipelines
- Research → Analysis → Writing → Review cycles
- Quality checkpoints
- Approval workflows

### Data Processing Workflows
- ETL operations with validation steps
- Error recovery and retries
- Resource optimization

### Agent Collaboration
- Multi-agent workflows with handoffs
- Synchronization points
- Conflict resolution

## Related Concepts

- [[human-in-the-loop]] - Human intervention patterns
- [[agent-deployment-patterns]] - Production deployment strategies
- [[stateless-agent-design]] - Stateless architecture principles
- [[workflow-automation]] - General workflow concepts
- [[observability]] - Monitoring workflow execution
- [[production-deployment]] - Production considerations

## Tools and Libraries

- **Workflow Engines**: Temporal, Airflow, Prefect
- **State Management**: Redis, PostgreSQL, DynamoDB
- **Orchestration**: Kubernetes Jobs, AWS Step Functions
- **Monitoring**: Prometheus, Grafana, DataDog

---

*Pause and resume workflows enable robust, interruptible agent processes that can handle complex, long-running tasks with reliability and efficiency.*
