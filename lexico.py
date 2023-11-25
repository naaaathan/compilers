class Token:
    def __init__(self, token_type, lexeme, position):
        self.token_type = token_type
        self.lexeme = lexeme
        self.position = position

class LexicalAnalyzer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_position = 0
        self.line = 1
        self.column = 1

    def analyze(self):
        while self.current_position < len(self.source_code):
            char = self.source_code[self.current_position]
            if char.isspace():
                if char == '\n':
                    self.line += 1
                    self.column = 1
                else:
                    self.column += 1
                self.current_position += 1
            elif char.isalpha():
                token = self.process_identifier_or_keyword()
                self.tokens.append(token)
            elif char.isdigit():
                token = self.process_number()
                self.tokens.append(token)
            elif char == '"':
                token = self.process_string_literal()
                self.tokens.append(token)
            elif char in ('+', '-', '*', '/', '(', ')', '=', ';', ',', '{', '}'):
                token = self.process_operator_or_separator()
                self.tokens.append(token)
            elif char == '<':
                token = self.process_relational_operator()
                self.tokens.append(token)
            else:
                self.handle_error(f"Caractere desconhecido: '{char}'")
                self.current_position += 1

        return self.tokens

    def process_identifier_or_keyword(self):
        start_position = self.current_position
        while self.current_position < len(self.source_code) and (self.source_code[self.current_position].isalnum() or self.source_code[self.current_position] == '_'):
            self.current_position += 1
        lexeme = self.source_code[start_position:self.current_position]
        token_type = 'identificador' if lexeme not in ('int', 'float', 'char') else lexeme
        return Token(token_type, lexeme, (self.line, self.column))

    def process_number(self):
        start_position = self.current_position
        while self.current_position < len(self.source_code) and self.source_code[self.current_position].isdigit():
            self.current_position += 1
        lexeme = self.source_code[start_position:self.current_position]
        return Token('numero', lexeme, (self.line, self.column))

    def process_string_literal(self):
        start_position = self.current_position
        self.current_position += 1  # Skip the opening double quote
        while self.current_position < len(self.source_code) and self.source_code[self.current_position] != '"':
            if self.source_code[self.current_position] == '\n':
                self.handle_error("String literal não terminada")
                break
            self.current_position += 1
        if self.current_position < len(self.source_code) and self.source_code[self.current_position] == '"':
            self.current_position += 1  # Skip the closing double quote
            lexeme = self.source_code[start_position:self.current_position]
            return Token('literal', lexeme, (self.line, self.column))
        else:
            self.handle_error("String literal não terminada")
            return Token('erro', '', (self.line, self.column))

    def process_operator_or_separator(self):
        char = self.source_code[self.current_position]
        self.current_position += 1
        return Token(char, char, (self.line, self.column))

    def process_relational_operator(self):
        start_position = self.current_position
        while self.current_position < len(self.source_code) and self.source_code[self.current_position] in ('>', '=', '!'):
            self.current_position += 1
        lexeme = self.source_code[start_position:self.current_position]
        return Token(lexeme, lexeme, (self.line, self.column))

    def handle_error(self, message):
        print(f"Erro léxico na linha {self.line}, coluna {self.column}: {message}")

# Exemplo de código-fonte (substitua pelo seu código)
source_code = """
function main() {
    int x = 10;
    float y = 3.14;
    char c = 'A';
    if (x > 5) then {
        y = y + 1.0;
    } else {
        c = 'B';
    }
}
"""

analisador = LexicalAnalyzer(source_code)
tokens = analisador.analyze()

for token in tokens:
    print(f"Tipo: {token.token_type}, Lexema: {token.lexeme}, Posição: {token.position}")
