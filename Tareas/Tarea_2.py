lista=[]

for x in range (5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

#suma= sum(valor);
#total=len(valor)
    
total= sum(lista)/float(len(lista))
                        
print("El promedio es:"+ str(total))

#/len(valor))

