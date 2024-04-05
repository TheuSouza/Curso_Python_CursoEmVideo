def notas(*num, sit=False):
    """

    -> Função soma notas e retorna um dict com valores e situação do aluno.
    :param num: Recebe varios valores para analise.
    :param sit: Opção para retornar a situação do aluno.
    :return: Retorna o Dict com todos os dados.
    """
    boletim = dict()
    nu = list()
    for c in num:
        nu.append(c)
    media = sum(nu) / len(nu)
    boletim['Total'] = len(nu)
    boletim['Menor'] = min(nu)
    boletim['Maior'] = max(nu)
    boletim['Media'] = media
    if sit:
        if media > 7:
            boletim['Situação'] = 'Bom!'
        if 5 <= media <= 7:
            boletim['Situação'] = 'Razoavel...'
        if media < 5:
            boletim['Situação'] = 'Ruim!'
    return boletim


print('- ' * 40)
resp = notas(9, 9.5, 6, 5.5, 8, 2, sit=True)
print(resp)
print('- ' * 40)
