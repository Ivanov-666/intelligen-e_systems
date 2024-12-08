parsing_table = {
    'E': {
        '(': "E -> T E'", 
        'int': "E -> T E'", 
        'false': "E -> T E'", 
        'true': "E -> T E'", 
        'function': "E -> T E'"
    },
    "E'": {
        '+': "E' -> + T E'",
        '-': "E' -> - T E'",
        ')': "E' -> ''",
        ',': "E' -> ''",
        '$': "E' -> ''"
    },
    'T': {
        '(': "T -> F T'",
        'int': "T -> F T'",
        'false': "T -> F T'",
        'true': "T -> F T'",
        'function': "T -> F T'"},
    "T'": {
        '+': "T' -> ''",
        '-': "T' -> ''",
        '*': "T' -> * F T'",
        '/': "T' -> / F T'",
        '||': "T' -> || F T'",
        '&&': "T' -> && F T'",
        '!=': "T' -> != F T'",
        '==': "T' -> == F T'",
        '>': "T' -> > F T'",
        '<': "T' -> < F T'",
        ')': "T' -> ''",
        ',': "T' -> ''",
        '$': "T' -> ''"
    },
    'F': {
        '(': 'F -> ( E )',
        'int': 'F -> int',
        'false': 'F -> false',
        'true': 'F -> true',
        'function': 'F -> function ( Args )'
    },
    'Args': {
        '(': "Args -> E Args'",
        'int': "Args -> E Args'",
        'false': "Args -> E Args'",
        'true': "Args -> E Args'",
        'function': "Args -> E Args'"
    },
    "Args'": {
        ')': "Args' -> ''",
        ',': "Args' -> , E Args'"
    }
}