I'll represent the step-by-step tree construction using Mermaid diagrams for the tokens `["(", "a", "(", "b", "c", ")", "d", ")"]`.

1. Initial state (create root):
```mermaid
graph TD
    R[root]
```

2. After processing "(" (first parenthesis):
```mermaid
graph TD
    R[root] --> P1["()"]
```

3. After processing "a":
```mermaid
graph TD
    R[root] --> P1["()"]
    P1 --> A[a]
```

4. After processing second "(":
```mermaid
graph TD
    R[root] --> P1["()"]
    P1 --> A[a]
    P1 --> P2["()"]
```

5. After processing "b":
```mermaid
graph TD
    R[root] --> P1["()"]
    P1 --> A[a]
    P1 --> P2["()"]
    P2 --> B[b]
```

6. After processing "c":
```mermaid
graph TD
    R[root] --> P1["()"]
    P1 --> A[a]
    P1 --> P2["()"]
    P2 --> B[b]
    P2 --> C[c]
```

7. After processing ")" (moves current pointer back to P1):
```mermaid
graph TD
    R[root] --> P1["()"]
    P1 --> A[a]
    P1 --> P2["()"]
    P2 --> B[b]
    P2 --> C[c]
```

8. After processing "d":
```mermaid
graph TD
    R[root] --> P1["()"]
    P1 --> A[a]
    P1 --> P2["()"]
    P2 --> B[b]
    P2 --> C[c]
    P1 --> D[d]
```

9. Final state after processing last ")":
```mermaid
graph TD
    R[root] --> P1["()"]
    P1 --> A[a]
    P1 --> P2["()"]
    P2 --> B[b]
    P2 --> C[c]
    P1 --> D[d]
```

Key points to note:
- The `current` pointer moves down when processing "("
- The `current` pointer moves up when processing ")"
- Regular tokens (a, b, c, d) are added as children to the current node
- Parent references are maintained but not shown in the diagrams
- The final tree structure represents the nested expression `(a(bc)d)`

This visualization helps understand how the parser builds the tree structure by tracking the current position and managing parent-child relationships.