import pygame
import random
import sys

from pygame.locals import*

Width=4
Height=4
FPSRATE=60
tile_size=80
res_width=1280
res_height=720
bsFontSize=30


WHITE = (255,255,255)
GREEN = (  0, 204,   0)
purple= (102,102,255)
Blank=None

X_Margin=int((res_width-(tile_size*Width+(Width-1)))/2)
Y_margin=int((res_height-(tile_size*Height+(Height-1)))/2)



def main():
    global FPS,UI,BsFont
    pygame.init()
    FPS=pygame.time.Clock()
    UI=pygame.display.set_mode((res_width, res_height))
    pygame.display.set_caption("GAME")
    
    Brd=BoardSpace()

    bg_image=pygame.image.load("stars.jpg").convert()
    UI.blit(bg_image, [0,0])
    FPS.tick(FPSRATE)

    
    
    

    


    
   

    





def LeftTop(t_x,t_y):
    left=X_Margin+(t_x*tile_size)+(t_x-1)
    top=Y_margin+(t_y*tile_size)+(t_y-1)
    return (left,top)



def Tile(t_x,t_y,number,adjx=0,adjy=0):

    
    left, top=LeftTop(t_x,t_y)
    pygame.draw.rect(UI,GREEN,(left+adjx,top+adjy,tile_size,tile_size))
    textS=BsFont.render(str(number),True,WHITE)
    textR=textS.get_rect(5)

def BoardSpace():
    counter=1
    board=[]
    for x in range(Width):
        column=[]
        for y in range(Height):
            column.append(counter)
            counter+=Width
        board.append(column)
        counter-=Width*(Height-1)+Width-1
    board[Width-1][Height-1]=Blank
    return board

def grid(board,message):
    UI.fill(purple)
    if message:
        ""
    
    for t_x in range(len(board)):
        for t_y in range(len(board[0])):
            if board[t_x][t_y]:
                ""


# Create a game loop


# Quit Pygame
pygame.quit()



if __name__=="__main__":
    main()