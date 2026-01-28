import sys
import os

# Garante que o Python encontre o detector.py
sys.path.append(os.path.dirname(__file__))

from detector import contains_personal_data

def main():
    print("Analisador de Pedidos de Acesso à Informação\n")

    text = input("Digite o texto do pedido:\n")

    result = contains_personal_data(text)

    if result:
        print("\nResultado: O pedido CONTÉM dados pessoais.")
    else:
        print("\nResultado: O pedido NÃO contém dados pessoais.")

if __name__ == "__main__":
    main()
