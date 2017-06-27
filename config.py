#Global constants for pygame applications

from drawconf import *

#Game window

RES_X = 1280
RES_Y = 960
CAPTION = 'Brick Warrior'
#CREDITS = 'by JSI'
FONT = 'arial'
FONTSIZE = 16
BIGSIZE = 32

#Menu
MENU_X = RES_X * 3 / 4
MENU_Y = 0
MENU_W = RES_X / 4
MENU_H = RES_Y
MENU_HEAD_X = MENU_X + 75
MENU_HEAD_Y = MENU_Y + 100
#MENU_COL_X = MENU_HEAD_X + 15
#MENU_COL_Y = MENU_HEAD_Y + 10
#COLSPAN = 80

#Keys

KEYTEXT = ['turn left', 'turn right', 'thrust']
IMAGE = 0

#Animation

SFPS = 1.0 / 4  #Frames per second for slowly changing views
FPS = 30        #Frames per second during driving
QPS = 1.0 / 10  #FPS after finishing the race
