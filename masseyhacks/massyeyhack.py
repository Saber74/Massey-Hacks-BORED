from pygame import *
from tkinter import *
import random
import requests
import geocoder
import json
import requests
import geocoder
mixer.init()
mixer.music.load("Elevator Music - So Chill.mp3")
positionList=[]
openList=[]
ratingList=[]
fontsize = 40
piclength = 0
size=(1000,800)
namesList=[]
font.init()
level=0
arial = font.SysFont('Arial',60)
codeFont = font.Font('CODE Light.otf',10)
mainFont = font.Font("Paper.otf",60)
rot = 0
xPos = 0
yPos = 0
typing = False
zipcode = ""
zcode = []
clockity = time.Clock()
vX, vY = 1, 1
screen = display.set_mode(size) 
starterRect=Rect(350,150,650,300)
r = requests.post("http://bugs.python.org",data={'number': 12524, 'type': 'issue', 'action': 'show'})
logo=image.load("game_logo.png")
yes=image.load("yes_notclicked.png")
yes_clicked=image.load("yes_clicked.png")
no=image.load("no_notclicked.png")
no_clicked=image.load("no_clicked.png")
amusementicon=image.load("logo_amusement.png")
foodicon=image.load("logo_food.png")
moviesicon=image.load("logo_movies.png")
resultbox = image.load("resultbox.png")

screen.fill((210,219,254))
screen.blit(logo,(0,0))
display.flip()

yesRect=Rect(100,300,300,100)
noRect=Rect(600,300,300,100)
amusementRect=Rect(100,400,170,170)
foodRect=Rect(415,400,170,170)
moviesRect=Rect(730,400,170,170)

running = True
repeat=True
gstatus=False
option="null"
decision=""

def geoget(city):
    try:

        r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})


        g = geocoder.google(city)

        r=requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(g.latlng[0])+","+str(g.latlng[1])+"&radius=15000&type=restaurant&keyword=cruise&key=AIzaSyAPRWyPRnzouTelozhPcH-DXhFwVTkEFJE")
        p=requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(g.latlng[0])+","+str(g.latlng[1])+"&radius=15000&type=theatres&keyword=cruise&key=AIzaSyAPRWyPRnzouTelozhPcH-DXhFwVTkEFJE")
        q=requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(g.latlng[0])+","+str(g.latlng[1])+"&radius=15000&type=activities&keyword=cruise&key=AIzaSyAPRWyPRnzouTelozhPcH-DXhFwVTkEFJE")

        open("test.json", 'w').write(q.text)
        open("test.json2",'w').write(p.text)
        open("test.json3",'w').write(r.text)
    except:
        text=str("Try Again")
        myFont=font.Font("Paper.otf",100)
        info=myFont.render(text,True,(0,0,200))
        display.update()
        pass
while running:
    for evt in event.get():  
        if evt.type == QUIT: 
            running = False
        if evt.type == KEYDOWN:
            if typing == True:
                if evt.key!=K_BACKSPACE:
                    zcode.append(evt.unicode)
                if evt.key == K_BACKSPACE:
                    if typing == True and fontsize<40:
                        testFont = font.Font('CODE Light.otf',fontsize+5)
                        zippic = testFont.render(zipcode[:-1],True,(0,0,0))
                        if zippic.get_width()<780:
                            fontsize+=5
                    if len(zcode)>0:
                        del zcode[-1]
                if evt.key == K_RETURN:
                    level = 4
                    fontsize = 40
                    codeFont = font.Font('CODE Light.otf',fontsize)
                zipcode=''.join(zcode)
                zipcode2=zipcode.upper()
   
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if mb[0] :
        if starterRect.collidepoint((mx,my)) and level == 0: 
            level+=1
    if level==1:
        screen.fill((210,219,254))
        screen.blit(yes,(100,300))
        screen.blit(no,(600,300))
        myFont=font.Font("Paper.otf",160)
        text=str("Are you bored?")
        info=myFont.render(text,True,(0,0,200))
        screen.blit(info,(100,70))
        if yesRect.collidepoint((mx,my)):
            screen.blit(yes_clicked,(100,300))
            if mb[0]:
                level+=1
                option="yes"
        elif noRect.collidepoint((mx,my)):
            screen.blit(no_clicked,(600,300))
            if mb[0]:
                level+=1
                option="no"

    elif  level==2:
        if option=="yes":
            level+=1
            mixer.music.play(-1)
        elif option=="no":
            screen.fill((0,0,0))
            if xPos <= 0 or xPos>=800:
                vX = -vX+random.randint(-1,1)
            if yPos<=0 or yPos>=600:
                vY = -vY+random.randint(-1,1)
            xPos+=vX
            yPos+=vY
            screen.blit(transform.rotate(arial.render("really..boi?",True,(255,255,255)),int(rot)),(int(xPos), int(yPos)))
            display.flip()
            rot = rot%360+1
            clockity.tick(120)
            if mb[1]:
                level-=1
    elif level==3:
        screen.fill((210,219,254))
        exFont = font.Font('CODE Light.otf',30)
        tFont=font.Font("Paper.otf",90)
        title=tFont.render("Enter Name of City: ",True,(0,0,200))
        example=exFont.render("Ex: Windsor, ON", True, (0,0,0))
        screen.blit(example,(150,340))
        screen.blit(title,(225,200))
        textboxRect=Rect(100,375,800,50)
        draw.rect(screen, (255,255,255), textboxRect)
        draw.rect(screen, (169,190,225), textboxRect, 3)
        
        if mb[0]:
            if textboxRect.collidepoint((mx,my)):
                typing = True
            else:
                typing = False
        
        if typing == True:
            draw.rect(screen, (105,135,200), textboxRect, 3)
        
        codeFont = font.Font('CODE Light.otf',fontsize)
        zippic = codeFont.render(zipcode,True,(0,0,0))
        piclength = zippic.get_width()
        if piclength>=780:
            fontsize -=5
        screen.blit(zippic,(110,385))
        display.update()
    elif level == 4:
        screen.fill((210,219,254))
        title=tFont.render("Choose an option:",True,(0,0,200))
        screen.blit(title,(225,200))
        screen.blit(amusementicon,(100,400))
        screen.blit(foodicon,(415,400))
        screen.blit(moviesicon,(730,400))

        if mb[0]:
            if amusementRect.collidepoint((mx,my)):
                decision="amusement"
                level+=1
            elif foodRect.collidepoint((mx,my)):
                decision="food"
                level+=1
            elif moviesRect.collidepoint((mx,my)):
                decision="movies"
                level+=1
    elif level == 5:
        screen.fill((210,219,254))
        title=tFont.render("Places Near You",True,(0,0,200))
        screen.blit(title,(225,50))
        codeFont = font.Font('CODE Light.otf',40)
        codeFont2 = font.Font('CODE Light.otf',20)
        if gstatus == False:
            geoget(zipcode2)
            gstatus = True
        if decision=="amusement":
            data=json.load(open("test.json"))
            for result in data["results"]:
                if len(namesList)<=3:
                    namesList.append(result["name"])
##                if len(ratingList)<=3:
##                    ratingList.append(result["rating"])
                if len(positionList)<=3:
                    positionList.append(result["vicinity"])
        elif decision=="food":
            data=json.load(open("test.json3"))
            for result in data["results"]:
                if len(namesList)<=3:
                    namesList.append(result["name"])
##                if len(ratingList)<=3:
##                    ratingList.append(result["rating"])
                if len(positionList)<=3:
                    positionList.append(result["vicinity"])
        elif decision=="movies":
            data=json.load(open("test.json2"))
            for result in data["results"]:
                if len(namesList)<=3:
                    namesList.append(result["name"])
##                if len(ratingList)<=3:
##                    ratingList.append(result["rating"])
                if len(positionList)<=3:
                    positionList.append(result["vicinity"])
        for i in range(4):
            draw.rect(screen, (255,255,255), (100,175+150*i,800,100))
            draw.rect(screen, (169,190,225), (100,175+150*i,800,100), 3)
            name = codeFont.render(namesList[i],True,(0,0,0))
            screen.blit(name,(110,185+150*i))
            address = codeFont2.render(positionList[i],True,(0,0,0))
            screen.blit(address,(110,235+150*i))
            

    display.update()
quit()
        
       
        
  

        
