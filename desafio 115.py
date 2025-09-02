import json
# JSON para dicionário
json_str = '{"nome": "Igor", "idade": 25}'
dados = json.loads(json_str)
# Dicionário para JSON
novo_json = json.dumps(dados)
print(novo_json)
