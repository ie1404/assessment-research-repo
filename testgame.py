import pygame
import time
import random
pygame.font.init()

# display res
WIDTH,HEIGHT=1280,720
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test game")

FPS=144

# taking image within folder and using as background variable and fits to window res.
BackGround=pygame.transform.scale   (pygame.image.load("stars.jpg"),(WIDTH,HEIGHT))

# player model
Player_width=20
Player_height=20

Player_velocity=10

Star_width=10
Star_height=10

Star_velocity=10

FONT=pygame.font.SysFont("Arial",30)

def draw(player,elapsed_time,stars,stars1,StarsRL):

    WINDOW.blit(BackGround,(0,0))

    time_text=FONT.render(f"Time: {round(elapsed_time)}s",1,"white")
    WINDOW.blit(time_text,(10,10))

    pygame.draw.rect(WINDOW,"red",player)

    for star in stars:
        pygame.draw.rect(WINDOW,"white",star)

    for star1 in stars1:
        pygame.draw.rect(WINDOW,"white",star1)

    for StarRL in StarsRL:
        pygame.draw.rect(WINDOW,"white",StarRL)

    # with update keeps image on screen
    pygame.display.update()


def main():
    run=True

    player=pygame.Rect(200, HEIGHT-Player_height,Player_width,Player_height)

    clock=pygame.time.Clock()

    start_time=time.time()
    elapsed_time=0

    star_add_increment=200
    star_count=0
    stars=[]

    star1_add_increment=200
    star1_count=0
    stars1=[]

    StarRL_add_increment=200
    StarRL_count=0
    StarsRL=[]
    
    hit=False


    while run:
        star_count+=clock.tick(FPS)
        star1_count+=clock.tick(FPS)
        StarRL_count+=clock.tick(FPS)  
        elapsed_time=time.time()-start_time   

        if star_count>star_add_increment:
            for _ in range(3):
                # area section that shows the range they can appear in
                star_x=random.randint(0,WIDTH-Star_width)
                # down
                star=pygame.Rect(star_x,Star_height,Star_width,Star_height)
                stars.append(star)
            
            star_add_increment=max(200,star_add_increment-50)
            star_count=0
        
        if star1_count>star1_add_increment:
            for _ in range(3):
                star1_y=random.randint(0,HEIGHT-Star_height)
                # across left to right
                star1=pygame.Rect(Star_height,star1_y,Star_width,Star_height)
                stars1.append(star1)
            
            star1_add_increment=max(200,star1_add_increment-50)
            star1_count=0

        if StarRL_count>StarRL_add_increment:
            for _ in range(3):
                StarRL_y=random.randint(0,HEIGHT-Star_height)

                StarRL=pygame.Rect(WIDTH,StarRL_y,Star_width,Star_height)
                StarsRL.append(StarRL)
            
            StarRL_add_increment=max(200,StarRL_add_increment-50)
            StarRL_count=0
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break   
        
        # detecting key press
        keys=pygame.key.get_pressed()
        # movement variable
        if keys[pygame.K_LEFT] and player.x-Player_velocity>=0:
            player.x-=Player_velocity
        if keys[pygame.K_RIGHT] and player.x+Player_velocity+Player_width<=WIDTH:
            player.x+=Player_velocity
        if keys[pygame.K_UP] and player.y+Player_velocity>=0:
            player.y-=Player_velocity
        if keys[pygame.K_DOWN] and player.y+Player_velocity+Player_height<=HEIGHT:
            player.y+=Player_velocity
        
        for star in stars[:]:
            star.y+=Star_velocity
            if star.y>HEIGHT:
                stars.remove(star)
            elif star.y>=player.y and star.colliderect(player):
                stars.remove(star)
                hit=True
                break
        
        
        for star1 in stars1[:]:
            star1.x+=Star_velocity
    
            if star1.x>WIDTH:
                stars1.remove(star1)
            
            
            elif star1.x>=player.x and star1.colliderect(player):
                stars1.remove(star1)
                hit=True
                break
        
        for StarRL in StarsRL[:]:
            StarRL.x-=Star_velocity

            if StarRL.x<=0:
                StarsRL.remove(StarRL)
            elif StarRL.x>=player.x and StarRL.colliderect(player):
                StarsRL.remove(StarRL)
                hit=True
                break


        
        if hit:
            lost_text=FONT.render("You lost!",1,"white")
            WINDOW.blit(lost_text, (WIDTH/2-lost_text.get_width()/2,HEIGHT/2-lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        #calls draw function 
        draw(player,elapsed_time,stars,stars1,StarsRL)

    pygame.quit()

# if this isnt here, it opens and closes  
if __name__=="__main__":
    main()