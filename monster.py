import random

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(object): # by explicitly stating the object in the Monster class, the class more easily works in Python 2 and Python 3 at the same time.
	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon = 'sword'
	sound = 'roar'

	def __init__(self, **kwargs): 
		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.min_experience, self.max_experience)
		self.color = random.choice(COLORS)

		for key, value in kwargs.items():
			setattr(self, key, value) # setattr, set attribute, take three arguments, what we set it on, the key passed in, and the value passed in.

	def battlecry(self): # a function that belongs to a class is called a method
		return self.sound.upper()


# Usually you limit yourself to one class per file, but in the case of subclasses it's less of a problem. 


class Goblin(Monster): # by putting Monster in as an argument, this tells python that Goblin is a subclass of Monster and that it automatically inherits all of the Monster attributes. 
	max_hit_points = 3
	max_experience = 2
	sound = 'squeak'


class Troll(Monster):
	min_hit_points = 3
	max_hit_points = 5
	min_experience = 2
	max_experience = 6
	sound = 'growl'

class Dragon(Monster):
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 10
	sound = 'roaaaaaaaar'