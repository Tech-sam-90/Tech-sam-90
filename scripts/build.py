#!/usr/bin/env python3
"""Render every output from data/profile.yaml.

    python scripts/build.py            # writes README.md, cv/*.tex, data/profile.json
    python scripts/build.py --check    # fails if outputs are out of date (for CI)

The CV PDF itself is compiled from cv/Samuel_Adeniji_CV.tex by latexmk
(done in the GitHub Action, or locally with `latexmk -pdf`).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, Undefined

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "profile.yaml"
TEMPLATES = ROOT / "templates"

OUTPUTS = {
    "README.md.j2": ROOT / "README.md",
    "cv.tex.j2": ROOT / "cv" / "Samuel_Adeniji_CV.tex",
}
JSON_OUT = ROOT / "data" / "profile.json"

# --------------------------------------------------------------------------
# Lightweight markup: **bold**, *italic*, [text](url), $math$, unicode dashes.
# --------------------------------------------------------------------------
TOKEN = re.compile(
    r"(?P<math>\$[^$]+\$)"
    r"|(?P<bold>\*\*(?P<btext>.+?)\*\*)"
    r"|(?P<ital>(?<!\*)\*(?P<itext>[^*]+?)\*(?!\*))"
    r"|(?P<link>\[(?P<ltext>[^\]]+)\]\((?P<url>[^)\s]+)\))"
)

_TEX_ESCAPES = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}", "<": r"\textless{}", ">": r"\textgreater{}",
}
_TEX_UNICODE = {
    "–": "--", "—": "---", "×": r"$\times$", "≥": r"$\geq$", "≤": r"$\leq$",
    "·": r"$\cdot$", "’": "'", "“": "``", "”": "''", "…": r"\ldots{}",
}


def _tex_plain(s: str) -> str:
    out = "".join(_TEX_ESCAPES.get(c, c) for c in s)
    for k, v in _TEX_UNICODE.items():
        out = out.replace(k, v)
    out = re.sub(r"\bLaTeX\b", r"\\LaTeX{}", out)
    out = re.sub(r"(?<=\.) (?=[a-z])", r"\\ ", out)   # "Dept. of" → inter-word space
    return out


def tex(s) -> str:
    """Markup → LaTeX."""
    if s is None:
        return ""
    s = " ".join(str(s).split())
    out, pos = [], 0
    for m in TOKEN.finditer(s):
        out.append(_tex_plain(s[pos:m.start()]))
        if m.group("math"):
            out.append(m.group("math").replace("–", "--"))
        elif m.group("bold"):
            out.append(r"\textbf{" + tex(m.group("btext")) + "}")
        elif m.group("ital"):
            out.append(r"\emph{" + tex(m.group("itext")) + "}")
        else:
            url = m.group("url").replace("%", r"\%").replace("#", r"\#")
            out.append(r"\href{" + url + "}{" + tex(m.group("ltext")) + "}")
        pos = m.end()
    out.append(_tex_plain(s[pos:]))
    return "".join(out)


def md(s) -> str:
    """Markup → GitHub Markdown (already markdown; just normalise whitespace)."""
    return "" if s is None else " ".join(str(s).split())


def plain(s) -> str:
    """Markup → plain text (for the website JSON `*_plain` fields)."""
    if s is None:
        return ""
    s = " ".join(str(s).split())
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("**", "")
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", s)
    s = re.sub(r"\$([^$]+)\$", lambda m: m.group(1).replace("{", "").replace("}", ""), s)
    return s


# --------------------------------------------------------------------------
# Author helpers
# --------------------------------------------------------------------------
def initials(name: str) -> str:
    """'Samuel Akinwumi Adeniji' → 'S. A. Adeniji'; 'Chris-Victor Ntwali' → 'C.-V. Ntwali'.
    Names that are already abbreviated ('K. E. Jack') pass through."""
    parts = name.split()
    if len(parts) == 1:
        return name
    given, last = parts[:-1], parts[-1]
    abbr = []
    for g in given:
        if re.fullmatch(r"[A-Z]\.", g):
            abbr.append(g)
        else:
            abbr.append("-".join(p[0] + "." for p in g.split("-")))
    return " ".join(abbr + [last])


def make_env(data: dict) -> Environment:
    me = data["person"]["name"]

    def cv_authors(authors):
        out = []
        for a in authors:
            t = tex(initials(a)).replace(". ", ".~")
            out.append(r"\textbf{" + t + "}" if a == me else t)
        return ", ".join(out)

    def md_authors(authors):
        return ", ".join(f"**{a}**" if a == me else a for a in authors)

    filters = {"tex": tex, "md": md, "plain": plain,
               "cv_authors": cv_authors, "md_authors": md_authors}
    return filters


def render_all(data: dict) -> dict[Path, str]:
    filters = make_env(data)
    results = {}
    for tpl_name, out_path in OUTPUTS.items():
        if tpl_name.endswith(".tex.j2"):
            # LaTeX-friendly delimiters so braces and % don't clash with Jinja.
            env = Environment(
                loader=FileSystemLoader(TEMPLATES), undefined=Undefined,
                block_start_string="<%", block_end_string="%>",
                variable_start_string="<<", variable_end_string=">>",
                comment_start_string="<#", comment_end_string="#>",
                trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True,
            )
        else:
            env = Environment(loader=FileSystemLoader(TEMPLATES), undefined=Undefined,
                              trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
        env.filters.update(filters)
        results[out_path] = env.get_template(tpl_name).render(**data)
    results[JSON_OUT] = build_json(data)
    return results


def build_json(data: dict) -> str:
    """Website-facing JSON: the same data, with plain-text twins of marked-up fields."""
    def walk(x):
        if isinstance(x, dict):
            out = {}
            for k, v in x.items():
                out[k] = walk(v)
                if k in {"bio", "summary", "note"} and isinstance(v, str):
                    out[k + "_plain"] = plain(v)
            return out
        if isinstance(x, list):
            return [walk(v) for v in x]
        return x

    payload = walk(data)

    # Site-ready extras, so the website needs no formatting logic of its own.
    me = data["person"]["name"]
    pubs_by_id = {p["id"]: p for p in data.get("publications", []) if p.get("id")}
    for pub in payload.get("publications", []):
        pub["authors_initials"] = ", ".join(initials(a) for a in pub["authors"])
        pub["self_index"] = pub["authors"].index(me) if me in pub["authors"] else -1
        parts = [pub.get("short_venue") or pub.get("venue")]
        if pub.get("details") and not pub.get("short_venue"):
            parts.append(pub["details"])
        venue = ", ".join(x for x in parts if x)
        if pub.get("note"):
            venue += f" ({pub['note']})"
        pub["venue_display"] = venue
        links = list(pub.get("links", []))
        if pub.get("doi"):
            links.append({"label": "DOI", "url": f"https://doi.org/{pub['doi']}"})
        pub["links"] = links
    for section in ("experience", "teaching", "projects"):
        for item in payload.get(section, []):
            if "bullets" in item:
                item["bullets_plain"] = [plain(b) for b in item["bullets"]]
            if section == "projects":
                pub = pubs_by_id.get(item.get("publication"))
                item["paper_links"] = [l for l in pub.get("links", []) if l["label"] != "Code"] if pub else []

    payload["generated_from"] = "data/profile.yaml"
    payload["cv_pdf"] = "cv/Samuel_Adeniji_CV.pdf"
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if outputs are stale")
    args = ap.parse_args()

    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    results = render_all(data)

    stale = []
    for path, content in results.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            stale.append(path.relative_to(ROOT))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")

    if args.check and stale:
        print("Out of date:", *stale, sep="\n  ")
        return 1
    print("Updated:" if stale else "Everything up to date.", *stale, sep="\n  ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
