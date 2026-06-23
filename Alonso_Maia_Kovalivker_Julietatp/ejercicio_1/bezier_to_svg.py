#!/usr/bin/env python3
"""
bezier_to_svg.py
Uso: python bezier_to_svg.py <entrada.txt> [salida.svg] [--mostrar-controles]

Lee un archivo con una lista de listas de puntos de control de curvas de Bézier cúbicas
(cada fila: x0 y0 x1 y1 x2 y2 x3 y3, todos en [0,1]) y genera un archivo SVG.

Opciones:
  --mostrar-controles   Dibuja también los puntos de control y las líneas auxiliares.
"""

import ast
import argparse
import math
import sys
from pathlib import Path


def load_segments(path: str) -> list[list[float]]:
    with open(path, "r") as f:
        data = ast.literal_eval(f.read())
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise ValueError("El archivo debe contener una lista de listas.")
    for row in data:
        if len(row) != 8:
            raise ValueError(f"Cada fila debe tener exactamente 8 valores; se encontraron {len(row)}: {row}")
    return data


def _bezier_axis_extrema(p0: float, p1: float, p2: float, p3: float) -> list[float]:
    """Devuelve los valores de t en (0,1) donde la derivada de la cúbica en un eje se anula."""
    a = -p0 + 3*p1 - 3*p2 + p3
    b = 2*p0 - 4*p1 + 2*p2
    c = -p0 + p1
    roots = []
    if abs(a) < 1e-12:
        if abs(b) > 1e-12:
            t = -c / b
            if 0.0 < t < 1.0:
                roots.append(t)
    else:
        disc = b*b - 4*a*c
        if disc >= 0:
            sq = math.sqrt(disc)
            for t in [(-b - sq) / (2*a), (-b + sq) / (2*a)]:
                if 0.0 < t < 1.0:
                    roots.append(t)
    return roots


def _bezier_eval(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
    """Evalúa la cúbica de Bézier en t para un eje dado."""
    mt = 1.0 - t
    return mt**3*p0 + 3*mt**2*t*p1 + 3*mt*t**2*p2 + t**3*p3


def compute_bounding_box(segments: list[list[float]], include_controls: bool = False) -> tuple[float, float, float, float]:
    """Calcula el bounding box exacto (xmin, ymin, xmax, ymax) de todos los segmentos."""
    xs, ys = [], []
    for seg in segments:
        x0, y0, cx1, cy1, cx2, cy2, x1, y1 = seg
        xs.extend([x0, x1])
        ys.extend([y0, y1])
        if include_controls:
            xs.extend([cx1, cx2])
            ys.extend([cy1, cy2])
        for t in _bezier_axis_extrema(x0, cx1, cx2, x1):
            xs.append(_bezier_eval(x0, cx1, cx2, x1, t))
        for t in _bezier_axis_extrema(y0, cy1, cy2, y1):
            ys.append(_bezier_eval(y0, cy1, cy2, y1, t))
    return min(xs), min(ys), max(xs), max(ys)


def segments_to_svg(segments: list[list[float]], base_size: int = 800,
                    stroke: str = "#1a73e8", stroke_width: float = 2.0,
                    show_control_lines: bool = False) -> str:
    """Convierte segmentos de Bézier a una cadena SVG.

    El lienzo se ajusta automáticamente al bounding box de las curvas más un 20% de margen
    (10% en cada lado). Las dimensiones en píxeles respetan la proporción del contenido.
    El eje Y está invertido: y=0 queda abajo, y=1 arriba.
    """
    xmin, ymin, xmax, ymax = compute_bounding_box(segments, include_controls=show_control_lines)

    # Añadir 10% en cada lado sobre el rango (= 20% total)
    dx = xmax - xmin or 1.0
    dy = ymax - ymin or 1.0
    xmin -= dx * 0.10;  xmax += dx * 0.10
    ymin -= dy * 0.10;  ymax += dy * 0.10
    dx = xmax - xmin
    dy = ymax - ymin

    # Dimensiones del lienzo en píxeles manteniendo la proporción
    aspect = dx / dy
    if aspect >= 1.0:
        width  = base_size
        height = max(1, int(base_size / aspect))
    else:
        height = base_size
        width  = max(1, int(base_size * aspect))

    def tx(x: float) -> float:
        return (x - xmin) / dx * width

    def ty(y: float) -> float:
        # Invertir Y: y=0 → abajo, y=1 → arriba
        return (1.0 - (y - ymin) / dy) * height

    paths = []
    control_lines = []

    for seg in segments:
        x0, y0, cx1, cy1, cx2, cy2, x1, y1 = seg
        sx0, sy0 = tx(x0), ty(y0)
        scx1, scy1 = tx(cx1), ty(cy1)
        scx2, scy2 = tx(cx2), ty(cy2)
        sx1, sy1 = tx(x1), ty(y1)

        paths.append(
            f'  <path d="M {sx0:.3f},{sy0:.3f} C {scx1:.3f},{scy1:.3f} '
            f'{scx2:.3f},{scy2:.3f} {sx1:.3f},{sy1:.3f}" '
            f'fill="none" stroke="{stroke}" stroke-width="{stroke_width}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
        )

        if show_control_lines:
            # Líneas punteadas desde los extremos hacia sus respectivos puntos de control
            control_lines.append(
                f'  <line x1="{sx0:.3f}" y1="{sy0:.3f}" x2="{scx1:.3f}" y2="{scy1:.3f}" '
                f'stroke="#aaa" stroke-width="0.8" stroke-dasharray="3,3"/>'
            )
            control_lines.append(
                f'  <line x1="{sx1:.3f}" y1="{sy1:.3f}" x2="{scx2:.3f}" y2="{scy2:.3f}" '
                f'stroke="#aaa" stroke-width="0.8" stroke-dasharray="3,3"/>'
            )
            # Puntos de control
            for (px, py), (ox, oy) in [((scx1, scy1), (cx1, cy1)), ((scx2, scy2), (cx2, cy2))]:
                control_lines.append(
                    f'  <circle cx="{px:.3f}" cy="{py:.3f}" r="3" fill="#e8471a" opacity="0.7"/>'
                )
                label = f"[{ox:.2f};{oy:.2f}]"
                control_lines.append(
                    f'  <text x="{px+5:.3f}" y="{py-4:.3f}" font-size="9" fill="#e8471a" '
                    f'font-family="monospace">{label}</text>'
                )
            # Puntos extremos
            for (px, py), (ox, oy) in [((sx0, sy0), (x0, y0)), ((sx1, sy1), (x1, y1))]:
                control_lines.append(
                    f'  <circle cx="{px:.3f}" cy="{py:.3f}" r="3" fill="#1a73e8"/>'
                )
                label = f"[{ox:.2f};{oy:.2f}]"
                control_lines.append(
                    f'  <text x="{px+5:.3f}" y="{py-4:.3f}" font-size="9" fill="#1a73e8" '
                    f'font-family="monospace">{label}</text>'
                )

    control_group = ""
    if show_control_lines and control_lines:
        control_group = (
            '\n  <g id="control-handles">\n'
            + "\n".join(control_lines)
            + "\n  </g>"
        )

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
{chr(10).join(paths)}{control_group}
</svg>
"""
    return svg


def main():
    parser = argparse.ArgumentParser(
        description="Convierte puntos de control de Bézier cúbicas a SVG."
    )
    parser.add_argument("entrada", help="Archivo de entrada con los puntos de control (.txt)")
    parser.add_argument("salida", nargs="?", help="Archivo de salida (.svg); por defecto mismo nombre que la entrada")
    parser.add_argument(
        "--mostrar-controles",
        action="store_true",
        default=False,
        help="Dibuja los puntos de control y las líneas auxiliares (por defecto: desactivado)",
    )
    args = parser.parse_args()

    input_path  = args.entrada
    input_dir   = Path(input_path).parent
    if args.salida:
        output_path = str(input_dir / Path(args.salida).name)
    else:
        output_path = str(input_dir / Path(input_path).with_suffix(".svg").name)

    segments = load_segments(input_path)
    print(f"Se cargaron {len(segments)} segmento(s) de Bézier desde '{input_path}'.")

    svg_content = segments_to_svg(segments, show_control_lines=args.mostrar_controles)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"SVG guardado en '{output_path}'.")


if __name__ == "__main__":
    main()
