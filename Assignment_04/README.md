# JARVIS Ultimate Voice Assistant

JARVIS is a **Python-based voice assistant** inspired by Tony Stark's AI in  *Iron Man* . It interacts with the user via  **voice commands** , performs tasks like opening applications, searching online, playing music, telling jokes, managing reminders, and provides AI-powered answers using  **Gemini AI** .

JARVIS is designed to be  **hands-free** , intelligent, and fully customizable.

## Enjoy this demo video

https://drive.google.com/file/d/11oB71x9EPjdjtLPKoRWnHYFLZD-YVQie/view?usp=drivesdk

---

## 🛠 Features

### **1. Smart Greetings**

* Greets based on time of day (morning, afternoon, evening)
* Personalizes greetings to the user

### **2. Voice Command Recognition**

* Uses Google Speech Recognition to convert voice to text
* Recognizes multiple languages (default: English - India)

### **3. Web & AI**

* Search Wikipedia and summarize results
* Open 50+ websites (Google, YouTube, LinkedIn, Netflix, Gmail, GitHub, etc.)
* AI-powered answers using **Gemini AI**
* Context-aware responses

### **4. System Utilities**

* Get time, date, day
* System info (CPU, RAM, Disk usage, Platform)
* Take screenshots
* Shutdown, restart, or cancel shutdown
* Internet speed check
* Clipboard & file management (optional features)

### **5. Productivity**

* Create and read notes
* Set reminders and timers
* Persistent to-do management (can be extended)
* Email and WhatsApp integration (optional)

### **6. Media & Entertainment**

* Play random music from specified folder
* Media controls: play, pause, next, previous, volume up/down, mute
* Roll dice or flip a coin
* Tell jokes and short stories (static + AI-generated)

### **7. Advanced Features**

* Wake-word detection for hands-free operation
* Voice customization (male/female, speed adjustment)
* AI-generated jokes, stories, or short answers
* Modular and easily extensible command system

---

## Requirements

* **Python 3.11+**
* Packages:
  <pre class="overflow-visible!" data-start="2085" data-end="2216"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>pyttsx3
  SpeechRecognition
  wikipedia
  pyautogui
  mss
  psutil
  requests
  google.generativeai
  python-dotenv
  </span></span></code></div></div></pre>
* Optional:
  <pre class="overflow-visible!" data-start="2231" data-end="2396"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>googletrans==4.0.0rc1  # For translation feature
  pywhatkit               # For WhatsApp messages
  speedtest-cli           # For network speed test
  </span></span></code></div></div></pre>

---

## Installation

1. Clone the repository:

   <pre class="overflow-visible!" data-start="2450" data-end="2533"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> https://github.com/mariamaria21/jarvis.git
   </span><span>cd</span><span> jarvis
   </span></span></code></div></div></pre>
2. Create a virtual environment:

   <pre class="overflow-visible!" data-start="2571" data-end="2609"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv .venv
   </span></span></code></div></div></pre>
3. Activate the virtual environment:
   **Windows (PowerShell):**

   <pre class="overflow-visible!" data-start="2681" data-end="2733"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-powershell"><span><span>.\.venv\Scripts\Activate.ps1
   </span></span></code></div></div></pre>

   **Linux / macOS:**

   <pre class="overflow-visible!" data-start="2760" data-end="2803"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>source</span><span> .venv/bin/activate
   </span></span></code></div></div></pre>
4. Install dependencies:

   <pre class="overflow-visible!" data-start="2833" data-end="2882"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
   </span></span></code></div></div></pre>
5. Run the assistant:

   <pre class="overflow-visible!" data-start="2909" data-end="2943"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python jarvis.py
   </span></span></code></div></div></pre>

---

## 🎛 Usage

* **Start JARVIS:**

  Run `python jarvis.py` in the terminal. JARVIS will greet you and display available commands.
* **Available Commands:**

  <pre class="overflow-visible!" data-start="3112" data-end="3544"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>- Web: "open youtube", "open google", "open linkedin"
  - Apps: "open notepad", "open calculator", "open paint"
  - Media: "play music", "pause", "next track", "volume up/down"
  - System: "system info", "screenshot", "shutdown", "restart"
  - Productivity: "create note", "read notes", "set reminder", "set timer"
  - Fun: "tell joke", "tell story", "roll dice", "flip coin"
  - AI: "setup ai", "ai [your question]"
  </span></span></code></div></div></pre>
* **Example Usage:**

  <pre class="overflow-visible!" data-start="3569" data-end="3841"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>User: "Hey JARVIS, open YouTube"
  JARVIS: "Opening YouTube"

  User: "JARVIS, tell me a joke"
  JARVIS: "Why don't programmers like nature? It has too many bugs."

  User: "AI, explain quantum computing in short"
  JARVIS: "Let me think about that..."
  </span></span></code></div></div></pre>

---

## 🛡 AI Integration

* Powered by **Gemini AI**
* Handles conversational queries and provides context-aware responses
* Can answer programming questions, general knowledge, and creative prompts
* Fallback to local jokes/stories if AI is unavailable

---

## 📂 Folder Structure

<pre class="overflow-visible!" data-start="4128" data-end="4464"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>JARVIS/
│
├─ jarvis.py           </span><span># Main program</span><span>
├─ config.py           </span><span># Configurations (paths, API keys, apps, websites)</span><span>
├─ notes/              </span><span># Saved notes</span><span>
├─ music/              </span><span># Music files</span><span>
├─ screenshots/        </span><span># Captured screenshots</span><span>
├─ logs/               </span><span># Application logs</span><span>
├─ requirements.txt    </span><span># Python dependencies</span><span>
</span></span></code></div></div></pre>

---

## Customization

* Change your  **name** ,  **music directory** ,  **LinkedIn URL** , and API keys in `Config` class.
* Add more **applications or websites** in `APPLICATIONS` and `WEBSITES` dictionaries.
* Adjust  **voice** ,  **speech rate** , and **wake-word detection** in `jarvis.py`.

---

## Future Improvements

* Persistent to-do list and reminders
* Dynamic AI-generated jokes, stories, and summaries
* Voice translation and multi-language support
* More system utilities (battery alerts, clipboard management)
* Integration with Google Calendar and email automation

---

## Author

**Maria** – Software Engineering student at SUST

Inspired by Tony Stark's JARVIS

---

## License

This project is **open-source** and free to use for learning purposes.

You can modify and extend it for personal projects.
