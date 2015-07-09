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

>>> from monster import Monster
>>> jubjub = Monster() # I can create a new monster by assigning a variable to the Monster() class

>>> type(jubjub) # when I check the type we can see that instead of a string, int, etc, it's a monster.Monster
<class 'monster.Monster'>

>>> jubjub.hit_points # jubjub starts will all of the default arguments and values (arguments? that's what he called them)
1
>>> jubjub.weapon 
'sword'

>>> jubjub.hit_points = 5 # but if we reassign the value of one attribute for jubjub it is mutable
>>> jubjub.hit_points
5

>>> jabberwock = Monster() # however the mutable value that we changed from jubjub above only affects jubjub it doesn't change any of the default Monster values. So when we create a new monster it will not be affected by those changes we made to jubjub
>>> jabberwock.hit_points
1
>>>

# WORKING WITH FUNCTIONS (METHODS) WITHIN CLASSES
>>> from monster import Monster # import the module

>>> jubjub = Monster() # create a new instance of the class
>>> jubjub.battlecry() # call the battlecry() 
'ROAR'

>>> jubjub.sound = 'tweet' # jubjub birds don't roar, let's reassign that 
>>> jubjub.battlecry()
'TWEET'
>>>