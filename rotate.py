import pygame, sys

def rotate(surface,angle):
	rotated_surface= pygame.transform.rotozoom(surface,angle,1)
	rotated_rect= rotated_surface.get_rect(center= (300, 300))
	return rotated_surface,rotated_rect

pygame.init()
clock= pygame.time.Clock()
screen_width, screen_height= 600, 600
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('rotating earth | Bhathi')
pygame.display.set_icon(pygame.image.load('earth.png'))

bg_img= pygame.image.load("bg.jpeg")
earth= pygame.image.load("earth.png")
earth= pygame.transform.smoothscale(earth,(400,400)) #change the size
earth_rect= earth.get_rect(center= (300, 300))
angle= 0

while True:
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			pygame.quit()
			sys.exit()

	angle-= 1 #clockwise (anticlockwise : angle+= 1 )
	screen.fill((000, 000, 000))
	earth_rotated,earth_rotated_rect= rotate(earth,angle)
	#consider the blit order...ex:bg first
	screen.blit(bg_img,(0,0))
	screen.blit(earth_rotated,earth_rotated_rect)
	pygame.display.flip()
	clock.tick(60)