from operacoes import calcular_media, verificar_reprovacao, relatorio_reprovados
dados_alunos = {
    26: {'nome': 'Maria', 'notas': [8.0, 7.0, 5.0, 9.0]},
    101: {'nome': 'Ana', 'notas': [9.0, 9.0, 8.0, 9.0]},
    13: {'nome': 'João', 'notas': [6.0, 5.0, 5.0, 5.0]},
    37: {'nome': 'Ágatha', 'notas': [8.0, 6.0, 7.5, 9.0]},
    72: {'nome': 'Joaquim', 'notas': [6.0, 5.5, 5.0, 7.0]},
    5: {'nome': 'Félix', 'notas': [10.0, 8.0, 8.0, 8.0]},
}
matriculas_reprovados = []
for matricula, info_aluno in dados_alunos.items():
    media = calcular_media(info_aluno['notas'])
    dados_alunos[matricula]['media'] = media
    if verificar_reprovacao(media):
        matriculas_reprovados.append(matricula)
if matriculas_reprovados:
    relatorio_reprovados(dados_alunos, matriculas_reprovados)
else:
    print("Nenhum aluno reprovado.")
