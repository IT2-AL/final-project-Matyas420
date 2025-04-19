import random
znacky_karet = ['♠', '♥', '♦', '♣']
hodnoty_karet = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
penize_hrace = 10000
karty = []

for hodnota in hodnoty_karet:
    for znacka in znacky_karet:
        karta = hodnota + znacka
        karty.append(karta)

random.shuffle(karty)

def sazka_hry(penize_hrace):
    while True:
        try:
            vstup_sazky = input(f"Máš u sebe {penize_hrace} Kč. Minimum pro sázku je 500 Kč. Kolik peněz chcete vsadit nebo zadejte 'all in'? ")

            if vstup_sazky.lower() == "all in":
                return penize_hrace
            
            sazka = int(vstup_sazky)

            if sazka < 500:
                    print("Musíte vsadit alespoň 500 Kč.")
            elif sazka > penize_hrace:
                    print("Tolik peněz u sebe nemáte!")
            else:
                    return sazka
        except:
            print("Prosím, zadejte částku jako číslo.")

sazka = sazka_hry(penize_hrace)
penize_hrace -= sazka



print(f"Vsadil si {sazka} Kč.")
print(f"Tvůj aktuální zůstatek v peněžence je {penize_hrace} Kč.")
