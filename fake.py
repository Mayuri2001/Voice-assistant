import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[1].id)
print(voices[1].id)
engine.say("Hello ")
engine.runAndWait()