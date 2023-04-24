parser grammar YarcParser;

options {
  superClass = YarcParserBase;
  tokenVocab = YarcLexer;
  language = Python3;
}

scene       : declaration header stmts EOF; // Starting rule
declaration : 'scenario' name NEWLINE;
header      : (settings | expr_stmt | writer | NEWLINE)*;
stmts       : open_stmt? ( create_stmt | edit_stmt | behavior_stmt | expr_stmt | NEWLINE)*;

/* Settings and writers */
settings : 'settings' ':' NEWLINE INDENT setting+ DEDENT;
setting  : LIB '=' test NEWLINE | option;
writer   : WRITER ID (':' NEWLINE INDENT option+ DEDENT)?;
option   : ID '=' test NEWLINE;

/* Statements */
/* Scene object creation and modifcation statements */
open_stmt   : 'open' test NEWLINE;
create_stmt : (name '=')? (create_expr | instantiate_expr | get_expr | group_expr);
edit_stmt   : EDIT name edit_block;

create_expr      : 'create' test? test edit_block?;
instantiate_expr : 'instantiate' test_or_distribution? test edit_block?;
group_expr       : 'group' '[' name (',' name)* ','? ']' edit_block?;
get_expr         : 'get' name 'at' test (':' NEWLINE INDENT simple_attr+ DEDENT)?;

edit_block       : ':' NEWLINE INDENT (attr | inner_behavior_stmt)+ DEDENT;

attr          : simple_attr | compound_attr | modify_attr;
simple_attr   : expr_stmt | modifier;
modifier      : name (':' name)? test_or_distribution? NEWLINE;

compound_attr : SCATTER; // TODO: finish this

modify_attr: // Special modifiers that must be treated in a specific way
  (
    'translate' AXIS? 'to' test_or_distribution
    | 'camera' 'translate' 'to' test_or_distribution
    | 'rotate' AXIS? test_or_distribution ORDER?
    | 'scale' test_or_distribution
    | 'look_at' test_or_distribution
    | 'size' test_or_distribution
    | 'semantics' test_or_distribution
    | 'visible' test_or_distribution
  ) NEWLINE
;

inner_behavior_stmt  : behavior_stmt inner_behavior_block;
inner_behavior_block : ':' NEWLINE INDENT attr+ DEDENT;

test_or_distribution : test | distribution_expr;
distribution_expr    : distribution '(' arglist ')';
distribution         : UNIFORM | NORMAL | CHOICE | SEQUENCE | LOG_UNIFORM;

/* Dynamic behavior statements */
behavior_stmt  : 'every' INTEGER? (FRAMES | TIME) behavior_block;
behavior_block : ':' NEWLINE INDENT (expr_stmt | edit_stmt | create_stmt)+ DEDENT;

/* Expression statements */
expr_stmt  : testlist (aug_assign | '=') (testlist | fetch_expr) NEWLINE;
aug_assign : '+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=' | '**=' | '//=';
fetch_expr : 'fetch' test 'in' test (MATCH test)?;

/* Expressions (taken from the Python 3 grammar) */
test        : or_test ('if' or_test 'else' test)?;
test_nocond : or_test;
or_test     : and_test ('or' and_test)*;
and_test    : not_test ('and' not_test)*;
not_test    : 'not' not_test | comparison;
comparison  : expr (comp_op expr)*;
comp_op     : '<' | '>' | '==' | '>=' | '<=' | '!=' | 'in' | 'not' 'in' | 'is' | 'is' 'not';
expr        : xor_expr ('|' xor_expr)*;
xor_expr    : and_expr ('^' and_expr)*;
and_expr    : shift_expr ('&' shift_expr)*;
shift_expr  : arith_expr (('<<' | '>>') arith_expr)*;
arith_expr  : term (('+' | '-') term)*;
term        : factor (('*' | '/' | '%' | '//') factor)*;
factor      : ('+' | '-' | '~') factor | power;
power       : atom_expr ('**' factor)?;
atom_expr   : atom trailer*;

atom:
  '(' testlist_comp? ')'
  | '[' testlist_comp? ']'
  | '[' signed_number '..' signed_number ']'
  | '<' vector_comp? '>'
  | '{' dict_or_set_maker? '}'
  | name
  | signed_number
  | STRING
  | 'none'
  | 'true'
  | 'false'
;

name:
  ID
  | '_'
  | primitives
  | VISIBLE
  | SIZE
  | LOOK_AT
  | UP_AXIS
  | SEMANTICS
  | TEXTURE
  | ORDER
;
primitives    : SHAPES | STEREO? CAMERA | LIGHT | MATERIAL;
signed_number : NUMBER | '-' NUMBER;

testlist_comp : test ( comp_for | (',' test)* ','?);
vector_comp   : expr ( comp_for | (',' expr)* ','?);

trailer       : '[' subscriptlist ']' | '.' name;
arglist       : argument (',' argument)* ','?;
argument      : test comp_for? | test '=' test;
subscriptlist : subscript_ (',' subscript_)* ','?;
subscript_    : test | test? ':' test? sliceop?;
sliceop       : ':' test?;

exprlist : expr (',' expr)* ','?;
testlist : test (',' test)* ','?;
dict_or_set_maker:
  test ':' test (comp_for | (',' test ':' test)* ','?)
  | test (comp_for | (',' test)* ','?)
;

comp_iter : comp_for | comp_if;
comp_for  : 'for' exprlist 'in' or_test comp_iter?;
comp_if   : 'if' test_nocond comp_iter?;
