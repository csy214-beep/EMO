# AGENTS.md

Personal emoticon/sticker library. The actual content is image files under `emo/`; there is no application code to run.

## Structure

- `emo/<category>/` — the sticker library. Each subfolder is a category; drop image files here. This is the primary "content" of the repo.
- `emoCut.py` — interactive image-splitting tool (uses `pillow`; `pip install -r requirements.txt`). Run `python emoCut.py`, prompts for an image, rows/cols, optional overlap/aspect-ratio. Outputs `tiles` + `info.txt` to `<name>_split_{rows}x{cols}/`.
- `scripts/update_stats.py` — regenerates the folder-count table in `README.md` between `<!-- stats_start -->` / `<!-- stats_end -->`.
- `scripts/generate_gallery.py` + `scripts/template.html` — builds a static `index.html` gallery in the repo root (placeholder `{{ DATA }}`).

## Gotchas

- **Do NOT hand-edit the stats block in `README.md`.** `update_stats.yml` (GitHub Actions, runs on push to `master`) regenerates and auto-commits it with `[skip ci]`.
- **`deploy-gallery.yml` is misplaced** at `.github/deploy-gallery.yml` instead of `.github/workflows/`, so the gallery deploy workflow currently never runs. Keep new workflows in `.github/workflows/`.
- **Default branch is `master`**, not `main`.
- **Filenames are non-ASCII and punctuation-heavy** (Chinese/Japanese, spaces, `！？（）`). Always quote paths in shell commands. `emoCut.py` uses CJK output messages.
- `.gitignore` ignores `**/bilibili超かぐや姫！`; `update_stats.py` skips files starting with `.preview` and `.html/.psd/.txt/.md/.url`.
- `scripts/*.py` are stdlib-only (no deps). Only `emoCut.py` needs `pillow`.

## Verify locally

- `python scripts/update_stats.py` — refresh README stats.
- `python scripts/generate_gallery.py` — (re)generate `index.html`, then open it in a browser.

No tests, lint, or typecheck config exists.