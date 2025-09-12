# 🧠 S.A.G.E 2.0 — Local AI Agent Playground  

S.A.G.E (System for Autonomous Guidance & Execution) 2.0 is a personal AI agent project designed to **explore and learn** the inner workings of **LLMs (Large Language Models)** and **autonomous AI agents** — while also being a useful assistant for research and project building.  

---

## 📌 Project Purpose  

This is a **learning + experimentation sandbox** built with modern AI tooling.  
S.A.G.E’s role is to help me **learn by doing** while providing concrete utilities:  

- Explore how agents reason, plan, and act  
- Learn the LangChain ecosystem (memory, tools, agents, retrievers)  
- Develop structured, tool-using agents that output clean JSON  
- Build utilities that support research, dataset creation, and automation  

---

## 🔨 Current Functionality  

| Feature / Tool        | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Research Assistant** | Takes a user query, searches the web, queries Wikipedia, and summarizes results. |
| **Structured Outputs** | Uses Pydantic schemas to enforce strict JSON structure for responses (topic, summary, sources, tools used). |
| **Web Search Tool**    | Integrates DuckDuckGo search for live information retrieval.                |
| **Wikipedia Tool**     | Queries Wikipedia for concise factual lookups.                             |
| **File Save Tool**     | Saves structured research results into timestamped `.txt` files.            |
| **JSON Validation**    | All outputs validated via Pydantic → ensures responses are consistent and usable. |

---

## 🛠️ Stack & Technologies  

| Layer              | Tool / Tech                              | Purpose                           |
|--------------------|------------------------------------------|-----------------------------------|
| **LLM**            | [Anthropic Claude 3 (Haiku)]             | Core model powering the agent     |
| **Framework**      | [LangChain](https://www.langchain.com)   | Agent orchestration & chaining    |
| **Validation**     | [Pydantic](https://docs.pydantic.dev)    | Strict JSON schemas for outputs   |
| **Environment**    | `Python 3.11+` + `venv` + `.env`         | Local development setup           |
| **Prompting**      | LangChain Prompt Templates               | Dynamic prompt injection          |
| **Agent Type**     | Tool-using Agent                         | Research assistant powered by external tools |
| **Tools**          | DuckDuckGo, Wikipedia, File Writer       | Information retrieval + persistence |

---

## 🚀 Getting Started  

### 1. Clone the repo
`
git clone https://github.com/yourusername/sage2.0.git
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
