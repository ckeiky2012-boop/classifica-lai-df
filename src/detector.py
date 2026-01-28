import re

def contains_personal_data(text: str) -> bool:
    """
    Verifica se um texto contém dados pessoais básicos,
    como CPF, e-mail ou telefone.
    """

    patterns = [
        r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",          # CPF com pontuação
        r"\b\d{11}\b",                            # CPF sem pontuação
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",  # e-mail
        r"\b\d{2}\s?\d{4,5}-?\d{4}\b"             # telefone
    ]

    for pattern in patterns:
        if re.search(pattern, text):
            return True

    return False
