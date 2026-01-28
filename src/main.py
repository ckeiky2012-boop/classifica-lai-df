import sys
import os

# Garante que o Python encontre o detector.py
sys.path.append(os.path.dirname(__file__))

from detector import contains_personal_data


def main():
    print("Analisador de Pedidos de Acesso à Informação\n")

    texto = input("Digite o texto do pedido:\n")

    resultado = contains_personal_data(texto)

    if resultado:
        print("Risco de privacidade detectado")
    else:
        print("Sem risco de privacidade identificado")


if __name__ == "__main__":
    main()
