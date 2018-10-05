#!/usr/bin/env python3

import math

a = float(input("Inserisca il coefficiente a: "))
b = float(input("Inserisca il coefficiente b: "))
c = float(input("Inserisca il coefficiente c: "))

delta = float(b ** 2 - 4 * a * c)

# È possibile calcolare la radice quadrata di delta anche così: delta ** (1/2).
# Tuttavia questo è più facilmente leggibile.
prima_rad = float((-b + math.sqrt(delta)) / (2 * a))
seconda_rad = float((-b - math.sqrt(delta)) / (2 * a))

print('x1 =', prima_rad)
print('x2 =', seconda_rad)
