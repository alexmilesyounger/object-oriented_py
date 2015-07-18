class Monster: 
# classes are Titlecased by convention in Python

# defining classes is a lot like defining functions, except we use the 'class' keyword to start them. You can do the parenthesis ( ) after and include a dependency, ex. Monster(object), but that's not strictly necessary. 

# Also 'objects' in object-oriented programming are also known as classes. objects = classes, classes = objects. Although, he said something like everyting in Python is an object, tu I think that's a level of theoretical digging that I'll skip for the moment. 
	def __init__(self, hit_points=5, weapon='sword', color='yellow', sound='roar'):
		self.hit_points = hit_points
		self.weapon = weapon
		self.color = color
		self.sound = sound

	def battlecry(self):
		return self.sound.upper()