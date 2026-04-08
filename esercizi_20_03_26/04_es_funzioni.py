import math

"""
Autore: Samuel Nobile
Data: 20/03/2026
Titolo: 
        La seguente è la formula per valutare numericamente il numero di Nepero e:
        


        4.a Scrivere una funzione che restituisca un valore approssimato di e all'ennesimo termine,
        dove N è inserito come parametro formale alla funzione.
        Esempio: calcola_e(3) restituirà il valore di e calcolato con tre termini della (1), cioè:

        e= 1/0! + 1/1! + 1/2! = 1 + 1 + 0.5 = 2.5
        
        La funzione calcola_e deve richiamare la funzione di calcolo del fattoriale.

        Scrivere il codice della funzione e il programma principale che la chiama chiedendo in input
        il numero N.



        4.b Supponendo di porre il numero di Nepero = 2.718281828459045 dico che
        errore = calcola_e(N) - Nepero
        sia l'errore che commetto nella valutazione di e.
        Modificare la funzione che restituisce la valutazione di e con N termini andando a far
        restituire anche l'errore commesso nella valutazione.
        Suggerimento: la funzione calcola_e(N) dovrà restituire due valori, 2.718281828459045
        potrebbe essere memorizzato in una variabile globale.
        esempio: valuta_e(3) restituisce il valore calcolato nel punto 4.a 2.5 e 0,218281828459045
        che rappresenta la differenza tra 2.718281828459045 e 2.5
        

"""

##
## Funzioni: def fattoriale(), def calcola_e()
##

def fattoriale(numero: int) -> int:
    """
    Funzione: calcola il fattoriale di un numero.
    int numero -> numero di cui fare il fattoriale

    Valore di ritorno: 
    int -> restituzione numero intero
    """
    prodotto_fattoriale = 1
    for i in range(1,numero + 1):
        prodotto_fattoriale*=i
    return prodotto_fattoriale
print(fattoriale(8))

# def calcola_e(numero: int) -> int:

#     """
#     Funzione: approssima numero all'ennesimo termine.
#     float numero -> numero da approssimare

#     Valore di ritorno: 
#     int -> restituzione numero intero
#     """
#     contatore = 0
#     somma_e = 0
#     while contatore <= numero:
#         somma_e+= 1/fattoriale(contatore)
#         contatore+=1
    
#     return somma_e

def calcola_e_errore(numero: int) -> int:

    """
    Funzione: approssima numero all'ennesimo termine. e calcola errore
    float numero -> numero da approssimare

    Valore di ritorno: 
    int -> restituzione numero intero
    """
    contatore = 0
    somma_e = 0
    while contatore <= numero:
        somma_e+= 1/fattoriale(contatore)
        # print(contatore,somma_e)
        contatore+=1
    
    errore = somma_e - NEPERO
    
    return somma_e, errore

# Sezione di input Dati
numero = int(input("Inserisci un numero: "))
# Inizializzazioni variabili

NEPERO = 2.718281828459045
# Elaborazione

# Eventuali sotto processi di Elaborazione
# Sezione di outputs
print(calcola_e_errore(numero))