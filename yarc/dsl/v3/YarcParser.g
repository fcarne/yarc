parser grammar YarcParser;

options {
  tokenVocab = YarcLexer;
  language = Python3;
  output = template;
}

scenario : declaration NEWLINE* settings? stage? writers?; // Starting rule

declaration : SCENARIO name (COLON name)? NEWLINE;
settings    : SETTINGS COLON NEWLINE INDENT option+ DEDENT;
stage       : STAGE COLON NEWLINE INDENT stmts DEDENT;
writers     : WRITERS COLON NEWLINE INDENT (expr_stmt | writer)+ DEDENT;

option : ID ASSIGN test NEWLINE;
stmts  : open_stmt? (aug_expr_stmt | edit_stmt | behavior_stmt)+;
writer : ID COLON NEWLINE INDENT option+ DEDENT;

/* Statements */
/* Scene object creation and modifcation statements */
open_stmt : OPEN test NEWLINE;
edit_stmt : EDIT (TIMELINE | name) edit_block;

create_expr:
  CREATE test? (
    (STEREO? CAMERA | shapes | light_type LIGHT | FROM test) (edit_block | NEWLINE)
    | MATERIAL (simple_block)
  )
;

shapes     : SHAPES | SHAPES_OR_LIGHTS;
light_type : LIGHT_TYPE | SHAPES_OR_LIGHTS;

instantiate_expr : INSTANTIATE (test)? FROM test (edit_block | NEWLINE);
group_expr       : GROUP LBRACK name (COMMA name)* RBRACK (edit_block | NEWLINE);
get_expr         : GET ((CAMERA | LIGHT | MATERIAL | name) AT)? test (simple_block | NEWLINE);

edit_block   : COLON NEWLINE INDENT (attr | inner_behavior_stmt)+ DEDENT;
simple_block : COLON NEWLINE INDENT simple_attr+ DEDENT;

attr          : core_attr | simple_attr | compound_attr;
simple_attr   : name (COLON name)? test? NEWLINE;

compound_attr : (SCATTER ON name | ROT_AROUND name | PHYSICS) (simple_block | NEWLINE);

core_attr: // Special modifiers that must be treated in a specific way
  (
    TRANSLATE AXIS? TO test
    | CAM_TRANSLATE TO test
    | ROTATE AXIS? test ORDER?
    | SCALE test
    | LOOK_AT test
    | UP_AXIS test
    | SIZE test
    | SEMANTICS test
    | VISIBLE test
  ) NEWLINE
;

inner_behavior_stmt  : behavior_expr inner_behavior_block;
inner_behavior_block : COLON NEWLINE INDENT attr+ DEDENT;

/* Dynamic behavior statements */
behavior_stmt  : behavior_expr behavior_block;
behavior_expr  : EVERY test? (FRAMES | TIME);
behavior_block : COLON NEWLINE INDENT (aug_expr_stmt | edit_stmt)+ DEDENT;

/* Expression statements */
expr_stmt : testlist (AUG_ASSIGN | ASSIGN) (testlist | fetch_expr) NEWLINE;

aug_expr_stmt: (
    testlist (
      AUG_ASSIGN (testlist | fetch_expr)? NEWLINE
      | ASSIGN (
        (testlist | fetch_expr) NEWLINE
        | create_expr | instantiate_expr | get_expr | group_expr
      )
    )
  )
  | create_expr | instantiate_expr | get_expr | group_expr
;

fetch_expr : FETCH test FROM test (MATCH test)? (LIMIT test)? RECURSIVE?;

/* Expressions (taken from the Python 3 grammar) */
test        : or_test (IF or_test ELSE test)?;
test_nocond : or_test;
or_test     : and_test (OR and_test)*;
and_test    : not_test (AND not_test)*;
not_test    : NOT not_test | comparison;
comparison  : expr (comp_op expr)*;
comp_op     : LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT;
expr        : xor_expr (BIT_OR xor_expr)*;
xor_expr    : and_expr (XOR and_expr)*;
and_expr    : shift_expr (BIT_AND shift_expr)*;
shift_expr  : arith_expr ((LSHIFT | RSHIFT) arith_expr)*;
arith_expr  : term ((PLUS | MINUS) term)*;
term        : factor ((MUL | DIV | MOD | IDIV) factor)*;
factor      : (PLUS | MINUS | BIT_NOT) factor | power;
power       : atom_expr (POWER factor)?;
atom_expr   : atom (: trailer)*;
atom:
  LPAREN test RPAREN
  | LBRACK (testlist_comp? | (MINUS? INTEGER) RANGE (MINUS? INTEGER)) RBRACK
  | LT vector_comp? GT
  | LBRACE dict_or_set_maker? RBRACE
  | LEN LPAREN test RPAREN
  | name | SETTING_ID | distribution_expr
  | INTEGER | FLOAT_NUMBER | STRING | NONE | TRUE | FALSE
;

name:
  ID
  | UNDERSCORE
  /*| primitives
  | VISIBLE
  | SIZE
  | LOOK_AT
  | UP_AXIS
  | SEMANTICS
  | TEXTURE
  | ORDER  */
;

distribution_expr : DISTRIBUTION LPAREN arglist RPAREN;

testlist_comp : test ( comp_for | (COMMA test)*);
vector_comp   : expr COMMA expr COMMA expr /*( comp_for | (COMMA expr)*)*/;

trailer       : LBRACK subscriptlist RBRACK | DOT (name  | AXIS);
arglist       : argument (COMMA argument)*;
argument      : test (comp_for | ASSIGN test)?;
subscriptlist : subscript_ (COMMA subscript_)*;
subscript_    : test (COLON (test)? (sliceop)?)? | COLON (test)? (sliceop)?;
sliceop       : COLON test?;

exprlist : expr (COMMA expr)*;
testlist : test (COMMA test)*;
dict_or_set_maker:
  test ( COLON test (comp_for | (COMMA test COLON test)*)
       | (comp_for | (COMMA test)*) )
;

comp_iter : comp_for | comp_if;
comp_for  : FOR exprlist IN or_test comp_iter?;
comp_if   : IF test_nocond comp_iter?;
