import os
from lexico import AnalizadorLexico


def isTerminal(x):
    terminais = {'fun', 'id', 'number', 'if', 'then', 'else', 'while', 'do', 'for', 'to',
                 'int', 'float', 'char', '{', '}', '+', '-', '*', '^', '/', '==', '<', '>', '$', ';', ':', ',', '(',
                 ')', '='}
    return x in terminais


class TabelaSintatica:
    def __init__(self):
        self.tabela = dict()

        self.tabela.update({'S': {'fun': 1}})
        self.tabela.update({'bloco': {'{': 2}})
        self.tabela.update({'declaracao': {'id': 4, 'if': 4, 'while': 4, 'for': 4, 'int': 3, 'float': 3, 'char': 3}})
        self.tabela.update({'tipo': {'int': 5, 'float': 6, 'char': 7}})
        self.tabela.update({'lista_ids': {'id': 8}})
        self.tabela.update({'lista_ids_linha': {';': 10, ',': 9}})
        self.tabela.update({'comandos': {'id': 11, '}': 12, 'if': 11, 'while': 11, 'for': 11}})
        self.tabela.update({'comando': {'id': 15, 'if': 13, 'while': 14, 'for': 14}})
        self.tabela.update({'selecao': {'if': 16}})
        self.tabela.update({'selecao_linha': {'id': 17, '{': 18, 'if': 17, 'while': 17, 'for': 17}})
        self.tabela.update({'selecao_linha_linha': {'id': 10, '{': 20, 'if': 19, 'while': 19, 'for': 19}})
        self.tabela.update({'repeticao': {'while': 21, 'for': 22}})
        self.tabela.update({'repeticao_linha': {'id': 23, '{': 24, 'if': 23, 'while': 23, 'for': 23}})
        self.tabela.update({'repeticao_linha_linha': {'id': 26, '{': 25, 'if': 26, 'while': 26, 'for': 22}})
        self.tabela.update({'atribuicao': {'id': 27}})
        self.tabela.update({'condicao': {'id': 28, 'number': 28, 'letra': 28}})
        self.tabela.update({'expressao': {'id': 29, 'number': 30, 'letra': 30}})
        self.tabela.update({'constante': {'number': 33, 'letra': 34}})
        self.tabela.update({'op_relacional': {'==': 35, '>=': 36, '<=': 37, '<>': 38}})

        self.producao = []
        self.producao.append([])

        self.producao.append(['fun', 'id', '(', ')', 'bloco'])
        self.producao.append(['{', 'declaracao', 'comandos', '}'])
        self.producao.append(['tipo', ':', 'lista_ids', ';', 'declaracao'])
        self.producao.append(['epsilon'])
        self.producao.append(['int'])
        self.producao.append(['float'])
        self.producao.append(['char'])
        self.producao.append(['id', 'lista_ids_linha'])
        self.producao.append([',', 'lista_ids'])
        self.producao.append(['epsilon'])
        self.producao.append(['comando', 'comandos'])
        self.producao.append(['epsilon'])
        self.producao.append(['selecao'])
        self.producao.append(['repeticao'])
        self.producao.append(['atribuicao'])
        self.producao.append(['if', '(', 'condicao', ')', 'then', 'selecao'])
        self.producao.append(['comando', 'else', 'selecao'])
        self.producao.append(['bloco', 'else', 'selecao_linha_linha'])
        self.producao.append(['comando'])
        self.producao.append(['bloco'])
        self.producao.append(['while', '(', 'condicao', ')', 'do', 'repeticao_linha'])
        self.producao.append(['for', 'repeticao_linha_linha'])
        self.producao.append(['comando'])
        self.producao.append(['bloco'])
        self.producao.append(['bloco', 'to', '(', 'condicao', ')'])
        self.producao.append(['comando', 'to', '(', 'condicao', ')'])
        self.producao.append(['id', '=', 'expressao', ";"])
        self.producao.append(['expressao', 'op_relacional', 'expressao'])
        self.producao.append(['id'])
        self.producao.append(['constante'])
        self.producao.append(['(', 'expressao', ')'])
        self.producao.append(['expressao', 'op_aritmetico', 'expressao'])
        self.producao.append(['number'])
        self.producao.append(['letra'])
        self.producao.append(['=='])
        self.producao.append(['>='])
        self.producao.append(['<='])
        self.producao.append(['<>'])


class IdTable:
    def __init__(self):
        self.symbolsTable = dict()
        self.cont = 0

        self.insert("fun")
        self.insert("if")
        self.insert("then")
        self.insert("else")
        self.insert("while")
        self.insert("do")
        self.insert("for")
        self.insert("to")
        self.insert("int")
        self.insert("float")
        self.insert("char")
        self.insert("{")
        self.insert("}")
        self.insert("(")
        self.insert(")")
        self.insert(",")
        self.insert(";")
        self.insert(":")
        self.insert("=")

    def insert(self, id):
        if id not in self.symbolsTable:
            self.symbolsTable[id] = self.cont
            self.cont += 1
            return self.cont - 1
        else:
            return self.symbolsTable[id]


def analisadorSintatico(analisadorLexico):
    global arvore
    arvore = dict()
    pilha = list()
    pilha.append("S")

    # Carrega proximo token
    token = analisadorLexico.run()
    print(f"token: {token}")
    proxToken = token[0].tipo
    print(f"proxToken: {proxToken}")
    tabelaSintatica = TabelaSintatica()

    while len(pilha) > 0:
        x = pilha[-1]
        pilha.pop()

        print(f"isTerminal({x}) = {isTerminal(x)}")

        if isTerminal(x):

            if x == proxToken:

                token = analisadorLexico.run()

                if token[0].tipo == "$":
                    print("Cadeia Aceita")
                    return "Cadeia Aceita"

                proxToken = token[0].tipo
                print(f"ProxToken:{proxToken}")
                continue
            else:
                print("Erro! Token {} nao era esperado! Linha: {} | Coluna: {}".format(token[0].atributo, token[1],
                                                                                       token[2]))
                break
        else:
            if x not in tabelaSintatica.tabela:
                print("Erro! Linha: {} | Coluna: {}".format(token[1], token[2]))
                print("Erro! A linguagem nao foi reconhecida!")
                break
            else:
                try:
                    idProducao = tabelaSintatica.tabela[x][proxToken]
                    producoes = tabelaSintatica.producao[idProducao]
                    print(f"vai pra producao de number {idProducao}")
                    print(f"nao eh terminal, producoes: {producoes}")
                    for prod in reversed(producoes):
                        if prod != 'epsilon':
                            pilha.append(prod)
                    arvore.update({x: reversed(producoes)})

                except:  # Não achou uma produção para o token
                    print("A linguagem nao foi reconhecida!")

    if len(pilha) == 0:
        return "A linguagem foi reconhec"
    return "Erro! A linguagem nao foi reconhecida!"


if __name__ == "__main__":
    analisadorLexo = AnalizadorLexico("teste1.txt")
    analisadorSintatico(analisadorLexo)
