# ULTRA-Z Project Context

Version: 1.0

Status: Active Development

---

# Project Overview

ULTRA-Z is a modular AI Operating System designed to function as a true personal digital assistant.

The goal is not to build a chatbot.

The goal is to build an intelligent assistant capable of understanding the user, remembering information, reasoning about tasks, automating workflows, interacting with the operating system, and continuously improving over time.

ULTRA-Z is designed as a long-term production project following modern software engineering principles.

---

# Core Vision

The assistant should behave like a real digital companion.

It should be able to:

- Hold natural conversations
- Remember previous interactions
- Learn from experience
- Plan tasks
- Execute workflows
- Use tools
- Control the operating system
- Browse the web
- Understand documents
- Understand images
- Automate repetitive work
- Continuously improve itself

The system should be modular, scalable, maintainable and easily extensible.

---

# Development Philosophy

Architecture First.

Implementation Second.

Testing Third.

Optimization Fourth.

Never skip phases.

Every feature must fit into the existing architecture.

Avoid quick fixes that violate long-term maintainability.

---

# Technology Stack

Backend

- Python
- FastAPI
- uv
- SQLAlchemy
- SQLite (development)
- PostgreSQL (future)

Frontend

- Electron
- React
- Vite
- TypeScript (planned)

AI Runtime

- Ollama (primary local runtime)
- OpenAI (future optional provider)
- Gemini (future optional provider)
- Anthropic (future optional provider)

Speech

- Faster-Whisper (Speech-to-Text)
- Piper (Text-to-Speech)

Automation

- Playwright
- PyAutoGUI
- Platform-specific OS integrations

Database

- SQLite
- PostgreSQL (future)

Testing

- pytest

Formatting

- Ruff
- Black

---

# High-Level Architecture

The backend is organized into independent modules.

Each module owns its own responsibility.

Major modules include:

Assistant
Memory
Runtime
Cognition
Workflow
Tools
Plugins
Database
Security
Events
State
API

Modules communicate through interfaces, events, or clearly defined service boundaries.

Avoid tight coupling.

---

# Responsibilities

Assistant

Coordinates all user interactions.

Memory

Stores conversations, knowledge, preferences and relationships.

Runtime

Communicates with AI providers and executes model inference.

Cognition

Responsible for reasoning, planning, goals, strategies and decision making.

Workflow

Executes multi-step tasks.

Tools

Provides capabilities such as browser automation, file operations, desktop control and system interaction.

Plugins

Allows future extensibility.

Events

Handles asynchronous communication.

State

Tracks the assistant lifecycle and execution state.

Database

Handles persistence.

Security

Authentication, authorization and secret management.

API

HTTP and WebSocket communication.

---

# Design Principles

Single Responsibility Principle

Open/Closed Principle

Dependency Injection

Event-Driven Communication

Loose Coupling

High Cohesion

Feature-Based Organization

Composition over Inheritance

Explicit Dependencies

Testability First

---

# Coding Standards

Use Python 3.12+

Use type hints everywhere.

Prefer async code for I/O.

Avoid global state.

Keep functions focused.

Keep classes focused.

Use dependency injection.

Avoid circular imports.

Do not duplicate business logic.

Business logic belongs in services.

Persistence belongs in repositories.

Validation belongs in schemas.

Routes should remain thin.

---

# Performance Goals

Fast startup.

Low memory usage.

Efficient asynchronous execution.

Lazy loading where appropriate.

Reuse expensive resources.

Avoid blocking operations.

---

# Security Goals

Never hardcode secrets.

Validate all external input.

Least privilege.

Secure configuration.

Protect user data.

Support local-first privacy.

---

# Memory Philosophy

Memory is a first-class system.

The assistant should remember:

- Conversations
- User preferences
- Long-term knowledge
- Relationships
- Learned facts
- Experiences
- Reflections

Memory should evolve over time.

---

# AI Runtime Philosophy

The runtime should support multiple providers.

Providers should be interchangeable.

The rest of the application should never depend on a specific AI provider.

Use interfaces to abstract provider implementations.

---

# Workflow Philosophy

Large tasks should be decomposed into smaller executable steps.

Workflows should support:

- Planning
- Execution
- Monitoring
- Recovery
- Completion

---

# Event Philosophy

Modules should communicate through events whenever practical.

Avoid direct dependencies between unrelated systems.

Events should be observable and traceable.

---

# Development Workflow

Every new feature follows this order:

1. Design
2. Architecture Review
3. Folder Structure
4. Implementation
5. Unit Tests
6. Integration Tests
7. Documentation
8. Code Review
9. Git Commit

---

# Long-Term Roadmap

Phase 1

Backend Foundation

Phase 2

Runtime

Phase 3

Memory

Phase 4

Cognition

Phase 5

Workflow Engine

Phase 6

Tool System

Phase 7

Plugin Platform

Phase 8

Desktop Application

Phase 9

Continuous Learning

Phase 10

Optimization and Release

---

# Current Development Status

Architecture: Complete

Project Management: Complete

Backend Foundation: In Progress

Current Module: Project Initialization

Current Priority:

Build a clean, production-grade backend foundation before implementing AI features.

---

# Expected Code Quality

Every contribution should be:

- Production-ready
- Readable
- Modular
- Testable
- Maintainable
- Well documented
- Consistent with the existing architecture

Avoid shortcuts.

Prioritize long-term maintainability over short-term speed.

When uncertain, preserve the existing architecture rather than inventing a new pattern.

---

# What ULTRA-Z Is Not

ULTRA-Z is not:

- A simple chatbot
- A single LLM wrapper
- A collection of scripts
- A prototype
- A proof of concept

ULTRA-Z is a complete AI Operating System designed for long-term evolution.

Every implementation decision should support that vision.