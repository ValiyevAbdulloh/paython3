jami = 0
sanoq = 0

xarajat = int(input("Xarajatni kiriting: "))

while xarajat != 0:
    jami += xarajat
    sanoq += 1
    xarajat = int(input("Xarajatni kiriting: "))

print("Jami:", jami)
print("Kiritilgan xarajatlar soni:", sanoq)

if sanoq > 0:
    ortacha = jami / sanoq
    print("O‘rtacha:", round(ortacha, 2))