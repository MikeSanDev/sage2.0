# 🧠 Sage 2.0 — Local AI Agent Playground

Sage 2.0 is a personal AI agent project designed to **explore and learn** the inner workings of **LLMs (Large Language Models)** and **autonomous AI agents**.

This repo is part of a hands-on journey to understand:
- 🧠 How LLMs work under the hood (currently using **Anthropic Claude 3**)
- 🔁 How agents can reason, plan, and take actions
- 🛠️ How tools, memory, prompts, and chains come together
- 💻 How to control or assist **local machine tasks** through an intelligent assistant

---

## 📌 Project Purpose

This is **not** a production-level agent (yet). It's a **learning and experimentation sandbox** built with modern AI tooling. The goal is to:

- Understand how to build an agent that can reason and act
- Learn the LangChain ecosystem (memory, tools, agents, retrievers)
- Eventually build a fully capable **local AI assistant** that can:
  - Answer questions
  - Access local files
  - Summarize documents
  - Execute scripts or commands
  - Help with coding or task automation

---

## 🛠️ Stack & Technologies

| Layer              | Tool / Tech                              | Purpose                           |
|-------------------|------------------------------------------|-----------------------------------|
| **LLM**            | [Anthropic Claude 3 (Sonnet)]            | Core model powering the agent     |
| **Framework**      | [LangChain](https://www.langchain.com)   | Agent orchestration & chaining    |
| **Memory**         | `ConversationBufferMemory`               | Persistent chat history           |
| **Environment**    | `Python 3.11+` + `venv` + `.env`         | Local dev                         |
| **Prompting**      | LangChain Prompt Templates               | Dynamic prompt injection          |
| **Agent Type**     | ReAct or Tool-using Agent                | Reasoning with tools (planned)    |
| **Future Tools**   | Web search, local file system, CLI tools | For task assistance on local PC   |

---

## 🚀 Getting Started

### 1. Clone the repo

`git clone https://github.com/yourusername/sage2.0.git
cd sage2.0`

### 2. Create environment
`python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows`

### 3. Install dependencies
`pip install -r requirements.txt`

### 4. Set your environment variables in .env
`ANTHROPIC_API_KEY=your_claude_api_key_here`

### 5. Run the agent
`python main.py`
