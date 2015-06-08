import speech_recognition as sr
import subprocess
import re

def voice2Audio():
    print("Recording speech 10secs")
    subprocess.call(['arecord', '-f', 'cd', '-t', 'wav', '-d', '5', '-q', '-r', '16000', '-c', '1', 'audio.wav'])

def audio2Text():
    r = sr.Recognizer()
    with sr.WavFile("audio.wav") as source:
        audio = r.record(source)

    list = ['az', 'damn it', 'ass', 'fz', 'sz', 'damn', 'god', 'stupid', 'oh my god', 'no']

    try:
	print("Transcribing...")
        x = str(r.recognize(audio))
	print x
	replace = re.sub("[*]", 'z ', x)
        wordList = re.sub("[^\w]", " ", replace).split()
	print wordList
	if any(i in wordList for i in list):
            print 'YOU DIE!'
        
    except LookupError:
        print("Could not understand audio")

while True:
    voice2Audio()
    audio2Text()
