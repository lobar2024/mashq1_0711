# 1-misol
def faktorial(n):
    if n < 0:
        return "Manfiy sonlar uchun faktorial aniqlanmagan"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

son = int(input("Faktorialini hisoblash uchun son kiriting: "))
natija = faktorial(son)
print(f"{son}! = {natija}")


# 2-misol
def palindrom_tekshir(satr):
    tozalangan = ''.join(satr.lower().split())
    if tozalangan == tozalangan[::-1]:
        return True
    return False

satr = input("Satr kiriting: ")
if palindrom_tekshir(satr):
    print(f"'{satr}' — palindrom!")
else:
    print(f"'{satr}' — palindrom emas.")


# 3-misol
def katta_kichik(royxat):
    if not royxat:
        return "Ro'yxat bo'sh"
    katta = max(royxat)
    kichik = min(royxat)
    return katta, kichik

royxat = list(map(int, input("Raqamlar ro'yxatini kiriting (bo'shliq bilan ajratib): ").split()))
katta, kichik = katta_kichik(royxat)
print(f"Eng katta: {katta}, Eng kichik: {kichik}")

# 4-misol
def unli_harflar(satr):
    unli = 'aeiouyAEIOUY'
    son = sum(1 for harf in satr if harf in unli)
    return son

satr = input("Satr kiriting: ")
natija = unli_harflar(satr)
print(f"Unli harflar soni: {natija}")


# 5-misol
def tub_son(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

son = int(input("Son kiriting: "))
if tub_son(son):
    print(f"{son} — tub son!")
else:
    print(f"{son} — tub son emas.")





