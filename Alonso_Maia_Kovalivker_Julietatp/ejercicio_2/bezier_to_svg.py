#!/usr/bin/env python3
"""
bezier_to_svg.py  –  Ejercicio 2: La podadora robot
Uso: python bezier_to_svg.py <entrada.txt> [salida.svg] [--mostrar-controles]

Lee un archivo con los puntos de control [[x0,y0],[x1,y1],...] que definen una
curva de Bézier de grado n (n = número de puntos − 1) en coordenadas del jardín,
y genera un SVG con el fondo del jardín y la curva superpuesta.

Formato del archivo de entrada (lista de pares [x, y]):
    [
        [x0, y0],
        [x1, y1],
        ...
        [xn, yn]
    ]
También se acepta una lista plana: [x0, y0, x1, y1, ..., xn, yn].

Opciones:
  --mostrar-controles   Dibuja los puntos de control y el polígono de control.
"""

import ast
import argparse
from pathlib import Path

# ── Geometría del jardín (coincide con el tikzpicture del enunciado) ──────────
GARDEN_XMIN, GARDEN_XMAX = -0.5, 13.5
GARDEN_YMIN, GARDEN_YMAX = -3.5, 3.5

WALLS = [
    ((0, 3),   (13, 3)),   # pared superior
    ((0, -3),  (13, -3)),  # pared inferior
    ((13, -3), (13, 3)),   # pared derecha
]

BUSHES = [          # (cx, cy, radio)
    (2,  1,  1.5),
    (4,  -1, 1.0),
    (5,  2,  1.0),
    (7,  0,  1.0),
    (8,  -2, 1.0),
    (6,  -2, 0.5),
    (10, 1,  1.5),
    (11, -2, 1.0),
]

ORIGIN = (0,  0)
DEST   = (12, 0)


def load_control_points(path: str) -> list[list[float]]:
    with open(path) as f:
        data = ast.literal_eval(f.read())
    # Formato esperado: [[x0, y0, x1, y1, ..., xn, yn]]
    if (
        isinstance(data, list)
        and len(data) == 1
        and isinstance(data[0], (list, tuple))
        and all(isinstance(v, (int, float)) for v in data[0])
    ):
        row = data[0]
        if len(row) < 4 or len(row) % 2 != 0:
            raise ValueError(
                "La lista de coordenadas debe tener al menos 4 valores y un número par de valores."
            )
        return [[float(row[i]), float(row[i + 1])] for i in range(0, len(row), 2)]
    raise ValueError(
        "Formato no reconocido. Use [[x0, y0, x1, y1, ..., xn, yn]]."
    )


def de_casteljau(points: list[list[float]], t: float) -> list[float]:
    """Evalúa la curva de Bézier en t con el algoritmo de De Casteljau."""
    pts = [[p[0], p[1]] for p in points]
    for r in range(1, len(pts)):
        for i in range(len(pts) - r):
            pts[i][0] = (1 - t) * pts[i][0] + t * pts[i + 1][0]
            pts[i][1] = (1 - t) * pts[i][1] + t * pts[i + 1][1]
    return pts[0]


def generate_svg(control_points: list[list[float]],
                 base_width: int = 840,
                 show_control_lines: bool = False) -> str:
    """Genera el SVG con el jardín de fondo y la curva de Bézier superpuesta."""

    gx = GARDEN_XMAX - GARDEN_XMIN   # 14
    gy = GARDEN_YMAX - GARDEN_YMIN   # 7

    W = base_width
    H = int(base_width / (gx / gy))

    def tx(x: float) -> float:
        return (x - GARDEN_XMIN) / gx * W

    def ty(y: float) -> float:
        return (1.0 - (y - GARDEN_YMIN) / gy) * H

    def tr(r: float) -> float:
        return r / gx * W

    L = []   # lista de elementos SVG

    # ── Defs: marcador de flecha ──────────────────────────────────────────────
    L += [
        '  <defs>',
        '    <marker id="arr" markerWidth="8" markerHeight="8"'
        ' refX="8" refY="4" orient="auto">',
        '      <path d="M0,0 L0,8 L8,4 z" fill="#333"/>',
        '    </marker>',
        '  </defs>',
    ]

    # ── Grilla ────────────────────────────────────────────────────────────────
    for xi in range(0, 14):
        L.append(
            f'  <line x1="{tx(xi):.2f}" y1="{ty(GARDEN_YMIN):.2f}"'
            f' x2="{tx(xi):.2f}" y2="{ty(GARDEN_YMAX):.2f}"'
            f' stroke="#d8d8d8" stroke-width="0.6"/>'
        )
    for yi in range(-3, 4):
        L.append(
            f'  <line x1="{tx(GARDEN_XMIN):.2f}" y1="{ty(yi):.2f}"'
            f' x2="{tx(GARDEN_XMAX):.2f}" y2="{ty(yi):.2f}"'
            f' stroke="#d8d8d8" stroke-width="0.6"/>'
        )

    # ── Eje X ─────────────────────────────────────────────────────────────────
    L.append(
        f'  <line x1="{tx(-0.5):.2f}" y1="{ty(0):.2f}"'
        f' x2="{tx(13.6):.2f}" y2="{ty(0):.2f}"'
        f' stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>'
    )
    L.append(
        f'  <text x="{tx(13.8):.2f}" y="{ty(0) + 5:.2f}"'
        f' font-size="14" font-family="serif" font-style="italic">x</text>'
    )
    for xi in range(0, 14):
        L.append(
            f'  <text x="{tx(xi):.2f}" y="{ty(0) + 18:.2f}"'
            f' text-anchor="middle" font-size="11" font-family="serif">{xi}</text>'
        )

    # ── Eje Y ─────────────────────────────────────────────────────────────────
    L.append(
        f'  <line x1="{tx(0):.2f}" y1="{ty(3.6):.2f}"'
        f' x2="{tx(0):.2f}" y2="{ty(-3.5):.2f}"'
        f' stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>'
    )
    L.append(
        f'  <text x="{tx(0) + 4:.2f}" y="{ty(3.75):.2f}"'
        f' font-size="14" font-family="serif" font-style="italic">y</text>'
    )
    for yi in [-3, -2, -1, 1, 2, 3]:
        L.append(
            f'  <text x="{tx(0) - 5:.2f}" y="{ty(yi) + 4:.2f}"'
            f' text-anchor="end" font-size="11" font-family="serif">{yi}</text>'
        )

    # ── Paredes ───────────────────────────────────────────────────────────────
    for (x0, y0), (x1, y1) in WALLS:
        L.append(
            f'  <line x1="{tx(x0):.2f}" y1="{ty(y0):.2f}"'
            f' x2="{tx(x1):.2f}" y2="{ty(y1):.2f}"'
            f' stroke="#8B4513" stroke-width="4" stroke-linecap="round"/>'
        )

    # ── Arbustos ──────────────────────────────────────────────────────────────
    for cx, cy, r in BUSHES:
        L.append(
            f'  <circle cx="{tx(cx):.2f}" cy="{ty(cy):.2f}" r="{tr(r):.2f}"'
            f' fill="rgba(100,200,50,0.45)" stroke="#3a8a18" stroke-width="1.5"/>'
        )
        L.append(
            f'  <circle cx="{tx(cx):.2f}" cy="{ty(cy):.2f}" r="2.5" fill="#3a8a18"/>'
        )

    # ── Origen (O) y Destino (D) ──────────────────────────────────────────────
    ox, oy_px = tx(ORIGIN[0]), ty(ORIGIN[1])
    dx_px, dy_px = tx(DEST[0]), ty(DEST[1])

    L.append(f'  <circle cx="{ox:.2f}" cy="{oy_px:.2f}" r="5" fill="#1a55c4"/>')
    L.append(
        f'  <text x="{ox + 10:.2f}" y="{oy_px - 8:.2f}"'
        f' font-size="13" font-weight="bold" font-family="serif" fill="#1a55c4">O</text>'
    )
    L.append(f'  <circle cx="{dx_px:.2f}" cy="{dy_px:.2f}" r="5" fill="#b01010"/>')
    L.append(
        f'  <text x="{dx_px - 18:.2f}" y="{dy_px - 8:.2f}"'
        f' font-size="13" font-weight="bold" font-family="serif" fill="#b01010">D</text>'
    )

    # ── Polígono y puntos de control (opcional) ───────────────────────────────
    if show_control_lines:
        poly_pts = " ".join(
            f"{tx(p[0]):.2f},{ty(p[1]):.2f}" for p in control_points
        )
        L.append(
            f'  <polyline points="{poly_pts}" fill="none"'
            f' stroke="#aaa" stroke-width="1" stroke-dasharray="5,4"/>'
        )
        for p in control_points:
            L.append(
                f'  <circle cx="{tx(p[0]):.2f}" cy="{ty(p[1]):.2f}" r="4"'
                f' fill="#e8471a" opacity="0.9"/>'
            )
            lbl = f"({p[0]:.3g},{p[1]:.3g})"
            L.append(
                f'  <text x="{tx(p[0]) + 6:.2f}" y="{ty(p[1]) - 5:.2f}"'
                f' font-size="9" font-family="monospace" fill="#e8471a">{lbl}</text>'
            )

    # ── Curva de Bézier (muestreada con De Casteljau) ─────────────────────────
    N = 400
    curve = [de_casteljau(control_points, k / N) for k in range(N + 1)]
    curve_pts = " ".join(f"{tx(p[0]):.2f},{ty(p[1]):.2f}" for p in curve)
    L.append(
        f'  <polyline points="{curve_pts}" fill="none"'
        f' stroke="#1a73e8" stroke-width="2.5"'
        f' stroke-linecap="round" stroke-linejoin="round"/>'
    )

    body = "\n".join(L)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg"\n'
        f'     width="{W}" height="{H}"\n'
        f'     viewBox="0 0 {W} {H}">\n'
        f'{body}\n'
        '</svg>\n'
    )


def main():
    parser = argparse.ArgumentParser(
        description="Dibuja una curva de Bézier de grado n sobre el jardín de la podadora."
    )
    parser.add_argument("entrada", help="Archivo de puntos de control (.txt)")
    parser.add_argument("salida", nargs="?", help="Archivo SVG de salida")
    parser.add_argument(
        "--mostrar-controles",
        action="store_true",
        default=False,
        help="Muestra los puntos de control y el polígono de control.",
    )
    args = parser.parse_args()

    input_path  = args.entrada
    output_path = args.salida or str(Path(input_path).with_suffix(".svg"))

    pts = load_control_points(input_path)
    n   = len(pts) - 1
    print(f"Curva de Bézier de grado {n} ({len(pts)} puntos de control) "
          f"cargada desde '{input_path}'.")

    svg = generate_svg(pts, show_control_lines=args.mostrar_controles)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"SVG guardado en '{output_path}'.")


if __name__ == "__main__":
    main()
