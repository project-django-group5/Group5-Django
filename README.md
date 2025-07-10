# Development Branch

This branch serves as the main integration point for features before merging into `main`.

## Purpose
- Collects all feature branches for integration testing
- Ensures code stability

## Workflow
1. Feature branches are merged into `dev` via pull requests.
2. QA tests are performed on the `dev` branch.
3. When stable, `dev` is merged into `main` for production release.

## How to contribute
- Create feature branches from `dev`.
- Submit pull requests targeting `dev`.
- Address review comments before merging.

## Notes
- Keep `dev` up-to-date with `main`.
- Avoid direct commits to `dev`; use PRs instead.
