import os
# import shutil
import spacy
import pyttsx3
import speech_recognition as sr

# Initialize natural language processing components
nlp = spacy.load("en_core_web_sm")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition
recognizer = sr.Recognizer()

# Define function to speak the response
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Define function for listening to voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""

# Define function for getting text input
def get_text_input():
    return input("Enter your command: ").lower()

# Define function for understanding the command
def understand(command):
    # Convert the command to lowercase for case-insensitive matching
    command_lower = command.lower()
    # Check if the command contains keywords associated with each intent
    if "shutdown" in command_lower:
        return "shutdown"
    elif "sleep" in command_lower:
        return "sleep"
    elif "restart" in command_lower:
        return "restart"
    else:
        return "unknown"


# Define functions for executing and responding to commands
def execute(intent):
    print("Executing intent:", intent)
    if intent == "shutdown":
        response = "Shutting down the computer."
        print(response)
        speak(response)
        os.system("shutdown /s /t 0")
    elif intent == "sleep":
        response = "Putting the computer to sleep."
        print(response)
        speak(response)
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif intent == "restart":
        response = "Restarting the computer."
        print(response)
        speak(response)
        os.system("shutdown /r /t 0")
    else:
        response = "Unknown intent: " + intent
        print(response)
        speak(response)


# Main loop for continuous interaction
while True:
    command = listen()
    if not command:
        command = get_text_input()
    if command:
        intent = understand(command)
        execute(intent)
