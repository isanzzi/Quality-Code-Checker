grammar CodeQualityDSL;

// Parser Rules
program
    : rule_definition+ EOF
    ;

rule_definition
    : 'rule' STRING '{' rule_body '}'
    ;

rule_body
    : rule_attribute+
    ;

rule_attribute
    : 'target' ':' target_type
    | 'condition' ':' condition_expr
    | 'severity' ':' severity_level
    | 'message' ':' STRING
    ;

target_type
    : 'function'
    | 'class'
    | 'variable'
    | 'import'
    ;

severity_level
    : 'error'
    | 'warning'
    | 'info'
    ;

condition_expr
    : comparison_expr                                    # ComparisonCondition
    | condition_expr AND condition_expr                  # AndCondition
    | condition_expr OR condition_expr                   # OrCondition
    | NOT condition_expr                                 # NotCondition
    | '(' condition_expr ')'                            # ParenCondition
    | IDENTIFIER '(' STRING ')'                         # FunctionCallCondition
    | IDENTIFIER                                        # IdentifierCondition
    ;

comparison_expr
    : IDENTIFIER operator NUMBER
    ;

operator
    : '>'
    | '<'
    | '>='
    | '<='
    | '=='
    | '!='
    ;

// Lexer Rules
AND: 'AND';
OR: 'OR';
NOT: '!' | 'NOT';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
STRING: '"' (~["\r\n])* '"';

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
