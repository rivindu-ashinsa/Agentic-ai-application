# Project Title: Agentic AI Application

## Overview
The Agentic AI Application is designed to summarize code files from a GitHub repository and generate a professional README.md file based on the extracted summaries. It utilizes OpenAI and Hugging Face models for natural language processing tasks.

## Key Features
- Fetches code files from a specified GitHub repository.
- Summarizes the content of each file to extract key details.
- Generates a well-structured README.md file based on the summaries.

## Tech Stack
- Python
- OpenAI API
- Hugging Face API
- Requests library
- dotenv for environment variable management

## Project Structure
```
.
├── .env # Environment variables
├── .gitignore # Git ignore file
├── GENERATED_README.md # Automatically generated README file
├── hf_models.py # Contains functions for interacting with Hugging Face models
├── main.py # Main application logic
├── README.md # This README file
├── requirements.txt # Project dependencies
└── scraper.py # Fetches code from GitHub repositories

```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Agentic-ai-application