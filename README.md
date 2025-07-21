# AI Code Agent

An open-source AI agent that automatically implements code changes from GitHub issues using Gemini CLI.

## Features

- 🤖 Reads GitHub issues labeled with `ai-agent`
- 🔄 Automatically creates feature branches
- 💻 Uses Gemini CLI to implement code changes
- 🔍 Creates pull requests with proposed solutions
- 📋 Project board integration (coming soon)

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js 20+
- GitHub Personal Access Token
- Google Cloud Service Account

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mbusk88/ai-code-agent.git
cd ai-code-agent
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Gemini CLI:
```bash
npm install -g @google/gemini-cli
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your GitHub token
```

5. Authenticate with Google Cloud:
```bash
gcloud auth application-default login --impersonate-service-account=SERVICE_ACCOUNT_EMAIL
```

### Usage

1. Create an issue in your target repository
2. Add the `ai-agent` label
3. The agent will be triggered automatically by GitHub Actions.

## Architecture

```
ai-code-agent/
├── .github/workflows/    # GitHub Actions (triggers on labels)
├── src/
│   ├── config.py        # Configuration management
│   ├── gemini_runner.py  # Gemini CLI integration
│   └── main.py          # Main orchestration (for Actions)
└── tests/               # Test suite (coming soon)
```

## How It Works

1. **GitHub Webhook**: When an issue is labeled with `ai-agent`, a GitHub Actions workflow is triggered.
2. **Issue Processing**: The system reads the issue details using the `@gemini-cli/mcp-github` MCP server.
3. **Jira Integration**: A corresponding ticket is created in Jira using the `@gemini-cli/mcp-jira` MCP server.
4. **AI Implementation**: The Gemini CLI, authenticated via a service account, analyzes the issue and implements the necessary code changes.
5. **Code Review**: A pull request is automatically created for human review.
6. **Jira Update**: The Jira ticket is updated with the pull request link and moved to the "In Review" column.

## Roadmap

- [ ] Project board integration
- [ ] Multiple agent support
- [ ] Test generation
- [ ] Code review feedback loop

## Contributing

This project is in early development. Feel free to:
- Open issues with ideas or bugs
- Submit PRs with improvements
- Share feedback on the approach

## License

MIT License - see LICENSE file for details

## Acknowledgments

- Built with [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- Inspired by the need for better developer automation
