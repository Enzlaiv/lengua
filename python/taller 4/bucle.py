
sum=0
cont_sum=0
a=int(input("ingrese el primer valor de la sume: "))
b=int(input("ingrese el segundo valor de la sume: "))

while a!=0:
    resol=a+b
    print("la suma de " ,a, " + " ,b," es igual a " , resol)
    sum=sum+resol
    cont_sum=cont_sum+sum   
    print("la suma total es", sum)
    print("esta operacion se uso", cont_sum,"veces")
    a=int(input("ingrese el primer valor de la sume: "))
    b=int(input("ingrese el segundo valor de la sume: "))