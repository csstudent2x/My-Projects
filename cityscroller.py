#GWC PROEJECT
#guidance comments by GWC

import pygame
import random
#define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
	return random.choice(colors)

#initialize the pygame class
pygame.init()

#width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#title of the window
pygame.display.set_caption("CityScroller")

#loops until the user clicks the close button
done = False

#used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
	"""
	used to create the building objects

	  x_point - an integer that represents where along the x-axis the building will be drawn
	  y_point - an integer that represents where along the y-axis the building will be drawn
	  x_point and y_point represent the top, left corner of the building

	  width - an integer that represents how wide the building will be in pixels
			a positive integer draws the building right to left(->)
			a negative integer draws the building left to right (<-)
	  height - an integer that represents how tall the building will be in pixels
			A positive integer draws the building up 
			A negative integer draws the building down 
	  color - a tuple of three elements which represents the color of the building
			Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

	it depends on:
		pygame being initialized in the environment
		it depends on a "screen" global variable that represents the surface where the buildings will be drawn

	"""
	def __init__(self, x_point, y_point, width, height, color):
		self.x_point = x_point
		self.y_point = y_point
		self.width = width
		self.height = height
		self.color = color
	def draw(self):
		pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height ))
		"""
		uses pygame and the global screen variable to draw the building on the screen
		"""

	def move(self, speed):
		self.x_point -= speed
	
		"""
		takes in an integer that represents the speed at which the building is moving
			a positive integer moves the building to the right ->
			a negative integer moves the building to the left  <-
		moves the building horizontally across the screen by changing the position of the
		x_point by the speed
		"""



class Scroller(object):
	"""
	object will create the group of buildings to fill the screen and scroll

	it takes:
		width - an integer that represents in pixels the width of the scroller
			this should only be a positive integer because a negative integer will draw buildings outside of the screen
		height - an integer that represents in pixels the height scroller
			a negative integer here will draw the buildings upside down
		base - an integer that represents where along the y-axis to start drawing buildings for this
			a negative integer will draw the buildings off the screen
			a smaller number means the buildings will be drawn higher up on the screen
			a larger number means the buildings will be drawn further down the screen
			to start drawing the buildings on the bottom of the screen this should be the height of the screen
		color - a tuple of three elements which represents the color of the building
			  each element being a number from 0 - 255 that represents how much red, green and blue the color should have
		speed - an integer that represents how fast the buildings will scroll

	it depends on:
		Building class being available to create the building obecjts
		building objects should have "draw" and "move" methods

	other info:
		it has an instance variable "buildings" which is a list of buildings for the scroller
	"""

	def __init__(self, width, height, base, color, speed):
		self.width = width	
		self.height = height
		self.base = base
		self.color = color
		self.speed = speed
		self.buildings_list = []


	def add_buildings(self):
		current_width = 0
		while current_width < self.width:
			add_building(current_width)
			current_width += self.buildings_list[-1].width

    """
		will call add_building until there the buildings fill up the width of the
		scroller.
		"""

	def add_building(self, x_location):
		random_width = random.randrange(self.width/10, self.width/4)		
		maximum_height = self.base - self.height
		height = random.randrange(50, maximum_height)
		y_location = self.base - height
		self.buildings_list.append(Building(x_location, y_location, random_width, height, self.color))
		#print(len(self.buildings_list))
		#takes in an x_location, an integer, that represents where along the x-axis to
		#put a buildng
		#adds a building to list of buildings

	def draw_buildings(self):
		for building in self.buildings_list:
			building.draw()
			
		"""
		calls the draw method on each building
		"""

	def move_buildings(self):
		for building in self.buildings_list:
			building.move(self.speed) # moving buildings 
		if len(self.buildings_list) == 0: 
			x_location = 0
			self.add_building(x_location)
		else:
			x_location = self.buildings_list[len(self.buildings_list)-1].x_point + self.buildings_list[len(self.buildings_list)-1].width #last element of list 
			self.add_building(x_location)
			
		
		"""
    calls the move method on each building passing in the speed variable
		as the buildings move off the screen a new one is added
		"""


FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 0, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 10, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
# -------- Main Program Loop -----------
while not done:
	# --- main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- game logic should go here

	# --- screen-clearing code goes here

	# here, we clear the screen to white. don't put other drawing commands
	# above this, or they will be erased with this command

	# if you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BACKGROUND_COLOR)

	# --- drawing code should go here
	
	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()


	# --- go ahead and update the screen with what we've drawn
	pygame.display.flip()

	# --- limit to 60 frames per second
	clock.tick(60)

# close the window and quit.
pygame.quit()
exit() # needed when using IDLE
