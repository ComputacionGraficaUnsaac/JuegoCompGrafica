# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from utils import *
from numba import jit

def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	
	pygame.display.flip()
	glFlush()
def PintarUnidad1(x, y, size):
	Puntos_Soldado1 = [
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

	for i in range(184):
		x = Puntos_Soldado1[i][0]*size
		y = Puntos_Soldado1[i][1]*size
		R = Colores_Soldado1[i][0]
		G = Colores_Soldado1[i][1]
		B = Colores_Soldado1[i][2]
		set_pixel(x,y,R,G,B,size)
	return


def PintarUnidad2(x, y, size):
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

	for i in range(292):
		x = Puntos_Soldado2[i][0]*size
		y = Puntos_Soldado2[i][1]*size
		R = Colores_Soldado2[i][0]
		G = Colores_Soldado2[i][1]
		B = Colores_Soldado2[i][2]
		set_pixel(x,y,R,G,B,size)

	return


def PintarUnidad3(x, y, size):
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

	Mortero = [
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

	for i in range(184):
		x = Puntos_Soldado3[i][0]*size
		y = Puntos_Soldado3[i][1]*size
		R = Colores_Soldado3[i][0]
		G = Colores_Soldado3[i][1]
		B = Colores_Soldado3[i][2]
		set_pixel(x,y,R,G,B,size)
	for i in range(685):
		x = Mortero[i][0]*size
		y = Mortero[i][1]*size
		R = Colores_Mortero[i][0]
		G = Colores_Mortero[i][1]
		B = Colores_Mortero[i][2]
		set_pixel(x,y,R,G,B,size)
	return

def main():
	scale = 10
	width, height = scale * 120, scale * 100

	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	glClearColor(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT)
	# -------
	# Point (pixel)
	# -------
	x1 = -30
	y1 = 30
	x2 = 20
	y2 =30
	x3 = -15
	y3 = -20
	PintarUnidad1(x1,y1,scale)
	PintarUnidad2(x2,y2,scale)
	PintarUnidad3(x3,y3,scale)
	print("Finish...")
	glFlush()
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return None
		#pygame.display.flip()
if __name__ == '__main__':
	main()