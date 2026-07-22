---
name: book-pbl-reading-coach
description: Turn a book into a reusable coached, problem-based learning project with an approved task map, public learning tasks, and hidden grading rubrics. Use when Codex needs to design or revise a book club, guided reading worksheet, PBL learning sheet, chapter-based self-study project, or reusable reading-coach workflow.
---

# Book PBL Reading Coach

Create reader-ready learning sheets and a reusable book package. Keep the book as the bounded knowledge source while training readers to analyze, criticize, redesign, persuade, and act.

## Required inputs

Obtain a lowercase ASCII `book_id`, the display title, the exact edition, a book file or reliable table of contents, target readers, learning purpose, desired difficulty, delivery platform, and privacy or community rules. Never infer chapter numbering from memory. Do not copy substantial copyrighted text; cite chapter ranges and paraphrase ideas.

## Book package contract

Store approved material under `PROJECT_ROOT/books/<book_id>/`:

```text
book.yaml
task-map.md
tasks/task-<task_id>.md
rubrics/task-<task_id>.md
```

`book.yaml` must contain `book_id`, `display_title`, `edition`, and the approved task IDs. Use the ASCII `book_id` in paths and commands; use `display_title` in reader-facing text. A task and its rubric must share the same `task_id`. Keep learner profiles outside this package and outside version control when they contain personal data.

## Workflow

1. Read `prompts/book-analysis.md` and analyze the author, period, intended problem, argument, limits, and chapter structure.
2. Read `prompts/task-map.md` and create a complete task map before drafting any task. Include Task 0 for background and expectations, then cover every assigned chapter exactly once unless a deliberate review is marked.
3. Present the map, edition, and task IDs for approval. Do not publish tasks or rubrics before the reading ranges are verified.
4. Read `prompts/task-generation.md` and draft one public task and its hidden rubric at a time. Keep both as drafts until explicit approval such as `pass`.
5. Read `prompts/quality-review.md` and revise failures before marking the task and rubric approved.
6. Write approved files to the book package. Publish a task to the configured destination only after approval; create one book project page and sequential task subpages when that destination is available.
7. End the book with a synthesis task that turns the earlier judgments into a reusable method or action system.

## Non-negotiable writing rules

Write in natural, complete paragraphs, normally 200–500 Chinese characters per paragraph when the output language is Chinese. Use few headings and avoid one-sentence paragraphs, dense question lists, repetitive transitions, underscores, and AI-outline style. Each task must contain a realistic PBL story with a person, numbers, constraints, trade-offs, and an unresolved decision. The reader must use the assigned chapters to critique, analyze, rewrite, persuade, or design a solution; summary alone is insufficient.

State the exact chapter range and chapter titles for the edition in use. Provide background facts and period context when beginners cannot reasonably research them, then ask readers to judge transferability and limitations. Mark invented cases as fictional but plausible. For personal finance or other sensitive topics, use a 100-unit model and remind readers not to disclose real private data.

Close each task with the problem-solving capability gained, the submission path to the community host or GET Brain, the joint host-and-AI feedback criteria, and the role of anonymized peer discussion. Praise valuable reasoning before escalating challenge. Do not upload original books, copyrighted scans, credentials, API keys, or personal financial data.

## Resources

Use `config/default-rules.md` for defaults and `config/notion-config.example.json` only as a field map. Use `templates/` for book, task, and feedback structures. Use the rich-dad-poor-dad files under `PROJECT_ROOT/books/` as a style reference rather than a source to copy mechanically.
