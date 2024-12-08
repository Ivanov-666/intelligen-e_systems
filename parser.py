class LLParser:
    def __init__(self, parsing_table):
        """
        Инициализация LL-парсера.

        :param parsing_table: Таблица переходов (dict[Nonterminal][Terminal] -> Rule)
        """
        self.parsing_table = parsing_table
        self.stack = []
        self.input_stream = []

    def parse(self, input_string):
        """
        Выполняет парсинг входной строки.

        :param input_string: Входная строка для разбора.
        :return: True, если строка успешно разобрана, иначе ошибка.
        """
        self.stack = ["$", "E"]
        self.input_stream = input_string + ["$"]

        while self.stack:
            stack_top = self.stack.pop()
            current_input = self.input_stream[0]

            try:
                rule = self.parsing_table[stack_top][current_input]
                _, production = rule.split("->")
                production = production.strip()
                self.stack.extend(reversed(production.split()))
                self.stack = list(filter(lambda x: x != "''", self.stack))
            except KeyError:
                try:
                    self.input_stream.remove(stack_top * (stack_top == current_input))
                except ValueError:
                    raise SyntaxError(f"Unexpected symbol '{current_input}' on stack '{stack_top}'")

        return all(map(lambda x: x == "$", self.input_stream))