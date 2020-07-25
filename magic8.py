import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Magic 8 Ball")

#Magic 8 ball background
background = pygame.image.load('8ball.png')

font = pygame.font.Font('freesansbold.ttf', 32)

def message():
	screen.blit(background, (0, 0))
	pygame.display.update()
	pygame.time.wait(500)
	magic = ['YES', 'NO', 'EH']
	num = random.randint(0,2)
	text = font.render(str(magic[num]), True, (50, 62, 168))

	if num == 0:
		screen.blit(text, (167,190))
	else:
		screen.blit(text, (176,190))
	

running = True
screen.fill((0,0,0))
screen.blit(background, (0, 0))

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	m1, m2, m3 = pygame.mouse.get_pressed()
	if m1 == True:
		message()	
		
	pygame.display.update()