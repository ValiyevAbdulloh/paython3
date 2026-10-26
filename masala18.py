shaharlar = {"Toshkent": 3000000, "Farg‘ona": 300000, "Samarqand": 600000}

print("500 000 dan ko‘p:")

for shahar, aholi in shaharlar.items():
    if aholi > 500000:
        print(shahar, end=", ")

eng_kop = max(shaharlar, key=shaharlar.get)

print("\nEng ko‘p aholi:", eng_kop)