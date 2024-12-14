import re
import pandas as pd
from parser import LLParser

parsing_table = pd.read_csv('table.csv')
parser = LLParser(parsing_table)

input_string = "type id = true && false ;"
input_string = re.sub('\d', 'int', input_string)
tokens = input_string.split(' ')

result = parser.parse(tokens)
print(result)

