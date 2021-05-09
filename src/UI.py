import os
import time
import threading

from src.Simulator import Simulator
from src.Window import Window

class UI:
	def __init__(self, initial, final, level, pivot):
		self.simulator = Simulator(initial, final, level, pivot)
		self.background = Window(*(0, 0),  *os.get_terminal_size(), *os.get_terminal_size(), '01 ')

	def render_background_with_form(self, form):
		height=len(form)
		width=len(form[0])
		x = self.background.x + (self.background.width - width) // 2
		y = self.background.y + (self.background.height - height) // 2
		for i in range(2):
			self.background.render_window(x=x, y=y, width=width, height=height, image=form)
			time.sleep(1)
			self.background.push_new_line_on_window()
		
	def run(self):
		form = [['=', '=', '=', '=', '=', '=', '=', '='], 
				['=', '=', '=', '=', '=', '=', '=', '='],
				['=', '=', '=', '=', '=', '=', '=', '='],
				['=', '=', '=', '=', '=', '=', '=', '='],
				['=', '=', '=', '=', '=', '=', '=', '='],
				['=', '=', '=', '=', '=', '=', '=', '='],
				['=', '=', '=', '=', '=', '=', '=', '='],
				['=', '=', '=', '=', '=', '=', '=', '='],
				['=', '=', '=', '=', '=', '=', '=', '=']]
		thread = threading.Thread(target=self.render_background_with_form,args=([form]))
		thread.start()
		# for i in range(len(data)):
		# 	for j in range(len(data[0])):
		# 		data[i][j] = '!'
# data = self.simulator.get_data(3)
# print(self.simulator.get_initial(data))
# response = input('Get response:')
# print(self.simulator.validate_input(response, data))
# def run(self, size):
#     
