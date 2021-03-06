# función para crear `flower_dictionary` desde el nombre de archivo
def crea_diccionario(archivo):
    diccionario_flores = {}

    with open(archivo, 'r') as f:
        for line in f.readlines():
            key, value = line.split(':')
            value = value.rstrip()
            diccionario_flores[key.lower()] = value

    return diccionario_flores

# Función principal para solicitar la entrada de usuario.
# No modificar este bloque del código
# Ajustar solo la ruta del archivo si es necesario
def main():
    d_flores = crea_diccionario('data_files/flowers.txt')
    nombre_completo = input("Capture solo su Nombre [espacio] Apellido: ")
    nombre = nombre_completo[0].lower()
    letra = nombre[0]
# imprimir el resultado con el valor correspondiente a la llave del diccionario
    print("Nombre único de flor, usando la primera letra: {}".format(d_flores[letra]))

main()
