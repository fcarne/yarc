lexer grammar YarcLexer;

options {
  superClass=YarcLexerBase;
  language=Python;
}


tokens {
  INDENT;
  DEDENT;
}

@header {
if __name__ is not None and "." in __name__:
    from .YarcLexerBase import YarcLexerBase
else:
    from YarcLexerBase import YarcLexerBase
}

/* Sections */
SCENARIO : 'scenario';
SETTINGS : 'settings';
STAGE    : 'stage';
WRITERS  : 'writers';

/* Primitives */
SHAPES           : 'Plane' | 'Cube' | 'Cone' | 'Torus';
SHAPES_OR_LIGHTS : 'Sphere' | 'Cylinder' | 'Disk';
CAMERA           : 'Camera';
LIGHT            : 'Light';
LIGHT_TYPE       : 'Rect' | 'Dome' | 'Distant';
STEREO           : 'Stereo';
MATERIAL         : 'Material';
TIMELINE         : 'Timeline';

/* Scene construction */
OPEN        : 'open';
CREATE      : 'create';
GROUP       : 'group';
INSTANTIATE : 'instantiate';
GET         : 'get';
EDIT        : 'edit';

/* Resource retriever */
/* Resource retriever */
FETCH     : 'fetch';
MATCH     : 'match';
LIMIT     : 'limit';
RECURSIVE : 'recursive';

/* Modifiers */
TRANSLATE     : 'translate';
CAM_TRANSLATE : 'camera_translate';
ROTATE        : 'rotate';
SCALE         : 'scale';
SEMANTICS     : 'semantics';
VISIBLE       : 'visible';
SIZE          : 'size';
LOOK_AT       : 'look_at';
UP_AXIS       : 'up_axis'; // look at ... up
AXIS          : 'x' | 'y' | 'z' | 'X' | 'Y' | 'Z';
ORDER         : AXIS AXIS AXIS;

/* Compound rules */
SCATTER    : 'scatter_' ('2d' | '3d');
ROT_AROUND : 'rotate_around';
PHYSICS    : 'collider' | 'kinematics' | 'rigid_body' | 'physics_material';

/* Dynamic behavior */ 
EVERY  : 'every';
FRAMES : 'frame' 's'?;
TIME   : 'sec' ('ond' 's'?)?;

/* Distributions */
UNIFORM     : 'Uniform';
NORMAL      : 'Normal';
CHOICE      : 'Choice';
SEQUENCE    : 'Sequence';
LOG_UNIFORM : 'LogUniform';

// Native code snippets
SNIPPET : NESTED_CODE { print("FOUND SNIPPET CODE!") } {self.skip()} ;

fragment NESTED_CODE:
  LBRACE LBRACE 
    ( options {k=2; greedy=false;}: NESTED_CODE	|	.	)*  // v3 
  RBRACE RBRACE
;

/* Additional keywords to be more natural language-like */ 
TO : 'to'; // translate to
ON : 'on'; // scatter on
AT : 'at'; // get ... at ...
/* 
 * Everything that follows is a reduced version of the Python 3 Lexer
 * found at (https://github.com/antlr/grammars-v4) 
 */

/* Keywords */
AND        : 'and';
ELSE       : 'else';
FALSE      : 'false';
FOR        : 'for';
FROM       : 'from';
IF         : 'if';
IN         : 'in';
IS         : 'is';
NONE       : 'none';
NOT        : 'not';
OR         : 'or';
TRUE       : 'true';
UNDERSCORE : '_';

/* Operators */
DOT      : '.';
RANGE    : '..';
ELLIPSIS : '...';
COMMA    : ',';
COLON    : ':';
SEMI     : ';';

ASSIGN  : '=';
BIT_OR  : '|';
XOR     : '^';
BIT_AND : '&';
BIT_NOT : '~';
LSHIFT  : '<<';
RSHIFT  : '>>';
PLUS    : '+';
MINUS   : '-';
MUL    : '*';
DIV     : '/';
MOD     : '%';
IDIV    : '//';
POWER   : '**';

LPAREN : '(' {self.openBrace()};
RPAREN : ')' {self.closeBrace()};
LBRACK : '[' {self.openBrace()};
RBRACK : ']' {self.closeBrace()};
LBRACE : '{' {self.openBrace()};
RBRACE : '}' {self.closeBrace()};

LT     : '<';
GT     : '>';
EQUALS : '==';
GT_EQ  : '>=';
LT_EQ  : '<=';
NOT_EQ : '!=';

ADD_ASSIGN    : '+=';
SUB_ASSIGN    : '-=';
MULT_ASSIGN   : '*=';
DIV_ASSIGN    : '/=';
MOD_ASSIGN    : '%=';
AND_ASSIGN    : '&=';
OR_ASSIGN     : '|=';
XOR_ASSIGN    : '^=';
LSHIFT_ASSIGN : '<<=';
RSHIFT_ASSIGN : '>>=';
POWER_ASSIGN  : '**=';
IDIV_ASSIGN   : '//=';

/* Identifiers */
ID         : ID_START ID_CONTINUE*;
SETTING_ID : '$' ID;

/* Basic types */
STRING: 
  ( ('u' | 'U')
  | ( ('f' | 'F')? ('r' | 'R'))
  | ( ('r' | 'R')? ('f' | 'F'))
  )? SHORT_STRING
;


INTEGER : 
  NON_ZERO_DIGIT DIGIT* | '0'+ // Decimal integer 
  | '0' ('o' | 'O') OCT_DIGIT+ // Octal integer 
  | '0' ('x' | 'X') HEX_DIGIT+ // Hexadecimal integer 
  | '0' ('b' | 'B') BIN_DIGIT+ // Binary integer
;

FLOAT_NUMBER : POINT_FLOAT | EXPONENT_FLOAT;

// Newline
NEWLINE:
  (
  ( '\r'? '\n' | '\r' | '\f') SPACES?
  ) {self.onNewLine();}
;

/* Misc */
SKIP_   : ( SPACES | COMMENT | LINE_JOINING) {self.skip()};
UNKNOWN : .;

/* Fragments */
fragment SHORT_STRING:
  '\'' (STRING_ESCAPE_SEQ | ~('\\' | '\r' | '\n' | '\f' | '\''))* '\''
  | '"' (STRING_ESCAPE_SEQ | ~('\\' | '\r' | '\n' | '\f' | '"'))* '"'
;
fragment STRING_ESCAPE_SEQ : '\\' ~('\t' | ' ' | '\r' | '\n' | '\f') | '\\' NEWLINE;

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
