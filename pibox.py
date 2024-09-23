import pygame 
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
scr_width=600
scr_height=600
win = pygame.display.set_mode((scr_width,scr_height))
pygame.display.set_caption("Pi Digits Using collisions!")
clock = pygame.time.Clock()
platform=pygame.transform.scale(pygame.image.load("white.jpg"),((600,300)))
#pygame.transform.scale(pygame.image.load("Box.png"),((50,50)))
#pygame.transform.scale(pygame.image.load("Box.png"),((100,100)))
clack=pygame.mixer.Sound("Clack.wav")
timesteps=range(100)
counter=0
digits=2
m1 = 1
m2 = 100**(digits)
v1 = 0
v2 = -10/len(timesteps)
font=pygame.font.SysFont("Roboto-Medium",48)

def Collision(x1,x2,w1,w2):
    return not (x1+w1<x2 or x1 > x2+w2)
def Bounce(m1,m2,v1,v2):
    sumM=m1+m2
    newV1=(m1 - m2) / sumM * v1
    newV1+=(2 * m2 / sumM) * v2
    return newV1
def Bounce2(m1,m2,v1,v2):
    sumM=m1+m2
    newV2=(2 * m1) / sumM * v1 + (m2 - m1) / sumM * v2
    return newV2
x1,y1 = (scr_width*0.35),(scr_height*0.517)
x2,y2 = (scr_width*0.6),(scr_height*0.434)
isquit=False
box1 = pygame.transform.scale(pygame.image.load("Box.png"),((50,50)))
box2 = pygame.transform.scale(pygame.image.load("Box.png"),((100,100)))
while not isquit:
    #Logic
            
                
    #Movement and Calculations
        for step in timesteps:
            if Collision(x1,x2,50,100):
                v1t=Bounce(m1,m2,v1,v2)
                v2t=Bounce2(m1,m2,v1,v2)
                v1=v1t
                v2=v2t
                counter+=1
                clack.play()
            elif x1<=0:
                counter+=1
                v1*=-1
                clack.play()
            x1+=v1
            x2+=v2
        win.fill((0,0,0))
        platform = pygame.draw.rect(win,(255,255,255),(0,scr_height*0.6,596,234),0)
        win.fill((0,255,255),(x2,y2,100,100))
        win.fill((0,0,255),(x1,y1,50,50))
        text=font.render("π={}.{}".format(str(counter)[:1],str(counter)[1:]),True,(0,0,0))#text=font.render(str(counter),True,(0,0,0))
        win.blit(text,(scr_width/2,scr_height*0.6))
        pygame.display.update()
        clock.tick(360)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isquit=True
pygame.quit()
quit()