import random
from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat, object): # IF you explicitly state the object (which helps the code be run by Python 2 and 3 at the same time) you have to enter the non-native, non-subclass class first. In this case putting Combat first, and then object. If you put object first you'd get a MRO (method resolution error) because it would try to import the Combat stuff and then override it with the object stuff. Object-oriented programming is confusing. 
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

	def __str__(self): 	# this function controls how the class instances will print themselves. 
		return '{} {}, HP: {}, XP: {}'.format(self.color.title(), 
											  self.__class__.__name__, 
											  self.hit_points,
											  self.experience)


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