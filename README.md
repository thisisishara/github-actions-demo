# github-actions-demo
This repo demonstrated how github actions can be utilized to do dev and prod deployments of a simple flask app while using semver for automatically version based on formatted commit messages

## Dev and Prod GitHub Actions Workflows
Inspect `.github/workflows/` dir to see both workflows which create release tags, build and push docker images to the hub, and create GitHub releases on merged PRs to `main` branch.

## Commit Message Format
For the workflows to be able to correctly determine the version tags, the commits must be created according to conventional commits. Refer to the docs [here](https://www.conventionalcommits.org/en/v1.0.0/)
```txt
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The <type> can be one of the following:

- BREAKING CHANGE: A breaking change that significantly differs from previous changes
- feat: A new feature
- fix: A bug fix
- docs: Documentation changes
- style: Changes that do not affect the meaning of the code (formatting, etc.)
- refactor: Code changes that neither fix a bug nor add a feature
- perf: Performance improvements
- test: Adding missing tests or correcting existing tests
- build: Changes to the build system or external dependencies
- ci: Changes to your CI configuration files and scripts
- chore: Other changes that don't modify src or test files
For example, a commit message for adding a new endpoint to your Flask app could look like this:

```text
feat: Add new endpoint for user authentication
This format will help you automate the versioning process based on your commit history.
```
