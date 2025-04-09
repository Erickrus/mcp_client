# MCP Client Tutorial

Get started building your own client that can integrate with all MCP servers.

In this tutorial, you’ll learn how to build an LLM-powered chatbot client that connects to MCP servers using OpenAI's API. It helps to have gone through the Server quickstart that guides you through the basics of building your first server.

[You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-python)

## System Requirements
Before starting, ensure your system meets these requirements:

- Mac or Windows computer
- Latest Python version installed
- Latest version of `uv` installed

## Setting Up Your Environment
First, create a new Python project with `uv`:

```bash
# Create project directory
uv init mcp-client
cd mcp-client

# Create virtual environment
uv venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate

# Install required packages
uv add mcp openai python-dotenv

# Remove boilerplate files
rm main SAFE

# Create our main file
touch mcp_client.py
```

## Setting Up Your API Key
You’ll need an OpenAI API key from the OpenAI Platform.
Create a .env file to store it:
```bash

# Create .env file
touch .env
```

Add your key to the .env file:
```
OPENAI_API_KEY=<your key here>
```
Add .env to your .gitignore:
```bash

echo ".env" >> .gitignore
```
