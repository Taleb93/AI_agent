# Local Coding Assistant (Ollama)

A simple command-line AI chat agent for programming, running fully locally on top of [Ollama](https://ollama.com). It uses the `qwen2.5-coder:7b` model and keeps the conversation history so follow-up questions work.

## Features

- Chat with a local coding-focused LLM in the terminal
- Conversation history is kept during a session
- Code is returned in Markdown code blocks
- No cloud, no API key required

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/download) installed and running
- The model `qwen2.5-coder:7b`

## Setup

```bash
pip install -r requirements.txt
ollama pull qwen2.5-coder:7b
```

## Usage

Make sure Ollama is running (default: `http://localhost:11434`), then start the chat:

```bash
python chat.py
```

Type your question and press Enter. Type `exit` or `quit` to leave.

## Configuration

Edit the constants at the top of [chat.py](chat.py):

- `URL` – Ollama chat endpoint
- `MODEL` – any Ollama model, e.g. `codellama` or `deepseek-coder`
- The system prompt in `messages` – controls the assistant's behavior and language (currently German)

## Project Structure

- `chat.py` – interactive chat loop
- `main.py` – reserved for the agent entry point
- `requirements.txt` – Python dependencies
