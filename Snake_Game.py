import pygame ,pygame.locals ,sys,random
from tkinter import *
from tkinter.font import  Font
from csv import *
from time import *
from tkinter import messagebox
pygame.init()
window=pygame.display.set_mode((460,460))
snakedot=[]
snakedot.append({"x":10,"y":10})
snakedot.append({"x":11,"y":10})
snakedot.append({"x":12,"y":10})


def Showline():
    for i in range(20,460,20):
        pygame.draw.line(window,(0,255,0),(i,0),(i,460))
    for i in range(20,460,20):
        pygame.draw.line(window,(0,255,0),(0,i),(460,i))

def drawsnake(fruitx, fruity):

    fruit = pygame.Rect(fruitx * 20, fruity * 20, 20, 20)
    pygame.draw.rect(window, (0, 0, 255), fruit)
    for i in range(0,len(snakedot)):
        snake=pygame.Rect(snakedot[i]["x"]*20,snakedot[i]["y"]*20,20,20)
        pygame.draw.rect(window,(255,255,255),snake)

def movesnake(fruitx,fruity):
    window.fill((0,0,0))
    #Showline()
    drawsnake(fruitx,fruity)

def col(lx,score,s):
    snake_head_x = lx[0]
    if snake_head_x in lx[1:] :
        gameover(score,s)
    else:
        pass

font1 = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 20)
def start_game(fruitx,fruity,s,m):
    direction = 1

    fpsclock =pygame.time.Clock()

    while True:
        d_in = direction
        for event in pygame.event.get():
                    #d_in is used to store the previous direction before changing the direction
            if event.type == pygame.QUIT:
                return score


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 1

                elif event.key == pygame.K_RIGHT:
                    direction = -1

                elif event.key == pygame.K_UP:
                    direction = 2

                elif event.key == pygame.K_DOWN:
                    direction = -2

        if d_in==-direction:


            if direction == 1:
                snakedot.insert(0, {"x": snakedot[0]["x"], "y": snakedot[0]["y"] - 1})
                snakedot.insert(0, {"x": snakedot[0]["x"] - 1, "y": snakedot[0]["y"]})

            elif direction == -1:
                snakedot.insert(0, {"x": snakedot[0]["x"], "y": snakedot[0]["y"] + 1})
                snakedot.insert(0, {"x": snakedot[0]["x"] + 1, "y": snakedot[0]["y"]})

            elif direction == 2:
                snakedot.insert(0, {"x": snakedot[0]["x"] + 1, "y": snakedot[0]["y"]})
                snakedot.insert(0, {"x": snakedot[0]["x"], "y": snakedot[0]["y"] - 1})

            elif direction == -2:
                snakedot.insert(0, {"x": snakedot[0]["x"] - 1, "y": snakedot[0]["y"]})
                snakedot.insert(0, {"x": snakedot[0]["x"], "y": snakedot[0]["y"] + 1})

            del snakedot[-1]
            del snakedot[-1]
        else:
            if direction == 1:
                snakedot.insert(0, {"x": snakedot[0]["x"] - 1, "y": snakedot[0]["y"]})
            elif direction == -1:
                snakedot.insert(0, {"x": snakedot[0]["x"] + 1, "y": snakedot[0]["y"]})
            elif direction == 2:
                snakedot.insert(0, {"x": snakedot[0]["x"], "y": snakedot[0]["y"] - 1})
            elif direction == -2:
                snakedot.insert(0, {"x": snakedot[0]["x"], "y": snakedot[0]["y"] + 1})

            if snakedot[0]["x"] == fruitx and snakedot[0]["y"] == fruity:
                fruitx = random.randint(5, 20)
                fruity = random.randint(5, 20)
            else:
                del snakedot[-1]


        if snakedot[0]["x"] < 0 or snakedot[0]["x"] > 23 or snakedot[0]["y"]<0 or snakedot[0]["y"]>23:

            gameover(len(snakedot)-3,s)

        lx=[]
        movesnake(fruitx,fruity)
        for i in range(len(snakedot)):
            lx.append((snakedot[i]["x"],snakedot[i]["y"]))
        score = len(snakedot) - 3
        col(lx,score,s)
        if score  >m:
            m=score
        text1 = font2.render("Score : %d" % (score), True, (255,0 , 0), (0, 0, 0))
        textRect1 = text1.get_rect()
        text3 = font2.render("High Score : %d" % (m), True, (255, 255, 255), (0, 0, 0))
        textRect3 = text1.get_rect()
        textRect3.center = (350, 10)
        text2 = font2.render(s, True, (255, 255, 255), (0, 0, 0))
        textRect2 = text2.get_rect()
        textRect1.center = (390, 445)
        window.blit(text1, textRect1)
        window.blit(text2, textRect2)
        window.blit(text3, textRect3)
        pygame.display.update()
        if score<=3:
            fpsclock.tick(6)
        elif score>3 and score<=15:
            fpsclock.tick(10)
        elif  score > 15  and  score <=25:
            fpsclock.tick(13)
        else:
            fpsclock.tick(16)
def gameover(score,s):

    window2 = pygame.display.set_mode((460, 400))
    pygame.display.set_caption('Final Score')
    text = font1.render("! Game Over !", True, (255, 0, 0), (255, 255, 255))
    text2 = font1.render("Your Score : %d" % (score), True, (0, 255, 0), (255, 255, 255))
    text3 = font1.render(" Name : %s" % (s), True, (0, 0, 255), (255, 255, 255))
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect.center = (460 // 2, 250)
    textRect2.center = (460 // 2, 110)
    textRect3.center = (460 // 2, 180)
    f = open("Player.csv", "a")
    w = writer(f)
    w.writerows([[s, score, asctime()]])
    f.close()
    while True:
        window2.fill((255, 255, 255))
        window2.blit(text, textRect2)
        window2.blit(text2, textRect)
        window2.blit(text3, textRect3)
        pygame.draw.rect(window2, (0,255,0), (150, 300, 150, 50))

        texta = font1.render("Exit Game" , True, (0, 255, 0), (255, 255, 255))

        textRecta = texta.get_rect()
        textRecta.center=((180+(150/2)), (300+(50/2)))
        window2.blit(texta, textRecta)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pos() >= (150, 300):
                    if pygame.mouse.get_pos() <= (320, 350):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

root=Tk()
c1 = Canvas(root, width=20, height=400, bg='White')
c1.pack(side=RIGHT)
c1 = Canvas(root, width=10, height=400, bg='orange')
c1.pack(side=RIGHT)

c1 = Canvas(root, width=10, height=400, bg='orange')
c1.pack(side=LEFT)
c1 = Canvas(root, width=10, height=400, bg='White')
c1.pack(side=LEFT)
c1 = Canvas(root, width=10, height=400, bg='green')
c1.pack(side=LEFT)
f1 = Font(family="Time New Roman", size=12, weight="bold")
f2 = Font(family="Time New Roman", size=15, weight="bold")
f3 = Font(family="Time New Roman", size=10, weight="bold")

def gui():
    def start():
        ff = open("Player.csv", "a")
        ff.close()
        score_list=[0]
        s=ss1.get()
        if s=="":
            messagebox.showinfo("Snake Game","Please Enter Your Name .")
        else:

            f1=open("Player.csv","r")
            r=reader(f1)
            for i in r:
                try:
                    score_list.append(i[1])
                except Exception as E:
                    pass

            f1.close()
            score_list=[int(x) for x in score_list]
            m=max(score_list)
            root.destroy()
            start_game(random.randint(5, 20), random.randint(5, 20),s,m)
    def High_Score():
        f2 = Font(family="Time New Roman", size=15, weight="bold")

        score_list=[]
        f1 = open("Player.csv", "r")
        r = reader(f1)
        for i in r:
            try:
                score_list.append([i[0].capitalize(),int(i[1])])
            except Exception as E:
                pass

        f1.close()
        for i in range(len(score_list)-1):
            for j in range(len(score_list)-i-1):
                if score_list[j][1]<score_list[j+1][1]:
                    temp=score_list[j]
                    score_list[j]=score_list[j+1]
                    score_list[j + 1]=temp
        t1=Toplevel()
        t1.geometry("400x500+200+100")
        j=0
        l3 = Label(t1, text="Snake Game", fg='red', font=f2).place(x=150, y=40)
        l3 = Label(t1, text="Top Ten Scores", fg='green', font=f2).place(x=140, y=70)
        l3 = Label(t1, text="Rank", fg='blue', font=f2).place(x=60, y=110)
        l3 = Label(t1, text="Name", fg='blue', font=f2).place(x=140, y=110)
        l3 = Label(t1, text="Score", fg='skyblue', font=f2).place(x=300, y=110)
        for i in score_list[:10]:
            l3 = Label(t1, text=str(j+1)+")", fg='blue', font=f2).place(x=60, y=140 + j * 30)
            l3 = Label(t1, text=i[0], fg='blue',font=f2).place(x=140, y=140+j*30)
            l3 = Label(t1, text=str(i[1]), fg='skyblue',font=f2).place(x=300, y=140+j*30)
            j=j+1
        b2 = Button(t1, text='Quit', command=t1.destroy, width=15, height=1, bg='red', fg='white', font=f2).place(x=120,   y=450)
        t1.resizable('false','false')
        t1.mainloop()
    root.title("Snake Game")
    l3 = Label(root, text=" Welcome To Snake Game", fg='green', font=f1).place(x=60, y=40)
    l3 = Label(root, text="Enter Your Name", fg='blue', font=f1).place(x=100, y=100)
    l3 = Label(root, text="Copyright @ Kundan Kumar ", fg='skyblue',font=f3).place(x=70, y=320)
    b1 = Button(root, text='Start Game', command=start, width=20, height=1, bg='green', fg='white', font=f1).place(x=70,y=180)
    b1 = Button(root, text='High Scores', command=High_Score, width=20, height=1, bg='skyblue', fg='white', font=f1).place(x=70,y=230)
    b2 = Button(root, text='Quit', command=root.quit, width=20, height=1, bg='red', fg='white', font=f1).place(x=70, y=280)
    ss1 = StringVar()
    e1 = Entry(root, textvariable=ss1,font=f2).place(x=60, y=140)
    root.geometry("300x350+100+120")
    root.resizable('false','false')
    root.mainloop()


gui()
