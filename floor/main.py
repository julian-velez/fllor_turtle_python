# Importa todas las funciones de turtle (para dibujar)
from turtle import *

# Importa colorsys para trabajar con colores en formato HSV
import colorsys as cs

# Acelera el dibujo (mientras más alto, más rápido)
tracer(40)

# Establece el color de fondo en negro
bgcolor('black')

# Oculta la flecha (tortuga) para que solo se vea el dibujo
hideturtle()

# Define el grosor del lápiz
pensize(6)

# Variable para manejar el tono del color (Hue en HSV)
h = 0.6

# Bucle que se repite 200 veces para crear el patrón
for i in range(200):

    # Convierte el color de HSV a RGB y lo aplica
    # h cambia para generar diferentes colores (efecto arcoíris)
    color(cs.hsv_to_rgb(h, 1, 1))

    # Incrementa el tono para el siguiente color
    h += 0.06

    # Dibuja un arco de círculo (cada vez más grande)
    circle(i * 0.5, 190)

    # Gira a la derecha 80 grados
    right(80)

    # Dibuja otro arco de círculo
    circle(i * 0.5, 190)

    # Gira a la izquierda 80 grados
    left(80)

    # Avanza hacia adelante aumentando la distancia progresivamente
    forward(i * 0.5)

    # Gira a la derecha 60 grados
    right(60)

# Mantiene la ventana abierta hasta que la cierres
done()