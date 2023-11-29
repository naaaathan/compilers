from lexico import analizador_lexico


TERMINAIS = {'fun', 'id', 'number', 'if', 'then', 'else', 'while', 'do', 'for', 'to',
             'int', 'float', 'char', '{', '}', '+', '-', '*', '^', '/', '==', '<', '>', '$', ';', ':', ',', '(',
             ')', '='}


def eh_terminal(x):
    return x in TERMINAIS


def cria_tabela_sintatica():
    return {
        'S': {'fun': 1},
        'bloco': {'{': 2},
        'declaracao': {'id': 4, 'if': 4, 'while': 4, 'for': 4, 'int': 3, 'float': 3, 'char': 3},
        'tipo': {'int': 5, 'float': 6, 'char': 7},
        'lista_ids': {'id': 8},
        'lista_ids_linha': {';': 10, ',': 9},
        'comandos': {'id': 11, '}': 12, 'if': 11, 'while': 11, 'for': 11},
        'comando': {'id': 15, 'if': 13, 'while': 14, 'for': 14},
        'selecao': {'if': 16},
        'selecao_linha': {'id': 17, '{': 18, 'if': 17, 'while': 17, 'for': 17},
        'selecao_linha_linha': {'id': 10, '{': 20, 'if': 19, 'while': 19, 'for': 19},
        'repeticao': {'while': 21, 'for': 22},
        'repeticao_linha': {'id': 23, '{': 24, 'if': 23, 'while': 23, 'for': 23},
        'repeticao_linha_linha': {'id': 26, '{': 25, 'if': 26, 'while': 26, 'for': 22},
        'atribuicao': {'id': 27},
        'condicao': {'id': 28, 'number': 28, 'letra': 28},
        'expressao': {'id': 29, 'number': 30, 'letra': 30},
        'constante': {'number': 33, 'letra': 34},
        'op_relacional': {'==': 35, '>=': 36, '<=': 37, '<>': 38}
    }


def cria_producoes():
    return [
        [],
        ['fun', 'id', '(', ')', 'bloco'],
        ['{', 'declaracao', 'comandos', '}'],
        ['tipo', ':', 'lista_ids', ';', 'declaracao'],
        ['ε'],
        ['int'],
        ['float'],
        ['char'],
        ['id', 'lista_ids_linha'],
        [',', 'lista_ids'],
        ['ε'],
        ['comando', 'comandos'],
        ['ε'],
        ['selecao'],
        ['repeticao'],
        ['atribuicao'],
        ['if', '(', 'condicao', ')', 'then', 'selecao'],
        ['comando', 'else', 'selecao'],
        ['bloco', 'else', 'selecao_linha_linha'],
        ['comando'],
        ['bloco'],
        ['while', '(', 'condicao', ')', 'do', 'repeticao_linha'],
        ['for', 'repeticao_linha_linha'],
        ['comando'],
        ['bloco'],
        ['bloco', 'to', '(', 'condicao', ')'],
        ['comando', 'to', '(', 'condicao', ')'],
        ['id', '=', 'expressao', ";"],
        ['expressao', 'op_relacional', 'expressao'],
        ['id'],
        ['constante'],
        ['(', 'expressao', ')'],
        ['expressao', 'op_aritmetico', 'expressao'],
        ['number'],
        ['letra'],
        ['=='],
        ['>='],
        ['<='],
        ['<>']
    ]


class TabelaSintatica:
    def __init__(self):
        self.tabela = cria_tabela_sintatica()
        self.producao = cria_producoes()


def analisador_sintatico(analisador_lexico):
    tree = dict()
    stack = ["S"]

    # Carrega próximo token
    token = analisador_lexico.run()
    prox_token = token[0].tipo
    tabela_sintatica = TabelaSintatica()

    while stack:

        x = stack.pop()

        if eh_terminal(x):

            if x == prox_token:
                token = analisador_lexico.run()

                if token[0].tipo == "$":
                    print("Cadeia Aceita")
                    return "Cadeia Aceita"

                prox_token = token[0].tipo
                continue
            else:
                print(f"Erro! Token {token[0].atributo} não era esperado! Linha: {token[1]} | Coluna: {token[2]}")
                break
        else:
            if x not in tabela_sintatica.tabela:
                print(f"Erro! Linha: {token[1]} | Coluna: {token[2]}")
                print("Erro! A linguagem não foi reconhecida!")
                break
            else:
                try:
                    id_producao = tabela_sintatica.tabela[x][prox_token]
                    producoes = tabela_sintatica.producao[id_producao]
                    print(f"Vai para a produção {id_producao}")
                    print(f"Não é terminal, produções: {producoes}")
                    stack.extend(reversed([prod for prod in producoes if prod != 'ε']))
                    tree.update({x: reversed(producoes)})

                except KeyError:  # Não achou uma produção para o token
                    print("Analise Sintática - A linguagem não foi reconhecida!")

    if not stack:
        return "Analise Sintática - A linguagem foi reconhecida"
    return "Erro análise sintática! A linguagem não foi reconhecida!"


if __name__ == "__main__":
    lexico = analizador_lexico("codigo_exemplo")
    analisador_sintatico(lexico)
