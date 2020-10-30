# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#import numba
import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np
from utils import *
from pygame import*
import sys
init()
#===================================================================
#Pintado de personajes
#===================================================================
def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)
	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	pygame.display.flip()
	glFlush()
def PintarUnidad1(x, y,caso,repos, size):
	Puntos_Soldado1 = [
									 (-4, 9),(-3, 9),(-2, 9),(-1, 9),(0, 9),(1, 9),(2, 9),(3, 9),
			   			  (-5, 8),(-4, 8),(3, 8),(-2, 8),(-1, 8),(0, 8),(1, 8),(2, 8),(3, 8),(4, 8),
			   (-6, 7),(-5, 7),(-4, 7),(-3, 7),(-2, 7),(-1, 7),(0, 7),(1, 7),(2, 7),(3, 7),(4, 7),(5, 7),
			   (-6, 6),(-5, 6),(-4, 6),(-3, 6),(-2, 6),(-1, 6),(0, 6),(1, 6),(2, 6),(3, 6),(4, 6),(5, 6),
			   (-6, 5),(-5, 5),(-4, 5),(-3, 5),(-2, 5),(-1, 5),(0, 5),(1, 5),(2, 5),(3, 5),(4, 5),(5, 5),
			   (-6, 4),(-5, 4),(-4, 4),(-3, 4),(-2, 4),(-1, 4),(0, 4),(1, 4),(2, 4),(3, 4),(4, 4),(5, 4),
	(-7, 3),(-6, 3),(-5, 3),(-4, 3),(-3, 3),(-2, 3),(-1, 3),(0, 3),(1, 3),(2, 3),(3, 3),(4, 3),(5, 3),(6, 3),
	(-7, 2),(-6, 2),(-5, 2),(-4, 2),(-3, 2),(-2, 2),(-1, 2),(0, 2),(1, 2),(2, 2),(3, 2),(4, 2),(5, 2),(6, 2),
			   (-6, 1),(-5, 1),(-4, 1),(-3, 1),(-2, 1),(-1, 1),(0, 1),(1, 1),(2, 1),(3, 1),(4, 1),(5, 1),
			   (-6, 0),(-5, 0),(-4, 0),(-3, 0),(-2, 0),(-1, 0),(0, 0),(1, 0),(2, 0),(3, 0),(4, 0),(5, 0),
	(-7,-1),(-6, -1),(-5, -1),(-4, -1),(-3, -1),(-2, -1),(-1, -1),(0, -1),(1, -1),(2, -1),(3, -1),(4, -1),(5, -1),(6, -1),
	(-7,-2),(-6, -2),(-5, -2),(-4, -2),(-3, -2),(-2, -2),(-1, -2),(0, -2),(1, -2),(2, -2),(3, -2),(4, -2),(5, -2),(6, -2),
			   (-6, -3),(-5, -3),(-4, -3),(-3, -3),(-2, -3),(-1, -3),(0, -3),(1, -3),(2, -3),(3, -3),(4, -3),(5, -3),
			   			  (-5, -4),(-4, -4),(-3, -4),(-2, -4),(-1, -4),(0, -4),(1, -4),(2, -4),(3, -4),(4, -4),
			   			  (-5, -5),(-4, -5),(-3, -5),(-2, -5),(-1, -5),(0, -5),(1, -5),(2, -5),(3, -5),(4, -5),
			   			  			 (-4, -6),(-3, -6),(-2, -6),					    (1, -6),(2, -6),(3, -6)
	]
	if(repos):
		negro = (107/255,142/255,35/255)
		verde = (107/255,142/255,35/255)
		crema = (107/255,142/255,35/255)
		blanc = (107/255,142/255,35/255)
		plomo = (107/255,142/255,35/255)
	else:
		negro = (0.0,0.0,0)
		verde = (0,0.25,0)
		crema = (1,0.89,0.75)
		blanc = (255,255,255)
		plomo = (139,69,19)

	Colores_Soldado1 = [
							negro, 	negro,	negro,	negro,	negro,	negro, 	negro,	negro,
					negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	negro,	verde,	blanc,	blanc,	blanc,	blanc,	verde,	negro,	negro,	negro,
			negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,
	negro,	crema,	negro,	negro,	crema,	crema,	crema,	crema,	crema,	crema,	negro,	negro,	crema,	negro,
	negro,	crema,	crema,	crema,	crema,	negro,	crema,	crema,	negro,	crema,	crema,	crema,	crema,	negro,
			negro,	negro,	crema,	crema,	plomo,	crema,	crema,	plomo,	crema,	crema,	negro,	negro,
			negro,	negro,	negro,	crema,	crema,	negro,	negro,	crema,	crema,	negro,	negro,	negro,
	negro,	crema,	crema,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	crema,	crema,	negro,
	negro,	crema,	crema,	negro,	verde,	negro,	verde,	verde,	negro,	verde,	negro,	crema,	crema,	negro,
			negro,	negro,	negro,	verde,	negro,	negro,	verde,	verde,	negro,	negro,	negro,	negro,	
					negro,	verde,	negro,	negro,	verde,	verde,	negro,	negro,	verde,	negro,
					negro,	verde,	verde,	verde,	negro,	negro,	verde,	negro,	verde,	negro,
							negro,	negro,	negro,					negro,	negro,	negro,

	]
	if(caso==0):	
		for i in range(184):
			xf = (x+Puntos_Soldado1[i][0])*size
			yf = (y+Puntos_Soldado1[i][1])*size
			R = Colores_Soldado1[i][0]
			G = Colores_Soldado1[i][1]
			B = Colores_Soldado1[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==1):
		for i in range(184):
			xf = (x-Puntos_Soldado1[i][0]+3)*size
			yf = (y-Puntos_Soldado1[i][1]+3)*size
			R = Colores_Soldado1[i][0]
			G = Colores_Soldado1[i][1]
			B = Colores_Soldado1[i][2]
			set_pixel(xf,yf,R,G,B,size)			
	elif(caso==2):
		for i in range(184):
			yf = (y+Puntos_Soldado1[i][0]+1)*size
			xf = (x+Puntos_Soldado1[i][1]+1)*size
			R = Colores_Soldado1[i][0]
			G = Colores_Soldado1[i][1]
			B = Colores_Soldado1[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==3):
		for i in range(184):
			yf = (y-Puntos_Soldado1[i][0])*size
			xf = (x-Puntos_Soldado1[i][1])*size
			R = Colores_Soldado1[i][0]
			G = Colores_Soldado1[i][1]
			B = Colores_Soldado1[i][2]
			set_pixel(xf,yf,R,G,B,size)
	return
def PintarUnidad2(x, y,caso,repos, size):
	Puntos_Soldado2 = [
									 (x-4, y+9),(x-3, y+9),(x-2, y+9),(x-1, y+9),(x+0, y+9),(x+1, y+9),(x+2, y+9),(x+3, y+9),
			   			  (x-5, y+8),(x-4, y+8),(x-3, y+8),(x-2, y+8),(x-1, y+8),(x+0, y+8),(x+1, y+8),(x+2, y+8),(x+3, y+8),(x+4, y+8),
			   (x-6, y+7),(x-5, y+7),(x-4, y+7),(x-3, y+7),(x-2, y+7),(x-1, y+7),(x+0, y+7),(x+1, y+7),(x+2, y+7),(x+3, y+7),(x+4, y+7),(x+5, y+7),
			   (x-6, y+6),(x-5, y+6),(x-4, y+6),(x-3, y+6),(x-2, y+6),(x-1, y+6),(x+0, y+6),(x+1, y+6),(x+2, y+6),(x+3, y+6),(x+4, y+6),(x+5, y+6),
			   (x-6, y+5),(x-5, y+5),(x-4, y+5),(x-3, y+5),(x-2, y+5),(x-1, y+5),(x+0, y+5),(x+1, y+5),(x+2, y+5),(x+3, y+5),(x+4, y+5),(x+5, y+5),
			   (x-6, y+4),(x-5, y+4),(x-4, y+4),(x-3, y+4),(x-2, y+4),(x-1, y+4),(x+0, y+4),(x+1, y+4),(x+2, y+4),(x+3, y+4),(x+4, y+4),(x+5, y+4),
	(x-7, y+3),(x-6, y+3),(x-5, y+3),(x-4, y+3),(x-3, y+3),(x-2, y+3),(x-1, y+3),(x+0, y+3),(x+1, y+3),(x+2, y+3),(x+3, y+3),(x+4, y+3),(x+5, y+3),(x+6, y+3),						(x+9, y+3),																																										   (x+24, y+3),
	(x-7, y+2),(x-6, y+2),(x-5, y+2),(x-4, y+2),(x-3, y+2),(x-2, y+2),(x-1, y+2),(x+0, y+2),(x+1, y+2),(x+2, y+2),(x+3, y+2),(x+4, y+2),(x+5, y+2),(x+6, y+2),			 (x+8, y+2),(x+9, y+2),(x+10, y+2),(x+11, y+2),(x+12, y+2),(x+13, y+2),(x+14, y+2),(x+15, y+2),(x+16, y+2),(x+17, y+2),(x+18, y+2),(x+19, y+2),(x+20, y+2),(x+21, y+2),(x+22, y+2),(x+23, y+2),(x+24, y+2),
			   (x-6, y+1),(x-5, y+1),(x-4, y+1),(x-3, y+1),(x-2, y+1),(x-1, y+1),(x+0, y+1),(x+1, y+1),(x+2, y+1),(x+3, y+1),(x+4, y+1),(x+5, y+1),						 (x+8, y+1),(x+9, y+1),(x+10, y+1),(x+11, y+1),(x+12, y+1),(x+13, y+1),(x+14, y+1),(x+15, y+1),(x+16, y+1),(x+17, y+1),(x+18, y+1),(x+19, y+1),(x+20, y+1),(x+21, y+1),
			   (x-6, y+0),(x-5, y+0),(x-4, y+0),(x-3, y+0),(x-2, y+0),(x-1, y+0),(x+0, y+0),(x+1, y+0),(x+2, y+0),(x+3, y+0),(x+4, y+0),(x+5, y+0),(x+6, y+0),(x+7, y+0),(x+8, y+0),(x+9, y+0),			   (x+11, y+0),			   (x+13, y+0),												   (x+18, y+0),(x+19, y+0),(x+20, y+0),
	(x-7, y-1),(x-6, y-1),(x-5, y-1),(x-4, y-1),(x-3, y-1),(x-2, y-1),(x-1, y-1),(x+0, y-1),(x+1, y-1),(x+2, y-1),(x+3, y-1),(x+4, y-1),(x+5, y-1),(x+6, y-1),(x+7, y-1),			(x+9, y-1),(x+10, y-1),(x+11, y-1),			   (x+13, y-1),						   (x+16, y-1),(x+17, y-1),(x+18, y-1),(x+19, y-1),(x+20, y-1),(x+21, y-1),(x+22, y-1),
	(x-7, y-2),(x-6, y-2),(x-5, y-2),(x-4, y-2),(x-3, y-2),(x-2, y-2),(x-1, y-2),(x+0, y-2),(x+1, y-2),(x+2, y-2),(x+3, y-2),(x+4, y-2),(x+5, y-2),(x+6, y-2),																	   (x+13, y-2),						   (x+16, y-2),(x+17, y-2),(x+18, y-2),(x+19, y-2),(x+20, y-2),(x+21, y-2),(x+22, y-2),(x+23, y-2),
			   (x-6, y-3),(x-5, y-3),(x-4, y-3),(x-3, y-3),(x-2, y-3),(x-1, y-3),(x+0, y-3),(x+1, y-3),(x+2, y-3),(x+3, y-3),(x+4, y-3),(x+5, y-3),																				   						   (x+15, y-3),(x+16, y-3),(x+17, y-3),(x+18, y-3),(x+19, y-3),(x+20, y-3),(x+21, y-3),(x+22, y-3),(x+23, y-3),
			   			  (x-5, y-4),(x-4, y-4),(x-3, y-4),(x-2, y-4),(x-1, y-4),(x+0, y-4),(x+1, y-4),(x+2, y-4),(x+3, y-4),(x+4, y-4),																						   (x+13, y-4),(x+14, y-4),(x+15, y-4),(x+16, y-4),(x+17, y-4),(x+18, y-4),(x+19, y-4),(x+20, y-4),(x+21, y-4),(x+22, y-4),(x+23, y-4),
			   			  (x-5, y-5),(x-4, y-5),(x-3, y-5),(x-2, y-5),(x-1, y-5),(x+0, y-5),(x+1, y-5),(x+2, y-5),(x+3, y-5),(x+4, y-5),																			   (x+12, y-5),(x+13, y-5),(x+14, y-5),(x+15, y-5),(x+16, y-5),(x+17, y-5),(x+18, y-5),(x+19, y-5),(x+20, y-5),(x+21, y-5),(x+22, y-5),(x+23, y-5),(x+24, y-5),
			   			  			 (x-4, y-6),(x-3, y-6),(x-2, y-6),					    (x+1, y-6),(x+2, y-6),(x+3, y-6),																						   (x+12, y-6),(x+13, y-6),(x+14, y-6),(x+15, y-6),(x+16, y-6),(x+17, y-6),(x+18, y-6),(x+19, y-6),(x+20, y-6),(x+21, y-6),(x+22, y-6),(x+23, y-6),
	]
	if(repos):
		negro = (107/255,142/255,35/255)
		verde = (107/255,142/255,35/255)
		crema = (107/255,142/255,35/255)
		blanc = (107/255,142/255,35/255)
		plomo = (107/255,142/255,35/255)
		plomo = (107/255,142/255,35/255)
		maro2 = (107/255,142/255,35/255)
		plom2 = (107/255,142/255,35/255)
		dorad = (107/255,142/255,35/255)
		arena = (107/255,142/255,35/255)
	else:
		negro = (0.0,0.0,0)
		verde = (0,0.25,0)
		crema = (1,0.89,0.75)
		blanc = (255,255,255)
		plomo = (139,69,19)
		plomo = (0.75,0.75,0.75)
		maro2 = (139/255, 69/255,19/255)
		plom2 = (0.41,0.41,0.41)
		dorad = (218/255,165/255,32/255)
		arena = ( 79/255, 64/255,18/255)
	Colores_Soldado2 = [
							negro, 	negro,	negro,	negro,	negro,	negro, 	negro,	negro,
					negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	negro,	verde,	blanc,	blanc,	blanc,	blanc,	verde,	negro,	negro,	negro,
			negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,
	negro,	crema,	negro,	negro,	crema,	crema,	crema,	crema,	crema,	crema,	negro,	negro,	crema,	negro,					plom2,																													plom2,
	negro,	crema,	crema,	crema,	crema,	negro,	crema,	crema,	negro,	crema,	crema,	crema,	crema,	negro,			plom2,	plom2,	plom2,	plom2,	plomo,	plomo,	plom2,	plom2,	plom2,	plom2,	plom2,	plom2,	plom2,	plom2,	plom2,	plom2,	plom2,
			negro,	negro,	crema,	crema,	plomo,	crema,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,					maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,
			negro,	negro,	negro,	crema,	crema,	negro,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	plom2,			plom2,			plomo,									negro,	negro,	negro,
	negro,	crema,	crema,	negro,	negro,	negro,	negro,	maro2,	maro2,	maro2,	maro2,	crema,	crema,	maro2,	maro2,			plom2,	plom2,	plom2,			plomo,					negro,	negro,	negro,	dorad,	negro,	negro,	negro,
	negro,	crema,	crema,	negro,	verde,	negro,	verde,	verde,	negro,	verde,	negro,	crema,	crema,	negro,													plomo,					negro,	dorad,	arena,	dorad,	dorad,	dorad,	dorad,	negro,
			negro,	negro,	negro,	verde,	negro,	negro,	verde,	verde,	negro,	negro,	negro,	negro,																			negro,	dorad, 	dorad,	arena,	dorad,	dorad,	dorad,	dorad,	negro,
					negro,	verde,	negro,	negro,	verde,	verde,	negro,	negro,	verde,	negro,																	negro,	negro,	dorad,	arena,	arena,	dorad,	arena,	arena,	arena,	arena,	negro,
					negro,	verde,	verde,	verde,	negro,	negro,	verde,	negro,	verde,	negro,															negro,	dorad,	dorad,	dorad,	dorad,	arena,	arena,	arena,	arena,	dorad,	dorad,	dorad,	negro,
							negro,	negro,	negro,					negro,	negro,	negro,																	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,

	]



	if(caso==0):	
		for i in range(292):
			xf = (Puntos_Soldado2[i][0])*size
			yf = (Puntos_Soldado2[i][1])*size
			R = Colores_Soldado2[i][0]
			G = Colores_Soldado2[i][1]
			B = Colores_Soldado2[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==1):
		for i in range(292):
			xf = (x-(Puntos_Soldado2[i][0]-x))*size
			yf = (y-(Puntos_Soldado2[i][1]-y))*size
			R = Colores_Soldado2[i][0]
			G = Colores_Soldado2[i][1]
			B = Colores_Soldado2[i][2]
			set_pixel(xf,yf,R,G,B,size)			
	elif(caso==2):
		for i in range(292):
			yf = (y+(Puntos_Soldado2[i][0]-x))*size
			xf = (x+(Puntos_Soldado2[i][1]-y))*size
			R = Colores_Soldado2[i][0]
			G = Colores_Soldado2[i][1]
			B = Colores_Soldado2[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==3):
		for i in range(292):
			yf = (y-(Puntos_Soldado2[i][0]-x))*size
			xf = (x-(Puntos_Soldado2[i][1]-y))*size
			R = Colores_Soldado2[i][0]
			G = Colores_Soldado2[i][1]
			B = Colores_Soldado2[i][2]
			set_pixel(xf,yf,R,G,B,size)
	return
def PintarUnidad3(x, y,caso,repos, size):
	Puntos_Soldado3 = [
									 (x-4, y+9),(x-3, y+9),(x-2, y+9),(x-1, y+9),(x+0, y+9),(x+1, y+9),(x+2, y+9),(x+3, y+9),
			   			  (x-5, y+8),(x-4, y+8),(x-3, y+8),(x-2, y+8),(x-1, y+8),(x+0, y+8),(x+1, y+8),(x+2, y+8),(x+3, y+8),(x+4, y+8),
			   (x-6, y+7),(x-5, y+7),(x-4, y+7),(x-3, y+7),(x-2, y+7),(x-1, y+7),(x+0, y+7),(x+1, y+7),(x+2, y+7),(x+3, y+7),(x+4, y+7),(x+5, y+7),
			   (x-6, y+6),(x-5, y+6),(x-4, y+6),(x-3, y+6),(x-2, y+6),(x-1, y+6),(x+0, y+6),(x+1, y+6),(x+2, y+6),(x+3, y+6),(x+4, y+6),(x+5, y+6),
			   (x-6, y+5),(x-5, y+5),(x-4, y+5),(x-3, y+5),(x-2, y+5),(x-1, y+5),(x+0, y+5),(x+1, y+5),(x+2, y+5),(x+3, y+5),(x+4, y+5),(x+5, y+5),
			   (x-6, y+4),(x-5, y+4),(x-4, y+4),(x-3, y+4),(x-2, y+4),(x-1, y+4),(x+0, y+4),(x+1, y+4),(x+2, y+4),(x+3, y+4),(x+4, y+4),(x+5, y+4),
	(x-7, y+3),(x-6, y+3),(x-5, y+3),(x-4, y+3),(x-3, y+3),(x-2, y+3),(x-1, y+3),(x+0, y+3),(x+1, y+3),(x+2, y+3),(x+3, y+3),(x+4, y+3),(x+5, y+3),(x+6, y+3),
	(x-7, y+2),(x-6, y+2),(x-5, y+2),(x-4, y+2),(x-3, y+2),(x-2, y+2),(x-1, y+2),(x+0, y+2),(x+1, y+2),(x+2, y+2),(x+3, y+2),(x+4, y+2),(x+5, y+2),(x+6, y+2),
			   (x-6, y+1),(x-5, y+1),(x-4, y+1),(x-3, y+1),(x-2, y+1),(x-1, y+1),(x+0, y+1),(x+1, y+1),(x+2, y+1),(x+3, y+1),(x+4, y+1),(x+5, y+1),
			   (x-6, y+0),(x-5, y+0),(x-4, y+0),(x-3, y+0),(x-2, y+0),(x-1, y+0),(x+0, y+0),(x+1, y+0),(x+2, y+0),(x+3, y+0),(x+4, y+0),(x+5, y+0),
	(x-7, y-1),(x-6, y-1),(x-5, y-1),(x-4, y-1),(x-3, y-1),(x-2, y-1),(x-1, y-1),(x+0, y-1),(x+1, y-1),(x+2, y-1),(x+3, y-1),(x+4, y-1),(x+5, y-1),(x+6, y-1),
	(x-7, y-2),(x-6, y-2),(x-5, y-2),(x-4, y-2),(x-3, y-2),(x-2, y-2),(x-1, y-2),(x+0, y-2),(x+1, y-2),(x+2, y-2),(x+3, y-2),(x+4, y-2),(x+5, y-2),(x+6, y-2),
			   (x-6, y-3),(x-5, y-3),(x-4, y-3),(x-3, y-3),(x-2, y-3),(x-1, y-3),(x+0, y-3),(x+1, y-3),(x+2, y-3),(x+3, y-3),(x+4, y-3),(x+5, y-3),
			   			  (x-5, y-4),(x-4, y-4),(x-3, y-4),(x-2, y-4),(x-1, y-4),(x+0, y-4),(x+1, y-4),(x+2, y-4),(x+3, y-4),(x+4, y-4),
			   			  (x-5, y-5),(x-4, y-5),(x-3, y-5),(x-2, y-5),(x-1, y-5),(x+0, y-5),(x+1, y-5),(x+2, y-5),(x+3, y-5),(x+4, y-5),
			   			  			 (x-4, y-6),(x-3, y-6),(x-2, y-6),					    (x+1, y-6),(x+2, y-6),(x+3, y-6)
	]
	if(repos):
		negro = (107/255,142/255,35/255)
		verde = (107/255,142/255,35/255)
		crema = (107/255,142/255,35/255)
		blanc = (107/255,142/255,35/255)
		plomo = (107/255,142/255,35/255)
		plom2 = (107/255,142/255,35/255)
	else:
		negro = (0.0,0.0,0)
		verde = (0,0.25,0)
		crema = (1,0.89,0.75)
		blanc = (255,255,255)
		plomo = (0.75,0.75,0.75)
		plom2 = (0.41,0.41,0.41)
	Colores_Soldado3 = [
							negro, 	negro, 	negro, 	negro,	negro, 	negro, 	negro,	negro,
					negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	verde,	negro,	negro,
			negro,	negro,	negro,	verde,	blanc,	blanc,	blanc,	blanc,	verde,	negro,	negro,	negro,
			negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,
	negro,	crema,	negro,	plom2,	crema,	crema,	crema,	crema,	crema,	crema,	plom2,	negro,	crema,	negro,
	negro,	crema,	crema,	plomo,	crema,	negro,	crema,	crema,	negro,	crema,	plomo,	crema,	crema,	negro,
			negro,	negro,	plomo,	crema,	plom2,	crema,	crema,	plom2,	crema,	plomo,	negro,	negro,
			negro,	negro,	negro,	plomo,	plomo,	plom2,	plom2,	plomo,	plomo,	negro,	negro,	negro,
	negro,	crema,	crema,	negro,	plomo,	plomo,	plomo,	plomo,	plomo,	plomo,	negro,	crema,	crema,	negro,
	negro,	crema,	crema,	negro,	verde,	negro,	verde,	verde,	negro,	verde,	negro,	crema,	crema,	negro,
			negro,	negro,	negro,	verde,	negro,	negro,	verde,	verde,	negro,	negro,	negro,	negro,	
					negro,	verde,	negro,	negro,	verde,	verde,	negro,	negro,	verde,	negro,
					negro,	verde,	verde,	verde,	negro,	negro,	verde,	negro,	verde,	negro,
							negro,	negro,	negro,					negro,	negro,	negro,

	]


#===================================================================
#Pintado del mapa
#===================================================================
def PintarMapa(x, y, size):
	Puntos_Mapa = [
	(x-4,y+6),(x-3,y+6),(x-2,y+6),(x-1,y+6),(x,y+6),(x+1,y+6),(x+2,y+6),(x+3,y+6),(x+4,y+6),
	(x-4,y+5),(x-3,y+5),(x-2,y+5),(x-1,y+5),(x,y+5),(x+1,y+5),(x+2,y+5),(x+3,y+5),(x+4,y+5),
	(x-4,y+4),(x-3,y+4),(x-2,y+4),(x-1,y+4),(x,y+4),(x+1,y+4),(x+2,y+4),(x+3,y+4),(x+4,y+4),
	(x-4,y+3),(x-3,y+3),(x-2,y+3),(x-1,y+3),(x,y+3),(x+1,y+3),(x+2,y+3),(x+3,y+3),(x+4,y+3),
	(x-4,y+2),(x-3,y+2),(x-2,y+2),(x-1,y+2),(x,y+2),(x+1,y+2),(x+2,y+2),(x+3,y+2),(x+4,y+2),
	]
	verde = (107/255,142/255,35/255)
	Colores_Fondo = [
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	]

	for i in range(45):
		x = Puntos_Mapa[i][0]*size
		y = Puntos_Mapa[i][1]*size
		R = Colores_Fondo[i][0]
		G = Colores_Fondo[i][1]
		B = Colores_Fondo[i][2]
		set_pixel(x,y,R,G,B,size)
	return
def PintarMapa2(x, y, size):
	Puntos_Mapa = [
	(x-4,y-6),(x-3,y-6),(x-2,y-6),(x-1,y-6),(x,y-6),(x+1,y-6),(x+2,y-6),(x+3,y-6),(x+4,y-6),
	(x-4,y-5),(x-3,y-5),(x-2,y-5),(x-1,y-5),(x,y-5),(x+1,y-5),(x+2,y-5),(x+3,y-5),(x+4,y-5),
	(x-4,y-4),(x-3,y-4),(x-2,y-4),(x-1,y-4),(x,y-4),(x+1,y-4),(x+2,y-4),(x+3,y-4),(x+4,y-4),
	(x-4,y-3),(x-3,y-3),(x-2,y-3),(x-1,y-3),(x,y-3),(x+1,y-3),(x+2,y-3),(x+3,y-3),(x+4,y-3),
	(x-4,y-2),(x-3,y-2),(x-2,y-2),(x-1,y-2),(x,y-2),(x+1,y-2),(x+2,y-2),(x+3,y-2),(x+4,y-2),
	]
	verde = (107/255,142/255,35/255)
	Colores_Fondo = [
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,verde,
	]

	for i in range(45):
		x = Puntos_Mapa[i][0]*size
		y = Puntos_Mapa[i][1]*size
		R = Colores_Fondo[i][0]
		G = Colores_Fondo[i][1]
		B = Colores_Fondo[i][2]
		set_pixel(x,y,R,G,B,size)
	return

def main():
	scale = 2
	scalefondo = 40
	width, height = scale * 300, scale * 300
	i=0
	Limites = [(0,300),(0,2000)]
	TamanioSoldados = [(1, 1),(1,1),(2,1),(2,1),(3,2)]
	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	glClearColor(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT)
	# -------
	# Point (pixel)
	# -------
	xmapa = 299
	ymapa = 299
	x = 0
	y = 0
	cursorPosicionamiento = [x,y]
	# -------
	# Transformation
	# -------
	# ---------------------------------------------------------
	#PintarMapa(xmapa,ymapa,scalefondo)
	#PintarMapa2(xmapa,ymapa,scalefondo)
	#PintarUnidad1(x,y,0,False,scale)
	while True:
		for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#True = False
			if event.type==pygame.MOUSEBUTTONDOWN:
				if mouse.get_pressed()[0]:
					pos=pygame.mouse.get_pos()
					print(pos)
					x=pos[0]
					y=pos[1]
					print("The number is", x)
					print("The number is", y)
					verde = (107/255,142/255,35/255)
					vverde = (0,0.25,0)
					negro = 107/255
					#PintarUnidad1(x,y,0,False,scale)
					set_pixel(x,y,negro,negro,negro,1)
					glFlush()
			if event.type==pygame.MOUSEBUTTONUP:
				if mouse.get_pressed()[0]:
					pos=pygame.mouse.get_pos()
					#print(pos)
					x,y=pos
					x=x-300
					print("The number is", x)
					y=y-200
					print("The number is", y)
					#PintarUnidad1(x,y,0,False,scale)
					set_pixel(x,y,R,G,B,scalefondo)

					glFlush()
		#pygame.display.flip()
if __name__ == '__main__':
	main()