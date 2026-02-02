# Open Source Playground

A project to explore and learn from open source libraries, with a focus on becoming a better programmer through hands-on experimentation.

## Current Focus: Instructor

Currently exploring [Instructor](https://github.com/jxnl/instructor) — a library for getting structured outputs from LLMs using Pydantic models.

### What is Instructor?

Instructor patches LLM API clients (like OpenAI) to return validated Pydantic objects instead of raw text. This enables:

- **Type-safe LLM responses** — Define your expected output schema as a Pydantic model
- **Automatic validation** — Responses are validated against your schema
- **Retry logic** — Failed validations can trigger automatic retries with feedback

### Examples

| File | Description |
|------|-------------|
| `instructor/ex-1.py` | Basic extraction — extracting a `Person` object from unstructured text |
| `instructor/ex-1.1.py` | Invoice extraction — extracting a `Bill` object with dates, amounts, and GST |

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run an example
uv run instructor/ex-1.py
```

### Prerequisites

- Python 3.13+
- [Ollama](https://ollama.ai/) running locally with the `llama3.2` model:

```bash
# Install and run Ollama, then pull the model
ollama pull llama3.2
```

## Dependencies

- `instructor` — Structured outputs from LLMs
- `pydantic` — Data validation using Python type hints
- `anthropic` — Anthropic API client
- `ollama` — Ollama Python client

## License

See [LICENSE](LICENSE) for details.
