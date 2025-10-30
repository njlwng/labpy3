# latihan1.py

from random import random

print("=== Program Menampilkan n Bilangan Acak yang Lebih Kecil dari 0.5 ===")

n = int(input("Masukkan nilai N: "))
i = 0

while i < n:
    a = random()
    if a < 0.5:
        print(f"data ke: {i+1} => {a}")
    i += 1

print("Selesai")

