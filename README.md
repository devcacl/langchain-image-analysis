# Python and Gemini: Orchestrating LLMs with LangChain

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-8E75B2?logo=google)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?logo=langchain\&logoColor=white)
![Cohere](https://img.shields.io/badge/Cohere-API-39594D?logo=cohere\&logoColor=white)

## Project Overview

This project explores how to use **LangChain as an orchestration framework for Large Language Models (LLMs)**, integrating Python, Google Gemini, and Cohere to build an intelligent workflow for image analysis and organization enriched with AI-generated annotations.

LangChain is used as the main framework because of its ability to connect and manage complex AI workflows that combine **multimodal AI capabilities and language models**, providing a modular and scalable architecture.

## Features

* Image analysis powered by multimodal AI.
* Intelligent annotation and organization of images.
* Integration with the **Google Gemini API**.
* LLM orchestration using **LangChain**.
* Implementation of simple chains.
* Orchestrator agent architecture.
* Agents used as tools.
* Modular architecture designed for extensibility.

## Technologies and Techniques

The project uses the following technologies and concepts:

| Technology / Concept   | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| **Python**             | Main programming language                   |
| **Google Gemini API**  | Multimodal AI and LLM capabilities          |
| **LangChain**          | LLM orchestration framework                 |
| **Cohere API**         | Additional language model capabilities      |
| **Simple Chains**      | Sequential LLM workflows                    |
| **Orchestrator Agent** | Coordinates multiple AI tasks               |
| **Agents as Tools**    | Enables agents to be used as callable tools |

## Project Architecture

The project demonstrates several approaches to LLM orchestration:

```text
User Input
    |
    v
LangChain
    |
    +-------------------+
    |                   |
    v                   v
Simple Chains     Orchestrator Agent
                        |
                        v
                 Agents as Tools
                        |
                        v
                Gemini / Cohere
                        |
                        v
              AI-Generated Results
```

This architecture allows different AI components to be combined into a single workflow while keeping each component modular and reusable.

## Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your system.

You can verify your Python installation with:

```bash
python --version
```

or on macOS/Linux:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_DIRECTORY>
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv .venv-gemini-3
.\.venv-gemini-3\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv-gemini-3
source .venv-gemini-3/bin/activate
```

### Install Dependencies

Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

The project requires API keys for the external AI services.

Create a `.env` file in the root directory of the project:

```env
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
COHERE_API_KEY="YOUR_COHERE_API_KEY"
```

Replace the placeholder values with your actual API keys.

Never commit your `.env` file or expose your API keys publicly.

It is recommended to add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```

## Running the Project

After configuring the environment variables and installing the dependencies, activate the virtual environment and run the corresponding Python script or notebook.

For example:

```bash
python main.py
```

If the project is notebook-based, launch Jupyter:

```bash
jupyter notebook
```

## Key Concepts

### Simple Chains

Simple chains allow multiple LLM operations to be executed sequentially, where the output of one operation can become the input of another.

### Orchestrator Agent

The orchestrator agent coordinates different tasks and determines which component or agent should handle each part of the workflow.

### Agents as Tools

This approach allows one agent to expose its capabilities as a tool that can be invoked by another agent, enabling more complex and flexible AI workflows.

## ALWAYS LEARNING, ALWAYS BUILDING :)



