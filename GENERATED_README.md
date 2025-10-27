# LangGraph AI Graphs and Agents

## Overview

This repository provides a collection of examples and implementations demonstrating the use of **LangGraph** for building stateful graphs, AI agents, and retrieval-augmented generation (RAG) workflows. It progresses from basic graph structures (nodes, edges, conditionals, and loops) to advanced AI-driven agents, including conversational chatbots with memory, ReAct-style agents capable of tool usage (e.g., arithmetic operations), and RAG agents for querying PDF documents. The codebase integrates with **LangChain** for language model (LLM) interactions, embeddings, and document processing, using OpenAI models accessed via the OpenRouter API.

Key concepts covered include state management with `TypedDict`, graph compilation, conditional routing, tool calling, conversation history, and vector-based document retrieval. The project is primarily built around interactive Jupyter notebooks for demonstration and standalone Python scripts for individual agents.

## Key Features

- **Basic Graph Structures**: Build and execute simple state graphs with nodes for message processing, value operations (e.g., addition/multiplication), and conditional logic (e.g., routing based on operation types).
- **AI-Driven Agents**:
  - Simple conversational agents that generate responses via LLMs (e.g., Mistral models) and maintain message history.
  - ReAct agents with tool integration, such as an addition tool, enabling tool-call workflows.
- **Retrieval-Augmented Generation (RAG)**: Load PDFs, chunk text, generate embeddings, store in Chroma vector database, and perform similarity searches for document querying and response generation.
- **Interactive Workflows**: Command-line interfaces for real-time user input, graph invocation, and conversation logging.
- **Logging and Persistence**: Automatic saving of conversation logs (e.g., human-AI interactions) to text files for review.
- **Modular Components**: Reusable state schemas (`AgentState`), tool definitions, and graph nodes for extensibility.

## Tech Stack

- **Python**: Core language for scripting and notebooks.
- **LangGraph**: For constructing and managing state graphs with nodes, edges, and conditional workflows.
- **LangChain (Core, Community, OpenAI)**: For LLM interactions, message handling (e.g., `HumanMessage`, `AIMessage`), document loaders (e.g., `PyPDFLoader`), text splitters, embeddings, and tools.
- **OpenAI API (via OpenRouter)**: Access to LLMs like `mistralai/mistral-7b-instruct` for chat completions and embeddings (e.g., `text-embedding-3-small`).
- **ChromaDB**: Vector store for RAG, supporting persistence and retrieval of embedded documents.
- **dotenv**: For loading environment variables (e.g., API keys).
- **Jupyter Notebooks**: For interactive demonstrations and step-by-step execution.
- **Other Python Libraries**: `typing` for type hints, `os` for file operations, and `IPython.display` for notebook visualizations.

## Project Structure

The repository is organized as follows:

```
.
├── .gitignore                    # Ignores sensitive files (e.g., .env patterns) to protect environment variables.
├── LangGraph.ipynb               # Main Jupyter notebook demonstrating LangGraph usage from basic graphs to advanced RAG agents.
├── .ipynb_checkpoints/           # Auto-generated checkpoints for notebooks (e.g., LangGraph-checkpoint.ipynb, app-checkpoint.py).
│   ├── LangGraph-checkpoint.ipynb
│   ├── app-checkpoint.py
│   └── logging-checkpoint.txt    # Snapshot of conversation logs.
├── Agents/                       # Collection of standalone Python scripts for specific AI agents.
│   ├── agent1.py                 # Simple agent for LLM-based message processing with user input.
│   ├── agent2.py                 # Conversational agent with memory and conversation logging.
│   ├── react_agent.py            # ReAct agent with tool calling (e.g., addition functionality).
│   └── logging.txt               # Persistent log file for conversation history (e.g., user-AI dialogues).
```

- **LangGraph.ipynb**: The primary demonstration notebook, covering tutorials on graph building, agent creation, and RAG. Includes interactive elements like user prompts and graph visualizations.
- **Agents Folder**: Executable Python scripts for isolated agent examples, each focusing on a specific functionality (e.g., tool-enabled ReAct workflows).
- **Checkpoints and Logs**: Automatically generated files for notebook recovery and interaction logging; can be ignored or cleaned up.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher.
- A GitHub repository clone: `git clone <repository-url> && cd <repository-directory>`.
- OpenAI API key (sign up at OpenAI; use OpenRouter for alternative access if needed).

### Installation
1. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install langgraph langchain langchain-core langchain-community langchain-openai langchain-chroma python-dotenv
   ```

3. Set up environment variables:
   - Create a `.env` file in the project root (it will be ignored by Git based on `.gitignore`).
   - Add your OpenAI API key: `OPENAI_KEY=your_openai_api_key_here`.
   - Optionally, add other vars if needed (e.g., custom base URLs for OpenRouter: `https://openrouter.ai/api/v1`).

4. For notebook usage, ensure Jupyter is installed and running:
   ```
   pip install jupyter
   jupyter notebook
   ```
   - Open `LangGraph.ipynb` for interactive demos.

### Running the Code
- The codebase uses OpenRouter as the base URL for OpenAI compatibility, with models like `mistralai/mistral-7b-instruct`. If you prefer direct OpenAI, update the `base_url` in scripts/notebooks accordingly.

## Usage

### Jupyter Notebook (`LangGraph.ipynb`)
- Launch Jupyter and open the notebook.
- Execute cells sequentially to explore:
  - **Basic Graphs**: Invoke simple graphs with states like `{"message": "Rivindu"}` to generate greetings or process values (e.g., summing lists).
  - **Conditional and Looping Graphs**: Test routing and loops, such as operations (`add`/`subtract`) or continuous processing.
  - **AI Agents**: Interact with LLM-powered agents. Enter inputs like `{"messages": [HumanMessage(content="Hello!")]}` to get responses, tool calls, or document drafts.
  - **RAG Agent**: Upload a PDF, run embedding and storage setup, then query with natural language (e.g., "Summarize the document") for retrieved answers.
- Example invocation inside a cell:
  ```python
  result = app.invoke({"messages": [("user", "What is 3 + 8")]})
  print(result)
  ```
- Supports streaming outputs for real-time feedback.

### Standalone Scripts (`Agents/` Folder)
- Run individual agents directly:
  - **agent1.py**: Run `python Agents/agent1.py`, enter a message (e.g., "Hello"), and observe LLM responses.
  - **agent2.py**: Run `python Agents/agent2.py` for a memory-enabled loop. Enter queries; type "exit" to save logs to `Agents/logging.txt`.
  - **react_agent.py**: Run `python Agents/react_agent.py` and stream inputs like `{"messages": [("user", "what is 5 + 7")]}` to see tool execution and results.

### Tips
- Logs (e.g., `logging.txt`) capture conversations in formats like `you : hii my name is rivindu` / `AI : Hello Rivindu...`.
- For RAG, ensure PDFs are accessible; ChromaDB persists data in a specified directory.
- Monitor API usage, as OpenAI calls incur costs.

## Contributing

Contributions are welcome! To get started:
- Fork the repository and create a feature branch.
- Add examples, fix bugs, or enhance documentation.
- Ensure code follows Python style (use tools like Black for formatting).
- Test scripts/notebooks with sample inputs and update this README if new features are added.
- Submit pull requests with clear descriptions.

## License

This project is licensed under the MIT License. See a full license file (if added to the repo) for details. If none exists, feel free to use under standard MIT terms (permissive, non-commercial OK).