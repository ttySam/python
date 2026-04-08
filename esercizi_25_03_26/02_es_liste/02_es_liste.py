
"""
    Autore: Samuel Nobile
    Data: 25/03/2026
    Titolo: Scrivere un programma che date due liste stampi "OK" se hanno almeno un membro comune 
            altrimenti stampi "KO".

            Esempio:
            * lista1=[1,5,8] lista2=[3,1,10] -> output: "OK"
            * lista1=[1,5,8] lista2=[3,11,10] -> output: "KO"


"""


##
## Funzioni:
##


def elementi_comuni(lista1 : list, lista2: list) -> str:
    """
    Funzione: elementi_comuni
    Parametri formali:
    list lista1 -> lista da valutare
    list lista2 -> lista da valutare
    Valore di ritorno:
    str -> 'OK' se hanno elementi in comune, 'KO' se non ne hanno
    """

    # iteriamo attraverso una delle due liste
    for i in lista1:
        # se almeno un elemento è nella lista restituiamo 'OK' sennò 'KO'
        if i in lista2:
            return "OK" # Valore di ritorno della funzione
        return "KO"     # Valore di ritorno della funzione


# Sezione di input Dati
# Inizializzazioni variabili
lista1=[1,5,8] 
lista2=[3,1,10]

lista3=[9,5,8] 
lista4=[3,6,4]
# Elaborazione
# Eventuali sotto processi di Elaborazione
# Sezione di output
print(elementi_comuni(lista1, lista2))
print(elementi_comuni(lista3, lista4))
