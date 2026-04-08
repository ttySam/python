
"""
    Autore: Samuel Nobile
    Data: 25/03/2026
    Titolo: Scrivere un programma Python per dividere una data lista in due parti in cui viene data la
            lunghezza della prima parte della lista.

            Esempio:
            Lista originale: [1, 1, 2, 3, 4, 4, 5, 1]

            Lunghezza della prima parte della lista: 3

            Output : Prima parte: [1, 1, 2] ,
            Seconda parte: [3, 4, 4, 5, 1]
"""


##
## Funzioni:
##

def dividi_lista(lista: list, divisore: int ) -> str:
    """
    Funzione: divide la lista in due. La prima lista è della lunghezza passata al programma come parametro
    Parametri formali:
    list lista -> lista da valutare
    Valore di ritorno:
    str -> stringa contente le due liste divise
    """
    # se il divisore è maggiore degli elementi contenuti nella lista, restituiamo un errore
    if divisore > len(lista):
        return "Non ci sono abbastanza elementi nella lista"
    
    # la prima lista inizia dal primo elemento nella lista e arriva fino al divisore escluso
    lista1 = lista[0:divisore]

    if len(lista1) == divisore:
        lista2 = []
    # la seconda lista inizia da divisore fino alla fine della lista
    lista2 = lista[divisore:]
    # Valore di ritorno della funzione
    return f"Prima Parte: {lista1}\nSeconda Parte: {lista2}"
    
# Sezione di input Dati
# Inizializzazioni variabili
lista = [1, 1, 2, 3, 4, 4, 5, 1]
# Elaborazione
# Eventuali sotto processi di Elaborazione
# Sezione di output
print(dividi_lista(lista, 5))
print(dividi_lista(lista, 9))


