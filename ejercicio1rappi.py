#Ejercicio 1: sistema de vacaciones de rappi con entrada de datos
print ("=======================================================")
print ("     Bienvenido al sistema de vacaciones de rappi")
print ("======================================================= \n")
print ("Ingrese los datos solicitados")
n = input("Nombre: ")
c = int(input("Clave del departamento: "))
a = float(input("Años de servicio: "))
#No tiene ningun año en la empresa
if a<1:
	print (n, "no tienes derecho a vacaciones")
#Clave 1
if c==1:
	if a>=1 and a<2:
		print ("Hola", n, "tiene 6 días de vacaciones")
	elif a>=2 and a<=6:
		print ("Hola", n, "tiene 14 días de vacaciones")
	elif a>=7:
		print ("Hola", n, "tiene 20 días de vacaciones")
#Clave 2
elif c==2:
	if a>=1 and a<2:
		print ("Hola", n, "tiene 7 días de vacaciones")
	elif a>=2 and a<=6:
		print ("Hola", n, "tiene 15 días de vacaciones")
	elif a>=7:
		print ("Hola", n, "tiene 22 días de vacaciones")
#Clave 3
elif c==3:
	if a>=1 and a<2:
		print ("Hola", n, "tiene 10 días de vacaciones")
	elif a>=2 and a<=6:
		print ("Hola", n, "tiene 20 días de vacaciones")
	elif a>=7:
		print ("Hola", n, "tiene 30 días de vacaciones")
#Si ingresa un numero diferente
else:
	print ("La clave no existe")
