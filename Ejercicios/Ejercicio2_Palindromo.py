pal = input("Ingrese primera palabra:");
pal2 = input ("Ingrese segunda palabra:");

lista1 = list(pal);
lista2 = list(pal2);

lista1.sort();
lista2.sort();

if lista1==lista2:
        print ("palabra es un palindromo");
else:
        print ("palabra no es un palindromo");   
    



