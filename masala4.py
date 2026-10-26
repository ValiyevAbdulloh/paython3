son = int(input("Son kiriting: "))
sanoq = 0

while son > 0:
    son = son // 10
    sanoq += 1

print("Raqamlar soni:", sanoq)