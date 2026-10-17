"""Placeholder threat-intelligence enrichment for the VSOC demo."""


def enrich_threat(threat: str) -> str:
    """Return a clearly labelled placeholder enrichment result.

    No external threat-intelligence feed or CVE database is queried.
    """
    return f"{threat} (demo classification: requires analyst review)"
