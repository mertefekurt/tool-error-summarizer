# tool-error-summarizer

**Data Sheet.** Summarize automation tool error logs into retry, auth, timeout, and schema findings.

## Inputs

Tool-call failures are noisy. This CLI converts raw error snippets into a compact operational report.

## Processing

`tool-error-summarizer` accepts tool error logs or JSONL traces in text, JSON, JSONL, or CSV form.

## Outputs

```bash
python -m pip install -e ".[dev]"
tool-error-summarizer examples/sample.txt
tool-error-summarizer examples/sample.txt --json --fail-on medium
```

## Failure Modes

| Rule | Severity | Meaning |
|---|---:|---|
| `auth-denied` | high | authorization failure detected |
| `timeout` | medium | timeout failure detected |
| `schema-mismatch` | low | schema validation failure detected |

## Verification

```bash
ruff check .
pytest
python -m tool_error_summarizer --help
```

License: MIT

### Example Input

```text
tool fetch failed timeout retry exhausted auth denied schema mismatch
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the tool-error-summarizer policy surface explicit.
