"""Generate the public HTML page and preserve the original Markdown."""

from html import escape
from pathlib import Path
import re
from shutil import copyfile
from string import Template

import markdown


def main():
    root = Path(__file__).resolve().parent
    source = (root / "index.md").read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", source, re.MULTILINE)
    summary = re.search(r"^> (.+)$", source, re.MULTILINE)
    if title is None or summary is None:
        raise ValueError("index.md must include a title and a one-line summary.")

    content = markdown.markdown(source, extensions=["tables", "toc", "sane_lists"])
    template = Template((root / "site/template.html").read_text(encoding="utf-8"))
    page = template.substitute(
        title=escape(title.group(1), quote=True),
        description=escape(summary.group(1), quote=True),
        content=content,
    )

    output = root / "dist"
    output.mkdir(exist_ok=True)
    (output / "index.html").write_text(page, encoding="utf-8")
    copyfile(root / "index.md", output / "index.md")
    copyfile(root / "site/style.css", output / "style.css")
    print("Built dist/index.html, dist/index.md, and dist/style.css")


if __name__ == "__main__":
    main()
