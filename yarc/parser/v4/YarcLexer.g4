lexer grammar YarcLexer;

tokens { INDENT, DEDENT }

options {
    superClass=YarcLexerBase;
    language = Python3;
}

SCENARIO : 'scenario' ;
OPTIONS : 'options' OPEN_BRACE ;
WRITER : 'writer' OPEN_BRACE ;
SNIPPET :	NESTED_CODE;

fragment NESTED_CODE 
 : OPEN_BRACE
  ( NESTED_CODE |.*? )
	/*( options {k=2; greedy=false;}
	:   NESTED_CODE
	|	.
	)* 
  // v3 */
	CLOSE_BRACE
   ;

// Everything that follows is a reduced version of the Python 3 Lexer (https://github.com/antlr/grammars-v4)

/* Keywords */ 
AND : 'and';
AS : 'as';
DEF : 'def';
DEL : 'del';
ELIF : 'elif';
ELSE : 'else';
FALSE : 'False';
FOR : 'for';
IF : 'if';
IN : 'in';
IS : 'is';
NONE : 'None';
NOT : 'not';
OR : 'or';
PASS : 'pass';
RETURN : 'return';
TRUE : 'True';
UNDERSCORE : '_' ;
WITH : 'with';

/* Operators, assignments and parenthesis */
DOT : '.';
RANGE : '..';
ELLIPSIS : '...';

STAR : '*';
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';

ASSIGN : '=';

OR_OP : '|';
XOR : '^';
AND_OP : '&';
NOT_OP : '~';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';
ADD : '+';
MINUS : '-';
DIV : '/';
MOD : '%';
IDIV : '//';
POWER : '**';
AT : '@';
ARROW : '->';

OPEN_PAREN : '(' {self.openBrace();};
CLOSE_PAREN : ')' {self.closeBrace();};
OPEN_BRACK : '[' {self.openBrace();};
CLOSE_BRACK : ']' {self.closeBrace();};
OPEN_BRACE : '{' {self.openBrace();};
CLOSE_BRACE : '}' {self.closeBrace();};

LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ : '!=';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MULT_ASSIGN : '*=';
AT_ASSIGN : '@=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
LEFT_SHIFT_ASSIGN : '<<=';
RIGHT_SHIFT_ASSIGN : '>>=';
POWER_ASSIGN : '**=';
IDIV_ASSIGN : '//=';

/* Basic types */

STRING
 : STRING_LITERAL
 ;

NUMBER
 : INTEGER
 | FLOAT_NUMBER
 ;

NAME
 : ID_START ID_CONTINUE*
 ;

NEWLINE
 : ( {self.atStartOfInput()}?   SPACES
   | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
   )
   {self.onNewLine();}
 ;

STRING_LITERAL
 : ( ('u' | 'U') 
   | ( ('f' | 'F')? ('r' | 'R') ) 
   | ( ('r' | 'R')? ('f' | 'F') ) 
   )? SHORT_STRING
 ;


INTEGER
 : DECIMAL_INTEGER
 | OCT_INTEGER
 | HEX_INTEGER
 | BIN_INTEGER
 ;

DECIMAL_INTEGER
 : NON_ZERO_DIGIT DIGIT*
 | '0'+
 ;

OCT_INTEGER
 : '0' ('o' | 'O') OCT_DIGIT+
 ;

HEX_INTEGER
 : '0' ('x' | 'X') HEX_DIGIT+
 ;

BIN_INTEGER
 : '0' ('b' | 'B') BIN_DIGIT+
 ;

FLOAT_NUMBER
 : POINT_FLOAT
 | EXPONENT_FLOAT
 ;

SKIP_
 : ( SPACES | COMMENT | LINE_JOINING ) -> skip
 ;

UNKNOWN_CHAR
 : .
 ;

/*  Fragments */

fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~('\\' | '\r' | '\n' | '\f' | '\'') )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~('\\' | '\r' | '\n' | '\f' | '"') )* '"'
 ;

fragment STRING_ESCAPE_SEQ
 : '\\' .
 | '\\' NEWLINE
 ;

fragment NON_ZERO_DIGIT
 : '1'..'9'
 ;

fragment DIGIT
 : '0'..'9'
 ;

fragment OCT_DIGIT
 : '0'..'7'
 ;

fragment HEX_DIGIT
 : DIGIT | 'a' .. 'f' | 'A' .. 'F' 
 ;

fragment BIN_DIGIT
 : '0' | '1'
 ;

fragment POINT_FLOAT
 : INT_PART? FRACTION
 | INT_PART '.'
 ;

fragment EXPONENT_FLOAT
 : ( INT_PART | POINT_FLOAT ) EXPONENT
 ;

fragment INT_PART
 : DIGIT+
 ;

fragment FRACTION
 : '.' DIGIT+
 ;

fragment EXPONENT
 : ('e' | 'E') ('+' | '-')? DIGIT+
 ;

fragment SPACES
 : ( ' ' | '\t')+
 ;

fragment COMMENT
 : '#' ~('\r' | '\n' | '\f')*
 ;

fragment LINE_JOINING
 : '\\' SPACES? ( '\r'? '\n' | '\r' | '\f')
 ;

fragment LETTER
 : 'a'..'z' | 'A'..'Z'
 ; 

fragment ID_START
 : UNDERSCORE | LETTER       
 ;

fragment ID_CONTINUE
 : ID_START | DIGIT
 ;
