import speech_recognition as sr
import pyttsx3

class SpeechRecognitionApp:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()
        self.speaker.setProperty('rate', 150)  # Setting speed of speech
    
    def listen(self):
        """Listen for speech input"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.recognizer.listen(source)
            return audio

    def recognize_speech(self, audio):
        """Recognize speech and respond based on the content"""
        try:
            text = self.recognizer.recognize_google(audio)
            text = text.lower()
            print(f"You said: {text}")
            
            if text == "hi":
                return self.say_hello()
            elif text == "stop":
                return self.say_goodbye()
            else:
                self.speaker.say("I didn't understand that.")
                self.speaker.runAndWait()

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Request failed; check your internet connection.")
    
    def say_hello(self):
        """Respond with 'Hello'"""
        response = "Hello"
        print(response)
        self.speaker.say(response)
        self.speaker.runAndWait()

    def say_goodbye(self):
        """Respond with 'Bye bye' and stop the program"""
        response = "Bye bye"
        print(response)
        self.speaker.say(response)
        self.speaker.runAndWait()
        exit(0)  # Exit the program

if __name__ == "__main__":
    app = SpeechRecognitionApp()

    while True:
        audio_input = app.listen()  # Listen for input
        app.recognize_speech(audio_input)  # Respond based on input
