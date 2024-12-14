class LLParser:
    def __init__(self, parsing_table):
        """
        Инициализация LL-парсера.

        :param parsing_table: Таблица переходов (dict[Nonterminal][Terminal] -> Rule)
        """
        self.parsing_table = parsing_table
        self.stack = ["eof"]
        self.input_stream = []

        self.row_func = {
            (0, 0, 0, 0): self.zero,
            (0, 0, 1, 0): self.error,
            (0, 0, 1, 1): self.error_stack,
            (0, 1, 1, 0): self.return_error,
            (1, 0, 1, 0): self.accept_error,
            (1, 1, 1, 0): self.accept_return_error,
        }

    def parse(self, input_string):
        start_state_id = 100
        is_final=False
        self.input_stream = input_string + ["eof"]

        while not (len(self.stack) == 0 and self.input_stream == ['eof']):
            try:
                row = self.parsing_table[self.parsing_table["State"] == start_state_id]
                start_state_id  = self.row_func[tuple(row[['Accept', 'Return', 'Error', 'Stack']].iloc[0])](row, self.input_stream[0])
            except:
                return False
        return True

    def zero(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            return row['NextState'].iloc[0]
        except:
            raise SyntaxError()
    
    def error(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            return row['NextState'].iloc[0]
        except:
            raise SyntaxError()
    
    def error_stack(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            self.stack.append(row['State'].iloc[0]+1)
            return row['NextState'].iloc[0]
        except:
            raise SyntaxError()
    
    def return_error(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            return self.stack.pop()
        except:
            raise SyntaxError()
        
    def accept_error(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            self.input_stream = self.input_stream[1:]
            return self.stack.pop()
        except:
            raise SyntaxError()

    def accept_return_error(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            self.input_stream = self.input_stream[1:]
            return row['NextState'].iloc[0]
        except:
            raise SyntaxError()
