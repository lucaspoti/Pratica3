def calcular_media(notas):
    return sum(notas) / len(notas)
def verificar_reprovacao(media):
    return media < 6
def relatorio_reprovados(dados_alunos, matriculas_reprovados):
    for matricula in matriculas_reprovados:
        aluno = dados_alunos[matricula]
        print(f"Aluno Reprovado: {aluno['nome']} – Matrícula: {matricula} – Média Final: {aluno['media']}")
