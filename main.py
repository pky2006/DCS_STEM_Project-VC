import pygame
import sys
import json
import os

with open("Question Bank.json") as file:
	ques=json.load(file,strict=False)

level_1=ques["lv_1"]
level_2=ques["lv_2"]
level_3=ques["lv_3"]

print(level_1,"\n",level_2,"\n",level_3)


pygame.init()
pygame.display.set_caption('DCS Q&A Game')
screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
f = pygame.font.Font('Font/YaHei.ttc',50)


while True:
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
 
    pygame.display.flip() #更新屏幕内容