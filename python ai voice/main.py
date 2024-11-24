import sys
import threading
import tkinter as tk
import speech_recognition
import pyttsx3 as tts
from neuralintents import BasicAssistant  # Update to BasicAssistant

class Assistant:
    
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)  # Corrected "reate" to "rate"
        
        self.assistant = BasicAssistant("intents.json")  # Updated from GenericAssistant to BasicAssistant
        self.assistant.train_model()
        
        self.root = tk.Tk()
        self.label = tk.Label(text="LOGO", font=("Arial", 120, "bold"))
        self.label.pack()
        threading.Thread(target=self.run_assistant).start()
        
        self.root.mainloop()
        
    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    
                    if "hey aung" in text:
                        self.label.config(fg="red")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)  # Corrected "recoginze" to "recognize"
                        text = text.lower()
                        
                        if text == "stop":
                            self.speaker.say("Bye Aung Min Soe")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()  # Corrected "destory" to "destroy"
                            sys.exit()
                            
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                                self.label.config(fg="black")
                                
            except Exception as e:
                print(f"Error: {e}")
                self.label.config(fg="black")
                continue

Assistant()
