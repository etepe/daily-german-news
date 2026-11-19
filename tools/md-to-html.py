#!/usr/bin/env python3
"""Turn a news sheet (markdown) into email-ready HTML.

Usage:  python3 tools/md-to-html.py sheets/2026-11-17.md > sheet.html

Standard library only. The output goes to stdout; use it as the HTML body
of an email.

Why a script: a sheet is over 10 KB and holds hundreds of German words.
Having a model convert it by hand risks silent letter errors every time.
"""
import html
import re
import sys

LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ONLY_LINK = re.compile(r"^\[[^\]]+\]\([^)]+\)$")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
CODE = re.compile(r"`([^`]+)`")

A = ' style="color:#1558d6"'
MONO = (
    ' style="font-family:ui-monospace,Menlo,monospace;font-size:.9em;'
    'background:#f1f3f4;padding:0 3px;border-radius:3px"'
)


def inline(text):
    """Inline markdown -> HTML. Escape first, then mark up."""
    out = html.escape(text, quote=False)
    out = LINK.sub(lambda m: f'<a href="{m.group(2)}"{A}>{m.group(1)}</a>', out)
    out = BOLD.sub(r"<strong>\1</strong>", out)
    out = CODE.sub(rf"<code{MONO}>\1</code>", out)
    return out


def glossary_item(text):
    """For `Wort – gloss`, bold the German; anything else stays as it is."""
    parts = text.split(" – ", 1)
    if len(parts) == 2 and not parts[0].startswith("["):
        return f"<strong>{inline(parts[0])}</strong> – {inline(parts[1])}"
    return inline(text)


def convert(md):
    out = [
        '<div style="font-family:-apple-system,BlinkMacSystemFont,'
        '\'Segoe UI\',Roboto,sans-serif;font-size:17px;line-height:1.55;'
        'max-width:640px;color:#202124">'
    ]
    para, items = [], []

    def flush():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()
        if items:
            out.append('<ul style="padding-left:20px;margin:12px 0">')
            out.extend(f"<li>{glossary_item(i)}</li>" for i in items)
            out.append("</ul>")
            items.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
        elif line.startswith("## "):
            flush()
            out.append(
                '<h2 style="font-size:18px;margin:30px 0 10px">'
                f"{inline(line[3:])}</h2>"
            )
        elif line.startswith("# "):
            flush()
            out.append(
                '<h1 style="font-size:21px;margin:0 0 4px">'
                f"{inline(line[2:])}</h1>"
            )
        elif line.startswith("---"):
            flush()
            out.append('<hr style="border:0;border-top:1px solid #dadce0;margin:26px 0">')
        elif ONLY_LINK.match(line.strip()):
            flush()
            out.append(
                '<p style="font-size:14px;margin:8px 0 0">'
                f"{inline(line.strip())}</p>"
            )
        elif line.startswith("* ") or line.startswith("- "):
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para.clear()
            items.append(line[2:].strip())
        else:
            if items:
                flush()
            para.append(line.strip())

    flush()
    out.append("</div>")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: md-to-html.py <sheet.md>")
    with open(sys.argv[1], encoding="utf-8") as fh:
        print(convert(fh.read()))
