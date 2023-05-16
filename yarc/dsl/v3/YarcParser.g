parser grammar YarcParser;

options {
  tokenVocab = YarcLexer;
  language = Python3;
  output = template;
  superClass = YarcParserBase;
}

@header {
from yarc.dsl.v3.handler.handler_factory import HandlerFactory
from yarc.dsl.v3.handler.handler import Attribute, Parameter

if __name__ is not None and "." in __name__:
    from .YarcParserBase import YarcParserBase
else:
    from YarcParserBase import YarcParserBase
}

scenario : (before+=code_snippet | NEWLINE)* declaration (before+=code_snippet | NEWLINE)* settings? stage writers? after+=(code_snippet)* 
  -> scenario(name={$declaration.scenario_name}, 
              before_snippets={$before}, 
              settings={$settings.st}, 
              stage={$stage.st}, 
              writers={$writers.st},
              after_snippets={$after}); // Starting rule

code_snippet :  SNIPPET {code=self.handler.parse_snippet($SNIPPET)} -> snippet(code={code});

declaration returns [scenario_name] : SCENARIO ID (COLON name)? NEWLINE 
  {$scenario_name=$ID.text} 
  {self.handler = HandlerFactory.get_handler($name.text, self)};
  
settings    : SETTINGS COLON NEWLINE INDENT stmts_+=(setting | code_snippet)+ DEDENT -> settings(settings={self.handler.settings_to_str()}, stmts={$stmts_});
stage       : STAGE COLON NEWLINE INDENT stmts DEDENT -> {$stmts.st};
writers     : WRITERS COLON NEWLINE INDENT stmts_+=(expr_stmt | code_snippet | writer)+ DEDENT -> writers(stmts={$stmts_});

setting        : ID ASSIGN test NEWLINE ( {self.handler.is_special_setting($ID.text)}? -> {self.handler.special_setting_to_str($ID.text, $test.st)}
                                        | -> setting(setting={$ID.text}, value={$test.st}) 
                                        ) {self.handler.add_setting(setting=$ID.text, value=$test.st)}; 
stmts          : stmts_+=(open_stmt)? stmts_+=(aug_expr_stmt | code_snippet | edit_stmt | behavior_stmt)+ -> stage(stmts={$stmts_});
writer @init {params = []}       
  : ID COLON NEWLINE INDENT (writer_param {params.append($writer_param.param)})+ DEDENT {self.handler.check_writer_params(params)} 
  -> writer(writer_id={$ID.text}, params={params});
writer_param returns [param]: ID ASSIGN test NEWLINE {$param = Parameter($ID.text,$test.st) };

/* Statements */
/* Scene object creation and modifcation statements */
open_stmt : OPEN test NEWLINE -> open_stmt(path={$test.st});
edit_stmt : EDIT (TIMELINE COLON NEWLINE INDENT (params+=name values+=test NEWLINE)+ DEDENT -> edit_timeline(params={$params}, values={$values}) 
                 | id=name edit_block[$id.st] -> edit_stmt(id={$id.st}, stmts={self.handler.get_attrs("edit", $edit_block.attrs)}, behaviors={self.handler.get_behaviors($edit_block.attrs)})
                 );

create_expr[id]:
  CREATE count=test? (
    prim=(SHAPE | LIGHT) (attrs=edit_block[$id] | NEWLINE) 
      -> create_prim(id={$id}, 
                     prim={self.handler.map($prim)}, 
                     params={self.handler.get_params($prim, $attrs.attrs, $count.st)}, 
                     stmts={self.handler.get_attrs($prim, $attrs.attrs)}, 
                     behaviors={self.handler.get_behaviors($attrs.attrs)})
    | prim=(STEREO? CAMERA) (attrs=edit_block[$id] | NEWLINE) 
      -> create_camera(id={$id}, 
                     prim={self.handler.map($prim)}, 
                     params={self.handler.get_params($prim, $attrs.attrs, $count.st)}, 
                     stmts={self.handler.get_attrs($prim, $attrs.attrs)}, 
                     behaviors={self.handler.get_behaviors($attrs.attrs)})
    | FROM file=test (attrs=edit_block[$id] | NEWLINE)
      -> create_from(id={$id},
                     file={$file.st}, 
                     params={self.handler.get_params("from_file", $attrs.attrs, $count.st)}, 
                     stmts={self.handler.get_attrs("from_file", $attrs.attrs)}, 
                     behaviors={self.handler.get_behaviors($attrs.attrs)})
    | MATERIAL (attrs=simple_block | NEWLINE) 
      -> create_material(id={$id}, 
                         params={self.handler.get_params("material", $attrs.attrs, $count.st)})
  )
;

instantiate_expr[id] : INSTANTIATE count=(test)? FROM file=test (edit_block[$id] | NEWLINE)
  -> instantiate_expr(id={$id}, 
                      file={$file.st}, 
                      params={self.handler.get_params("instantiate", $edit_block.attrs, $count.st)}, 
                      stmts={self.handler.get_attrs("instantiate", $edit_block.attrs)}, 
                      behaviors={self.handler.get_behaviors($edit_block.attrs)}) ;
group_expr[id]       : GROUP LBRACK names+=name (COMMA names+=name)* RBRACK (edit_block[$id] | NEWLINE)
  -> group_expr(id={$id},
                names={$names},
                params={self.handler.get_params("group", $edit_block.attrs)}, 
                stmts={self.handler.get_attrs("group", $edit_block.attrs)},
                behaviors={self.handler.get_behaviors($edit_block.attrs)}) ;
get_expr[id]         : GET (filter=(CAMERA | LIGHT | MATERIAL | name) AT)? path=test (simple_block | NEWLINE)
  -> get_expr(id={$id}, 
              filter={$filter.st},
              path={$path.st},
              params={self.handler.get_params("get", $simple_block.attrs)});

edit_block[id] returns [attrs] 
@init {$attrs = []} 
  : COLON NEWLINE INDENT (stmt_=(attr | inner_behavior_stmt[$id]) {$attrs.append($stmt_.attr)})+ DEDENT;
simple_block returns [attrs]
@init {$attrs = []} 
  : COLON NEWLINE INDENT (simple_attr {$attrs.append($simple_attr.attr)})+ DEDENT;

attr returns [attr] : a=(core_attr | simple_attr | compound_attr) {$attr=$a.attr} -> {$a.st};
simple_attr returns [attr]
@after {$attr=Attribute($name_.st, $value.st, retval.st)}   
  : name_=name (COLON type=name)? value=test NEWLINE 
  -> simple_attr(name={$name_.st}, type={$type.st}, value={$value.st}) ;

compound_attr returns [attr] 
@after {$attr=Attribute($name_.text, "", retval.st)}
  : ( name_=SCATTER ON surface=name (attrs=simple_block | NEWLINE) 
      -> scatter_expr(scatter_type={self.handler.map($name_)}, 
                      surface={$surface.st}, 
                      params={self.handler.get_params($name_, $attrs.attrs)}) 
    | name_=ROT_AROUND center=name (attrs=simple_block | NEWLINE)
      -> rot_around_expr(center={$center.st}, 
                         params={self.handler.get_params($name_, $attrs.attrs)})
    | name_=PHYSICS (attrs=simple_block | NEWLINE)
      -> physics_expr(physics_attr={self.handler.map($name_)},
                      params={self.handler.get_params($name_, $attrs.attrs)})
    | name_=MOVE_TO_CAM camera=name (attrs=simple_block | NEWLINE)
      -> move_to_camera_expr(camera={$camera.st},
                             params={self.handler.get_params($name_, $attrs.attrs)})
    );

core_attr returns [attr] // Special modifiers that must be treated in a specific way
@after {$attr=Attribute(name, $value.st, retval.st)}
  : ( TRANSLATE axis=AXIS? TO value=test {name = self.handler.map($TRANSLATE, $axis)} -> translate_expr(type={name}, value={$value.st})
    | ROTATE axis=AXIS? value=test ORDER? {name = self.handler.map($ROTATE, $axis)} -> rotate_expr(type={name}, value={$value.st})
    | SCALE value=test {name = self.handler.map($SCALE)} -> scale_expr(value={$value.st})
    | LOOK_AT value=test {name = self.handler.map($LOOK_AT)} -> look_at_expr(value={$value.st})
    | UP_AXIS value=test {name = self.handler.map($UP_AXIS)} -> look_at_up_axis_expr(value={$value.st})
    | SIZE value=test {name = self.handler.map($SIZE)} -> size_expr(value={$value.st})
    | SEMANTICS value=test {name = self.handler.map($SEMANTICS)} -> semantics_expr(value={$value.st})
    | VISIBLE value=test {name = self.handler.map($VISIBLE)} -> visible_expr(value={$value.st})
    | MATERIAL value=test {name = self.handler.map($MATERIAL)} -> material_expr(value={$value.st})
  ) NEWLINE ;

inner_behavior_stmt[id] returns [attr]
@after {$attr=Attribute("behavior", "", retval.st)}  
  : behavior_expr inner_behavior_block -> inner_behavior_stmt(behavior={$behavior_expr.st}, id={$id}, block={$inner_behavior_block.st});
inner_behavior_block : COLON NEWLINE INDENT stmts_+=attr+ DEDENT -> behavior_block(stmts={$stmts_});

/* Dynamic behavior statements */
behavior_stmt  : behavior_expr behavior_block -> behavior_stmt(behavior={$behavior_expr.st}, block={$behavior_block.st});
behavior_expr  : EVERY interval=test? type=(FRAMES | TIME) -> behavior_expr(interval={$interval.st}, is_frame={self.handler.is_frame($type)});
behavior_block : COLON NEWLINE INDENT stmts_+=(aug_expr_stmt | code_snippet | edit_stmt)+ DEDENT -> behavior_block(stmts={$stmts_});

/* Expression statements */
expr_stmt : assignable=testlist op=(AUG_ASSIGN | ASSIGN) value=(testlist | fetch_expr) NEWLINE 
  -> expr_stmt(assignable={$assignable.st}, op={$op.text}, value={$value.st}) ;

aug_expr_stmt: (
    id=testlist (
      op=AUG_ASSIGN value=(testlist | fetch_expr) NEWLINE -> expr_stmt(assignable={$id.st}, op={$op.text}, value={$value.st}) 
      | op=ASSIGN (
        value=(testlist | fetch_expr) NEWLINE -> expr_stmt(assignable={$id.st}, op={$op.text}, value={$value.st}) 
        | value=(model_expr[$id.st]) -> {$value.st}
      )
    ) 
  ) 
  | {id = self.handler.get_random_uid()} model_expr[id] -> {$model_expr.st}
;

model_expr[id]: expr_=(create_expr[$id] | instantiate_expr[$id] | get_expr[$id] | group_expr[$id]) -> {expr_.st};

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
comparison  : exprs+=expr (ops+=comp_op exprs+=expr)* -> comparison(exprs={$exprs}, ops={$ops});
comp_op     : op=(LT | GT | EQUALS | GT_EQ | LT_EQ | NOT_EQ | IN | NOT IN | IS | IS NOT) -> {$op};
expr        : exprs+=xor_expr (BIT_OR exprs+=xor_expr)* -> expr(exprs={$exprs});
xor_expr    : exprs+=and_expr (XOR exprs+=and_expr)* -> xor_expr(exprs={$exprs});
and_expr    : exprs+=shift_expr (BIT_AND exprs+=shift_expr)* -> and_expr(exprs={$exprs});
shift_expr  : exprs+=arith_expr (ops+=(LSHIFT | RSHIFT) exprs+=arith_expr)* -> shift_expr(exprs={$exprs}, ops={$ops});
arith_expr  : terms+=term (ops+=(PLUS | MINUS) terms+=term)* -> arith_expr(terms={$terms}, ops={$ops});
term        : factors+=factor (ops+=(MUL | DIV | MOD | IDIV) factors+=factor)* -> term(factors={$factors}, ops={$ops});
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
  | distribution -> {$distribution.st}
  | INTEGER -> {$INTEGER.text}
  | FLOAT_NUMBER -> {$FLOAT_NUMBER.text}
  | STRING -> {self.handler.expand_string($STRING)} // Add string expansion
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

distribution : DISTRIBUTION LPAREN args=arglist RPAREN -> distribution(name={self.handler.map($DISTRIBUTION)}, arglist={$args.st})
               | COMBINE LPAREN args=arglist RPAREN ->  combined_distribution(distrs={$args.st});

testlist_comp :  exprs+=test ( comp_for -> list_comp(expr={$exprs[0]}, for={$comp_for.st})
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
