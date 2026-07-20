from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "SKILL.md", "config/default-rules.md",
    "config/notion-config.example.json", "prompts/book-analysis.md",
    "prompts/task-map.md", "prompts/task-generation.md",
    "prompts/quality-review.md", "templates/project-page.md",
    "templates/task-page.md", "templates/feedback.md",
    "examples/rich-dad-poor-dad/task-map.md",
    "examples/rich-dad-poor-dad/approved-task-samples.md",
    "tests/chapter-coverage.md", "tests/style-checklist.md",
    ".github/workflows/validate-skill.yml",
]

errors = [f"missing: {path}" for path in REQUIRED if not (ROOT / path).is_file()]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not re.match(r"^---\nname: book-pbl-reading-coach\ndescription: .+\n---\n", skill):
    errors.append("SKILL.md frontmatter is invalid")

banned = {".epub", ".pdf", ".mobi", ".key", ".pem"}
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in banned:
        errors.append(f"banned file type: {path.relative_to(ROOT)}")
    if path.is_file() and path.name.startswith(".env") and path.name != ".env.example":
        errors.append(f"secret-like file: {path.relative_to(ROOT)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("repository validation passed")
