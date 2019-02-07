
lista = []
for x in range(2):
    lista2=[] 
    for i in range (3):
        x=int(input("Ingrese un la altura de la persona:")) 
        lista2.insert(i,x)
        i+=1
    lista.append(lista2)

maximo= max(*lista)


print (str("El indice con la mayor altura, es el:") + str(lista.index(maximo)))
