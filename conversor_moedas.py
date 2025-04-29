def converter_moeda(valor, de, para):
    taxas = {
        'euro': {'real': 5.5, 'dolar': 1.1, 'won': 1500},
        'real': {'euro': 0.18, 'dolar': 0.20, 'won': 270},
        'dolar': {'euro': 0.91, 'real': 5.0, 'won': 1350},
        'won': {'euro': 0.00067, 'real': 0.0037, 'dolar': 0.00074}
    }

    try:
        taxa = taxas[de][para]
        resultado = valor * taxa
        return round(resultado, 2)
    except KeyError:
        print("Conversão não suportada.")
        return None


opcoes = {
    "1": "euro",
    "2": "real",
    "3": "dolar",
    "4": "won"
}

print("=== Conversor de Moedas ===")
print("Escolha a moeda de origem:")
print("1 - Euro\n2 - Real\n3 - Dolar\n4 - Won")
origem = input("Digite o número correspondente a Moeda para converter De: ").strip()

print("\nEscolha a moeda de destino:")
print("1 - Euro\n2 - Real\n3 - Dolar\n4 - Won")
destino = input("Digite o número correspondente a Moeda para converter Para: ").strip()

valor = float(input("\nDigite a Quantia a ser convertido: "))

moeda_origem = opcoes.get(origem)
moeda_destino = opcoes.get(destino)

if moeda_origem and moeda_destino:
    print(f"\nVocê quer converter {valor} de {moeda_origem} para {moeda_destino}")
    resultado = converter_moeda(valor, moeda_origem, moeda_destino)
    if resultado is not None:
        print(f"Resultado: {resultado} {moeda_destino}")
else:
    print("Opção inválida de moeda. Por favor, insira números válidos para as moedas.")
