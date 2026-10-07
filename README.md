<div align="center">

# ✈️ AI Travel Planner Agent

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Google Search](https://img.shields.io/badge/Google-Serper_API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://serper.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**An intelligent autonomous travel planning assistant powered by LangChain ReAct agents, Groq high-speed LLM, and real-time Google Search integration.**

*Generate personalized day-by-day itineraries, live weather, budget feasibility, packing checklists, and local recommendations in seconds.*

</div>

---

## 🌟 Key Features

- 🤖 **Autonomous AI Agent** — Leverages LangChain ReAct architecture with tool-calling capabilities to browse the web in real-time.
- 🎯 **Hyper-Personalized Itineraries** — Tailors trips based on:
  - **Traveler Profile:** Solo, Couple / Honeymoon, Family, Friends
  - **Preferences:** Budget, duration, travel pace (relaxed vs. fast-paced), food preferences, and interests
- 💰 **Trip Feasibility & Budget Breakdown** — Analyzes whether the desired trip is practical within your budget and provides alternative cost-saving recommendations.
- 🌐 **International & Domestic Travel Ready** — Covers flights, airport transfers, hotel tiers, visa requirements, travel insurance, and currency considerations.
- ⛅ **Real-Time Weather & Local Insights** — Fetches live destination weather and flags tourist scams, safety warnings, and cultural customs.
- 🎒 **Automated Packing Checklist** — Custom checklist generated dynamically based on weather, activities, and trip duration.
- 💻 **Intuitive Streamlit UI** — Clean, user-friendly interface for effortless planning.

---

## 🏗️ System Architecture

```text
                        ┌──────────────────┐
                        │   User Inputs    │
                        │ (Streamlit Web)  │
                        └────────┬─────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │  LangChain AI Agent   │
                     │   (ReAct Framework)   │
                     └───────────┬───────────┘
                                 │
             ┌───────────────────┴───────────────────┐
             ▼                                       ▼
  ┌─────────────────────┐                 ┌─────────────────────┐
  │ Google Serper Tool  │                 │      Groq LLM       │
  │ (Live Web Search)   │                 │ (Fast LLM Inference)│
  └──────────┬──────────┘                 └──────────┬──────────┘
             │                                       │
             └───────────────────┬───────────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │  Structured Travel Plan │
                    │ (Budget, Day Itinerary, │
                    │   Packing & Warnings)   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Streamlit UI Display   │
                    └─────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Devpatel7777/AI-Travel-Planner.git
cd AI-Travel-Planner
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_google_serper_api_key_here
```
> - Get your Groq API key: [console.groq.com](https://console.groq.com)
> - Get your Serper API key: [serper.dev](https://serper.dev)

### 5. Launch the Application
```bash
streamlit run AI_TRAVEL_AGENT.py
```
Open `http://localhost:8501` in your browser.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Agent Framework** | LangChain (ReAct Agent) | Multi-step reasoning and dynamic tool execution |
| **LLM Inference** | Groq Cloud | Ultra-fast inference with open-source LLMs |
| **Search Engine** | Google Serper API | Live search results for hotels, places, and attractions |
| **Web Frontend** | Streamlit | Responsive, interactive user interface |
| **Language** | Python 3.11+ | Core programming language |

---

## 👤 Author

**Dev Patel**
- GitHub: [@Devpatel7777](https://github.com/Devpatel7777)
- Email: [devpatel846211@gmail.com](mailto:devpatel846211@gmail.com)

---

<div align="center">
⭐ Star this repo if you find it helpful!
</div>
