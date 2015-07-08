class Monster: 
# classes are Titlecased by convention in Python

# defining classes is a lot like defining functions, except we use the 'class' keyword to start them. You can do the parenthesis ( ) after and include a dependency, ex. Monster(object), but that's not strictly necessary. 

# Also 'objects' in object-oriented programming are also known as classes. objects = classes, classes = objects. Although, he said something like everyting in Python is an object, tu I think that's a level of theoretical digging that I'll skip for the moment. 
	hit_points = 1
	color = 'yellow'
	weapon = 'sword'


# to call this up in the Python shell I could access it by doing:
>>> from monster import Monster
>>> Monster.hit_points
1
>>> Monster.color
'yellow'
>>> Monster.weapon
'sword'
