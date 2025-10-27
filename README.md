# River Points Tracker (CLI)

A tiny, friendly command‑line calculator to **estimate points** in the River ecosystem
based on simple inputs (stake amount, daily social engagement, and staking multiplier).

> ⚠️ This is a **community utility** for educational purposes only. It is **not** an official tool.

## Features
- Quick CLI: `river-points calc --stake 1000 --engagement 250 --days 30`
- Simple model: stake yield points + engagement points + optional compounding multiplier.
- Pretty output and JSON export.
- Tested with `pytest` and shipped with GitHub Actions CI.

## Installation
```bash
# Create and activate a virtual env (recommended)
python -m venv .venv && . .venv/bin/activate  # on Windows: .venv\Scripts\activate

# Install package in editable mode
pip install -e .
```

## Usage
```bash
# Basic
river-points calc --stake 1500 --engagement 300 --days 30

# With custom rates
river-points calc --stake 2000 --engagement 500 --days 45           --stake-apr 0.10 --engagement-rate 0.5 --multiplier 1.2

# JSON output for spreadsheets / dashboards
river-points calc --stake 1000 --engagement 200 --days 14 --json
```

## Model (default assumptions)
- **Stake points**: `stake * (stake_apr / 365) * days`
- **Engagement points**: `engagement_per_day * engagement_rate * days`
- **Multiplier**: applied once at the end to total points (e.g., staking boosts).

These defaults are **guesses** and meant to be edited in `calculator.py` to match
whatever public docs or community consensus you prefer.

## Development
```bash
# Run tests
pytest

# Lint (optional if you install ruff)
ruff check .
```

## Releasing
This is a pure utility repo — feel free to fork and adapt.

## License
MIT
