import pygame
import sys
import json
import os
from pygame.locals import *
import time

score = 0
correct = 0
wrong = 0
history =[]

with open("Question Bank.json",encoding='utf-8') as file:
	ques=json.load(file,strict=False)

level_1=ques["lv_1"]
level_2=ques["lv_2"]
level_3=ques["lv_3"]

pygame.init()
pygame.display.set_caption('DCS Q&A Game')
screen = pygame.display.set_mode((700,700))
f = pygame.font.Font('Font/YaHei.ttc',20)
screen.fill("white")



def print_text(x,y,text,color=(0,0,0),shadow=False,font=f,surface=screen):
    if shadow == True:
        imgText = font.render(text,True,(0,0,0))
        screen.blit(imgText,(x-2,y-2))
    # imgText = font.render(text,True,color)
    # screen.blit(imgText,(x,y))
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    pos=(x,y)
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
            	x = pos[0]  # Reset the x.
            	y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y = y + word_height  # Start on new row.

# for i in range(0,4):
# 	print_text(0+20,50,str(level_1[i]['Question']),"black")
# 	print(level_1[i]['Question'])
# 	pygame.time.wait(100)
#print_text(0,50,str(level_1[0]['Question']),"black")

print_text(50,50,"A. Cities experience much warmer temperatures than nearby rural areas.B. Rural areas are warmer than nearby cities to affect these cities’ temperature.C. Both cities and rural areas are very hot.D. There is lots of pollution in the city.")












while True:
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.flip() #更新屏幕内容




# ---
# class game(object):
# 	def __init__(self,filename):
# 		self.score = 0
# 		self.correct = 0
# 		self.wrong = 0
# 		self.history = []
	
# 	def show_question(self,question_type):
# 		print_text(210,5,"Q&A Game")
# 		print_text(190,500-20,"Press Keys (1-4) to answer", "red")
# 		print_text(530,5,"Score")
# 		print_text(550,25,str(self.score),red)

# 		print_text(5,80,"Question ",str(len(question_type)))

# def print_text(font,x,y,text,color=(255,255,255),shadow=True):
#     if shadow:
#         imgText = font.render(text,True,(0,0,0))
#         screen.blit(imgText,(x-2,y-2))
#     imgText = font.render(text,True,color)
#     screen.blit(imgText,(x,y))

# pygame.init()
# screen = pygame.display.set_mode((600,500))
# pygame.display.set_caption("DCS Q&A Game @ Valtorta College")
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == KEYUP:
#             if event.key == pygame.K_ESCAPE:
#                 pygame.quit()
#                 sys.exit()
#             elif event.key == pygame.K_1:
#                 game.handle_input(1)
#             elif event.key == pygame.K_2:
#                 game.handle_input(2)
#             elif event.key == pygame.K_3:
#                 game.handle_input(3)
#             elif event.key == pygame.K_4:
#                 game.handle_input(4)
#             elif event.key == pygame.K_RETURN:
#                 game.next_question()

#     screen.fill((0,0,200))
#     game.show_question(level_1)
#     pygame.display.update()