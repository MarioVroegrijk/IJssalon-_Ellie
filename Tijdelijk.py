prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}

aanbieding = prijzen["aardbei"] * 0.8

# reclame_tekst met 2 decimalen
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}"

# vind de eerste punt in de prijs
comma_pos = reclame_tekst.find(".")
# zoek de eerste '0' na de punt
if comma_pos != -1:
    index_of_zero = reclame_tekst.find("0", comma_pos + 1)
else:
    index_of_zero = -1

# reclame_tekst2 met index
reclame_tekst2 = f"{reclame_tekst}[: {index_of_zero}]"

# reclame_tekst3 in hoofdletters
reclame_tekst3 = reclame_tekst2.upper()

# reclame_tekst4 als lijst van woorden
reclame_tekst4 = reclame_tekst3.split()

# loop door de woorden en pas hoofd-/kleine letters toe afhankelijk van lengte
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
