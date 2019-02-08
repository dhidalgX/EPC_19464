def suma(a,b):
         print (("el resultado es:") + str(a+b))
def resta(a,b):
        print (("el resultado es:") + str(a-b))

def mult(a,b):
        print (("el resultado es:") + str(a*b))

def div(a,b):
        print (("el resultado es:") + str(a/b))

def menu():
        print ("************")
        print ("Calculadora")
        print ("************")
        print ("Seleciona una opcion:")
        print ("1) Suma")
        print ("2) Resta")
        print ("3) Multiplicacion")
        print ("4) Division """)
        print ("0) Salir")
        return int(input("opcion : "))

while(True):
        opcion = menu()
        if(opcion==0):
            break

        else:

                num = int(input("Ingrese el primer numero: "))
                den = int(input("Ingrese el segundo numero: "))

                if(opcion==1):
                        suma(num,den)
                elif(opcion==2):
                        resta(num,den)
                elif(opcion==3):
                        mult(num,den)
                elif(opcion==2):
                        div(num,den)
    
