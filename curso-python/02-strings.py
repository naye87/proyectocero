texto="Hola Mundo"
print(texto.upper())#metodo es una funcion=objeto. para que el texto sea funcion se ingresa un punto, se despliegan funciones , despues parentesis.
 #shift + alt + flecha abajo duplica la linea
print(texto.lower()) #minusculas
print(texto.find("Mun")) #encontrar la posicion. 012345 buscador tipo indice
print(texto.find("Mun")) #importante mayusculas, te encuentra el mismo formato 
print(texto.replace("Mun","chanchito feliz"))#control+alt+3 reemplaza entre comillas y con coma
nuevotexto=texto.replace("Mun","chanchito feliz") #es un texto nuevo que copia el primero con modificación
print(texto, nuevotexto)#imprime muestra amos textos
print("Mundo" in texto) #(texto) es la variable en la que quiero buscar el texto Mundo, el resultado es boolean true o false, dependiendo si lo encontro donde le indicas.
