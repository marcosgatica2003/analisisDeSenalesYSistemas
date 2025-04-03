import cmath

z = (-2+2j)**5
r, theta = cmath.polar(z)

print(f"{z:.2f} -> {r:.2f}cjs({theta:.2f})")
