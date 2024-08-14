
meu_dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}
meu_dicionario.update({
    2: {'nome': 'João', 'idade': 32, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})
print("Dicionário atualizado:", meu_dicionario)
copia_dicionario = meu_dicionario.copy()
elemento_removido = meu_dicionario.pop(1)
print("Elemento removido com pop:", elemento_removido)
print("Dicionário após remoção com pop:", meu_dicionario)
ultimo_elemento_removido = meu_dicionario.popitem()
print("Último elemento removido com popitem:", ultimo_elemento_removido)
print("Dicionário após remoção com popitem:", meu_dicionario)
meu_dicionario.clear()
copia_dicionario.clear()
print("Primeiro dicionário após clear:", meu_dicionario)
print("Cópia do dicionário após clear:", copia_dicionario)
chaves = ['a', 'b', 'c']
valor_padrao = 0
novo_dicionario = dict.fromkeys(chaves, valor_padrao)
print("Conteúdo de novo_dicionario com items():", novo_dicionario.items())
print("Chaves de novo_dicionario com keys():", novo_dicionario.keys())
print("Valores de novo_dicionario com values():", novo_dicionario.values())
