import math

#Val = Numero de digitos despues del decimal.

val = input ("Ingrese el numero de digitos:");
valInt = int(val);

#Redondeo Pi a 8 decimales
piRound = round(math.pi,8)
piStr = str(piRound);

#Pi a string y se toma el tamano total de caracteres
piLenth = len(piStr)

#Se resta al total de caracters el numero de digitos ingresados
decimal = (piLenth - valInt);

#Se multiplica "*" por el numero de digitos ingresados
asterix = valInt*"*";

#Variable 'resultado' es un string con un valor numeral
resultado = "El resultado es: %." + str(decimal)+"s"


print( str(resultado) % piStr, asterix);


