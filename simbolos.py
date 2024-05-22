def reemplazar_simbolos(texto):
    reemplazos = {
        "mas": "+",
        "menos": "-",
        "por": "*",
        "dividido": "/",
        "mayor que": " > ",
        "menor que": " < ",
        "equivale": " == ",
        "diferente": " != ",
        "mayor igual": " >= ",
        "menor igual": " <= ",
        "print": "print"
    }
    for palabra, simbolo in reemplazos.items():
        texto = texto.replace(palabra, simbolo)
    return texto

def evaluar_expresion(expresion):
    try:
        resultado = eval(expresion)
        return str(resultado)
    except Exception as e:
        return str(e)

def procesar_archivo(entrada, salida):
    with open(entrada, 'r') as archivo_entrada:
        lineas = archivo_entrada.readlines()

    lineas_procesadas = []
    for linea in lineas:
        linea = reemplazar_simbolos(linea)
        resultado = evaluar_expresion(linea)
        lineas_procesadas.append(resultado + "\n")  # Agregar un salto de línea después de cada resultado

    with open(salida, 'w') as archivo_salida:
        archivo_salida.writelines(lineas_procesadas)

# Ejemplo de uso
entrada = "entrada.txt"
salida = "salida.txt"
procesar_archivo(entrada, salida)
