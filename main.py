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
print(karty)

while True:
    try:
        sazka = int(input(f"Máš u sebe {penize_hrace} Kč. Minimum pro sázku je 500 Kč. Kolik peněž chcete vsadit?"))

        if sazka < 500:
            print("Musíte vsadit alespoň 500 Kč.")
        if sazka > penize_hrace:
            print("Tolik peněz u sebe nemáš!")
        else:
            break
    except ValueError:
        print("Prosím, zadejte částku!")


