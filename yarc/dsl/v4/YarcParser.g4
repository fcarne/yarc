parser grammar YarcParser;

options {
    superClass = YarcParserBase;
    tokenVocab = YarcLexer;
    language = Python3;
}

// All comments that start with "///" are copy-pasted from
// The Python Language Reference

file_input: (NEWLINE)* EOF;

stmt: simple_stmts | compound_stmt;
simple_stmts: simple_stmt (';' simple_stmt)* ';'? NEWLINE;
simple_stmt: (expr_stmt | pass_stmt );
expr_stmt: testlist_star_expr (annassign | augassign (testlist) |
                     ('=' (testlist_star_expr))*);
annassign: ':' test ('=' test)?;
testlist_star_expr: (test|star_expr) (',' (test|star_expr))* ','?;
augassign: ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' |
            '<<=' | '>>=' | '**=' | '//=');
// For normal and annotated assignments, additional restrictions enforced by the interpreter
pass_stmt: '...';
return_stmt: 'return' testlist?;
// note below: the ('.' | '...') is necessary because '...' is tokenized as ELLIPSIS
import_as_name: name;
dotted_as_name: dotted_name;
import_as_names: import_as_name (',' import_as_name)* ','?;
dotted_as_names: dotted_as_name (',' dotted_as_name)*;
dotted_name: name ('.' name)*;

compound_stmt: if_stmt | for_stmt;
if_stmt: 'if' test ':' block ('else' ':' block)?;
for_stmt: 'for' exprlist 'in' testlist ':' block ('else' ':' block)?;
// NB compile.c makes sure that the default except clause is last
block: simple_stmts | NEWLINE INDENT stmt+ DEDENT;
subject_expr: star_named_expression ',' star_named_expressions? | test ;
star_named_expressions: ',' star_named_expression+ ','? ;
star_named_expression: '*' expr | test ;
guard: 'if' test ;
patterns: open_sequence_pattern | pattern ;
pattern: or_pattern ;
or_pattern: closed_pattern ('|' closed_pattern)* ;
closed_pattern: literal_pattern | capture_pattern | wildcard_pattern | value_pattern | group_pattern | sequence_pattern | mapping_pattern | class_pattern ;
literal_pattern: signed_number { $parser.CannotBePlusMinus() }? | complex_number | strings | 'none' | 'true' | 'false' ;
literal_expr: signed_number { $parser.CannotBePlusMinus() }? | complex_number | strings | 'none' | 'true' | 'false' ;
complex_number: signed_real_number '+' imaginary_number 
    | signed_real_number '-' imaginary_number  
    ;
signed_number: NUMBER | '-' NUMBER ;
signed_real_number: real_number | '-' real_number ;
real_number: NUMBER ;
imaginary_number: NUMBER ;
capture_pattern: pattern_capture_target ;
pattern_capture_target: /* cannot be '_' */ name { $parser.CannotBeDotLpEq() }? ;
wildcard_pattern: '_' ;
value_pattern: attr { $parser.CannotBeDotLpEq() }? ;
attr: name ('.' name)+ ;
name_or_attr: attr | name ;
group_pattern: '(' pattern ')' ;
sequence_pattern:
    '[' maybe_sequence_pattern? ']' 
    | '(' open_sequence_pattern? ')' 
    ;
open_sequence_pattern: maybe_star_pattern ',' maybe_sequence_pattern? ;
maybe_sequence_pattern: maybe_star_pattern (',' maybe_star_pattern)* ','? ;
maybe_star_pattern: star_pattern | pattern ;
star_pattern:
    '*' pattern_capture_target 
    | '*' wildcard_pattern 
    ;
mapping_pattern: '{' '}' 
    | '{' double_star_pattern ','? '}' 
    | '{' items_pattern ',' double_star_pattern ','? '}' 
    | '{' items_pattern ','? '}' 
    ;
items_pattern: key_value_pattern (',' key_value_pattern)* ;
key_value_pattern: (literal_expr | attr) ':' pattern ;
double_star_pattern: '**' pattern_capture_target ;
class_pattern: name_or_attr '(' ')' 
    | name_or_attr '(' positional_patterns ','? ')' 
    | name_or_attr '(' keyword_patterns ','? ')' 
    | name_or_attr '(' positional_patterns ',' keyword_patterns ','? ')' 
    ;
positional_patterns: pattern (',' pattern)* ;
keyword_patterns: keyword_pattern (',' keyword_pattern)* ;
keyword_pattern: name '=' pattern ;

test: or_test ('if' or_test 'else' test)?;
test_nocond: or_test;
or_test: and_test ('or' and_test)*;
and_test: not_test ('and' not_test)*;
not_test: 'not' not_test | comparison;
comparison: expr (comp_op expr)*;
// <> isn't actually a valid comparison operator in Python. It's here for the
// sake of a __future__ import described in PEP 401 (which really works :-)
comp_op: '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not';
star_expr: '*' expr;
expr: xor_expr ('|' xor_expr)*;
xor_expr: and_expr ('^' and_expr)*;
and_expr: shift_expr ('&' shift_expr)*;
shift_expr: arith_expr (('<<'|'>>') arith_expr)*;
arith_expr: term (('+'|'-') term)*;
term: factor (('*'|'@'|'/'|'%'|'//') factor)*;
factor: ('+'|'-'|'~') factor;
atom: name | NUMBER | STRING+ | '...' | 'none' | 'true' | 'false' ;
name : ID | '_' ;
subscriptlist: subscript_ (',' subscript_)* ','?;
subscript_: test | test? ':' test? sliceop?;
sliceop: ':' test?;
exprlist: (expr|star_expr) (',' (expr|star_expr))* ','?;
testlist: test (',' test)* ','?;


// not used in grammar, but may appear in "node" passed from Parser to Compiler
encoding_decl: name;


strings: STRING+ ;
