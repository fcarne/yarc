parser grammar YarcParser;

options {
  tokenVocab = YarcLexer;
  language = Python3;
  output = template;
  superClass = YarcParserBase;
}

@header {
from yarc.dsl.v3.handler.handler_factory import HandlerFactory

if __name__ is not None and "." in __name__:
    from .YarcParserBase import YarcParserBase
else:
    from YarcParserBase import YarcParserBase
}

scenario : declaration NEWLINE* settings? stage? writers? 
  -> scenario(name={$declaration.scenario_name}, settings={$settings.st}, stage={$stage.st}, writers={$writers.st})
; // Starting rule

declaration returns [scenario_name] : SCENARIO ID (COLON name)? NEWLINE 
  {$scenario_name=$ID.text} 
  {self.handler = HandlerFactory.get_handler($name.text, self)};
  
settings    : SETTINGS COLON NEWLINE INDENT sets+=setting+ DEDENT -> settings(setting_list={$sets});
stage       : STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st};
writers     : WRITERS COLON NEWLINE INDENT stmts_+=(expr_stmt | writer)+ DEDENT -> writers(stmts={$stmts_});

setting        : ID ASSIGN test NEWLINE -> setting(setting={$ID.text}, value={$test.st}); // Add special settings handling
stmts          : stmts_+=(open_stmt)? stmts_+=(aug_expr_stmt | edit_stmt | behavior_stmt)+ -> stage(stmts={$stmts_});
writer         : ID COLON NEWLINE INDENT writer_params+=writer_param+ DEDENT -> writer(writer_id={$ID.text}, writer_params={$writer_params}, rps={["rp"]}); // Get render products from handler
writer_param   : ID ASSIGN test NEWLINE -> writer_param(param={$ID.text}, value={$test.st});

/* Statements */
/* Scene object creation and modifcation statements */
open_stmt : OPEN test NEWLINE -> open_stmt(path={$test.st});
edit_stmt : EDIT (TIMELINE COLON NEWLINE INDENT (params+=name values+=test NEWLINE)+ DEDENT -> edit_timeline(params={$params}, values={$values}) 
                 | name edit_block);

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

attr          : attr_=(core_attr | simple_attr | compound_attr) -> {$attr_.st};
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
  ) NEWLINE ;

inner_behavior_stmt  : behavior_expr inner_behavior_block;
inner_behavior_block : COLON NEWLINE INDENT attr+ DEDENT;

/* Dynamic behavior statements */
behavior_stmt  : behavior_expr behavior_block;
behavior_expr  : EVERY test? (FRAMES | TIME);
behavior_block : COLON NEWLINE INDENT (aug_expr_stmt | edit_stmt)+ DEDENT;

/* Expression statements */
expr_stmt : assignable=testlist op=(AUG_ASSIGN | ASSIGN) value=(testlist | fetch_expr) NEWLINE 
  -> expr_stmt(assignable={$assignable.st}, op={$op.text}, value={$value.st});

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

fetch_expr : FETCH ext=test FROM path=test (MATCH filter=test)? (LIMIT limit=test)? RECURSIVE?
  -> fetch_expr(ext={$ext.st}, path={$path.st}, filter={$filter.st}, limit={$limit.st}, recursive={$RECURSIVE});

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
  | STRING -> {$STRING.text} // Add string expansion
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

testlist_comp : exprs+=test ( comp_for -> list_comp(expr={$exprs[0]}, for={$comp_for.st})
                     | (COMMA exprs+=test)* -> test_list(exprs={$exprs})
                     | RANGE to=test (STEP step=test)? -> range(from={$exprs[0]}, to={$to.st}, step={$step.st})
              );

vector_comp   : x=expr COMMA y=expr COMMA z=expr -> vector_comp(x={$x.st}, y={$y.st}, z={$z.st});
/*( comp_for | (COMMA expr)*)*/
trailer       : LBRACK subscriptlist RBRACK -> index(index={$subscriptlist.st}) 
              | DOT name -> dot_attr(attr={$name.st});
arglist       : args+=argument (COMMA args+=argument)* -> arg_list(args={$args});
argument      : kw_or_arg=test (ASSIGN arg=test)? -> arg(kw_or_arg={$kw_or_arg.st}, arg={$arg.st});
subscriptlist : subs+=subscript_ (COMMA subs+=subscript_)* -> subscript_list(subs={$subs});
subscript_    : from_=test (COLON to=(test)? step=(sliceop)?)? -> subscript(from={$from_.st}, colon={$COLON}, to={$to.st}, step={$step.st})
              | COLON to=(test)? step=(sliceop)?  -> subscript(colon={$COLON}, to={$to.st}, step={$step.st});
sliceop       : COLON test? -> subscipt_step(step={$test.st});

exprlist : exprs+=expr (COMMA exprs+=expr)* -> test_list(exprs={$exprs});
testlist : exprs+=test (COMMA exprs+=test)* -> test_list(exprs={$exprs});
dict_or_set_maker:
  exprs+=test ( COLON values+=test (for_=comp_for -> dict_comp(key={$exprs[0]}, value={$values[0]}, for={$for_.st})
                                   | (COMMA exprs+=test COLON values+=test)*) -> key_value_list(keys={$exprs}, values={$values})
              | (for_=comp_for -> list_comp(expr={$exprs[0]}, for={$for_.st})   
                | (COMMA exprs+=test)*)  -> test_list(exprs={$exprs})
              )
;

comp_iter : comp=(comp_for | comp_if) -> {$comp.st};
comp_for  : FOR exprlist IN or_test comp_iter? -> comp_for(exprs={$exprlist.st}, seq={$or_test.st}, comp_iter={$comp_iter.st});
comp_if   : IF test_nocond comp_iter? -> comp_if(cond={$test_nocond.st}, comp_iter={$comp_iter.st});
