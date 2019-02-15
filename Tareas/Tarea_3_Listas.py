#class Menu:
def menu ():
#def menu(self):
#menu = str(value)
    print ("            ")
    print ("************")
    print ("Que deseas hacer?")
    print ("************")
    print ("Seleciona una opcion:")
    print ("1) Mostrar todas las listas")
    print ("2) Cantidad de palabras de una lista")
    print ("3) Repeticion de palabras en la lista")
    print ("4) Susticion de palabras en una lista")
    print ("5) Eliminar palabra ")
    print ("6) Eliminar elementos repetidos ")
    print ("7) ")
    print ("8) Copiar lista")
    print ("9) Cambiar posicion de nombre de lista")
    print ("0) Salir")
    return int(input("opcion : "))

#class operacion:

listaX = []
def lista(a,b):
    for i in range(a):
            x=str(b) 
            listaX.insert(i,x)
            contador+=1
            i+=1   
    print (str(listaX))
     
def numero(a,b):
    print (("La cantidad de palabras de la lista es: "), str(len(a[b])))


def search(a,b,c):
    cuenta = int(a[b].count(c))
    print ("La palabra ", str(c), " aparece ", str(cuenta), " vez en el indice ", str(b))

def sust(a,b,c):
    for i in range(len(lista[c])):     
        if lista[c][i] == a:
            lista[c][i] = b                                 
    print("La lista ahora es:", lista[c])

def elim(a,b):
    lista[b].remove(str(a))                 
    print("La lista ahora es:", lista[b])

    
def rep(a,b):
    while lista[b].count(a)>0:
        lista[b].remove(str(a))           
    print("La lista ahora es:", lista[b])
    
lista = []
contador = 0
for x in range(int(input("Ingrese cantidad de listas: "))):
        lista2=[] 
        for i in range(int(input("Ingrese cantidad de nombres para lista: "))):
            x=str(input("Ingresar Nombre: ")) 
            lista2.insert(i,x)
            contador+=1
            i+=1
        lista.append(lista2)

#opcion = menu()
while(True):
        
        opcion = menu()      
        if(opcion==0):
            print ("byeee...")
            break

        else:
             if(opcion==1):
                print ("El contenido de las listas es: " ,lista)
              
             elif(opcion==2):
                index = int(input("Ingrese el indice: "))
                numero(lista,index)

                
             elif(opcion==3):
                palabra = str(input("Palabra a buscar: "))
                indice = int(input("En cual indice desea buscar: "))
                search(lista,indice,palabra)

             elif(opcion==4): 
                buscar = input("Sustituir la palabra: ")
                sustituir = input("por la palabra: ")
                indice = int(input("En cual indice desea ejecutar: "))
                sust(buscar,sustituir,indice)
                
             elif(opcion==5):
                pala = input("Palabras a eliminar: ")
                indice = int(input("En cual indice desea ejecutar: "))
                elim(pala,indice)

             elif(opcion==6):
                pala = input("Palabras a eliminar: ")
                indice = int(input("En cual indice desea ejecutar: "))
                elim(pala,indice)

      
