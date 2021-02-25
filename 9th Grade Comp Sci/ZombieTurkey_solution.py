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
turkey = Image("turkey.gif", game)
#Down Scales The Turkey
turkey.resizeBy(-70)
#Set speed and Angle of movement
turkey.setSpeed(6,45)



'''Zombie'''
#Creates the Zombie Image
zombie = Image("zombie.png", game)
#Down Scales the Zombie
zombie.resizeBy(-90)
#Set speed & Angle of movement -- Important to make this different than turkey otherwise they will follow each other
zombie.setSpeed(2,20)
zombie.health = 20



'''Scope'''
#Creates the CrossHair
scope = Image("crosshair.png", game)
#Down Scales the crosshair
scope.resizeBy(-70)


'''Sounds -- require a path AND a channel'''
#Sound and Channel for the the crosshair
shoot = Sound("Gun2.wav", 1)
#Sound and Channel for Zombie being hit
hit = Sound("ZombieDie.wav", 2)
#Sound and Channel for Turkey being bit
bit = Sound("TurkeyGooble.wav", 3)
#Sound and Channel for Zombie Chomping on Turkey
chomp = Sound("ZombieChomp.wav", 4)


'''Fonts'''
f = Font(black, 40, green, "Comic Sans MS")

# level = 1
while not game.over:
	# zombies = createZombie(level)
	'''Need this to initialize the game'''
	#This code processess the input: Keyboard, Mouse, Joystick
	game.processInput()
	#This code draws the background
	bk.draw()

	'''Draw and move Characters'''
	#Draw the turkey & Make it move
	turkey.move(bounce = True)
	#Draw zombie and make it move
	zombie.move(bounce = True)
	#Draw Scope -- We want the scope to follow the mouse: moveTo()  processInput() has the mouse.x, mouse.y
	scope.moveTo(mouse.x, mouse.y)


	'''Actions'''
	#Makes sound if Click the Mouse
	if mouse.LeftClick:
		shoot.play()

	#Clicking Mouse on Zombie
	if mouse.collidedWith(zombie, shape = 'rectangle') and mouse.LeftClick:
		#Decrease the Zombies Health -- always starts at 100 (See Image(object) --> self.heatlh = 100)
		zombie.health -=5

		'''Change Zombie's Position'''
		#X position 0 < x < 800 -- Don't want zombie to randomly appear on the edge of the screen; then he wont bounce
		x = randint(100,600)
		#Y position 0 < y < 600
		y = randint(100, 500)
		#Move Zombie to new coordinates
		zombie.moveTo(x, y)

		#Increase speed of zombie after he is hit
		zombie.speed += 1
		#Make sound of Zombie being hit
		hit.play()

	#Zombie collidedWith() Turkey
	if zombie.collidedWith(turkey):
		#Decrease Turkey Health
		turkey.health -= 5

		'''Change Zombie's Position'''
		#X position 0 < x < 800 -- Don't want turkey to randomly appear on the edge of the screen; then he wont bounce
		x = randint(100,600)
		#Y position 0 < y < 600
		y = randint(100, 500)
		#Move Turkey to new coordinates
		turkey.moveTo(x, y)

		#Play Bit Sound
		bit.play()
		#Play Chomp Sound
		chomp.play()


	# How to end the game
	if zombie.health <= 0 or turkey.health <= 0:
		game.over = True




	'''Display Stats of Images'''
	#Display Turkey's Health
	game.drawText(turkey.health, turkey.x + 25, turkey.y + 60, f)
	#Display Zombie Stats
	game.drawText(zombie.health, zombie.x + 25, zombie.y + 60, f)



	#updates the game 30 frames per second (fps)
	game.update(30)



#Quits out of the game once the while loop finishes
game.quit()