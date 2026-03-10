# Contributing

## Scope

This project favors small, reviewable changes over broad rewrites. Good contributions usually improve one of:

- category quality
- summary quality
- operational reliability
- tests
- templates and presentation

## Development workflow

1. create an environment with Python 3.11
2. install dependencies from `requirements.txt`
3. run `python scripts/reset_state.py` if you need a clean local state
4. run `python scripts/main.py` with a test window
5. inspect generated files under `data/` and `content/posts/`

## Contribution guidelines

- keep deterministic behavior whenever possible
- do not hardcode secrets
- preserve the original English title and abstract
- avoid guessing affiliations
- prefer small PRs with focused intent

## Pull request checklist

- explain the user-visible change
- explain any classification tradeoff
- mention how you tested it
- include before/after examples if template output changed
