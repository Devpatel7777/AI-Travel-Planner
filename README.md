<div align="center">

# AI Travel Planner

### Intelligent Travel Planning Powered by Generative AI

Build personalized travel itineraries using **Large Language Models, AI Agents, LangChain, Groq LLM, and Google Search integration.**

<p>

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

<img src="https://img.shields.io/badge/LangChain-AI-green?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Google-Serper_API-blue?style=for-the-badge&logo=google"/>

</p>

</div>

---

# Overview

AI Travel Planner is an **AI-powered travel assistant** that generates personalized travel plans based on destination, budget, duration, travel type, traveler profile, hotel preference, food preference, interests, and travel pace.

Instead of manually searching across multiple websites, users provide their travel requirements and the application generates a structured travel plan containing transportation, accommodation, attractions, restaurants, weather information, shopping recommendations, budget analysis, packing requirements, and travel tips.

The project demonstrates the practical implementation of **Generative AI, AI Agents, LangChain, Prompt Engineering, Tool Calling, API Integration, and Streamlit application development**.

---

# Key Features

### AI-Powered Trip Planning

Generate personalized travel plans based on user requirements.

### Trip Feasibility Analysis

Analyze whether the requested trip is practical according to the available budget.

### Budget Analysis

Estimate major travel expenses and provide a structured budget breakdown.

### International Travel Planning

For international trips, the planner considers:

- International flight requirements
- Airport transfers
- Local transportation
- Hotel accommodation
- Food
- Activities
- Visa
- Travel insurance
- Baggage
- Miscellaneous expenses

### Traveler-Based Recommendations

The travel experience is adapted according to the selected traveler type:

- Solo
- Couple / Husband & Wife
- Family
- Friends

### Personalized Recommendations

Recommendations can include:

- Hotels
- Restaurants
- Tourist attractions
- Shopping places
- Activities
- Local experiences

### Weather Information

Provides destination-related weather information to help users prepare for their trip.

### Day-Wise Itinerary

Generates a structured itinerary according to:

- Destination
- Number of days
- Budget
- Traveler type
- Interests
- Travel pace

### Packing Checklist

Generates a practical packing checklist based on the trip.

### Travel Warnings

Provides important travel considerations such as:

- Road safety
- Tourist scams
- Local customs
- Weather conditions
- Food and water safety

### Budget Alternatives

If the estimated trip cost is higher than the user's budget, the planner can suggest cost-saving alternatives such as:

- Budget accommodation
- Public transportation
- Local restaurants
- Shoulder-season travel
- Reduced expensive activities

---

# System Architecture

```text
                         User
                           |
                           v
                Streamlit Web Interface
                           |
                           v
                  LangChain AI Agent
                           |
                +----------+----------+
                |                     |
                v                     v
        Google Search Tool        Groq LLM
                |                     |
                +----------+----------+
                           |
                           v
                Travel Planning Logic
                           |
                           v
              Personalized Travel Plan
                           |
                           v
                 Streamlit Web UI
````

---

# Project Workflow

```text
User Input
    |
    v
Trip Details & Preferences
    |
    v
Prompt Construction
    |
    v
LangChain AI Agent
    |
    +----------------------+
    |                      |
    v                      v
Google Search          Groq LLM
    |                      |
    +----------+-----------+
               |
               v
       Travel Plan Generation
               |
               v
       Budget & Feasibility
               |
               v
      Day-Wise Itinerary
               |
               v
 Hotels + Restaurants + Weather
               |
               v
 Packing List + Travel Warnings
               |
               v
        Final Travel Plan
```

---

# Tech Stack

| Category               | Technology        |
| ---------------------- | ----------------- |
| Programming Language   | Python 3.11+      |
| Frontend               | Streamlit         |
| AI Framework           | LangChain         |
| Large Language Model   | Groq              |
| Search Integration     | Google Serper API |
| Environment Management | python-dotenv     |
| Version Control        | Git & GitHub      |

---

# Application Preview

## Home Page

![AI Travel Planner Home](screenshots/home.png)

---

## Trip Input

![Trip Input](screenshots/input.png)

---

## Generated Travel Plan

![Generated Travel Plan](screenshots/output.png)

---

## Project Screenshots

Additional application screenshots are available in the `screenshots` directory.

---

# Folder Structure

```text
AI-Travel-Planner/
|
├── AI_TRAVEL_AGENT.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
|
├── screenshots/
|   ├── home.png
|   ├── input.png
|   ├── output.png
|   ├── feasibility.png
|   ├── budget.png
|   ├── itinerary.png
|   ├── hotels.png
|   ├── restaurants.png
|   ├── weather.png
|   └── packing.png
|
└── assets/
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Devpatel7777/AI-Travel-Planner.git
```

## Navigate to the Project

```bash
cd AI-Travel-Planner
```

## Create a Virtual Environment

```bash
python -m venv env
```

## Activate the Environment

### Windows

```bash
env\Scripts\activate
```

### macOS / Linux

```bash
source env/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
SERPER_API_KEY=YOUR_SERPER_API_KEY
```

Do not upload your actual API keys to GitHub.

Add `.env` to `.gitignore`.

```text
.env
env/
__pycache__/
*.pyc
```

---

# Run the Application

Run the following command:

```bash
streamlit run AI_TRAVEL_AGENT.py
```

The application will be available at:

```text
http://localhost:8501/
```

---

# Example Input

```text
Destination City: Vietnam

Budget: ₹5,00,000

Number of Days: 6

Travel Type: Couple / Husband & Wife

Hotel Preference: Standard

Food Preference: Vegetarian

Interests:
Nature
Beaches
Culture
Food
Shopping
Photography
Romantic Experiences

Travel Pace: Balanced
```

The AI uses these inputs to generate a personalized travel plan.

---

# Example Output

The generated travel plan can contain:

```text
Trip Feasibility

Estimated Total Cost

Budget Breakdown

Transportation Plan

Traveler Profile

Hotel Recommendations

Tourist Attractions

Day-Wise Itinerary

Restaurant Recommendations

Shopping Places

Weather Information

Packing Checklist

Travel Warnings

Budget-Saving Alternatives
```

---

# Use Cases

* Personal Trip Planning
* Couple Travel Planning
* Family Vacation Planning
* Friends Trips
* Budget Travel
* International Travel Planning
* Weekend Getaways
* Student Tours
* Business Trips

---

# Skills Demonstrated

* Generative AI
* Large Language Models
* LangChain
* AI Agents
* Tool Calling
* Prompt Engineering
* API Integration
* Google Search Integration
* Streamlit Development
* Python Development
* Environment Variable Management
* AI Application Development
* Budget Analysis
* Recommendation Systems

---

# Challenges Addressed

During development, the project addresses practical challenges such as:

* Budget-constrained travel planning
* International transportation planning
* Personalized recommendations
* Different traveler profiles
* Dynamic travel information
* Large AI prompts and token limitations
* External API limitations
* Structured AI response generation

---

# Future Enhancements

* Real-Time Flight Price Integration
* Hotel Booking API Integration
* Interactive Google Maps
* Flight and Hotel Booking Links
* Multi-City Trip Planning
* PDF Travel Guide Generation
* Voice-Based Travel Assistant
* User Authentication
* Saved Travel History
* Expense Tracking
* Multi-Language Support
* Real-Time Travel Alerts
* Mobile Application
* Personalized Travel History

---

# Learning Outcomes

This project provided practical experience in building an end-to-end Generative AI application.

Key learning areas include:

* Building AI agents
* Integrating LLMs into applications
* Working with LangChain
* Designing effective prompts
* Calling external tools through AI agents
* Integrating search APIs
* Building interactive Streamlit applications
* Managing API credentials securely
* Handling API and token limitations
* Generating structured AI outputs
* Designing user-focused AI applications

---

# Developer

## Dev Patel

**Data Analyst | Generative AI Engineer | AI Agent Developer**

GitHub:
[https://github.com/Devpatel7777](https://github.com/Devpatel7777)

---

# Support

If you found this project useful, consider giving the repository a star on GitHub.

---

# Disclaimer

Travel prices, hotel availability, weather conditions, transportation schedules, visa requirements, and other travel information may change.

Users should verify important travel and booking information through official sources before making final decisions.

---

<div align="center">

### AI Travel Planner

Built with Python, Streamlit, LangChain and Generative AI.

</div>

