# Multi-Tool AI Agent Using LangChain

An AI-powered assistant built using LangChain and Groq integrating multiple real-world tools such as:

- Weather Search
- Internet Search
- YouTube Search
- Email Automation
- PDF Reader

This project demonstrates tool calling, API integrations, and agentic AI workflows using Python.

---

# Features

✅ Weather Information using OpenWeatherMap API  
✅ Internet Search using Tavily API  
✅ YouTube Video Search using YouTube Data API  
✅ Gmail Email Automation using SMTP  
✅ PDF Reading and Text Extraction  
✅ Arithmetic Operations  
✅ Conversational AI Assistant using Groq + LangChain  

---

# Tech Stack

- Python
- LangChain
- Groq
- Tavily API
- OpenWeatherMap API
- YouTube Data API
- SMTP
- PyPDF

---

# Installation

## Clone Repository

```bash
git clone https://github.com/shanjaiy2006/multi-tool-ai-agent.git
```

## Navigate to Project

```bash
cd multi-tool-ai-agent
```

## Install Dependencies

```bash
uv sync
```

OR

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_key
WEATHER_API_KEY=your_key
TAVILY_API_KEY=your_key
EMAIL_ADDRESS=your_email
EMAIL_APP_PASSWORD=your_password
YOUTUBE_API_KEY=your_key
```

---

# Run Project

```bash
python main.py
```

---

# Example Prompts

```text
Tell me the weather in Chennai

Search latest AI news

Find Spring Boot tutorials on YouTube

Send email to abc@gmail.com saying hello

Read resume.pdf
```

---

# Project Architecture

User Prompt → LangChain Agent → Tool Selection → External API → Response

---

# Future Improvements

- Streamlit UI
- Chat Memory
- Voice Assistant
- RAG Integration
- Database Support
- Docker Deployment

---

# Author
Shanjaiy Samarjith

GitHub:
https://github.com/shanjaiy2006
