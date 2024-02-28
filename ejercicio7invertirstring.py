#invertir una cadena de carateres ingresada por teclado
print ("===========================================")
print ("=", "Invertir cadenas".center(40), "=")
print ("===========================================")
c=input("Ingresa una cadena: ")
#c="Hola"
inv=""
for i in c:
	inv=i+inv
print(inv)
