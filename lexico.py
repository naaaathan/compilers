import os

class Token:
    def __init__(self, tipo, atributo):
        self.tipo = tipo
        self.atributo = atributo
    
    def __str__(self):
        return f"Token({self.tipo}, {self.atributo})"


class AnalizadorLexico():
    def __init__(self, programFileName):
        self.ERROR = None
        self.programFileName = programFileName
        self.programFile = open(programFileName, "r+") 
        self.linha = 1
        self.coluna = 1
        self.currentPositionFile = 0
        self.endFile = os.path.getsize("./" + self.programFileName)

    def isDigitOrLetter(self,symbol):
        return symbol.isalnum() or symbol == '_'


    def nextToken(self,state, symbol):
        if state == -1: 
            # [ _ | b | d | g | h | j-q | t-z ] -> S0
            if symbol == '_' : 
                return (1, Token("identificador", "identificador"))
            elif symbol == 'b':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'd':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'g':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'h':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'j':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'k':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'l':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'm':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'n':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'o':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'p':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'q':
                return (1, Token("identificador", "identificador"))
            elif symbol == 't':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'u':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'v':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'w':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'x':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'y':
                return (1, Token("identificador", "identificador"))
            elif symbol == 'z':
                return (1, Token("identificador", "identificador"))

            # c -> S101
            elif symbol == 'c':
                return (101, None)
            
            # i -> S91
            elif symbol == 'i':
                return (91, None)
            
            # a -> S49
            elif symbol == 'a':
                return (49, None)
            
            # e -> S18
            elif symbol == 'e':
                return (18, None)
            
            # f -> S4
            elif symbol == 'f':
                return (4, None)

            # s -> S14
            elif symbol == 's':
                return (14, None)
            

            # r -> S41
            elif symbol == 'r':
                return (41, None)
            
            # < -> S69
            elif symbol == '<':
                return (69, Token("RELOP", "LT"))
            
            # > -> S73
            elif symbol == '>':
                return (73, Token("RELOP", "GT"))
            
            # = -> S54
            elif symbol == '=':
                return (54, Token("=","="))
            
            # : -> S83
            elif symbol ==':':
                return (83, Token(":",":"))
            
            # , -> S84
            elif symbol ==',':
                return (84, Token(",", ","))
            
            # ; -> S85
            elif symbol ==';':
                return (85, Token(";", ";"))

            # ( -> S86
            elif symbol =='(':
                return (86, Token("(", "("))

            # ) -> S87
            elif symbol ==')':
                return (87, Token(")", ")"))
            
            # { -> S88
            elif symbol =='{':
                return (88, Token("{", "{"))
            
            # } -> S89
            elif symbol =='}':
                return (89, Token("}", "}"))
            
            # digito -> S57
            elif symbol.isnumeric():
                return (57, Token("digito","numero"))

            # letra -> S110
            elif symbol == "'":
                return (110, None)
            
# ESTADOS 107 108 --------------------------------------------------
            # [ , \t, \n] -> 107
            elif symbol == ' ' or symbol == '\t' or symbol == '\n':
                return (107, Token("espaco","espaco"))

            # + -> S77
            elif symbol == '+':
                return (77, Token("op_aritimetico", "+"))
            
            # - -> S78
            elif symbol == '-':
                return (78, Token("op_aritimetico", "-"))
            
            # * -> S79
            elif symbol == '*':
                return (79, Token("op_aritimetico", "*"))
            
            # / -> S80
            elif symbol == '/':
                return (80, Token("op_aritimetico", "/"))

            # ^ -> S81
            elif symbol == '^':
                return (81, Token("op_aritimetico", "^"))
            
            else:
                return (self.ERROR, None)
            
        # State 0 ------------------------------------------------------
        elif state == 0:
            if symbol.isalnum() or symbol == '_':
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
        
        # State 1 ------------------------------------------------------
        elif state == 1:
            if symbol.isalnum() or symbol == '_':
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
        
        # State 4 ------------------------------------------------------
        elif state == 4:
            if symbol == 'u':
                return (5, None)
            elif symbol == 'a':
                return (26, None)
            elif symbol == 'l':
                return (96, None)
            elif symbol != 'u'and symbol != 'a'and symbol != 'l' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)

        # State 5 ------------------------------------------------------
        elif state == 5:
            if symbol == 'n':
                return (6, None)
            elif symbol != 'n'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 6 ------------------------------------------------------
        elif state == 6:
            if symbol == 'c':
                return (7, None)
            elif symbol != 'c'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 7 ------------------------------------------------------
        elif state == 7:
            if symbol == 't':
                return (8, None)
            elif symbol != 't'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 8 ------------------------------------------------------
        elif state == 8:
            if symbol == 'i':
                return (9, None)
            elif symbol != 'i'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 9 ------------------------------------------------------
        elif state == 9:
            if symbol == 'o':
                return (10, None)
            elif symbol != 'o'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
        
        # State 10 ------------------------------------------------------
        elif state == 10:
            if symbol == 'n':
                return (11, Token("function", "function"))
            elif symbol != 'n'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 11 ------------------------------------------------------
        elif state == 11:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 14 ------------------------------------------------------
        elif state == 14:
            if symbol == 'e':
                return (15, Token("se", "se"))
            elif symbol != 'e' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 15 ------------------------------------------------------
        elif state == 15:
            if symbol == 'n':
                return (116, None)
            elif symbol != 'n' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)


        # State 18 ------------------------------------------------------
        elif state == 18:
            if symbol == 'n':
                return (19, None)
            elif symbol != 'n'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 19 ------------------------------------------------------
        elif state == 19:
            if symbol == 't':
                return (20, None)
            elif symbol == 'q':
                return (33, None)
            elif symbol != 't' and symbol != 'q' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 20 ------------------------------------------------------
        elif state == 20:
            if symbol == 'a':
                return (21, None)
            elif symbol != 'a'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 21 ------------------------------------------------------
        elif state == 21:
            if symbol == 'o':
                return (22, Token("entao","entao"))
            elif symbol != 'o'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, Token("identificador", "identificador"))
            
        # State 22 ------------------------------------------------------
        elif state == 22:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 26 ------------------------------------------------------
        elif state == 26:
            if symbol == 'c':
                return (27, None)
            elif symbol != 'c'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 27 ------------------------------------------------------
        elif state == 27:
            if symbol == 'a':
                return (28, Token("faca", "faca"))
            elif symbol != 'a'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 28 ------------------------------------------------------
        elif state == 28:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 33 ------------------------------------------------------
        elif state == 33:
            if symbol == 'u':
                return (34, None)
            elif symbol != 'u'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 34 ------------------------------------------------------
        elif state == 34:
            if symbol == 'a':
                return (35, None)
            elif symbol != 'a'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 35 ------------------------------------------------------
        elif state == 35:
            if symbol == 'n':
                return (36, None)
            elif symbol != 'n'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 36 ------------------------------------------------------
        elif state == 36:
            if symbol == 't':
                return (37, None)
            elif symbol != 't'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)

        # State 37 ------------------------------------------------------
        elif state == 37:
            if symbol == 'o':
                return (38, Token("enquanto", "enquanto"))
            elif symbol != 'o'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 38 ------------------------------------------------------
        elif state == 38:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 41 ------------------------------------------------------
        elif state == 41:
            if symbol == 'e':
                return (42, None)
            elif symbol != 'e' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)

        # State 42 ------------------------------------------------------
        elif state == 42:
            if symbol == 'p':
                return (43, None)
            elif symbol != 'p' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 43 ------------------------------------------------------
        elif state == 43:
            if symbol == 'i':
                return (44, None)
            elif symbol != 'i' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 44 ------------------------------------------------------
        elif state == 44:
            if symbol == 't':
                return (45, None)
            elif symbol != 't' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
    
        # State 45 ------------------------------------------------------
        elif state == 45:
            if symbol == 'a':
                return (46, Token("repita", "repita"))
            elif symbol != 'a' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 46 ------------------------------------------------------
        elif state == 46:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)

        # State 49 ------------------------------------------------------
        elif state == 49:
            if symbol == 't':
                return (50, None)
            elif symbol != 't' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 50 ------------------------------------------------------
        elif state == 50:
            if symbol == 'e':
                return (51, Token("ate", "ate"))
            elif symbol != 'e' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)

        # State 51 ------------------------------------------------------            
        elif state == 51:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador", "identificador"))
            else:
                return (self.ERROR, None)
            
        # State 54 ------------------------------------------------------
        elif state == 54:
            if symbol == '=':
                return (68 , Token("op_relacional", "="))
            else:
                return (self.ERROR, None)

        # State 57 ------------------------------------------------------    
        elif state == 57:
            if symbol.isnumeric():
                return (57, Token("digito","numero"))
            elif symbol == '.':
                return (59, None)
            elif symbol == 'E':
                return (62, None)
            else:
                return (self.ERROR, None)
            
        # State 59 ------------------------------------------------------    
        elif state == 59:
            if symbol.isnumeric():
                return (60, Token("digito","numero"))
            else:
                return (self.ERROR, None)

        # State 60 ------------------------------------------------------    
        elif state == 60:
            if symbol.isnumeric():
                return (60, Token("digito","numero"))
            elif symbol == 'E':
                return (62, None)
            else:
                return (self.ERROR, None)
            
        # State 62 ------------------------------------------------------    
        elif state == 62:
            if symbol.isnumeric():
                return (64, Token("digito","numero"))
            elif symbol == '+' or symbol == '-':
                return (63, None)
            else:
                return (self.ERROR, None)

        # State 63 ------------------------------------------------------    
        elif state == 63:
            if symbol.isnumeric():
                return (64, Token("digito","numero"))
            else:
                return (self.ERROR, None)
            
        # State 64 ------------------------------------------------------    
        elif state == 64:
            if symbol.isnumeric():
                return (64, Token("digito","numero"))
            else:
                return (self.ERROR, None)

        # State 69 ------------------------------------------------------
        elif state == 69:
            if symbol == '>':
                return (70, Token("op_relacional","<>"))
            elif symbol == '=':
                return (71, Token("op_relacional","<="))
            else:
                return (self.ERROR, None)
            
        # State 73 ------------------------------------------------------
        elif state == 73:
            if symbol == '=':
                return (74, Token("op_relacional",">="))
            else:
                return (self.ERROR, None)
            
        # State 80 ------------------------------------------------------    
        elif state == 80:
            if symbol == '*':
                return (122, None)
            else:
                return (self.ERROR, None)
        
        # State 91 ------------------------------------------------------
        elif state == 91:
            if symbol != 'n' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            elif symbol == 'n':
                return (92, None)
            else:
                return (self.ERROR, None)

        # State 92 ------------------------------------------------------
        elif state == 92:
            if symbol == 't':
                return (93, Token("int","int"))
            elif symbol != 't' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
            
        # State 93 ------------------------------------------------------
        elif state == 93:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
            
        # State 96 ------------------------------------------------------
        elif state == 96:
            if symbol == 'o':
                return (97, None)
            elif symbol != 'o' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)

        # State 97 ------------------------------------------------------
        elif state == 97:
            if symbol == 'a':
                return (98, None)
            elif symbol != 'a' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)

        # State 98 ------------------------------------------------------
        elif state == 98:
            if symbol == 't':
                return (99, Token("float","float"))
            elif symbol != 't' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
            
        # State 99 ------------------------------------------------------
        elif state == 99:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)

        # State 101 ------------------------------------------------------
        elif state == 101:
            if symbol == 'h':
                return (102, None)
            elif symbol != 'h' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)

        # State 102 ------------------------------------------------------
        elif state == 102:
            if symbol == 'a':
                return (103, None)
            elif symbol != 'a'and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
        
        # State 103 ------------------------------------------------------
        elif state == 103:
            if symbol == 'r':
                return (104, Token("char","char"))
            elif symbol != 'r' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)        

        # State 104 ------------------------------------------------------
        elif state == 104:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
            
        # State 107 ------------------------------------------------------
        elif state == 107:
            if symbol == ' ' or symbol == '\t' or symbol == '\n':
                return (107, Token("espaco","espaco"))
            else:
                return (self.ERROR, None)
            
        # State 110 ------------------------------------------------------    
        elif state == 110:
            if symbol.isalpha():
                return (111, None)
            else:
                return (self.ERROR, None)
            
        # State 111 ------------------------------------------------------    
        elif state == 111:
            if symbol == "'":
                return (112, Token("letra","letra"))
            else:
                return (self.ERROR, None)
            
        # State 116 ------------------------------------------------------
        elif state == 116:
            if symbol == 'a':
                return (117, None)
            elif symbol != 'a' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
            
        # State 117 ------------------------------------------------------
        elif state == 117:
            if symbol == 'o':
                return (118, Token("senao","senao"))
            elif symbol != 'o' and self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
            
        # State 118 ------------------------------------------------------
        elif state == 118:
            if self.isDigitOrLetter(symbol):
                return (1, Token("identificador","identificador"))
            else:
                return (self.ERROR, None)
            
        # State 122 ------------------------------------------------------    
        elif state == 122:
            if symbol == '*':
                return (123, None)
            elif symbol != '*':
                return (122, None)
            else:
                return (self.ERROR, None)
            
        # State 123 ------------------------------------------------------    
        elif state == 123:
            if symbol == '/':
                return (124, Token("comentario","comentario"))
            elif symbol != '/':
                return (122, None)
            else:
                return (self.ERROR, None)    
        else:
            return (self.ERROR, None)

    def nextChar(self, file):
        return file.read(1)
    

    def readSymbol(self, file, position):
        file.seek(position)
        return file.read(1)

    def run(self):
        tokens = []
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
            print(currentState[0])
            print(currentState[1])

            if currentState[0] == self.ERROR:
        
                print(f"Erro léxico na linha {self.linha}, coluna {self.coluna}: caracter '{symbol}' não reconhecido.")
                return []

            if currentState[1] is not None:
                if symbol == '\n':
                    self.coluna = 0
                    self.linha += 1

                if currentState[1].atributo != 'comentario' and currentState[1].atributo != 'espaco':
                    if currentState[1].atributo == 'identificador':
                        token_value = token_value.strip()
                    tokens.append((Token(currentState[1].atributo, token_value), self.linha, self.coluna))
                    token_value = ""
                    currentState = (-1, None)
                else:
                    token_value += symbol

        return tokens


    def analisar_codigo(self, codigo):
        self.programFile.close()
        with open(self.programFileName, "w") as f:
            f.write(codigo)

        self.programFile = open(self.programFileName, "r+")
        self.linha = 1
        self.coluna = 1
        self.currentPositionFile = 0
        self.endFile = os.path.getsize("./" + self.programFileName)

        return self.run()
    

analizador = AnalizadorLexico("codigo_exemplo")
tokens = analizador.run()

for token, linha, coluna in tokens:
    print(f"Token: {token.tipo}, Linha: {linha}, Coluna: {coluna}")
