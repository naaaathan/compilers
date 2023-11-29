import os


class Token:
    def __init__(self, tipo, atributo):
        self.tipo = tipo
        self.atributo = atributo

    def __str__(self):
        return f"Token({self.tipo}, {self.atributo})"


class AnalisadorLexico:
    def __init__(self, nome_do_programa):
        self.ERROR = None
        self.nome_do_programa = nome_do_programa
        self.arquivo = open(nome_do_programa, "r+")
        self.linha = 1
        self.coluna = 1
        self.posicao_arquivo = 0
        self.final_do_arquivo = os.path.getsize("./" + self.nome_do_programa)

    @staticmethod
    def digito_ou_letra(palavra):
        return palavra.isalnum() or palavra == '_'

    def get_next(self):
        current_position = self.arquivo.tell()
        next_char = self.arquivo.read(1)
        self.arquivo.seek(current_position)
        return next_char

    def get_token(self, estado, palavra):
        if estado == -1:
            # não encontra dentro das palavras reservadas
            if palavra in ['_', 'a', 'b', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o',
                           'p', 'q', 'r', 's', 'u', 'v', 'x', 'y', 'z']:
                return 1, Token("id", "id")

            # char [2, 3, 4, 5]
            elif palavra == 'c':
                return 2, None

            # do [6, 7]
            elif palavra == 'd':
                return 6, None

            # else [8, 9, 10, 11]
            elif palavra == 'e':
                return 8, None

            # fun [12, 13, 14] for [12, 15, 16] float [12, 17, 18, 19, 20]
            elif palavra == 'f':
                return 12, None

            # if [21, 22] int [21, 23, 24]
            elif palavra == 'i':
                return 21, None

            # then [25, 26, 27, 28] to [25, 29]
            elif palavra == 't':
                return 25, None

            # while [30, 31, 32, 33, 34]
            elif palavra == 'w':
                return 30, None

            elif palavra == '<':
                return 69, Token("RELOP", "LT")

            elif palavra == '>':
                return 73, Token("RELOP", "GT")

            elif palavra == '=':
                return 54, Token("=", "=")

            elif palavra == ':':
                return 83, Token(":", ":")

            elif palavra == ',':
                return 84, Token(",", ",")

            elif palavra == ';':
                return 85, Token(";", ";")

            elif palavra == '(':
                return 86, Token("(", "(")

            elif palavra == ')':
                return 87, Token(")", ")")

            elif palavra == '{':
                return 88, Token("{", "{")

            elif palavra == '}':
                return 89, Token("}", "}")

            elif palavra.isnumeric():
                return 57, Token("digito", "number")

            elif palavra == "'":
                return 110, None

            elif palavra == ' ' or palavra == '\t' or palavra == '\n':
                return 107, Token("espaco", "espaco")

            elif palavra == '+':
                return 77, Token("op_aritimetico", "+")

            elif palavra == '-':
                return 78, Token("op_aritimetico", "-")

            elif palavra == '*':
                return 79, Token("op_aritimetico", "*")

            elif palavra == '/':
                return 80, Token("op_aritimetico", "/")

            elif palavra == '^':
                return 81, Token("op_aritimetico", "^")

            else:
                return self.ERROR, None

        elif estado == 0:
            if palavra.isalnum() or palavra == '_':
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 1:
            if palavra.isalnum() or palavra == '_':
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # CHAR

        elif estado == 2:
            if palavra == 'h':
                return 3, None
            elif palavra != 'h' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 3:
            if palavra == 'a':
                return 4, None
            elif palavra != 'a' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 4:
            if palavra == 'r':
                return 5, Token("char", "char")
            elif palavra != 'r' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 5:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # DO

        elif estado == 6:
            if palavra == 'o':
                return 7, Token("do", "do")
            elif palavra != 'o' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 7:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # ELSE

        elif estado == 8:
            if palavra == 'l':
                return 9, None
            elif palavra != 'l' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 9:
            if palavra == 's':
                return 10, None
            elif palavra != 's' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 10:
            if palavra == 'e':
                return 11, Token("else", "else")
            elif palavra != 'e' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 11:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # FUN

        elif estado == 12:
            if palavra == 'u':
                return 13, None
            if palavra == 'o':
                return 15, None
            elif palavra == 'l':
                return 17, None
            elif palavra != 'u' and palavra != 'o' and palavra != 'l' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 13:
            if palavra == 'n':
                return 14, Token("fun", "fun")
            elif palavra != 'n' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 14:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # FOR

        elif estado == 15:
            if palavra == 'r':
                return 16, Token("for", "for")
            if palavra != 'r' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 16:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # FLOAT

        elif estado == 17:
            if palavra == 'o':
                return 18, None
            elif palavra != 'o' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 18:
            if palavra == 'a':
                return 19, None
            elif palavra != 'a' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 19:
            if palavra == 't':
                return 20, Token("float", "float")
            elif palavra != 't' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 20:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # IF

        elif estado == 21:
            if palavra == 'f':
                return 22, Token("if", "if")
            elif palavra == 'n':
                return 23, None
            elif palavra != 'n' and palavra != 'f' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 22:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # INT

        elif estado == 23:
            if palavra == 't':
                return 24, Token("int", "int")
            elif palavra != 't' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 24:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # THEN

        elif estado == 25:
            if palavra == 'h':
                return 26, None
            elif palavra == 'o':
                return 29, Token("to", "to")
            elif palavra != 'h' and palavra != 'o' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")

            else:
                return self.ERROR, None

        elif estado == 26:
            if palavra == 'e':
                return 27, None
            elif palavra != 'e' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 27:
            if palavra == 'n':
                return 28, Token("then", "then")
            elif palavra != 'n' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 28:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # TO

        elif estado == 29:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        # WHILE

        elif estado == 30:
            if palavra == 'h':
                return 31, None
            elif palavra != 'h' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 31:
            if palavra == 'i':
                return 32, None
            elif palavra != 'i' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 32:
            if palavra == 'l':
                return 33, None
            elif palavra != 'l' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 33:
            if palavra == 'e':
                return 34, Token("while", "while")
            elif palavra != 'e' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 34:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 51:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 54:
            if palavra == '=':
                return 68, Token("==", "==")
            else:
                return self.ERROR, None

        elif estado == 57:
            if palavra.isnumeric():
                return 57, Token("digito", "number")
            elif palavra == ',':
                return 59, None
            elif palavra == 'E':
                return 62, None
            else:
                return self.ERROR, None

        elif estado == 59:
            if palavra.isnumeric():
                return 60, Token("digito", "number")
            else:
                return self.ERROR, None

        elif estado == 60:
            if palavra.isnumeric():
                return 60, Token("digito", "number")
            elif palavra == 'E':
                return 62, None
            else:
                return self.ERROR, None

        elif estado == 62:
            if palavra.isnumeric():
                return 64, Token("digito", "number")
            elif palavra == '+' or palavra == '-':
                return 63, None
            else:
                return self.ERROR, None

        elif estado == 63:
            if palavra.isnumeric():
                return 64, Token("digito", "number")
            else:
                return self.ERROR, None

        elif estado == 64:
            if palavra.isnumeric():
                return 64, Token("digito", "number")
            else:
                return self.ERROR, None

        elif estado == 69:
            if palavra == '>':
                return 70, Token("op_relacional", "<>")
            elif palavra == '=':
                return 71, Token("op_relacional", "<=")
            else:
                return self.ERROR, None

        elif estado == 73:
            if palavra == '=':
                return 74, Token("op_relacional", ">=")
            else:
                return self.ERROR, None

        elif estado == 80:
            if palavra == '/':
                return 122, None
            else:
                return self.ERROR, None

        elif estado == 96:
            if palavra == 'o':
                return 97, None
            elif palavra != 'o' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 97:
            if palavra == 'a':
                return 98, None
            elif palavra != 'a' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 98:
            if palavra == 't':
                return 99, Token("float", "float")
            elif palavra != 't' and self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 99:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 107:
            if palavra == ' ' or palavra == '\t' or palavra == '\n':
                return 107, Token("espaco", "espaco")
            else:
                return self.ERROR, None

        elif estado == 110:
            if palavra.isalpha():
                return 111, None
            else:
                return self.ERROR, None

        elif estado == 111:
            if palavra == "'":
                return 112, Token("letra", "letra")
            else:
                return self.ERROR, None

        elif estado == 118:
            if self.digito_ou_letra(palavra):
                return 1, Token("id", "id")
            else:
                return self.ERROR, None

        elif estado == 122:
            if palavra == '\n':
                return 124, Token("comentario", "comentario")
            elif palavra != '\n':
                return 122, None
            else:
                return self.ERROR, None

        else:
            return self.ERROR, None

    @staticmethod
    def next_char(file):
        return file.read(1)

    @staticmethod
    def read_symbol(file, position):
        file.seek(position)
        return file.read(1)

    def run(self):
        token = ""
        estado_atual = (-1, None)

        while self.posicao_arquivo != self.final_do_arquivo:
            palavra = self.read_symbol(self.arquivo, self.posicao_arquivo)

            self.coluna += 1
            self.posicao_arquivo += 1
            estado_atual = self.get_token(estado_atual[0], palavra)

            if estado_atual[1] == None:
                # LOOKAHEAD
                token = token + palavra
            else:
                if palavra == '\n':
                    self.coluna = 0
                    self.linha += 1

                if self.posicao_arquivo == self.final_do_arquivo:
                    return (Token("$", "$"), self.linha, self.coluna)

                if self.get_token(estado_atual[0], self.read_symbol(self.arquivo, self.posicao_arquivo))[
                    0] == self.ERROR:
                    if estado_atual[1].atributo == 'comentario' or estado_atual[1].atributo == 'espaco':
                        estado_atual = (-1, None)
                        continue

                    token = token + palavra
                    return (Token(estado_atual[1].atributo, token), self.linha, self.coluna)