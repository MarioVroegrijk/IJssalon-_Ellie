
# Functie: aanbieding van ijs
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting:.2f} euro."

# Functie: hoogste en laagste inkomsten
def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

# Functie: gemiddelde inkomsten
def gemiddelde(mijn_lijst):
    return sum(mijn_lijst) / len(mijn_lijst)

# Functie: meervoudig (gebruikt laag_en_hoog)
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

# Print aanbieding
print(aanbieding_1("aardbei", 4, 0.1))

# Inkomsten invoeren
inkomsten = [float(input(f"Dag {i+1} inkomsten: ").replace(",", ".")) for i in range(7)]

# BTW invoeren
btw = float(input("Voer het btw-percentage in (bijv. 0,09 voor 9%): ").replace(",", "."))

# Berekeningen
totaal = sum(inkomsten)
btw_bedrag = totaal * btw
hoog, laag = meervoudig(inkomsten)
gemiddeld = gemiddelde(inkomsten)

# Output
print(f"\nTotaal inkomsten: {totaal:.2f} euro, btw: {btw_bedrag:.2f} euro ({int(btw*100)}%)")
print(f"Hoogste inkomsten: {hoog:.2f} euro\nLaagste inkomsten: {laag:.2f} euro")
print(f"Gemiddelde inkomsten: {gemiddeld:.2f} euro")
