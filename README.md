TASK1:
🎙️ Python Voice Assistant
A simple yet powerful voice-controlled assistant created using Python. This assistant can search Wikipedia, tell the time, open websites like Google and Spotify, and even crack a joke!

Features
Voice-based command recognition
Text-to-speech responses
Wikipedia summaries
Time-telling functionality
Jokes for entertainment
Opens popular websites like Google and Spotify
Graceful greeting and exit
Requirements
Make sure you have the following Python libraries installed:

speechrecognition
pyttsx3
wikipedia
pyjokes
pyaudio (for microphone access)
Standard libraries: datetime, webbrowser, os
You can install the dependencies using:

pip install speechrecognition pyttsx3 wikipedia pyjokes pyaudio

# How to Use
- Clone or download this repository.
- Ensure your microphone is connected and configured.
- Run the Python script:
python voice_assistant.py


  

# Speak commands like:
- “Wikipedia Albert Einstein”
- “Open Google”
- “What’s the time”
- “Tell me a joke”
- “Open Spotify”

TASK2:
BMI Calculator GUI
A simple and intuitive Body Mass Index (BMI) calculator built with Python and Tkinter. Users can input their height and weight to instantly calculate their BMI.

Features
1.Clean and minimal graphical interface 2.Real-time BMI calculation on button click 3. Input validation with error handling 4.Lightweight and beginner-friendly Python script

Requirements
Python 3.x
Tkinter (pre-installed with Python on most systems)
How to Run
Clone this repository or download the Python file.

git clone https://github.com/your-username/bmi-calculator-gui.git
cd bmi-calculator-gui

TASK3:
Password Generator (Python GUI)
A user-friendly password generator built using Python's Tkinter library. This tool lets you customize the number of letters, numbers, and symbols to generate secure and personalized passwords.

Features
1.Custom input for letters, numbers, and symbols 2.Generates a randomized secure password 3.Lightweight, responsive GUI 4.Easy to use for beginners

Screenshots
Screenshot 2025-06-22 141011

Screenshot 2025-06-22 141033

Requirements
Python 3.x
Tkinter (usually comes pre-installed with Python)
How to Run
1.Clone the repository:
git clone https://github.com/your-username/password-generator-gui.git
cd password-generator-gui

TASK4:
# Weather Forecast Application
This is a simple desktop weather application built using Python and Tkinter. The app allows users to enter a city name and retrieve real-time weather data using the OpenWeatherMap API.
# Features
- Real-time weather data for any city
- Temperature displayed in Celsius and Fahrenheit
- Clean and responsive GUI made with Tkinter
- Weather condition display (e.g., Clear, Clouds, Rain)
- Error handling for invalid or empty city input
# Requirements
- Python 3.x
- requests
- configparser
- emoji (optional, if using emojis elsewhere)
Install dependencies:
pip install requests emoji


# API Key Setup
- Sign up at OpenWeatherMap and get a free API key.
- Create a file named api.key in the same directory as the script.
- Format the file as shown:
[api_key]
key=your_api_key_here


# How to Run
python weather_app.py


Then, enter any city name and click Search Weather  to see the current weather conditions.
📂 File Structure
├── weather_app.py       # Main Python script
├── api.key              # API key storage


