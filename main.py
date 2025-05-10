import random                                                                                                          

znacky_karet = ['♠', '♥', '♦', '♣']                                          # pole ve kterém jsou znaky pro karty
hodnoty_karet = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7,              # pole ve kterém jsou hodnoty karet a jejich "názvy"
'8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
pocatecni_penize = 10000                                                     # proměnná s hodnotou 10 000
penize_hrace = pocatecni_penize                                              # proměnná která není napsána na "tvrdo"
minimum_sazky = 500                                                          # proměnná s hodnotou 500 pro sázku

def vytvor_balicek():                                                        # funkce, která má zamíchat karty v poli hodnoty a znaky 
    karty = []                                                               # balíček karet kam se uloží karty se znaky                                                                
    for hodnota in hodnoty_karet:                                            # pro každou hodnotu karty
        for znacka in znacky_karet:                                          # pro každou značku karty
            karty.append(hodnota + znacka)                                   # pridá kartu do balíčku
    random.shuffle(karty)                                                    # zamíchá balíček karet
    return karty                                                             # return vrátí hodnotu karty pro 

def sazka_hry(penize_hrace):                                                 # funkce pro zadání sázky
    while True:                                                              # smyčka pro opakované zopakování sázky
        try:
            vstup_sazky = input(f"Minimum pro sázku je {minimum_sazky} Kč. Kolik peněz chcete vsadit nebo zadejte 'all in'? ")
            if vstup_sazky.lower() == "all in":                              # pokud hráč zadá all in tak nečekaně zadá všechny své peníze 
                return penize_hrace                                          # hráč vsadí všechny své peníze
            
            sazka = int(vstup_sazky)                                         # převede vstupní sázku na číslo
            
            if sazka < minimum_sazky:                                        # pokud je sázka menší než minimální
                print("Musíte vsadit alespoň 500 Kč.")

            elif sazka > penize_hrace:                                       # pokud je sázka větší než hráčovi peníze
                print("Tolik peněz u sebe nemáte!")
            else:
                return sazka                                                 # pokud bude sázka vyhovavat tak ji vrátí 
        except:
            print("Prosím, zadejte částku jako číslo.")                      # ošetření proti chybám, kdyby hráč zadal colik jiného než číslo nebo "all in"

def soucet_karet(ruka):                                                      # funkce na výpočet součtu hodnot karet v ruce
    vypocet = 0                                                              # proměná vypocet je nastavena na 0
    eso = 0                                                                  # proměná eso je nastavena na 0

    for karta in ruka:                                                       # pro každou kartu v ruce
        hodnota = karta[:-1]                                                 # vrátí hodnotu bez značky
        if hodnota == "A":                                                   # pokud je hodnota rovna A jako Eso
            eso += 1                                                         # zvyšuje počet es
            vypocet += 11                                                    # přičte hodnotu esa
        else:
            vypocet += hodnoty_karet[hodnota]                                # přičte do proměnné vypocet číselnou hodnotu karty podle jejího názvu

    
    while vypocet > 21 and eso > 0:                                          # pokud je součet větší než 21 a máme esa
        vypocet -= 10                                                        # odebírá se 10 za každé eso, aby se hodnotilo jako 1 místo 11
        eso -= 1                                                             # snižuje počet es

    return vypocet                                                           # vrátí konečný součet
def pravidla_hry(soucet_hrace, soucet_dealer, sazka):                        # funkce na vyhodnocení výsledků
    global penize_hrace                                                      # program bude moct pracovat s proměnnou penize_hrace i mimo funkci
    if soucet_hrace > 21:                                                    # pokud hráč přesáhne 21 tak se vrátí prohra
        return "prohra"
    elif soucet_dealer > 21:                                                 # pokud dealer přesáhne 21 tak se vrátí výhra a také hráč dostane 2x svoji sázku
        print("Dealer přesáhl 21, prohrává!")
        penize_hrace += sazka * 2
        return "vyhra"
    elif soucet_hrace > soucet_dealer:                                       # pokud hráč bude mít větší součet karet než dealerovi karty tak hráč vyhrává 
        penize_hrace += sazka * 2
        return "vyhra"
    elif soucet_hrace < soucet_dealer:                                       # pokud hráč bude mít nižší součet karet než dealerovi karty tak hráč prohrává
        return "prohra"
    else:
        print("Remíza")                                                      # jinak se vrátí remíza a hráč dostane zpátky své vsazené peníze
        penize_hrace += sazka
        return "remiza"
    
def hrat_blackjack():                                                        # funkce pro zahájení hry
    global penize_hrace                                                       
    while True:                                                              # smyčka pro opakování hry/kola
        if penize_hrace < minimum_sazky:                                     # pokod bude mít hráč míž méně peněz než je minimální sázka tak konec hry
            print("Nemáte dostatek peněz na další sázku. Konec hry.")
            break                                                            # pro ukončení programu

        karty = vytvor_balicek()                                             # vytvoření zamíchaného balíčku karet
        hrac_karty = [karty.pop(), karty.pop()]                              # do pole hrac_karty se přidají dvě karty z pole karty a také se odstraní z toho pole
        dealer_karty = [karty.pop()]                                         # dealer dostane jednu kartu
        sazka = sazka_hry(penize_hrace)                                      # hráč zadá sázku

        if sazka == penize_hrace:                                            # pokud hráč vsadí všechny peníze
            penize_hrace = 0
            print(f"Vsadil jste: {sazka} Kč.")                               # vypíše se aktuální stav hráčovi sázky
        else:
            penize_hrace -= sazka                                            # zadaná sázka se odečte od hráčovi peněženky
            print(f"Vsadil jste {sazka} Kč.")

        print(f"Váš aktuální zůstatek v peněžence je {penize_hrace} Kč.")    # aktuální stav o zůstatku v peněžence

        vzdal_se = False                                                     # Nastavení na False na začátku každé hry

        while True:
                print("-------------------------------------------------------------------------------")
                print("                               𝘿𝙚𝙖𝙡𝙚𝙧                                          ")
                print("                Karty dealera:", *dealer_karty, "[ ? ]"                         )  # * vypíše všechny karty z pole
                print("                                                                               ")
                print(                                                               "\t" * 8,"1 - Hit")  # tabulátory (\t) pro design a * pro kolikrát
                print(                                                            "\t" * 8, "2 - Double")
                print(                                                            "\t" * 8, "3 - Stát" )
                print("              Vaše karty:", *hrac_karty,               "\t" * 4, "4 - Vzdat se" )
                print("-------------------------------------------------------------------------------")
                tah = input("Váš tah: ")                                                                  # hráč je na tahu

                if tah == "1":                                                                            # pokud tah bude roven 1
                    hrac_karty.append(karty.pop())                                                        # hráč dostane další kartu z pole karty
                    if soucet_karet(hrac_karty) > 21:                                                     # jestliže bude mít hráč více jak 21
                        print("Přesáhl jste 21! Prohráli jste!")                                          # print vypíše
                        break                                                                             # konec tahu

                elif tah == "2":                                                                          # jestli tah bude roven 2
                    if penize_hrace < sazka:                                                              # pokud hráč nebude mít na zdvojnásobení sázky
                        print("Nemáte dostatek peněz na zdvojnásobení sázky!")                            # nemá dostatek peněž
                        continue                                                                          # ale pokud ano program bude pokračovat dále
                    penize_hrace -= sazka                                                                 # sázka se ještě jednou odečte od jeho peněz
                    sazka *= 2                                                                            # a následně se sázka zdvojnásobí
                    hrac_karty.append(karty.pop())                                                        
                    print("Zvolili jste Double – berete jednu kartu a stojíte.")                          # po zvolení Double, hráč bude táhnout už pouze jednu kartu
                    if soucet_karet(hrac_karty) > 21:                                                     # pokud přesáhne tak prohrál
                        print("Přesáhl jste 21 po zdvojnásobení! Prohrál jste.")
                    break

                elif tah == "3":                                                                          # když hráč zvolí stát tak se tím přeskočí jeho tah a hraje dealer
                    break

                elif tah == "4":                                                                          # ale pokud se vzdá
                    vzdal_se = True                                                                       # Nastavení na True, pokud hráč zvolí "Vzdat se"
                    print("Vzdáváte se, přicházíte o polovinu sázky.")                                    
                    penize_hrace += sazka // 2                                                            # dealer vrátí hráči polovinu jeho vsazené částky
                    print(f"Aktuální zůstatek: {penize_hrace} Kč.")                                       # výpis aktuálního stavu jeho peněženky
                    break

        if not vzdal_se:                                                                                  # vyhodnocení výsledků, pokud hráč se nevzdal
            if soucet_karet(hrac_karty) <= 21:                                                            # jestlíže bude mít hráč méně nebo rovno 21
                while soucet_karet(dealer_karty) < 17:                                                    # dealer hraje dokud nebude mít alespoň 17
                    dealer_karty.append(karty.pop())                                                      # přidává karty dealerovi 
                    if soucet_karet(dealer_karty) > 21:                                                   # pokud přesáhne tak se vyhodnotí výsledek
                        break  

            soucet_hrace = soucet_karet(hrac_karty)                                                       # volání funkce součet karet hráče
            soucet_dealer = soucet_karet(dealer_karty)                                                    # volání funkce součet karet dealera
            vysledek = pravidla_hry(soucet_hrace, soucet_dealer, sazka)                                   # výsledek hry s voláním funkcí pravidly pro vyhodnocení

            print("Karty dealera:", *dealer_karty)                                                        # dealerovi výsledné karty 
            print("Vaše karty:", *hrac_karty)                                                             # hráčovi výsledné karty 
            print(f"Výsledek hry: {vysledek}")                                                            # vyhodnocení hry
            print(f"Aktuální zůstatek: {penize_hrace} Kč.")

    
        znovu = input("Chcete hrát znovu? (ano/ne): ").lower()                                           # po každé hře se program zeptá hráče, jestli chce pokračovat
        if znovu != "ano":                                                                               # pokud hráč zadá cokoliv jiného než "ano" tak se program ukončí (bylo by dobré vzdy naspat "ne" pro jasné rozhodnutí)
            print(f"Díky za hru! Odcházíte s {penize_hrace} Kč.")
            break

print("********************************************************************************")                # první co se zobrazí když spustíte program
print("♠                                                                              ♠")
print("♥                          𝙑í𝙩𝙚𝙟𝙩𝙚 𝙫𝙚 𝙝ř𝙚 𝘽𝙡𝙖𝙘𝙠𝙅𝙖𝙘𝙠                            ♥")
print("♣                                                                              ♣")
print("*********************************************************************************") 
print(f"Máte u sebe {penize_hrace} Kč.")
hrat_blackjack()                                                                                         # spuštění hry