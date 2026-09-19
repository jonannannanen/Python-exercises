# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
# halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def kpl_hinta(halkaisija, hinta):
    radius = halkaisija / 2 / 100
    pinta_ala = math.pi * radius ** 2
    result = hinta / pinta_ala
    return result

halkaisija1 = float(input("Ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Ensimmäisen pizzan hinta: "))

halkaisija2 = float(input("Toisen pizzan halkaisija: "))
hinta2 = float(input("Toisen pizzan hinta: "))

kpl_hinta1 = kpl_hinta(halkaisija1, hinta1)
kpl_hinta2 = kpl_hinta(halkaisija2, hinta2)

if kpl_hinta1 < kpl_hinta2:
    print("Paremi vastine rahalle: Pizza nro. 1.")
elif kpl_hinta2 < kpl_hinta1:
    print("Parempi vastine rahalle: Pizza nro. 2.")
else:
    print("Molemmissa pizzoissa on sama vastine.")