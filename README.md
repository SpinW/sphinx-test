# SpinW Sphinx Docs

This repository builds a Sphinx documentation site for SpinW, pySpinW, and
SpinWcore.

## Sphinx setup

- Source directory: `docs/`
- Entry page: `docs/index.rst`
- Config file: `docs/conf.py`
- Theme: `pydata_sphinx_theme`
- Extensions:
  - `sphinx.ext.autodoc` for the generated pySpinW API page
  - `sphinx.ext.autosummary`
  - `sphinx.ext.napoleon`
  - `sphinx.ext.mathjax` for equations
  - `myst_parser` (with `dollarmath` and `deflist`) for Markdown sources
- Custom CSS: `docs/_static/site.css`

## Customizations

On top of the pydata-sphinx-theme defaults, `site.css` styles homepage-specific
elements:

- `project-cards` / `project-card` grid for the project tiles, with hover states
- `project-logo` and `project-badges` layout inside each card
- `partner-table` / `partner-logo` sizing for the partner logo grid
- navbar spacing tweaks (`.bd-navbar-elements.navbar-nav`)

## Migration progress (from spinw.org)

The current docs site renovates the legacy https://spinw.org Jekyll site
(source: `../spinw.github.io`). The old site exposes **392 URLs** via its
sitemap. Status of the migration as of 2026-06-26:

| Area | Old-site pages | Migrated | Status | Notes |
|---|---|---|---|---|
| Landing (homepage) | 1 | 1 | ✅ done | `docs/index.rst` — cards, logos, badges all ported |
| About / Maintainers (`/aboutme/`) | 1 | 0 | ⛔ not started | Plan: fold into `docs/resources/contact.rst` as an "About" subsection |
| FAQ | 1 | 1 | ✅ done | `docs/resources/faq.rst` |
| Support / Contact | 1 | 1 | ✅ done | `docs/resources/contact.rst` |
| MATLAB Installation | 1 | 1 | ✅ done | `docs/spinw/installation.md` |
| Python Installation | 1 | 1 | ✅ done | `docs/pyspinw/installation.rst` |
| News (index + posts) | 7 | 7 | ✅ done | All 6 dated posts in `docs/news_posts/` |
| Publications / Citing SpinW | 86 | 1 | ✅ done | `docs/resources/citing.rst` — canonical Toth & Lake (2015) citation + live Dimensions badge linking to the up-to-date citing-papers list |
| Presentations (10 talks) | 11 | 0 | ⛔ not started | `docs/resources/presentations.rst` is a stub; sources in `../spinw.github.io/pages/_presentations/` |
| MATLAB Tutorials | 33 | 31 | 🟡 partial | 31 numbered tutorials ported under `docs/spinw/tutorials/`. Old site had Python-tutorials hub and pySpinW-examples hub not yet covered separately |
| pySpinW overview | 1 | 1 | ✅ done | `docs/pyspinw/overview.rst` |
| pySpinW examples | 1 | 1 | 🟡 partial | `docs/pyspinw/examples.rst` links to GitHub only — does not inline the example output |
| Python API (`/pythonapi.html`) | 1 | 1 | 🟡 partial | `docs/api/pySpinW.rst` invokes `automodule`; requires `../pySpinW` importable to render |
| SpinW class overview (`/SWclass/`, `/core-classes/`) | 2 | 1 | 🟡 partial | `docs/spinw/class.md` covers the overview; the `/core-classes/` hub page is not separately ported |
| SpinW properties (`/SWproperties/`) | 1 | 1 | ✅ done | `docs/spinw/properties.md` |
| `spinw` class methods reference | 76 | 0 | ⛔ not started | Section index `docs/spinw/methods.rst` exists (globbed toctree, empty). Sources: `../spinw.github.io/pages/_spinw/` (76 MD files) |
| `swfiles` / `sw_*` namespace | 50 | 0 | ⛔ not started | Section index `docs/spinw/files.rst` exists. Sources: `../spinw.github.io/pages/_swfiles/` (54 MD files) |
| `swfunc` (lineshapes) | 6 | 0 | ⛔ not started | No section index yet. Sources: `../spinw.github.io/pages/_swfunc/` (6 files) |
| `swplot` namespace | 43 | 0 | ⛔ not started | Section index `docs/spinw/plot.rst` exists. Sources: `../spinw.github.io/pages/_swplot/` (44 files) |
| `swpref` namespace | 25 | 0 | ⛔ not started | Section index `docs/spinw/pref.rst` exists. Sources: `../spinw.github.io/pages/_swpref/` (25 files) |
| `swsym` namespace | 11 | 0 | ⛔ not started | Section index `docs/spinw/sym.rst` exists. Sources: `../spinw.github.io/pages/_swsym/` (11 files) |
| `ndbase` namespace | 12 | 0 | ⛔ not started | No section index yet. Sources: `../spinw.github.io/pages/ndbase/` (12 files) |
| SpinWcore (C++) | 0 | 0 | ⛔ not started | `docs/spinwcore.rst` is a placeholder; old site had no dedicated section (forward-looking gap) |
| Tag pages (`/tags/*`, `/tag_*.html`) | 12 | 0 | ❌ dropped | Jekyll-theme defaults, not content |
| **Total** | **~392** | **~50** | | |

### Known gaps

The four largest blockers, in priority order:

1. **MATLAB function reference (~245 pages)** — the entire `spinw_*`, `sw_*`,
   `swfunc_*`, `swplot_*`, `swpref_*`, `swsym_*`, `ndbase_*` namespaces. Source
   markdown for every page exists in `../spinw.github.io/pages/_*/` (228 files
   total). Will be auto-ported by a generator script.
2. **85 publications** — single structured-data file at
   `../spinw.github.io/publications.json` (44 KB, JSON) carries title /
   authors / journal / DOI / date for all entries. Consolidate to one
   `docs/resources/publications.rst` grouped by year.
3. **10 presentation pages** — source MD at
   `../spinw.github.io/pages/_presentations/`. Port one-to-one as
   `docs/resources/presentations/*.rst`.
4. **Python API `automodule` rendering** — `docs/api/pySpinW.rst` emits empty
   output unless `../pySpinW` is importable inside the `uv` env.

### Next steps

In execution order (see `~/.claude/plans/the-current-website-in-sleepy-mountain.md`
for the full plan):

1. Wire up the Python API page so `automodule` actually renders.
2. Generate `docs/resources/publications.rst` from
   `../spinw.github.io/publications.json`.
3. Port the 10 presentation pages into `docs/resources/presentations/`.
4. Run a generator script that converts the 228 MATLAB function-reference MD
   files from `../spinw.github.io/pages/_*/` into the corresponding
   `docs/spinw/{methods,files,plot,pref,sym,func,ndbase}/` trees. The
   globbed toctrees in the existing section index files (`methods.rst`,
   `files.rst`, `plot.rst`, `pref.rst`, `sym.rst`) will pick them up
   automatically; add `func.rst` and `ndbase.rst` indexes.
5. Add intro paragraphs to the bare section indexes
   (`docs/spinw/index.rst`, `docs/pyspinw/index.rst`,
   `docs/resources/index.rst`), fold `/aboutme/` into
   `docs/resources/contact.rst`, fix the `<sript>` typo in
   `docs/spinw/class.md`, and correct the tutorial count in
   `docs/spinw/tutorials.md`.

