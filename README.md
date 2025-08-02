# 🩺 Health Chatbot Web App

A simple **AI-powered Health Chatbot** built using **Streamlit** and **OpenAI's GPT-3.5 API** that can answer general health-related queries in a friendly and safe manner. 

> **Disclaimer:** This chatbot is for educational purposes only and does **NOT** provide medical diagnoses or treatment advice. Always consult a healthcare professional for serious concerns.

---

## 🚀 Features
- Chat interface to ask health-related questions.
- Uses **OpenAI GPT-3.5 (via API)** for responses.
- Friendly assistant-like replies with safety filters.
- Warns on critical medical inquiries (diagnoses, prescriptions, emergencies).
- Lightweight, runs entirely in-browser (via Streamlit).

---

## 📦 Tech Stack
- Python 🐍
- Streamlit 🖥️
- OpenAI API (GPT-3.5)
- dotenv (for API key management)

---
## 🔑 Prerequisites
1. Python 3.8+
2. OpenAI API Key (Get it from https://platform.openai.com/)

---

## 📥 Installation
git clone https://github.com/Nasir-Raza-AI/Health-Chatbot.git
cd Health-Chatbot
pip install -r requirements.txt

---

Create a .env file and add your OpenAI API key:
OPENAI_API_KEY=your-api-key-here

---

**🟢 Run the App**
streamlit run chatbot.py

---

**🖥️ Demo Usage**
Ask questions like:

"What causes a sore throat?"

"Is paracetamol safe for children?"

The chatbot will provide a general, friendly response.

If a dangerous query is detected (diagnose/prescribe), it will warn the user.

---

**⚠️ Disclaimer**
This chatbot is designed for general informational purposes only.

It is NOT a replacement for professional medical advice, diagnosis, or treatment.

---

**📄 License**
This project is licensed under the MIT License.

---

**🤝 Contributions**
Feel free to Fork & PR to enhance this chatbot (e.g., add Hugging Face model integration or WhatsApp-like UI).

---
