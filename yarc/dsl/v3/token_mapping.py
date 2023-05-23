from yarc.dsl.v3 import YarcLexer

TOKEN_TYPE_TO_TEXT = {
    YarcLexer.SCENARIO: "scenario",
    YarcLexer.SETTINGS: "settings",
    YarcLexer.STAGE: "stage",
    YarcLexer.WRITERS: "writers",
    YarcLexer.SHAPE: "Shape",
    YarcLexer.CAMERA: "Camera",
    YarcLexer.LIGHT: "Light",
    YarcLexer.STEREO: "Stereo",
    YarcLexer.MATERIAL: "Material",
    YarcLexer.TIMELINE: "Timeline",
    YarcLexer.OPEN: "open",
    YarcLexer.CREATE: "create",
    YarcLexer.GROUP: "group",
    YarcLexer.INSTANTIATE: "instantiate",
    YarcLexer.GET: "get",
    YarcLexer.EDIT: "edit",
    YarcLexer.FETCH: "fetch",
    YarcLexer.MATCH: "match",
    YarcLexer.LIMIT: "limit",
    YarcLexer.RECURSIVE: "recursive",
    YarcLexer.TRANSLATE: "translate",
    YarcLexer.ROTATE: "rotate",
    YarcLexer.SCALE: "scale",
    YarcLexer.SEMANTICS: "semantics",
    YarcLexer.VISIBLE: "visible",
    YarcLexer.SIZE: "size",
    YarcLexer.LOOK_AT: "look_at",
    YarcLexer.UP_AXIS: "up_axis",
    YarcLexer.PIVOT: "pivot",
    YarcLexer.MATERIAL_: "material",
    YarcLexer.AXIS: "axis",
    YarcLexer.ORDER: "order",
    YarcLexer.SCATTER: "scatter",
    YarcLexer.ROT_AROUND: "rotate_around",
    YarcLexer.MOVE_TO_CAM: "move_to_camera",
    YarcLexer.PHYSICS: "physics",
    YarcLexer.EVERY: "every",
    YarcLexer.FRAMES: "frames",
    YarcLexer.TIME: "time",
    YarcLexer.DISTRIBUTION: "distribution",
    YarcLexer.COMBINE: "combine",
    YarcLexer.SNIPPET: "snippet",
    YarcLexer.TO: "to",
    YarcLexer.ON: "on",
    YarcLexer.AT: "at",
    YarcLexer.AND: "and",
    YarcLexer.ELSE: "else",
    YarcLexer.FALSE: "false",
    YarcLexer.FOR: "for",
    YarcLexer.FROM: "from",
    YarcLexer.IF: "if",
    YarcLexer.IN: "in",
    YarcLexer.IS: "is",
    YarcLexer.LEN: "len",
    YarcLexer.NONE: "none",
    YarcLexer.NOT: "not",
    YarcLexer.OR: "or",
    YarcLexer.STEP: "step",
    YarcLexer.TRUE: "true",
    YarcLexer.UNDERSCORE: "_",
    YarcLexer.DOT: ".",
    YarcLexer.RANGE: "..",
    YarcLexer.ELLIPSIS: "...",
    YarcLexer.COMMA: ",",
    YarcLexer.COLON: ":",
    YarcLexer.SEMI: ";",
    YarcLexer.ASSIGN: "=",
    YarcLexer.BIT_OR: "|",
    YarcLexer.XOR: "^",
    YarcLexer.BIT_AND: "&",
    YarcLexer.BIT_NOT: "~",
    YarcLexer.LSHIFT: "<<",
    YarcLexer.RSHIFT: ">>",
    YarcLexer.PLUS: "+",
    YarcLexer.MINUS: "-",
    YarcLexer.MUL: "*",
    YarcLexer.DIV: "/",
    YarcLexer.MOD: "%",
    YarcLexer.IDIV: "//",
    YarcLexer.POWER: "**",
    YarcLexer.LPAREN: "(",
    YarcLexer.RPAREN: ")",
    YarcLexer.LBRACK: "[",
    YarcLexer.RBRACK: "]",
    YarcLexer.LBRACE: "{",
    YarcLexer.RBRACE: "}",
    YarcLexer.LT: "<",
    YarcLexer.GT: ">",
    YarcLexer.EQUALS: "==",
    YarcLexer.GT_EQ: ">=",
    YarcLexer.LT_EQ: "<=",
    YarcLexer.NOT_EQ: "!=",
    YarcLexer.AUG_ASSIGN: "+=",
}
