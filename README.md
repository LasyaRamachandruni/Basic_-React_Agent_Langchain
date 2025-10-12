# Basic React Agent with LangChain

A simple starter template for building intelligent agents using Google's Gemini models and LangChain's ReAct framework. This project helps you quickly prototype reasoning agents that can use tools and make decisions autonomously.

## Features

- **Gemini 2.x Integration** - Works with the latest Gemini models (`gemini-2.5-pro`, `gemini-2.5-flash`)
- **ReAct Agent Pattern** - Implements reasoning + acting workflow for intelligent tool use
- **Tool Integration** - Easy-to-extend architecture for adding custom tools
- **Simple Configuration** - Environment-based API key management

## Getting Started

### Prerequisites

- Python 3.8+
- Google AI API Key ([get one here](https://makersuite.google.com/app/apikey))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/basic-react-agent-langchain.git
cd basic-react-agent-langchain
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install langchain langchain-google-genai langchain-community google-generativeai python-dotenv
```

4. Set up your API key:

Create a `.env` file in the root directory:
```
GOOGLE_API_KEY=your_api_key_here
```

### Running the Agent

```bash
python 1.introduction/react_agent_basic.py
```

## Configuration

You can switch between different Gemini models by editing the configuration in `react_agent_basic.py`:

```python
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-pro",  # or use "models/gemini-2.5-flash" for faster responses
    google_api_key=os.environ["GOOGLE_API_KEY"]
)
```

## Adding Custom Tools

The agent architecture supports custom tool integration. Check the LangChain documentation for examples of how to create and register your own tools.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Generative AI Python SDK](https://ai.google.dev/tutorials/python_quickstart)
- [LangGraph for Advanced Agents](https://langchain-ai.github.io/langgraph/)

## Troubleshooting

**Model not found errors**: Make sure you're using a valid model name. You can list available models with `genai.list_models()`.

**Parsing errors**: Try adding `handle_parsing_errors=True` when initializing your agent, or consider migrating to LangGraph for more robust agent workflows.

**Slow responses**: Switch to `gemini-2.5-flash` for faster inference at the cost of some capability.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT License - feel free to use this in your own projects.
