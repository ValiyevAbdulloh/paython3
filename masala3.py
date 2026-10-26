daftar = 12

while daftar > 0:
    sotildi = int(input("Sotildi: "))

    if sotildi > daftar:
        print("Buncha daftar yo‘q!")
    else:
        daftar -= sotildi
        print("Qoldi:", daftar)

print("Ombor bo‘sh")