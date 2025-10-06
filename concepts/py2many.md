# py2many

## Universal Python Transpiler

py2many is an open-source Python transpiler that converts Python source code into multiple statically-typed programming languages, enabling developers to write once in Python and deploy across various language ecosystems.

**Repository:** [https://github.com/py2many/py2many](https://github.com/py2many/py2many)

---

## 🎯 Purpose & Use Cases

- **Performance Optimization:** Transpile Python algorithms to Rust, C++, or Go for significant speed improvements while maintaining Python's development experience
- **Security Enhancement:** Write security-sensitive code in Python, verify with tests, then transpile to safer systems languages like Rust
- **Cross-Platform Development:** Accelerate Python code by transpiling to native extensions or standalone applications
- **Mobile & Systems Programming:** Alternative to multi-platform solutions by writing in Python and deploying to multiple targets
- **Educational Tool:** Learn new programming languages by comparing Python implementations with transpiled equivalents

---

## 🛠️ Key Features

- **Multi-Language Support:** Converts Python to 8+ programming languages
- **Type Inference:** Automatically infers and converts Python types to target language types
- **Performance Optimization:** Generates optimized code for systems programming languages
- **Cross-Platform:** Works on Linux, macOS, and Windows
- **Open Source:** MIT licensed with active community development

---

## 🌐 Supported Languages & Status

- **Primary Focus:** Python to Rust (most mature feature set and active development)
- **Production Ready:** Python to C++ (C++14 historically supported, C++17+ required for advanced features)
- **Beta Support:** Python to Julia, Kotlin, Nim, Go, Dart, D, V, Zig, Mojo
- **Enhanced Python:** Can emit enhanced Python 3 code with inferred type annotations

---

## 🔧 How It Works

py2many uses Python's Abstract Syntax Tree (AST) to parse Python code and transform it into equivalent code in target languages. The transpilation process includes:

1. **AST Parsing:** Analyzes Python source code structure
2. **Type Inference:** Determines variable and function types
3. **Code Generation:** Produces idiomatic code in target languages
4. **Optimization:** Applies language-specific optimizations and best practices

---

## 📝 Usage Examples

```bash
# Install py2many
pip3 install py2many

# Convert Python to Rust
py2many --rust=1 tests/cases/fib.py

# Convert Python to C++
py2many --cpp=1 tests/cases/fib.py

# Convert Python to Go
py2many --go=1 tests/cases/fib.py
```

**Example Transpilation (Python to Rust):**

```python
def fib(i: int) -> int:
    if i == 0 or i == 1:
        return 1
    return fib(i - 1) + fib(i - 2)
```

Becomes:

```rust
fn fib(i: i32) -> i32 {
    if i == 0 || i == 1 {
        return 1;
    }
    return fib(i - 1) + fib(i - 2);
}
```

---

## 🔗 Related Concepts

- [Frameworks](./frameworks.md) — Development frameworks and tools
- [Python](./python.md) — Python programming language concepts
- [Rust](./rust.md) — Rust programming language
- [Go](./go.md) — Go programming language

---

## 📚 Resources & Links

- **Official Repository:** [https://github.com/py2many/py2many](https://github.com/py2many/py2many)
- **Documentation:** [README.md](https://github.com/py2many/py2many#readme)
- **Examples:** [tests/expected](https://github.com/adsharma/py2many/tree/main/tests/expected)
- **Contributing:** [CONTRIBUTING.md](https://github.com/adsharma/py2many/blob/main/CONTRIBUTING.md)

[Back to Concepts Hub](./README.md)
