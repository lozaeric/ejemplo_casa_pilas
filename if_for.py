### for ###
# horas del dia

for hs in range(0,24):
    print ("Son las "+str(hs)+" horas")


print()
print()


### if ###

# noche
print ("Anochece")
es_noche = True
es_dia = False
if es_dia:
    print ("Es de dia y hay un sol radiante")
if es_noche:
    print ("Es de noche y podemos observar la luna")
    
# dia
print ("Amanece") 
es_noche = False
es_dia = True
if es_dia:
    print ("Es de dia y hay un sol radiante")
if es_noche:
    print ("Es de noche y podemos observar la luna")


print()
print()


### if y for ###

for hs in range(0,24):
	print ("Son las "+str(hs)+" horas")
	if hs == 7:
		es_dia = False
		es_noche = True
		print ("Amanece")
	if hs == 19:
		es_dia = True
		es_noche = False
		print ("Anochece")

