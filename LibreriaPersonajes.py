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
	Colores_Soldado12 = [
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
		R = Colores_Soldado12[i][0]
		G = Colores_Soldado12[i][1]
		B = Colores_Soldado12[i][2]
		set_pixel(x,y,R,G,B,size)
	return
def PintarUnidad3(x, y, size):
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
	plomo = (0.75,0.75,0.75)
	plom2 = (0.41,0.41,0.41)
	Colores_Soldado12 = [
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

	for i in range(184):
		x = Puntos_Soldado1[i][0]*size
		y = Puntos_Soldado1[i][1]*size
		R = Colores_Soldado12[i][0]
		G = Colores_Soldado12[i][1]
		B = Colores_Soldado12[i][2]
		set_pixel(x,y,R,G,B,size)
	return


def main():
	scale = 14
	width, height = scale * 40, scale * 40

	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	glClearColor(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT)
	# -------
	# Point (pixel)
	# -------
	x =10
	y =0

	# -------
	# Transformation
	# -------
	Colores_Soldado1 = [(0,1,2),(4,5,6)

		]
	#DrawPolygon_(vertices_p1, 255/255, 0/255, 0/255, scale)
	# print(vertices_p1)
	# ---------------------------------------------------------
	PintarUnidad3(x,y,scale)
	#PintarUnidad3(x,y,scale)
	#PintarUnidad1(30,-70,scale)
	#PintarUnidad1(-30,-60,scale)
	#PintarUnidad1(-30,-60,scale)
	#PintarUnidad1(-30,-60,scale)
	#PintarUnidad1(-30,-60,scale)
	#PintarUnidad1(-30,-60,scale)
	#PintarUnidad1(-30,-60,scale)
	#glOrtho( GLdouble ( left ) , GLdouble ( right ) , GLdouble ( bottom ) , GLdouble ( top ) , GLdouble ( nearVal ) , GLdouble ( farVal ) )
	#glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	print("Finish...")
	glFlush()
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return None
		#pygame.display.flip()
if __name__ == '__main__':
	main()