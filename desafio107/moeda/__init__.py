from desafio107 import form


def dobro(num, foo=False):
    num = num * 2
    if foo:
        return form.form(num)
    else:
        return num


def metad(num, foo=False):
    num = num / 2
    if foo:
        return form.form(num)
    else:
        return num


def aumen(num, acres=0, foo=False):
    num = num + (num * acres) / 100
    if foo:
        return form.form(num)
    else:
        return num


def reduz(num, decr=0, foo=False):
    num = num - (num * decr) / 100
    if foo:
        return form.form(num)
    else:
        return num





