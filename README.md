# 🧠 Sage 2.0 — Local AI Agent Playground

Sage 2.0 is a personal AI agent project designed to **explore and learn** the inner workings of **LLMs (Large Language Models)** and **autonomous AI agents**.

This repo is part of a hands-on journey to understand:
- 🧠 How LLMs work under the hood (currently using **Anthropic Claude 3**)
- 🔁 How agents can reason, plan, and take actions
- 🛠️ How tools, memory, prompts, and chains come together
- 💻 How to control or assist **local machine tasks** through an intelligent assistant

---

## 📌 Project Purpose

This is **not** a production-level agent (yet). It’s a **learning and experimentation sandbox** built with modern AI tooling.  

Sage’s role is to help me **learn by doing** while providing useful utilities along the way. Current goals:  
- Understand how to build an agent that can reason and act  
- Learn the LangChain ecosystem (memory, tools, agents, retrievers)  
- Develop **concrete utilities** that make Sage helpful in daily projects  

### 🔨 Current Tools & Purposes

| Tool / Capability       | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Dataset Builder**      | Generate structured JSON datasets of dance prompts (Concepts, Themes, Training) for later fine-tuning models (e.g., Ollama/Mistral). |
| **Task Tracker**         | Break down project goals into actionable steps, output JSON, and (future) sync with Notion or task managers. |
| **Q&A / Summarizer**     | Answer questions or summarize docs (planned).                          |
| **Local File Tools**     | Read and process local files for quick retrieval or summarization (planned). |
| **Script Executor**      | Assist with coding tasks, run local scripts, or automate workflows (future). |

---

## 🛠️ Stack & Technologies

| Layer              | Tool / Tech                              | Purpose                           |
|--------------------|------------------------------------------|-----------------------------------|
| **LLM**            | [Anthropic Claude 3 (Haiku)]             | Core model powering the agent     |
| **Framework**      | [LangChain](https://www.langchain.com)   | Agent orchestration & chaining    |
| **Memory**         | `ConversationBufferMemory`               | Persistent chat history           |
| **Validation**     | [Pydantic](https://docs.pydantic.dev)    | Strict JSON schemas for outputs   |
| **Environment**    | `Python 3.11+` + `venv` + `.env`         | Local dev                         |
| **Prompting**      | LangChain Prompt Templates               | Dynamic prompt injection          |
| **Agent Type**     | ReAct / Tool-using Agent (planned)       | Reasoning with tools              |
| **Future Tools**   | Notion API, web search, local CLI tools  | Expanding Sage’s reach            |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/sage2.0.git
cd sage2.0


### 2. Create environment
`python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows`

### 3. Install dependencies
`pip install -r requirements.txt`

### 4. Set your environment variables in .env
`ANTHROPIC_API_KEY=your_claude_api_key_here`

### 5. Run the agent
`python main.py`
