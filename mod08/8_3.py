# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman
# ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä
# vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa
# valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on
# EFHK. Löydät koodeja helposti selaimen avulla.)

lentokentät = {}

while True:
    valinta = input("uusi, hae tai lopeta: ")

    if valinta == "lopeta":
        break

    elif valinta == "hae":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentokentät:
            print(lentokentät[icao])    # hakee

        else:
            print("Lentokenttää ei löytynyt")

    elif valinta == "uusi":
        icao = input("Anna ICAO-koodi: ")
        name = input("Anna lentoaseman nimi: ")
        lentokentät[icao] = name    # tallentaa

