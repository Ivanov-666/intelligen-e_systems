grammar SpaceBattleParser;
options { tokenVocab=SpaceBattleLexer; }

rules
    : rule (NEWLINE rule)* NEWLINE?
    ;

rule
    : order
    | ruleExtention
    | create
    | spawn
    ;
    
create
    : CREATE ID TYPE;
    
order
    : ENTITY MAY TYPE RULE (',' RULE)* 
    ;

ruleExtention
    : RULE INCLUDES RULE (',' RULE)*
    ;
    
spawn
    : SPAWN TYPE EVERY INT SECONDS
    ;


