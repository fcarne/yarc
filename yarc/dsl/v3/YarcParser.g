parser grammar YarcParser;

options {
  tokenVocab = YarcLexer;
  language = Python3;
  output = template;
}

scenario : declaration NEWLINE* settings? stage? writers? 
  -> scenario(name={$declaration.scenario_name}, settings={$settings.st}, stage={$stage.st}, writers={$writers.st})
; // Starting rule

declaration returns [scenario_name] : SCENARIO ID (COLON name)? NEWLINE {$scenario_name=$ID.text};
settings    : SETTINGS COLON NEWLINE INDENT sets+=setting+ DEDENT -> settings(setting_list={$sets});
stage       : STAGE COLON NEWLINE INDENT stmts DEDENT;
writers     : WRITERS COLON NEWLINE INDENT (expr_stmt | writer)+ DEDENT;

setting        : ID ASSIGN test NEWLINE -> setting(setting={$ID.text}, value={$test.st}); // Add special settings handling
stmts          : open_stmt? (aug_expr_stmt | edit_stmt | behavior_stmt)+;
writer         : ID COLON NEWLINE INDENT writer_setting+ DEDENT;
writer_setting : ID ASSIGN test NEWLINE;
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
test        : expr_=or_test (IF cond=or_test ELSE else_expr=test)? 
            -> test(expr={$expr_.st}, cond={$cond.st}, else_expr={$else_expr.st}) ;
test_nocond : or_test -> test(expr={$or_test.st});
or_test     : exprs+=and_test (OR exprs+=and_test)* -> or_test(exprs={$exprs});
and_test    : exprs+=not_test (AND exprs+=not_test)* -> and_test(exprs={$exprs});
not_test    : NOT expr_=not_test  -> not_test(expr={$expr_.st})
            | comparison -> {$comparison.st};
comparison  : exprs+=expr (comp_op exprs+=expr)* -> comparison(exprs={$exprs}, op={$comp_op.text});
comp_op     : LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT ;
expr        : exprs+=xor_expr (BIT_OR exprs+=xor_expr)* -> expr(exprs={$exprs});
xor_expr    : exprs+=and_expr (XOR exprs+=and_expr)* -> xor_expr(exprs={$exprs});
and_expr    : exprs+=shift_expr (BIT_AND exprs+=shift_expr)* -> and_expr(exprs={$exprs});
shift_expr  : exprs+=arith_expr (op=(LSHIFT | RSHIFT) exprs+=arith_expr)* -> shift_expr(exprs={$exprs}, op={$op});
arith_expr  : terms+=term (op=(PLUS | MINUS) terms+=term)* -> arith_expr(terms={$terms}, op={$op});
term        : factors+=factor (op=(MUL | DIV | MOD | IDIV) factors+=factor)* -> term(factors={$factors}, op={$op});
factor      : prefix=(PLUS | MINUS | BIT_NOT) factor_=factor -> prefix_factor(factor={$factor_.st}, prefix={$prefix})
            | power -> {$power.st};
power       : atom_expr (POWER factor)? -> power(atom={$atom_expr.st}, factor={$factor.st});
atom_expr   : atom (trailers+=trailer)* -> atom_expr(atom={$atom.st}, trailers={$trailers});
atom:
  (LPAREN test_=test RPAREN -> parenthesized_expr(expr={$test_.st})
  | LBRACK testlist_comp? RBRACK -> list(list_comp={$testlist_comp.st})
  | LT vector_comp? GT -> vector(values={$vector_comp.st})
  | LBRACE dict_or_set_maker? RBRACE -> dict(dict_comp={$dict_or_set_maker.st})
  | LEN LPAREN test_=test RPAREN -> len(value={$test_.st})
  | name -> {$name.st}
  | SETTING_ID -> setting_id(id={$SETTING_ID.text}) 
  | DISTRIBUTION LPAREN arglist RPAREN -> distribution(name={$DISTRIBUTION.text}, arglist={$arglist.st})
  | INTEGER -> {$INTEGER.text}
  | FLOAT_NUMBER -> {$FLOAT_NUMBER.text}
  | STRING -> {$STRING.text}
  | NONE -> null()
  | TRUE -> true()
  | FALSE -> false()
  )
;

name:
  ID -> {$ID.text}
  | UNDERSCORE -> {$UNDERSCORE.text}
  /*| primitives
  | VISIBLE
  | SIZE
  | LOOK_AT
  | UP_AXIS
  | SEMANTICS
  | TEXTURE
  | ORDER  */
;

testlist_comp : test ( comp_for | (COMMA test)* | RANGE test (STEP test)? );
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
