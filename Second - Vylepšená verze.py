from colorama import Fore, Style, init

# Inicializace knihovny colorama (pro Windows)
init(autoreset=True)


def je_cislo(vstup):  # Rozlišuje, zda je vstup číslo nebo text
    if vstup.isdigit():
        cislo = int(vstup)
        if cislo < 0 or cislo > 100:  # Pokud je číslo mimo rozsah, vyhodí hlášku
            return "Číslo mimo rozsahu od 0 do 100."
        return cislo_text(cislo)  # Pošle do funkce pro převod čísla na text
    else:
        return text_cislo(vstup)  # Pošle do funkce pro převod textu na číslo


def text_cislo(vstup):
    # Slovníky pro převod čísla na text
    jednotky = {"nula": 0, "jedna": 1, "dva": 2, "tři": 3, "čtyři": 4, "pět": 5, "šest": 6, "sedm": 7, "osm": 8,
                 "devět": 9}
    desitky = {"deset": 10, "jedenáct": 11, "dvanáct": 12, "třináct": 13, "čtrnáct": 14, "patnáct": 15,
                "šestnáct": 16, "sedmnáct": 17, "osmnáct": 18, "devatenáct": 19, "dvacet": 20, "třicet": 30,
                "čtyřicet": 40, "padesát": 50, "šedesát": 60, "sedmdesát": 70, "osmdesát": 80, "devadesát": 90,
                "sto": 100}

    vstup = vstup.lower()  # Převádí text na malá písmena
    cisla = vstup.split()  # Rozdělení textu na jednotlivá slova

    vysledek = 0  # Nastavuje počáteční hodnotu na 0

    for slovo in cisla:  # Prochází jednotlivé slova
        if slovo in desitky:
            vysledek += desitky[slovo]
        elif slovo in jednotky:
            vysledek += jednotky[slovo]
        else:
            return "Neplatný vstup"  # Vyhazuje hlášku, pokud je vstup neplatný

    return vysledek


def cislo_text(cislo):
    if 20 <= cislo < 100:
        desitky = cislo // 10
        prvni_cislo = {2: "Dvacet", 3: "Třicet", 4: "Čtyřicet", 5: "Padesát", 6: "Šedesát", 7: "Sedmdesát",
                       8: "Osmdesát", 9: "Devadesát"}
        jednotky = cislo % 10
        druhe_cislo = {0: "", 1: " jedna", 2: " dva", 3: " tři", 4: " čtyři", 5: " pět", 6: " šest", 7: " sedm",
                       8: " osm", 9: " devět"}

        return prvni_cislo[desitky] + druhe_cislo[jednotky]

    if cislo == 0:
        return "Nula"

    if cislo == 100:
        return "Sto"

    if 1 <= cislo < 10:
        prvni_cislo = {1: "Jedna", 2: "Dva", 3: "Tři", 4: "Čtyři", 5: "Pět", 6: "Šest", 7: "Sedm", 8: "Osm",
                       9: "Devět"}
        return prvni_cislo[cislo]

    if 10 <= cislo < 20:
        dvojcisli = {10: "Deset", 11: "Jedenáct", 12: "Dvanáct", 13: "Třináct", 14: "Čtrnáct", 15: "Patnáct",
                     16: "Šestnáct", 17: "Sedmnáct", 18: "Osmnáct", 19: "Devatenáct"}
        return dvojcisli[cislo]


if __name__ == "__main__":
    # Červený a tučný "XX"
    red_bold_xx = Fore.RED + Style.BRIGHT + "XX" + Style.RESET_ALL
    red_bold_XXX = Fore.RED + Style.BRIGHT + "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" + Style.RESET_ALL
    red_bold_text = Fore.RED + Style.BRIGHT + "Zadej číslo nebo textový vstup: " + Style.RESET_ALL
    green_bold_input = Fore.GREEN + Style.BRIGHT  # Zelený text pro input
    red_output = Fore.RED + Style.BRIGHT  # Červený text pro výstup

    # Vypíše designovaný text
    print(f"{red_bold_XXX}")
    print(f"{red_bold_XXX}")
    print(f"{red_bold_xx}                                               {red_bold_xx}")
    print(f"{red_bold_xx}  Program pro převod čísla na text a obráceně  {red_bold_xx}")
    print(f"{red_bold_xx}                                               {red_bold_xx}")
    print(f"{red_bold_XXX}")
    print(f"{red_bold_XXX}")
    print("")

    # Zadání vstupu zeleně
    vstup = input(green_bold_input + red_bold_text)

    # Výstup převedeného čísla nebo textu červeně
    text = je_cislo(vstup)  # Zde voláme funkci je_cislo a ukládáme výstup do proměnné text
    print(f"{red_output}Převedené číslo nebo text: {Fore.GREEN}{text}")


