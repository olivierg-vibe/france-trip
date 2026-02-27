# Contributing to Hyperdrive DCF

Thank you for your interest in contributing to the Hyperdrive DCF framework.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest enhancements
- Include steps to reproduce, expected vs actual behavior, and your environment

### Pull Requests

1. Fork the repository and create a branch from `main`
2. Make your changes following the guidelines below
3. Test your changes with a sample project
4. Submit a PR with a clear description of the change and its motivation

## Extending the Framework

### Adding a Command

1. Create a new `.md` file in `.claude/commands/`
2. Follow the frontmatter format used by existing commands (name, description)
3. Define the command's workflow steps, inputs, and outputs
4. Document the command in `README.md`

### Adding an Agent

1. Create a new `.md` file in `.claude/agents/`
2. Include the required frontmatter (name, description, model, color)
3. Define the agent's role, responsibilities, and workflow
4. Keep the agent generic -- avoid hardcoded project names, URLs, or module references

### Adding a Rule

1. Create a new `.md` file in `.claude/rules/`
2. Rules are auto-loaded into every Claude Code session
3. Keep rules concise and focused on a single concern

### Adding a Skill

1. Create a new `.md` file in `.claude/skills/`
2. Skills are optional and provide specialized capabilities
3. Follow the existing skill format for consistency

## Code of Conduct

- Be respectful and constructive
- Focus on the work, not the person
- Welcome newcomers and help them get started

## Guidelines

- Keep changes focused -- one concern per PR
- Do not modify or delete existing files in `.claude/commands/`, `.claude/agents/`, `.claude/rules/`, or `.claude/skills/` without discussion in an issue first. Adding new files is welcome — follow the extension guides above.
- Avoid adding project-specific references (hardcoded names, URLs) to framework files
- Test with both simple and complex project structures
- Update documentation when adding or changing commands

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
