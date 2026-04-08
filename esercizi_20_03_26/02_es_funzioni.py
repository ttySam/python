"""
Autore: Samuel Nobile
Data: 20/03/2026
Titolo: 
        Creare una funzione che abbia come parametri formali un numero arbitrario di valori numerici. 
        Si vuole che restituisca la somma dei soli numeri pari e il prodotto dei soli numeri dispari. 
        Successivamente creare un programma che richiami tale funzione e che stampi in output i risultati .
        No standard input.
"""

##
## Funzioni: def somma_moltiplica()
##

def somma_moltiplica(*params: int) -> str:

    """
    Funzione: somma numeri pari e moltiplica numeri dispari 
    int num -> primo numero
    int num2 -> secondo numero
    int num3 -> terzo numero
    int num4 -> quarto numero
    Valore di ritorno:
    str -> restituzione somma e prodotto
    """
    somma = 0
    prodotto = 1
    for num in params:
        if num % 2 == 0:
            somma+=num

        else:
            prodotto*=num

    return "La somma è " + str(somma) + ", il prodotto è " + str(prodotto)

# Sezione di input Dati

# Inizializzazioni variabili
# Elaborazione

print(somma_moltiplica(7,6,3,2))
# Eventuali sotto processi di Elaborazione
# Sezione di output