#Eliminar una palabra de una cadena de caracteres
t="Eliminar palabras"
print ("============================================")
print ("=", t.center(40), "=")
print ("============================================ \n")
p=input("Ingrese una cadena de caracteres: ")
#cp="Siempre se puede cuando se quiere"
#sc="cuando"
sc=input("Ingrese que quiere eliminar: ")
f=p.find(sc)
c=sc.count("")
c2=p.count("")
print (p[0:f-1], p[f+c:c2])
