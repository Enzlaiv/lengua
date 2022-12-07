
acum = []
n = int(input("Ingrese la cantidad de datos: "))
i=0
while i<n:
	dato=float(input(f"Ingrese el dato {i+1} : "))
	acum.append(dato)
	i+=1
promedio=sum(acum)/len(acum)

print("El promedio es: ",promedio)
