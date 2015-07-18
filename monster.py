class Monster: 
	def __init__(self, **kwargs): # **kwargs will take whatever arguments we give it as a dictionary and will parse them into keyword = value pairs
		self.hit_points = kwargs.get('hit_points', 1)
		self.weapon = kwargs.get('weapon', 'sword')
		self.color = kwargs.get('color', 'yellow')
		self.sound = kwargs.get('sound', 'roar')

	def battlecry(self): # a function that belongs to a class is called a method
		return self.sound.upper()