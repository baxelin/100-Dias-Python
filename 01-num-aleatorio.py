import random

def numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo - 1)

if __name__ == "__main__":
    print("Gerando um número entre 1 e 100...")
    print(numero_aleatorio(1, 100))