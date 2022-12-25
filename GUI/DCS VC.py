import sys
import pygame
import button_push as bp
import colour as cl
import time

pygame.init()

#創建窗口
screen_width= 900
screen_height= 650
screen = pygame.display.set_mode((screen_width,screen_height))
screen_rect=screen.get_rect()
pygame.display.set_caption("VC_DCS")

#分數
score = 0
score_font=pygame.font.SysFont("Arial",200)

play= False

#定義變量----遊戲菜單
menu_state = 'main'
#定義變量----問題
Question = False

#字體
font =pygame.font.SysFont("Arial",45)

#Model
DCS1_img =pygame.image.load('images/DCS1.png')
DCS2_img =pygame.image.load('images/DCS2.png')
DCS3_img =pygame.image.load('images/DCS3.png')

#問題圖像
question1_img =pygame.image.load('images/question1.png')
question2_img =pygame.image.load('images/question2.png')
question3_img =pygame.image.load('images/question3.png')
question4_img =pygame.image.load('images/question4.png')
question5_img =pygame.image.load('images/question5.png')
question6_img =pygame.image.load('images/question6.png')
#question7_img =pygame.image.load('images/question7.png')(cancel)
question8_img =pygame.image.load('images/question8.png')
question9_img =pygame.image.load('images/question9.png')
question10_img =pygame.image.load('images/question10.png')
question11_img =pygame.image.load('images/question11.png')
question12_img =pygame.image.load('images/question12.png')
question13_img =pygame.image.load('images/question13.png')

#答案圖像
solution1_img =pygame.image.load('images/solution1.png')
solution2_img =pygame.image.load('images/solution2.png')
solution3_img =pygame.image.load('images/solution3.png')
solution4_img =pygame.image.load('images/solution4.png')
solution5_img =pygame.image.load('images/solution5.png')
solution6_img =pygame.image.load('images/solution6.png')
solution8_img =pygame.image.load('images/solution8.png')
solution9_img =pygame.image.load('images/solution9.png')
solution10_img =pygame.image.load('images/solution10.png')
solution11_img =pygame.image.load('images/solution12.png')
solution12_img =pygame.image.load('images/solution11.png')
solution13_img =pygame.image.load('images/solution13.png')

#true or not圖像
answer= 1
True_img= font.render(" GoodJob! The answer is correct! ",True,cl.Dark_Forest)
False_img= font.render(" OH! The answer is wrong. Keep going! ",True,cl.Carnelian)
next_img= font.render(" Next ",True,cl.white)
menu_img =pygame.image.load('images/menu.png')
end_img =pygame.image.load('images/end.png')

#菜單圖像
start_img= font.render(" START ",True,cl.white)
model_img= font.render(" MODEL ",True,cl.white)
explain_img= font.render(" EXPLAIN ",True,cl.white)
starting_img= font.render(" gaming ....",True,cl.white)
explaining_img= font.render(" explaining.....",True,cl.black)
starting_img=font.render(" question1 ",True,cl.black)
back_img=font.render(' BACK ',True,cl.white)
close_img=font.render(' Close ',True,cl.white)
play_img=font.render(' Play ',True,cl.white)

#答題圖像
A_img= font.render(" A ",True,cl.white)
B_img= font.render(" B ",True,cl.white)
C_img= font.render(" C ",True,cl.white)
D_img= font.render(" D ",True,cl.white)
E_img= font.render(" E ",True,cl.white)


#菜單按鈕
start_button= bp.Button(40,200,start_img,1)
model_button= bp.Button(40,420,model_img,1)
#explain_button= bp.Button(40,500,explain_img,1)
close_button= bp.Button(10,550,close_img,1)
play_button= bp.Button(10,550,play_img,1)

#答題按鈕
A_button = bp.Button(50,500,A_img,2)
B_button = bp.Button(210,500,B_img,2)
C_button = bp.Button(370,500,C_img,2)
D_button = bp.Button(530,500,D_img,2)
E_button = bp.Button(690,500,E_img,2)


#菜單按鈕
back_button=bp.Button(750,550,back_img,1)
next_button = bp.Button(780,550,next_img,1)


    

#窗口顯示
run=True
while run:
    screen.fill(cl.white)

    #動作
    for event in pygame.event.get():
        #退出
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            quit()
    #分數
    score_surface=score_font.render(str(score),True,cl.black)
    
    #菜單狀態
    if menu_state== 'main':
        screen.blit(menu_img,(0,0))
        if start_button.draw(screen):
            menu_state="question1"
        if model_button.draw(screen):
            menu_state="model"


    
    #模型
    elif menu_state=="model":
        screen.blit(DCS2_img,(0,0))
        if back_button.draw(screen):
            menu_state="main"

    #question1
    elif menu_state=="question1":
        screen.blit(question1_img,(0,0))
        if B_button.B_draw(screen) or C_button.C_draw(screen) or D_button.D_draw(screen):
            answer = 1
            menu_state="solution1"
        elif A_button.A_draw(screen):
            answer =0
            menu_state="solution1"
            score=score+1

    #question2        
    elif menu_state=="question2":
        screen.blit(question2_img,(0,0))
        if A_button.A_draw(screen) or B_button.B_draw(screen) or D_button.D_draw(screen):
            menu_state="solution2"
            answer = 1
        elif C_button.C_draw(screen):
            menu_state="solution2"
            answer=0
            score=score+1

    #question3        
    elif menu_state=="question3":
        screen.blit(question3_img,(0,0))
        if A_button.A_draw(screen):
            menu_state="solution3"
            answer = 1
        elif B_button.B_draw(screen):
            menu_state="solution3"
            answer =0
            score=score+1

    #question4       
    elif menu_state=="question4":
        screen.blit(question4_img,(0,0))
        if A_button.A_draw(screen):
            menu_state="solution4"
            answer = 1
        elif B_button.B_draw(screen):
            menu_state="solution4"
            answer = 0
            score=score+1

    #question5     
    elif menu_state=="question5":
        screen.blit(question5_img,(0,0))
        if C_button.C_draw(screen) or B_button.B_draw(screen) or D_button.D_draw(screen):
            menu_state="solution5"
            answer = 1
        elif A_button.A_draw(screen):
            menu_state="solution5"
            answer = 0
            score=score+1


    #question6  
    elif menu_state=="question6":
        screen.blit(question6_img,(0,0))
        if A_button.A_draw(screen) or C_button.C_draw(screen) or B_button.B_draw(screen) or D_button.D_draw(screen):
            menu_state="solution6"
            answer = 1
        elif E_button.E_draw(screen):
            menu_state="solution6"
            answer = 0
            score=score+1


    #question7  (cancel)
    #elif menu_state=="question7":
    #    screen.blit(question7_img,(0,0))
    #    if A_button.A_draw(screen) or B_button.B_draw(screen) or D_button.D_draw(screen):
    #        menu_state="solution7"
    #        answer = 1
    #    elif C_button.C_draw(screen):
    #        menu_state="solution7"
    #        answer = 0
    
    #question8
    elif menu_state=="question8":
        screen.blit(question8_img,(0,0))
        if A_button.A_draw(screen) or C_button.C_draw(screen) or B_button.B_draw(screen) or D_button.D_draw(screen):
            menu_state="solution8"
            answer = 1
        elif E_button.E_draw(screen):
            menu_state="solution8"
            answer = 0
            score=score+1

    #question9
    elif menu_state=="question9":
        screen.blit(question9_img,(0,0))
        if A_button.A_draw(screen) or C_button.C_draw(screen) or E_button.E_draw(screen) or D_button.D_draw(screen):
            menu_state="solution9"
            answer = 1
        elif B_button.B_draw(screen):
            menu_state="solution9"
            answer = 0
            score=score+1

    #question10
    elif menu_state=="question10":
        screen.blit(question10_img,(0,0))
        if A_button.A_draw(screen) or C_button.C_draw(screen) or B_button.B_draw(screen) or D_button.D_draw(screen):
            menu_state="solution10"
            answer = 1
        elif E_button.E_draw(screen):
            menu_state="solution10"
            answer = 0
            score=score+1
                
    #question11
    elif menu_state=="question11":
        screen.blit(question11_img,(0,0))
        if C_button.C_draw(screen) or B_button.B_draw(screen) or D_button.D_draw(screen):
            menu_state="solution11"
            answer = 1
        elif A_button.A_draw(screen):
            menu_state="solution11"
            answer = 0
            score=score+1
        
    #question12
    elif menu_state=="question12":
        screen.blit(question12_img,(0,0))
        if A_button.A_draw(screen) or C_button.C_draw(screen)or D_button.D_draw(screen):
            menu_state="solution12"
            answer = 1
        elif B_button.B_draw(screen):
            menu_state="solution12"
            answer = 0
            score=score+1
            
    #question13
    elif menu_state=="question13":
        screen.blit(question13_img,(0,0))
        if A_button.A_draw(screen) or C_button.C_draw(screen):
            menu_state="solution13"
            answer = 1
        elif B_button.B_draw(screen):
            menu_state="solution13"
            answer = 0
            score=score+1

     #solution1
    elif menu_state=="solution1":
        screen.blit(solution1_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question2"

    #solution2
    elif menu_state=="solution2":
        screen.blit(solution2_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question3"

    #solution3 
    elif menu_state=="solution3":
        screen.blit(solution3_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question4"
    
    #solution4
    elif menu_state=="solution4":
        screen.blit(solution4_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question5"

    #solution5
    elif menu_state=="solution5":
        screen.blit(solution5_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question6"

    #solution6 
    elif menu_state=="solution6":
        screen.blit(solution6_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question8"

    #solution7 (cancel)
    #elif menu_state=="solution7":
    #    screen.blit(solution3_img,(0,0))
    #    if answer== 1:
    #        score = score+1
    #        screen.blit(True_img,(20,0))
    #    if answer==0:
    #        screen.blit(False_img,(20,0))
    #    if next_button.draw(screen):
    #        menu_state="question8"

    #solution8 
    elif menu_state=="solution8":
        screen.blit(solution8_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question9"          

    #solution9
    elif menu_state=="solution9":
        screen.blit(solution9_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question10"  

    #solution10 
    elif menu_state=="solution10":
        screen.blit(solution10_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question11"

    #solution11 
    elif menu_state=="solution11":
        screen.blit(solution11_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question12"
    
    #solution12 
    elif menu_state=="solution12":
        screen.blit(solution12_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="question13"

    #solution13 
    elif menu_state=="solution13":
        screen.blit(solution13_img,(0,0))
        if answer== 0:
            screen.blit(True_img,(20,0))
        if answer==1:
            screen.blit(False_img,(20,0))
        if next_button.draw(screen):
            menu_state="End"
     #End
    elif menu_state=="End":
        screen.blit(end_img,(0,0))
        screen.blit(score_surface,(500,200))
        if close_button.B_draw(screen):
            run=False
            pygame.quit()



    pygame.display.update()
