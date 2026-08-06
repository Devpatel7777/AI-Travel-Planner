<div align="center">

# ✈️ AI Travel Planner

### Intelligent Travel Planning Powered by Generative AI

Build personalized travel itineraries in seconds using **Large Language Models, AI Agents, LangChain, Groq LLM, and Real-Time Google Search**.

<p>

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

<img src="https://img.shields.io/badge/LangChain-AI-green?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Google-Serper_API-blue?style=for-the-badge&logo=google"/>

</p>

</div>

---

# 📖 Overview

AI Travel Planner is an **AI-powered travel assistant** that creates complete, personalized travel plans based on a user's destination, budget, duration, travel type, hotel preference, and food preference.

Instead of manually searching across multiple websites, users simply enter their travel details, and the AI generates a comprehensive itinerary that includes hotels, attractions, restaurants, transportation, weather updates, shopping recommendations, budgeting, and essential travel tips. :contentReference[oaicite:0]{index=0}

This project demonstrates the practical implementation of **Generative AI**, **AI Agents**, **Prompt Engineering**, and **Tool Calling** in a real-world application. :contentReference[oaicite:1]{index=1}

---

# ✨ Key Features

### 🤖 AI-Powered Trip Planning

Generate complete travel itineraries in seconds.

### 🌍 Real-Time Information

Uses Google Search to fetch the latest travel information whenever required.

### 🏨 Smart Recommendations

- Hotels
- Restaurants
- Tourist Attractions
- Shopping Places

### 💰 Budget Planning

Travel recommendations optimized according to the user's budget.

### 🌦 Weather Updates

Provides current weather information for better trip planning.

### 🚗 Local Transportation

Suggests the most suitable transportation options.

### 🎒 Packing Checklist

Essential items based on the travel destination.

### 💡 Travel Tips

Helpful recommendations to improve the travel experience.

---

# 🏗 System Architecture

```text
                  User

                    │

                    ▼

          Streamlit Web Interface

                    │

                    ▼

          LangChain AI Agent

          ↙                  ↘

 Google Search Tool      Groq LLM

          ↘                  ↙

     Personalized Travel Plan

                    │

                    ▼

          Beautiful Streamlit UI
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| AI Framework | LangChain |
| Large Language Model | Groq |
| Search Engine | Google Serper API |
| Environment | python-dotenv |

---

# 🚀 Project Workflow

```text
User Input

↓

Prompt Engineering

↓

LangChain Agent

↓

Google Search (Latest Information)

↓

Groq Large Language Model

↓

Travel Plan Generation

↓

Display Results in Streamlit
```

---

# 📸 Application Preview

## 🏠 Home Page

> Add Screenshot

---

## ✈️ Generated Travel Plan

> Add Screenshot

---

## 📊 Example Output

> Add Screenshot

---

# 📂 Folder Structure

```text
AI-Travel-Planner/

│── AI_TRAVEL_AGENT.py

│── requirements.txt

│── README.md

│── .env

├── screenshots/

│      ├── home.png

│      ├── input.png

│      └── output.png

└── assets/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Devpatel7777/AI-Travel-Planner.git
```

Move into the project

```bash
cd AI-Travel-Planner
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=YOUR_API_KEY

SERPER_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run AI_TRAVEL_AGENT.py
```

---

# 🎯 Use Cases

- Personal Trip Planning
- Family Vacation Planning
- Budget Travel
- Weekend Getaways
- Student Tours
- Business Trips

---

# 💼 Skills Demonstrated

- Generative AI
- Large Language Models (LLMs)
- LangChain
- AI Agents
- Tool Calling
- Prompt Engineering
- API Integration
- Streamlit Development
- Python Development
- Environment Variable Management

---

# 🚀 Future Enhancements

- Flight Booking Integration
- Hotel Booking APIs
- Interactive Google Maps
- PDF Travel Guide
- Voice Assistant
- User Authentication
- Travel History
- Expense Tracking
- Multi-Language Support
- Dark Mode

---

# 👨‍💻 Developer

## Dev Patel

**Data Analyst | Generative AI Engineer | AI Agent Developer**

📧 Email : Your Email

💼 LinkedIn : Your LinkedIn

🐙 GitHub : https://github.com/Devpatel7777

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates future development.

---

<div align="center">

### ⭐ If you like this project, don't forget to Star the repository ⭐

</div>
