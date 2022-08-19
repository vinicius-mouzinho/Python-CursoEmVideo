# Faça um programa que tenha uma função chamada notas(), que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações: - Quantidade de notas; - A maior nota; - A menor nota; - A média da turma;
# - A situação(opcional). Adicione também as docstrings da função.
def notas(* n, sit=False):
    """
        -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos, aceita-se várias.
    :param sit: Valor opcional explicando, indicando se se deve ou não adicionar a situação da turma.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r




