lexer grammar YarcLexer;

tokens {
 INDENT,
 DEDENT
}

options {
 superClass = YarcLexerBase;
 language = Python3;
}

// Keywords 'options', 'writer' and some other kw are considered keywords but only when followed by
// '{' or '(', and considered as a single token. Otherwise, the symbols are tokenized as NAME and
// allowed as an identifier.

// Setup
SCENARIO : 'scenario';
SETTINGS : 'settings' COLON;
WRITER   : 'writer';

SNIPPET : NESTED_CODE;

// Random distributions
UNIFORM     : 'Uniform' LPAREN;
NORMAL      : 'Normal' LPAREN;
CHOICE      : 'Choice' LPAREN;
SEQUENCE    : 'Sequence' LPAREN;
LOG_UNIFORM : 'LogUniform' LPAREN;

// Mesh creation/import
CREATE      : 'create';
INSTANTIATE : 'instantiate';

// Object getter
GET : 'get';

// Modifiers
X : 'x';
Y : 'y';
Z : 'z';

EDIT      : 'edit' | 'modify';
SET       : 'set';
TRANSLATE : 'translate';
ROTATE    : 'rotate';
SCALE     : 'scale';
SEMANTICS : 'semantics';

SCATTER : 'scatter' ('2d' | '3d')?;

// Behavior
EVERY  : 'every';
FRAMES : 'frame' 's'?;
TIME   : 'sec' ('ond' 's'?)?;

fragment NESTED_CODE:
 LBRACE (NESTED_CODE | .*?)
 /*( options {k=2; greedy=false;}: NESTED_CODE	|	.	)*  // v3 */ 
 RBRACE
;

// Everything that follows is a reduced version of the Python 3 Lexer (https://github.com/antlr/grammars-v4)

/* Keywords */
AND        : 'and';
AS         : 'as';
DEF        : 'def';
ELIF       : 'elif';
ELSE       : 'else';
FALSE      : 'False';
FOR        : 'for';
IF         : 'if';
IN         : 'in';
IS         : 'is';
NONE       : 'None';
NOT        : 'not';
OR         : 'or';
PASS       : 'pass';
RETURN     : 'return';
TRUE       : 'True';
UNDERSCORE : '_';
WITH       : 'with';

/* Operators */
DOT        : '.';
RANGE      : '..';
ELLIPSIS   : '...';
COMMA      : ',';
COLON      : ':';
SEMI_COLON : ';';

ASSIGN      : '=';
BIT_OR      : '|';
XOR         : '^';
BIT_AND     : '&';
BIT_NOT     : '~';
LEFT_SHIFT  : '<<';
RIGHT_SHIFT : '>>';
ADD         : '+';
MINUS       : '-';
DIV         : '/';
STAR        : '*';
MOD         : '%';
IDIV        : '//';
POWER       : '**';
AT          : '@';
ARROW       : '->';

LPAREN : '(' {self.openBrace();};
RPAREN : ')' {self.closeBrace();};
LBRACK : '[' {self.openBrace();};
RBRACK : ']' {self.closeBrace();};
LBRACE : '{' {self.openBrace();};
RBRACE : '}' {self.closeBrace();};

LESS_THAN     : '<';
GREATER_THAN  : '>';
EQUALS        : '==';
GT_EQ         : '>=';
LT_EQ         : '<=';
NOT_EQ        : '!=';
ADD_ASSIGN    : '+=';
SUB_ASSIGN    : '-=';
MULT_ASSIGN   : '*=';
AT_ASSIGN     : '@=';
DIV_ASSIGN    : '/=';
MOD_ASSIGN    : '%=';
AND_ASSIGN    : '&=';
OR_ASSIGN     : '|=';
XOR_ASSIGN    : '^=';
LSHIFT_ASSIGN : '<<=';
RSHIFT_ASSIGN : '>>=';
POWER_ASSIGN  : '**=';
IDIV_ASSIGN   : '//=';

/* Basic types */
STRING : STRING_LITERAL;
NUMBER : INTEGER | FLOAT_NUMBER;
NAME   : ID_START ID_CONTINUE*;

STRING_LITERAL: (
  ('u' | 'U')
  | ( ('f' | 'F')? ('r' | 'R'))
  | ( ('r' | 'R')? ('f' | 'F'))
 )? SHORT_STRING
;

INTEGER:
 DECIMAL_INTEGER
 | OCT_INTEGER
 | HEX_INTEGER
 | BIN_INTEGER
;

DECIMAL_INTEGER : NON_ZERO_DIGIT DIGIT* | '0'+;
OCT_INTEGER     : '0' ('o' | 'O') OCT_DIGIT+;
HEX_INTEGER     : '0' ('x' | 'X') HEX_DIGIT+;
BIN_INTEGER     : '0' ('b' | 'B') BIN_DIGIT+;

FLOAT_NUMBER : POINT_FLOAT | EXPONENT_FLOAT;

NEWLINE: (
  {self.atStartOfInput()}? SPACES
  | ( '\r'? '\n' | '\r' | '\f') SPACES?
 ) {self.onNewLine();}
;

SKIP_   : ( SPACES | COMMENT | LINE_JOINING) -> skip;
UNKNOWN : .;

/*  Fragments */
fragment SHORT_STRING:
 '\'' (STRING_ESCAPE_SEQ | ~('\\' | '\r' | '\n' | '\f' | '\''))* '\''
 | '"' (STRING_ESCAPE_SEQ | ~('\\' | '\r' | '\n' | '\f' | '"'))* '"'
;

fragment STRING_ESCAPE_SEQ : '\\' . | '\\' NEWLINE;

fragment NON_ZERO_DIGIT : '1' ..'9';
fragment DIGIT          : '0' ..'9';
fragment OCT_DIGIT      : '0' ..'7';
fragment HEX_DIGIT      : DIGIT | 'a' .. 'f' | 'A' .. 'F';
fragment BIN_DIGIT      : '0' | '1';

fragment POINT_FLOAT    : INT_PART? FRACTION | INT_PART '.';
fragment EXPONENT_FLOAT : ( INT_PART | POINT_FLOAT) EXPONENT;
fragment INT_PART       : DIGIT+;
fragment FRACTION       : '.' DIGIT+;
fragment EXPONENT       : ('e' | 'E') ('+' | '-')? DIGIT+;

fragment ID_START    : UNDERSCORE | LETTER;
fragment ID_CONTINUE : ID_START | DIGIT;
fragment LETTER      : 'a' ..'z' | 'A' ..'Z';

fragment SPACES       : ( ' ' | '\t')+;
fragment COMMENT      : '#' ~('\r' | '\n' | '\f')*;
fragment LINE_JOINING : '\\' SPACES? ( '\r'? '\n' | '\r' | '\f');