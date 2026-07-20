---
name: book-pbl-reading-coach
description: Turn a book into a coached, problem-based learning project with verified chapter coverage, realistic cases, critical reading, sequential approval, community discussion, AI feedback, and optional Notion delivery. Use when Codex needs to design or revise a book club, guided reading worksheet, PBL learning sheet, chapter-based self-study project, or reusable reading-coach workflow.
---

# Book PBL Reading Coach

Create reader-ready learning sheets, not internal course outlines. Preserve the book as the bounded knowledge source while training readers to analyze, criticize, redesign, persuade, and act.

## Required inputs

Obtain the book file or a reliable table of contents, the exact edition, target readers, learning purpose, desired difficulty, delivery platform, and any privacy or community rules. Never infer chapter numbering from memory. Do not copy substantial copyrighted text; cite chapter ranges and paraphrase ideas.

## Workflow

1. Read `prompts/book-analysis.md` and analyze the author, period, intended problem, argument, limits, and chapter structure.
2. Read `prompts/task-map.md` and create a complete task map before drafting any task. Include Task 0 for background and expectations, then cover every assigned chapter exactly once unless a deliberate review is marked.
3. Present the map for approval. Do not publish tasks before the map and reading ranges are verified.
4. Read `prompts/task-generation.md` and draft one task at a time. Stop after each task and wait for explicit approval such as `pass`.
5. Read `prompts/quality-review.md`, run the checks in `tests/`, and revise failures before delivery.
6. After approval, publish the task to the configured destination. Create one book project page and sequential task subpages. Never place tokens or book files in the repository or destination configuration.
7. End the book with a synthesis task that turns the earlier judgments into a reusable method or action system.

## Non-negotiable writing rules

Write in natural, complete paragraphs, normally 200–500 Chinese characters per paragraph when the output language is Chinese. Use few headings and avoid one-sentence paragraphs, dense question lists, repetitive transitions, underscores, and AI-outline style. Each task must contain a realistic PBL story with a person, numbers, constraints, trade-offs, and an unresolved decision. The reader must use the assigned chapters to critique, analyze, rewrite, persuade, or design a solution; summary alone is insufficient.

State the exact chapter range and chapter titles for the edition in use. Provide background facts and period context when beginners cannot reasonably research them, then ask readers to judge transferability and limitations. Mark invented cases as fictional but plausible. For personal finance or other sensitive topics, use a 100-unit model and remind readers not to disclose real private data.

Close each task with the problem-solving capability gained, the submission path to the community host or GET Brain, the joint host-and-AI feedback criteria, and the role of anonymized peer discussion. Praise valuable reasoning before escalating challenge. Do not upload original books, copyrighted scans, credentials, API keys, or personal financial data.

## Resources

Use `config/default-rules.md` for defaults and `config/notion-config.example.json` only as a field map. Use `templates/` for book, task, and feedback structures. Use `examples/rich-dad-poor-dad/` as a style reference rather than a source to copy mechanically. Run `tests/validate_repository.py` before publishing repository changes.
