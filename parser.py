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
            (0, 0, 0, 0): self.ZeroState,
            (0, 0, 1, 0): self.ErrorState,
            (0, 0, 1, 1): self.ErrorStackState,
            (0, 1, 1, 0): self.ReturnErrorState,
            (1, 0, 1, 0): self.AcceptErrorState,
            (1, 1, 1, 0): self.AcceptReturnErrorState,
        }

    def parse(self, input_string):
        start_state_id = 100
        is_final=False
        self.input_stream = input_string + ["eof"]

        while not (len(self.stack) == 0 and self.input_stream == ['eof']):
            try:
                row = self.parsing_table[self.parsing_table["State"] == start_state_id]
                start_state_id, is_final = self.row_func[tuple(row[['Accept', 'Return', 'Error', 'Stack']].iloc[0])](row, self.input_stream[0])
            except:
                return False
        return True

    def ZeroState(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            return row['NextState'].iloc[0], False
        except:
            raise SyntaxError()
    
    def ErrorState(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            return row['NextState'].iloc[0], False
        except:
            raise SyntaxError()
    
    def ErrorStackState(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            self.stack.append(row['State'].iloc[0]+1)
            return row['NextState'].iloc[0], False
        except:
            raise SyntaxError()
    
    def ReturnErrorState(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            return self.stack.pop(), True
        except:
            raise SyntaxError()
        
    def AcceptErrorState(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            self.input_stream = self.input_stream[1:]
            return self.stack.pop(), False
        except:
            raise SyntaxError()

    def AcceptReturnErrorState(self, row, current_token):
        try:
            assert current_token in row['M'].iloc[0]
            self.input_stream = self.input_stream[1:]
            return row['NextState'].iloc[0], True
        except:
            raise SyntaxError()
