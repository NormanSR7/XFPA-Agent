# XFPA Agent Project
A LangChain-powered SQL Agent that connects to a live SQLite database, allowing users to ask natural-language questions about product data. This project forms part of a broader exploration into intelligent financial planning and analysis (XFPA), using real-time data, automation, and AI agents.

---

## Features
- Fetches real-time product data from a public API
- Cleans and flattens JSON into a SQL-ready format
- Stores product data in a local SQLite database
- Uses LangChain and OpenAI GPT to answer SQL-based questions
- Prepares data for use in BI tools like Power BI or Excel
- Logs personal learning and build process in `xfpa_journal.md`

---

## Tech Stack
| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data manipulation |
| SQLite | Local database engine |
| SQLAlchemy | Python-SQL bridge |
| LangChain | Agent framework |
| OpenAI | Natural language model (GPT-4 or 3.5) |
| VS Code | Development environment |
| Git + GitHub | Version control and cloud backup |

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Virtual Environment (`venv`)
- OpenAI API key
- Git installed

### Installation Steps
```bash
git clone https://github.com/your-username/XFPA-Agent.git
cd XFPA-Agent
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt

### 
