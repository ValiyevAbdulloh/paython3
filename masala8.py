harorat = (18, 20, 17, 23, 25, 21, 19)

natija = []

for h in harorat:
    if h > 20:
        natija.append(h)

print("Haroratlar:", *natija, sep=" ")
print("Kunlar soni:", len(natija))