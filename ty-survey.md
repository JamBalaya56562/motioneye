# ty (type checker) survey — 2026-10-31

The user would like to add ty to find hidden mistakes; not proposed upstream yet (after the ruff migration, maintainers' consent needed).

## Setup

- ty 0.0.95 (PyPI: `Development Status :: 4 - Beta`), mypy 2.4.1, on `dev@upstream` (`994644c3`), Python 3.12 container with motionEye's deps
- CI already runs mypy on 3.9 to 3.15 (`test_python.yml`: `mypy --install-types --non-interactive --enable-error-code import-untyped .`): 0 issues

## Python 3.9

- `ty check --python-version 3.9` works on the whole project; 3.9 and 3.14 give identical results (150 each); third-party imports resolve
- Probe file: 3.10 syntax (`match`) is reported for 3.9; `itertools.pairwise` (3.10) and a runtime `int | None` annotation without `from __future__ import annotations` are NOT reported
- So 3.9 compatibility still relies on the 3.9 pytest job in CI

## 150 diagnostics on dev (by rule)

| Rule | Count |
|---|---|
| unresolved-attribute | 68 |
| invalid-argument-type | 22 |
| invalid-assignment | 19 |
| unresolved-reference | 13 |
| unsupported-operator | 8 |
| no-matching-overload | 6 |
| invalid-mutable-override | 5 |
| redundant-condition | 3 |
| invalid-method-override | 3 |
| not-subscriptable, invalid-return-type, call-non-callable | 1 each |

Kinds (my reading, all reviewed):
- Untyped module constants in `settings.py` (e.g. `PASSWORD_HOOK = None`) inferred as their literal: "always falsy", invalid assignments in `meyectl.py`. Annotating `settings.py` should remove a whole family (guess)
- Optional not narrowed: `re.match(...).group()`, `Popen.stdin`, `int | None` passed to `os.kill`; mostly safe in practice
- Attributes added at runtime (`Process.progress`), tornado override signatures (`base.py`), `_` from gettext (13; whether ty can declare extra builtins is unverified)
- Real-bug candidates (unverified): `mjpgclient.py:328` `camera_config.get('stream_auth_method') > 0` (None > 0 raises TypeError if the key is missing); `uploadservices.py:720` and `:982` concatenate a possibly None string

mypy finds nothing, probably because by default it does not check the bodies of unannotated functions (guess); ty infers them.

## Possible plan

1. Before: annotate `settings.py` etc., settle `_`, fix real bugs found in separate PRs
2. Add `[tool.ty]` with `python-version = "3.9"`, run it in `test_python.yml` next to mypy (pre-commit hooks lack the project's deps); possibly non-blocking until zero
3. mypy: keep alongside while ty is beta, or replace — maintainers' call
