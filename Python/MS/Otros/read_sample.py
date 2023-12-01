content=open("sample1.txt")
for line in content:
    print(line)
content.seek(0)
print(type(content))
content.seek(0)
print(content)
content.seek(0)
print(content.mode)
##  print(content.read())
content.seek(0)
print(type(content.read()))

content.seek(0)
print(content.readlines())
content.close()

#  Best Practice
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read(10)  # Lee los primeros 10 caracteres
    archivo.seek(0)  # Mueve el cursor al principio
    primera_linea = archivo.readline()  # Lee la primera línea
    archivo.seek(0)  # Mueve el cursor al principio nuevamente
    lineas = archivo.readlines()  # Lee todas las líneas restantes

# Cuando se sale del bloque 'with', el archivo se cierra automáticamente.
