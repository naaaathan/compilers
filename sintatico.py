import os
from AnalisadorLexico import AnalizadorLexico


def isTerminal(x):
    terminais = {'function', 'identificador', 'numero', 'se', 'entao', 'senao', 'enquanto', 'faca', 'repita', 'ate',
                 'int', 'float', 'char', '{', '}', '+', '-', '*', '^', '/', '==', '<', '>', '$', ';', ':', ',', '(',
                 ')', '='}
    return x in terminais


class TabelaSintatica:
    def __init__(self):
        self.tabela = dict()

        self.tabela.update({'S': {'function': 1}})
        self.tabela.update({'bloco': {'{': 2}})
        self.tabela.update({'declaracao_das_variaveis': {'identificador': 4, 'se': 4, 'enquanto': 4, 'repita': 4,
                                                         'int': 3, 'float': 3, 'char': 3}})
        self.tabela.update({'tipo': {'int': 5, 'float': 6, 'char': 7}})
        self.tabela.update({'lista_ids': {'identificador': 8}})
        self.tabela.update({'lista_ids_linha': {';': 10, ',': 9}})
        self.tabela.update(
            {'sequencia_de_comandos': {'identificador': 11, '}': 12, 'se': 11, 'enquanto': 11, 'repita': 11}})
        self.tabela.update({'comando': {'identificador': 15, 'se': 13, 'enquanto': 14, 'repita': 14}})
        self.tabela.update({'selecao': {'se': 16}})
        self.tabela.update({'selecao_linha': {'identificador': 17, '{': 18, 'se': 17, 'enquanto': 17, 'repita': 17}})
        self.tabela.update(
            {'selecao_linha_linha': {'identificador': 10, '{': 20, 'se': 19, 'enquanto': 19, 'repita': 19}})
        self.tabela.update({'repeticao': {'enquanto': 21, 'repita': 22}})
        self.tabela.update({'repeticao_linha': {'identificador': 23, '{': 24, 'se': 23, 'enquanto': 23, 'repita': 23}})
        self.tabela.update(
            {'repeticao_linha_linha': {'identificador': 26, '{': 25, 'se': 26, 'enquanto': 26, 'repita': 22}})
        self.tabela.update({'atribuicao': {'identificador': 27}})
        self.tabela.update({'condicao': {'identificador': 28, 'numero': 28, 'letra': 28}})
        self.tabela.update({'expressao': {'identificador': 29, 'numero': 30, 'letra': 30}})
        self.tabela.update({'constante': {'numero': 33, 'letra': 34}})

        self.producao = []
        self.producao.append([])
        # 1. S ➡ function identificador ( ) bloco
        self.producao.append(['function', 'identificador', '(', ')', 'bloco'])
        # 2. bloco ➡ { declaracao_das_variaveis sequencia_de_comandos }
        self.producao.append(['{', 'declaracao_das_variaveis', 'sequencia_de_comandos', '}'])
        # 3. declaracao_das_variaveis ➡ tipo : lista_ids ; declaracao_das_variaveis
        self.producao.append(['tipo', ':', 'lista_ids', ';', 'declaracao_das_variaveis'])
        # 4. declaracao_das_variaveis ➡ ε
        self.producao.append(['epsilon'])
        # 5. tipo ➡ int
        self.producao.append(['int'])
        # 6. tipo ➡ float
        self.producao.append(['float'])
        # 7. tipo ➡ char
        self.producao.append(['char'])
        # 8. lista_ids → identificador lista_ids’
        self.producao.append(['identificador', 'lista_ids_linha'])
        # 9. lista_ids' → , lista_ids
        self.producao.append([',', 'lista_ids'])
        # 10. lista_ids' → ε
        self.producao.append(['epsilon'])
        # 11. sequencia_de_comandos → comando sequencia_de_comandos
        self.producao.append(['comando', 'sequencia_de_comandos'])
        # 12. sequencia_de_comandos → ε
        self.producao.append(['epsilon'])
        # 13. comando → selecao
        self.producao.append(['selecao'])
        # 14. comando → repeticao
        self.producao.append(['repeticao'])
        # 15. comando → atribuicao
        self.producao.append(['atribuicao'])
        # 16. selecao → se (condicao) entao selecao’
        self.producao.append(['se', '(', 'condicao', ')', 'entao', 'selecao'])
        # 17. selecao’ → comando senao selecao’’
        self.producao.append(['comando', 'senao', 'selecao'])
        # 18. selecao’ → bloco senao selecao’’
        self.producao.append(['bloco', 'senao', 'selecao_linha_linha'])
        # 19. selecao’’ → comando
        self.producao.append(['comando'])
        # 20. selecao’’ → bloco
        self.producao.append(['bloco'])
        # 21. repeticao → enquanto (condicao) faca repeticao’
        self.producao.append(['enquanto', '(', 'condicao', ')', 'faca', 'repeticao_linha'])
        # 22. repeticao → repita repeticao’’
        self.producao.append(['repita', 'repeticao_linha_linha'])
        # 23. repeticao’ → comando
        self.producao.append(['comando'])
        # 24. repeticao’ → bloco
        self.producao.append(['bloco'])
        # 25. repeticao’’ → bloco ate (condicao)
        self.producao.append(['bloco', 'ate', '(', 'condicao', ')'])
        # 26. repeticao’’ → comando ate (condicao)
        self.producao.append(['comando', 'ate', '(', 'condicao', ')'])
        # 27. atribuicao → identificador = expressao ;
        self.producao.append(['identificador', '=', 'expressao'])
        # 28. condicao → expressao op_relacional expressao
        self.producao.append(['expressao', 'op_relacional', 'expressao'])
        # 29. expressao → identificador
        self.producao.append(['identificador'])
        # 30. expressao → constante
        self.producao.append(['constante'])
        # 31. expressao → (expressao)
        self.producao.append(['(', 'expressao', ')'])
        # 32. expressao → expressao op_aritmetico expressao
        self.producao.append(['expressao', 'op_aritmetico', 'expressao'])
        # 33. constante → numero
        self.producao.append(['numero'])
        # 34. constante →letra
        self.producao.append(['letra'])


class IdTable:
    def __init__(self):
        self.symbolsTable = dict()
        self.cont = 0

        self.insert("function")
        self.insert("se")
        self.insert("entao")
        self.insert("senao")
        self.insert("enquanto")
        self.insert("faca")
        self.insert("repita")
        self.insert("ate")
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
    proxToken = token[0].tipo
    tabelaSintatica = TabelaSintatica()

    while len(pilha) > 0:
        x = pilha[-1]
        pilha.pop()

        if isTerminal(x):

            if x == proxToken:

                token = analisadorLexico.run()

                if token[0].tipo == "$":
                    print("Cadeia Aceita")
                    return "Cadeia Aceita"

                proxToken = token[0].tipo
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
                    print(f"vai pra producao de numero {idProducao}")
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
    fileName = input("Arquivo para analise: ")
    analisadorLexo = AnalizadorLexico(fileName)
    analisadorSintatico(analisadorLexo)