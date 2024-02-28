print ("===========================")
print ("=  Sucesión de fibonacci  =")
print ("===========================")
#Sucesión de fibonacci del 0 al 1597
x, y = 0, 1
while x<1500:
	print (x, y, end=" ")
	x=x+y
	y=y+x
print ("")
