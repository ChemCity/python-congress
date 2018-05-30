#!/usr/bin/python
# -*- coding: UTF-8 -*-



import pygame

from pygame.locals import *
from sys import exit #向sys模块借一个exit函数来退出程序
import sys
#指定图像文件名称
backgroud_image_filename = sys.path[0] + '\\sushiplate.jpg'
mouse_image_filename = sys.path[0] + '\\fugu.png'

#初始化pygame 为使用硬件做准备
pygame.init()

#创建一个窗口
screen = pygame.display.set_mode((640,480), 0, 32)
#screen = pygame.display.set_mode((640,480), RESIZABLE | NOFRAME, 32)
#设置窗口标题
pygame.display.set_caption("hello world")

#加载并转换图像
background = pygame.image.load(backgroud_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

#游戏主循环
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	#将背景图画上去
	screen.blit(background, (0,0))
	#获取鼠标位置
	x,y = pygame.mouse.get_pos()
	#计算光标位置
	x -= mouse_cursor.get_width() / 2
	y -= mouse_cursor.get_height() / 2
	#把光标画上去
	screen.blit(mouse_cursor, (x,y))
	
	#刷新画面
	pygame.display.update()

'''
convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件
（事实上因为 它太常用了，如果你不写pygame也会帮你做）；convert_alpha相比convert，
保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的
形状。

游戏的主循环是一个无限循环，直到用户跳出。在这个主循环里做的事情就是不停地画背景
和更新光标位置，虽然背景是不动的，我们还是需要每次都画它， 否则鼠标覆盖过的位置
就不能恢复正常了。

blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定
记得用update更新一下，否则画面一片漆黑。
'''





