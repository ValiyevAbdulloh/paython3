matematika = {"Ali", "Vali", "Madina", "Jasur", "Aziza"}
ingliz = {"Madina", "Jasur", "Sardor", "Aziza", "Malika"}

ikkala = matematika & ingliz
bitta = matematika ^ ingliz

print("Ikkala kursda:", ", ".join(sorted(ikkala)))
print("Faqat bitta kursda:", ", ".join(sorted(bitta)))