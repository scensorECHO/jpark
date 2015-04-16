import time
import pyaudio  
import wave
import _thread   
import threading
import datetime
        
class ThreadClass(threading.Thread):
	def run(self):
		while 1:
			#define stream chunk   
			chunk = 1024  

			#open a wav format music  
			f = wave.open(r"/home/tom/Documents/magicwrd.wav","rb")  
			#instantiate PyAudio  
			p = pyaudio.PyAudio()  
			#open stream  
			stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
			                channels = f.getnchannels(),  
			                rate = f.getframerate(),  
			                output = True)  
			#read data  
			data = f.readframes(chunk) 
			#paly stream  
			while data != '':  
				stream.write(data)  
				data = f.readframes(chunk) 
			time.sleep(.5)

# def magicWord():
# 	while 1:

denied = 'access: PERMISSION DENIED'
magicword = 'YOU DIDN\'T SAY THE MAGIC WORD!'

print ('Jurassic Park, System Security Interface')
print ('Version 4.0.5, Alpha E')
print ('Ready')
line = input('> ')
print(denied)
line = input('> ')
print(denied)
line = input('> ')
print(denied, end="")
time.sleep(1)
print('.....and......')
time.sleep(1)

t = ThreadClass()
t.start()

while 1:
	print(magicword)
	time.sleep(.2)
		
		


#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  
