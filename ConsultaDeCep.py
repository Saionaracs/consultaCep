import requests

cep = input('Digite o CEP: ')
cep = cep.replace('-', '')

while True:
    # Validação do CEP
    while len(cep) != 8 or not cep.isdigit():
        print('CEP inválido. Digite um CEP com 8 números.')
        cep = input('Digite o CEP: ')
        cep = cep.replace('-', '')
        
        # Consulta a API
    url = f"https://brasilapi.com.br/api/cep/v2/{cep}"
    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:

      print('CEP:', dados['cep'])
      print('Rua:', dados['street'])
      print('Cidade:', dados['city'])
      print('Estado:', dados['state'])
      print('Bairro:', dados['neighborhood'])
      break

    else:
      print('CEP não encontrado.')
      cep = input('Digite outro CEP: ')
      cep = cep.replace('-', '')
