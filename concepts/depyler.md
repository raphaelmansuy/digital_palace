# Depyler

Depyler is a Python-to-Rust transpiler with semantic verification and memory safety analysis. It translates annotated Python code into idiomatic Rust, preserving program semantics while providing compile-time safety guarantees. Depyler helps developers transition from Python to more energy-efficient and memory-safe Rust code.

---

## Key Features

- **Type-Directed Transpilation:** Uses Python type annotations to generate appropriate Rust types
- **Memory Safety Analysis:** Infers ownership and borrowing patterns for safe Rust code
- **Semantic Verification:** Property-based testing to verify behavioral equivalence between Python and Rust versions
- **MCP Integration:** Model Context Protocol server for AI assistant integration
- **Multiple Backends:** Generate Rust or Ruchy script code
- **Quality Standards:** High test coverage (70%+), zero clippy warnings, comprehensive documentation

---

## Supported Python Features

### Currently Supported

- Functions with type annotations
- Basic types (int, float, str, bool)
- Collections (List, Dict, Tuple, Set)
- Control flow (if, while, for, match)
- List/dict/set comprehensions
- Exception handling (mapped to Result<T, E>)
- Classes and methods
- Async/await (basic)
- Context managers (with statements)
- Iterators

### Not Supported

- Dynamic features (eval, exec)
- Runtime reflection
- Multiple inheritance
- Monkey patching

---

## Installation

```bash
cargo install depyler
```

**Requirements:**

- Rust 1.83.0 or later
- Python 3.8+ (for test validation)

---

## Usage

### Basic Transpilation

```bash
# Transpile a Python file to Rust
depyler transpile example.py
```

### With Semantic Verification

```bash
# Transpile with semantic verification
depyler transpile example.py --verify
```

### Analyze Migration Complexity

```bash
# Analyze migration complexity
depyler analyze example.py
```

### Library Usage

```rust
use depyler::{transpile_file, TranspileOptions};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let options = TranspileOptions::default()
        .with_verification(true);

    let rust_code = transpile_file("example.py", options)?;
    println!("{}", rust_code);

    Ok(())
}
```

### MCP Integration

Add to Claude Desktop config (`~/.config/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "depyler": {
      "command": "depyler",
      "args": ["agent", "start", "--foreground", "--port", "3000"]
    }
  }
}
```

Available MCP tools:

- `transpile_python` - Convert Python code to Rust
- `analyze_migration_complexity` - Analyze migration effort
- `verify_transpilation` - Verify semantic equivalence
- `pmat_quality_check` - Code quality analysis

---

## Example

**Input (`example.py`):**

```python
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Output (`example.rs`):**

```rust
fn fibonacci(n: i32) -> i32 {
    if n <= 1 {
        return n;
    }
    fibonacci(n - 1) + fibonacci(n - 2)
}
```

---

## Architecture

Depyler uses a multi-stage compilation pipeline:

```text
Python AST → HIR → Type Inference → Rust AST → Code Generation
```

Key components:

- **Parser:** RustPython AST parser
- **HIR:** High-level intermediate representation
- **Type System:** Conservative type inference with annotation support
- **Verification:** Property-based testing for semantic equivalence
- **Codegen:** Rust code generation via syn/quote

---

## Quality Standards

- Test coverage: 70%+ (596 passing tests)
- Max cyclomatic complexity: ≤20
- Zero clippy warnings (`-D warnings`)
- Zero self-admitted technical debt (SATD)
- TDG grade: A+ (99.1/100)

---

## Development

### Running Tests

```bash
# Run all tests
cargo test --workspace

# Run with coverage
cargo llvm-cov --html --open

# Run benchmarks
cargo bench
```

### Quality Checks

```bash
# Lint
cargo clippy --all-targets --all-features -- -D warnings

# Format
cargo fmt --all
```

---

## External Links

- [Depyler GitHub Repository](https://github.com/paiml/depyler)
- [Crates.io Package](https://crates.io/crates/depyler)
- [API Documentation](https://docs.rs/depyler)
- [MCP Quickstart Guide](https://github.com/paiml/depyler/blob/main/docs/MCP_QUICKSTART.md)
- [Agent Mode Guide](https://github.com/paiml/depyler/blob/main/AGENT.md)

---

## See Also

- [Frameworks](./frameworks.md)
- [Model Compression](./model-compression.md)
- [Production Deployment](./production-deployment.md)
- [MCP](./mcp.md)

---

## License

Licensed under either of:

- Apache License, Version 2.0
- MIT license

[Back to Concepts Hub](./README.md)
