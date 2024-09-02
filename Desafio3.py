import json

# código estruturado para usar arquivo .JSON, considerando que o nome do arquivo seria faturamento.

with open('faturamento.json') as f:
    dados = json.load(f)

faturamento = dados["faturamento_diario"]
faturamento = [x for x in faturamento if x > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for x in faturamento if x > media_mensal)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
