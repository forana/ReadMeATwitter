import subprocess
import config
import pipes

def speak(text):
	subprocess.call(config.SPEAK_CMD + [pipes.quote(text)])
