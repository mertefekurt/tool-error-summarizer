# Tool Error Summarizer

Tool Error Summarizer is meant for quick pull-request checks around tooling reviews. It favors explicit rules over a bulky dashboard.

![Tool Error Summarizer cover](assets/readme-cover.svg)

## Rule ledger

- `auth-denied` - authorization failure detected (high); Check scopes, credentials, and tenant access..
- `timeout` - timeout failure detected (medium); Review retries, latency budget, and upstream health..
- `schema-mismatch` - schema validation failure detected (low); Update tool schema or argument generation..

## Finding map

![Workflow diagram](assets/readme-diagram.svg)

## Command path

```bash
git clone https://github.com/mertefekurt/tool-error-summarizer.git
cd tool-error-summarizer
python -m pip install -e ".[dev]"
tool-error-summarizer examples/sample.txt
```

## Maintenance rhythm

```bash
ruff check .
pytest
python -m tool_error_summarizer --help
```
