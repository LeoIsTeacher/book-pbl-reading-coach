# Book PBL Reading Coach

这个仓库包含两个可复用的项目级 Skill：一个负责把书籍转化为教练式 PBL 共读项目，另一个依据已确认的任务与批改标准反馈学员作业。原书文件、访问令牌和个人隐私数据不进入仓库。

## Skills

- `.agents/skills/book-pbl-reading-coach/`：创建书籍分析、任务地图、任务0、公开任务与隐藏批改标准，并在拆书时同步保存。
- `.agents/skills/assignment-feedback-coach/`：根据指定书籍、任务、隐藏批改标准和成员姓名生成教练式反馈，并在确认发送后更新成长档案。

## 书籍包

每本书使用一个稳定的 ASCII `book_id`，读者界面继续使用中文或其他语言的 `display_title`：

```text
books/<book_id>/
├── book.yaml
├── task-map.md
├── tasks/
│   └── task-<task_id>.md
└── rubrics/
    └── task-<task_id>.md
```

`book.yaml` 记录书名、任务编号和书籍包状态，不要求出版社、出版年份、译者或其他版本元数据。任务设计 Skill 写入已确认的任务与批改标准；反馈 Skill 只读取当前 `book_id` 与 `task_id` 对应的文件，不混用其他书籍或版本的材料。`books/_template/` 提供新书的起始目录。

## 当前书籍包

- `books/rich-dad-poor-dad/`：`display_title` 为《富爸爸穷爸爸》，包含任务地图、任务0至任务8的公开任务和隐藏批改标准。

## 安全边界

不要提交 EPUB、PDF、扫描件、长篇原文、`.env`、Notion Token、API Key 或真实财务数据。成长档案存放在受控的私有工作区，不进入这个仓库。
