i=1;
for (( ; ; ))
do
	echo "Recording your Speech (Ctrl+C to Transcribe)"
	arecord -f cd -t wav -d 10 -q -r 16000 -c 1 audio.wav
  
	echo "Converting Speech to Text..."
	python speech.py

done
