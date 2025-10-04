# Bun

**Bun** is a fast JavaScript runtime, package manager, bundler, and test runner designed as a drop-in replacement for Node.js. It provides a complete toolkit for building, testing, and deploying JavaScript and TypeScript applications with exceptional performance and developer experience.

## Key Features

- **Fast Runtime**: Uses JavaScriptCore engine for rapid startup and execution times
- **All-in-One Toolkit**: Package manager, test runner, bundler, and runtime in one
- **Node.js Compatible**: Drop-in replacement with 100% Node.js API compatibility
- **TypeScript First**: Native TypeScript and JSX support without configuration
- **Built-in APIs**: Extensive native APIs for common tasks like HTTP servers, databases, and file operations

## Core Advantages

### **Performance & Speed**

- **Rapid Startup**: JavaScriptCore provides significantly faster cold start times than V8
- **High-Performance APIs**: Native implementations of HTTP, WebSocket, and database drivers
- **Optimized Package Management**: 10-30x faster than npm, yarn, and pnpm
- **Efficient Bundling**: Fast production-ready code bundling for frontend and backend

### **Developer Experience**

- **Unified Workflow**: Single tool for development, testing, building, and deployment
- **Zero Configuration**: TypeScript, JSX, and module resolution work out of the box
- **Cross-Platform Shell**: Native bash-like shell API for scripting and automation
- **Jest-Compatible Testing**: Drop-in replacement for Jest with superior performance

## Implementation Patterns

### **Basic HTTP Server**

```typescript
const server = Bun.serve({
  port: 3000,
  fetch(request) {
    return new Response("Hello from Bun!");
  },
});

console.log(`Server running at http://localhost:${server.port}`);
```

### **File System Operations**

```typescript
// Read a file
const file = Bun.file("data.json");
const data = await file.json();

// Write a file
await Bun.write("output.txt", "Hello, World!");

// Read directory
const files = await Bun.readdir("src");
```

### **Database Operations**

```typescript
// SQLite
const db = new Bun.sqlite("app.db");
const users = db.query("SELECT * FROM users").all();

// PostgreSQL
import { sql } from "bun";

const users = await sql`SELECT * FROM users LIMIT 10`;
```

### **Dependency Management**

```bash
# Install dependencies (30x faster than npm)
bun install

# Add a package
bun add react

# Run scripts
bun run dev

# Execute packages
bunx create-react-app my-app
```

### **Testing**

```typescript
import { expect, test, describe } from "bun:test";

describe("Math operations", () => {
  test("addition", () => {
    expect(2 + 2).toBe(4);
  });

  test("async operations", async () => {
    const result = await Promise.resolve(42);
    expect(result).toBe(42);
  });
});
```

### **Bundling**

```typescript
await Bun.build({
  entrypoints: ["./src/index.ts"],
  outdir: "./dist",
  target: "browser",
  minify: true,
});
```

### **Shell Scripting**

```typescript
// Cross-platform shell commands
const result = await $`ls -la`;
console.log(result.stdout);

// Piping and chaining
await $`cat file.txt | grep "search" | wc -l`;
```

## Tools & Ecosystem

### **Official Resources**

- **[Bun Documentation](https://bun.com/docs/)** - Comprehensive official documentation
- **[GitHub Repository](https://github.com/oven-sh/bun)** - Source code and issue tracking
- **[Guides](https://bun.com/guides/)** - Practical guides and examples
- **[Blog](https://bun.com/blog/)** - Latest updates and announcements

### **Built-in Tools**

- **Package Manager**: `bun install` - npm-compatible with superior performance
- **Test Runner**: `bun test` - Jest-compatible testing framework
- **Bundler**: `bun build` - Production-ready code bundling
- **Runtime**: `bun run` - Fast JavaScript/TypeScript execution

## Use Cases

### **Web Development**

- **Full-Stack Applications**: Single runtime for frontend and backend
- **API Servers**: High-performance HTTP and WebSocket servers
- **Real-time Applications**: Built-in WebSocket support for live features
- **Static Site Generation**: Fast bundling for modern web frameworks

### **Backend Services**

- **Microservices**: Lightweight, fast-starting service containers
- **Database Applications**: Native drivers for SQLite, PostgreSQL, and Redis
- **CLI Tools**: Cross-platform command-line applications
- **Automation Scripts**: Shell scripting and process automation

### **Development Workflow**

- **Monorepo Management**: Workspace support for large codebases
- **Testing Infrastructure**: Fast, reliable test execution
- **Build Pipelines**: Efficient bundling and optimization
- **Deployment**: Single-file executables for easy distribution

## Performance Optimization

### **Runtime Optimization**
```typescript
// Use Bun's native APIs for best performance
const server = Bun.serve({
  port: 3000,
  fetch: handler,
  // Enable HTTP/2
  tls: {
    key: Bun.file("key.pem"),
    cert: Bun.file("cert.pem"),
  },
});
```

### **Package Management**
```bash
# Use global cache for faster installs
bun install

# Lockfile optimization
bun install --frozen-lockfile

# Workspace filtering
bun run --filter="packages/*" build
```

### **Bundling Optimization**
```typescript
await Bun.build({
  entrypoints: ["./index.ts"],
  outdir: "./dist",
  // Tree shaking
  minify: {
    whitespace: true,
    identifiers: true,
    syntax: true,
  },
  // Code splitting
  splitting: true,
  // Source maps for debugging
  sourcemap: "external",
});
```

## Integration Patterns

### **React Applications**
```typescript
// bunfig.toml
[install]
registry = "https://registry.npmjs.org"

// package.json
{
  "scripts": {
    "dev": "bun run --hot src/index.tsx",
    "build": "bun run build.ts"
  }
}
```

### **Express.js Migration**
```typescript
// Before (Node.js + Express)
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000);

// After (Bun)
const server = Bun.serve({
  port: 3000,
  fetch(req) {
    if (req.url.endsWith('/')) {
      return new Response('Hello World!');
    }
    return new Response('Not Found', { status: 404 });
  },
});
```

### **Database Integration**
```typescript
// SQLite with migrations
const db = new Bun.sqlite("app.db");

// Create tables
db.run(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
  )
`);

// Prepared statements for performance
const insertUser = db.prepare("INSERT INTO users (name, email) VALUES (?, ?)");
insertUser.run("John Doe", "john@example.com");
```

### **Testing Setup**
```typescript
// bunfig.toml
[test]
preload = "./test-setup.ts"

// test-setup.ts
import { beforeAll } from "bun:test";

beforeAll(() => {
  // Global test setup
  console.log("Setting up tests...");
});
```

## Related Concepts

- **[Hono](./hono.md)** - Web framework optimized for Bun and other runtimes
- **[API Design](./api-design.md)** - API development principles and patterns
- **[Frameworks](./frameworks.md)** - Overview of development frameworks
- **[Production Deployment](./production-deployment.md)** - Deploying applications to production

## Best Practices

### **Application Structure**
- **Modular Code**: Organize code into logical modules and packages
- **Type Safety**: Leverage TypeScript for better development experience
- **Environment Configuration**: Use environment variables for configuration
- **Error Handling**: Implement proper error boundaries and logging

### **Performance Guidelines**
- **Native APIs**: Prefer Bun's built-in APIs over third-party libraries when possible
- **Efficient Bundling**: Use appropriate minification and code splitting
- **Database Optimization**: Use prepared statements and connection pooling
- **Memory Management**: Be mindful of memory usage in long-running applications

### **Development Best Practices**

- **Version Control**: Use semantic versioning and proper commit messages
- **Testing Strategy**: Write comprehensive tests with good coverage
- **CI/CD Integration**: Automate testing and deployment pipelines
- **Monitoring**: Implement logging and performance monitoring

## Learning Resources

### **Official Documentation**
- **[Getting Started](https://bun.com/docs/quickstart)** - Basic setup and first steps
- **[Runtime Guide](https://bun.com/docs/runtime)** - Using Bun as a JavaScript runtime
- **[Package Manager](https://bun.com/docs/cli/install)** - Dependency management with Bun
- **[Test Runner](https://bun.com/docs/cli/test)** - Writing and running tests

### **Guides and Tutorials**
- **[HTTP Server Guide](https://bun.com/guides/http/server)** - Building web servers
- **[Database Guide](https://bun.com/docs/runtime/sqlite)** - Working with databases
- **[Bundler Guide](https://bun.com/docs/bundler)** - Code bundling and optimization
- **[Migration Guides](https://bun.com/guides)** - Migrating from other tools

### **Community Resources**
- **[Discord Community](https://bun.com/discord)** - Real-time community support
- **[GitHub Discussions](https://github.com/oven-sh/bun/discussions)** - Community discussions
- **[Blog](https://bun.com/blog/)** - Latest features and updates
- **[Awesome Bun](https://github.com/oven-sh/awesome-bun)** - Community-curated resources

## Future Directions

### **Platform Expansion**
- **Enhanced Node.js Compatibility**: Continued improvements in Node.js API support
- **New Runtime Features**: Additional built-in APIs and performance optimizations
- **Cloud Integration**: Deeper integration with cloud platforms and services
- **Tool Ecosystem**: Expansion of the built-in tool suite

### **Performance Improvements**
- **Startup Time Optimization**: Further reductions in cold start times
- **Memory Efficiency**: Better memory management and garbage collection
- **Concurrent Execution**: Improved parallel processing capabilities
- **Cross-Platform Performance**: Optimized performance across all supported platforms

### **Developer Tools**
- **Enhanced Debugging**: Better debugging and profiling tools
- **IDE Integration**: Improved support in code editors and IDEs
- **Plugin System**: Extensible plugin architecture for custom tools
- **Documentation**: Expanded guides and learning resources

[Back to Concepts Hub](./README.md)