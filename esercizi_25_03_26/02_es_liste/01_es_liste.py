
"""
    Autore: Samuel Nobile
    Data: 25/03/2026
    Titolo: Scrivere un programma python che rimuova gli elementi duplicati da una lista.
            Esempio:
            listaIN = [2,-4,5,6,5,5,2]
            listaOUT=[2,-4,5,6]


"""

##
## Funzioni: def remove_dupl()
##

def remove_dupl(lista:list) -> str:
    """
    Funzione: rimuove i duplicati da una lista
    Parametri formali:
    list lista -> lista da valutare
    Valore di ritorno:
    str -> stringa con la lista senza duplicati
    """
    lista_nuova = [] # inizializziamo una lista vuota

    if type(lista) != list:
        return "Non è una lista"
    
    elif len(lista) == 0: # se la lunghezza della lista è pari a zero restituiamo un messaggio
        return "La lista è vuota"

    else:
        for i in lista: #iteriamo attraverso la lista

            if i not in lista_nuova:    # se un elemento non è presente nella lista nuova, lo aggiungiamo
                lista_nuova.append(i)

        if lista_nuova == lista:
            return "La lista originale non contiene duplicati"

        return f"La lista senza duplicati: {lista_nuova}"


# Sezione di input Dati
# Inizializzazioni variabili
lista1 = [1 , 3, 4, 5, 5]
lista2 = [1, 2, 3, 4]
lista3 = []
lista4 = ""
# Elaborazione
# Eventuali sotto processi di Elaborazione
# Sezione di output
print(remove_dupl(lista1))
print(remove_dupl(lista2))
print(remove_dupl(lista3))
print(remove_dupl(lista4))

