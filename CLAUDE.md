# CLAUDE.md — AI Assistant Guide for onboard-asof

This file provides guidance for AI assistants (Claude and others) working in this repository.

## Project Overview

**Repository:** `prof-ramos/onboard-asof`
**Status:** Early-stage / bootstrapping. As of the initial commit, no source code exists yet — only this documentation and an empty `README.md`.

The project name suggests an **onboarding system** with some notion of "as-of" (point-in-time) semantics, but the concrete architecture has not yet been established. Treat any assumptions about the tech stack as tentative until `README.md` or source files are populated.

---

## Repository Layout (Current)

```
onboard-asof/
├── CLAUDE.md       ← this file
└── README.md       ← project description (currently empty)
```

This layout will grow as the project is developed. Update this section whenever significant directories or files are added.

---

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` / `master` | Stable, production-ready code |
| `claude/<description>-<session-id>` | AI-assisted feature branches |
| `feature/<name>` | Human-led feature work |

**Rule:** Never push directly to `main` or `master`. All work goes through a branch and a pull request.

AI-generated branches must follow the pattern `claude/<short-description>-<SESSION_ID>` to avoid 403 errors on push.

---

## Git Workflow

```bash
# Start work on a new task
git checkout -b claude/<short-description>-<SESSION_ID>

# Stage and commit
git add <specific files>   # never use `git add -A` blindly
git commit -m "feat: concise description of what and why"

# Push
git push -u origin claude/<short-description>-<SESSION_ID>
```

### Commit Message Style

Follow the **Conventional Commits** format:

```
<type>(<optional scope>): <short summary>

<optional body explaining WHY, not WHAT>
```

Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`.

---

## Development Setup

> No stack has been chosen yet. Once it is, document the following here:
> - Language & runtime version (e.g., Node 20, Python 3.12)
> - Package manager (e.g., npm, pnpm, uv, cargo)
> - Installation steps (`npm install`, `pip install -e .`, etc.)
> - How to run the dev server
> - Required environment variables (create a `.env.example` as the canonical list)

---

## Testing

> No test framework has been configured yet. Once tests exist, document:
> - How to run all tests
> - How to run a single test file
> - Coverage commands
> - What must pass before a PR can be merged

**Convention:** Tests must always pass before pushing. If a test is broken by intentional design changes, update the test in the same commit.

---

## Linting & Formatting

> To be defined once the stack is chosen. Recommended defaults:
> - **JavaScript/TypeScript:** ESLint + Prettier
> - **Python:** Ruff (lint + format)
> - **Rust:** `cargo fmt` + `cargo clippy`

Auto-format files before every commit. Do not disable lint rules without a comment explaining why.

---

## Environment Variables

- Keep a `.env.example` file at the repo root with every variable name and a placeholder value.
- Never commit real secrets or `.env` files.
- Document each variable's purpose in `.env.example`.

---

## AI Assistant Conventions

### Do
- Read files before editing them.
- Prefer editing existing files over creating new ones.
- Keep changes minimal and focused — only what was asked.
- Use the `TodoWrite` tool to track multi-step tasks.
- Commit with descriptive messages that explain the *why*.
- Push to the branch specified in the task; never push to `main`/`master`.

### Don't
- Don't add unrequested features, refactors, or comments.
- Don't use `git add -A` or `git add .` — stage specific files.
- Don't use `--no-verify` to skip hooks.
- Don't introduce security vulnerabilities (SQLi, XSS, command injection, etc.).
- Don't hard-code secrets or credentials.
- Don't create documentation files (`.md`) unless explicitly asked.

### Searching the Codebase
- Use `Glob` for finding files by name pattern.
- Use `Grep` for searching file contents.
- Use the `Explore` subagent for broad, multi-step codebase exploration.

---

## Security

- Validate all input at system boundaries (user input, external APIs).
- Do not trust data from external sources without sanitization.
- Follow the principle of least privilege for any credentials or permissions.
- Report suspected vulnerabilities; do not silently work around them.

---

## Updating This File

Keep `CLAUDE.md` current as the project evolves:

- Add new sections when the tech stack is chosen.
- Update the directory tree when significant structure is added.
- Document non-obvious conventions or decisions here so future contributors (human or AI) don't have to rediscover them.
