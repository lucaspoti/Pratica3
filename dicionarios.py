meu_dicionario = {}
meu_dicionario['codigo1'] = 'Python'
meu_dicionario['codigo2'] = 'Java'
meu_dicionario['codigo3'] = 'PHP'
print("Conteúdo de 'meu_dicionario':", meu_dicionario)
print("Tipo de dados de 'meu_dicionario':", type(meu_dicionario))
print("Valor da chave 'codigo1' usando get:", meu_dicionario.get('codigo1'))
print("Tamanho de 'meu_dicionario':", len(meu_dicionario))
dicionario_frutas = dict({
    1: {'nome': 'limão', 'tipo': 'ácida'},
    2: {'nome': 'laranja', 'tipo': 'ácida'},
    3: {'nome': 'manga', 'tipo': 'semiácida'},
    4: {'nome': 'maçã', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'}
})
print("Chave 1 - Nome:", dicionario_frutas[1]['nome'], "Tipo:", dicionario_frutas[1]['tipo'])
print("Chave 2 - Nome:", dicionario_frutas[2]['nome'], "Tipo:", dicionario_frutas[2]['tipo'])
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']}, Tipo: {valor['tipo']}")
