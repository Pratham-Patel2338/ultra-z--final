# ULTRA-Z Copilot Instructions

## Project Overview

You are contributing to ULTRA-Z.

ULTRA-Z is a modular AI Operating System built with Python, FastAPI, uv, Electron and React.

This is NOT a demo project.

This is a long-term production software project.

Always prioritize maintainability, scalability and readability over writing short code.

---

# General Rules

Never make architectural decisions.

Never create new folders unless explicitly requested.

Never rename files.

Never change the project structure.

Never install packages unless asked.

Never modify configuration files unless requested.

Never generate placeholder implementations unless instructed.

Do not delete existing code.

---

# Coding Style

Use Python 3.12+

Use type hints everywhere.

Use async/await whenever I/O is involved.

Keep functions small.

One responsibility per function.

One responsibility per class.

Avoid deeply nested code.

Avoid duplicated logic.

Prefer composition over inheritance.

Write readable code instead of clever code.

---

# Naming Conventions

Classes

PascalCase

Functions

snake_case

Variables

snake_case

Constants

UPPER_SNAKE_CASE

Private members

_leading_underscore

---

# Documentation

Every module should contain a module docstring.

Every public class should contain a docstring.

Every public function should contain a docstring.

Do not generate unnecessary comments.

Explain WHY, not WHAT.

---

# Error Handling

Never silently ignore exceptions.

Never use bare except.

Catch specific exceptions.

Log meaningful errors.

Return informative messages.

---

# Logging

Use the project logger.

Never use print().

Log important events.

Do not log sensitive information.

---

# FastAPI

Use APIRouter.

Use dependency injection.

Keep route handlers thin.

Business logic belongs in services.

Validation belongs in Pydantic schemas.

Database logic belongs in repositories.

---

# Architecture

Follow this responsibility chain.

Route

↓

Service

↓

Repository

↓

Database

Never access the database directly from routes.

Never put business logic inside routes.

---

# Module Independence

Every module should be independent.

Avoid circular imports.

Communicate through interfaces or events.

Never tightly couple modules.

---

# Configuration

Never hardcode secrets.

Read configuration from settings.

Support environment variables.

---

# Testing

Every feature should be testable.

Avoid global state.

Prefer dependency injection.

Keep modules isolated.

---

# Performance

Prefer async APIs.

Avoid unnecessary object creation.

Reuse expensive resources.

Avoid blocking calls.

---

# Security

Never expose secrets.

Validate all inputs.

Escape user-generated data.

Never trust external data.

Use least privilege.

---

# Git

Do not generate commit messages.

Do not modify Git history.

Do not stage files automatically.

---

# Code Generation

Generate only the requested files.

Avoid unrelated changes.

Do not refactor existing code unless asked.

Do not invent features.

Do not create TODO items unless requested.

---

# Output Quality

Always produce production-quality code.

Readable code is preferred over short code.

Favor maintainability over optimization.

Follow SOLID principles where appropriate.

Keep modules cohesive.

Minimize coupling.

---

# AI Assistant Rules

ULTRA-Z is built using a modular architecture.

Subsystems include:

Assistant

Memory

Runtime

Cognition

Workflow

Events

State

Plugins

Tools

Database

Security

Never merge responsibilities across modules.

Each module owns its own logic.

---

# Development Philosophy

Architecture First.

Implementation Second.

Testing Third.

Optimization Fourth.

Never skip steps.

Follow the existing project structure.

When uncertain, preserve consistency with the existing architecture instead of inventing a new pattern.x