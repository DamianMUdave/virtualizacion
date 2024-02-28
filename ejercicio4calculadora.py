print ("============================")
print ("= Calculadora de 2 digitos =")
print ("============================ \n")
print ("""
1.-Suma
2.-Resta
3.-Multiplicación
4.-División
5.-Exponencial \n
""")
o = float(input("Que operación vas a realizar: "))
if o<1 or o>5:
	print ("Inserte una opción valida")
else:
	print (o)
	n1 = float(input("Introduce el primer número: "))
	n2 = float(input("Introduce en segundo número: "))
	print (o)
	#Suma
	if o>=1 and o<2:
		o=n1+n2
		print ("La suma es:", o)
	#Resta
	elif o>=2 and o<3:
		o=n1-n2
		print ("La resta es:",o)
	#Multiplicación
	elif o>=3 and o<4:
		o=n1*n2
		print ("La multiplicación es:", o)
	#División
	elif o>=4 and o<5:
		o=n1/n2
		print ("La división es:", o)
		o=n1%n2
		print ("Su residuo es:", o)
	#Exponencial
	elif o>=5 and o<6:
		o=n1**n2
		print ("El número", n1, "elevado a", n2, "es igual a", o)
