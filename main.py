import turtle
import random
import textwrap
from narratives import narrativas_tesoro
from sequences import secuencias

def wrap_text(text, width):
    """Envuelve el texto para mostrarlo adecuadamente en gráficos de Turtle."""
    wrapper = textwrap.TextWrapper(width=width)  # Crea un envoltorio para el texto
    word_list = wrapper.wrap(text=text)  # Envuelve el texto en una lista de líneas
    wrapped_text = "\n".join(word_list)  # Une las líneas en una sola cadena con saltos de línea
    return wrapped_text

# Configuración inicial de la ventana de Turtle
windows_width = 1280
windows_height = 720
text_position = (-400, 300)  # Posición del texto del título
narrative_position = (-440, -210)  # Posición del texto de la narrativa

def pedir_datos_niño():
    print("Bienvenido a este cuenta cuentos digital")
    nombre = input("¿Cuál es tu nombre? ")  # Pide el nombre del niño
    while True:
        edad = input("¿Cuántos años tienes? ")
        try:
            edad = int(edad)  # Convierte la entrada en un entero
            break
        except ValueError:
            print("Por favor, introduce un número válido para la edad.")

    # Lista de colores válidos y su traducción
    valid_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black', 'brown', 'pink', 'cyan', 'magenta']
    color_translation = {
        'rojo': 'red', 'azul': 'blue', 'verde': 'green', 'amarillo': 'yellow',
        'morado': 'purple', 'naranja': 'orange', 'negro': 'black', 'marrón': 'brown',
        'rosa': 'pink', 'cian': 'cyan', 'magenta': 'magenta'
    }
    color_favorito = input("¿Cuál es tu color favorito? (rojo, azul, verde, amarillo, morado, naranja, negro, marrón, rosa, cian, magenta) ")
    color_favorito = color_translation.get(color_favorito.lower(), None)  # Traduce el color a inglés
    while color_favorito not in valid_colors:
        color_favorito = input("Ese color no es válido. Por favor, introduce un color válido: ")  # Pide el color nuevamente si no es válido
        color_favorito = color_translation.get(color_favorito.lower(), None)

    return nombre, edad, color_favorito

def mostrar_secuencia(secuencia, narrativas, pantalla, t, nombre, color_favorito):
    t.clear()  # Limpia la pantalla de dibujo anterior
    t.goto(text_position)  # Mueve la tortuga a la posición del texto
    t.write(secuencia["titulo"], font=("Arial", 18, "bold"))  # Escribe el título de la secuencia
    secuencia["funcion_escena"](t, color_favorito)  # Ejecuta la función de escena
    narrativa_aleatoria = random.choice(narrativas)  # Selecciona una narrativa aleatoria
    wrapped_narrativa = wrap_text(narrativa_aleatoria.format(nombre_niño=nombre), 120)  # Formatea y envuelve la narrativa
    t.goto(narrative_position)  # Mueve la tortuga a la posición de la narrativa
    for line in wrapped_narrativa.split("\n"):  # Escribe la narrativa línea por línea
        t.write(line, font=("Arial", 12), align="left")
        t.sety(t.ycor() - 20)  # Ajusta la posición y para la siguiente línea

def mostrar_cuento(secuencias, narrativas, nombre, color_favorito):
    pantalla = turtle.Screen()
    pantalla.setup(width=windows_width, height=windows_height)
    pantalla.title("Laboratorio 1 - Sara Chacón")
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    idx_secuencia = 0  # Índice inicial de la secuencia

    def mostrar_secuencia_actual():
        mostrar_secuencia(secuencias[idx_secuencia], narrativas[idx_secuencia], pantalla, t, nombre, color_favorito)
        if idx_secuencia == len(secuencias) - 1:  # Verifica si es la última secuencia
            mostrar_resultados()  # Muestra los resultados finales
        else:
            respuesta = input("¿Desea continuar? (S/N): ")  # Pregunta si desea continuar
            if respuesta.lower() == 's':
                avanzar_cuento()  # Avanza al siguiente cuento
            else:
                mostrar_resultados()  # Muestra resultados y termina

    def avanzar_cuento():
        nonlocal idx_secuencia
        idx_secuencia += 1  # Incrementa el índice de secuencia
        mostrar_secuencia_actual()  # Muestra la nueva secuencia

    def mostrar_resultados():
        print("Has llegado al final, gracias por leerlo completo")
        turtle.done()  # Termina los gráficos de turtle
        pantalla.bye()  # Cierra la ventana de turtle

    mostrar_secuencia_actual()  # Inicia el proceso mostrando la primera secuencia

nombre_niño, edad_niño, color_favorito_niño = pedir_datos_niño()
mostrar_cuento(secuencias, narrativas_tesoro, nombre_niño, color_favorito_niño)
