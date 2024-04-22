
import argparse
import math
from turtle import Screen, Turtle
from typing import Optional

from svgpathtools import svg2paths

turtle = Turtle()
screen = Screen()


def analizar_estilos(attrs: list[dict]) -> list[dict]:
        # Analiza y convierte los estilos CSS en un formato manejable en Python#
    for dictionary in attrs:
        try:
            pairs = dictionary['style'].replace(' ', '')
        except KeyError:
            continue
        pairs = pairs.rstrip(';').split(';')
        for pair in pairs:
            key, value = pair.split(':')
            if value == 'none':
                value = None
            dictionary[key] = value
    return attrs


def analizar_trazos(paths: list, quality: int = 8, offset: tuple[float, float] = (0, 0)) -> list[list]:
     #Convierte los caminos SVG en una lista de puntos para ser dibujados con Turtle. #
    new_paths = []
    for path in paths:
        new_path = []
        for subpaths in path.continuous_subpaths():
            points = []
            for segment in subpaths:
                interp_num = math.ceil(segment.length() / quality)
                positions = [x / interp_num for x in range(interp_num)]
                points.extend([segment.point(position) for position in positions])
            new_path.append([(point.real + offset[0], -point.imag - offset[1]) for point in points])
        new_paths.append(new_path)
    return new_paths


def move_to(coords: tuple[float, float], draw: bool = True):
    # Mueve la tortuga a la posición especificada, opcionalmente dibujando una línea. #
    wasdown = turtle.isdown()
    turtle.pen(pendown=draw)
    turtle.goto(coords[0], coords[1])
    turtle.pen(pendown=wasdown)


def dibujar_trazos(path, color: Optional[str] = None, fill: Optional[str] = None):
    #    """ Dibuja los caminos procesados con los colores especificados. """ #
    if color:
        turtle.color(color)
    for segment in path:
        move_to(segment[0], False)
        if fill:
            turtle.color(fill)
            turtle.begin_fill()
        for point in segment[1:]:
            move_to(point, True)
        if fill:
            turtle.end_fill()


def main(file_path: str, frame_center: tuple[float, float], frame_size: tuple[float, float], loop: bool = False, quality: int = 1, n: int = 0):
    paths, attrs, svg_attrs = svg2paths(file_path, return_svg_attributes=True)
    attrs = analizar_estilos(attrs)

    # Dimensiones originales del SVG
    original_width = float(svg_attrs['width'])
    original_height = float(svg_attrs['height'])

    # Calcular escala para ajustar el SVG dentro del marco
    scale_width = frame_size[0] / original_width
    scale_height = frame_size[1] / original_height
    scale = min(scale_width, scale_height)  # Usar la menor escala para asegurar que el SVG quepa completamente

    # Calcular el nuevo tamaño del SVG basado en la escala
    scaled_width = original_width * scale
    scaled_height = original_height * scale

    # Calcular el offset para centrar el SVG en el marco
    offset_x = frame_center[0] - scaled_width / 2
    offset_y = frame_center[1] - scaled_height / 2

    # Ajustar paths al nuevo tamaño y posición
    paths = analizar_trazos(paths, quality, (offset_x, -offset_y))  # Ajustar Y negativo por la orientación de Turtle
    screen.tracer(n=n, delay=0)
    screen.screensize(scaled_width, scaled_height)
    while True:
        turtle.reset()
        turtle.hideturtle()
        for path, attr in zip(paths, attrs):
            dibujar_trazos(path, attr.get('stroke'), attr.get('fill'))
        if not loop:
            break
    screen.update()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-l', '--loop', action='store_true')
    parser.add_argument('-q', '--quality', type=int, default=1)
    parser.add_argument('-n', type=int, default=0)
    args = parser.parse_args()
    main(args.path, args.loop, args.quality, args.n)
