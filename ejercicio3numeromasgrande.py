print ("======================================")
print ("         Número más grande")
print ("====================================== \n")
print ("Escribe 3 números enteros")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
if n1>n2 and n1>n3:
	print (n1, "es mayor")
elif n2>n3:
	print (n2, "es mayor")
else:
	print (n3, "es mayor")
