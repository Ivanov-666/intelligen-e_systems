import re

from consts import parsing_table
from parser import LLParser

parser = LLParser(parsing_table)

# Пример входной строки
input_string = "function ( 1 + 2 , 4 )"
input_string = re.sub('\d', 'int', input_string)
tokens = input_string.split(' ')
try:
    result = parser.parse(tokens)
    print("Строка успешно разобрана:", result)
except SyntaxError as e:
    print("Ошибка разбора:", e)
    
