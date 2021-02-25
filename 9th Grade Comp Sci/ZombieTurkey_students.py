from gamelib import *

'''Initialize the Game'''
#Creates the game with Width, Height, and Title
game = Game(800, 600, "Zombie Thanksgiving")

'''Background for the Game'''
#Creates the background for the game
bk = Image("Zbk.jpg", game)
bk.resizeTo(game.width, game.height)


'''Turkey'''
#Creates the turkey Image

#Down Scales The Turkey by a percentage

#Set speed and Angle of movement




'''Zombie'''
#Creates the Zombie Image

#Down Scales the Zombie by a percentage

#Set speed & Angle of movement -- Important to make this different than turkey otherwise they will follow each other




'''Scope'''
#Creates the CrossHair

#Down Scales the crosshair by a percentage



'''Sounds -- require a path AND a channel as input'''
#Sound and Channel for the the crosshair

#Sound and Channel for Zombie being hit

#Sound and Channel for Turkey being bit

#Sound and Channel for Zombie Chomping on Turkey



'''Fonts'''
f = Font(black, 40, green, "Comic Sans MS")


while not game.over:

	'''Need this to initialize the game'''
	#This code processess the input: Keyboard, Mouse, Joystick
	game.processInput()
	#This code draws the background
	bk.draw()

	'''Draw and move Characters'''
	#Draw the turkey & Make it move

	#Draw zombie and make it move

	#Draw Scope -- We want the scope to follow the mouse: moveTo()  processInput() has the mouse.x, mouse.y



	'''Actions'''
	#Makes sound if Click the Mouse


	#Clicking Mouse on Zombie

		#Decrease the Zombies Health -- always starts at 100 (See Image(object) --> self.heatlh = 100)


		'''Change Zombie's Position'''
		#X position 0 < x < 800 -- Don't want zombie to randomly appear on the edge of the screen; then he wont bounce

		#Y position 0 < y < 600

		#Move Zombie to new coordinates

		#Increase speed of zombie after he is hit

		#Make sound of Zombie being hit


	#When Zombie collided with Turkey

		#Decrease Turkey Health


		'''Change Zombie's Position'''
		#X position 0 < x < 800 -- Don't want turkey to randomly appear on the edge of the screen; then he wont bounce

		#Y position 0 < y < 600

		#Move Turkey to new coordinates
		

		#Play Bit Sound
		
		#Play Chomp Sound
		



	# How to end the game
	




	'''Display Stats of Images'''
	#Display Turkey's Health
	
	#Display Zombie Stats
	



	#updates the game 30 frames per second (fps)
	game.update(30)



#Quits out of the game once the while loop finishes
game.quit()