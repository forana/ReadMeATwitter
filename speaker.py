import subprocess
import pipes
import urllib

CMD = "mpg123 %s 2> /dev/null"
URL = "http://translate.google.com/translate_tts?tl=en&q=%s"

def speak(text):
	fullURL = URL % (urllib.quote(text),)
	fullCMD = CMD % (pipes.quote(fullURL),)
	subprocess.call(fullCMD, shell = True)
