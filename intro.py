#esto es un comentario
'''
comentario 
de varias 
lineas
'''

#!/usr/bin/env python --> script python
#-*- coding: utf-8 --> codificacion utf8

__author__ = "Iago"
__license = "GPL"
__email__ = "a22iagopp@iessanclmente.net"

mi_variable = 8
print(mi_variable)

print(type("Hola"))

numero_entero = 1
print(type(numero_entero))

numero_float = 1.2
print(type(True))

nombre = "Iago"
apellido = "Páramo"

print("Mi nombre es:",nombre, "\nMi apellido es:\t", apellido )

print(3 == "3")

num, edad = 3, 4

print("Hola, me llamo {}".format(nombre))
print("Hola, tengo {} años y mi numero favorito es {}".format(edad,num))
print("Hola, tengo %d años y mi numero favorito es %f" %(edad,num))