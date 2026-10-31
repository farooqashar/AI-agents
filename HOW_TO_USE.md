# Using the agent definitions

These files contain reusable task instructions. They are not a runtime, tool implementation, or automatic installer.

## Start with a root-level file

From a checkout, ask your assistant:

```text
Read debugging.md and use its instructions to investigate this failing endpoint.
Expected: HTTP 200. Actual: HTTP 500. Relevant files: app/routes.py and tests/test_routes.py.
Produce a minimal fix and report verification evidence.
```

For a review:

```text
Read code-review.md and review this diff. Report findings with severity,
file locations, impact, and verification gaps. Do not modify files.
```

When files are not locally accessible, attach the definition or supply its contents. Give the agent its task context, constraints, and acceptance criteria; do not assume it inherits conversation history.

## Host integration

For native subagents, use the host's documented installation directory, configuration schema, and invocation mechanism. The frontmatter here is repository metadata, not a promise that any particular host recognizes or enforces it. Verify compatibility against the installed host version before creating an adapter.

For ChatGPT, projects, or API integrations, supply the Markdown as instructions using the interface available to you. File references alone do not create tools or subprocesses. API applications must supply tools and enforce permissions separately.

## Permissions

Every definition declares edit, bash, and web explicitly. These describe intended access only. The host's policies remain authoritative; Bash may write files or invoke network clients even when edit or web is denied. Use a restricted host environment when read-only execution is required.

## Adding an agent

Copy [templates/agent.md](templates/agent.md), define one primary outcome, add its root-level link to [README.md](README.md), and verify the six required sections. Test representative successful, failure, and boundary cases before relying on it.
