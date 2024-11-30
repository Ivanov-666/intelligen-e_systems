import re

from consts import action_map, goto_map, productions
from parser import LR_Parser

input_string = 'function ( 2 + 4 / 8 != wdfsdf )'
input_string = re.sub('\d', 'int', input_string)
tokens = input_string.split(' ')
parser = LR_Parser(action_map, goto_map, productions)

parser.parse(tokens)