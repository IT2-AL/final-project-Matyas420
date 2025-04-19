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

print("********************************************************************************")
print("♠                                                                              ♠")
print("♥                          𝙑í𝙩𝙚𝙟𝙩𝙚 𝙫𝙚 𝙝ř𝙚 𝘽𝙡𝙖𝙘𝙠𝙅𝙖𝙘𝙠                            ♥")
print("♣                                                                              ♣")
print("♣                                                                              ♣")
print("*********************************************************************************") 

def sazka_hry(penize_hrace):
    while True:
        try:
            vstup_sazky = input(" Minimum pro sázku je 500 Kč. Kolik peněz chcete vsadit nebo zadejte 'all in'? ")

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

print(f"Vsadil jste {sazka} Kč.")
print(f"Váš aktuální zůstatek v peněžence je {penize_hrace} Kč.")

print("-------------------------------------------------------------------------------")
print("                               𝘿𝙚𝙖𝙡𝙚𝙧                                          ")
print("                                                                               ")
print("                                                                               ")
print("                                                                               ")
print("-------------------------------------------------------------------------------")

dealer_karty = []
hrac_karty = []







print(f" Zůstatek: {penize_hrace} Kč")
print("--------------------------------------------------------------------------")