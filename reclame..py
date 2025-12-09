# Functie: kwadraat en basisberekeningen
def mijn_functie_2(getal1, getal2):
    som = getal1 + getal2
    verschil = getal1 - getal2
    product = getal1 * getal2
    quotient = getal1 / getal2 if getal2 != 0 else None  # voorkomen van delen door nul
    return som, verschil, product, quotient


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


# --------------------------
# Nieuwe functie: combinatie()
# --------------------------
def combinatie(invoer_lijst_2):
    """
    Roept laag_en_hoog() aan met invoer_lijst_2,
    en gebruikt de twee getallen als argumenten voor mijn_functie_2().
    Geeft de resultaten van mijn_functie_2() terug.
    """
    korte_lijst = laag_en_hoog(invoer_lijst_2)  # tuple van twee getallen
    resultaat = mijn_functie_2(*korte_lijst)     # unpack naar twee argumenten
    return resultaat


# --------------------------
# Hoofdprogramma
# --------------------------
if __name__ == "__main__":
    # Print aanbieding
    print(aanbieding_1("aardbei", 4, 0.1))

    # Inkomsten invoeren
    inkomsten = [float(input(f"Dag {i+1} inkomsten: ").replace(",", ".")) for i in range(7)]

    # BTW invoeren
    btw = float(input("Voer het btw-percentage in (bijv. 0,09 voor 9%): ").replace(",", "."))

    # Berekeningen inkomsten
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    hoog, laag = meervoudig(inkomsten)
    gemiddeld = gemiddelde(inkomsten)

    # Output inkomsten
    print(f"\nTotaal inkomsten: {totaal:.2f} euro, btw: {btw_bedrag:.2f} euro ({int(btw*100)}%)")
    print(f"Hoogste inkomsten: {hoog:.2f} euro\nLaagste inkomsten: {laag:.2f} euro")
    print(f"Gemiddelde inkomsten: {gemiddeld:.2f} euro")

    # Voorbeeld van combinatie()
    test_lijst = [5, 10, 3, 8]
    comb_resultaat = combinatie(test_lijst)
    print("\nResultaten combinatie():")
    print(f"Optellen: {comb_resultaat[0]}")
    print(f"Aftrekken: {comb_resultaat[1]}")
    print(f"Vermenigvuldigen: {comb_resultaat[2]}")
    print(f"Delen: {comb_resultaat[3]}")
