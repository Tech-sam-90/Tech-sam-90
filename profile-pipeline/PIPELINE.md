# Profile pipeline

One file, `data/profile.yaml`, drives everything:

| Output | Built by | Where it shows up |
|---|---|---|
| `README.md` | `scripts/build.py` + `templates/README.md.j2` | GitHub profile page |
| `cv/Samuel_Adeniji_CV.tex` → `.pdf` | `templates/cv.tex.j2` + LaTeX | CV (same design as before) |
| `data/profile.json` | `scripts/build.py` | Website, read at build time |

## Everyday use

1. Edit `data/profile.yaml` (on github.com is fine: pencil icon → commit).
2. The **Build profile** Action runs. It regenerates the README, compiles the CV PDF,
   commits both, and pings Vercel to rebuild the website.

Never edit `README.md`, `cv/*.tex` or `profile.json` by hand: they are overwritten on
every build. To change layout, edit the templates in `templates/`.

## Writing text in the YAML

- `**bold**`, `*italic*`, `[text](https://url)` work everywhere.
- Use real characters: `–` for ranges, `—` for asides, `×`, `≥`. LaTeX escaping
  (`%`, `&`, `_`, …) is automatic.
- `$K{=}32$` is inline math: LaTeX in the CV, rendered by GitHub in the README.
- Author lists use full names; the CV abbreviates them (`S. A. Adeniji`) and your name
  is bolded automatically. Hyphenate double given names (`Chris-Victor`) to get `C.-V.`.

Per-item switches:

- `projects[].on_cv` / `on_readme`: where a project appears.
- `projects[].summary` (GitHub/website) vs `bullets` (CV): keep these two in step when a
  result changes. They sit next to each other in the file for that reason.
- `publications[].selected: true`: also listed on GitHub and the website.
- `skills[].readme: true`: group included in the GitHub "Tools" line.

## Build locally (optional)

```bash
pip install -r requirements.txt
python scripts/build.py                 # README.md, cv/*.tex, data/profile.json
cd cv && latexmk -pdf Samuel_Adeniji_CV.tex
python scripts/build.py --check         # exit 1 if generated files are stale
```

## One-time setup

1. Copy these files into the `Tech-sam-90/Tech-sam-90` repo (the profile repo).
2. **Settings → Actions → General → Workflow permissions →** *Read and write*.
3. In Vercel: project → Settings → Git → **Deploy Hooks** → create one for `main`.
   Add its URL to the profile repo as secret **`VERCEL_DEPLOY_HOOK`**.
4. Point the website at the data (see below).

## Website hookup

The website reads the public JSON and CV straight from the profile repo:

```ts
const BASE = "https://raw.githubusercontent.com/Tech-sam-90/Tech-sam-90/main";

export async function getProfile() {
  const res = await fetch(`${BASE}/data/profile.json`);
  if (!res.ok) throw new Error(`profile.json: ${res.status}`);
  return res.json();
}

export const CV_URL = `${BASE}/cv/Samuel_Adeniji_CV.pdf`;
```

Fetch it at build time, so the site stays static and fast, and render
`person.bio`, `projects`, `publications` and so on. Fields with markup also come
with a `*_plain` twin (`summary_plain`, `bio_plain`) for places where links and bold
aren't wanted.

## Not automated

- **LinkedIn** has no API for editing a profile. After a significant change, update
  the headline, About and Featured sections by hand.
- **Google Scholar** indexes papers on its own.
