"""
 effectue quelques test pour afficher ceux qui sont premiers
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
        verifie si un nombre est premier
    """
    if p<2:
        return False
    for i in range(2,int(sqrt(p))+1):
        if p%i == 0:
            return False
    return True
#j'ai découvert en ce jour que 0 et 1 n'étaient pas premiers.




#### Fonction principale


def main():
    """
        fonction principale
    """
    # vos appels à la fonction secondaire ici
    isprime(669)
    isprime(777)
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
