from random import choice

class Window:
	def __init__(self, x, y, width, height, terminal_width, terminal_height, characters):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.characters = characters
		self.image = self.generate_image()
		self.terminal_width = terminal_width
		self.terminal_height = terminal_height

	def generate_image(self):
		return [[choice(self.characters) for _ in range(self.width)] for _ in range(self.height)]

	def render_window(self, form=None):
		if form:
			while form.active:
				pass
		for y in range(self.terminal_height):
			if y < self.y or y >= self.height + self.y:
				print('\n', end='\r')
				continue
			line = ''
			for x in range(self.terminal_width):
				if x < self.x or x >= self.width + self.x:
					line += ' '
				elif form and y >= form.y and x >= form.x and y < form.y + form.height and x < form.x + form.width:
					line += form.image[y - form.y][x - form.x]
				else:
					line += self.image[y - self.y][x - self.x]
			print(line, end='\r')
	
	def push_new_line_on_window(self):
		self.image.pop()
		self.image.insert(0, [choice(self.characters) for _ in range(self.width)])