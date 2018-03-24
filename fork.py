import pygame
pygame.init()
#width and height
width = 1000
height = 800
#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#display maker
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ross is gay")

clock = pygame.time.Clock()
#images
rossFace = pygame.image.load("C:/Users/peepdussy/Downloads/ross face fixed.png")
menuScreenImage = pygame.image.load("C:/Users/peepdussy/Downloads/the game.png")




def ross(x,y):
    gameDisplay.blit(rossFace,(x,y))


x = (width//10)
y = (height //100)

def mainMenu():
    gameDisplay.blit(menuScreenImage,(-100,0))
    button = pygame.Rect(300,500,400,400)
    pygame.draw.rect(gameDisplay,red, button)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos) == True:
                return True


def main():
#game running loop
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill(white)
        mainMenuTruth = mainMenu()
        if mainMenuTruth == True:
            ross(x,y)
            
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
main()
     
    
