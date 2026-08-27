# Kirjoita ohjelma, joka kysyy käyttäjältä
# lämpötilan fahrenheittina ja muuttaa sen
# celsiukseksi

print("Tämä ohjelma muuntaa fahrenheitit celsius-asteiksi.\n")
fahrenheit = input("Anna lämpötila fahrenheit-yksikössä: ")

celsius = (int(fahrenheit) - 32) * 5/9

print(celsius)