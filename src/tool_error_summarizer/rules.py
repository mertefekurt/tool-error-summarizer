from __future__ import annotations

from tool_error_summarizer.models import Rule

PROJECT_NAME = 'tool-error-summarizer'
SUMMARY = 'Summarize automation tool error logs into retry, auth, timeout, and schema findings.'
SAMPLE_RISK = 'tool fetch failed timeout retry exhausted auth denied schema mismatch'
SAMPLE_CLEAN = 'tool fetch success duration 120ms status ok'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='auth-denied',
        severity='high',
        pattern='\\bauth denied|permission denied|401|403\\b',
        message='authorization failure detected',
        recommendation='Check scopes, credentials, and tenant access.',
    ),
    Rule(
        code='timeout',
        severity='medium',
        pattern='\\btimeout|deadline exceeded\\b',
        message='timeout failure detected',
        recommendation='Review retries, latency budget, and upstream health.',
    ),
    Rule(
        code='schema-mismatch',
        severity='low',
        pattern='\\bschema mismatch|invalid schema|validation failed\\b',
        message='schema validation failure detected',
        recommendation='Update tool schema or argument generation.',
    ),
)
