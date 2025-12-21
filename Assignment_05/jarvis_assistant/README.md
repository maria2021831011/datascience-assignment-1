# JARVIS AI - Intelligent Assistant

![JARVIS AI](https://img.shields.io/badge/JARVIS%20AI-Your%20Personal%20Assistant-667eea?style=for-the-badge&logo=ai&logoColor=white)
![Powered by Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Powered by Gemini AI](https://img.shields.io/badge/Powered%20by-Gemini%20AI-4285F4?style=for-the-badge&logo=google)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)

**An intelligent AI assistant with voice interaction, multi-chat support, and futuristic interface**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-🚀-00d4ff?style=for-the-badge&logo=streamlit)](#)

MY demo video--> https://drive.google.com/file/d/1ItfxC-6N6YeY8MxXn6OzVve62yUzhSZm/view?usp=drivesdk

[![Documentation](https://img.shields.io/badge/Documentation-📚-764ba2?style=for-the-badge)](#documentation)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)

## ✨ Features

<div align="center">

| Feature                 | Icon | Description                                     |
| ----------------------- | ---- | ----------------------------------------------- |
| **Multi-Role AI** | 🤖   | Switch between Assistant, Tutor, Coder & Mentor |
| **Voice Input**   | 🎤   | Speak naturally, JARVIS listens                 |
| **Multi-Chat**    | 💬   | Create & manage unlimited chat sessions         |
| **File Upload**   | 📁   | Upload text files for AI analysis               |
| **Memory**        | 💾   | Persistent conversation memory                  |
| **Export**        | 📤   | Export chats as PDF/TXT files                   |
| **Beautiful UI**  | 🎨   | Futuristic interface with animations            |

</div>

Quick Installation
bash

# Clone repository

git clone https://github.com/maria2021831011/datascience-assignment-1/tree/main/Assignment_05/jarvis_assistant
cd jarvis-ai

# Install dependencies

pip install -r requirements.txt

# Configure API key

echo "GEMINI_API_KEY=your_api_key_here" > .env

# Launch JARVIS

streamlit run main.py
📦 Requirements
Create requirements.txt:

txt
streamlit==1.28.0
google-generativeai==0.3.0
python-dotenv==1.0.0
speechrecognition==3.10.0
pyaudio==0.2.11
fpdf==1.7.2
Pillow==10.0.0
🏗️ Project Structure
text
jarvis-ai/
├── 📁 app.py
├── 📁 auth/
│   └── auth_manager.py
├── 📁 jarvis/
│   ├── gemini_engine.py ├── assistant.py
│   ├── memory.py
│   └── prompt_controller.py
├── 📁 utils/
│   ├── voice_input.py
│   └── export_chat.py
├── 📁 config/
│   └── settings.py
├── 📁 data/
│   ├── users.json
│   └── memory.json
├── 📄 .env
├── 📄 .env.example
└── 📄 requirements.txt

## 🎮 How to Use

### 1. **Authentication**

* First-time users: Register with email & password
* Returning users: Login with credentials

### 2. **Select AI Role**

* **🤖 Assistant** : General purpose help
* **👨‍🏫 Tutor** : Educational support
* **👨‍💻 Coder** : Programming assistance
* **👨‍🚀 Mentor** : Career guidance

### 3. **Start Chatting**

* Type your message in chat input
* Click 🎤 for voice input
* Upload files with 📎 button
* Create new chats with 🆕 button

### 4. **Manage Chats**

* Switch between different chats
* Rename chats for organization
* Export chats as PDF/TXT
* Clear chat history when needed

## 💡 Examples

### For Students:

**bash**

```
# Ask JARVIS:
"Explain quantum physics in simple terms"
"Help me solve this math problem"
"Create a study plan for exams"
```

### For Developers:

**bash**

```
# Ask JARVIS:
"Write Python code for REST API"
"Debug this JavaScript error"
"Explain machine learning algorithms"
```

### For Professionals:

**bash**

```
# Ask JARVIS:
"Review my resume"
"Prepare for job interview"
"Business strategy suggestions"
```

## 🎨 UI Features

### Futuristic Design

* Cosmic gradient background
* Animated particles
* Glassmorphism effects
* Neon chat bubbles
* Real-time streaming responses
* Typing indicators

### Responsive Layout

* Works on desktop & mobile
* Adaptive chat interface
* Sidebar navigation
* Clean input controls

## 🔧 Advanced Usage

### Voice Commands

**python**

```
# Click microphone button
# Speak naturally
# JARVIS converts speech to text
# AI responds instantly
```

### File Analysis

**python**

```
# Upload text files
# JARVIS analyzes content
# Provides summaries
# Answers questions about file
```

### Export Options

**python**

```
# Export current chat as:
# - PDF (formatted document)
# - TXT (plain text)
# Files saved with timestamp
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://license/) file for details.

## 🙏 Acknowledgments

* **Google Gemini AI** for powerful language models
* **Streamlit** for amazing web framework
* **SpeechRecognition** for voice capabilities
* **Open source community** for inspiration

<div align="center">

---

<div align="center">

## ⭐ Support JARVIS

If you find this project helpful, please give it a star!
It helps others discover JARVIS and motivates further development.

**Built with**

</div>
