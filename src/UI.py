import os
import time

from src.Simulator import Simulator
from src.Window import Window


class UI:
	def __init__(self, initial, final, level, pivot):
		self.simulator = Simulator(initial, final, level, pivot)
		self.background = Window(*(10, 10),  *(20, 20), *os.get_terminal_size(), '01 ')

	def render_data(self, rectangle):
		for line in rectangle:
			print(''.join(line), end='\r')

	def run(self):
		for i in range(25):
			data = [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']]
			self.background.render_window(x=15, y=15, width=3, height=3, image=data)
			time.sleep(1)
			self.background.push_new_line_on_window()

		# data = self.simulator.get_data(3)
		# print(self.simulator.get_initial(data))
		# response = input('Get response:')
		# print(self.simulator.validate_input(response, data))
	# def run(self, size):
	#     
