<img src="assets/readme-cover.svg" alt="Tool Error Summarizer cover" width="100%" />

# Tool Error Summarizer

Summarize automation tool error logs into retry, auth, timeout, and schema findings.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `tool-error-summarizer` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `auth-denied` | high | authorization failure detected |
| `timeout` | medium | timeout failure detected |
| `schema-mismatch` | low | schema validation failure detected |

## Command line

```bash
python -m pip install -e ".[dev]"
tool-error-summarizer examples/sample.txt
tool-error-summarizer examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
tool fetch failed timeout retry exhausted auth denied schema mismatch
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
