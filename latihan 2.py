# latihan2.py

modal = 100000000
laba = 0
total = 0

for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0
    elif bulan == 3 or bulan == 4:
        laba = modal * 0.01
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba = modal * 0.05
    elif bulan == 8:
        laba = modal * 0.03
    total = total + laba
    print(f"laba bulan ke- {bulan} sebesar: {laba}")

print(f"Total laba adalah: {total}")
