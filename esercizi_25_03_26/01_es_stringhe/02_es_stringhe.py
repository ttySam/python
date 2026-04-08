"""
    Autore: Samuel Nobile
    Data: 25/03/2026
    Titolo: scrivere un programma che dica se una stringa è palindroma.
            Esempio:
            str="ABBA" PALINDROMA
            str="PIPPO" NON PALINDROMA


"""


##
## Funzioni: def is_pal()
##


def is_pal(string:str) -> str:
    """
    Funzione: controlla se una parola è palindroma
    Parametri formali:
    string -> stringa da valutare
    Valore di ritorno:
    str -> stringa che dice se la parola è palindroma o no

    """
    if string == "":
        return "La stringa è vuota" # se la stringa è vuota restituiamo un errore
    elif string == string[::-1]:
        return f"{string} è una parola palindroma" # se la stringa è palindroma
    else:
        return f"{string} non è una parola palindroma" # se la stringa non è palindroma



# Sezione di input Dati
# Inizializzazioni variabili
stringa = "Carro"
stringa2= "itopinonavevanonipoti"
stringa3= ""

# Elaborazione
# Eventuali sotto processi di Elaborazione
# Sezione di output

print(is_pal(stringa))
print(is_pal(stringa2))
print(is_pal(stringa3))

