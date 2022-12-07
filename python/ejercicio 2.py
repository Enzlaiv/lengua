import time

#OP=OPCION DE RECOMENDACIONES

op=int(input("menu de recomendaciones: \n 1. literatura \n 2. cine \n 3- musica \n 4. videojuegos \n 5.salir  \n Elija una opcion (1-5): "))

while op !=0:

	if op==1:
		print("Lecturas recomendables:")
		print(" + Esperandolo a Tito y otros cuentos de fubol (Eduardo Sacheri)")
		print(" + El juego de Ender (Orson Scott Card)")
		print(" + El sueño de los heroes (Adolfo Bioy Casares)")
	elif op==2:
		print("Peliculas recomendables:")
		print(" + Matrix (1999)")
		print(" + El ultimo samuray (2003)")
		print(" + Cars (2006)")
	elif op==3:
		print("Discos recomendables:")
		print(" + Despedazado por mil partes (La Renga, 1996)")
		print(" + Bufalo (La Mississippi, 2008)")
		print(" + Gaia (Mago de Oz, 2003)")
	elif op==4:
		print("Videojuegos clasicos recomendables")
		print(" + Dia del tentaculo (LucasArts, 1993)")
		print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
		print(" + Death Rally (Remedy/Apogee, 1996)")
	elif op==5:
		print("Gracias, vuelva prontos")
		
	else:
		print("Opcion no valida")
	print("-----volviendo al menu principal...---")
	time.sleep(5)
	op=int(input("menu de recomendaciones: \n 1. literatura \n 2. cine \n 3- musica \n 4. videojuegos \n 5.salir  \n Elija una opcion (1-5): "))

else:
    print("opcion fuera de rango")