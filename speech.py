import speech_recognition as sr
import subprocess

def voice2Audio():
    print("Recording speech 10secs")
    subprocess.call(['arecord', '-f', 'cd', '-t', 'wav', '-d', '10', '-q', '-r', '16000', '-c', '1', 'audio.wav'])

def audio2Text():
    r = sr.Recognizer()
    with sr.WavFile("audio.wav") as source:
        audio = r.record(source)

    try:
	print("Transcribing...")
        x = "Transcription: " + r.recognize(audio)
        print x
    except LookupError:
        print("Could not understand audio")

while True:
    voice2Audio()
    audio2Text()
