"""Parte 2: integración del tráfico de red mediante trapecios compuestos.

Ejecutar con Python 3: python parte2_integracion.py
No requiere instalar bibliotecas externas.
"""

import math


def trapecio_compuesto(f, a, b, n):
    """Aproxima la integral de f entre a y b con n subintervalos iguales."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n debe ser un entero positivo")
    h = (b - a) / n
    suma_interior = math.fsum(f(a + i * h) for i in range(1, n))
    return h * ((f(a) + f(b)) / 2 + suma_interior)


def R(t):
    """Tasa de transferencia en Mbps; el seno se evalúa en radianes."""
    return 10 + 5 * math.sin(math.pi * t / 4) + math.exp(0.15 * t)


def primitiva(t):
    """Integral indefinida de R, sin la constante de integración."""
    return 10 * t - (20 / math.pi) * math.cos(math.pi * t / 4) + math.exp(0.15 * t) / 0.15


def main():
    a, b = 0, 12
    exacto = primitiva(b) - primitiva(a)
    print(f"Valor exacto de referencia: {exacto:.12f} Megabits\n")
    print(f"{'n':>6} {'h (s)':>12} {'Integral (Mb)':>20} {'Error absoluto (Mb)':>22} {'Error (%)':>16}")
    print("-" * 80)
    for n in (4, 10, 50, 100, 1000):
        aproximado = trapecio_compuesto(R, a, b, n)
        error = abs(exacto - aproximado)
        porcentaje = error / abs(exacto) * 100
        print(f"{n:6d} {(b-a)/n:12.6f} {aproximado:20.12f} {error:22.12f} {porcentaje:16.10f}")


if __name__ == "__main__":
    main()
