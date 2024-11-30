class LR_Parser:
    def __init__(self, action_table, goto_table, productions):
        self.action_table = action_table
        self.goto_table = goto_table
        self.productions = productions
        self.handlers = {
            "s": self.shift,
            "r": self.reduce,
            "a": self.accept,
        }

    def parse(self, tokens):
        stack = [0]
        tokens.append('$')
        parsing_end = False

        while parsing_end != True:
            state = stack[-1]
            current_token = tokens[0]

            try: 
                action = self.action_table[state].get(current_token)
                action_type, next_state = action[0], action[1:]
            except:
                raise ValueError(f"Ошибка синтаксического анализа в состоянии {state}")

            
            parsing_end = self.handlers[action_type](stack, tokens, next_state)

    def shift(self, stack, tokens, next_state):
        """Обрабатывает действие shift."""
        token = tokens.pop(0)
        stack.append(token)
        stack.append(int(next_state))
        return False

    def reduce(self, stack, tokens, production_index):
        """Обрабатывает действие reduce."""
        production_index = int(production_index)
        lhs, rhs = self.productions[production_index]
        for _ in range(2 * len(rhs)):
            stack.pop()
        state = stack[-1]
        stack.append(lhs)

        try:
            next_state = self.goto_table[state].get(lhs)
        except:
            raise SyntaxError(f"Ошибка синтаксического анализа в состоянии {state} при продукции '{lhs} -> {rhs}'")
        
        stack.append(next_state)
        return False

    def accept(self, stack, tokens, *args):
        """Обрабатывает действие accept."""
        print("Анализ завершен: входное выражение принадлежит языку.")
        return True
    