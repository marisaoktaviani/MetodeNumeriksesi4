
import math

# Nama  : Marisa Oktaviani
# NIM   : 20250040069
# Metode: Bisection (Biseksi)

def f(t):
    return 800 * math.exp(0.3 * t) - 2000 - 400 * t

a = 5.0
b = 6.0
tol = 0.00001
maks_iterasi = 100

print("=" * 85)
print("       PROGRAM METODE BISEKSI - TITIK IMPAS BIAYA CLOUD")
print("Nama : Marisa")
print("NIM  : 20250040069")
print("=" * 85)

print(f"{'Iterasi':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<20}")
print("-" * 85)

if f(a) * f(b) >= 0:
    print("Interval tidak memenuhi syarat metode biseksi.")
else:
    for i in range(1, maks_iterasi + 1):
        c = (a + b) / 2
        fc = f(c)

        print(
            f"{i:<10}{a:<15.4f}{b:<15.4f}"
            f"{c:<15.4f}{fc:<20.4f}"
        )

        if abs(fc) < tol:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("-" * 85)
    print(f"Titik impas (t) = {c:.4f} bulan")
    print(f"Nilai f(t)      = {f(c):.4f}")
    print("=" * 85)