import os
import time
import threading

from src.Form import Form
from src.Window import Window
from src.Simulator import Simulator

class UI:
	def __init__(self, initial, final, level, pivot):
		self.simulator = Simulator(initial, final, level, pivot)
		self.background = Window(*(0, 0),  *os.get_terminal_size(), *os.get_terminal_size(), '01 ')

	def render_background_with_form(self, form):
		x = self.background.x + (self.background.width - form.width) // 2
		y = self.background.y + (self.background.height - form.height) // 2
		form.set_x_y(x, y)
		for i in range(100000):
			self.background.render_window(form)
			time.sleep(0.3)
			self.background.push_new_line_on_window()
		
	def one_game(self, form):
		tick = 0.3
		form.set_string('Enter size:', *(1, 1))
		time.sleep(tick)
		size = form.get_and_set_string_from_input(2, 1)
	
		data = self.simulator.get_data(int(size))
		initial = self.simulator.get_initial(data)
		form.set_string(initial, *(3, 1))
		time.sleep(tick)

		form.set_string('Enter string:', *(4 + 2, 1))
		time.sleep(tick)
		user_input = form.get_and_set_string_from_input(5 + 2, 1)

		form.set_string('Result:', *(6 + 2, 1))
		time.sleep(tick)
		result = self.simulator.validate_input(user_input, data)
		if result['status'] == 'SUCCESS':
			i = 7
			form.set_string('SUCCESS', *(7 + 2, 1))
			time.sleep(tick)
		else:
			for i, message in enumerate(result['messages'], start=7 + 2):
				result = ''
				if message[0] == 'incompatible':
					result = f'#{message[1]}, expected {message[3]} but was {message[2]}'
				else:
					result = f'Incorrect size'
				
				form.set_string(result, *(i, 1))
				time.sleep(tick)
		
		form.set_string('pause', *(i + 1 + 2, 1))
		time.sleep(tick)
		user_input = form.get_and_set_string_from_input(i + 2 + 2, 1)
		form.clean()

	def run(self):
		width, height = os.get_terminal_size()

		form = Form(width // 2, height // 2)
		thread = threading.Thread(target=self.render_background_with_form,args=([form]))
		thread.start()

		while True:
			self.one_game(form)