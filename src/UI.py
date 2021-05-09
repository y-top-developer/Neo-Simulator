import os
import time
import threading

from src.Simulator import Simulator
from src.Window import Window

class Form:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.image = self.generate_image()

	def generate_image(self):
		result = []
		for i in range(self.height):
			line = []
			for j in range(self.width):
				if i in [0, self.height - 1] or j in [0, self.width - 1]:
					line.append('#')
				else:
					line.append(' ')
			result.append(line)
		return result



class UI:
	def __init__(self, initial, final, level, pivot):
		self.simulator = Simulator(initial, final, level, pivot)
		self.background = Window(*(0, 0),  *os.get_terminal_size(), *os.get_terminal_size(), '01 ')

	def render_background_with_form(self, form):
		x = self.background.x + (self.background.width - form.width) // 2
		y = self.background.y + (self.background.height - form.height) // 2
		for i in range(4):
			self.background.render_window(x=x, y=y, width=form.width, height=form.height, image=form.image)
			time.sleep(1)
			self.background.push_new_line_on_window()
		
	def run(self):
		form = Form(10, 10)
		thread = threading.Thread(target=self.render_background_with_form,args=([form]))
		thread.start()
		# a = input()
		# form.set('Enter size:', *(0, 0))


		# for i in range(len(data)):
		# 	for j in range(len(data[0])):
		# 		data[i][j] = '!'
# data = self.simulator.get_data(3)
# print(self.simulator.get_initial(data))
# response = input('Get response:')
# print(self.simulator.validate_input(response, data))
# def run(self, size):
#     
