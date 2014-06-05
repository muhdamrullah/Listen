#FaceRecog.asia
#10/29/13
#stt.sh
i=1;
for (( ; ; ))
do
	echo "Recording your Speech (Ctrl+C to Transcribe)"
	arecord -f cd -t wav -d 10 -q -r 16000 | flac - -s -f --best --sample-rate 16000 -o facerecog.flac;

	echo "Converting Speech to Text..."
	wget -q -U "Mozilla/5.0" --post-file facerecog.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw" | cut -d\" -f12  > stt.txt

	echo "EarRecog said:"
	value=`cat stt.txt`
	echo "$value"
        python sentiment.py
#part 2
#	python SillyTweet.py "Detecting ... $value"
done
