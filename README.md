Listen to the audio through natural language processing

Installation
::

    $ pip install -U textblob
    $ python -m textblob.download_corpora
    $ sudo apt-get install flac

Go to this site for twitter integration:

http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/

For the 2 programs speech.py and AudioCommand.sh:
::

    $ git clone git://github.com/Uberi/speech_recognition
    $ cd speech_recognition ; python setup.py install
    $ cd .. ; git clone git://github.com/muhdamrullah/Listen
    
Program the speech.py to execute command while the AudioCommand.sh will run full command

