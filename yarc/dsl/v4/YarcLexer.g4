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
// '{' or '(', and considered as a single token. Otherwise, the symbols are tokenized as ID and
// allowed as an identifier.

// Setup
SCENARIO : 'scenario';
SETTINGS : 'settings';
WRITER   : 'writer';

// Primitives
SHAPES: 'plane' |'cube'| 'sphere' | 'cylinder'|'cone' |'torus' | 'disk';
CAMERA : 'camera';
LIGHT : 'light';
STEREO : 'stereo';
MATERIAL: 'material';
TIMELINE: 'timeline';

// Mesh creation/import
CREATE      : 'create';
INSTANTIATE : 'instantiate';
GROUP : 'group';
OPEN        : 'open';

// Getters: Scene nodes and files
GET : 'get';
FETCH : 'fetch';
MATCH: 'match' | 'like';


// Modifiers
EDIT      : 'edit' | 'modify';
SET       : 'set';

TRANSLATE : 'translate';
ROTATE    : 'rotate';
SCALE     : 'scale';
SEMANTICS : 'semantics';
VISIBLE   : 'visible';
SIZE      : 'size';
LOOK_AT   : 'look_at';
UP_AXIS : 'up_axis'; // look at ... up
AXIS : 'x' | 'y' | 'z' | 'X' | 'Y' | 'Z' ;

// Complex rules
SCATTER : 'scatter';
SCATTER_TYPE: '2d' | '3d' ;
AROUND : 'around';
TEXTURE: 'texture';

// Dynamic Behavior
EVERY  : 'every';
FRAMES : 'frame' 's'?;
TIME   : 'sec' ('ond' 's'?)?;

// Random distributions
UNIFORM     : 'Uniform';
NORMAL      : 'Normal' ;
CHOICE      : 'Choice' ;
SEQUENCE    : 'Sequence' ;
LOG_UNIFORM : 'LogUniform';

// Native code snippets
SNIPPET : NESTED_CODE { print("FOUND SNIPPET CODE!") } -> skip;

fragment NESTED_CODE:
 LBRACE LBRACE (NESTED_CODE | .)*?
 /*( options {k=2; greedy=false;}: NESTED_CODE	|	.	)*  // v3 */ 
 RBRACE RBRACE
;

// Additional keywords to be more natural language-like
TO : 'to'; // translate to
ON : 'on'; // scatter on
AT : 'at'; // get ... at ...

// Everything that follows is a reduced version of the Python 3 Lexer (https://github.com/antlr/grammars-v4)

/* Keywords */
AND        : 'and';
DEF        : 'def';
ELSE       : 'else';
FALSE      : 'false';
FOR        : 'for';
IF         : 'if';
IN         : 'in';
IS         : 'is';
NONE       : 'none';
NOT        : 'not';
OR         : 'or';
RETURN     : 'return';
TRUE       : 'true';
UNDERSCORE : '_';

/* Operators */
DOT        : '.';
RANGE      : '..';
ELLIPSIS   : '...';
COMMA      : ',';
COLON      : ':';
SEMI       : ';';

ASSIGN      : '=';
BIT_OR      : '|';
XOR         : '^';
BIT_AND     : '&';
BIT_NOT     : '~';
LSHIFT  : '<<';
RSHIFT : '>>';
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
ID   : ID_START ID_CONTINUE*;
OPTION_ID : '$' ID ; 

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

// Newline
NEWLINE: (
  {self.atStartOfInput()}? SPACES
  | ( '\r'? '\n' | '\r' | '\f') SPACES?
 ) {self.onNewLine();}
;

// Misc
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