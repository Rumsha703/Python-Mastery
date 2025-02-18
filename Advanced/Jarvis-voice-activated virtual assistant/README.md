# Jarvis - Voice-Activated Virtual Assistant

Jarvis is a voice-activated virtual assistant designed to perform tasks such as web browsing, playing music, fetching news, and responding to user queries using OpenAI's GPT-3.5-turbo model. Inspired by the iconic AI from Iron Man, Jarvis is your personal assistant for everyday tasks.

---

## Features

- **Voice Recognition**  
  Utilizes the `speech_recognition` library to listen for and recognize voice commands.  
  Activates upon detecting the wake word **"Jarvis."**

- **Text-to-Speech**  
  Converts text to speech using `pyttsx3` for local conversion.  
  Uses `gTTS` (Google Text-to-Speech) and `pygame` for playback.

- **Web Browsing**  
  Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.

- **Music Playback**  
  Interfaces with a `musicLibrary` module to play songs via web links.

- **News Fetching**  
  Fetches and reads the latest news headlines using `NewsAPI`.

- **OpenAI Integration**  
  Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo.  
  Acts as a general virtual assistant similar to Alexa or Google Assistant.

---

## Workflow

1. **Initialization**  
   - Greets the user with *"Initializing Jarvis...."*

2. **Wake Word Detection**  
   - Listens for the wake word **"Jarvis."**  
   - Acknowledges activation by saying *"Ya."*

3. **Command Processing**  
   - Processes commands to determine actions such as:  
     - Opening a website  
     - Playing music  
     - Fetching news  
     - Generating a response via OpenAI  

4. **Speech Output**  
   - Provides responses using the `speak` function with either `pyttsx3` or `gTTS`.

---

## Libraries Used

- **`speech_recognition`**: For voice recognition and command processing.  
- **`webbrowser`**: For opening websites.  
- **`pyttsx3`**: For local text-to-speech conversion.  
- **`musicLibrary`**: For playing music via web links.  
- **`requests`**: For making API requests (e.g., fetching news).  
- **`openai`**: For integrating with OpenAI's GPT-3.5-turbo model.  
- **`gTTS`**: For Google Text-to-Speech functionality.  
- **`pygame`**: For audio playback.  
- **`os`**: For system-level operations.

---

## How to Use

1. Install the required libraries:
   ```bash
   pip install speechrecognition pyttsx3 gtts pygame requests openai


## How to Run
1. Clone the repository (if you haven't already):
   ```bash
   git clone https://github.com/Rumsha703/Python-Mastery.git