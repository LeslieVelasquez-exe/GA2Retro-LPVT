#RETROALIMENTACIÓN GA2
#Análisis de Sistemas
#Leslie Pamela Velásquez Tzarax (29)

#8. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
#porcentual anual y el número de años, y muestre por pantalla el capital
#obtenido en la inversión redondeado con dos decimales.

cantidad = float(input("¿Cantidad a invertir?")) #Guardamos en una variable la cantidad ingresada para invertir en float.
interes = float(input("¿Interés porcentual anual?")) #Guardamos igualmente en float el interés ingresado por el usuario.
años = int(input("¿Años?")) #Guardamos la cantidad de años con int, que haya ingresado el usuario.

#Realizamos la operación correspondiente, redondeamos y concatenamos pasándolo a String para imprimirlo.
print("Capital final: " + str(round(cantidad * (interes/100+1) ** años, 2)))