parser grammar YarcParser;

options {
    superClass = YarcParserBase;
    tokenVocab = YarcLexer;
    language = Python3;
}

// file_input: (NEWLINE | stmt)* EOF;

file_input : head NEWLINE* body EOF; 
            
head: header 
      (expr_stmt | NEWLINE)* 
      settings?
      (expr_stmt | NEWLINE)* 
      writer? 
;

body: stmts* ;

header: SCENARIO name ;

// Settings
settings : SETTINGS ':' NEWLINE INDENT setting+ DEDENT;
setting :  option | LIB '=' test NEWLINE;

// Writer definition
writer: WRITER ID (':' NEWLINE INDENT writer_attr+ DEDENT)? ;
writer_attr: option ;

option : ID '=' test NEWLINE ;


stmts: '=='+;

/* Expressions */
test: or_test ('if' or_test 'else' test)?;
test_nocond: or_test;
or_test: and_test ('or' and_test)*;
and_test: not_test ('and' not_test)*;
not_test: 'not' not_test | comparison;
comparison: expr (comp_op expr)*;
comp_op: '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not';
expr: xor_expr ('|' xor_expr)*;
xor_expr: and_expr ('^' and_expr)*;
and_expr: shift_expr ('&' shift_expr)*;
shift_expr: arith_expr (('<<'|'>>') arith_expr)*;
arith_expr: term (('+'|'-') term)*;
term: factor (('*'|'/'|'%'|'//') factor)*;
factor: ('+'|'-'|'~') factor | power;
power: atom_expr ('**' factor)?;
atom_expr: atom trailer*;
atom: '(' testlist_comp? ')'
   | '[' testlist_comp? ']'
   | '<' testlist_comp? '>'
   | '{' dictorsetmaker? '}'
   | name | signed_number | STRING | '...' | 'none' | 'true' | 'false' ;

name : ID | '_' | primitives | VISIBLE | SIZE | LOOK_AT | UP_AXIS | SEMANTICS | TEXTURE;
primitives: SHAPES | STEREO? CAMERA | LIGHT | MATERIAL ;
signed_number: NUMBER | '-' NUMBER ;

testlist_comp: test ( comp_for | (',' test)* ','? );
trailer: '(' arglist? ')' |'[' subscriptlist ']' | '.' name ;
arglist: argument (',' argument)* ','?;
argument: test comp_for? | test '=' test;

subscriptlist: subscript_ (',' subscript_)* ','?;
subscript_: test | test? ':' test? sliceop?;
sliceop: ':' test?;
exprlist: expr (',' expr)* ','?;
testlist: test (',' test)* ','?;
dictorsetmaker: ( (test ':' test (comp_for | (',' test ':' test)* ','?)) |
                  (test (comp_for | (',' test)* ','?)) );

comp_iter: comp_for | comp_if;
comp_for: 'for' exprlist 'in' or_test comp_iter?;
comp_if: 'if' test_nocond comp_iter?;

expr_stmt: testlist (augassign | '=') testlist NEWLINE;
augassign: ('+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' |
            '<<=' | '>>=' | '**=' | '//=');
        
