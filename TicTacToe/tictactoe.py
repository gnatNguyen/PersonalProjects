import pygame as pg
from pygame.locals import *
import random
import time

SCREEN_WIDTH = 600

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

pg.display.set_caption("tic tac toe")
a = pg.image.load('tictactoe.png')
pg.display.set_icon(a)

rect_size = 60

grid = [[None,None,None],
		[None,None,None],
		[None,None,None]]

x_turn = True
o_turn = False

screen.fill((30, 30, 30))

def main():
	global screen

	running = True
	turn = 0
	pos = pg.mouse.get_pos()

	while running:
		for event in pg.event.get():
		    if event.type == QUIT:
		      running = False
		    if event.type == pg.KEYDOWN:
		    	if event.key == pg.K_DOWN:
		    		running = False

		    if event.type == pg.MOUSEBUTTONDOWN:
		    	pos = pg.mouse.get_pos()
		    	x_pos = pos[0]
		    	y_pos = pos[1]
		    	boxClicked(x_pos, y_pos)

		drawBoard()
		pg.display.flip()

		x_win, o_win = checkWinConditions()
		if x_win:
			running = False
			winningText("X PLAYER WINS!")
			time.sleep(3)
		elif o_win:
			running = False
			winningText("O PLAYER WINS")
			time.sleep(3)

def winningText(text):
	global screen
	font = pg.font.Font('freesansbold.ttf',40)
	message = font.render(text, False, (255, 0, 0))
	screen.blit(message,(150,10))
	pg.display.update()

def drawBoard():
	global screen
	pg.draw.rect(screen, (255,255,255), (255, 150, 10, 300))
	pg.draw.rect(screen, (255,255,255), (365, 150, 10, 300))

	pg.draw.rect(screen, (255,255,255), (160, 235, 300, 10))
	pg.draw.rect(screen, (255,255,255), (160, 345, 300, 10))

def checkWinConditions():
	x_win = False
	o_win = False
	if None not in grid[0]:
		if "o" not in grid[0]:
			x_win = True
		if "x" not in grid[0]:
			o_win = True

	elif None not in grid[1]:
		if "o" not in grid[1]:
			x_win = True
		if "x" not in grid[1]:
			o_win = True
	elif None not in grid[2]:
		if "o" not in grid[2]:
			x_win = True
		if "x" not in grid[2]:
			o_win = True

	if "x" == grid[0][0] and "x" == grid[1][1] and "x" == grid[2][2]:
		x_win = True
	elif "x" == grid[0][2] and "x" == grid[1][1] and "x" == grid[2][0]:
		x_win = True
	elif "x" == grid[0][0] and "x" == grid[1][0] and "x" == grid[2][0]:
		x_win = True
	elif "x" == grid[0][1] and "x" == grid[1][1] and "x" == grid[2][1]:
		x_win = True
	elif "x" == grid[0][2] and "x" == grid[1][2] and "x" == grid[2][2]:
		x_win = True
	elif "o" == grid[0][0] and "o" == grid[1][1] and "o" == grid[2][2]:
		o_win = True
	elif "o" == grid[0][2] and "o" == grid[1][1] and "o" == grid[2][0]:
		o_win = True
	elif "o" == grid[0][0] and "o" == grid[1][0] and "o" == grid[2][0]:
		o_win = True
	elif "o" == grid[0][1] and "o" == grid[1][1] and "o" == grid[2][1]:
		o_win = True
	elif "o" == grid[0][2] and "o" == grid[1][2] and "o" == grid[2][2]:
		o_win = True
	return x_win, o_win

def boxClicked(x_pos, y_pos):
	global x_turn, o_turn
	
	if x_pos >= 180 and x_pos <= 180+rect_size:
		if y_pos >= 160 and y_pos <= 160+rect_size:
			if grid[0][0] == None:
				if x_turn:
					grid[0][0] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (180,160), (230,210), 3)
					pg.draw.line(screen, (255,255,255), (230,160), (180,210), 3)
					
				elif o_turn:
					grid[0][0] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (210, 190), 25, 2)
			
	if x_pos >= 285 and x_pos <= 285+rect_size:
		if y_pos >= 160 and y_pos <= 160+rect_size:
			if grid[0][1] == None:
				if x_turn:
					grid[0][1] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (285,160), (335,210), 3)
					pg.draw.line(screen, (255,255,255), (335,160), (285,210), 3)
				elif o_turn:
					grid[0][1] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (315, 190), 25, 2)
			
	if x_pos >= 390 and x_pos <= 390+rect_size:
		if y_pos >= 160 and y_pos <= 160+rect_size:
			if grid[0][2] == None:
				if x_turn:
					grid[0][2] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (390,160), (440,210), 3)
					pg.draw.line(screen, (255,255,255), (440,160), (390,210), 3)
				elif o_turn:
					grid[0][2] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (420, 190), 25, 2)
			
	if x_pos >= 180 and x_pos <= 180+rect_size:
		if y_pos >= 265 and y_pos <= 265+rect_size:
			if grid[1][0] == None:
				if x_turn:
					grid[1][0] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (180,265), (230,315), 3)
					pg.draw.line(screen, (255,255,255), (230,265), (180,315), 3)
				elif o_turn:
					grid[1][0] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (210, 295), 25, 2)
			
	if x_pos >= 285 and x_pos <= 285+rect_size:
		if y_pos >= 265 and y_pos <= 265+rect_size:
			if grid[1][1] == None:
				if x_turn:
					grid[1][1] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (285,265), (335,315), 3)
					pg.draw.line(screen, (255,255,255), (335,265), (285,315), 3)
				elif o_turn:
					grid[1][1] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (315, 295), 25, 2)
			
	if x_pos >= 390 and x_pos <= 390+rect_size:
		if y_pos >= 265 and y_pos <= 265+rect_size:
			if grid[1][2] == None:
				if x_turn:
					grid[1][2] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (390,265), (440,315), 3)
					pg.draw.line(screen, (255,255,255), (440,265), (390,315), 3)
				elif o_turn:
					grid[1][2] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (420, 295), 25, 2)
			
	if x_pos >= 180 and x_pos <= 180+rect_size:
		if y_pos >= 370 and y_pos <= 370+rect_size:
			if grid[2][0] == None:
				if x_turn:
					grid[2][0] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (180,370), (230,420), 3)
					pg.draw.line(screen, (255,255,255), (230,370), (180,420), 3)
				elif o_turn:
					grid[2][0] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (210, 400), 25, 2)
			
	if x_pos >= 285 and x_pos <= 285+rect_size:
		if y_pos >= 370 and y_pos <= 370+rect_size:
			if grid[2][1] == None:
				if x_turn:
					grid[2][1] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (285,370), (335,420), 3)
					pg.draw.line(screen, (255,255,255), (335,370), (285,420), 3)
				elif o_turn:
					grid[2][1] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (315, 400), 25, 2)
			
	if x_pos >= 390 and x_pos <= 390+rect_size:
		if y_pos >= 370 and y_pos <= 370+rect_size:
			if grid[2][2] == None:
				if x_turn:
					grid[2][2] = "x"
					x_turn = False
					o_turn = True
					pg.draw.line(screen, (255,255,255), (390,370), (440,420), 3)
					pg.draw.line(screen, (255,255,255), (440,370), (390,420), 3)
				elif o_turn:
					grid[2][2] = "o"
					x_turn = True
					o_turn = False
					pg.draw.circle(screen, (255,255,255), (420, 400), 25, 2)
			
main()
pg.quit()