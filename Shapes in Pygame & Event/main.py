import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill("Grey")
pygame.display.update()

class Circle():
    def __init__(self, size, color, spawnpos, bordersize):
        self.circsize = size
        self.circcolor = color
        self.circspawn = spawnpos
        self.circborder = bordersize
        self.circsurface = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circsurface, self.circcolor, self.circspawn, self.circsize, self.circborder)
    
    def grow(self, r):
        self.circsize = self.circsize+r
        self.draw_circle = pygame.draw.circle(self.circsurface, self.circcolor, self.circspawn, self.circsize, self.circborder)

class Rectangle():
    def __init__(self, color, width, height, x, y, bordersize):
        self.rectwidth = width
        self.rectheight = height
        self.rectcolor = color
        self.rectx = x
        self.recty = y
        self.rectborder = bordersize
        self.rectsurface = screen
    
    def draw(self):
        self.draw_rect = pygame.draw.rect(self.rectsurface, self.rectcolor, (self.rectwidth, self.rectheight, self.rectx, self.recty), self.rectborder)



b_rect = Rectangle("Blue", 50, 50, 175, 175, 0)
g_rect = Rectangle("Green", 275, 275, 50, 50, 0)


# circ = Circle(50, (0,0,255), (100,100), 0)
# circ.draw()



pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    b_rect.draw()
    g_rect.draw()
    pygame.display.update()
pygame.quit()
