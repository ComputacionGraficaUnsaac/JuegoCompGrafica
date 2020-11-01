# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from utils import *
import random
import math
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

	Puntos_Mortero = [
																																																																															(x+33,y+27),(x+34,y+27),(x+35,y+27),
																																																																												(x+32,y+26),(x+33,y+26),(x+34,y+26),(x+35,y+26),(x+36,y+26),
																																																																									(x+31,y+25),(x+32,y+25),(x+33,y+25),(x+34,y+25),(x+35,y+25),(x+36,y+25),(x+37,y+25),
																																																																									(x+31,y+24),(x+32,y+24),(x+33,y+24),(x+34,y+24),(x+35,y+24),(x+36,y+24),(x+37,y+24),(x+38,y+24),
																																																																						(x+30,y+23),(x+31,y+23),(x+32,y+23),(x+33,y+23),(x+34,y+23),(x+35,y+23),(x+36,y+23),(x+37,y+23),(x+38,y+23),(x+39,y+23),
																																																																			(x+29,y+22),(x+30,y+22),(x+31,y+22),(x+32,y+22),(x+33,y+22),(x+34,y+22),(x+35,y+22),(x+36,y+22),(x+37,y+22),(x+38,y+22),(x+39,y+22),
																																																																(x+28,y+21),(x+29,y+21),(x+30,y+21),(x+31,y+21),(x+32,y+21),(x+33,y+21),(x+34,y+21),(x+35,y+21),(x+36,y+21),(x+37,y+21),(x+38,y+21),(x+39,y+21),
																																																																(x+28,y+20),(x+29,y+20),(x+30,y+20),(x+31,y+20),(x+32,y+20),(x+33,y+20),(x+34,y+20),(x+35,y+20),(x+36,y+20),(x+37,y+20),(x+38,y+20),
																																																													(x+27,y+19),(x+28,y+19),(x+29,y+19),(x+30,y+19),(x+31,y+19),(x+32,y+19),(x+33,y+19),(x+34,y+19),(x+35,y+19),(x+36,y+19),(x+37,y+19),
																																																										(x+26,y+18),(x+27,y+18),(x+28,y+18),(x+29,y+18),(x+30,y+18),(x+31,y+18),(x+32,y+18),(x+33,y+18),(x+34,y+18),(x+35,y+18),(x+36,y+18),(x+37,y+18),
																																																							(x+25,y+17),(x+26,y+17),(x+27,y+17),(x+28,y+17),(x+29,y+17),(x+30,y+17),(x+31,y+17),(x+32,y+17),(x+33,y+17),(x+34,y+17),(x+35,y+17),(x+36,y+17),
																																																							(x+25,y+16),(x+26,y+16),(x+27,y+16),(x+28,y+16),(x+29,y+16),(x+30,y+16),(x+31,y+16),(x+32,y+16),(x+33,y+16),(x+34,y+16),(x+35,y+16),
																																																				(x+24,y+15),(x+25,y+15),(x+26,y+15),(x+27,y+15),(x+28,y+15),(x+29,y+15),(x+30,y+15),(x+31,y+15),(x+32,y+15),(x+33,y+15),(x+34,y+15),(x+35,y+15),
																																																	(x+23,y+14),(x+24,y+14),(x+25,y+14),(x+26,y+14),(x+27,y+14),(x+28,y+14),(x+29,y+14),(x+30,y+14),(x+31,y+14),(x+32,y+14),(x+33,y+14),(x+34,y+14),
																																								(x+20,y+13),(x+21,y+13),(x+22,y+13),(x+23,y+13),(x+24,y+13),(x+25,y+13),(x+26,y+13),(x+27,y+13),(x+28,y+13),(x+29,y+13),(x+30,y+13),(x+31,y+13),(x+32,y+13),(x+33,y+13),(x+34,y+13),(x+35,y+13),(x+36,y+13),(x+37,y+13),(x+38,y+13),
																																								(x+20,y+12),(x+21,y+12),(x+22,y+12),(x+23,y+12),(x+24,y+12),(x+25,y+12),(x+26,y+12),(x+27,y+12),(x+28,y+12),(x+29,y+12),(x+30,y+12),(x+31,y+12),(x+32,y+12),(x+33,y+12),(x+34,y+12),(x+35,y+12),(x+36,y+12),(x+37,y+12),(x+38,y+12),
																																								(x+20,y+11),(x+21,y+11),(x+22,y+11),(x+23,y+11),(x+24,y+11),(x+25,y+11),(x+26,y+11),(x+27,y+11),(x+28,y+11),(x+29,y+11),(x+30,y+11),(x+31,y+11),(x+32,y+11),(x+33,y+11),(x+34,y+11),(x+35,y+11),(x+36,y+11),(x+37,y+11),(x+38,y+11),
																																								(x+20,y+10),(x+21,y+10),(x+22,y+10),(x+23,y+10),(x+24,y+10),(x+25,y+10),(x+26,y+10),(x+27,y+10),(x+28,y+10),(x+29,y+10),(x+30,y+10),(x+31,y+10),(x+32,y+10),(x+33,y+10),(x+34,y+10),(x+35,y+10),(x+36,y+10),(x+37,y+10),(x+38,y+10),
																																								(x+20, y+9),(x+21, y+9),(x+22, y+9),(x+23,y+ 9),(x+24,y+ 9),(x+25,y+ 9),(x+26,y+ 9),(x+27,y+ 9),(x+28,y+ 9),(x+29,y+ 9),(x+30,y+ 9),(x+31,y+ 9),(x+32,y+ 9),(x+33,y+ 9),(x+34,y+ 9),(x+35,y+ 9),(x+36,y+ 9),(x+37,y+ 9),(x+38,y+ 9),
																															(x+17, y+8),(x+18, y+8),(x+19, y+8),(x+20, y+8),(x+21, y+8),(x+22, y+8),(x+23,y+ 8),(x+24,y+ 8),(x+25,y+ 8),(x+26,y+ 8),(x+27,y+ 8),(x+28,y+ 8),(x+29,y+ 8),(x+30,y+ 8),(x+31,y+ 8),(x+32,y+ 8),(x+33,y+ 8),(x+34,y+ 8),(x+35,y+ 8),(x+36,y+ 8),(x+37,y+ 8),(x+38,y+ 8),(x+39,y+ 8),(x+40,y+ 8),(x+41,y+ 8),
																															(x+17, y+7),(x+18, y+7),(x+19, y+7),(x+20, y+7),(x+21, y+7),(x+22, y+7),(x+23,y+ 7),(x+24,y+ 7),(x+25,y+ 7),(x+26,y+ 7),(x+27,y+ 7),(x+28,y+ 7),(x+29,y+ 7),(x+30,y+ 7),(x+31,y+ 7),(x+32,y+ 7),(x+33,y+ 7),(x+34,y+ 7),(x+35,y+ 7),(x+36,y+ 7),(x+37,y+ 7),(x+38,y+ 7),(x+39,y+ 7),(x+40,y+ 7),(x+41,y+ 7),
																															(x+17, y+6),(x+18, y+6),(x+19, y+6),(x+20, y+6),(x+21, y+6),(x+22, y+6),(x+23,y+ 6),(x+24,y+ 6),(x+25,y+ 6),(x+26,y+ 6),(x+27,y+ 6),(x+28,y+ 6),(x+29,y+ 6),(x+30,y+ 6),(x+31,y+ 6),(x+32,y+ 6),(x+33,y+ 6),(x+34,y+ 6),(x+35,y+ 6),(x+36,y+ 6),(x+37,y+ 6),(x+38,y+ 6),(x+39,y+ 6),(x+40,y+ 6),(x+41,y+ 6),
																															(x+17, y+5),(x+18, y+5),(x+19, y+5),(x+20, y+5),(x+21, y+5),(x+22, y+5),(x+23,y+ 5),(x+24,y+ 5),(x+25,y+ 5),(x+26,y+ 5),(x+27,y+ 5),(x+28,y+ 5),(x+29,y+ 5),(x+30,y+ 5),(x+31,y+ 5),(x+32,y+ 5),(x+33,y+ 5),(x+34,y+ 5),(x+35,y+ 5),(x+36,y+ 5),(x+37,y+ 5),(x+38,y+ 5),(x+39,y+ 5),(x+40,y+ 5),(x+41,y+ 5),
																(x+12, y+4),(x+13, y+4),(x+14, y+4),(x+15, y+4),(x+16, y+4),(x+17, y+4),(x+18, y+4),(x+19, y+4),(x+20, y+4),(x+21, y+4),(x+22, y+4),(x+23,y+ 4),(x+24,y+ 4),(x+25,y+ 4),(x+26,y+ 4),(x+27,y+ 4),(x+28,y+ 4),(x+29,y+ 4),(x+30,y+ 4),(x+31,y+ 4),(x+32,y+ 4),(x+33,y+ 4),(x+34,y+ 4),(x+35,y+ 4),(x+36,y+ 4),(x+37,y+ 4),(x+38,y+ 4),(x+39,y+ 4),(x+40,y+ 4),(x+41,y+ 4),(x+42,y+ 4),(x+43,y+ 4),(x+44,y+ 4),(x+45,y+ 4),(x+46,y+ 4),
													(x+11, y+3),(x+12, y+3),(x+13, y+3),(x+14, y+3),(x+15, y+3),(x+16, y+3),(x+17, y+3),(x+18, y+3),(x+19, y+3),(x+20, y+3),(x+21, y+3),(x+22, y+3),(x+23,y+ 3),(x+24,y+ 3),(x+25,y+ 3),(x+26,y+ 3),(x+27,y+ 3),(x+28,y+ 3),(x+29,y+ 3),(x+30,y+ 3),(x+31,y+ 3),(x+32,y+ 3),(x+33,y+ 3),(x+34,y+ 3),(x+35,y+ 3),(x+36,y+ 3),(x+37,y+ 3),(x+38,y+ 3),(x+39,y+ 3),(x+40,y+ 3),(x+41,y+ 3),(x+42,y+ 3),(x+43,y+ 3),(x+44,y+ 3),(x+45,y+ 3),(x+46,y+ 3),(x+47,y+ 3),
													(x+11, y+2),(x+12, y+2),(x+13, y+2),(x+14, y+2),(x+15, y+2),(x+16, y+2),(x+17, y+2),(x+18, y+2),(x+19, y+2),(x+20, y+2),(x+21, y+2),(x+22, y+2),(x+23,y+ 2),(x+24,y+ 2),(x+25,y+ 2),(x+26,y+ 2),(x+27,y+ 2),(x+28,y+ 2),(x+29,y+ 2),(x+30,y+ 2),(x+31,y+ 2),(x+32,y+ 2),(x+33,y+ 2),(x+34,y+ 2),(x+35,y+ 2),(x+36,y+ 2),(x+37,y+ 2),(x+38,y+ 2),(x+39,y+ 2),(x+40,y+ 2),(x+41,y+ 2),(x+42,y+ 2),(x+43,y+ 2),(x+44,y+ 2),(x+45,y+ 2),(x+46,y+ 2),(x+47,y+ 2),
													(x+11, y+1),(x+12, y+1),(x+13, y+1),(x+14, y+1),(x+15, y+1),(x+16, y+1),(x+17, y+1),(x+18, y+1),(x+19, y+1),(x+20, y+1),(x+21, y+1),(x+22, y+1),(x+23,y+ 1),(x+24,y+ 1),(x+25,y+ 1),(x+26,y+ 1),(x+27,y+ 1),(x+28,y+ 1),(x+29,y+ 1),(x+30,y+ 1),(x+31,y+ 1),(x+32,y+ 1),(x+33,y+ 1),(x+34,y+ 1),(x+35,y+ 1),(x+36,y+ 1),(x+37,y+ 1),(x+38,y+ 1),(x+39,y+ 1),(x+40,y+ 1),(x+41,y+ 1),(x+42,y+ 1),(x+43,y+ 1),(x+44,y+ 1),(x+45,y+ 1),(x+46,y+ 1),(x+47,y+ 1),
				(x+8, y+0),	(x+9, y+0),				(x+11, y+0),(x+12, y+0),(x+13, y+0),(x+14, y+0),(x+15, y+0),(x+16, y+0),(x+17, y+0),(x+18, y+0),(x+19, y+0),(x+20, y+0),(x+21, y+0),(x+22, y+0),(x+23,y+ 0),(x+24,y+ 0),(x+25,y+ 0),(x+26,y+ 0),(x+27,y+ 0),(x+28,y+ 0),(x+29,y+ 0),(x+30,y+ 0),(x+31,y+ 0),(x+32,y+ 0),(x+33,y+ 0),(x+34,y+ 0),(x+35,y+ 0),(x+36,y+ 0),(x+37,y+ 0),(x+38,y+ 0),(x+39,y+ 0),(x+40,y+ 0),(x+41,y+ 0),(x+42,y+ 0),(x+43,y+ 0),(x+44,y+ 0),(x+45,y+ 0),(x+46,y+ 0),(x+47,y+ 0),
	(x+7, y-1),							(x+10, y-1),(x+11, y-1),(x+12, y-1),(x+13, y-1),(x+14, y-1),(x+15, y-1),(x+16, y-1),(x+17, y-1),(x+18, y-1),(x+19, y-1),(x+20, y-1),(x+21, y-1),(x+22, y-1),(x+23,y- 1),(x+24,y- 1),(x+25,y- 1),(x+26,y- 1),(x+27,y- 1),(x+28,y- 1),(x+29,y- 1),(x+30,y- 1),(x+31,y- 1),(x+32,y- 1),(x+33,y- 1),(x+34,y- 1),(x+35,y- 1),(x+36,y- 1),(x+37,y- 1),(x+38,y- 1),(x+39,y- 1),(x+40,y- 1),(x+41,y- 1),(x+42,y- 1),(x+43,y- 1),(x+44,y- 1),(x+45,y- 1),(x+46,y- 1),(x+47,y- 1),
	(x+7, y-2),							(x+10, y-2),(x+11, y-2),(x+12, y-2),(x+13, y-2),(x+14, y-2),(x+15, y-2),(x+16, y-2),(x+17, y-2),(x+18, y-2),(x+19, y-2),(x+20, y-2),(x+21, y-2),(x+22, y-2),(x+23,y- 2),(x+24,y- 2),(x+25,y- 2),(x+26,y- 2),(x+27,y- 2),(x+28,y- 2),(x+29,y- 2),(x+30,y- 2),(x+31,y- 2),(x+32,y- 2),(x+33,y- 2),(x+34,y- 2),(x+35,y- 2),(x+36,y- 2),(x+37,y- 2),(x+38,y- 2),(x+39,y- 2),(x+40,y- 2),(x+41,y- 2),(x+42,y- 2),(x+43,y- 2),(x+44,y- 2),(x+45,y- 2),(x+46,y- 2),(x+47,y- 2),
				(x+8, y-3),	(x+9, y-3),				(x+11, y-3),(x+12, y-3),(x+13, y-3),(x+14, y-3),(x+15, y-3),(x+16, y-3),(x+17, y-3),(x+18, y-3),(x+19, y-3),(x+20, y-3),(x+21, y-3),(x+22, y-3),(x+23,y- 3),(x+24,y- 3),(x+25,y- 3),(x+26,y- 3),(x+27,y- 3),(x+28,y- 3),(x+29,y- 3),(x+30,y- 3),(x+31,y- 3),(x+32,y- 3),(x+33,y- 3),(x+34,y- 3),(x+35,y- 3),(x+36,y- 3),(x+37,y- 3),(x+38,y- 3),(x+39,y- 3),(x+40,y- 3),(x+41,y- 3),(x+42,y- 3),(x+43,y- 3),(x+44,y- 3),(x+45,y- 3),(x+46,y- 3),(x+47,y- 3),
																(x+12, y-4),(x+13, y-4),(x+14, y-4),(x+15, y-4),(x+16, y-4),(x+17, y-4),(x+18, y-4),(x+19, y-4),(x+20, y-4),(x+21, y-4),(x+22, y-4),(x+23,y- 4),(x+24,y- 4),(x+25,y- 4),(x+26,y- 4),(x+27,y- 4),(x+28,y- 4),(x+29,y- 4),(x+30,y- 4),(x+31,y- 4),(x+32,y- 4),(x+33,y- 4),(x+34,y- 4),(x+35,y- 4),(x+36,y- 4),(x+37,y- 4),(x+38,y- 4),(x+39,y- 4),(x+40,y- 4),(x+41,y- 4),(x+42,y- 4),(x+43,y- 4),(x+44,y- 4),(x+45,y- 4),(x+46,y- 4),
																									(x+15, y-5),(x+16, y-5),(x+17, y-5),(x+18, y-5),(x+19, y-5),																																																									(x+39,y- 5),(x+40,y- 5),(x+41,y- 5),(x+42,y- 5),(x+43,y- 5),
																												(x+16, y-6),(x+17, y-6),(x+18, y-6),																																																															(x+40,y- 6),(x+41,y- 6),(x+42,y- 6),
	]
	if(repos):
		maron = (107/255,142/255,35/255)
		maro2 = (107/255,142/255,35/255)
		dorad = (107/255,142/255,35/255)
		canon = (107/255,142/255,35/255)
	else:
		maron = (205/255,133/255,63/255)
		maro2 = (139/255, 69/255,19/255)
		dorad = (218/255,165/255,32/255)
		canon = ( 47/255, 79/255,79/255)

	Colores_Mortero = [

																																																					negro,	canon,	canon,
																																																			negro,	negro,	negro,	canon,	canon,
																																																	plomo,	plomo,	negro,	negro,	negro,	canon,	canon,
																																																	plomo,	canon,	canon,	negro,	negro,	negro,	canon,	canon,
																																															plomo,	canon,	canon,	canon,	canon,	negro,	negro,	negro,	canon,	canon,
																																													plomo,	canon,	canon,	canon,	canon,	canon,	canon,	negro,	negro,	negro,	canon,
																																											plomo,	plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	negro,	negro,	negro,
																																											plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	negro,
																																									plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,
																																							plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,
																																					plomo,	plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,
																																					plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,
																																			plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,
																																	plomo,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,	canon,
																											negro,	negro,	plomo,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	plomo,	negro,	negro,
																											negro,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron, 	negro,
																											negro,	maron,	negro,	dorad,	dorad,	dorad,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	negro,	maron, 	negro,
																											negro,	maron,	plomo,	dorad,	dorad,	dorad,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron, 	negro,
																											negro,	maron,	plomo,	dorad,	dorad,	dorad,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron, 	negro,
																					negro,	negro,	negro,	negro,	negro,	plomo,	dorad,	dorad,	dorad,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	plomo,	negro,	negro,	negro,	negro,	negro,
																					negro,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	negro,
																					negro,	maron,	maron,	maron,	maron,	negro,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	negro,	maron,	maron,	maron,	maron,	negro,
																					negro,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	negro,
											negro,	plomo,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	plomo,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	plomo,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	plomo,	negro,
									negro,	maron,	plomo,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron,	plomo,	maron,	negro,
									negro,	maron,	negro,	maron,	maron,	plomo,	negro,	plomo,	maron,	maron,	maron,	negro,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	negro,	dorad,	dorad,	dorad,	maron,	maron,	plomo,	negro,	plomo,	negro,	maron,	negro,
									negro,	maron,	plomo,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	dorad,	dorad,	dorad,	maron,	maron,	maron,	plomo,	maron,	plomo,	maron,	negro,
			plomo,	plomo,			negro,	maron,	plomo,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	plomo,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	maro2,	plomo,	dorad,	dorad,	dorad,	maro2,	maro2,	maro2,	maro2,	maro2,	plomo,	maron,	negro,
	plomo,					plomo,	negro,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	dorad,	dorad,	dorad,	maron,	maron,	maron,	maron,	maron,	plomo,	maron,	negro,
	plomo,					plomo,	negro,	maron,	negro,	maron,	maron,	negro,	negro,	negro,	maron,	maron,	maron,	negro,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	negro,	maron,	maron,	maron,	negro,	negro,	negro,	maron,	maron,	negro,	maron,	negro,
			plomo,	plomo,			negro,	maron,	plomo,	maron,	negro,	negro,	plomo,	negro,	negro,	maron,	maron,	plomo,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	maron,	plomo,	maron,	maron,	negro,	negro,	plomo,	negro,	negro,	maron,	plomo,	maron,	negro,
											negro,	negro,	negro,	negro,	plomo,	plomo,	plomo,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	negro,	plomo,	plomo,	plomo,	negro,	negro,	negro,	negro,
																	negro,	negro,	plomo,	negro,	negro,																																							negro,	negro,	plomo,	negro,	negro,
																			negro,	negro,	negro,																																											negro,	negro,	negro,
	]					

	if(caso==0):	
		for i in range(184):
			xf = (Puntos_Soldado3[i][0])*size
			yf = (Puntos_Soldado3[i][1])*size
			R = Colores_Soldado3[i][0]
			G = Colores_Soldado3[i][1]
			B = Colores_Soldado3[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==1):
		for i in range(184):
			xf = (x-(Puntos_Soldado3[i][0]-x))*size
			yf = (y-(Puntos_Soldado3[i][1]-y))*size
			R = Colores_Soldado3[i][0]
			G = Colores_Soldado3[i][1]
			B = Colores_Soldado3[i][2]
			set_pixel(xf,yf,R,G,B,size)			
	elif(caso==2):
		for i in range(184):
			yf = (y+(Puntos_Soldado3[i][0]-x))*size
			xf = (x+(Puntos_Soldado3[i][1]-y))*size
			R = Colores_Soldado3[i][0]
			G = Colores_Soldado3[i][1]
			B = Colores_Soldado3[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==3):
		for i in range(184):
			yf = (y-(Puntos_Soldado3[i][0]-x))*size
			xf = (x-(Puntos_Soldado3[i][1]-y))*size
			R = Colores_Soldado3[i][0]
			G = Colores_Soldado3[i][1]
			B = Colores_Soldado3[i][2]
			set_pixel(xf,yf,R,G,B,size)
	#==============================
	if(caso==0):	
		for i in range(685):
			xf = (Puntos_Mortero[i][0])*size
			yf = (Puntos_Mortero[i][1])*size
			R = Colores_Mortero[i][0]
			G = Colores_Mortero[i][1]
			B = Colores_Mortero[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==1):
		for i in range(685):
			xf = (x-(Puntos_Mortero[i][0]-x))*size
			yf = (y-(Puntos_Mortero[i][1]-y))*size
			R = Colores_Mortero[i][0]
			G = Colores_Mortero[i][1]
			B = Colores_Mortero[i][2]
			set_pixel(xf,yf,R,G,B,size)			
	elif(caso==2):
		for i in range(685):
			yf = (y+(Puntos_Mortero[i][0]-x))*size
			xf = (x+(Puntos_Mortero[i][1]-y))*size
			R = Colores_Mortero[i][0]
			G = Colores_Mortero[i][1]
			B = Colores_Mortero[i][2]
			set_pixel(xf,yf,R,G,B,size)
	elif(caso==3):
		for i in range(685):
			yf = (y-(Puntos_Mortero[i][0]-x))*size
			xf = (x-(Puntos_Mortero[i][1]-y))*size
			R = Colores_Mortero[i][0]
			G = Colores_Mortero[i][1]
			B = Colores_Mortero[i][2]
			set_pixel(xf,yf,R,G,B,size)
	return
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

def MostrarMatriz(a):
	i=0
	j=0
	for i in range (len(a)): 
		for j in range (len(a[i])):
			print (a[i][j],end=" ")
		print ("\n")

def RecorrerTrues(a):
	i=0
	j=0
	countTrues=0
	for i in range (len(a)): 
		for j in range (len(a[i])):
			if (a[i][j]==True):
				countTrues=countTrues+1
	if countTrues>0:
		return 1
	else:
		return 0


def MatrizParaEnemigos(Opciones):
	#Usar matrices predefinidas para posibles posiciones de enemigos:
	if (Opciones == 1):
		a = [[True,True,False,False,False,False,True,False,False],
			[False,False,False,False,False,False,False,False,False],
			[True, False,False,True,True,False,False,False,False],
			[False,False,False,False,False,True,True,True,False],
			[False,False,False,False,False,True,True,True,False]]
	elif (Opciones == 2):
		a = [[False,False,False,True,True,False,False,False,True],
			[True,True,True,False,False,False,False,False,False],
			[True,True,True,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False],
			[False,False,False,True,False,False,False,True,True]]
	elif (Opciones == 3):
		a = [[True,False,False,True,False,False,False,False,False],
			[False,False,False,True,False,False,True,True,True],
			[False,False,False,False,False,False,True,True,True],
			[False,True,False,False,False,False,False,False,False],
			[False,False,False,False,True,True,False,False,False]]
	elif (Opciones == 4):
		a = [[False,True,True,False,False,True,False,False,False],
			[False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,True,True],
			[False,True,True,True,False,False,False,False,False],
			[False,True,True,True,False,False,False,False,True]]
	elif (Opciones == 5):
		a = [[False,False,True,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False],
			[True,True,False,False,False,False,True,True,False],
			[True,True,False,False,False,False,False,False,False],
			[True,True,False,False,True,True,False,False,True]]
	return (a)
def Proyectil(x, y, size):
	Puntos_Proyectil = [
	(-5, 7), (-4, 7), (-3, 7), (-2, 7), (-1, 7), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
	(-5, 6), (-4, 6), (-3, 6), (-2, 6), (-1, 6), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), 
	(-5, 5), (-4, 5), (-3, 5), (-2, 5), (-1, 5), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), 
	(-5, 4), (-4, 4), (-3, 4), (-2, 4), (-1, 4), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), 
	(-5, 3), (-4, 3), (-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
	(-5, 2), (-4, 2), (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), 
	(-5, 1), (-4, 1), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
	(-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), 
	(-5, -1),(-4, -1),(-3, -1),(-2, -1),(-1, -1),(0, -1),(1, -1),(2, -1),(3, -1),(4, -1),
	(-5, -2),(-4, -2),(-3, -2),(-2, -2),(-1, -2),(0, -2),(1, -2),(2, -2),(3, -2),(4, -2)
	]
	negro = (0.0,0.0,0)
	plomo = (139/255,69/255,19/255)
	dorad = (218/255,165/255,32/255)
	Colores_Proyectil= [
	negro,negro,negro,negro,negro,negro,negro,negro,negro,negro,
	negro,plomo,plomo,plomo,plomo,plomo,plomo,plomo,plomo,negro,
	negro,plomo,dorad,plomo,plomo,plomo,plomo,plomo,plomo,negro,
	negro,plomo,plomo,dorad,dorad,plomo,plomo,dorad,plomo,dorad,
	negro,plomo,plomo,plomo,dorad,plomo,plomo,plomo,dorad,negro,
	negro,plomo,plomo,plomo,plomo,dorad,plomo,plomo,plomo,negro,
	negro,plomo,plomo,plomo,plomo,plomo,plomo,plomo,plomo,negro,
	negro,plomo,dorad,plomo,plomo,dorad,plomo,dorad,plomo,dorad,
	negro,plomo,plomo,plomo,plomo,plomo,plomo,plomo,plomo,negro,
	negro,negro,negro,negro,negro,negro,negro,negro,negro,negro
	]
	#animacion
	for j in range(1,size):
		for i in range(100):
			xf = x+(Puntos_Proyectil[i][0]*j)
			yf = y+(Puntos_Proyectil[i][1]*j)
			R = Colores_Proyectil[i][0]
			G = Colores_Proyectil[i][1]
			B = Colores_Proyectil[i][2]
			set_pixel(xf,yf,R,G,B,j)
			pygame.time.wait(1)
def Correcto(x, y, size):
	Puntos_Proyectil = [
	(-5, 7), (-4, 7), (-3, 7), (-2, 7), (-1, 7), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
	(-5, 6), (-4, 6), (-3, 6), (-2, 6), (-1, 6), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), 
	(-5, 5), (-4, 5), (-3, 5), (-2, 5), (-1, 5), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), 
	(-5, 4), (-4, 4), (-3, 4), (-2, 4), (-1, 4), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), 
	(-5, 3), (-4, 3), (-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
	(-5, 2), (-4, 2), (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), 
	(-5, 1), (-4, 1), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
	(-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), 
	(-5, -1),(-4, -1),(-3, -1),(-2, -1),(-1, -1),(0, -1),(1, -1),(2, -1),(3, -1),(4, -1),
	(-5, -2),(-4, -2),(-3, -2),(-2, -2),(-1, -2),(0, -2),(1, -2),(2, -2),(3, -2),(4, -2)
	]
	negro = (0.0,0.0,0)
	plomo = (139/255,69/255,19/255)
	dorad = (218/255,165/255,32/255)
	rojos = (1,0,0)
	Colores_Proyectil= [
	rojos,negro,negro,negro,negro,negro,negro,negro,negro,rojos,
	negro,rojos,plomo,plomo,plomo,plomo,plomo,plomo,rojos,negro,
	negro,plomo,rojos,plomo,plomo,plomo,plomo,rojos,plomo,negro,
	negro,plomo,plomo,rojos,dorad,plomo,rojos,dorad,plomo,dorad,
	negro,plomo,plomo,plomo,rojos,rojos,plomo,plomo,dorad,negro,
	negro,plomo,plomo,plomo,rojos,rojos,plomo,plomo,plomo,negro,
	negro,plomo,plomo,rojos,plomo,plomo,rojos,plomo,plomo,negro,
	negro,plomo,rojos,plomo,plomo,dorad,plomo,rojos,plomo,dorad,
	negro,rojos,plomo,plomo,plomo,plomo,plomo,plomo,rojos,negro,
	rojos,negro,negro,negro,negro,negro,negro,negro,negro,rojos
	]
	#animacion
	for i in range(100):
		xf = x+(Puntos_Proyectil[i][0]*size)
		yf = y+(Puntos_Proyectil[i][1]*size)
		R = Colores_Proyectil[i][0]
		G = Colores_Proyectil[i][1]
		B = Colores_Proyectil[i][2]
		set_pixel(xf,yf,R,G,B,size)
		pygame.time.wait(1)


def lowsito():
	pantalla = pygame.display.set_mode((450,300),0,32)
	pygame.display.set_caption("Modulo de fuentes")
	reloj = pygame.time.Clock()
	fuente = pygame.font.Font(None, 30)
	texto1 = fuente.render("         PERDISTE MANITO", 0, (255, 255, 255))
	texto2 = fuente.render("         TAS BAJO PRIMO", 0, (255, 255, 255))
	pygame.mixer.music.load("Game Over.mp3")
	pygame.mixer.music.play(1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main()
		reloj.tick(20)
		pantalla.blit(texto1, (100,100))
		pantalla.blit(texto2, (100,150))
		pygame.display.update()
def winner():
	pantalla = pygame.display.set_mode((450,300),0,32)
	pygame.display.set_caption("Modulo de fuentes")
	reloj = pygame.time.Clock()
	fuente = pygame.font.Font(None, 30)
	texto1 = fuente.render("            GANASTE ", 0, (255, 255, 255))
	texto2 = fuente.render("          ¿TAN FINO?", 0, (255, 255, 255))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main()
		reloj.tick(20)
		pantalla.blit(texto1, (100,100))
		pantalla.blit(texto2, (100,150))
		pygame.display.update()


def ValidarMovimiento(Pos,Rotacion,Limites,i,Mov):    
	TamanioSoldados = [(0,0),(0,0),(1,0),(1,0),(2,1)]
	if Mov=="U":
		if Rotacion==0:
			return Pos[1]+20+(TamanioSoldados[i][1]*20)>Limites[1][1]
		if Rotacion==2:
			return Pos[1]+20+(TamanioSoldados[i][0]*20)>Limites[1][1]
		else:
			return Pos[1]+20>Limites[1][1]
	elif Mov=="D":
		if Rotacion==1:
			return Pos[1]-20-(TamanioSoldados[i][1]*20)<Limites[0][1]
		if Rotacion==3:
			return Pos[1]-20-(TamanioSoldados[i][0]*20)<Limites[0][1]
		else:
			return Pos[1]-20<Limites[0][1]
	elif Mov=="R":
		if Rotacion==0:
			return Pos[0]+20+(TamanioSoldados[i][0]*20)>Limites[1][0]
		if Rotacion==2:
			return Pos[0]+20+(TamanioSoldados[i][1]*20)>Limites[1][0]
		else:
			return Pos[0]+20>Limites[1][0]
	else:
		if Rotacion==1:
			return Pos[0]-20-(TamanioSoldados[i][0]*20)<Limites[0][0]
		if Rotacion==3:
			return Pos[0]-20-(TamanioSoldados[i][1]*20)<Limites[0][0]
		else:
			return Pos[0]-20<Limites[0][0]

def ValidarRotacion(Pos,Limites,Rotacion,i):
	Limites = [(-80,40),(80,120)]
	if i==1 or i==0:
		return True
	if Rotacion==0:
		if i==2 or i==3:
			return (Pos[0]-20 >= -80)
		else:
			return (Pos[0]-40>= -80 and Pos[1] -20>= 40)
	elif Rotacion==1:
		if i==2 or i==3:
			return (Pos[1]+20<=120)
		else:
			return (Pos[1]+40<=120 and Pos[0] +20<=80)
	elif Rotacion==2:
		if i==2 or i==3:
			return (Pos[1]-20>=40)
		else:
			return (Pos[0]-20>=-80 and Pos[1]-40>=40)
	else:
		if i==1 or i==2:
			return (Pos[0]+20<=80)
		else:
			return (Pos[0]+40<=80 and Pos[1] +20<=120)

def main():
	scale = 2
	scalefondo = 40
	TurnoMaquina = False
	width, height = scale * 300, scale * 300
	i=0
	Limites = [(-80,40),(80,120)]
	pygame.init()
	pygame.display.set_caption('C.G. I')

	display_openGL(width, height, scale)
	glClearColor(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT)
	pygame.mixer.music.load("8 Bit Tribute to Russia.mp3")
	pygame.mixer.music.play(1)
	a = [[False,False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False,False]]
	Memoria_Ataque_Usuario = [
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False]
	]
	Memoria_Ataque_PC = [
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False,False,False]
	]

	x = random.randint(1,5)
	MatrizEnemiga = MatrizParaEnemigos(x)
	# -------
	# Point (pixel)
	# -------
	xmapa = 0
	ymapa = 0
	x = -80
	y = 40
	MovCostados = 0
	MovAltura = 4
	# -------
	# Transformation
	# -------
	# ---------------------------------------------------------
	PintarMapa(xmapa,ymapa,scalefondo)
	PintarMapa2(xmapa,ymapa,scalefondo)
	PintarUnidad1(x,y,0,False,scale)
	POSALIDOS=[]
	VIVOSALIDOS=[]
	for i in range (5):
		Rotacion=0
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT :
					cursorPosicionamiento = [x,y]
					if ValidarMovimiento(cursorPosicionamiento,Rotacion,Limites,i,"L"):
    						print("Salio del mapa")
					else:
						x-=20
						if (MovCostados >= 0):
							if (i<=1):
								PintarUnidad1(x+20,y,Rotacion,True,scale)
								PintarUnidad1(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados] = False
								a[MovAltura][MovCostados-1] = True
							elif (i>=2 and i<4):
								PintarUnidad2(x+20,y,Rotacion,True,scale)
								PintarUnidad2(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura][MovCostados-1]=True
								a[MovAltura][MovCostados]=True
							elif (i == 4):
								PintarUnidad3(x+20,y,Rotacion,True,scale)
								PintarUnidad3(x,y,Rotacion,False,scale)
								a[MovAltura-1][MovCostados]=False
								a[MovAltura-1][MovCostados+1]=False
								a[MovAltura-1][MovCostados+2]=False
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura][MovCostados+2]=False
								a[MovAltura-1][MovCostados-1]=True
								a[MovAltura-1][MovCostados]=True
								a[MovAltura-1][MovCostados+1]=True
								a[MovAltura][MovCostados-1]=True
								a[MovAltura][MovCostados]=True
								a[MovAltura][MovCostados+1]=True
							else:
								print ("Alto ya no puedes pasar")
							MovCostados -= 1
					print("IZQUIERDA")
				elif event.key == pygame.K_RIGHT:
					cursorPosicionamiento = [x,y]
					if ValidarMovimiento(cursorPosicionamiento,Rotacion,Limites,i,"R"):
						print("Salio del mapa")
					else:
						x+=20
						if(MovCostados <= 9):
							if (i<=1):
								PintarUnidad1(x-20,y,Rotacion,True,scale)
								PintarUnidad1(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados] = False
								a[MovAltura][MovCostados+1] = True
							elif (i>=2 and i<4):
								PintarUnidad2(x-20,y,Rotacion,True,scale)
								PintarUnidad2(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura][MovCostados+1]=True
								a[MovAltura][MovCostados+2]=True
							elif (i == 4):
								PintarUnidad3(x-20,y,Rotacion,True,scale)
								PintarUnidad3(x,y,Rotacion,False,scale)
								a[MovAltura-1][MovCostados]=False
								a[MovAltura-1][MovCostados+1]=False
								a[MovAltura-1][MovCostados+2]=False
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura][MovCostados+2]=False
								a[MovAltura-1][MovCostados+1]=True
								a[MovAltura-1][MovCostados+2]=True
								a[MovAltura-1][MovCostados+3]=True
								a[MovAltura][MovCostados+1]=True
								a[MovAltura][MovCostados+2]=True
								a[MovAltura][MovCostados+3]=True
							else:
								print ("Alto ya no puedes pasar")
							MovCostados += 1
					print("DERECHA")
				elif event.key == pygame.K_UP :
					cursorPosicionamiento = [x,y]
					if ValidarMovimiento(cursorPosicionamiento,Rotacion,Limites,i,"U"):
						print("Salio del mapa")
					else:
						y+=20
						if(MovAltura >= 0):
							if (i<=1):
								PintarUnidad1(x,y-20,Rotacion,True,scale)
								PintarUnidad1(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados] = False
								a[MovAltura-1][MovCostados] = True
							elif (i>=2 and i<4):
								PintarUnidad2(x,y-20,Rotacion,True,scale)
								PintarUnidad2(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura-1][MovCostados]=True
								a[MovAltura-1][MovCostados+1]=True
							elif (i == 4):
								PintarUnidad3(x,y-20,Rotacion,True,scale)
								PintarUnidad3(x,y,Rotacion,False,scale)
								a[MovAltura-1][MovCostados]=False
								a[MovAltura-1][MovCostados+1]=False
								a[MovAltura-1][MovCostados+2]=False
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura][MovCostados+2]=False
								a[MovAltura-2][MovCostados]=True
								a[MovAltura-2][MovCostados+1]=True
								a[MovAltura-2][MovCostados+2]=True
								a[MovAltura-1][MovCostados]=True
								a[MovAltura-1][MovCostados+1]=True
								a[MovAltura-1][MovCostados+2]=True
							else:
								print ("Alto ya no puedes pasar")
							MovAltura -= 1
					print("ARRIBA")
				elif event.key == pygame.K_DOWN :
					cursorPosicionamiento = [x,y]
					if ValidarMovimiento(cursorPosicionamiento,Rotacion,Limites,i,"D"):
						print("Salio del mapa")
					else:
						y-=20
						if(MovAltura <= 4):
							if (i<=1):
								PintarUnidad1(x,y+20,Rotacion,True,scale)
								PintarUnidad1(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados] = False
								a[MovAltura+1][MovCostados] = True
							elif (i>=2 and i<4):
								PintarUnidad2(x,y+20,Rotacion,True,scale)
								PintarUnidad2(x,y,Rotacion,False,scale)
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura+1][MovCostados]=True
								a[MovAltura+1][MovCostados+1]=True
							elif (i == 4):
								PintarUnidad3(x,y+20,Rotacion,True,scale)
								PintarUnidad3(x,y,Rotacion,False,scale)
								a[MovAltura-1][MovCostados]=False
								a[MovAltura-1][MovCostados+1]=False
								a[MovAltura-1][MovCostados+2]=False
								a[MovAltura][MovCostados]=False
								a[MovAltura][MovCostados+1]=False
								a[MovAltura][MovCostados+2]=False
								a[MovAltura][MovCostados]=True
								a[MovAltura][MovCostados+1]=True
								a[MovAltura][MovCostados+2]=True
								a[MovAltura+1][MovCostados]=True
								a[MovAltura+1][MovCostados+1]=True
								a[MovAltura+1][MovCostados+2]=True
							else:
								print ("Alto ya no puedes pasar")
							MovAltura+=1
					print("ABAJO")
				elif event.key == pygame.K_r :
					cursorPosicionamiento = [x,y]
					if ValidarRotacion(cursorPosicionamiento,Limites,Rotacion,i):
						if (i<=1):
							PintarUnidad1(x,y,Rotacion,True,scale)
							Rotacion=(Rotacion+1)%4
							PintarUnidad1(x,y,Rotacion,False,scale)
						elif (i>=2 and i<4):
							PintarUnidad2(x,y,Rotacion,True,scale)
							Rotacion=(Rotacion+1)%4
							PintarUnidad2(x,y,Rotacion,False,scale)
						elif (i == 4):
							PintarUnidad3(x,y,Rotacion,True,scale)
							Rotacion=(Rotacion+1)%4
							PintarUnidad3(x,y,Rotacion,False,scale)
						else:
							print ("Alto ya no puedes pasar")
					print("ROTACION")
				elif event.key == pygame.K_g :
					x=-80
					y=40
					Rotacion=0
					MovCostados = 0
					MovAltura = 4
					i+=1
					event.key = pygame.KEYUP
					print("FIJADO")
					if (i<=1):
						PintarUnidad1(x,y,0,False,scale)
						a[4][0]=True
						MostrarMatriz(a)
					elif (i>=2 and i<4):
						PintarUnidad2(x,y,0,False,scale)
						a[4][0]=True
						a[4][1]=True
						MostrarMatriz(a)
					elif (i == 4):
						PintarUnidad3(x,y,0,False,scale)
						a[3][0]=True
						a[3][1]=True
						a[3][2]=True
						a[4][0]=True
						a[4][1]=True
						a[4][2]=True
						MostrarMatriz(a)
					else:
						MostrarMatriz(a)
					print (i)


				elif event.key == pygame.K_a:#para player
					print("TURNO PLAYER")
					print("PLAYER JUGANDO")
					pos = pygame.mouse.get_pos()
					matrizX=(pos[0]//40)-3
					matrizY=(pos[1]//40)-9
					if(matrizX>=0 and matrizY >=0 and matrizX<9 and matrizY<5):
						Area_Atacada =  (Memoria_Ataque_Usuario[matrizY][matrizX])
						if(Area_Atacada == False):
							Memoria_Ataque_Usuario[matrizY][matrizX] = True
							x = ((pos[0])//40)*40-278
							y = ((-pos[1])//40)*40+310
							print("matrixx",matrizX)
							print("matrixy",matrizY)
							print("---")
							Proyectil(x,y,5)
							if MatrizEnemiga[matrizY][matrizX]==True:
								Correcto(x,y,4)
								MatrizEnemiga[matrizY][matrizX]=False
							print("MATRIZ PC LUEGO DE JUGADA DE PLAYER")
							MostrarMatriz(MatrizEnemiga)
							if RecorrerTrues(MatrizEnemiga)==0:
								print("Gano PLayer")
								winner()
								break
							TurnoMaquina = True
				if TurnoMaquina:#para pc
					Falta_Atacar = True
					print("TURNO PC")
					print("PC JUGANDO")
					while(Falta_Atacar):
						xx = random.randint(120,480)
						yy = random.randint(40,240)
						matrizX=((xx//40)-3)
						matrizY=(yy//40)-1
						Area_Atacada =  (Memoria_Ataque_PC[matrizY][matrizX])
						if(Area_Atacada == False):
							Memoria_Ataque_PC[matrizY][matrizX] = True
							x = ((xx//40)*40-278)
							y = (-yy//40)*40+310
							print("matrixx",matrizX)
							print("matrixy",matrizY)
							print("x",x)
							print("y",y)
							Proyectil(x,y,5)
							if a[matrizY][matrizX]==True:
								Correcto(x,y,4)
								print("LE ATINASTE!!")
								a[matrizY][matrizX]=False
							print("MATRIZ PLAYER LUEGO DE JUGADA DE PC")
							MostrarMatriz(a)
							if RecorrerTrues(a)==0:
								print("--Gano PC--")
								
								lowsito()
								break
							TurnoMaquina = False
							Falta_Atacar = False

		glFlush()
		#pygame.display.flip()
if __name__ == '__main__':
	main()