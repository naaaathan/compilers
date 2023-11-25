class Arvore:
    def __init__(self, value):
        self.value = value
        self.children = []

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
        except SyntaxError as e:
            print(f"Erro sintático: {e}")

    def match(self, expected_token):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == expected_token:
            self.pos += 1
        else:
            raise SyntaxError(f"Esperado '{expected_token}', encontrado '{self.tokens[self.pos]}'.")

    def s(self):
        if self.tokens[self.pos] == 'function':
            self.match('function')
            identificador = self.tokens[self.pos]
            self.match('identificador')
            bloco = self.bloco()
            return Arvore('S', [identificador, bloco])
        else:
            raise SyntaxError("Erro de sintaxe em S.")

    def bloco(self):
        if self.tokens[self.pos] == '{':
            self.match('{')
            declaracao = self.declaracao()
            comandos = self.comandos()
            self.match('}')
            return Arvore('bloco', [declaracao, comandos])
        else:
            raise SyntaxError("Erro de sintaxe em bloco.")

    def declaracao(self):
        if self.tokens[self.pos] in ['int', 'float', 'char']:
            tipo = self.tokens[self.pos]
            self.match('tipo')
            self.match(':')
            ids = self.ids()
            self.match(';')
            declaracao = self.declaracao()
            return Arvore('declaracao', [tipo, ids, declaracao])
        else:
            return None  # ε

    def ids(self):
        if self.tokens[self.pos] == 'identificador':
            identificador = self.tokens[self.pos]
            self.match('identificador')
            ids_ = self.ids_()
            return Arvore('ids', [identificador, ids_])
        else:
            raise SyntaxError("Erro de sintaxe em ids.")

    def ids_(self):
        if self.tokens[self.pos] == ',':
            self.match(',')
            ids = self.ids()
            return Arvore('ids\'', [',', ids])
        else:
            return None  # ε

    def comandos(self):
        if self.tokens[self.pos] in ['if', 'while', 'for', 'identificador']:
            comando = self.comando()
            comandos = self.comandos()
            return Arvore('comandos', [comando, comandos])
        else:
            return None  # ε

    def comando(self):
        if self.tokens[self.pos] == 'if':
            selecao = self.selecao()
            return Arvore('comando', [selecao])
        elif self.tokens[self.pos] == 'while':
            repeticao = self.repeticao()
            return Arvore('comando', [repeticao])
        elif self.tokens[self.pos] == 'for':
            repeticao = self.repeticao()
            return Arvore('comando', [repeticao])
        elif self.tokens[self.pos] == 'identificador':
            atribuicao = self.atribuicao()
            return Arvore('comando', [atribuicao])
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
            return Arvore('selecao', [condicao, selecao_])
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
        return Arvore('selecao\'', [comando, bloco, selecao__])

    def selecao__(self):
        comando = None
        if self.tokens[self.pos] == 'identificador' or self.tokens[self.pos] in ['if', 'while', 'for']:
            comando = self.comando()
        return Arvore('selecao\'\'', [comando])

    def repeticao(self):
        if self.tokens[self.pos] == 'while':
            self.match('while')
            self.match('(')
            condicao = self.condicao()
            self.match(')')
            self.match('do')
            repeticao_ = self.repeticao_()
            return Arvore('repeticao', [condicao, repeticao_])
        elif self.tokens[self.pos] == 'for':
            self.match('for')
            repeticao__ = self.repeticao__()
            return Arvore('repeticao', [repeticao__])

    def repeticao_(self):
        comando = self.comando()
        return Arvore('repeticao\'', [comando])

    def repeticao__(self):
        comando = self.comando()
        self.match(';')
        self.match('(')
        condicao = self.condicao()
        self.match(')')
        return Arvore('repeticao\'\'', [comando, condicao])

    def atribuicao(self):
        identificador = self.tokens[self.pos]
        self.match('identificador')
        self.match('=')
        expressao = self.expressao()
        self.match(';')
        return Arvore('atribuicao', [identificador, expressao])

    def condicao(self):
        expressao1 = self.expressao()
        op_relacional = self.op_relacional()
        expressao2 = self.expressao()
        return Arvore('condicao', [expressao1, op_relacional, expressao2])

    def op_relacional(self):
        if self.tokens[self.pos] in ['>', '>=', '<', '<=', '==', '!=']:
            op = self.tokens[self.pos]
            self.match(op)
            return Arvore('op_relacional', [op])
        else:
            raise SyntaxError("Erro de sintaxe em op_relacional.")

    def expressao(self):
        if self.tokens[self.pos] == 'identificador':
            identificador = self.tokens[self.pos]
            self.match('identificador')
            return Arvore('expressao', [identificador])
        elif self.tokens[self.pos] == 'constante':
            constante = self.tokens[self.pos]
            self.match('constante')
            return Arvore('expressao', [constante])
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
            return Arvore('comando', [selecao])
        elif self.tokens[self.pos] == 'while':
            repeticao = self.repeticao()
            return Arvore('comando', [repeticao])
        elif self.tokens[self.pos] == 'for':
            repeticao = self.repeticao()
            return Arvore('comando', [repeticao])
        elif self.tokens[self.pos] == 'identificador':
            atribuicao = self.atribuicao()
            return Arvore('comando', [atribuicao])
        elif self.tokens[self.pos] in ('+', '-', '*', '/'):
            op_aritmetico = self.op_aritmetico()
            expressao = self.expressao()
            self.match(';')
            return Arvore('comando', [op_aritmetico, expressao])
        else:
            raise SyntaxError("Erro de sintaxe em comando.")

    def op_aritmetico(self):
        op = self.tokens[self.pos]
        if op in ('+', '-', '*', '/'):
            self.match(op)
            return Arvore('op_aritmetico', op)
        else:
            raise SyntaxError(f"Erro de sintaxe em operador aritmético: '{op}'")

    def expressao(self):
        if self.tokens[self.pos] == 'identificador':
            identificador = self.tokens[self.pos]
            self.match('identificador')
            return Arvore('expressao', [identificador])
        elif self.tokens[self.pos] == 'constante':
            constante = self.tokens[self.pos]
            self.match('constante')
            return Arvore('expressao', [constante])
        elif self.tokens[self.pos] == '(':
            self.match('(')
            expressao = self.expressao()
            self.match(')')
            return Arvore('expressao', ['(', expressao, ')'])
        else:
            raise SyntaxError("Erro de sintaxe em expressao.")

    def print_tree(self, node, indent=""):
        print(indent + node.value)
        for child in node.children:
            self.print_tree(child, indent + "  ")

# Tokens de exemplo (substitua pelos tokens da sua linguagem)
tokens = ['function', 'identificador', '{', 'int', ':', 'identificador', ',', 'identificador', ';', '}', 'eof']

analisador = AnalisadorSintatico(tokens)
analisador.parse()
