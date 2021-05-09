class Form:
	def __init__(self, width, height):
		self.x = 0
		self.y = 0
		self.width = width
		self.height = height
		self.image = self.generate_image()
		self.active = False

	def set_x_y(self, x, y):
		self.x = x
		self.y = y

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

	def clean(self):
		self.image = self.generate_image()

	def set_string(self, string, y, x):
		iterator = 0
		y = 1 if y == 0 else y
		for i in range(y, self.height - 1):
			for j in range(1, self.width - 1):
				if iterator >= len(string):
					return
				self.image[i][j] = string[iterator]
				iterator += 1

	def get_and_set_string_from_input(self, x, y):
		self.active = True
		string = input()
		self.set_string(string, x, y)
		self.active = False
		return string