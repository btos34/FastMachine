import pygame

pygame.init()


favicon = pygame.image.load('resources/images/favicon.png')

pygame.display.set_icon(favicon)
# da canvas
canvas = pygame.display.set_mode((600, 600))

# game title
pygame.display.set_caption("FastMachine: Gotta Go Fast")
exit = False

while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
	pygame.display.update()
