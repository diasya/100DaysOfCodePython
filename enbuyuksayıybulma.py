sayilar = input("Input the list of numbers: ").split()
for n in range(0, len(sayilar)):
    sayilar[n] = int(sayilar[n])

dummy = sayilar[0]
for i in sayilar:
    if dummy < i:
        dummy = i

print(dummy)
