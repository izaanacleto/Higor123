elementos_quimicos = {
    "h": {"nome": "Hidrogênio", "numero_atomico": 1, "massa_atomica": 1.008},
    "he": {"nome": "Hélio", "numero_atomico": 2, "massa_atomica": 4.0026},
    "li": {"nome": "Lítio", "numero_atomico": 3, "massa_atomica": 6.94},
    "be": {"nome": "Berílio", "numero_atomico": 4, "massa_atomica": 9.0122},
    "b": {"nome": "Boro", "numero_atomico": 5, "massa_atomica": 10.81},
    "c": {"nome": "Carbono", "numero_atomico": 6, "massa_atomica": 12.011},
    "n": {"nome": "Nitrogênio", "numero_atomico": 7, "massa_atomica": 14.007},
    "o": {"nome": "Oxigênio", "numero_atomico": 8, "massa_atomica": 15.999},
    "f": {"nome": "Flúor", "numero_atomico": 9, "massa_atomica": 18.998},
    "ne": {"nome": "Neônio", "numero_atomico": 10, "massa_atomica": 20.180}
}

sigla = ""
while not sigla == "sair":
    sigla = input("Digite a sigla do elemento químico: ").lower()
    if not sigla == "sair":
        elemento = elementos_quimicos.get(sigla)
        if elemento:
            print(f"Nome: {elemento['nome']}")
            print(f"Número Atômico: {elemento['numero_atomico']}")
            print(f"Massa Atômica: {elemento['massa_atomica']}")
        else:
            print("Elemento não encontrado.")
