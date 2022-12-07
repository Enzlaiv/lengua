def saludar():
    print("estoy saludando")
def doble_valor(x):
    print(x*2)
def triple_valor(x):
    print(x*3)

print("llamando a la funcion saludar")
saludar

x=int(input("ingrese valor para x :"))

print("llamando a la funcion doble_valor")
doble_valor
print (f"el doble de {x} es {doble_valor(x)}")
print(f"el valor original de x es {x}")

print("llamando a la funcion triple_valor")
triple_valor
print(f"entonces el nuevo valor de x es {triple_valor(x)}")




