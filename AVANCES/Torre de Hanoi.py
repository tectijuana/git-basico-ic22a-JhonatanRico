def hanoi(n):
    if n == 1:
        count = 1
    else:
        count = (2 * hanoi(n-1) + 1)
    return count

def main():
    n = eval(input("Introduzca el número total de discos de la Torre de Hanói:"))
    print("{} los discos deben moverse: {} veces".format(n, hanoi(n)))

if __name__ == "__main__":
    main()

