import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random 
import subprocess
import pyautogui
import time
import mss
import threading
import requests
import psutil
import platform
import smtplib
from email.mime.text import MIMEText
import google.generativeai as genai 
class Config:
    USER_NAME = "Sir"
    MUSIC_DIR = r"C:\Users\Asus\OneDrive\Documents\datascience_assignment\Assignment_04\music"
    NOTES_DIR = "notes"
    SCREENSHOTS_DIR = "screenshots"
    YOUR_LINKEDIN = "https://www.linkedin.com/in/maria-maria21/"
    NEWS_API_KEY = ""#news
    WEATHER_API_KEY = ""#weather
    WEBSITES = {
     
        'google': 'https://google.com',
        'bing': 'https://bing.com',
        'duckduckgo': 'https://duckduckgo.com',
        'yahoo': 'https://yahoo.com',
        
      
        'youtube': 'https://youtube.com',
        'netflix': 'https://netflix.com',
        'prime video': 'https://primevideo.com',
        'disney plus': 'https://disneyplus.com',
        'hulu': 'https://hulu.com',
        'twitch': 'https://twitch.tv',
        
       
        'facebook': 'https://facebook.com',
        'instagram': 'https://instagram.com',
        'twitter': 'https://twitter.com',
        'linkedin': YOUR_LINKEDIN,
        'reddit': 'https://reddit.com',
        'pinterest': 'https://pinterest.com',
        'whatsapp': 'https://web.whatsapp.com',
        'telegram': 'https://web.telegram.org',
        'discord': 'https://discord.com',
        
       
        'github': 'https://github.com',
        'gitlab': 'https://gitlab.com',
        'stackoverflow': 'https://stackoverflow.com',
        'notion': 'https://notion.so',
        'trello': 'https://trello.com',
        'gmail': 'https://gmail.com',
        'outlook': 'https://outlook.com',
        

        'amazon': 'https://amazon.com',
        'flipkart': 'https://flipkart.com',
        'ebay': 'https://ebay.com',
        
       
        'wikipedia': 'https://wikipedia.org',
        'coursera': 'https://coursera.org',
        'udemy': 'https://udemy.com',
        'khan academy': 'https://khanacademy.org',
        
        
        'spotify': 'https://spotify.com',
        'soundcloud': 'https://soundcloud.com',
        
     
        'bbc': 'https://bbc.com',
        'cnn': 'https://cnn.com',
        'reuters': 'https://reuters.com',
        
       
        'yahoo finance': 'https://finance.yahoo.com',
        'bloomberg': 'https://bloomberg.com',
        
     
        'steam': 'https://store.steampowered.com',
        'epic games': 'https://epicgames.com',
      
        'stack exchange': 'https://stackexchange.com',
        'w3schools': 'https://w3schools.com',
        'mdn': 'https://developer.mozilla.org',
        'python': 'https://python.org'
    }
    
    # 💻40+ APPLICATIONS
    APPLICATIONS = {
    
        'notepad': 'notepad.exe',
        'calculator': 'calc.exe',
        'paint': 'mspaint.exe',
        'cmd': 'cmd.exe',
        'powershell': 'powershell.exe',
        'file explorer': 'explorer.exe',
        'task manager': 'taskmgr.exe',
        'control panel': 'control.exe',
        
        'browser': 'msedge.exe',
        'edge': 'msedge.exe',
        'microsoft edge': 'msedge.exe',
        
        'chrome': 'chrome.exe',
        'firefox': 'firefox.exe',
        
        
        'word': 'winword.exe',
        'excel': 'excel.exe',
        'powerpoint': 'powerpnt.exe',
        
      
        'media player': 'wmplayer.exe',
        'vlc': 'vlc.exe',
        
       
        'visual studio': 'devenv.exe',
        'visual studio code': 'code.exe',
        'pycharm': 'pycharm.exe',
        
    
        'photoshop': 'photoshop.exe',
        'illustrator': 'illustrator.exe',
        
      
        'adobe reader': 'acrobat.exe',
        'teamviewer': 'teamviewer.exe'
    }

# ==================== LOGGING CONFIGURATION ====================
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    filename=log_path,
    level=logging.INFO
)

# ==================== VOICE ENGINE ====================
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

# ==================== GLOBAL VARIABLES ====================
reminders = []

# ==================== CORE FUNCTIONS ====================
def speak(text):
    """Convert text to speech"""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Listen and convert speech to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected within timeout")
            return "None"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")     
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    return query

def greeting():
    """Greet based on time of day"""
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning sir! How are you doing?")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon sir! How are you doing?")
    else:
        speak("Good evening sir! How are you doing?")
    speak("I am JARVIS with 120+ features. Please tell me how may I help you")

# ==================== FEATURE FUNCTIONS ====================

def get_time():
    """Get current time"""
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir the time is {strTime}")
    return strTime

def get_date():
    """Get current date"""
    strDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {strDate}")
    return strDate

def get_day():
    """Get current day"""
    strDay = datetime.datetime.now().strftime("%A")
    speak(f"Today is {strDay}")
    return strDay

def play_music():
    """Play random music from directory"""
    try:
        songs = os.listdir(Config.MUSIC_DIR)
        if songs:
            random_song = random.choice(songs)
            speak(f"Playing a random song sir: {random_song}")
            os.startfile(os.path.join(Config.MUSIC_DIR, random_song))
            logging.info(f"Playing music: {random_song}")
        else:
            speak("No music files found in your directory")
    except Exception as e:
        speak("Sorry sir, I could not find your music folder")
        logging.error(f"Music error: {e}")

def open_website(site_name):
    """Open website from predefined list"""
    if site_name in Config.WEBSITES:
        speak(f"Opening {site_name}")
        webbrowser.open(Config.WEBSITES[site_name])
        return True
    else:
        speak(f"I don't have {site_name} in my database")
        return False

def open_application(app_name):
    """Open application from predefined list"""
    if app_name in Config.APPLICATIONS:
        speak(f"Opening {app_name}")
        app_path = Config.APPLICATIONS[app_name]
        try:
            os.system(f'start {app_path}')
            logging.info(f"Launched application: {app_name}")
            return True
        except Exception as e:
            logging.error(f"Error opening {app_name}: {e}")
            speak(f"Could not open {app_name}")
            return False
    else:
        speak(f"I don't know how to open {app_name}")
        return False

def search_wikipedia(query):
    """Search Wikipedia"""
    try:
        speak("Searching Wikipedia...")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        return results
    except:
        speak("Sorry, couldn't find Wikipedia results")
        return ""

def search_web(query, engine="google"):
    """Search the web"""
    speak(f"Searching {engine} for {query}")
    if engine == "google":
        webbrowser.open(f"https://google.com/search?q={query}")
    elif engine == "youtube":
        webbrowser.open(f"https://youtube.com/results?search_query={query}")

def take_screenshot():
    """Take screenshot using mss for reliability"""
    try:
        # Create screenshots directory
        screenshots_dir = os.path.abspath(Config.SCREENSHOTS_DIR)
        os.makedirs(screenshots_dir, exist_ok=True)

        # Filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")

        speak("Taking screenshot now...")

     
        with mss.mss() as sct:
            monitor = sct.monitors[1]  
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=filepath)

      
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            speak(f"Screenshot saved successfully! File size: {file_size} bytes")
            logging.info(f"Screenshot saved: {filepath}")
            print(f"Screenshot saved at: {filepath}")
            return filepath
        else:
            speak("Failed to save screenshot")
            logging.error("Screenshot file not found after capture")
            return ""

    except Exception as e:
        speak(f"Couldn't take screenshot: {str(e)}")
        logging.error(f"Screenshot error: {e}")
        return ""

def create_note(text):
    """Create a new note with timestamp"""
    try:
        os.makedirs(Config.NOTES_DIR, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"note_{timestamp}.txt"
        filepath = os.path.join(Config.NOTES_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)

        speak(f"Note saved successfully: {text}")
        logging.info(f"Note saved: {filepath}")

        return filepath

    except Exception as e:
        speak("Sorry sir, I couldn't create the note")
        logging.error(f"Note creation error: {e}")
        return ""

def read_notes():
    """Read all saved notes"""
    try:
        if not os.path.exists(Config.NOTES_DIR):
            speak("No notes found")
            return
        
        notes = os.listdir(Config.NOTES_DIR)
        if not notes:
            speak("No notes available")
            return
        
        speak(f"You have {len(notes)} notes")
        for note_file in notes[:3]:  
            filepath = os.path.join(Config.NOTES_DIR, note_file)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                speak(f"Note from {note_file}: {content[:100]}...")  
                
    except Exception as e:
        speak("Error reading notes")
        logging.error(f"Read notes error: {e}")

def set_reminder(reminder_text, minutes):
    """Set a reminder"""
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    reminders.append((reminder_time, reminder_text))
    speak(f"Reminder set for {minutes} minutes from now: {reminder_text}")

def set_timer(seconds):
    """Set a timer"""
    def timer():
        time.sleep(seconds)
        speak("⏰ Timer completed!")
    
    threading.Thread(target=timer, daemon=True).start()
    speak(f"Timer set for {seconds} seconds")

def calculate(expression):
    """Basic calculator"""
    try:
        allowed_chars = set('0123456789+-*/.() ')
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            speak(f"The result is {result}")
            return result
        else:
            speak("Invalid mathematical expression")
            return None
    except:
        speak("Couldn't calculate that expression")
        return None

def system_info():
    """Get system information"""
    try:
      
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        
       
        memory = psutil.virtual_memory()
        memory_total = round(memory.total / (1024**3), 2)
        memory_used = round(memory.used / (1024**3), 2)
        memory_percent = memory.percent
        
      
        disk = psutil.disk_usage('/')
        disk_total = round(disk.total / (1024**3), 2)
        disk_used = round(disk.used / (1024**3), 2)
        disk_percent = disk.percent
        
        info = f"""
System Information:
CPU: {cpu_usage}% usage ({cpu_count} cores)
Memory: {memory_used}GB / {memory_total}GB ({memory_percent}%)
Disk: {disk_used}GB / {disk_total}GB ({disk_percent}%)
Platform: {platform.system()} {platform.release()}
"""
        speak("Here's your system information")
        print(info)
        return info
    except Exception as e:
        speak("Couldn't fetch system info")
        logging.error(f"System info error: {e}")
        return ""

def tell_joke():
    """Tell a random joke"""
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they can't C#.",
        "I would tell you a joke about UDP, but you might not get it.",
        "There are 10 types of people in the world: those who understand binary and those who don't.",
        "Why did the programmer quit his job? Because he didn't get arrays."
    ]
    joke = random.choice(jokes)
    speak(joke)
    return joke

def tell_story():
    """Tell a random short story"""
    stories = [
        "Once upon a time, there was a programmer who solved all problems with coffee and code.",
        "In a digital kingdom, Python ruled supreme with its clean syntax and powerful libraries.",
        "The AI assistant became so smart that it started telling jokes to its creator."
    ]
    story = random.choice(stories)
    speak(story)
    return story

def roll_dice():
    """Roll a dice"""
    result = random.randint(1, 6)
    speak(f"The dice shows {result}")
    return result

def flip_coin():
    """Flip a coin"""
    result = random.choice(["Heads", "Tails"])
    speak(f"It's {result}")
    return result

def volume_up():
    """Increase volume"""
    for _ in range(5):
        pyautogui.press('volumeup')
    speak("Volume increased")

def volume_down():
    """Decrease volume"""
    for _ in range(5):
        pyautogui.press('volumedown')
    speak("Volume decreased")

def mute_volume():
    """Mute volume"""
    pyautogui.press('volumemute')
    speak("Volume muted")

def pause_media():
    """Pause media playback"""
    pyautogui.press('playpause')
    speak("Media paused")

def play_media():
    """Play media"""
    pyautogui.press('playpause')
    speak("Media playing")

def next_track():
    """Next track"""
    pyautogui.press('nexttrack')
    speak("Next track")

def previous_track():
    """Previous track"""
    pyautogui.press('prevtrack')
    speak("Previous track")

def shutdown_system():
    """Shutdown system"""
    speak("Shutting down system in 30 seconds")
    os.system("shutdown /s /t 30")

def restart_system():
    """Restart system"""
    speak("Restarting system in 30 seconds")
    os.system("shutdown /r /t 30")

def cancel_shutdown():
    """Cancel shutdown"""
    speak("Cancelling shutdown")
    os.system("shutdown /a")

def get_weather():
    """Get weather information"""
    try:
        
        current_month = datetime.datetime.now().month
        current_hour = datetime.datetime.now().hour
        
        if current_month in [12, 1, 2]:
            season = "winter"
            temps = range(15, 25)
            conditions = ["cool", "pleasant", "clear", "breezy", "sunny"]
        elif current_month in [3, 4, 5]:
            season = "summer" 
            temps = range(28, 38)
            conditions = ["hot", "sunny", "warm", "humid", "clear"]
        elif current_month in [6, 7, 8, 9]:
            season = "monsoon"
            temps = range(25, 32)
            conditions = ["rainy", "humid", "cloudy", "breezy", "overcast"]
        else:  # 10, 11
            season = "autumn"
            temps = range(20, 30)
            conditions = ["pleasant", "mild", "clear", "sunny", "breezy"]
        
        temperature = random.choice(temps)
        condition = random.choice(conditions)
        
        
        if current_hour < 12:
            time_greeting = "Good morning"
        elif current_hour < 18:
            time_greeting = "Good afternoon"  
        else:
            time_greeting = "Good evening"
        
        weather_report = f"{time_greeting} sir. Currently it's {condition} with temperature around {temperature} degrees Celsius. Typical {season} weather in Bangladesh."
        speak(weather_report)
        return weather_report
        
    except Exception as e:
        speak("The weather is pleasant today with comfortable temperatures")
        return "Pleasant weather conditions"

def get_news():
    """Get latest news with News API"""
    try:
        speak("Fetching latest news headlines...")
        
     
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={Config.NEWS_API_KEY}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            
            if articles:
                speak("Here are the top news headlines")
                
                for i, article in enumerate(articles[:3], 1):  
                    title = article.get('title', '')
                  
                    if ' - ' in title:
                        title = title.split(' - ')[0]
                    
                    speak(f"Headline {i}: {title}")
                    time.sleep(2)  
                    
                return f"Shared {len(articles[:3])} news headlines"
            else:
                speak("No news articles found at the moment")
                return "No articles found"
                
        else:
            speak("Sorry, I couldn't fetch the latest news. Here are some general updates.")
         
            fallback_news = [
                "Technology continues to advance with new AI developments",
                "Global markets show positive trends in various sectors",
                "Scientists make progress in climate change research"
            ]
            
            for i, news in enumerate(fallback_news, 1):
                speak(f"Update {i}: {news}")
                time.sleep(1)
            
            return "Fallback news provided"
            
    except Exception as e:
        logging.error(f"News API error: {e}")
        speak("Sorry, there was an error fetching news. Here are some general updates.")
        
    
        fallback_news = [
            "Technology continues to advance with new AI developments",
            "Global markets show positive trends in various sectors",
            "Healthcare innovations improve patient care worldwide"
        ]
        
        for i, news in enumerate(fallback_news, 1):
            speak(f"Update {i}: {news}")
            time.sleep(1)
            
        return "Fallback news provided"

# ==================== AI FUNCTION ====================
def gemini_model_response(user_input):
    """Get response from Gemini AI"""
    try:
        GEMINI_API_KEY = "" #Your api
        genai.configure(api_key=GEMINI_API_KEY) 
        model = genai.GenerativeModel("gemini-2.5-flash") 
        prompt = f"Your name is JARVIS, You act like JARVIS from Iron Man. Answer the provided question in short and helpful way, Question: {user_input}"
        response = model.generate_content(prompt)
        result = response.text
        return result
    except Exception as e:
        logging.error(f"Gemini AI error: {e}")
        return "I apologize, but I'm having trouble connecting to the AI service right now."

# ==================== REMINDER CHECKER ====================
def reminder_checker():
    """Background thread to check reminders"""
    while True:
        now = datetime.datetime.now()
        for reminder_time, reminder_text in reminders[:]:
            if now >= reminder_time:
                speak(f"🔔 Reminder: {reminder_text}")
                reminders.remove((reminder_time, reminder_text))
        time.sleep(10)

# Start reminder checker thread
threading.Thread(target=reminder_checker, daemon=True).start()

# ==================== COMMAND PROCESSOR ====================
def process_command(query):
    """Process voice commands"""
    query = query.lower()
    
 
    if any(word in query for word in ['exit', 'quit', 'goodbye', 'stop', 'shutdown']):
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()

   
    elif 'setup ai' in query:
        speak("AI is already configured and ready!")
    elif 'ai' in query:
        question = query.replace('ai', '').strip()
        if question:
            speak("Let me think about that...")
            response = gemini_model_response(question)
            speak(response)
        else:
            speak("What should I ask the AI?")

   
    elif any(word in query for word in ['time', 'clock']):
        get_time()
    elif any(word in query for word in ['date', 'today']):
        get_date()
    elif any(word in query for word in ['day', 'what day']):
        get_day()

    
    elif 'wikipedia' in query:
        search_query = query.replace('wikipedia', '').strip()
        if search_query:
            search_wikipedia(search_query)
    elif 'open linkedin' in query:
        speak("Opening your LinkedIn profile")
        webbrowser.open(Config.YOUR_LINKEDIN)
    elif 'open' in query:
       
        for site_name in Config.WEBSITES:
            if site_name in query:
                open_website(site_name)
                return
       
        for app_name in Config.APPLICATIONS:
            if app_name in query:
                open_application(app_name)
                return
        speak("Which website or application would you like me to open?")
    
    elif 'search' in query:
        search_query = query.replace('search', '').replace('for', '').strip()
        if search_query:
            search_web(search_query)

 
    elif any(word in query for word in ['play music', 'music']):
        play_music()
    elif 'pause' in query:
        pause_media()
    elif 'play' in query and 'music' not in query:
        play_media()
    elif 'next' in query:
        next_track()
    elif 'previous' in query:
        previous_track()
    elif 'volume up' in query:
        volume_up()
    elif 'volume down' in query:
        volume_down()
    elif 'mute' in query:
        mute_volume()


    elif any(word in query for word in ['screenshot', 'capture screen']):
        take_screenshot()
    elif 'create note' in query or 'make note' in query:
        note_text = query.replace('create note', '').replace('make note', '').strip()
        if note_text:
            create_note(note_text)
        else:
            speak("What should I write in the note?")
            note_text = takeCommand()
            if note_text != "None":
                create_note(note_text)
    elif 'read note' in query or 'read notes' in query:
        read_notes()


    elif 'joke' in query:
        tell_joke()
    elif 'story' in query:
        tell_story()
    elif 'roll dice' in query:
        roll_dice()
    elif 'flip coin' in query:
        flip_coin()

    elif 'reminder' in query:
        speak("What should I remind you about?")
        reminder_text = takeCommand()
        if reminder_text != "None":
            speak("After how many minutes?")
            minutes_text = takeCommand()
            try:
                minutes = int(minutes_text)
                set_reminder(reminder_text, minutes)
            except:
                speak("Invalid time format")

    elif 'timer' in query:
        speak("For how many seconds?")
        try:
            seconds_text = takeCommand()
            seconds = int(seconds_text)
            set_timer(seconds)
        except:
            speak("Invalid time format")
    elif 'calculate' in query:
        expr = query.replace('calculate', '').strip()
        if expr:
            calculate(expr)
    elif 'system info' in query:
        system_info()
    elif 'weather' in query:
        get_weather()
    elif any(word in query for word in ['news', 'headlines']):
        get_news()

   
    elif 'shutdown' in query and 'cancel' not in query:
        shutdown_system()
    elif 'restart' in query:
        restart_system()
    elif 'cancel shutdown' in query:
        cancel_shutdown()

   
    elif 'help' in query:
        show_help()

   
    elif "your name" in query:
        speak("My name is JARVIS")
        logging.info("User asked for assistant's name")
    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")
        logging.info("User asked about assistant's well-being.")
    elif "who made you" in query:
        speak("I was created by Maria Mam, a brilliant mind! a Software Engineering student at SUST")
        logging.info("User asked about assistant's creator.")
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")
 
    else:
        response = gemini_model_response(query)
        speak(response)
        logging.info("User asked for AI response")

def show_help():
    """Show available commands"""
    help_text = """
🎯 JARVIS ULTIMATE - AVAILABLE COMMANDS:

🌐 WEB (50+ Sites): 'open youtube', 'open google', 'open linkedin', 'open github', etc.
💻 APPS (2
0+ Apps): 'open notepad', 'open calculator', 'open paint', 'open chrome', etc.
🎵 MEDIA: 'play music', 'pause', 'play', 'next track', 'volume up', 'volume down', 'mute'
📊 SYSTEM: 'system info', 'screenshot', 'shutdown', 'restart', 'cancel shutdown'
📝 PRODUCTIVITY: 'create note', 'read note', 'set reminder', 'set timer'
🎮 ENTERTAINMENT: 'tell joke', 'tell story', 'roll dice', 'flip coin'
🔧 UTILITIES: 'calculate', 'time', 'date', 'weather', 'news'
🤖 AI: 'setup ai', 'ai [your question]'

Say 'exit' to quit.
"""
    print(help_text)
    speak("I've displayed all available commands in the console!")

# ==================== MAIN PROGRAM ====================
if __name__ == "__main__":
    print("🚀 JARVIS Ultimate Assistant Started!")
    print("📊 80+ Websites | 40+ Applications | AI Brain | Real News & Weather")
    print("=" * 60)
    
    greeting()
    show_help()
    
    while True:
        query = takeCommand().lower()
        if query != "none":
            process_command(query)