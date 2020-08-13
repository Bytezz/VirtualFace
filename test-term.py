import thread,pyttsx3,time,terminal_virtualface as virtualface
def voice(txt):
	global tts
	global busy
	tts.say(txt)
	busy=True
	tts.runAndWait()
	tts.stop()
	busy=False
virtualface.face()
global tts
global busy
tts=pyttsx3.init()
busy=True
thread.start_new_thread(voice,("Hello, World!",))
while busy:
	virtualface.face(speak=True)
	time.sleep(.1)
virtualface.face()