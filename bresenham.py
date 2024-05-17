import pygame
import sys
#initialize pygame
pygame.init()
#setup the display
WIDTH, HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham Line Drawing Algorithm")
#colors
WHITE=(123, 231, 111)
BLACK=(10,20,30)
#Function to draw a line using DDA algorithm
def drawLineBresenham(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    # if x2>x1:
    #     lx=1
    # else:
    #     lx=-1
    # if y2>y1:
    #     ly=1
    # else:
    #     ly=-1
    lx=1
    ly=1
    x=x1
    y=y1
    if(dx>dy):
        p=2*dy-dx
        while x!=x2:
            if(p<0):
                x=x+lx
                y=y
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
            screen.set_at((round(x),round(y)),WHITE)
    else:
        p=2*dx-dy
        while y!=y2:
            if(p<0):
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((round(x),round(y)),WHITE)




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
        drawLineBresenham(200,20,20,200)
        #update the diplay
        pygame.display.flip()

if __name__== "__main__":
    main()


