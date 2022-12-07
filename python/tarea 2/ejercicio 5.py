import random
n=[]
elementos=10
i=0
for i in range(elementos):
    n.append(random.randint(0,101))

print(f"los elementos del arreglo son \n {n}")
n.reverse()
print(f"en orden inverso \n {n}")