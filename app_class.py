from settings import *
from tkinter import *
from sys import exit
import pafy
import vlc

class App:
	_geometry = ''
	_stopped  = None
	def __init__(self):
		self.root = Tk()
		self.video = pafy.new(URL)
		self.best = self.video.getbest()
		self.playurl = self.best.url
		self.Instance = vlc.Instance()
		self.player = self.Instance.media_player_new()
		self.Media = self.Instance.media_new(self.playurl)
		self.Media.get_mrl()
		self.player.set_media(self.Media)
		self.player.play()
		self.running = True
		self.state = 'running'
		self.running_events()
		self.running_update()
		self.running_draw()

	def run(self):
		self.root.mainloop()

################# HELP FUNCTIONS #################

############# RUNNING FUNCTIONS #################
	def running_events(self):
		self.root.bind("<Escape>", exit)

	def running_update(self):
		pass

	def running_draw(self):
		pass

		


