# MicroSaaS Exit Kit

**Signature:** Mourad.Soltani

A minimal, shippable CLI tool for solo founders preparing to sell or hand off a micro-SaaS. Generates structured **buyer notes** and **one-to-one outreach templates**.

## Features
- Generate professional buyer notes Markdown
- Generate personalized (one-to-one only) outreach templates
- Health check flag
- Pure Python (stdlib only) — no dependencies
- Includes health tests

## Quick Start
```bash
python exitkit.py --product "MyTool" --niche "docs sync" --mrr 500 --features "CLI" "Tests"
```

Outputs:
- `BUYER_NOTES.md`
- `OUTREACH_TEMPLATES.md`

Health check:
```bash
python exitkit.py --health
```

Run tests:
```bash
python -m pytest tests/  # or python tests/test_health.py
```

## Why this exists
Solo founders need clean buyer packages and personal outreach when exploring exits or partnerships. This tool keeps it simple and focused.

**Author:** Mourad.Soltani  
**License:** MIT (see LICENSE)
"""
