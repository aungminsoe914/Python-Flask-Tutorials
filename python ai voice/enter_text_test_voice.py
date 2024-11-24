import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print available voices (optional)
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.languages}")

# Set the voice to a selected voice (change the index if necessary)
female_voice_index = 19  # Change this index to the desired voice
engine.setProperty('voice', voices[female_voice_index].id)

# Example text to be spoken
text_to_speak = "Hello, this is a voice test."

# Speak the text
engine.say(text_to_speak)
engine.runAndWait()
