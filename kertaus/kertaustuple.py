# listat = []
# monikko = ()
# joukko = {}
# sanakirja = {:}

# TUPLES ARE TOUGH, FOREVER
# joukko on specific, jokaista objektia voi olla siellä vain yksi kappale

# viikonpäivät = ("MA", "TI", "KE", "TO")
# viikonpäivät = ("PE", "LA", "SU")

# def luvut(luku1, luku2):
#     eka = luku1
#     toka = luku2
#     return eka, toka

# noppa1, noppa2 = luvut(1,2)

# print(noppa1, noppa2)

numerot = {"Viivi": "050-1234567",
           "Ahmed": "040-1112223",
           "Pekka": "050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

print(numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")
else:
    print("Tietoja ei löytynyt")
    userinput = input("Lisätäänkö nimi? (Y/N)")
    if userinput == "Y":
        numerot[nimi] = "000"

print(numerot)