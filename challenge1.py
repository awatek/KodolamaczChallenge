def main():
    print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:")
    liczba1 = float(input())
    operacja = str(input())
    liczba2 = float(input())
    if operacja == "+":
        wynik = liczba1 + liczba2
    elif operacja == "-":
        wynik = liczba1 - liczba2
    elif operacja == "*":
        wynik = liczba1 * liczba2
    elif operacja == "/":
        wynik = liczba1 / liczba2 
    else:
        wynik = liczba1 % liczba2
    print ("Twój wynik to: " + str(wynik))
    print("Chcesz wykonać kolejne działanie? Wpisz literę t lub n.")
    decyzja = str(input())
    if decyzja == "t":
        main()
    else:
        print("Działanie zakończone.")
if __name__ == "__main__":
    main()