prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}

aanbieding = prijzen["aardbei"] * 0.8

# reclame_tekst met puntnotatie
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}"

# reclame_tekst2 met komma i.p.v. punt (Nederlandse notatie)
reclame_tekst2 = reclame_tekst.replace('.', ',')

print(reclame_tekst2)