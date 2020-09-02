

import pygame
import random

#define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

#set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


#SnowFlake class
class snowflakes():
	def __init__(self, size, start_x, start_y,wind=False):
		self.size=size
		self.x=start_x
		self.y=start_y
	def fall (self, speed_x, speed_y):
		self.x+=speed_x
		self.y+=speed_y 
	def draw(self):
		pygame.draw.circle(screen, WHITE,(self.x, self.y), self.size)
	

#loop until the user clicks the close button.
done = False

#used to manage how fast the screen updates
clock = pygame.time.Clock()

#speed
speed = 3

#snow List
snow_list = []
for i in range(100):
	x = random.randrange(0,1000)
	y = random.randrange(0,1000)
	snow_list.append([x, y])


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
	# background image
	screen.fill(BLACK)

	# --- drawing code should go here
	# begin Snow
	
	
	for i in range(len(snow_list)):
		pygame.draw.circle(screen, WHITE, snow_list[i], 2)
		snow_list[i][1] += 1
		if snow_list[i][1] > 1000:
			y = random.randrange(0,700 )
			snow_list[i][1] = y
			x = random.randrange(0, 700)
			snow_list[i][0] = x



	
 

	# end Snow
	# --- go ahead and update the screen with what we've drawn
	pygame.display.flip()

	# --- limit to 60 frames per second
	clock.tick(60)

# close the window and quit
pygame.quit()
exit() # needed when using IDLE
