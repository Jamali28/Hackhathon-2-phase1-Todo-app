---
id: 1
title: Create Hackathon TODO App Constitution
stage: constitution
date: 2025-12-24
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: muhee
command: sp.constitution
labels: [constitution, hackathon, todo-app, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

```text
You are a proffesional Spec-driven developer Create a comprehensive project constitution for a Hackathon Phase 1 TODO application: a simple in-memory Python console-based tool implementing add, delete, update, view, and mark complete features. Focus on the following foundational principles and guidelines:

- Code Quality: Adhere to PEP 8 style, use meaningful variable/function names, keep functions short and single-responsibility, include type hints and docstrings for all public methods. Prioritize readability and maintainability over premature optimization.
- Testing Standards: Require unit tests for core task management functions (e.g., add, delete, update, mark) using Python's built-in unittest module. Aim for at least 80% coverage of business logic. Include edge case tests (e.g., invalid IDs, empty lists).
- User Experience Consistency: Ensure the CLI is intuitive with clear prompts, numbered menus, and consistent output formatting (e.g., task lists with ID, title, description, and status indicators like [ ] or [x]). Handle errors gracefully with user-friendly messages, no crashes on invalid input.
- Performance Requirements: Use efficient in-memory data structures (e.g., list of dicts) for O(1) average-case operations where possible. Since it's console-based and in-memory, target sub-second response times for all operations with up to 1000 tasks.
- Development Governance: All features must derive from specifications generated via Spec-Kit Plus. Use spec-driven development exclusively: start with specs, clarify ambiguities, create plans and tasks, then implement. Track all spec iterations in a history folder. Enforce Python 3.13+ best practices, modular project structure (/src with separate modules for logic and CLI), and clean commits in Git. Decisions should prioritize MVP simplicity for Hackathon timelines—avoid unnecessary features or dependencies.
- Overall Standards: Promote open-source best practices in the GitHub repo, including a detailed README.md with setup instructions (using UV for dependency management). Ensure the constitution guides AI-assisted code generation (via Claude) to produce consistent, reliable outputs aligned with these principles.30.7sExpert14 sourcesin markdownMarkdownCreate a comprehensive project constitution for this Hackathon Phase 1 TODO application: a simple command-line Python console-based in-memory TODO tool.

The application must implement exactly the five basic features:
- Add Task (create new tasks with title and description)
- Delete Task (remove by ID)
- Update Task (modify title/description by ID)
- View Task List (display all tasks with ID, title, description, and completion status)
- Mark as Complete (toggle completion status by ID)

All data is stored in memory only (no files or databases). The app runs as an interactive console loop until exit.

Output the constitution as a complete Markdown file content for `.specify/memory/constitution.md`.

Structure it clearly with sections. Use bullet points or numbered lists for principles.

Key sections and content guidelines:

### Project Overview
Briefly describe the project: Phase 1 of a Hackathon TODO app – in-memory console TODO with core CRUD + completion toggle.

### Core Principles
- Simplicity First: This is a Hackathon MVP. Prioritize quick implementation, readability, and minimalism. Avoid over-engineering, unnecessary abstractions, or extra features.
- Spec-Driven Development: All code must derive from specifications created via Spec-Kit Plus workflow. Never implement without a spec, plan, and tasks.
- Clean Code: Follow PEP 8. Use meaningful names, short functions (single responsibility), type hints everywhere, and docstrings for public functions/modules.

### Technical Stack
- Python 3.13+
- Package manager: UV
- No external dependencies beyond standard library (keep it pure Python)
- In-memory storage: List of dictionaries or dataclasses
- CLI: Built with standard input()/print(), interactive loop

### Code Quality Standards
- Use type hints with Python 3.13 features (e.g., | for unions)
- Modular structure: `/src` with separate modules (e.g., `tasks.py` for logic, `cli.py` for interface, `main.py` as entry point)
- Functions should be pure where possible; keep side effects minimal
- Graceful error handling: Validate inputs, user-friendly messages, no crashes

### Testing Requirements
- Use Python's built-in `unittest` module
- Write tests for all core task operations (add, delete, update, mark, list)
- Include edge cases: empty list, invalid IDs, duplicate IDs (prevented), etc.
- Aim for high coverage of business logic

### User Experience Guidelines
- Intuitive CLI: Menu-driven or clear command prompts (e.g., options like 'add', 'list', 'update <id>', etc.)
- Consistent formatting: Task list with ID, status indicator ([ ] or [x]), title, description
- Helpful messages and prompts
```

## Response snapshot

Created a comprehensive project constitution for the Hackathon Phase 1 TODO application, including:
- Project Overview section describing the application
- Six Core Principles: Simplicity First, Spec-Driven Development, Clean Code, Performance Efficiency, Error Handling and User Experience, Test-Driven Development
- Technical Stack section outlining the technology choices
- Code Quality Standards with specific requirements
- Testing Requirements with coverage targets
- User Experience Guidelines for CLI consistency
- Governance section with amendment procedures

The constitution was written to the file `.specify/memory/constitution.md` with version 1.0.0, ratified on 2025-12-24.

## Outcome

- ✅ Impact: Created foundational constitution document for the TODO application project
- 🧪 Tests: No tests created in this step
- 📁 Files: Updated .specify/memory/constitution.md with complete constitution
- 🔁 Next prompts: Next steps would include creating the spec, plan, and tasks based on this constitution
- 🧠 Reflection: The constitution establishes clear principles and guidelines that will guide all future development for this Hackathon project

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Not applicable