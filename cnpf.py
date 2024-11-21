from cnpj import CNPJClient
from pprint import pprint

while True:
    cnpj_client = CNPJClient()
    cnpj = input("Entre com um cnpj para consulta ou /'S/' para sair: ")
    if cnpj.upper() == "S":
        break
    else:
        resultado = cnpj_client.cnpj(cnpj)
        print(resultado)
        # ender = []
        # ender = resultado["endereco"]
        # bprint(ender["logradouro"])
