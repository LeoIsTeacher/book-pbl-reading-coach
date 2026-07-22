from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    ".agents/skills/book-pbl-reading-coach/SKILL.md",
    ".agents/skills/book-pbl-reading-coach/agents/openai.yaml",
    ".agents/skills/book-pbl-reading-coach/config/default-rules.md",
    ".agents/skills/book-pbl-reading-coach/prompts/book-analysis.md",
    ".agents/skills/book-pbl-reading-coach/prompts/task-map.md",
    ".agents/skills/book-pbl-reading-coach/prompts/task-generation.md",
    ".agents/skills/book-pbl-reading-coach/prompts/quality-review.md",
    ".agents/skills/assignment-feedback-coach/SKILL.md",
    ".agents/skills/assignment-feedback-coach/references/growth-profile.md",
    "books/_template/book.yaml",
    "books/rich-dad-poor-dad/book.yaml",
    "books/rich-dad-poor-dad/task-map.md",
    ".github/workflows/validate-skill.yml",
]

errors = [f"missing: {path}" for path in REQUIRED if not (ROOT / path).is_file()]

for skill_name in ("book-pbl-reading-coach", "assignment-feedback-coach"):
    skill = ROOT / ".agents" / "skills" / skill_name / "SKILL.md"
    if skill.is_file() and not re.match(
        rf"^---\nname: {re.escape(skill_name)}\ndescription: .+\n---\n",
        skill.read_text(encoding="utf-8"),
    ):
        errors.append(f"{skill_name} frontmatter is invalid")

for task_id in range(9):
    rubric = ROOT / "books" / "rich-dad-poor-dad" / "rubrics" / f"task-{task_id}.md"
    if not rubric.is_file():
        errors.append(f"missing rich-dad-poor-dad rubric: task-{task_id}")

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
