# Frontend lint/format (Biome) survey — 2026-10-31

The user's idea, later than the Python tooling (ruff, ty, uv). It may meet opposition: the maintainers may want strict rules for the Python core but none for the frontend JavaScript, so raise it last, if at all.

## Current state (dev@upstream `994644c3`)

- No JS/CSS lint or format at all: no `package.json`, no ESLint/Prettier/Biome/oxlint config, no pre-commit hook for JS
- Hand-written frontend: `main.js` 5,653 lines, `ui.js` 855, `frame.js` 146; CSS 3 files, about 2,000 lines
- Vendored: `jquery.min.js`, `gettext.min.js`; generated: 34 translation JSON files; `templates/main.html` is Jinja2
- Markdown: only `README.md` and `docker/README.md` (the wiki is a separate repo), so Markdown support is not a deciding factor

## Biome 2.6.4 on dev (recommended rules)

- Lint: 213 errors, 355 warnings, 408 infos
  - style: `useArrowFunction` 236, `useLiteralKeys` 220, `useTemplate` 163
  - `noDoubleEquals` 111, `noInnerDeclarations` 89 (old-style JS)
  - possibly real (unverified): `noRedeclare` 6, `noUnusedVariables` 10, `noAssignInExpressions` 5
  - CSS: `noImportantStyles` 16, `noDescendingSpecificity` 4
- Format if applied: about 11,600 changed diff lines in `main.js`, 1,600 in `ui.js`, 1,600 in `main.css`, i.e. nearly every line

## Biome vs oxc

- Biome preferred: one tool and config for JS, CSS and JSON lint + format; oxlint is JS only (guess), and speed does not matter at this size
- Markdown: Biome lists it as Supported, oxfmt formats it too (docs)
- HTML formatting is experimental in Biome; Jinja2 templates must be excluded anyway

## Possible plan

1. Lint only, starting with correctness/suspicious rules, style rules off
2. Format later in one dedicated commit listed in `.git-blame-ignore-revs`, at a time with few open PRs touching `main.js`
3. Exclude vendored libs, translation JSON, Jinja2 templates
