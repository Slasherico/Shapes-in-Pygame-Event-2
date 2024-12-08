import pygame, time
pygame.init()

display_surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Birthday Greeting Card')
img = pygame.image.load('images/Blank_Paper.jpg')
imge = pygame.transform.scale(img,(600,600))

while True:
    font = pygame.font.SysFont('Aptos', 72)
    h_text = font.render('Happy', True, 'Red')
    b_text = font.render('Birthday', True, 'Blue')
    
    display_surface.fill('White')
    display_surface.blit(imge, (0,0))
    display_surface.blit(h_text, (200, 200))
    display_surface.blit(b_text, (400,200))
    
    pygame.display.update()
    time.sleep(2)