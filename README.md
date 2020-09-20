# Laboratorio programado de transformaciones en OpenCV - Python
Primer laboratorio programado del curso de Introducción al Reconocimiento de Patrones

---
## Menú Principal

Al iniciar el programa se le muestra al usuario la lista de transformaciones disponibles además de la opción de detener el programa. Se espera en el menú a que el usuario ingrese un valor para ejecutar la opción seleccionada; en caso que ingrese una opción no valida se le indica el usuario y se le vuelve a mostrar el menú.

## Transform 1

La primera transformación consiste en cargar la iamgen, y extraer la información de los valores RGB de un pixel (x, y) brindado por el usuario
Se utiliza la sintaxis b, g, r = (img[x, y]), por de esta forma se extrae el vector de valores de color, del pixel (x, y), ya que se lee la imagen como si fuera una matriz de pixeles 

---
## Transform 2

La segunda transformación usa un par de coordenadas de inicio (x1,y1) y finales (x2,y2) para mostrar una región recortada de la imagen original
Se le solicita al usuario los valores (x, y) del par ordenado de inicio y de fin del recorte y se usa la sintaxis
imagenRecortada = imagenOrigen[yInicio:yfin , xInicio:xFin]
Que significa que toma de la imagen original desde el y de inicio hasta el y final, y desde el x de inicio hasta el x final.
La operacion se puede invalidar si se ingresa un valor negativo o fuera de las proporciones de la imagen original

---
## Transform 3

Esta transformación consiste en cambiar el tamaño de la imagen
Se le solicita al usuario las nuevas medidas en pixeles que tendrá la imagen; esta operación no toma en cuenta el ratio de aspecto de la imagen original.

---
## Transform 4

Esta transformación permite ingresar un valor a modoficar el ancho de pixeles de la imagen, y esta se modifica en base al aspecto y proporciones originales (sin deformarse)

Se solicita un valor para ajustar la imagen según su anchura, se realiza un cálculo en base a lo mostrado en el material de referencia para calcular las nuevas dimensiones de la imagen.
Se hace un resize en base a la imagen original y las dimensiones nuevas y se muestran la imagen original y la modificada, ambas conservan la misma proporción o aspect ratio

---
## Transform 5
Este transform permite rotar la imagen un número dado de grados
La imagen se girara una cantidad de grados determinada por el usuario; si se ingresan grados negativos la imagen se rotará en sentido de reloj, caso contrario si los grados son positivos.  

---
## Transform 6

Suavizar la imagen con filtro Gaussiano
Se aplica un kernel Gaussiano a la imagen que le aplicara un nivel de blur a la imagen. El nivel de suavizado debe ser impar y a mayor el nivel especificado el efecto será más pronunciado. El nivel de suavizado debe ser impar debido a que el algoritmo realiza la operación utilizando matrices y genera un valor en el centro de la matriz y ese centro debe ser un pixel, cosa que no ocurre cuando la matriz tiene dimensiones pares

---
## Propiedad

Autores: Danilo Chaves y  Leonardo Lizano

---
## Referencias

Material de apoyo utilizado:
A. Rosebrock, “Opencv tutorial: A guide to learn opencv.” [Online]. Available: https:
//www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
