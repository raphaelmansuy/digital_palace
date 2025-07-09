# TIL: Complete Guide to VS Code and GitHub Configuration Files (2025-07-09)

Today I learned about the comprehensive configuration system for VS Code and GitHub, including all file types, paths, and actionable configurations for optimizing development workflows.

## What are Configuration Files?

Configuration files are JSON, YAML, and other structured files that define behavior, settings, and automation for VS Code and GitHub. They enable:

- **Workspace standardization** across team members
- **Automated workflows** and CI/CD pipelines
- **Development environment consistency**
- **Tool integration** and customization
- **Security and access control**

## VS Code Configuration Files

### 1. Core Settings & Preferences

#### User Settings (Global)
**Path**: `~/.vscode/settings.json` (macOS/Linux), `%APPDATA%\Code\User\settings.json` (Windows)
**Purpose**: Global user preferences across all workspaces

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "files.autoSave": "onFocusChange",
  "terminal.integrated.shell.osx": "/bin/zsh",
  "python.defaultInterpreterPath": "/usr/local/bin/python3",
  "eslint.enable": true,
  "prettier.singleQuote": true,
  "git.autofetch": true,
  "workbench.colorTheme": "Dark+ (default dark)",
  "extensions.autoUpdate": false
}
```

#### Workspace Settings
**Path**: `.vscode/settings.json` (workspace root)
**Purpose**: Project-specific settings that override user settings

```json
{
  "python.pythonPath": "./venv/bin/python",
  "eslint.workingDirectories": ["frontend", "backend"],
  "files.exclude": {
    "**/node_modules": true,
    "**/.git": true,
    "**/dist": true,
    "**/__pycache__": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true
  },
  "typescript.preferences.includePackageJsonAutoImports": "on"
}
```

### 2. Debugging Configuration

#### Launch Configuration
**Path**: `.vscode/launch.json`
**Purpose**: Define debugging configurations for different languages and frameworks

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Node.js",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/src/index.js",
      "env": {
        "NODE_ENV": "development"
      },
      "console": "integratedTerminal",
      "skipFiles": ["<node_internals>/**"]
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "envFile": "${workspaceFolder}/.env"
    },
    {
      "name": "Attach to Chrome",
      "type": "chrome",
      "request": "attach",
      "port": 9222,
      "webRoot": "${workspaceFolder}/src"
    },
    {
      "name": "Debug TypeScript",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/src/main.ts",
      "outFiles": ["${workspaceFolder}/dist/**/*.js"],
      "runtimeArgs": ["-r", "ts-node/register"],
      "envFile": "${workspaceFolder}/.env"
    }
  ]
}
```

### 3. Task Automation

#### Tasks Configuration
**Path**: `.vscode/tasks.json`
**Purpose**: Define build tasks, test runners, and custom commands

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build TypeScript",
      "type": "typescript",
      "tsconfig": "tsconfig.json",
      "problemMatcher": ["$tsc"],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "npm",
      "args": ["test"],
      "group": "test",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "Docker Build",
      "type": "shell",
      "command": "docker",
      "args": ["build", "-t", "${workspaceFolderBasename}:latest", "."],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always"
      }
    },
    {
      "label": "Start Dev Server",
      "type": "shell",
      "command": "npm",
      "args": ["run", "dev"],
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "."
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting development server",
          "endsPattern": "Local:.*http://localhost"
        }
      }
    }
  ]
}
```

### 4. Extensions & Recommendations

#### Extensions Configuration
**Path**: `.vscode/extensions.json`
**Purpose**: Recommend extensions for the workspace

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-vscode.vscode-typescript-next",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-eslint",
    "bradlc.vscode-tailwindcss",
    "ms-vscode.vscode-json",
    "ms-azuretools.vscode-docker",
    "github.copilot",
    "github.vscode-github-actions",
    "ms-vscode-remote.remote-containers"
  ],
  "unwantedRecommendations": [
    "ms-vscode.vscode-typescript",
    "hookyqr.beautify"
  ]
}
```

### 5. Code Snippets

#### User Snippets
**Path**: `~/.vscode/snippets/` or `.vscode/*.code-snippets`
**Purpose**: Custom code snippets for faster development

```json
{
  "React Functional Component": {
    "prefix": "rfc",
    "body": [
      "import React from 'react';",
      "",
      "interface ${1:ComponentName}Props {",
      "  $2",
      "}",
      "",
      "const ${1:ComponentName}: React.FC<${1:ComponentName}Props> = ({ $3 }) => {",
      "  return (",
      "    <div>",
      "      $0",
      "    </div>",
      "  );",
      "};",
      "",
      "export default ${1:ComponentName};"
    ],
    "description": "Creates a React functional component with TypeScript"
  },
  "Express Route Handler": {
    "prefix": "route",
    "body": [
      "app.${1|get,post,put,delete|}('${2:/api/endpoint}', async (req: Request, res: Response) => {",
      "  try {",
      "    $3",
      "    res.status(200).json({ success: true });",
      "  } catch (error) {",
      "    res.status(500).json({ error: error.message });",
      "  }",
      "});"
    ],
    "description": "Express.js route handler with error handling"
  }
}
```

### 6. Multi-root Workspaces

#### Workspace Configuration
**Path**: `project.code-workspace`
**Purpose**: Define multi-root workspaces with different project folders

```json
{
  "folders": [
    {
      "name": "Frontend",
      "path": "./frontend"
    },
    {
      "name": "Backend",
      "path": "./backend"
    },
    {
      "name": "Shared",
      "path": "./shared"
    }
  ],
  "settings": {
    "typescript.preferences.includePackageJsonAutoImports": "off",
    "eslint.workingDirectories": [
      "frontend",
      "backend"
    ]
  },
  "extensions": {
    "recommendations": [
      "ms-vscode.vscode-typescript-next",
      "ms-python.python"
    ]
  },
  "launch": {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Launch Full Stack",
        "type": "node",
        "request": "launch",
        "program": "${workspaceFolder:Backend}/src/index.js"
      }
    ]
  }
}
```

### 7. DevContainer Configuration

#### DevContainer
**Path**: `.devcontainer/devcontainer.json`
**Purpose**: Define development container environment

```json
{
  "name": "Node.js & TypeScript",
  "image": "mcr.microsoft.com/vscode/devcontainers/typescript-node:18",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.vscode-typescript-next",
        "esbenp.prettier-vscode",
        "ms-vscode.vscode-eslint"
      ],
      "settings": {
        "terminal.integrated.shell.linux": "/bin/zsh"
      }
    }
  },
  "forwardPorts": [3000, 3001],
  "postCreateCommand": "npm install",
  "remoteUser": "node",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "mounts": [
    "source=${localWorkspaceFolder}/.env,target=/workspace/.env,type=bind,consistency=cached"
  ]
}
```

### 8. Language-Specific Configuration

#### TypeScript Configuration
**Path**: `tsconfig.json`, `jsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020", "DOM"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "moduleResolution": "node",
    "allowSyntheticDefaultImports": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

## GitHub Configuration Files

### 1. Repository Configuration

#### GitHub Repository Settings
**Path**: `.github/` directory (repository root)

#### Repository Metadata
**Path**: `.github/CODEOWNERS`
**Purpose**: Define code review requirements

```
# Global owners
* @team-leads @senior-developers

# Frontend team
/frontend/ @frontend-team
/src/components/ @ui-team

# Backend team
/backend/ @backend-team
/api/ @api-team

# Infrastructure
/docker/ @devops-team
/.github/workflows/ @ci-cd-team
/terraform/ @infrastructure-team

# Documentation
/docs/ @technical-writers
*.md @documentation-team

# Security sensitive files
/secrets/ @security-team
/.env.example @security-team
```

### 2. GitHub Actions Workflows

#### Main Workflow
**Path**: `.github/workflows/ci.yml`
**Purpose**: Continuous integration and deployment

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
    paths:
      - 'src/**'
      - '*.json'
      - '.github/workflows/**'

permissions:
  contents: read
  security-events: write
  pull-requests: write

env:
  NODE_VERSION: '18.x'
  PYTHON_VERSION: '3.11'

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16.x, 18.x, 20.x]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run linting
        run: npm run lint
        
      - name: Run tests
        run: npm run test:coverage
        
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/lcov.info
          
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run security audit
        run: npm audit --audit-level=moderate
        
      - name: CodeQL Analysis
        uses: github/codeql-action/init@v3
        with:
          languages: javascript
          
  build:
    needs: [test, security]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          
      - run: npm ci
      - run: npm run build
      
      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-files
          path: dist/
          
  deploy:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy to production
        run: echo "Deploying to production..."
```

#### Release Workflow
**Path**: `.github/workflows/release.yml`

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  create-release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          draft: false
          prerelease: false
          
  docker-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
        
      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
          
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:latest
            ghcr.io/${{ github.repository }}:${{ github.ref_name }}
```

### 3. Issue and PR Templates

#### Bug Report Template
**Path**: `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
name: Bug Report
description: File a bug report to help us improve
title: "[Bug]: "
labels: ["bug", "triage"]
assignees:
  - maintainer-team

body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
        
  - type: input
    id: contact
    attributes:
      label: Contact Details
      description: How can we get in touch with you if we need more info?
      placeholder: ex. email@example.com
    validations:
      required: false
      
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Also tell us, what did you expect to happen?
      placeholder: Tell us what you see!
    validations:
      required: true
      
  - type: dropdown
    id: version
    attributes:
      label: Version
      description: What version of our software are you running?
      options:
        - 1.0.2 (Default)
        - 1.0.1
        - 1.0.0
    validations:
      required: true
      
  - type: dropdown
    id: browsers
    attributes:
      label: What browsers are you seeing the problem on?
      multiple: true
      options:
        - Firefox
        - Chrome
        - Safari
        - Microsoft Edge
        
  - type: textarea
    id: logs
    attributes:
      label: Relevant log output
      description: Please copy and paste any relevant log output.
      render: shell
```

#### Pull Request Template
**Path**: `.github/pull_request_template.md`

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tests pass locally with my changes
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] Any dependent changes have been merged and published in downstream modules

## Screenshots (if applicable)

## Related Issues
Fixes #(issue)
```

### 4. Security Configuration

#### Security Policy
**Path**: `.github/SECURITY.md`

```markdown
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.9.x   | :white_check_mark: |
| 1.8.x   | :x:                |
| < 1.8   | :x:                |

## Reporting a Vulnerability

Please report security vulnerabilities to security@company.com

We will respond within 48 hours and provide a timeline for resolution.

Do NOT open public issues for security vulnerabilities.
```

#### Dependabot Configuration
**Path**: `.github/dependabot.yml`

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "09:00"
    open-pull-requests-limit: 10
    reviewers:
      - "team-leads"
    assignees:
      - "security-team"
    commit-message:
      prefix: "npm"
      include: "scope"
      
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
    ignore:
      - dependency-name: "alpine"
        versions: ["3.14"]
        
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

### 5. GitHub Pages & Documentation

#### GitHub Pages Configuration
**Path**: `.github/workflows/deploy-docs.yml`

```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]
    paths: ['docs/**']

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: npm
          
      - name: Install dependencies
        run: npm ci
        
      - name: Build documentation
        run: npm run docs:build
        
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./docs/dist

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## Environment & Project Files

### 1. Environment Configuration

#### Environment Variables
**Path**: `.env`, `.env.local`, `.env.production`

```bash
# .env.example
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET=your-super-secret-jwt-key
OAUTH_CLIENT_ID=your-oauth-client-id
OAUTH_CLIENT_SECRET=your-oauth-client-secret

# External APIs
STRIPE_SECRET_KEY=sk_test_...
SENDGRID_API_KEY=SG....
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...

# Application
NODE_ENV=development
PORT=3000
LOG_LEVEL=debug
API_BASE_URL=http://localhost:3000/api

# Feature Flags
ENABLE_FEATURE_X=true
ENABLE_ANALYTICS=false
```

### 2. Docker Configuration

#### Dockerfile
**Path**: `Dockerfile`

```dockerfile
# Multi-stage build for production
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine AS production

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

WORKDIR /app

COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

USER nextjs

EXPOSE 3000

ENV NODE_ENV=production

CMD ["npm", "start"]
```

#### Docker Compose
**Path**: `docker-compose.yml`

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:password@db:5432/appdb
    depends_on:
      - db
      - redis
    volumes:
      - .:/app
      - /app/node_modules
    command: npm run dev

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

## Package & Dependency Management

### 1. Node.js Configuration

#### Package.json
**Path**: `package.json`

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "Production-ready application",
  "main": "dist/index.js",
  "scripts": {
    "start": "node dist/index.js",
    "dev": "tsx watch src/index.ts",
    "build": "tsc && tsc-alias",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint src --ext .ts,.tsx --fix",
    "lint:check": "eslint src --ext .ts,.tsx",
    "format": "prettier --write \"src/**/*.{ts,tsx,json}\"",
    "format:check": "prettier --check \"src/**/*.{ts,tsx,json}\"",
    "type-check": "tsc --noEmit",
    "clean": "rimraf dist",
    "docker:build": "docker build -t my-app .",
    "docker:run": "docker run -p 3000:3000 my-app"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=8.0.0"
  },
  "keywords": ["node", "typescript", "api"],
  "author": "Your Name <your.email@example.com>",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "cors": "^2.8.5",
    "helmet": "^7.0.0",
    "dotenv": "^16.3.1"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/express": "^4.17.17",
    "typescript": "^5.1.6",
    "tsx": "^3.12.7",
    "jest": "^29.6.1",
    "eslint": "^8.44.0",
    "prettier": "^3.0.0"
  },
  "volta": {
    "node": "18.17.0",
    "npm": "9.6.7"
  }
}
```

### 2. Python Configuration

#### Requirements Files
**Path**: `requirements.txt`, `requirements-dev.txt`, `pyproject.toml`

```txt
# requirements.txt
fastapi==0.103.0
uvicorn[standard]==0.23.2
pydantic==2.3.0
sqlalchemy==2.0.20
alembic==1.11.1
python-multipart==0.0.6
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0
pytest==7.4.0
pytest-asyncio==0.21.1
httpx==0.24.1
```

#### Pyproject.toml
**Path**: `pyproject.toml`

```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "my-python-app"
version = "0.1.0"
description = "A Python application"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.103.0"
uvicorn = {extras = ["standard"], version = "^0.23.2"}

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
black = "^23.7.0"
isort = "^5.12.0"
mypy = "^1.5.0"
pre-commit = "^3.3.3"

[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = "-v --tb=short"
```

## Linting & Code Quality

### 1. ESLint Configuration

#### ESLint Config
**Path**: `.eslintrc.json`

```json
{
  "extends": [
    "eslint:recommended",
    "@typescript-eslint/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint", "import"],
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module",
    "project": "./tsconfig.json"
  },
  "env": {
    "node": true,
    "es2022": true,
    "jest": true
  },
  "rules": {
    "@typescript-eslint/no-unused-vars": [
      "error",
      { "argsIgnorePattern": "^_" }
    ],
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/no-explicit-any": "warn",
    "import/order": [
      "error",
      {
        "groups": [
          "builtin",
          "external",
          "internal",
          "parent",
          "sibling",
          "index"
        ],
        "newlines-between": "always"
      }
    ],
    "prefer-const": "error",
    "no-var": "error"
  },
  "ignorePatterns": ["dist/", "node_modules/", "*.js"]
}
```

### 2. Prettier Configuration

#### Prettier Config
**Path**: `.prettierrc.json`

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "endOfLine": "lf",
  "overrides": [
    {
      "files": "*.md",
      "options": {
        "printWidth": 100,
        "proseWrap": "always"
      }
    },
    {
      "files": "*.json",
      "options": {
        "printWidth": 120
      }
    }
  ]
}
```

#### Prettier Ignore
**Path**: `.prettierignore`

```
# Build outputs
dist/
build/
*.min.js
*.min.css

# Dependencies
node_modules/
vendor/

# Generated files
coverage/
*.lock
package-lock.json

# Logs
*.log

# OS files
.DS_Store
Thumbs.db
```

## Git Configuration

### 1. Git Ignore

#### Gitignore
**Path**: `.gitignore`

```gitignore
# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Production builds
/dist
/build
*.tgz
*.tar.gz

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/
*.lcov

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Python
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/
.pytest_cache/

# Database
*.db
*.sqlite3

# Logs
logs/
*.log

# Docker
.dockerignore
```

### 2. Git Attributes

#### Git Attributes
**Path**: `.gitattributes`

```gitattributes
# Auto detect text files and perform LF normalization
* text=auto

# Force specific files to be treated as text
*.txt text
*.md text
*.json text
*.js text eol=lf
*.ts text eol=lf
*.tsx text eol=lf
*.css text eol=lf
*.html text eol=lf
*.yml text eol=lf
*.yaml text eol=lf

# Force binary files to be treated as binary
*.png binary
*.jpg binary
*.jpeg binary
*.gif binary
*.ico binary
*.mov binary
*.mp4 binary
*.mp3 binary
*.flv binary
*.fla binary
*.swf binary
*.gz binary
*.zip binary
*.7z binary
*.ttf binary
*.eot binary
*.woff binary
*.woff2 binary

# Git LFS (Large File Storage)
*.psd filter=lfs diff=lfs merge=lfs -text
*.ai filter=lfs diff=lfs merge=lfs -text
*.sketch filter=lfs diff=lfs merge=lfs -text

# Archive files
*.zip export-ignore
*.tar export-ignore
*.tar.gz export-ignore

# Export ignore
.gitattributes export-ignore
.gitignore export-ignore
.github/ export-ignore
docs/ export-ignore
tests/ export-ignore
```

## Pre-commit Hooks

### 1. Pre-commit Configuration

#### Pre-commit Config
**Path**: `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
      - id: check-added-large-files
        args: ['--maxkb=1000']
      - id: mixed-line-ending
        args: ['--fix=lf']

  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.44.0
    hooks:
      - id: eslint
        files: \.(js|ts|tsx)$
        types: [file]

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.0.0
    hooks:
      - id: prettier
        types_or: [javascript, jsx, ts, tsx, json, yaml, markdown]

  - repo: https://github.com/commitizen-tools/commitizen
    rev: v3.6.0
    hooks:
      - id: commitizen
```

## Best Practices & Tips

### 1. Configuration File Organization

#### Directory Structure
```
project-root/
├── .github/                    # GitHub-specific configs
│   ├── workflows/             # GitHub Actions
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   └── pull_request_template.md
├── .vscode/                   # VS Code workspace configs
│   ├── settings.json         # Workspace settings
│   ├── launch.json           # Debug configurations
│   ├── tasks.json            # Build tasks
│   └── extensions.json       # Recommended extensions
├── .devcontainer/            # Development container
│   └── devcontainer.json
├── docs/                     # Documentation
├── src/                      # Source code
├── tests/                    # Test files
├── .env.example             # Environment template
├── .gitignore               # Git ignore rules
├── .gitattributes          # Git attributes
├── .prettierrc.json        # Prettier config
├── .eslintrc.json          # ESLint config
├── tsconfig.json           # TypeScript config
├── package.json            # Node.js dependencies
├── docker-compose.yml      # Docker services
└── README.md               # Project documentation
```

### 2. Security Considerations

#### Secrets Management
```json
// .github/workflows/secure.yml
{
  "steps": [
    {
      "name": "Use secrets safely",
      "env": {
        "API_KEY": "${{ secrets.API_KEY }}",
        "DATABASE_URL": "${{ secrets.DATABASE_URL }}"
      },
      "run": "echo 'Never log secrets directly'"
    }
  ]
}
```

#### Environment File Security
```bash
# Always use .env.example for templates
# .env.example
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
API_SECRET=your-secret-here
JWT_SECRET=generate-a-secure-random-string

# Add .env to .gitignore
echo ".env" >> .gitignore
```

### 3. Team Collaboration

#### Consistent Development Environment
```json
// .vscode/settings.json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true,
    "source.organizeImports": true
  },
  "typescript.preferences.includePackageJsonAutoImports": "on",
  "files.insertFinalNewline": true,
  "files.trimTrailingWhitespace": true
}
```

#### Extension Recommendations
```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-vscode.vscode-typescript-next",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-eslint",
    "github.copilot",
    "ms-azuretools.vscode-docker"
  ],
  "unwantedRecommendations": [
    "ms-vscode.vscode-typescript"
  ]
}
```

## Advanced Configuration Patterns

### 1. Monorepo Configuration

#### Workspace Package.json
```json
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": [
    "packages/*",
    "apps/*"
  ],
  "scripts": {
    "build": "lerna run build",
    "test": "lerna run test",
    "lint": "lerna run lint"
  },
  "devDependencies": {
    "lerna": "^7.1.4",
    "@typescript-eslint/eslint-plugin": "^6.0.0"
  }
}
```

#### Lerna Configuration
**Path**: `lerna.json`

```json
{
  "version": "independent",
  "npmClient": "npm",
  "command": {
    "publish": {
      "conventionalCommits": true,
      "message": "chore(release): publish"
    },
    "bootstrap": {
      "ignore": "component-*",
      "npmClientArgs": ["--no-package-lock"]
    }
  }
}
```

### 2. Conditional Configuration

#### Environment-based VS Code Settings
```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "files.associations": {
    "*.env.*": "dotenv",
    "Dockerfile.*": "dockerfile"
  }
}
```

### 3. Multi-Platform Configuration

#### Cross-Platform Scripts
```json
// package.json
{
  "scripts": {
    "clean": "rimraf dist",
    "copy-files": "cpy 'src/**/*.json' dist",
    "start:dev": "cross-env NODE_ENV=development nodemon src/index.ts",
    "build:prod": "cross-env NODE_ENV=production webpack --mode production"
  }
}
```

## Configuration File Validation & Testing

### 1. JSON Schema Validation

#### Custom Schema for Config Files
```json
// schemas/vscode-settings.schema.json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "editor.fontSize": {
      "type": "number",
      "minimum": 8,
      "maximum": 72
    },
    "editor.tabSize": {
      "type": "number",
      "minimum": 1,
      "maximum": 8
    }
  }
}
```

### 2. Configuration Testing

#### GitHub Actions Workflow Validation
```yaml
# .github/workflows/validate-config.yml
name: Validate Configuration Files

on:
  pull_request:
    paths:
      - '.github/**'
      - '.vscode/**'
      - '*.json'
      - '*.yml'
      - '*.yaml'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Validate JSON files
        run: |
          find . -name "*.json" -not -path "./node_modules/*" | xargs -I {} sh -c 'echo "Validating {}" && cat {} | jq .'
          
      - name: Validate YAML files
        run: |
          find . -name "*.yml" -o -name "*.yaml" | xargs -I {} sh -c 'echo "Validating {}" && yamllint {}'
```

## 🔗 Related Resources

- [VS Code Documentation](https://code.visualstudio.com/docs) - Official VS Code documentation
- [GitHub Actions Documentation](https://docs.github.com/en/actions) - Official GitHub Actions guide
- [TypeScript Configuration](https://www.typescriptlang.org/tsconfig) - Complete TSConfig reference
- [ESLint Configuration](https://eslint.org/docs/user-guide/configuring/) - ESLint setup guide
- [Docker Documentation](https://docs.docker.com/) - Container configuration guides

## Quick Reference Commands

### Configuration File Creation
```bash
# Initialize basic config files
npm init -y                              # package.json
tsc --init                              # tsconfig.json
npx eslint --init                       # .eslintrc.json
echo '{}' > .prettierrc.json           # prettier config
touch .env .env.example                # environment files

# VS Code workspace
mkdir .vscode
touch .vscode/settings.json
touch .vscode/launch.json
touch .vscode/tasks.json
touch .vscode/extensions.json

# GitHub setup
mkdir -p .github/workflows
mkdir -p .github/ISSUE_TEMPLATE
touch .github/workflows/ci.yml
touch .github/CODEOWNERS
touch .github/SECURITY.md
```

### Configuration Validation
```bash
# Validate JSON files
find . -name "*.json" | xargs -I {} jq empty {}

# Validate YAML files
find . -name "*.yml" -o -name "*.yaml" | xargs yamllint

# Check TypeScript config
npx tsc --noEmit

# Validate package.json
npm install --dry-run
```

### Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Generate VS Code settings
code --install-extension ms-vscode.vscode-eslint
code --install-extension esbenp.prettier-vscode

# Setup pre-commit hooks
npm install -D husky lint-staged
npx husky install
```

*This comprehensive guide covers all major configuration files for VS Code and GitHub, providing actionable examples and best practices for modern development workflows.*
