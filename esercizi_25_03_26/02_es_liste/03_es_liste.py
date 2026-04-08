
"""
    Autore: Samuel Nobile
    Data: 25/03/2026
    Titolo: Scrivi un programma per trovare il secondo numero più piccolo in una lista.

"""


##
## Funzioni:
##

def secondo_minore(lista : list, ) -> int:
    """
    Funzione: elementi_comuni
    Parametri formali:
    list lista -> lista da valutare
    Valore di ritorno:
    int -> secondo numero più piccolo
    """

    # ordiniamo la lista
    lista_ordinata = sorted(lista)

    # Valore di ritorno della funzione
    return lista_ordinata[1] # restituiamo il secondo valore nella lista 
    
# Sezione di input Dati
# Inizializzazioni variabili
lista1=[1,5,8] 
lista2=[3,1,10]
lista3=[9,5,8] 
lista4=[3,6,4]
# Elaborazione
# Eventuali sotto processi di Elaborazione
# Sezione di output
print(secondo_minore(lista1))
print(secondo_minore(lista2))
print(secondo_minore(lista3))
print(secondo_minore(lista4))

