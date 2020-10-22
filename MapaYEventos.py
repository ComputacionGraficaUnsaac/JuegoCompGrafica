def PintarMapa(x, y, size):
	Puntos_Mapa = [
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
	]

	for i in range(36):
		x = Puntos_Mapa[i][0]*size
		y = Puntos_Mapa[i][1]*size
		R = Colores_Fondo[i][0]
		G = Colores_Fondo[i][1]
		B = Colores_Fondo[i][2]
		set_pixel(x,y,R,G,B,size)
	return
def PintarMapa2(x, y, size):
	Puntos_Mapa = [
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
	]

	for i in range(36):
		x = Puntos_Mapa[i][0]*size
		y = Puntos_Mapa[i][1]*size
		R = Colores_Fondo[i][0]
		G = Colores_Fondo[i][1]
		B = Colores_Fondo[i][2]
		set_pixel(x,y,R,G,B,size)
	return

def main():
	scale = 2
	scalefondo = 50
	width, height = scale * 300, scale * 300
	i=0
	
	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	glClearColor(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT)
	# -------
	# Point (pixel)
	# -------
	xmapa = 0
	ymapa = 0
	x = -100
	y = 120
	# -------
	# Transformation
	# -------
	# ---------------------------------------------------------
	PintarMapa(xmapa,ymapa,scalefondo)
	PintarMapa2(xmapa,ymapa,scalefondo)
	PintarUnidad1(x,y,scale)
	Sprites = []
	for i in range (5):
		if (i<=1):
			PintarUnidad1(x,y,scale)
		elif (i>=2 and i<4):
			PintarUnidad1(x,y,scale)
		else:
			PintarUnidad3(x,y,scale)
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					return

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT :
					x-=20
					if (i<=1):
						PintarUnidad1(x,y,scale)
					elif (i>=2 and i<4):
						PintarUnidad1(x,y,scale)
					else:
						PintarUnidad3(x,y,scale)
					print("IZQUIERDA")
				elif event.key == pygame.K_RIGHT:
					x+=20
					if (i<=1):
						PintarUnidad1(x,y,scale)
					elif (i>=2 and i<4):
						PintarUnidad1(x,y,scale)
					else:
						PintarUnidad3(x,y,scale)
					print("DERECHA")
				elif event.key == pygame.K_UP :
					y+=20
					if (i<=1):
						PintarUnidad1(x,y,scale)
					elif (i>=2 and i<4):
						PintarUnidad1(x,y,scale)
					else:
						PintarUnidad3(x,y,scale)
					print("ARRIBA")
				elif event.key == pygame.K_DOWN :
					y-=20
					if (i<=1):
						PintarUnidad1(x,y,scale)
					elif (i>=2 and i<4):
						PintarUnidad1(x,y,scale)
					else:
						PintarUnidad3(x,y,scale)
					print("ABAJO")
				elif event.key == pygame.K_r :
					print("ROTACION")
				elif event.key == pygame.K_g :
					print("FIJADO")
					x=-100
					y=120
					i+=1
			glFlush()
		#pygame.display.flip()
if __name__ == '__main__':
	main()