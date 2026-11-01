# Agent Registry

This directory contains pre-built, reusable agent definitions for common use cases. Each agent is specialized in a specific domain and can be used as a subagent for focused tasks.

## Available Agents

### Development & Engineering

- **[linting.md](linting.md)** - Code quality checks, style enforcement, and best practices
- **[testing.md](testing.md)** - Test generation, validation, and quality assurance
- **[code-review.md](code-review.md)** - Code review with focus on quality, security, and best practices
- **[security.md](security.md)** - Vulnerability scanning and secure coding practices
- **[documentation.md](documentation.md)** - Technical documentation generation and maintenance
- **[database.md](database.md)** - Database design, queries, optimization, and administration
- **[api.md](api.md)** - API design, development, testing, and documentation
- **[devops.md](devops.md)** - CI/CD, deployment, infrastructure, and operational excellence
- **[debugging.md](debugging.md)** - Root-cause analysis, bug isolation, and regression prevention
- **[system-design.md](system-design.md)** - Scalable architecture planning, tradeoff analysis, and reliability design

### Analysis & Data

- **[research.md](research.md)** - Deep research, analysis, and information gathering
- **[data-analysis.md](data-analysis.md)** - Data processing, statistical analysis, and visualization
- **[browser.md](browser.md)** - Web browsing, scraping, and online information gathering

### Content & Communication

- **[writing.md](writing.md)** - Content creation, editing, and various writing styles
- **[summarizer.md](summarizer.md)** - Condensing information and creating concise summaries
- **[prompt-engineering.md](prompt-engineering.md)** - Prompt design, evaluation, and LLM workflow optimization

### Finance & Business

- **[finance.md](finance.md)** - Financial analysis, calculations, and money management

### Lifestyle & Personal

- **[travel.md](travel.md)** - Travel planning, destinations, and logistics
- **[activities-food.md](activities-food.md)** - Activity planning, dining, and entertainment recommendations
- **[health.md](health.md)** - Fitness, nutrition, mental health, and wellness
- **[learning.md](learning.md)** - Learning strategies, educational content, and skill development

### Productivity

- **[productivity.md](productivity.md)** - Task management, time optimization, and workflow improvement

## Usage

These Markdown definitions can be reused as task instructions. Native agent discovery, installation, supported frontmatter, and permissions depend on the host tool; referencing a file alone does not install a subagent.

### Quick Start

Tell your AI assistant to use an agent definition:

```
"Use finance.md as a subagent to analyze this budget"
"Spawn a subagent from security.md to review this code"
"Act as the agent defined in research.md"
```

The AI tool will read the markdown file and operate as that specialized agent.

See [HOW_TO_USE.md](HOW_TO_USE.md) for detailed examples.

### Agent Definition Format

Each agent includes:

```markdown
---
description: Brief description of the agent's purpose
mode: subagent
permission:
  edit: allow/deny
  bash: allow/deny
  web: allow/deny
---

[Detailed system instructions and focus areas]
```

### Permission Levels

- **edit**: Whether the agent can modify files
- **bash**: Whether the agent can execute shell commands
- **web**: Whether the agent can access web resources

### Creating Custom Agents

To create your own agent:

1. Create a new `.md` file in this directory
2. Add explicit description, mode, and edit/bash/web permissions
3. Follow the six sections in [templates/agent.md](templates/agent.md)
4. Define focus areas and best practices
5. Include examples where helpful

### Best Practices

- **Use specialized agents** for focused tasks rather than generic prompts
- **Read the agent definition** to understand its capabilities and limitations
- **Provide context** when invoking agents - they don't have conversation history
- **Combine agents** for multi-step workflows (e.g., research → write → review)
- **Update agents** as best practices evolve

## Agent Categories

### Read-Only Agents
Agents intended for analysis (Bash-enabled agents can still change state; host restrictions must enforce read-only execution):
- Research, Summarizer, Browser, Finance, Health, Learning, Travel, Activities/Food, Productivity

### Code-Modifying Agents
Agents that can edit code and files:
- Linting, Testing, Documentation, Database, API, DevOps, Debugging, System Design, Writing, Data Analysis, Prompt Engineering

### Development Workflow
Typical agent combinations:
1. **Feature Development**: Documentation → Testing → Code Review → Linting
2. **Bug Investigation**: Debugging → Testing → Code Review
3. **Content Creation**: Research → Writing → Summarizer
4. **Infrastructure Setup**: System Design → DevOps → Security → Documentation
5. **API Development**: API → Documentation → Testing → Security

## Contributing

To contribute a new agent:

1. Identify a clear, focused domain
2. Research best practices in that domain
3. Write comprehensive but practical instructions
4. Include examples and common patterns
5. Define appropriate permissions
6. Test the agent with real tasks
7. Submit a pull request

## Repository and attribution

Agent files live at the repository root. Use [HOW_TO_USE.md](HOW_TO_USE.md) for invocation guidance and [templates/agent.md](templates/agent.md) for new definitions.

Report issues in [this repository](https://github.com/farooqashar/AI-agents/issues).

The original registry referred to santai-cli. This repository currently has no LICENSE file; confirm provenance and applicable license terms before redistribution. This cleanup does not assign a new license.

## Workflow ownership

| Outcome | Primary agent | Handoff |
|---|---|---|
| Reproduce and repair a bug | Debugging | Testing for broader coverage |
| Automated style/type diagnostics | Linting | Debugging for logic defects |
| Findings on a diff | Code Review (no edits) | Security for deep threat analysis |
| Service architecture | System Design | API, Database, DevOps for implementation |
| Sourced synthesis | Research | Browser for interactive extraction |
| Technical reference updates | Documentation | Writing for general prose |

Long historical snippets live under `examples/`; inspect the current stack before adapting them.
