import os


class Token:
    def __init__(self, tipo, atributo):
        self.tipo = tipo
        self.atributo = atributo

    def __str__(self):
        return f"Token({self.tipo}, {self.atributo})"


class AnalizadorLexico:
    def __init__(self, programFileName):
        self.ERROR = None
        self.programFileName = programFileName
        self.programFile = open(programFileName, "r+")
        self.linha = 1
        self.coluna = 1
        self.currentPositionFile = 0
        self.endFile = os.path.getsize("./" + self.programFileName)

    @staticmethod
    def isDigitOrLetter(symbol):
        return symbol.isalnum() or symbol == '_'

    def peekNextChar(self):
        current_position = self.programFile.tell()
        next_char = self.programFile.read(1)
        self.programFile.seek(current_position)
        return next_char

    def nextToken(self, state, symbol):

        lookahead_symbol = self.peekNextChar()

        if state == -1:
            # [ _ | b | d | g | h | j-q | t-z ] -> S0
            if symbol == '_':
                return 1, Token("id", "id")
            elif symbol == 'b':
                return 1, Token("id", "id")
            elif symbol == 'g':
                return 1, Token("id", "id")
            elif symbol == 'h':
                return 1, Token("id", "id")
            elif symbol == 'j':
                return 1, Token("id", "id")
            elif symbol == 'k':
                return 1, Token("id", "id")
            elif symbol == 'l':
                return 1, Token("id", "id")
            elif symbol == 'm':
                return 1, Token("id", "id")
            elif symbol == 'n':
                return 1, Token("id", "id")
            elif symbol == 'o':
                return 1, Token("id", "id")
            elif symbol == 'p':
                return 1, Token("id", "id")
            elif symbol == 'q':
                return 1, Token("id", "id")
            elif symbol == 'r':
                return 1, Token("id", "id")
            elif symbol == 't':
                return 1, Token("id", "id")
            elif symbol == 'u':
                return 1, Token("id", "id")
            elif symbol == 's':
                return 1, Token("id", "id")
            elif symbol == 'v':
                return 1, Token("id", "id")
            elif symbol == 'x':
                return 1, Token("id", "id")
            elif symbol == 'y':
                return 1, Token("id", "id")
            elif symbol == 'z':
                return 1, Token("id", "id")

            elif symbol == 'a':
                return 49, None

            elif symbol == 'c':
                return 101, None

            elif symbol == 'd':
                return 120, None

            elif symbol == 'i':
                return 91, None

            elif symbol == 'e':
                return 18, None

            elif symbol == 'f':
                return 4, None

            elif symbol == 'w':
                return 41, None

            elif symbol == '<':
                return 69, Token("RELOP", "LT")

            elif symbol == '>':
                return 73, Token("RELOP", "GT")

            elif symbol == '=':
                return 54, Token("=", "=")

            elif symbol == ':':
                return 83, Token(":", ":")

            elif symbol == ',':
                return 84, Token(",", ",")

            elif symbol == ';':
                return 85, Token(";", ";")

            elif symbol == '(':
                return 86, Token("(", "(")

            elif symbol == ')':
                return 87, Token(")", ")")

            elif symbol == '{':
                return 88, Token("{", "{")

            elif symbol == '}':
                return 89, Token("}", "}")

            elif symbol.isnumeric():
                return 57, Token("digito", "numero")

            elif symbol == "'":
                return 110, None

            elif symbol == ' ' or symbol == '\t' or symbol == '\n':
                return 107, Token("espaco", "espaco")

            elif symbol == '+':
                return 77, Token("op_aritimetico", "+")

            elif symbol == '-':
                return 78, Token("op_aritimetico", "-")

            elif symbol == '*':
                return 79, Token("op_aritimetico", "*")

            elif symbol == '/':
                return 80, Token("op_aritimetico", "/")

            elif symbol == '^':
                return 81, Token("op_aritimetico", "^")

            else:
                return self.ERROR, None

        elif state == 0:
            if symbol.isalnum() or symbol == '_':
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 1:
            if symbol.isalnum() or symbol == '_':
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 4:
            if symbol == 'u':
                return 5, None
            elif symbol == 'l':
                return 96, None
            elif symbol != 'u' and symbol != 'l' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 5:
            if symbol == 'n':
                return 125, Token("fun", "fun")
            elif symbol != 'n' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 125:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 6:
            if symbol != 'c' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 7:
            if symbol != 't' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 8:
            if symbol != 'i' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 9:
            if symbol != 'o' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 10:
            if symbol != 'n' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 11:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 18:
            if symbol == 'l':
                return 19, None
            elif symbol != 'l' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 19:
            if symbol == 's':
                return 20, None
            elif symbol != 's' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 20:
            if symbol == 'e':
                return 22, Token("else", "else")
            elif symbol != 'e' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 22:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 41:
            if symbol == 'h':
                return 42, None
            elif symbol != 'h' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 42:
            if symbol == 'i':
                return 43, None
            elif symbol != 'i' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 43:
            if symbol == 'l':
                return 43, None
            elif symbol != 'l' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 44:
            if symbol == 'e':
                return 45, Token("while", "while")
            elif symbol != 'e' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 45:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 49:
            if self.isDigitOrLetter(symbol) or not self.isDigitOrLetter(lookahead_symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 51:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 54:
            if symbol == '=':
                return 68, Token("op_relacional", "=")
            else:
                return self.ERROR, None

        elif state == 57:
            if symbol.isnumeric():
                return 57, Token("digito", "numero")
            elif symbol == '.':
                return 59, None
            elif symbol == 'E':
                return 62, None
            else:
                return self.ERROR, None

        elif state == 59:
            if symbol.isnumeric():
                return 60, Token("digito", "numero")
            else:
                return self.ERROR, None

        elif state == 60:
            if symbol.isnumeric():
                return 60, Token("digito", "numero")
            elif symbol == 'E':
                return 62, None
            else:
                return self.ERROR, None

        elif state == 62:
            if symbol.isnumeric():
                return 64, Token("digito", "numero")
            elif symbol == '+' or symbol == '-':
                return 63, None
            else:
                return self.ERROR, None

        elif state == 63:
            if symbol.isnumeric():
                return 64, Token("digito", "numero")
            else:
                return self.ERROR, None

        elif state == 64:
            if symbol.isnumeric():
                return 64, Token("digito", "numero")
            else:
                return self.ERROR, None

        elif state == 69:
            if symbol == '>':
                return 70, Token("op_relacional", "<>")
            elif symbol == '=':
                return 71, Token("op_relacional", "<=")
            else:
                return self.ERROR, None

        elif state == 73:
            if symbol == '=':
                return 74, Token("op_relacional", ">=")
            else:
                return self.ERROR, None

        elif state == 80:
            if symbol == '*':
                return 122, None
            else:
                return self.ERROR, None

        elif state == 91:
            if symbol != 'n' and symbol != 'f' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            elif symbol == 'n':
                return 92, None
            elif symbol == 'f':
                return 93, Token("if", "if")
            else:
                return self.ERROR, None

        elif state == 92:
            if symbol == 't':
                return 93, Token("int", "int")
            elif symbol != 't' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 93:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 96:
            if symbol == 'o':
                return 97, None
            elif symbol != 'o' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 97:
            if symbol == 'a':
                return 98, None
            elif symbol != 'a' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 98:
            if symbol == 't':
                return 99, Token("float", "float")
            elif symbol != 't' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 99:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 101:
            if symbol == 'h':
                return 102, None
            elif symbol != 'h' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 102:
            if symbol == 'a':
                return 103, None
            elif symbol != 'a' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 103:
            if symbol == 'r':
                return 104, Token("char", "char")
            elif symbol != 'r' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 104:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 107:
            if symbol == ' ' or symbol == '\t' or symbol == '\n':
                return 107, Token("espaco", "espaco")
            else:
                return self.ERROR, None

        elif state == 110:
            if symbol.isalpha():
                return 111, None
            else:
                return self.ERROR, None

        elif state == 111:
            if symbol == "'":
                return 112, Token("letra", "letra")
            else:
                return self.ERROR, None

        elif state == 118:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 120:
            if symbol == 'o':
                return 121, Token("do", "do")
            elif symbol != 'o' and self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 121:
            if self.isDigitOrLetter(symbol):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif state == 122:
            if symbol == '*':
                return 123, None
            elif symbol != '*':
                return 122, None
            else:
                return self.ERROR, None

        elif state == 123:
            if symbol == '/':
                return 124, Token("comentario", "comentario")
            elif symbol != '/':
                return 122, None
            else:
                return self.ERROR, None
        else:
            return self.ERROR, None

    @staticmethod
    def nextChar(file):
        return file.read(1)

    @staticmethod
    def readSymbol(file, position):
        file.seek(position)
        return file.read(1)

    def run(self):
        tks = []
        currentState = (-1, None)
        token_value = ""
        in_string_literal = False

        while self.currentPositionFile < self.endFile:
            symbol = self.nextChar(self.programFile)
            self.coluna += 1
            self.currentPositionFile += 1

            if symbol == '"':
                in_string_literal = not in_string_literal

            if not in_string_literal and symbol.isspace():
                continue

            currentState = self.nextToken(currentState[0], symbol)
            # print(symbol)
            # print(currentState[0])

            if currentState[0] == self.ERROR:
                print(f"Erro léxico na linha {self.linha}, coluna {self.coluna}: caracter '{symbol}' não reconhecido.")
                return []

            if currentState[1] is not None:
                if symbol == '\n':
                    self.coluna = 0
                    self.linha += 1

                if currentState[1].atributo != 'comentario' and currentState[1].atributo != 'espaco':
                    if currentState[1].atributo == 'id':
                        token_value = token_value.strip()
                    tks.append((Token(currentState[1].atributo, token_value), self.linha, self.coluna))
                    token_value = ""
                    currentState = (-1, None)
                else:
                    token_value += symbol

        return tks


analizador = AnalizadorLexico("codigo_exemplo")
tokens = analizador.run()

for token, linha, coluna in tokens:
    print(f"Token: {token.tipo}, Linha: {linha}, Coluna: {coluna}")
