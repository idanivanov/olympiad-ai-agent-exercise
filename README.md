# Olympiad AI Agent Exercise

This is a simple exercise to get you started with AI agents.

## Setup

### Prerequisites

Install [uv](https://github.com/astral-sh/uv) (Python package manager):

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation

```bash
git clone https://github.com/idanivanov/olympiad-ai-agent-exercise.git
cd olympiad-ai-agent-exercise
uv venv
uv sync
```

### Configuration

Create a `.env` file in the root of the project and add your environment variables.

#### Required Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `LANGCHAIN_API_KEY`: Your LangChain API key for LangSmith tracing

#### Optional Environment Variables

- `LANGCHAIN_TRACING_V2`: Whether to use LangSmith tracing v2
- `LANGCHAIN_ENDPOINT`: The LangSmith endpoint
- `LANGCHAIN_PROJECT`: The LangSmith project

### Running the Agent

```bash
uv run main.py
```

## Agent Design

![Agent Design](assets/graph.png)

- Planning
- Tools
    - Web Search
    - File System
