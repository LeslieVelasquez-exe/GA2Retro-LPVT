#RETROALIMENTACIÓN GA2
#Análisis de Sistemas
#Leslie Pamela Velásquez Tzarax (29)

#9. Una juguetería tiene mucho éxito en dos de sus productos: payasos y
#muñecas. Suele hacer venta por correo y la empresa de logística les cobra por
#peso de cada paquete así que deben calcular el peso de los payasos y
#muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y
#muñecas vendidos en el último pedido y calcule el peso total del paquete que
#será enviado.

peso_payaso = 112 #Guardamos el peso del payaso.
peso_muñeca = 75 #Guardamos el peso de la muñeca.

payasos = int(input("Introduce el número de payasos a enviar: ")) #Guardamos con int el número de payasos
muñecas = int(input("Introduce el número de muñecas a enviar: ")) #Guardamos con int el número de muñecas
peso_total = peso_payaso * payasos + peso_muñeca * muñecas #Calculamos el peso total multiplicando la cantidad por su peso.

print("El peso total del paquete es: " + str(peso_total)) #Imprimimos el resultado.