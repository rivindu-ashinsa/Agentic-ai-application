# Project Title: Agentic AI Application

## Overview
The Agentic AI Application summarizes code files from GitHub repositories and generates professional README files using OpenAI and Hugging Face models for NLP tasks.

## Key Features
- GitHub repository code fetching
- File content summarization
- Automated README generation

## Tech Stack
- Python
- OpenAI API
- Hugging Face API
- Requests library
- dotenv

## Project Structure
```
.
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
├── GENERATED_README.md  # Auto-generated README
├── hf_models.py        # Hugging Face integration
├── main.py             # Core application logic
├── README.md           # Project documentation
├── requirements.txt    # Dependencies
└── scraper.py         # GitHub code fetcher
```

## Setup
1. Clone and navigate:
```bash
git clone <repository-url>
cd Agentic-ai-application
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```
OPEN_AI_KEY=<your_openai_key>
GITHUB_TOKEN=<your_github_token>
HF_TOKEN=<your_huggingface_token>
```

## Usage
Execute:
```bash
python main.py
```
Note: Configure repository URL in main.py's app.invoke method.

## Contributing
Issues and pull requests welcome.

## License
MIT License
