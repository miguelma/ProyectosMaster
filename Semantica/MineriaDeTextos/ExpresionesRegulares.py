#!/usr/bin/python
# -*- coding: utf-8 -*-

# Se pide codificar las siguientes expresiones regulares para encontrar
# las palabras que se piden en cada ejercicio. Esto es, la expresion
# regular debe ser capaz de encontrar palabras que cumplan la
# especificacion y solo esas. Para simplificar la tarea del alumno, se
# dejan dos ejemplos, una palabra que si cumple la especificacion y
# otro que no. Los dos ultimos 
# ejercicios son opcionales. 
import re

# Ejercicio 1: las palabras con letras minusculas


patron1 = r'^[a-z]+$'
if re.search(patron1,'estoesvalido'):
    print ("Ejercicio 1.1: OK")
if not re.search(patron1,'AQUI NO ESTA (de seguro)'):
    print ("Ejercicio 1.2: OK")


# Ejercicio 2: las palabras que empiecen por minuscula y luego solo tengan letras


patron2 = r'^[a-z][A-z]+$'
if re.search(patron2,'estoesvalido'):
    print( "Ejercicio 2.1: OK")
if not re.search(patron2,'estoNOESVALIDO7'):
    print( "Ejercicio 2.2: OK")


# Ejercicio 3: las palabras que tengan al menos dos numeros y lo demas sean letras

patron3 = r'^\w*\d+\w*\d+\w*$'
if re.search(patron3,'7estoesvalido7'):
    print ("Ejercicio 3.1: OK")
if not re.search(patron3,'estoNOESVALIDO7'):
    print ("Ejercicio 3.2: OK")

# Ejercicio 4: Las palabras que contengan la cadena 111 al final


patron4 = r'^\w*[1]{3}$'
if re.search(patron4,'7estoesvalido111'):
    print ("Ejercicio 4.1: OK")
if not re.search(patron4,'estoNOESVALIDO11117'):
    print ("Ejercicio 4.2: OK")

# Ejercicio 5: Las palabras que no tengan el parentesis al principio )


patron5 = r'^[^(]\S*$'
if re.search(patron5,'7estoesvalido111___@@@@'):
    print ("Ejercicio 5.1: OK")
if not re.search(patron5,'(estoNOESVALIDO11117'):
    print ("Ejercicio 5.2: OK")

# Ejercicio 6: Las palabras que no contengan :( y esten formadas por
# letras y espacios (DIFICIL)

#^[:]*[^(]*$
patron6 = r'^(?!.*:\().*$'
if re.search(patron6,'esto es valido :)'):
    print ("Ejercicio 6.1: OK")
if not re.search(patron6,'(esto me pone triste :('):
    print ("Ejercicio 6.2: OK")

# Ejercicio 7: Las palabras que contengan algun smiley de los siguientes :) ;)


patron7 = r'^\D*[:;][)]\D*$'
if re.search(patron7,'esto es valido :)'):
    print ("Ejercicio 7.1: OK")
if not re.search(patron7,'(esto no es valido :D'):
    print ("Ejercicio 7.2: OK")


# Ejercicio 8: Las palabras que acaben con algun smiley de los
# siguientes :) ;) XD y empiecen con un OLA, los demas caracteres
# pueden ser cualesquiera. 


patron8 = r'^(?:OLA).*([:;][)]|[X][D])$'
if re.search(patron8,'OLA esto es valido XD'):
    print ("Ejercicio 8.1: OK")
if not re.search(patron8,'OLA esto no es valido 8)'):
    print ("Ejercicio 8.2: OK")


# Ejercicio 9: Cualquier etiqueta que pueda aparecer en XML 


patron9 = r'^<\w*(?: \w*="\w*")*>$'
if re.search(patron9,'<etiqueta valida="YES" corta="YES">'):
    print ("Ejercicio 9.1: OK")
if not re.search(patron9,'<etiqueta valida="no">>'):
    print ("Ejercicio 9.2: OK")




# Ejercicio 10: Cualquier direccion IP version 4 bien formada, esto
# es, tres numeros entre 0 y 255, separados por un punto


patron10 = r'^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
if re.search(patron10,'193.144.132.1'):
    print ("Ejercicio 10.1: OK")
if not re.search(patron10,'Esto no lo es 193.122.888.222'):
    print ("Ejercicio 10.2: OK")


# Ejercicio 11: (Opcional) Las palabras que sean direcciones de email


patron11 = r'^\S+[@]\S+[\.]\S+$'
if re.search(patron11,'esto@correcto.es'):
    print ("Ejercicio 11.1: OK")
if not re.search(patron11,'esto  incorrecto@.com'):
    print ("Ejercicio 11.2: OK")



# Ejercicio 12: Utilizar la opcion re.VERBOSE para poner comentarios
# a  dos expresiones regulares.  

patron121 = r'''
    ^          
    \S+        # cualquier caracter que no es un espacio. correo
    [@]        # simbolo @ 
    \S+        # cualquier caracter que no es un espacio. tipo de correo
    [\.]       # simbolo .
    \S+        # cualquier caracter que no es un espacio. dominio
    $          
'''

pattern_compiled1 = re.compile(patron121, re.VERBOSE)

if pattern_compiled1.search('esto@correcto.es'):
    print("Ejercicio 12.1: OK")



patron122 = r'''
    ^         
    (?:OLA)   # La palabra tiene que tener OLA al principio
    .*        # culaquier cosa después
    (         # Le sigue algo de lo siguiente: .) ;) o XD
    [:;][)]  
    |       
    [X][D]  
    )         
    $         
'''

# Compile the pattern with re.VERBOSE flag
pattern_compiled2 = re.compile(patron122, re.VERBOSE)

# Test the pattern
if pattern_compiled2.search('OLAdfhj:)'):
    print("Ejercicio 12.2: OK")



