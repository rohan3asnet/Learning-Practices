import pygame
import sys
#initialize pygame
pygame.init()
#setup the display
WIDTH, HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")
#colors
WHITE=(123, 231, 111)
BLACK=(10,20,30)
#Function to draw a line using DDA algorithm
def drawLineDDA(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dx), abs(dy))
    xIncrement=dx/steps
    yIncrement=dy/steps
    x=x1
    y=y1
    for i in range(steps):
        screen.set_at((round(x),round(y)),WHITE)
        x+=xIncrement
        y+=yIncrement


#main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        #clear the screen
        screen.fill(BLACK)
        #draw aline using DDA algorithm
        drawLineDDA(20,20,100,100)
        #update the diplay
        pygame.display.flip()

if __name__== "__main__":
    main()


