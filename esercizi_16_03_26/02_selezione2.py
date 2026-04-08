
"""
Autore: Samuel Nobile
Data: 13/03/2026
Titolo: 
        Scrivere un programma che legga le lunghezze dei tre lati di un triangolo a, b, c e ne calcoli
        il perimetro e l'area S, quest'ultima tramite la formula di Erone
        S = sqrt(p(p-a)(p-b)(p-c))
        dove p è il semiperimetro
"""

# Sezione di input Dati
a = float(input("Inserisci un numero: "))
b = float(input("Inserisci un numero: "))
c = float(input("Inserisci un numero: "))
# Inizializzazioni variabili
perimetro = 0
area = 0
semiperimetro = 0
# Elaborazione
if a > (b + c) or b > ( a + c) or c > (a + b):
    print("Con questi numeri non è possibile creare un triangolo")
elif a<=0 or b<=0 or c<=0:
    print("Tutti i numeri devono essere maggiori di zero")
# Eventuali sotto processi di Elaborazione
else:
    perimetro = a+b+c
    semiperimetro= perimetro / 2
    area = (semiperimetro*(semiperimetro-a)*(semiperimetro-b)*(semiperimetro-c))**0.5
# Sezione di output
    print("Il perimetro misura ", perimetro)
    print("L'area misura ", area)

