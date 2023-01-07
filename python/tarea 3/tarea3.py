
sum = 0
rest = 0
multi = 0
div = 0
cont_sum = 0
cont_rest = 0
cont_multi = 0
cont_div = 0

while (True):
  print("MENÚ")
  print("1. Realizar una suma")
  print("2. realizar una resta")
  print("3. realizar una multiplicacion")
  print("4. realizar una division")
  print("5. mostrar detalladamente los valores ingresados")
  print("6. cerrar programa")
  opc = int(input("Escoja una opción: "))
  if (opc == 1):
    a = int(input("ingrese el primer valor de la suma : "))
    b = int(input("ingrese el segundo valor de la suma: "))
    resol = a + b
    print("La suma de ", a, " + ", b, " es igual a ", resol)
    sum = sum + resol
    cont_sum = cont_sum + 1
  elif (opc == 2):
    a = int(input("ingrese el primer valor de la resta :"))
    b = int(input("ingrese el segundo valor de la resta :"))
    resol = a - b
    print("La resta de ", a, " - ", b, " es igual a ", resol)
    rest = rest + resol
    cont_rest = cont_rest + 1
  elif (opc == 3):
    a = int(input("ingrese el primer valor de la multiplicacion : "))
    b = int(input("ingrese el segundo valor de la multiplicacion :"))
    resol = a * b
    print("La multiplicacion de ", a, " X ", b, " es igual a ", resol)
    multi = multi + resol
    cont_multi = cont_multi + 1

  elif (opc == 4):
    a = int(input("ingrese el primer valor de la division : "))
    b = int(input("ingrese el segundo valor de la division : "))

    resol = a / b
    print(f"la division de {a} entre {b} es {resol}")
    div = div + resol
    cont_div = cont_div + 1
  elif (opc == 5):
      print("_______________________________________________________________")
    print("|              | * El acumulativo de las operciones es ",sum,)
    print("|     SUMA     | * Esta operación se uso ",cont_sum," veces")
    print("|              | * El número de digitos es : ",len(str(sum)))
    
    print("|              | * El acumulativo de las operciones es ",rest,)
    print("|     RESTA    | * Esta operación se uso ",cont_rest," veces")
    print("|              | * El número de digitos es : ",len(str(rest)))

    print("|              | * El acumulativo de las operciones es ",multi,)
    print("|MULTIPLICACIÓN| * Esta operación se uso ",cont_multi," veces")
    print("|              | * El número de digitos es : ",len(str(multi)))

    print("|              | * El acumulativo de las operciones es ",div,)
    print("|   DIVISIÓN   | * Esta operación se uso ",cont_div," veces")
    print("|              | * El número de digitos es : ",len(str(div)))


    
  elif (opc == 6):
    print("GRACIAS POR PARTICIPAR, BUEN DÍA")
    break
  else:
    print("OPCIÓN INVALIDA !!!, INTENTELO NUEVAMENTE.")
