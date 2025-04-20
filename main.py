import random
znacky_karet = ['♠', '♥', '♦', '♣']
hodnoty_karet = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
penize_hrace = 10000
karty = []
dealer_karty = []
hrac_karty = []
nova_karta = []


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
print(f"Máte u sebe {penize_hrace} Kč.")
def sazka_hry(penize_hrace):
    while True:
        try:
            vstup_sazky = input("Minimum pro sázku je 500 Kč. Kolik peněz chcete vsadit nebo zadejte 'all in'? ")

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

hrac_karty.append(karty.pop())
hrac_karty.append(karty.pop())

dealer_karty.append(karty.pop())
dealer_karty.append(karty.pop())

print("-------------------------------------------------------------------------------")
print("                               𝘿𝙚𝙖𝙡𝙚𝙧                                          ")
print("                Karty dealera:", dealer_karty[0], "[ ? ]"                       )
print("                                                                               ")
print(                                                                "\t" * 9,  "hit" )
print(                                                                "\t" * 9, "double")
print(                                                                "\t" * 9, "stát" )
print("              Vaše karty:", hrac_karty[0], hrac_karty[1], "\t" * 5, "vzdat se"  )
print("-------------------------------------------------------------------------------")

def prubeh_hry():
    while True:
            hrac_tah = input("Váš tah 1/2/3/4:")

            if hrac_tah.lower() == "4":
                print("Je nám líto že odcházíte.")
                print("--------------------------- Konec hry -------------------------------")
                break     

            if hrac_tah.lower() == "1":
                nova_karta = karty.pop()
                hrac_karty.append(nova_karta)
                print("-------------------------------------------------------------------------------")
                print("                               𝘿𝙚𝙖𝙡𝙚𝙧                                          ")
                print("                Karty dealera:", dealer_karty[0], "[ ? ]"                       )
                print("                                                                               ")
                print(                                                                "\t" * 9,  "hit" )
                print(                                                                "\t" * 9, "double")
                print(                                                                "\t" * 9, "stát" )
                print("              Vaše karty:", hrac_karty[0], hrac_karty[1], nova_karta, "\t" * 5, "vzdat se"  )
                print("-------------------------------------------------------------------------------")
prubeh_hry()
                
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

soucet_karet(hrac_karty)

         

