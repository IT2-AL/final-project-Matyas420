import random

znacky_karet = ['♠', '♥', '♦', '♣']
hodnoty_karet = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
pocatecni_penize = 10000
penize_hrace = pocatecni_penize
minimum_sazky = 500

def vytvor_balicek():
    karty = []
    for hodnota in hodnoty_karet:
        for znacka in znacky_karet:
            karty.append(hodnota + znacka)
    random.shuffle(karty)
    return karty

def sazka_hry(penize_hrace):
    while True:
        try:
            vstup_sazky = input(f"Minimum pro sázku je {minimum_sazky} Kč. Kolik peněz chcete vsadit nebo zadejte 'all in'? ")
            if vstup_sazky.lower() == "all in":
                return penize_hrace
            
            sazka = int(vstup_sazky)
            
            if sazka < minimum_sazky:
                print("Musíte vsadit alespoň 500 Kč.")
                
            elif sazka > penize_hrace:
                print("Tolik peněz u sebe nemáte!")
            else:
                return sazka
        except:
            print("Prosím, zadejte částku jako číslo.")
            
sazka = sazka_hry(penize_hrace)
penize_hrace -= sazka

print(f"Máte u sebe {penize_hrace} Kč.")

print(f"Vsadil jste {sazka} Kč.")
print(f"Váš aktuální zůstatek v peněžence je {penize_hrace} Kč.")
def soucet_karet(ruka):
    vypocet = 0
    eso = 0
    for karta in ruka:
        hodnota = karta[:-1]
        vypocet += hodnoty_karet[hodnota]
        if hodnota == "A":
            eso += 1
    while vypocet > 21 and eso > 0:
        vypocet -= 10
        eso -= 1
    return vypocet

def pravidla_hry(soucet_hrace, soucet_dealer, sazka):
    global penize_hrace
    if soucet_hrace > 21:
        print("Přesáhl jste 21! Prohrál jste.")
        return "prohra"
    elif soucet_dealer > 21:
        print("Dealer přesáhl 21! Vyhrál jste.")
        penize_hrace += sazka * 2
        return "vyhra"
    elif soucet_hrace > soucet_dealer:
        print("Máte větší součet karet než dealer. Vyhrál jste!")
        penize_hrace += sazka * 2
        return "vyhra"
    elif soucet_dealer > soucet_hrace:
        print("Máte nižší součet karet než dealer. Prohrál jste!")
        return "prohra"
    else:
        print("Remíza")
        penize_hrace += sazka
        return "remiza"

def hrat_blackjack():
    global penize_hrace
    while True:
        if penize_hrace < minimum_sazky:
            print("Nemáte dostatek peněz na další sázku. Konec hry.")
            break

        karty = vytvor_balicek()
        hrac_karty = [karty.pop(), karty.pop()]
        dealer_karty = [karty.pop(), karty.pop()]
        sazka = sazka_hry(penize_hrace)
        penize_hrace -= sazka

        while True:
            print("-------------------------------------------------------------------------------")
            print("                               𝘿𝙚𝙖𝙡𝙚𝙧                                          ")
            print("                Karty dealera:", *dealer_karty, "[ ? ]"                       )
            print("                                                                               ")
            print("                                                                               ")
            print(                                                                "\t" * 9,  "Hit" )
            print(                                                                "\t" * 9, "Double")
            print(                                                                "\t" * 9, "Stát" )
            print("              Vaše karty:", *hrac_karty,                   "\t" * 5, "Vzdat se"  )
            print("-------------------------------------------------------------------------------")
            print("1 - Hit | 2 - Double| 3 - Stát | 4 - Vzdat se")
            tah = input("Váš tah: ")

            if tah == "1":
                hrac_karty.append(karty.pop())
                if soucet_karet(hrac_karty) > 21:
                    print("Přesáhl jste 21!")
                    break
            elif tah == "3":
                while soucet_karet(dealer_karty) < 17:
                    dealer_karty.append(karty.pop())
                break
            elif tah == "4":
                print("Vzdáváte se, přicházíte o polovinu sázky.")
                penize_hrace += sazka // 2
                return
            else:
                print("Neplatný tah. Zkuste to znovu.")

        soucet_hrace = soucet_karet(hrac_karty)
        soucet_dealer = soucet_karet(dealer_karty)
        vysledek = pravidla_hry(soucet_hrace, soucet_dealer, sazka)

        print("Karty dealera:", *dealer_karty)
        print("Vaše karty:", *hrac_karty)
        print(f"Výsledek hry: {vysledek}")
        print(f"Aktuální zůstatek: {penize_hrace} Kč.")

        znovu = input("Chcete hrát znovu? (ano/ne): ").lower()
        if znovu != "ano":
            print("Díky za hru! Odcházíte s", penize_hrace, "Kč.")
            break

# Spuštění hry
print("********************************************************************************")
print("♠                                                                              ♠")
print("♥                          𝙑í𝙩𝙚𝙟𝙩𝙚 𝙫𝙚 𝙝ř𝙚 𝘽𝙡𝙖𝙘𝙠𝙅𝙖𝙘𝙠                            ♥")
print("♣                                                                              ♣")
print("*********************************************************************************") 
print(f"Máte u sebe {penize_hrace} Kč.")
hrat_blackjack()
