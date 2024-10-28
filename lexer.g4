lexer grammar SpaceBattleLexer;

ENTITY: 'Player'| 'Game';           
MAY: 'can_order';                 
COMMAND: 'command'; 
INCLUDES: 'includes';
CREATE: 'create';
SECONDS: 'seconds';
SPAWN: 'spawn';
EVERY: 'every';

COMMA: ',';
INT : [0-9]+ ;
RULE: [a-zA-Z]+ '_Command';
TYPE: [a-zA-Z]+ '_Type';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE: '\r'? '\n';
WS: [ \t\r\n]+ -> skip;
