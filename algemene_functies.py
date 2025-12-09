def mijn_functie_1():
    getal = int(input("Voer een getal in: "))
    resultaat = getal * getal
    print(f"Het kwadraat van {getal} is {resultaat}")


def mijn_functie_2():
    getal1 = float(input("Voer het eerste getal in: "))
    getal2 = float(input("Voer het tweede getal in: "))

    som = getal1 + getal2
    verschil = getal1 - getal2
    product = getal1 * getal2
    quotient = getal1 / getal2

    print("\nUitkomsten:")
    print(f"{getal1} + {getal2} = {som}  (optellen)")
    print(f"{getal1} - {getal2} = {verschil}  (aftrekken)")
    print(f"{getal1} * {getal2} = {product}  (vermenigvuldigen)")
    print(f"{getal1} / {getal2} = {quotient}  (delen)")


# Hoofdmenu
print("Kies een functie:")
print("1: Kwadraat berekenen")
print("2: Twee getallen berekenen")

keuze = input("Maak je keuze: ")

if keuze == "1":
    mijn_functie_1()
elif keuze == "2":
    mijn_functie_2()
else:
    print("Ongeldige keuze")