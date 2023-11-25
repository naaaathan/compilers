class Arvore:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        try:
            tree = self.s()
            if self.pos == len(self.tokens):
                print("Análise sintática concluída com sucesso.")
                self.print_tree(tree)
            else:
                print("Erro sintático: Tokens não consumidos após a análise.")
                print("Tokens restantes:", self.tokens[self.pos:])
        except SyntaxError as e:
            print(f"Erro sintático: {e}")

    def match(self, expected_token, lookahead=0):
        index = self.pos + lookahead
        if index < len(self.tokens) and self.tokens[index] == expected_token:
            self.pos += 1 + lookahead  # Avança para o próximo token considerando o lookahead
        else:
            raise SyntaxError(f"Esperado '{expected_token}', encontrado '{self.tokens[index]}'.")

    def s(self):
        if self.tokens[self.pos] == 'function':
            self.match('function')
            identificador = self.tokens[self.pos]
            self.match('identificador')
            bloco = self.bloco()
            return Arvore('S', [Arvore(identificador), bloco])
        else:
            raise SyntaxError("Erro de sintaxe em S.")

    def bloco(self):
        if self.tokens[self.pos] == '{':
            self.match('{')
            declaracao = self.declaracao()
            comandos = self.comandos()
            self.match('}')
            return Arvore('bloco', [Arvore('declaracao', [declaracao]), Arvore('comandos', [comandos])])
        else:
            raise SyntaxError("Erro de sintaxe em bloco.")

    def declaracao(self):
        if self.tokens[self.pos] in ['int', 'float', 'char']:
            tipo = self.tokens[self.pos]
            self.match(tipo)
            self.match(':')
            ids = self.ids()
            self.match(';')
            declaracao = self.declaracao()
            return Arvore('declaracao', [Arvore(tipo), Arvore(ids), declaracao])
        else:
            return Arvore('declaracao', [])

    def ids(self):
        if self.tokens[self.pos] == 'identificador':
            identificador = self.tokens[self.pos]
            self.match('identificador')
            ids_ = self.ids_()
            return Arvore('ids', [Arvore(identificador), Arvore(ids_)])
        else:
            raise SyntaxError("Erro de sintaxe em ids.")

    def ids_(self):
        if self.tokens[self.pos] == ',':
            self.match(',')
            ids = self.ids()
            return Arvore('ids\'', [Arvore(','), Arvore(ids)])
        else:
            return None  # ε

    def comandos(self):
        if self.tokens[self.pos] in ['if', 'while', 'for', 'identificador']:
            comando = self.comando()
            comandos = self.comandos()
            return Arvore('comandos', [Arvore(comando), Arvore(comandos)])
        else:
            return None 

    def comando(self):
        if self.tokens[self.pos] == 'if':
            selecao = self.selecao()
            return Arvore('comando', [Arvore(selecao)])
        elif self.tokens[self.pos] == 'while':
            repeticao = self.repeticao()
            return Arvore('comando', [Arvore(repeticao)])
        elif self.tokens[self.pos] == 'for':
            repeticao = self.repeticao()
            return Arvore('comando', [Arvore(repeticao)])
        elif self.tokens[self.pos] == 'identificador':
            atribuicao = self.atribuicao()
            return Arvore('comando', [Arvore(atribuicao)])
        else:
            raise SyntaxError("Erro de sintaxe em comando.")

    def selecao(self):
        if self.tokens[self.pos] == 'if':
            self.match('if')
            self.match('(')
            condicao = self.condicao()
            self.match(')')
            self.match('then')
            selecao_ = self.selecao_()
            return Arvore('selecao', [Arvore(condicao), Arvore(selecao_)])
        else:
            raise SyntaxError("Erro de sintaxe em selecao.")

    def selecao_(self):
        comando = None
        if self.tokens[self.pos] == 'identificador' or self.tokens[self.pos] in ['if', 'while', 'for']:
            comando = self.comando()
        elif self.tokens[self.pos] == '{':
            bloco = self.bloco()
        self.match('else')
        selecao__ = self.selecao__()
        return Arvore('selecao\'', [Arvore(comando), Arvore(bloco), Arvore(selecao__)])

    def selecao__(self):
        comando = None
        if self.tokens[self.pos] == 'identificador' or self.tokens[self.pos] in ['if', 'while', 'for']:
            comando = self.comando()
        return Arvore('selecao\'\'', [Arvore(comando)])

    def repeticao(self):
        if self.tokens[self.pos] == 'while':
            self.match('while')
            self.match('(')
            condicao = self.condicao()
            self.match(')')
            self.match('do')
            repeticao_ = self.repeticao_()
            return Arvore('repeticao', [Arvore(condicao, repeticao_)])
        elif self.tokens[self.pos] == 'for':
            self.match('for')
            repeticao__ = self.repeticao__()
            return Arvore('repeticao', [Arvore(repeticao__)])

    def repeticao_(self):
        comando = self.comando()
        return Arvore('repeticao\'', [Arvore(comando)])

    def repeticao__(self):
        comando = self.comando()
        self.match(';')
        self.match('(')
        condicao = self.condicao()
        self.match(')')
        return Arvore('repeticao\'\'',  [Arvore(comando, condicao)])

    def atribuicao(self):
        identificador = self.tokens[self.pos]
        self.match('identificador')
        self.match('=')
        expressao = self.expressao()
        self.match(';')
        return Arvore('atribuicao', [Arvore(identificador, expressao)])

    def condicao(self):
        expressao1 = self.expressao()
        op_relacional = self.op_relacional()
        expressao2 = self.expressao()
        return Arvore('condicao', [Arvore(expressao1, op_relacional, expressao2)])

    def op_relacional(self):
        if self.tokens[self.pos] in ['>', '>=', '<', '<=', '==', '!=']:
            op = self.tokens[self.pos]
            self.match(op)
            return Arvore('op_relacional', [Arvore(op)])
        else:
            raise SyntaxError("Erro de sintaxe em op_relacional.")

    def expressao(self):
        if self.tokens[self.pos] == 'identificador':
            identificador = self.tokens[self.pos]
            self.match('identificador')
            return Arvore('expressao', [Arvore(identificador)])
        elif self.tokens[self.pos] == 'constante':
            constante = self.tokens[self.pos]
            self.match('constante')
            return Arvore('expressao', [Arvore(constante)])
        elif self.tokens[self.pos] == '(':
            self.match('(')
            expressao = self.expressao()
            self.match(')')
            return Arvore('expressao', ['(', expressao, ')'])
        else:
            raise SyntaxError("Erro de sintaxe em expressao.")

    def comando(self):
        if self.tokens[self.pos] == 'if':
            selecao = self.selecao()
            return Arvore('comando', [Arvore(selecao)])
        elif self.tokens[self.pos] == 'while':
            repeticao = self.repeticao()
            return Arvore('comando', [Arvore(repeticao)])
        elif self.tokens[self.pos] == 'for':
            repeticao = self.repeticao()
            return Arvore('comando', [Arvore(repeticao)])
        elif self.tokens[self.pos] == 'identificador':
            atribuicao = self.atribuicao()
            return Arvore('comando', [Arvore(atribuicao)])
        elif self.tokens[self.pos] in ('+', '-', '*', '/'):
            op_aritmetico = self.op_aritmetico()
            expressao = self.expressao()
            self.match(';')
            return Arvore('comando', [Arvore(op_aritmetico, expressao)])
        else:
            raise SyntaxError("Erro de sintaxe em comando.")

    def op_aritmetico(self):
        op = self.tokens[self.pos]
        if op in ('+', '-', '*', '/'):
            self.match(op)
            return Arvore('op_aritmetico', [Arvore(op)])
        else:
            raise SyntaxError(f"Erro de sintaxe em operador aritmético: '{op}'")

    def expressao(self):
        if self.tokens[self.pos] == 'identificador':
            identificador = self.tokens[self.pos]
            self.match('identificador')
            return Arvore('expressao', [Arvore(identificador)])
        elif self.tokens[self.pos] == 'constante':
            constante = self.tokens[self.pos]
            self.match('constante')
            return Arvore('expressao', [Arvore(constante)])
        elif self.tokens[self.pos] == '(':
            self.match('(')
            expressao = self.expressao()
            self.match(')')
            return Arvore('expressao', ['(', expressao, ')'])
        else:
            raise SyntaxError("Erro de sintaxe em expressao.")

    def print_tree(self, node, indent=""):
        if node is not None:
            if isinstance(node.value, Arvore):
                print(indent + str(node.value.value))
                for child in node.value.children:
                    self.print_tree(child, indent + "  ")
            else:
                print(indent + str(node.value))
                for child in node.children:
                    self.print_tree(child, indent + "  ")

tokens = ['function', 'identificador', '{', 'int', ':', 'identificador', ',', 'identificador', ';', '}']

analisador = AnalisadorSintatico(tokens)
analisador.parse()