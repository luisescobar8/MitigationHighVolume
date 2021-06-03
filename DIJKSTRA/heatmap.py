import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import random

matrixLinks = [ None for i in range(16) ]
bandwidth = [ None for i in range(16) ]
linksA = []

for i in range(16):
    linksA = str(i)
    matrixLinks[i] = "Switch " + linksA 
    bandwidth[i] = random.randint(10, 100)


for i, v in enumerate(bandwidth):
    plt.text(v, i, str(v), color='black')

y_pos = np.arange(len(bandwidth))
plt.barh(y_pos, bandwidth, align='center', alpha=0.5)
plt.yticks(y_pos, matrixLinks)

plt.ylabel("Links")
plt.xlabel('Bandwidth')
plt.title('Bandwidth Links')
plt.show()



# lenguajes = &#91;['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
# #Obtenemos una lista con las posiciones de cada lenguaje, ejemplo 0, 1, 2, 3.....
# y_pos = np.arange(len(lenguajes))
 
# #Ahora obtenemos la cantidad de usos de cada lenguaje
# cantidad_usos = &#91;10,8,6,4,2,1]
 
# #Creamos la grafica pasando los valores en el eje X, Y, donde X = cantidad_usos y Y = lenguajes
# plt.barh(y_pos, cantidad_usos, align='center', alpha=0.5)
# #Añadimos la etiqueta de nombre de cada lenguaje en su posicion correcta
# plt.yticks(y_pos, lenguajes)
# #añadimos una etiqueta en el eje X
# plt.xlabel('Usuarios')
# #Y una etiqueta superior
# plt.title('Lenguajes Mas Usados En El Año')
# plt.savefig('barras_horizontal.png')
# plt.show()

