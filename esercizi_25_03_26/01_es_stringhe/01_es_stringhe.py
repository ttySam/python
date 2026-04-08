"""
    Autore: Samuel Nobile
    Data: 25/03/2026
    Titolo: Scrivere un programma per rimuovere l'n- esimo carattere da una stringa non vuota.
            Progettare una funzione che accetti la stringa, la posizione del carattere e restituisca la
            stringa modificata.


"""
from os import remove


##
## Funzioni: def mod_str()
##


def mod_str(string:str, n:int) -> str:

    """
    Funzione: Prende in input una stringa e un intero, e rimuove l'n-esimo carattere
    Parametri formali:
    str string -> stringa da modificare
    int n -> intero da usare per la selezione del carattere da rimuovere
    Valore di ritorno:
    str -> stringa aggiornata
    """
    if string == "":
        return "La stringa è vuota"
    lista_stringa = []
    for i in string: # iteriamo attraverso alla stringa
        lista_stringa.append(i) # aggiungiamo all'interno di una lista i singoli caratteri in ordine

    lista_stringa.pop(n) # rimuove l'elemento in posizione n dalla lista

    stringa_nuova = "".join(lista_stringa) # uniamo in una stringa gli elementi rimanenti della lista



    return stringa_nuova # Valore di ritorno della funzione

# Sezione di input Dati
# Inizializzazioni variabili
stringa_bella = "AllYouNeedIsLove"
# Elaborazione

# Eventuali sotto processi di Elaborazione

# Sezione di output
print(mod_str("lol", 2))
print(mod_str("", 2))


