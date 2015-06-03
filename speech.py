import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("test3.wav") as source:
    audio = r.record(source)

try:
    print("Transcription: " + r.recognize(audio))
except LookupError:
    print("Could not understand audio")
