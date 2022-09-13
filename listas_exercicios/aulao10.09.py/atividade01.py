from csv import DictReader
import json
# criar script que converse .cvs em json
# Já converte arquivo csv em dicionário


def ler_arquivo_csv():
    # Open(quem,como)
    # quem -> caminho + nome do arquivo
    # como: 'r' ler, 'w': escreWer
    with open("entrada01.csv", "r") as arq_csv:
        # arq_csv = open(entrada01.csv, "r")
        leitor_csv = DictReader(arq_csv)
        registros = [
            registro
            for registro in leitor_csv
        ]
        #registros = []
        #
        print(registros)
    return registros


def salvar_arquivos_json(registros):
    with open(a.json, "w") as arq_json:
        json.dump(registros, salvar_arquivos_json)


def principal():
    registros = ler_arquivo_csv()
    salvar_arquivos_json(registros)


if __name__ == "__main__":
    principal()
