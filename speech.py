import speech_recognition as sr
import subprocess
import re

def voice2Audio():
    print("Recording speech 10secs")
    subprocess.call(['arecord', '-f', 'cd', '-t', 'wav', '-d', '5', '-q', '-r', '16000', '-c', '1', 'audio.wav'])

def playVideo():
    subprocess.call(['mplayer', '-fs', 'DynabitesPlayMini.mov'])

def audio2Text():
    r = sr.Recognizer()
    with sr.WavFile("audio.wav") as source:
        audio = r.record(source)

    listVulgar = ['az', 'bz', 'cz', 'dz', 'ez', 'fz', 'gz', 'hz', 'iz', 'jz', 'kz', 'lz', 'mz', 'nz', 'oz,', 'pz', 'qz', 'rz', 'sz', 'tz', 'uz', 'vz', 'wz', 'xz', 'yz', 'zz', 'damn', 'ass', 'god', 'stupid', 'no']

    try:
	print("Transcribing...")
        x = str(r.recognize(audio))
	print x
	replace = re.sub("[*]", 'z ', x)
        wordList = re.sub("[^\w]", " ", replace).split()
	print wordList

#Executes the command here
	if any(i in wordList for i in listVulgar):
            print 'YOU DIE!'
	    playVideo()
        
    except LookupError:
        print("Could not understand audio")

while True:
    voice2Audio()
    audio2Text()
