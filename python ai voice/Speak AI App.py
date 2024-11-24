import tkinter as tk
import pyttsx3

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speak AI App")
        self.root.geometry("400x200")

        # Initialize speaker
        self.speaker = pyttsx3.init()
        self.speaker.setProperty('rate', 139)  # Set the speed of the voice

        # Select a female voice
        voices = self.speaker.getProperty('voices')
        print(voices,'-----------------')
        # print(dict(voices))
        for voice in voices:
            if 'female' in voice.name.lower():  # Look for a female voice
                self.speaker.setProperty('voice', voice.id)
                break

        # Label
        self.label = tk.Label(root, text="Speak AI", font=("Arial", 14))
        self.label.pack(pady=10)

        # Text Entry
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=10)

        # Speak Button
        self.speak_button = tk.Button(root, text="Speak", command=self.speak_text)
        self.speak_button.pack(pady=10)

    def speak_text(self):
        """Retrieve text from entry and speak it in a female voice"""
        text = self.text_entry.get()
        if text:
            # print(f"Text entered: {text}")
            # self.speaker.say(text)  
            # self.speaker.runAndWait()
            if text == "hi":
                self.speaker.say("Hi, Master")
                self.speaker.runAndWait()
            elif text == "what is love":
                self.speaker.say("Love is not easy for you now time, please try again ams ")
                self.speaker.runAndWait()
        else:
            self.speaker.say("Please enter some text") 
            self.speaker.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
