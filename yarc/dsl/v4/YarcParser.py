# Generated from c:\Users\feder\Desktop\University\Magistrale\Secondo_Anno\1_Linguaggi\Progetto\yarc\yarc\dsl\v4\YarcParser.g4 by ANTLR 4.9.2
import sys
from io import StringIO

from antlr4 import (
    DFA,
    ATNDeserializer,
    NoViableAltException,
    Parser,
    ParserATNSimulator,
    ParserRuleContext,
    PredictionContextCache,
    RecognitionException,
    Token,
    TokenStream,
)

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3{")
        buf.write("\u02fd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write('\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%\4&\t')
        buf.write("&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\7")
        buf.write("\2\u0087\n\2\f\2\16\2\u008a\13\2\3\2\5\2\u008d\n\2\3\2")
        buf.write("\5\2\u0090\n\2\3\2\5\2\u0093\n\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3\u009b\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\6\4\u00a4")
        buf.write("\n\4\r\4\16\4\u00a5\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\6\6\u00b7\n\6\r\6\16\6\u00b8")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\5\b\u00c3\n\b\3\b\3\b")
        buf.write("\3\b\6\b\u00c8\n\b\r\b\16\b\u00c9\3\t\3\t\3\t\3\t\3\t")
        buf.write("\6\t\u00d1\n\t\r\t\16\t\u00d2\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\5\13\u00de\n\13\3\13\3\13\3\f\3\f\5\f")
        buf.write("\u00e4\n\f\3\f\5\f\u00e7\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00f0\n\f\3\f\3\f\5\f\u00f4\n\f\3\f\3\f\5\f\u00f8")
        buf.write("\n\f\3\r\3\r\3\16\3\16\3\17\3\17\5\17\u0100\n\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u0106\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\7\20\u010d\n\20\f\20\16\20\u0110\13\20\3\20\3\20\3")
        buf.write("\20\5\20\u0115\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u011c")
        buf.write("\n\21\3\21\5\21\u011f\n\21\3\21\3\21\3\21\5\21\u0124\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\6\22\u012b\n\22\r\22\16\22")
        buf.write("\u012c\3\22\3\22\3\23\3\23\3\23\3\23\6\23\u0135\n\23\r")
        buf.write("\23\16\23\u0136\3\23\3\23\3\24\3\24\3\24\5\24\u013e\n")
        buf.write("\24\3\25\3\25\3\25\5\25\u0143\n\25\3\25\5\25\u0146\n\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0150\n")
        buf.write("\26\3\26\3\26\5\26\u0154\n\26\3\27\3\27\5\27\u0158\n\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0161\n\27\3")
        buf.write("\27\3\27\5\27\u0165\n\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0173\n\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\6\31\u017e\n\31")
        buf.write("\r\31\16\31\u017f\3\31\3\31\3\32\3\32\3\32\3\33\3\33\5")
        buf.write("\33\u0189\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\6\34")
        buf.write("\u0192\n\34\r\34\16\34\u0193\3\34\3\34\3\35\3\35\3\35")
        buf.write("\5\35\u019b\n\35\3\35\3\35\5\35\u019f\n\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u01a7\n\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u01ae\n\36\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u01b6\n\36\5\36\u01b8\n\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u01be\n\36\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u01c6\n")
        buf.write("\37\3\37\3\37\5\37\u01ca\n\37\3\37\5\37\u01cd\n\37\3 ")
        buf.write('\3 \3!\3!\3!\3!\3!\3!\5!\u01d7\n!\3"\3"\3#\3#\3#\7#')
        buf.write("\u01de\n#\f#\16#\u01e1\13#\3$\3$\3$\7$\u01e6\n$\f$\16")
        buf.write("$\u01e9\13$\3%\3%\3%\5%\u01ee\n%\3&\3&\3&\3&\7&\u01f4")
        buf.write("\n&\f&\16&\u01f7\13&\3'\3'\3'\3'\3'\3'\3'\3'\3")
        buf.write("'\3'\3'\3'\5'\u0205\n'\3(\3(\3(\7(\u020a\n(\f(\16")
        buf.write("(\u020d\13(\3)\3)\3)\7)\u0212\n)\f)\16)\u0215\13)\3*\3")
        buf.write("*\3*\7*\u021a\n*\f*\16*\u021d\13*\3+\3+\3+\7+\u0222\n")
        buf.write("+\f+\16+\u0225\13+\3,\3,\3,\7,\u022a\n,\f,\16,\u022d\13")
        buf.write(",\3-\3-\3-\7-\u0232\n-\f-\16-\u0235\13-\3.\3.\3.\5.\u023a")
        buf.write("\n.\3/\3/\3/\5/\u023f\n/\3\60\3\60\7\60\u0243\n\60\f\60")
        buf.write("\16\60\u0246\13\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write("\u024e\n\61\3\61\5\61\u0251\n\61\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u0257\n\61\3\61\5\61\u025a\n\61\3\61\3\61\3\61\5\61")
        buf.write("\u025f\n\61\3\61\3\61\3\61\5\61\u0264\n\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0270\n\61")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\7\65\u027f\n\65\f\65\16\65\u0282\13\65\5\65")
        buf.write("\u0284\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u0292\n\67\38\38\38\78\u0297\n")
        buf.write("8\f8\168\u029a\138\39\39\39\39\59\u02a0\n9\3:\3:\3:\7")
        buf.write(":\u02a5\n:\f:\16:\u02a8\13:\3;\3;\3;\5;\u02ad\n;\3;\5")
        buf.write(";\u02b0\n;\5;\u02b2\n;\3;\3;\5;\u02b6\n;\3;\5;\u02b9\n")
        buf.write(";\5;\u02bb\n;\3<\3<\5<\u02bf\n<\3=\3=\3=\7=\u02c4\n=\f")
        buf.write("=\16=\u02c7\13=\3>\3>\3>\7>\u02cc\n>\f>\16>\u02cf\13>")
        buf.write("\3?\3?\3?\3?\3?\3?\3?\3?\3?\7?\u02da\n?\f?\16?\u02dd\13")
        buf.write("?\5?\u02df\n?\3?\3?\3?\7?\u02e4\n?\f?\16?\u02e7\13?\5")
        buf.write("?\u02e9\n?\5?\u02eb\n?\3@\3@\5@\u02ef\n@\3A\3A\3A\3A\3")
        buf.write("A\5A\u02f6\nA\3B\3B\3B\5B\u02fb\nB\3B\2\2C\2\4\6\b\n\f")
        buf.write('\16\20\22\24\26\30\32\34\36 "$&(*,.\60\62\64\668:<>@')
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\2\f\3\2\t")
        buf.write("\n\4\2\n\n\r\r\3\2*+\3\2do\3\2OP\3\2QR\3\2SV\4\2NNQR\4")
        buf.write("\2CCpp\3\2,\60\2\u0344\2\u0084\3\2\2\2\4\u0096\3\2\2\2")
        buf.write("\6\u009e\3\2\2\2\b\u00a9\3\2\2\2\n\u00b0\3\2\2\2\f\u00bc")
        buf.write("\3\2\2\2\16\u00c2\3\2\2\2\20\u00cb\3\2\2\2\22\u00d6\3")
        buf.write("\2\2\2\24\u00da\3\2\2\2\26\u00e1\3\2\2\2\30\u00f9\3\2")
        buf.write("\2\2\32\u00fb\3\2\2\2\34\u00fd\3\2\2\2\36\u0107\3\2\2")
        buf.write('\2 \u0116\3\2\2\2"\u0125\3\2\2\2$\u0130\3\2\2\2&\u013d')
        buf.write("\3\2\2\2(\u013f\3\2\2\2*\u014f\3\2\2\2,\u0172\3\2\2\2")
        buf.write(".\u0176\3\2\2\2\60\u0179\3\2\2\2\62\u0183\3\2\2\2\64\u0186")
        buf.write("\3\2\2\2\66\u018c\3\2\2\28\u0197\3\2\2\2:\u01bd\3\2\2")
        buf.write("\2<\u01bf\3\2\2\2>\u01ce\3\2\2\2@\u01d0\3\2\2\2B\u01d8")
        buf.write("\3\2\2\2D\u01da\3\2\2\2F\u01e2\3\2\2\2H\u01ed\3\2\2\2")
        buf.write("J\u01ef\3\2\2\2L\u0204\3\2\2\2N\u0206\3\2\2\2P\u020e\3")
        buf.write("\2\2\2R\u0216\3\2\2\2T\u021e\3\2\2\2V\u0226\3\2\2\2X\u022e")
        buf.write("\3\2\2\2Z\u0239\3\2\2\2\\\u023b\3\2\2\2^\u0240\3\2\2\2")
        buf.write("`\u026f\3\2\2\2b\u0271\3\2\2\2d\u0273\3\2\2\2f\u0278\3")
        buf.write("\2\2\2h\u027a\3\2\2\2j\u0285\3\2\2\2l\u0291\3\2\2\2n\u0293")
        buf.write("\3\2\2\2p\u029b\3\2\2\2r\u02a1\3\2\2\2t\u02ba\3\2\2\2")
        buf.write("v\u02bc\3\2\2\2x\u02c0\3\2\2\2z\u02c8\3\2\2\2|\u02d0\3")
        buf.write("\2\2\2~\u02ee\3\2\2\2\u0080\u02f0\3\2\2\2\u0082\u02f7")
        buf.write("\3\2\2\2\u0084\u0088\5\4\3\2\u0085\u0087\7y\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3")
        buf.write("\2\2\2\u008b\u008d\5\6\4\2\u008c\u008b\3\2\2\2\u008c\u008d")
        buf.write("\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u0090\5\b\5\2\u008f")
        buf.write("\u008e\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2")
        buf.write("\u0091\u0093\5\n\6\2\u0092\u0091\3\2\2\2\u0092\u0093\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\7\2\2\3\u0095\3")
        buf.write("\3\2\2\2\u0096\u0097\7\5\2\2\u0097\u009a\5b\62\2\u0098")
        buf.write("\u0099\7H\2\2\u0099\u009b\5b\62\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\7")
        buf.write("y\2\2\u009d\5\3\2\2\2\u009e\u009f\7\6\2\2\u009f\u00a0")
        buf.write("\7H\2\2\u00a0\u00a1\7y\2\2\u00a1\u00a3\7\3\2\2\u00a2\u00a4")
        buf.write("\5\f\7\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00a8\7\4\2\2\u00a8\7\3\2\2\2\u00a9\u00aa\7\7\2")
        buf.write("\2\u00aa\u00ab\7H\2\2\u00ab\u00ac\7y\2\2\u00ac\u00ad\7")
        buf.write("\3\2\2\u00ad\u00ae\5\16\b\2\u00ae\u00af\7\4\2\2\u00af")
        buf.write("\t\3\2\2\2\u00b0\u00b1\7\b\2\2\u00b1\u00b2\7H\2\2\u00b2")
        buf.write("\u00b3\7y\2\2\u00b3\u00b6\7\3\2\2\u00b4\u00b7\58\35\2")
        buf.write("\u00b5\u00b7\5\20\t\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\7\4\2\2")
        buf.write("\u00bb\13\3\2\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7J\2")
        buf.write("\2\u00be\u00bf\5@!\2\u00bf\u00c0\7y\2\2\u00c0\r\3\2\2")
        buf.write("\2\u00c1\u00c3\5\22\n\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c8\5:\36\2\u00c5")
        buf.write("\u00c8\5\24\13\2\u00c6\u00c8\5\62\32\2\u00c7\u00c4\3\2")
        buf.write("\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\17\3\2\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7H\2\2\u00cd")
        buf.write("\u00ce\7y\2\2\u00ce\u00d0\7\3\2\2\u00cf\u00d1\5\f\7\2")
        buf.write("\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5")
        buf.write("\7\4\2\2\u00d5\21\3\2\2\2\u00d6\u00d7\7\21\2\2\u00d7\u00d8")
        buf.write("\5@!\2\u00d8\u00d9\7y\2\2\u00d9\23\3\2\2\2\u00da\u00dd")
        buf.write("\7\26\2\2\u00db\u00de\7\20\2\2\u00dc\u00de\5b\62\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write('\u00df\u00e0\5"\22\2\u00e0\25\3\2\2\2\u00e1\u00e3\7\22')
        buf.write("\2\2\u00e2\u00e4\5@!\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00f7\3\2\2\2\u00e5\u00e7\7\16\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00f0\7\13\2\2\u00e9\u00f0\5\30\r\2\u00ea\u00eb")
        buf.write("\5\32\16\2\u00eb\u00ec\7\f\2\2\u00ec\u00f0\3\2\2\2\u00ed")
        buf.write("\u00ee\7:\2\2\u00ee\u00f0\5@!\2\u00ef\u00e6\3\2\2\2\u00ef")
        buf.write("\u00e9\3\2\2\2\u00ef\u00ea\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write('\u00f0\u00f3\3\2\2\2\u00f1\u00f4\5"\22\2\u00f2\u00f4')
        buf.write("\7y\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f8\3\2\2\2\u00f5\u00f6\7\17\2\2\u00f6\u00f8\5$\23")
        buf.write("\2\u00f7\u00ef\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\27\3")
        buf.write("\2\2\2\u00f9\u00fa\t\2\2\2\u00fa\31\3\2\2\2\u00fb\u00fc")
        buf.write("\t\3\2\2\u00fc\33\3\2\2\2\u00fd\u00ff\7\24\2\2\u00fe\u0100")
        buf.write("\5@!\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\u0102\7:\2\2\u0102\u0105\5@!\2\u0103\u0106")
        buf.write('\5"\22\2\u0104\u0106\7y\2\2\u0105\u0103\3\2\2\2\u0105')
        buf.write("\u0104\3\2\2\2\u0106\35\3\2\2\2\u0107\u0108\7\23\2\2\u0108")
        buf.write("\u0109\7Z\2\2\u0109\u010e\5b\62\2\u010a\u010b\7G\2\2\u010b")
        buf.write("\u010d\5b\62\2\u010c\u010a\3\2\2\2\u010d\u0110\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3")
        buf.write("\2\2\2\u0110\u010e\3\2\2\2\u0111\u0114\7[\2\2\u0112\u0115")
        buf.write('\5"\22\2\u0113\u0115\7y\2\2\u0114\u0112\3\2\2\2\u0114')
        buf.write("\u0113\3\2\2\2\u0115\37\3\2\2\2\u0116\u011e\7\25\2\2\u0117")
        buf.write("\u011c\7\13\2\2\u0118\u011c\7\f\2\2\u0119\u011c\7\17\2")
        buf.write("\2\u011a\u011c\5b\62\2\u011b\u0117\3\2\2\2\u011b\u0118")
        buf.write("\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011d\u011f\7\64\2\2\u011e\u011b\3\2\2")
        buf.write("\2\u011e\u011f\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0123")
        buf.write("\5@!\2\u0121\u0124\5$\23\2\u0122\u0124\7y\2\2\u0123\u0121")
        buf.write("\3\2\2\2\u0123\u0122\3\2\2\2\u0124!\3\2\2\2\u0125\u0126")
        buf.write("\7H\2\2\u0126\u0127\7y\2\2\u0127\u012a\7\3\2\2\u0128\u012b")
        buf.write("\5&\24\2\u0129\u012b\5.\30\2\u012a\u0128\3\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\7")
        buf.write("\4\2\2\u012f#\3\2\2\2\u0130\u0131\7H\2\2\u0131\u0132\7")
        buf.write("y\2\2\u0132\u0134\7\3\2\2\u0133\u0135\5(\25\2\u0134\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\7\4\2\2")
        buf.write("\u0139%\3\2\2\2\u013a\u013e\5,\27\2\u013b\u013e\5(\25")
        buf.write("\2\u013c\u013e\5*\26\2\u013d\u013a\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013d\u013c\3\2\2\2\u013e'\3\2\2\2\u013f\u0142")
        buf.write("\5b\62\2\u0140\u0141\7H\2\2\u0141\u0143\5b\62\2\u0142")
        buf.write("\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2")
        buf.write("\u0144\u0146\5@!\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2")
        buf.write("\2\2\u0146\u0147\3\2\2\2\u0147\u0148\7y\2\2\u0148)\3\2")
        buf.write("\2\2\u0149\u014a\7&\2\2\u014a\u014b\7\63\2\2\u014b\u0150")
        buf.write("\5b\62\2\u014c\u014d\7'\2\2\u014d\u0150\5b\62\2\u014e")
        buf.write("\u0150\7(\2\2\u014f\u0149\3\2\2\2\u014f\u014c\3\2\2\2")
        buf.write("\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u0154\5")
        buf.write("$\23\2\u0152\u0154\7y\2\2\u0153\u0151\3\2\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154+\3\2\2\2\u0155\u0157\7\33\2\2\u0156\u0158")
        buf.write("\7$\2\2\u0157\u0156\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159\u015a\7\62\2\2\u015a\u0173\5@!\2")
        buf.write("\u015b\u015c\7\34\2\2\u015c\u015d\7\62\2\2\u015d\u0173")
        buf.write("\5@!\2\u015e\u0160\7\35\2\2\u015f\u0161\7$\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0164\5@!\2\u0163\u0165\7%\2\2\u0164\u0163\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0173\3\2\2\2\u0166\u0167\7\36\2")
        buf.write('\2\u0167\u0173\5@!\2\u0168\u0169\7"\2\2\u0169\u0173\5')
        buf.write("@!\2\u016a\u016b\7#\2\2\u016b\u0173\5@!\2\u016c\u016d")
        buf.write("\7!\2\2\u016d\u0173\5@!\2\u016e\u016f\7\37\2\2\u016f\u0173")
        buf.write("\5@!\2\u0170\u0171\7 \2\2\u0171\u0173\5@!\2\u0172\u0155")
        buf.write("\3\2\2\2\u0172\u015b\3\2\2\2\u0172\u015e\3\2\2\2\u0172")
        buf.write("\u0166\3\2\2\2\u0172\u0168\3\2\2\2\u0172\u016a\3\2\2\2")
        buf.write("\u0172\u016c\3\2\2\2\u0172\u016e\3\2\2\2\u0172\u0170\3")
        buf.write("\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\7y\2\2\u0175-\3")
        buf.write("\2\2\2\u0176\u0177\5\64\33\2\u0177\u0178\5\60\31\2\u0178")
        buf.write("/\3\2\2\2\u0179\u017a\7H\2\2\u017a\u017b\7y\2\2\u017b")
        buf.write("\u017d\7\3\2\2\u017c\u017e\5&\24\2\u017d\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\7\4\2\2\u0182\61")
        buf.write("\3\2\2\2\u0183\u0184\5\64\33\2\u0184\u0185\5\66\34\2\u0185")
        buf.write("\63\3\2\2\2\u0186\u0188\7)\2\2\u0187\u0189\5@!\2\u0188")
        buf.write("\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u018a\u018b\t\4\2\2\u018b\65\3\2\2\2\u018c\u018d\7H\2")
        buf.write("\2\u018d\u018e\7y\2\2\u018e\u0191\7\3\2\2\u018f\u0192")
        buf.write("\5:\36\2\u0190\u0192\5\24\13\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0193\u0194\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\7")
        buf.write("\4\2\2\u0196\67\3\2\2\2\u0197\u019a\5z>\2\u0198\u019b")
        buf.write("\5> \2\u0199\u019b\7J\2\2\u019a\u0198\3\2\2\2\u019a\u0199")
        buf.write("\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019f\5z>\2\u019d\u019f")
        buf.write("\5<\37\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a1\7y\2\2\u01a19\3\2\2\2\u01a2")
        buf.write("\u01b7\5z>\2\u01a3\u01a6\5> \2\u01a4\u01a7\5z>\2\u01a5")
        buf.write("\u01a7\5<\37\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\7")
        buf.write("y\2\2\u01a9\u01b8\3\2\2\2\u01aa\u01b5\7J\2\2\u01ab\u01ae")
        buf.write("\5z>\2\u01ac\u01ae\5<\37\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\7y\2\2\u01b0")
        buf.write("\u01b6\3\2\2\2\u01b1\u01b6\5\26\f\2\u01b2\u01b6\5\34\17")
        buf.write("\2\u01b3\u01b6\5 \21\2\u01b4\u01b6\5\36\20\2\u01b5\u01ad")
        buf.write("\3\2\2\2\u01b5\u01b1\3\2\2\2\u01b5\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b8\3\2\2\2")
        buf.write("\u01b7\u01a3\3\2\2\2\u01b7\u01aa\3\2\2\2\u01b8\u01be\3")
        buf.write("\2\2\2\u01b9\u01be\5\26\f\2\u01ba\u01be\5\34\17\2\u01bb")
        buf.write("\u01be\5 \21\2\u01bc\u01be\5\36\20\2\u01bd\u01a2\3\2\2")
        buf.write("\2\u01bd\u01b9\3\2\2\2\u01bd\u01ba\3\2\2\2\u01bd\u01bb")
        buf.write("\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be;\3\2\2\2\u01bf\u01c0")
        buf.write("\7\27\2\2\u01c0\u01c1\5@!\2\u01c1\u01c2\7:\2\2\u01c2\u01c5")
        buf.write("\5@!\2\u01c3\u01c4\7\30\2\2\u01c4\u01c6\5@!\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7")
        buf.write("\u01c8\7\31\2\2\u01c8\u01ca\5@!\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01cd\7")
        buf.write("\32\2\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("=\3\2\2\2\u01ce\u01cf\t\5\2\2\u01cf?\3\2\2\2\u01d0\u01d6")
        buf.write("\5D#\2\u01d1\u01d2\7;\2\2\u01d2\u01d3\5D#\2\u01d3\u01d4")
        buf.write("\7\67\2\2\u01d4\u01d5\5@!\2\u01d5\u01d7\3\2\2\2\u01d6")
        buf.write("\u01d1\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7A\3\2\2\2\u01d8")
        buf.write("\u01d9\5D#\2\u01d9C\3\2\2\2\u01da\u01df\5F$\2\u01db\u01dc")
        buf.write("\7@\2\2\u01dc\u01de\5F$\2\u01dd\u01db\3\2\2\2\u01de\u01e1")
        buf.write("\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("E\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e7\5H%\2\u01e3")
        buf.write("\u01e4\7\65\2\2\u01e4\u01e6\5H%\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3")
        buf.write("\2\2\2\u01e8G\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb")
        buf.write("\7?\2\2\u01eb\u01ee\5H%\2\u01ec\u01ee\5J&\2\u01ed\u01ea")
        buf.write("\3\2\2\2\u01ed\u01ec\3\2\2\2\u01eeI\3\2\2\2\u01ef\u01f5")
        buf.write("\5N(\2\u01f0\u01f1\5L'\2\u01f1\u01f2\5N(\2\u01f2\u01f4")
        buf.write("\3\2\2\2\u01f3\u01f0\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6K\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f8\u0205\7^\2\2\u01f9\u0205\7_\2\2\u01fa")
        buf.write("\u0205\7`\2\2\u01fb\u0205\7a\2\2\u01fc\u0205\7b\2\2\u01fd")
        buf.write("\u0205\7c\2\2\u01fe\u0205\7<\2\2\u01ff\u0200\7?\2\2\u0200")
        buf.write("\u0205\7<\2\2\u0201\u0205\7=\2\2\u0202\u0203\7=\2\2\u0203")
        buf.write("\u0205\7?\2\2\u0204\u01f8\3\2\2\2\u0204\u01f9\3\2\2\2")
        buf.write("\u0204\u01fa\3\2\2\2\u0204\u01fb\3\2\2\2\u0204\u01fc\3")
        buf.write("\2\2\2\u0204\u01fd\3\2\2\2\u0204\u01fe\3\2\2\2\u0204\u01ff")
        buf.write("\3\2\2\2\u0204\u0201\3\2\2\2\u0204\u0202\3\2\2\2\u0205")
        buf.write("M\3\2\2\2\u0206\u020b\5P)\2\u0207\u0208\7K\2\2\u0208\u020a")
        buf.write("\5P)\2\u0209\u0207\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020cO\3\2\2\2\u020d\u020b")
        buf.write("\3\2\2\2\u020e\u0213\5R*\2\u020f\u0210\7L\2\2\u0210\u0212")
        buf.write("\5R*\2\u0211\u020f\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211")
        buf.write("\3\2\2\2\u0213\u0214\3\2\2\2\u0214Q\3\2\2\2\u0215\u0213")
        buf.write("\3\2\2\2\u0216\u021b\5T+\2\u0217\u0218\7M\2\2\u0218\u021a")
        buf.write("\5T+\2\u0219\u0217\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219")
        buf.write("\3\2\2\2\u021b\u021c\3\2\2\2\u021cS\3\2\2\2\u021d\u021b")
        buf.write("\3\2\2\2\u021e\u0223\5V,\2\u021f\u0220\t\6\2\2\u0220\u0222")
        buf.write("\5V,\2\u0221\u021f\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221")
        buf.write("\3\2\2\2\u0223\u0224\3\2\2\2\u0224U\3\2\2\2\u0225\u0223")
        buf.write("\3\2\2\2\u0226\u022b\5X-\2\u0227\u0228\t\7\2\2\u0228\u022a")
        buf.write("\5X-\2\u0229\u0227\3\2\2\2\u022a\u022d\3\2\2\2\u022b\u0229")
        buf.write("\3\2\2\2\u022b\u022c\3\2\2\2\u022cW\3\2\2\2\u022d\u022b")
        buf.write("\3\2\2\2\u022e\u0233\5Z.\2\u022f\u0230\t\b\2\2\u0230\u0232")
        buf.write("\5Z.\2\u0231\u022f\3\2\2\2\u0232\u0235\3\2\2\2\u0233\u0231")
        buf.write("\3\2\2\2\u0233\u0234\3\2\2\2\u0234Y\3\2\2\2\u0235\u0233")
        buf.write("\3\2\2\2\u0236\u0237\t\t\2\2\u0237\u023a\5Z.\2\u0238\u023a")
        buf.write("\5\\/\2\u0239\u0236\3\2\2\2\u0239\u0238\3\2\2\2\u023a")
        buf.write("[\3\2\2\2\u023b\u023e\5^\60\2\u023c\u023d\7W\2\2\u023d")
        buf.write("\u023f\5Z.\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f")
        buf.write("]\3\2\2\2\u0240\u0244\5`\61\2\u0241\u0243\5l\67\2\u0242")
        buf.write("\u0241\3\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3\2\2\2")
        buf.write("\u0244\u0245\3\2\2\2\u0245_\3\2\2\2\u0246\u0244\3\2\2")
        buf.write("\2\u0247\u0248\7X\2\2\u0248\u0249\5@!\2\u0249\u024a\7")
        buf.write("Y\2\2\u024a\u0270\3\2\2\2\u024b\u0259\7Z\2\2\u024c\u024e")
        buf.write("\5h\65\2\u024d\u024c\3\2\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("\u025a\3\2\2\2\u024f\u0251\7R\2\2\u0250\u024f\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0253\7")
        buf.write("s\2\2\u0253\u0254\3\2\2\2\u0254\u0256\7E\2\2\u0255\u0257")
        buf.write("\7R\2\2\u0256\u0255\3\2\2\2\u0256\u0257\3\2\2\2\u0257")
        buf.write("\u0258\3\2\2\2\u0258\u025a\7s\2\2\u0259\u024d\3\2\2\2")
        buf.write("\u0259\u0250\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u0270\7")
        buf.write("[\2\2\u025c\u025e\7^\2\2\u025d\u025f\5j\66\2\u025e\u025d")
        buf.write("\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0260\3\2\2\2\u0260")
        buf.write("\u0270\7_\2\2\u0261\u0263\7\\\2\2\u0262\u0264\5|?\2\u0263")
        buf.write("\u0262\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265\3\2\2\2")
        buf.write("\u0265\u0270\7]\2\2\u0266\u0270\5b\62\2\u0267\u0270\7")
        buf.write("q\2\2\u0268\u0270\5d\63\2\u0269\u0270\7s\2\2\u026a\u0270")
        buf.write("\7x\2\2\u026b\u0270\7r\2\2\u026c\u0270\7>\2\2\u026d\u0270")
        buf.write("\7B\2\2\u026e\u0270\78\2\2\u026f\u0247\3\2\2\2\u026f\u024b")
        buf.write("\3\2\2\2\u026f\u025c\3\2\2\2\u026f\u0261\3\2\2\2\u026f")
        buf.write("\u0266\3\2\2\2\u026f\u0267\3\2\2\2\u026f\u0268\3\2\2\2")
        buf.write("\u026f\u0269\3\2\2\2\u026f\u026a\3\2\2\2\u026f\u026b\3")
        buf.write("\2\2\2\u026f\u026c\3\2\2\2\u026f\u026d\3\2\2\2\u026f\u026e")
        buf.write("\3\2\2\2\u0270a\3\2\2\2\u0271\u0272\t\n\2\2\u0272c\3\2")
        buf.write("\2\2\u0273\u0274\5f\64\2\u0274\u0275\7X\2\2\u0275\u0276")
        buf.write("\5n8\2\u0276\u0277\7Y\2\2\u0277e\3\2\2\2\u0278\u0279\t")
        buf.write("\13\2\2\u0279g\3\2\2\2\u027a\u0283\5@!\2\u027b\u0284\5")
        buf.write("\u0080A\2\u027c\u027d\7G\2\2\u027d\u027f\5@!\2\u027e\u027c")
        buf.write("\3\2\2\2\u027f\u0282\3\2\2\2\u0280\u027e\3\2\2\2\u0280")
        buf.write("\u0281\3\2\2\2\u0281\u0284\3\2\2\2\u0282\u0280\3\2\2\2")
        buf.write("\u0283\u027b\3\2\2\2\u0283\u0280\3\2\2\2\u0284i\3\2\2")
        buf.write("\2\u0285\u0286\5N(\2\u0286\u0287\7G\2\2\u0287\u0288\5")
        buf.write("N(\2\u0288\u0289\7G\2\2\u0289\u028a\5N(\2\u028ak\3\2\2")
        buf.write("\2\u028b\u028c\7Z\2\2\u028c\u028d\5r:\2\u028d\u028e\7")
        buf.write("[\2\2\u028e\u0292\3\2\2\2\u028f\u0290\7D\2\2\u0290\u0292")
        buf.write("\5b\62\2\u0291\u028b\3\2\2\2\u0291\u028f\3\2\2\2\u0292")
        buf.write("m\3\2\2\2\u0293\u0298\5p9\2\u0294\u0295\7G\2\2\u0295\u0297")
        buf.write("\5p9\2\u0296\u0294\3\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296")
        buf.write("\3\2\2\2\u0298\u0299\3\2\2\2\u0299o\3\2\2\2\u029a\u0298")
        buf.write("\3\2\2\2\u029b\u029f\5@!\2\u029c\u02a0\5\u0080A\2\u029d")
        buf.write("\u029e\7J\2\2\u029e\u02a0\5@!\2\u029f\u029c\3\2\2\2\u029f")
        buf.write("\u029d\3\2\2\2\u029f\u02a0\3\2\2\2\u02a0q\3\2\2\2\u02a1")
        buf.write("\u02a6\5t;\2\u02a2\u02a3\7G\2\2\u02a3\u02a5\5t;\2\u02a4")
        buf.write("\u02a2\3\2\2\2\u02a5\u02a8\3\2\2\2\u02a6\u02a4\3\2\2\2")
        buf.write("\u02a6\u02a7\3\2\2\2\u02a7s\3\2\2\2\u02a8\u02a6\3\2\2")
        buf.write("\2\u02a9\u02b1\5@!\2\u02aa\u02ac\7H\2\2\u02ab\u02ad\5")
        buf.write("@!\2\u02ac\u02ab\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02af")
        buf.write("\3\2\2\2\u02ae\u02b0\5v<\2\u02af\u02ae\3\2\2\2\u02af\u02b0")
        buf.write("\3\2\2\2\u02b0\u02b2\3\2\2\2\u02b1\u02aa\3\2\2\2\u02b1")
        buf.write("\u02b2\3\2\2\2\u02b2\u02bb\3\2\2\2\u02b3\u02b5\7H\2\2")
        buf.write("\u02b4\u02b6\5@!\2\u02b5\u02b4\3\2\2\2\u02b5\u02b6\3\2")
        buf.write("\2\2\u02b6\u02b8\3\2\2\2\u02b7\u02b9\5v<\2\u02b8\u02b7")
        buf.write("\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02bb\3\2\2\2\u02ba")
        buf.write("\u02a9\3\2\2\2\u02ba\u02b3\3\2\2\2\u02bbu\3\2\2\2\u02bc")
        buf.write("\u02be\7H\2\2\u02bd\u02bf\5@!\2\u02be\u02bd\3\2\2\2\u02be")
        buf.write("\u02bf\3\2\2\2\u02bfw\3\2\2\2\u02c0\u02c5\5N(\2\u02c1")
        buf.write("\u02c2\7G\2\2\u02c2\u02c4\5N(\2\u02c3\u02c1\3\2\2\2\u02c4")
        buf.write("\u02c7\3\2\2\2\u02c5\u02c3\3\2\2\2\u02c5\u02c6\3\2\2\2")
        buf.write("\u02c6y\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c8\u02cd\5@!\2")
        buf.write("\u02c9\u02ca\7G\2\2\u02ca\u02cc\5@!\2\u02cb\u02c9\3\2")
        buf.write("\2\2\u02cc\u02cf\3\2\2\2\u02cd\u02cb\3\2\2\2\u02cd\u02ce")
        buf.write("\3\2\2\2\u02ce{\3\2\2\2\u02cf\u02cd\3\2\2\2\u02d0\u02ea")
        buf.write("\5@!\2\u02d1\u02d2\7H\2\2\u02d2\u02de\5@!\2\u02d3\u02df")
        buf.write("\5\u0080A\2\u02d4\u02d5\7G\2\2\u02d5\u02d6\5@!\2\u02d6")
        buf.write("\u02d7\7H\2\2\u02d7\u02d8\5@!\2\u02d8\u02da\3\2\2\2\u02d9")
        buf.write("\u02d4\3\2\2\2\u02da\u02dd\3\2\2\2\u02db\u02d9\3\2\2\2")
        buf.write("\u02db\u02dc\3\2\2\2\u02dc\u02df\3\2\2\2\u02dd\u02db\3")
        buf.write("\2\2\2\u02de\u02d3\3\2\2\2\u02de\u02db\3\2\2\2\u02df\u02eb")
        buf.write("\3\2\2\2\u02e0\u02e9\5\u0080A\2\u02e1\u02e2\7G\2\2\u02e2")
        buf.write("\u02e4\5@!\2\u02e3\u02e1\3\2\2\2\u02e4\u02e7\3\2\2\2\u02e5")
        buf.write("\u02e3\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6\u02e9\3\2\2\2")
        buf.write("\u02e7\u02e5\3\2\2\2\u02e8\u02e0\3\2\2\2\u02e8\u02e5\3")
        buf.write("\2\2\2\u02e9\u02eb\3\2\2\2\u02ea\u02d1\3\2\2\2\u02ea\u02e8")
        buf.write("\3\2\2\2\u02eb}\3\2\2\2\u02ec\u02ef\5\u0080A\2\u02ed\u02ef")
        buf.write("\5\u0082B\2\u02ee\u02ec\3\2\2\2\u02ee\u02ed\3\2\2\2\u02ef")
        buf.write("\177\3\2\2\2\u02f0\u02f1\79\2\2\u02f1\u02f2\5x=\2\u02f2")
        buf.write("\u02f3\7<\2\2\u02f3\u02f5\5D#\2\u02f4\u02f6\5~@\2\u02f5")
        buf.write("\u02f4\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u0081\3\2\2\2")
        buf.write('\u02f7\u02f8\7;\2\2\u02f8\u02fa\5B"\2\u02f9\u02fb\5~')
        buf.write("@\2\u02fa\u02f9\3\2\2\2\u02fa\u02fb\3\2\2\2\u02fb\u0083")
        buf.write("\3\2\2\2b\u0088\u008c\u008f\u0092\u009a\u00a5\u00b6\u00b8")
        buf.write("\u00c2\u00c7\u00c9\u00d2\u00dd\u00e3\u00e6\u00ef\u00f3")
        buf.write("\u00f7\u00ff\u0105\u010e\u0114\u011b\u011e\u0123\u012a")
        buf.write("\u012c\u0136\u013d\u0142\u0145\u014f\u0153\u0157\u0160")
        buf.write("\u0164\u0172\u017f\u0188\u0191\u0193\u019a\u019e\u01a6")
        buf.write("\u01ad\u01b5\u01b7\u01bd\u01c5\u01c9\u01cc\u01d6\u01df")
        buf.write("\u01e7\u01ed\u01f5\u0204\u020b\u0213\u021b\u0223\u022b")
        buf.write("\u0233\u0239\u023e\u0244\u024d\u0250\u0256\u0259\u025e")
        buf.write("\u0263\u026f\u0280\u0283\u0291\u0298\u029f\u02a6\u02ac")
        buf.write("\u02af\u02b1\u02b5\u02b8\u02ba\u02be\u02c5\u02cd\u02db")
        buf.write("\u02de\u02e5\u02e8\u02ea\u02ee\u02f5\u02fa")
        return buf.getvalue()


class YarcParser(Parser):
    grammarFileName = "YarcParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'scenario'",
        "'settings'",
        "'stage'",
        "'writers'",
        "<INVALID>",
        "<INVALID>",
        "'Camera'",
        "'Light'",
        "<INVALID>",
        "'Stereo'",
        "'Material'",
        "'Timeline'",
        "'open'",
        "'create'",
        "'group'",
        "'instantiate'",
        "'get'",
        "'edit'",
        "'fetch'",
        "'match'",
        "'limit'",
        "'recursive'",
        "'translate'",
        "'camera_translate'",
        "'rotate'",
        "'scale'",
        "'semantics'",
        "'visible'",
        "'size'",
        "'look_at'",
        "'up_axis'",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'rotate_around'",
        "<INVALID>",
        "'every'",
        "<INVALID>",
        "<INVALID>",
        "'Uniform'",
        "'Normal'",
        "'Choice'",
        "'Sequence'",
        "'LogUniform'",
        "<INVALID>",
        "'to'",
        "'on'",
        "'at'",
        "'and'",
        "'def'",
        "'else'",
        "'false'",
        "'for'",
        "'from'",
        "'if'",
        "'in'",
        "'is'",
        "'none'",
        "'not'",
        "'or'",
        "'return'",
        "'true'",
        "'_'",
        "'.'",
        "'..'",
        "'...'",
        "','",
        "':'",
        "';'",
        "'='",
        "'|'",
        "'^'",
        "'&'",
        "'~'",
        "'<<'",
        "'>>'",
        "'+'",
        "'-'",
        "'/'",
        "'*'",
        "'%'",
        "'//'",
        "'**'",
        "'('",
        "')'",
        "'['",
        "']'",
        "'{'",
        "'}'",
        "'<'",
        "'>'",
        "'=='",
        "'>='",
        "'<='",
        "'!='",
        "'+='",
        "'-='",
        "'*='",
        "'/='",
        "'%='",
        "'&='",
        "'|='",
        "'^='",
        "'<<='",
        "'>>='",
        "'**='",
        "'//='",
    ]

    symbolicNames = [
        "<INVALID>",
        "INDENT",
        "DEDENT",
        "SCENARIO",
        "SETTINGS",
        "STAGE",
        "WRITERS",
        "SHAPES",
        "SHAPES_OR_LIGHTS",
        "CAMERA",
        "LIGHT",
        "LIGHT_TYPE",
        "STEREO",
        "MATERIAL",
        "TIMELINE",
        "OPEN",
        "CREATE",
        "GROUP",
        "INSTANTIATE",
        "GET",
        "EDIT",
        "FETCH",
        "MATCH",
        "LIMIT",
        "RECURSIVE",
        "TRANSLATE",
        "CAM_TRANSLATE",
        "ROTATE",
        "SCALE",
        "SEMANTICS",
        "VISIBLE",
        "SIZE",
        "LOOK_AT",
        "UP_AXIS",
        "AXIS",
        "ORDER",
        "SCATTER",
        "ROT_AROUND",
        "PHYSICS",
        "EVERY",
        "FRAMES",
        "TIME",
        "UNIFORM",
        "NORMAL",
        "CHOICE",
        "SEQUENCE",
        "LOG_UNIFORM",
        "SNIPPET",
        "TO",
        "ON",
        "AT",
        "AND",
        "DEF",
        "ELSE",
        "FALSE",
        "FOR",
        "FROM",
        "IF",
        "IN",
        "IS",
        "NONE",
        "NOT",
        "OR",
        "RETURN",
        "TRUE",
        "UNDERSCORE",
        "DOT",
        "RANGE",
        "ELLIPSIS",
        "COMMA",
        "COLON",
        "SEMI",
        "ASSIGN",
        "BIT_OR",
        "XOR",
        "BIT_AND",
        "BIT_NOT",
        "LSHIFT",
        "RSHIFT",
        "PLUS",
        "MINUS",
        "DIV",
        "MUL",
        "MOD",
        "IDIV",
        "POWER",
        "LPAREN",
        "RPAREN",
        "LBRACK",
        "RBRACK",
        "LBRACE",
        "RBRACE",
        "LT",
        "GT",
        "EQUALS",
        "GT_EQ",
        "LT_EQ",
        "NOT_EQ",
        "ADD_ASSIGN",
        "SUB_ASSIGN",
        "MULT_ASSIGN",
        "DIV_ASSIGN",
        "MOD_ASSIGN",
        "AND_ASSIGN",
        "OR_ASSIGN",
        "XOR_ASSIGN",
        "LSHIFT_ASSIGN",
        "RSHIFT_ASSIGN",
        "POWER_ASSIGN",
        "IDIV_ASSIGN",
        "ID",
        "SETTING_ID",
        "STRING",
        "INTEGER",
        "DEC_INTEGER",
        "OCT_INTEGER",
        "HEX_INTEGER",
        "BIN_INTEGER",
        "FLOAT_NUMBER",
        "NEWLINE",
        "SKIP_",
        "UNKNOWN",
    ]

    RULE_scenario = 0
    RULE_declaration = 1
    RULE_settings = 2
    RULE_stage = 3
    RULE_writers = 4
    RULE_option = 5
    RULE_stmts = 6
    RULE_writer = 7
    RULE_open_stmt = 8
    RULE_edit_stmt = 9
    RULE_create_expr = 10
    RULE_shapes = 11
    RULE_light_type = 12
    RULE_instantiate_expr = 13
    RULE_group_expr = 14
    RULE_get_expr = 15
    RULE_edit_block = 16
    RULE_simple_block = 17
    RULE_attr = 18
    RULE_simple_attr = 19
    RULE_compound_attr = 20
    RULE_core_attr = 21
    RULE_inner_behavior_stmt = 22
    RULE_inner_behavior_block = 23
    RULE_behavior_stmt = 24
    RULE_behavior_expr = 25
    RULE_behavior_block = 26
    RULE_expr_stmt = 27
    RULE_aug_expr_stmt = 28
    RULE_fetch_expr = 29
    RULE_aug_assign = 30
    RULE_test = 31
    RULE_test_nocond = 32
    RULE_or_test = 33
    RULE_and_test = 34
    RULE_not_test = 35
    RULE_comparison = 36
    RULE_comp_op = 37
    RULE_expr = 38
    RULE_xor_expr = 39
    RULE_and_expr = 40
    RULE_shift_expr = 41
    RULE_arith_expr = 42
    RULE_term = 43
    RULE_factor = 44
    RULE_power = 45
    RULE_atom_expr = 46
    RULE_atom = 47
    RULE_name = 48
    RULE_distribution_expr = 49
    RULE_distribution = 50
    RULE_testlist_comp = 51
    RULE_vector_comp = 52
    RULE_trailer = 53
    RULE_arglist = 54
    RULE_argument = 55
    RULE_subscriptlist = 56
    RULE_subscript_ = 57
    RULE_sliceop = 58
    RULE_exprlist = 59
    RULE_testlist = 60
    RULE_dict_or_set_maker = 61
    RULE_comp_iter = 62
    RULE_comp_for = 63
    RULE_comp_if = 64

    ruleNames = [
        "scenario",
        "declaration",
        "settings",
        "stage",
        "writers",
        "option",
        "stmts",
        "writer",
        "open_stmt",
        "edit_stmt",
        "create_expr",
        "shapes",
        "light_type",
        "instantiate_expr",
        "group_expr",
        "get_expr",
        "edit_block",
        "simple_block",
        "attr",
        "simple_attr",
        "compound_attr",
        "core_attr",
        "inner_behavior_stmt",
        "inner_behavior_block",
        "behavior_stmt",
        "behavior_expr",
        "behavior_block",
        "expr_stmt",
        "aug_expr_stmt",
        "fetch_expr",
        "aug_assign",
        "test",
        "test_nocond",
        "or_test",
        "and_test",
        "not_test",
        "comparison",
        "comp_op",
        "expr",
        "xor_expr",
        "and_expr",
        "shift_expr",
        "arith_expr",
        "term",
        "factor",
        "power",
        "atom_expr",
        "atom",
        "name",
        "distribution_expr",
        "distribution",
        "testlist_comp",
        "vector_comp",
        "trailer",
        "arglist",
        "argument",
        "subscriptlist",
        "subscript_",
        "sliceop",
        "exprlist",
        "testlist",
        "dict_or_set_maker",
        "comp_iter",
        "comp_for",
        "comp_if",
    ]

    EOF = Token.EOF
    INDENT = 1
    DEDENT = 2
    SCENARIO = 3
    SETTINGS = 4
    STAGE = 5
    WRITERS = 6
    SHAPES = 7
    SHAPES_OR_LIGHTS = 8
    CAMERA = 9
    LIGHT = 10
    LIGHT_TYPE = 11
    STEREO = 12
    MATERIAL = 13
    TIMELINE = 14
    OPEN = 15
    CREATE = 16
    GROUP = 17
    INSTANTIATE = 18
    GET = 19
    EDIT = 20
    FETCH = 21
    MATCH = 22
    LIMIT = 23
    RECURSIVE = 24
    TRANSLATE = 25
    CAM_TRANSLATE = 26
    ROTATE = 27
    SCALE = 28
    SEMANTICS = 29
    VISIBLE = 30
    SIZE = 31
    LOOK_AT = 32
    UP_AXIS = 33
    AXIS = 34
    ORDER = 35
    SCATTER = 36
    ROT_AROUND = 37
    PHYSICS = 38
    EVERY = 39
    FRAMES = 40
    TIME = 41
    UNIFORM = 42
    NORMAL = 43
    CHOICE = 44
    SEQUENCE = 45
    LOG_UNIFORM = 46
    SNIPPET = 47
    TO = 48
    ON = 49
    AT = 50
    AND = 51
    DEF = 52
    ELSE = 53
    FALSE = 54
    FOR = 55
    FROM = 56
    IF = 57
    IN = 58
    IS = 59
    NONE = 60
    NOT = 61
    OR = 62
    RETURN = 63
    TRUE = 64
    UNDERSCORE = 65
    DOT = 66
    RANGE = 67
    ELLIPSIS = 68
    COMMA = 69
    COLON = 70
    SEMI = 71
    ASSIGN = 72
    BIT_OR = 73
    XOR = 74
    BIT_AND = 75
    BIT_NOT = 76
    LSHIFT = 77
    RSHIFT = 78
    PLUS = 79
    MINUS = 80
    DIV = 81
    MUL = 82
    MOD = 83
    IDIV = 84
    POWER = 85
    LPAREN = 86
    RPAREN = 87
    LBRACK = 88
    RBRACK = 89
    LBRACE = 90
    RBRACE = 91
    LT = 92
    GT = 93
    EQUALS = 94
    GT_EQ = 95
    LT_EQ = 96
    NOT_EQ = 97
    ADD_ASSIGN = 98
    SUB_ASSIGN = 99
    MULT_ASSIGN = 100
    DIV_ASSIGN = 101
    MOD_ASSIGN = 102
    AND_ASSIGN = 103
    OR_ASSIGN = 104
    XOR_ASSIGN = 105
    LSHIFT_ASSIGN = 106
    RSHIFT_ASSIGN = 107
    POWER_ASSIGN = 108
    IDIV_ASSIGN = 109
    ID = 110
    SETTING_ID = 111
    STRING = 112
    INTEGER = 113
    DEC_INTEGER = 114
    OCT_INTEGER = 115
    HEX_INTEGER = 116
    BIN_INTEGER = 117
    FLOAT_NUMBER = 118
    NEWLINE = 119
    SKIP_ = 120
    UNKNOWN = 121

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ScenarioContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(YarcParser.DeclarationContext, 0)

        def EOF(self):
            return self.getToken(YarcParser.EOF, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.NEWLINE)
            else:
                return self.getToken(YarcParser.NEWLINE, i)

        def settings(self):
            return self.getTypedRuleContext(YarcParser.SettingsContext, 0)

        def stage(self):
            return self.getTypedRuleContext(YarcParser.StageContext, 0)

        def writers(self):
            return self.getTypedRuleContext(YarcParser.WritersContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_scenario

    def scenario(self):
        localctx = YarcParser.ScenarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_scenario)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.declaration()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.NEWLINE:
                self.state = 131
                self.match(YarcParser.NEWLINE)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.SETTINGS:
                self.state = 137
                self.settings()

            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.STAGE:
                self.state = 140
                self.stage()

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.WRITERS:
                self.state = 143
                self.writers()

            self.state = 146
            self.match(YarcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCENARIO(self):
            return self.getToken(YarcParser.SCENARIO, 0)

        def name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext, i)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_declaration

    def declaration(self):
        localctx = YarcParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(YarcParser.SCENARIO)
            self.state = 149
            self.name()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 150
                self.match(YarcParser.COLON)
                self.state = 151
                self.name()

            self.state = 154
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SettingsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SETTINGS(self):
            return self.getToken(YarcParser.SETTINGS, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def option(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.OptionContext)
            else:
                return self.getTypedRuleContext(YarcParser.OptionContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_settings

    def settings(self):
        localctx = YarcParser.SettingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_settings)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(YarcParser.SETTINGS)
            self.state = 157
            self.match(YarcParser.COLON)
            self.state = 158
            self.match(YarcParser.NEWLINE)
            self.state = 159
            self.match(YarcParser.INDENT)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 160
                self.option()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.ID):
                    break

            self.state = 165
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StageContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAGE(self):
            return self.getToken(YarcParser.STAGE, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def stmts(self):
            return self.getTypedRuleContext(YarcParser.StmtsContext, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_stage

    def stage(self):
        localctx = YarcParser.StageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(YarcParser.STAGE)
            self.state = 168
            self.match(YarcParser.COLON)
            self.state = 169
            self.match(YarcParser.NEWLINE)
            self.state = 170
            self.match(YarcParser.INDENT)
            self.state = 171
            self.stmts()
            self.state = 172
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WritersContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITERS(self):
            return self.getToken(YarcParser.WRITERS, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Expr_stmtContext, i)

        def writer(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.WriterContext)
            else:
                return self.getTypedRuleContext(YarcParser.WriterContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_writers

    def writers(self):
        localctx = YarcParser.WritersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_writers)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(YarcParser.WRITERS)
            self.state = 175
            self.match(YarcParser.COLON)
            self.state = 176
            self.match(YarcParser.NEWLINE)
            self.state = 177
            self.match(YarcParser.INDENT)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 6, self._ctx)
                if la_ == 1:
                    self.state = 178
                    self.expr_stmt()

                elif la_ == 2:
                    self.state = 179
                    self.writer()

                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 64) & ~0x3F) == 0
                        and (
                            (1 << (_la - 64))
                            & (
                                (1 << (YarcParser.TRUE - 64))
                                | (1 << (YarcParser.UNDERSCORE - 64))
                                | (1 << (YarcParser.BIT_NOT - 64))
                                | (1 << (YarcParser.PLUS - 64))
                                | (1 << (YarcParser.MINUS - 64))
                                | (1 << (YarcParser.LPAREN - 64))
                                | (1 << (YarcParser.LBRACK - 64))
                                | (1 << (YarcParser.LBRACE - 64))
                                | (1 << (YarcParser.LT - 64))
                                | (1 << (YarcParser.ID - 64))
                                | (1 << (YarcParser.SETTING_ID - 64))
                                | (1 << (YarcParser.STRING - 64))
                                | (1 << (YarcParser.INTEGER - 64))
                                | (1 << (YarcParser.FLOAT_NUMBER - 64))
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 184
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YarcParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_option

    def option(self):
        localctx = YarcParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(YarcParser.ID)
            self.state = 187
            self.match(YarcParser.ASSIGN)
            self.state = 188
            self.test()
            self.state = 189
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_stmt(self):
            return self.getTypedRuleContext(YarcParser.Open_stmtContext, 0)

        def aug_expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Aug_expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Aug_expr_stmtContext, i)

        def edit_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Edit_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Edit_stmtContext, i)

        def behavior_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Behavior_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Behavior_stmtContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_stmts

    def stmts(self):
        localctx = YarcParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmts)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.OPEN:
                self.state = 191
                self.open_stmt()

            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 197
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.CREATE,
                    YarcParser.GROUP,
                    YarcParser.INSTANTIATE,
                    YarcParser.GET,
                    YarcParser.UNIFORM,
                    YarcParser.NORMAL,
                    YarcParser.CHOICE,
                    YarcParser.SEQUENCE,
                    YarcParser.LOG_UNIFORM,
                    YarcParser.FALSE,
                    YarcParser.NONE,
                    YarcParser.NOT,
                    YarcParser.TRUE,
                    YarcParser.UNDERSCORE,
                    YarcParser.BIT_NOT,
                    YarcParser.PLUS,
                    YarcParser.MINUS,
                    YarcParser.LPAREN,
                    YarcParser.LBRACK,
                    YarcParser.LBRACE,
                    YarcParser.LT,
                    YarcParser.ID,
                    YarcParser.SETTING_ID,
                    YarcParser.STRING,
                    YarcParser.INTEGER,
                    YarcParser.FLOAT_NUMBER,
                ]:
                    self.state = 194
                    self.aug_expr_stmt()
                elif token in [YarcParser.EDIT]:
                    self.state = 195
                    self.edit_stmt()
                elif token in [YarcParser.EVERY]:
                    self.state = 196
                    self.behavior_stmt()
                else:
                    raise NoViableAltException(self)

                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.CREATE)
                                | (1 << YarcParser.GROUP)
                                | (1 << YarcParser.INSTANTIATE)
                                | (1 << YarcParser.GET)
                                | (1 << YarcParser.EDIT)
                                | (1 << YarcParser.EVERY)
                                | (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 64) & ~0x3F) == 0
                        and (
                            (1 << (_la - 64))
                            & (
                                (1 << (YarcParser.TRUE - 64))
                                | (1 << (YarcParser.UNDERSCORE - 64))
                                | (1 << (YarcParser.BIT_NOT - 64))
                                | (1 << (YarcParser.PLUS - 64))
                                | (1 << (YarcParser.MINUS - 64))
                                | (1 << (YarcParser.LPAREN - 64))
                                | (1 << (YarcParser.LBRACK - 64))
                                | (1 << (YarcParser.LBRACE - 64))
                                | (1 << (YarcParser.LT - 64))
                                | (1 << (YarcParser.ID - 64))
                                | (1 << (YarcParser.SETTING_ID - 64))
                                | (1 << (YarcParser.STRING - 64))
                                | (1 << (YarcParser.INTEGER - 64))
                                | (1 << (YarcParser.FLOAT_NUMBER - 64))
                            )
                        )
                        != 0
                    )
                ):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WriterContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YarcParser.ID, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def option(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.OptionContext)
            else:
                return self.getTypedRuleContext(YarcParser.OptionContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_writer

    def writer(self):
        localctx = YarcParser.WriterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_writer)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(YarcParser.ID)
            self.state = 202
            self.match(YarcParser.COLON)
            self.state = 203
            self.match(YarcParser.NEWLINE)
            self.state = 204
            self.match(YarcParser.INDENT)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 205
                self.option()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.ID):
                    break

            self.state = 210
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Open_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(YarcParser.OPEN, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_open_stmt

    def open_stmt(self):
        localctx = YarcParser.Open_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_open_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(YarcParser.OPEN)
            self.state = 213
            self.test()
            self.state = 214
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Edit_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EDIT(self):
            return self.getToken(YarcParser.EDIT, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def TIMELINE(self):
            return self.getToken(YarcParser.TIMELINE, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_edit_stmt

    def edit_stmt(self):
        localctx = YarcParser.Edit_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_edit_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(YarcParser.EDIT)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.TIMELINE]:
                self.state = 217
                self.match(YarcParser.TIMELINE)
            elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.state = 218
                self.name()
            else:
                raise NoViableAltException(self)

            self.state = 221
            self.edit_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Create_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(YarcParser.CREATE, 0)

        def MATERIAL(self):
            return self.getToken(YarcParser.MATERIAL, 0)

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def CAMERA(self):
            return self.getToken(YarcParser.CAMERA, 0)

        def shapes(self):
            return self.getTypedRuleContext(YarcParser.ShapesContext, 0)

        def light_type(self):
            return self.getTypedRuleContext(YarcParser.Light_typeContext, 0)

        def LIGHT(self):
            return self.getToken(YarcParser.LIGHT, 0)

        def FROM(self):
            return self.getToken(YarcParser.FROM, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def simple_block(self):
            return self.getTypedRuleContext(YarcParser.Simple_blockContext, 0)

        def STEREO(self):
            return self.getToken(YarcParser.STEREO, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_create_expr

    def create_expr(self):
        localctx = YarcParser.Create_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_create_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(YarcParser.CREATE)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                    )
                )
                != 0
            ) or (
                ((_la - 64) & ~0x3F) == 0
                and (
                    (1 << (_la - 64))
                    & (
                        (1 << (YarcParser.TRUE - 64))
                        | (1 << (YarcParser.UNDERSCORE - 64))
                        | (1 << (YarcParser.BIT_NOT - 64))
                        | (1 << (YarcParser.PLUS - 64))
                        | (1 << (YarcParser.MINUS - 64))
                        | (1 << (YarcParser.LPAREN - 64))
                        | (1 << (YarcParser.LBRACK - 64))
                        | (1 << (YarcParser.LBRACE - 64))
                        | (1 << (YarcParser.LT - 64))
                        | (1 << (YarcParser.ID - 64))
                        | (1 << (YarcParser.SETTING_ID - 64))
                        | (1 << (YarcParser.STRING - 64))
                        | (1 << (YarcParser.INTEGER - 64))
                        | (1 << (YarcParser.FLOAT_NUMBER - 64))
                    )
                )
                != 0
            ):
                self.state = 224
                self.test()

            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.SHAPES,
                YarcParser.SHAPES_OR_LIGHTS,
                YarcParser.CAMERA,
                YarcParser.LIGHT_TYPE,
                YarcParser.STEREO,
                YarcParser.FROM,
            ]:
                self.state = 237
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 15, self._ctx)
                if la_ == 1:
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.STEREO:
                        self.state = 227
                        self.match(YarcParser.STEREO)

                    self.state = 230
                    self.match(YarcParser.CAMERA)

                elif la_ == 2:
                    self.state = 231
                    self.shapes()

                elif la_ == 3:
                    self.state = 232
                    self.light_type()
                    self.state = 233
                    self.match(YarcParser.LIGHT)

                elif la_ == 4:
                    self.state = 235
                    self.match(YarcParser.FROM)
                    self.state = 236
                    self.test()

                self.state = 241
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.COLON]:
                    self.state = 239
                    self.edit_block()
                elif token in [YarcParser.NEWLINE]:
                    self.state = 240
                    self.match(YarcParser.NEWLINE)
                else:
                    raise NoViableAltException(self)

            elif token in [YarcParser.MATERIAL]:
                self.state = 243
                self.match(YarcParser.MATERIAL)

                self.state = 244
                self.simple_block()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShapesContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHAPES(self):
            return self.getToken(YarcParser.SHAPES, 0)

        def SHAPES_OR_LIGHTS(self):
            return self.getToken(YarcParser.SHAPES_OR_LIGHTS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_shapes

    def shapes(self):
        localctx = YarcParser.ShapesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_shapes)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if not (_la == YarcParser.SHAPES or _la == YarcParser.SHAPES_OR_LIGHTS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Light_typeContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIGHT_TYPE(self):
            return self.getToken(YarcParser.LIGHT_TYPE, 0)

        def SHAPES_OR_LIGHTS(self):
            return self.getToken(YarcParser.SHAPES_OR_LIGHTS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_light_type

    def light_type(self):
        localctx = YarcParser.Light_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_light_type)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not (_la == YarcParser.SHAPES_OR_LIGHTS or _la == YarcParser.LIGHT_TYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instantiate_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANTIATE(self):
            return self.getToken(YarcParser.INSTANTIATE, 0)

        def FROM(self):
            return self.getToken(YarcParser.FROM, 0)

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_instantiate_expr

    def instantiate_expr(self):
        localctx = YarcParser.Instantiate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_instantiate_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(YarcParser.INSTANTIATE)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                    )
                )
                != 0
            ) or (
                ((_la - 64) & ~0x3F) == 0
                and (
                    (1 << (_la - 64))
                    & (
                        (1 << (YarcParser.TRUE - 64))
                        | (1 << (YarcParser.UNDERSCORE - 64))
                        | (1 << (YarcParser.BIT_NOT - 64))
                        | (1 << (YarcParser.PLUS - 64))
                        | (1 << (YarcParser.MINUS - 64))
                        | (1 << (YarcParser.LPAREN - 64))
                        | (1 << (YarcParser.LBRACK - 64))
                        | (1 << (YarcParser.LBRACE - 64))
                        | (1 << (YarcParser.LT - 64))
                        | (1 << (YarcParser.ID - 64))
                        | (1 << (YarcParser.SETTING_ID - 64))
                        | (1 << (YarcParser.STRING - 64))
                        | (1 << (YarcParser.INTEGER - 64))
                        | (1 << (YarcParser.FLOAT_NUMBER - 64))
                    )
                )
                != 0
            ):
                self.state = 252
                self.test()

            self.state = 255
            self.match(YarcParser.FROM)
            self.state = 256
            self.test()
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 257
                self.edit_block()
            elif token in [YarcParser.NEWLINE]:
                self.state = 258
                self.match(YarcParser.NEWLINE)
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Group_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(YarcParser.GROUP, 0)

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext, i)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_group_expr

    def group_expr(self):
        localctx = YarcParser.Group_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_group_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(YarcParser.GROUP)
            self.state = 262
            self.match(YarcParser.LBRACK)
            self.state = 263
            self.name()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 264
                self.match(YarcParser.COMMA)
                self.state = 265
                self.name()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self.match(YarcParser.RBRACK)
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 272
                self.edit_block()
            elif token in [YarcParser.NEWLINE]:
                self.state = 273
                self.match(YarcParser.NEWLINE)
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Get_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(YarcParser.GET, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def simple_block(self):
            return self.getTypedRuleContext(YarcParser.Simple_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def AT(self):
            return self.getToken(YarcParser.AT, 0)

        def CAMERA(self):
            return self.getToken(YarcParser.CAMERA, 0)

        def LIGHT(self):
            return self.getToken(YarcParser.LIGHT, 0)

        def MATERIAL(self):
            return self.getToken(YarcParser.MATERIAL, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_get_expr

    def get_expr(self):
        localctx = YarcParser.Get_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_get_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(YarcParser.GET)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 23, self._ctx)
            if la_ == 1:
                self.state = 281
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.CAMERA]:
                    self.state = 277
                    self.match(YarcParser.CAMERA)
                elif token in [YarcParser.LIGHT]:
                    self.state = 278
                    self.match(YarcParser.LIGHT)
                elif token in [YarcParser.MATERIAL]:
                    self.state = 279
                    self.match(YarcParser.MATERIAL)
                elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                    self.state = 280
                    self.name()
                else:
                    raise NoViableAltException(self)

                self.state = 283
                self.match(YarcParser.AT)

            self.state = 286
            self.test()
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 287
                self.simple_block()
            elif token in [YarcParser.NEWLINE]:
                self.state = 288
                self.match(YarcParser.NEWLINE)
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Edit_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def attr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.AttrContext)
            else:
                return self.getTypedRuleContext(YarcParser.AttrContext, i)

        def inner_behavior_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Inner_behavior_stmtContext)
            else:
                return self.getTypedRuleContext(
                    YarcParser.Inner_behavior_stmtContext, i
                )

        def getRuleIndex(self):
            return YarcParser.RULE_edit_block

    def edit_block(self):
        localctx = YarcParser.Edit_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_edit_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(YarcParser.COLON)
            self.state = 292
            self.match(YarcParser.NEWLINE)
            self.state = 293
            self.match(YarcParser.INDENT)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 296
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.TRANSLATE,
                    YarcParser.CAM_TRANSLATE,
                    YarcParser.ROTATE,
                    YarcParser.SCALE,
                    YarcParser.SEMANTICS,
                    YarcParser.VISIBLE,
                    YarcParser.SIZE,
                    YarcParser.LOOK_AT,
                    YarcParser.UP_AXIS,
                    YarcParser.SCATTER,
                    YarcParser.ROT_AROUND,
                    YarcParser.PHYSICS,
                    YarcParser.UNDERSCORE,
                    YarcParser.ID,
                ]:
                    self.state = 294
                    self.attr()
                elif token in [YarcParser.EVERY]:
                    self.state = 295
                    self.inner_behavior_stmt()
                else:
                    raise NoViableAltException(self)

                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.TRANSLATE)
                                | (1 << YarcParser.CAM_TRANSLATE)
                                | (1 << YarcParser.ROTATE)
                                | (1 << YarcParser.SCALE)
                                | (1 << YarcParser.SEMANTICS)
                                | (1 << YarcParser.VISIBLE)
                                | (1 << YarcParser.SIZE)
                                | (1 << YarcParser.LOOK_AT)
                                | (1 << YarcParser.UP_AXIS)
                                | (1 << YarcParser.SCATTER)
                                | (1 << YarcParser.ROT_AROUND)
                                | (1 << YarcParser.PHYSICS)
                                | (1 << YarcParser.EVERY)
                            )
                        )
                        != 0
                    )
                    or _la == YarcParser.UNDERSCORE
                    or _la == YarcParser.ID
                ):
                    break

            self.state = 300
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def simple_attr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Simple_attrContext)
            else:
                return self.getTypedRuleContext(YarcParser.Simple_attrContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_block

    def simple_block(self):
        localctx = YarcParser.Simple_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_simple_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(YarcParser.COLON)
            self.state = 303
            self.match(YarcParser.NEWLINE)
            self.state = 304
            self.match(YarcParser.INDENT)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 305
                self.simple_attr()
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.UNDERSCORE or _la == YarcParser.ID):
                    break

            self.state = 310
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def core_attr(self):
            return self.getTypedRuleContext(YarcParser.Core_attrContext, 0)

        def simple_attr(self):
            return self.getTypedRuleContext(YarcParser.Simple_attrContext, 0)

        def compound_attr(self):
            return self.getTypedRuleContext(YarcParser.Compound_attrContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_attr

    def attr(self):
        localctx = YarcParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_attr)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.TRANSLATE,
                YarcParser.CAM_TRANSLATE,
                YarcParser.ROTATE,
                YarcParser.SCALE,
                YarcParser.SEMANTICS,
                YarcParser.VISIBLE,
                YarcParser.SIZE,
                YarcParser.LOOK_AT,
                YarcParser.UP_AXIS,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.core_attr()
            elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.simple_attr()
            elif token in [
                YarcParser.SCATTER,
                YarcParser.ROT_AROUND,
                YarcParser.PHYSICS,
            ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.compound_attr()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_attrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext, i)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_attr

    def simple_attr(self):
        localctx = YarcParser.Simple_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_simple_attr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.name()
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 318
                self.match(YarcParser.COLON)
                self.state = 319
                self.name()

            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                    )
                )
                != 0
            ) or (
                ((_la - 64) & ~0x3F) == 0
                and (
                    (1 << (_la - 64))
                    & (
                        (1 << (YarcParser.TRUE - 64))
                        | (1 << (YarcParser.UNDERSCORE - 64))
                        | (1 << (YarcParser.BIT_NOT - 64))
                        | (1 << (YarcParser.PLUS - 64))
                        | (1 << (YarcParser.MINUS - 64))
                        | (1 << (YarcParser.LPAREN - 64))
                        | (1 << (YarcParser.LBRACK - 64))
                        | (1 << (YarcParser.LBRACE - 64))
                        | (1 << (YarcParser.LT - 64))
                        | (1 << (YarcParser.ID - 64))
                        | (1 << (YarcParser.SETTING_ID - 64))
                        | (1 << (YarcParser.STRING - 64))
                        | (1 << (YarcParser.INTEGER - 64))
                        | (1 << (YarcParser.FLOAT_NUMBER - 64))
                    )
                )
                != 0
            ):
                self.state = 322
                self.test()

            self.state = 325
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compound_attrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCATTER(self):
            return self.getToken(YarcParser.SCATTER, 0)

        def ON(self):
            return self.getToken(YarcParser.ON, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def ROT_AROUND(self):
            return self.getToken(YarcParser.ROT_AROUND, 0)

        def PHYSICS(self):
            return self.getToken(YarcParser.PHYSICS, 0)

        def simple_block(self):
            return self.getTypedRuleContext(YarcParser.Simple_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_compound_attr

    def compound_attr(self):
        localctx = YarcParser.Compound_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_compound_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.SCATTER]:
                self.state = 327
                self.match(YarcParser.SCATTER)
                self.state = 328
                self.match(YarcParser.ON)
                self.state = 329
                self.name()
            elif token in [YarcParser.ROT_AROUND]:
                self.state = 330
                self.match(YarcParser.ROT_AROUND)
                self.state = 331
                self.name()
            elif token in [YarcParser.PHYSICS]:
                self.state = 332
                self.match(YarcParser.PHYSICS)
            else:
                raise NoViableAltException(self)

            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 335
                self.simple_block()
            elif token in [YarcParser.NEWLINE]:
                self.state = 336
                self.match(YarcParser.NEWLINE)
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Core_attrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def TRANSLATE(self):
            return self.getToken(YarcParser.TRANSLATE, 0)

        def TO(self):
            return self.getToken(YarcParser.TO, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def CAM_TRANSLATE(self):
            return self.getToken(YarcParser.CAM_TRANSLATE, 0)

        def ROTATE(self):
            return self.getToken(YarcParser.ROTATE, 0)

        def SCALE(self):
            return self.getToken(YarcParser.SCALE, 0)

        def LOOK_AT(self):
            return self.getToken(YarcParser.LOOK_AT, 0)

        def UP_AXIS(self):
            return self.getToken(YarcParser.UP_AXIS, 0)

        def SIZE(self):
            return self.getToken(YarcParser.SIZE, 0)

        def SEMANTICS(self):
            return self.getToken(YarcParser.SEMANTICS, 0)

        def VISIBLE(self):
            return self.getToken(YarcParser.VISIBLE, 0)

        def AXIS(self):
            return self.getToken(YarcParser.AXIS, 0)

        def ORDER(self):
            return self.getToken(YarcParser.ORDER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_core_attr

    def core_attr(self):
        localctx = YarcParser.Core_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_core_attr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.TRANSLATE]:
                self.state = 339
                self.match(YarcParser.TRANSLATE)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.AXIS:
                    self.state = 340
                    self.match(YarcParser.AXIS)

                self.state = 343
                self.match(YarcParser.TO)
                self.state = 344
                self.test()
            elif token in [YarcParser.CAM_TRANSLATE]:
                self.state = 345
                self.match(YarcParser.CAM_TRANSLATE)
                self.state = 346
                self.match(YarcParser.TO)
                self.state = 347
                self.test()
            elif token in [YarcParser.ROTATE]:
                self.state = 348
                self.match(YarcParser.ROTATE)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.AXIS:
                    self.state = 349
                    self.match(YarcParser.AXIS)

                self.state = 352
                self.test()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.ORDER:
                    self.state = 353
                    self.match(YarcParser.ORDER)

            elif token in [YarcParser.SCALE]:
                self.state = 356
                self.match(YarcParser.SCALE)
                self.state = 357
                self.test()
            elif token in [YarcParser.LOOK_AT]:
                self.state = 358
                self.match(YarcParser.LOOK_AT)
                self.state = 359
                self.test()
            elif token in [YarcParser.UP_AXIS]:
                self.state = 360
                self.match(YarcParser.UP_AXIS)
                self.state = 361
                self.test()
            elif token in [YarcParser.SIZE]:
                self.state = 362
                self.match(YarcParser.SIZE)
                self.state = 363
                self.test()
            elif token in [YarcParser.SEMANTICS]:
                self.state = 364
                self.match(YarcParser.SEMANTICS)
                self.state = 365
                self.test()
            elif token in [YarcParser.VISIBLE]:
                self.state = 366
                self.match(YarcParser.VISIBLE)
                self.state = 367
                self.test()
            else:
                raise NoViableAltException(self)

            self.state = 370
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_behavior_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def behavior_expr(self):
            return self.getTypedRuleContext(YarcParser.Behavior_exprContext, 0)

        def inner_behavior_block(self):
            return self.getTypedRuleContext(YarcParser.Inner_behavior_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_inner_behavior_stmt

    def inner_behavior_stmt(self):
        localctx = YarcParser.Inner_behavior_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_inner_behavior_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.behavior_expr()
            self.state = 373
            self.inner_behavior_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_behavior_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def attr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.AttrContext)
            else:
                return self.getTypedRuleContext(YarcParser.AttrContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_inner_behavior_block

    def inner_behavior_block(self):
        localctx = YarcParser.Inner_behavior_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_inner_behavior_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(YarcParser.COLON)
            self.state = 376
            self.match(YarcParser.NEWLINE)
            self.state = 377
            self.match(YarcParser.INDENT)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 378
                self.attr()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.TRANSLATE)
                                | (1 << YarcParser.CAM_TRANSLATE)
                                | (1 << YarcParser.ROTATE)
                                | (1 << YarcParser.SCALE)
                                | (1 << YarcParser.SEMANTICS)
                                | (1 << YarcParser.VISIBLE)
                                | (1 << YarcParser.SIZE)
                                | (1 << YarcParser.LOOK_AT)
                                | (1 << YarcParser.UP_AXIS)
                                | (1 << YarcParser.SCATTER)
                                | (1 << YarcParser.ROT_AROUND)
                                | (1 << YarcParser.PHYSICS)
                            )
                        )
                        != 0
                    )
                    or _la == YarcParser.UNDERSCORE
                    or _la == YarcParser.ID
                ):
                    break

            self.state = 383
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Behavior_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def behavior_expr(self):
            return self.getTypedRuleContext(YarcParser.Behavior_exprContext, 0)

        def behavior_block(self):
            return self.getTypedRuleContext(YarcParser.Behavior_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_stmt

    def behavior_stmt(self):
        localctx = YarcParser.Behavior_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_behavior_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.behavior_expr()
            self.state = 386
            self.behavior_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Behavior_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVERY(self):
            return self.getToken(YarcParser.EVERY, 0)

        def FRAMES(self):
            return self.getToken(YarcParser.FRAMES, 0)

        def TIME(self):
            return self.getToken(YarcParser.TIME, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_expr

    def behavior_expr(self):
        localctx = YarcParser.Behavior_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_behavior_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(YarcParser.EVERY)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                    )
                )
                != 0
            ) or (
                ((_la - 64) & ~0x3F) == 0
                and (
                    (1 << (_la - 64))
                    & (
                        (1 << (YarcParser.TRUE - 64))
                        | (1 << (YarcParser.UNDERSCORE - 64))
                        | (1 << (YarcParser.BIT_NOT - 64))
                        | (1 << (YarcParser.PLUS - 64))
                        | (1 << (YarcParser.MINUS - 64))
                        | (1 << (YarcParser.LPAREN - 64))
                        | (1 << (YarcParser.LBRACK - 64))
                        | (1 << (YarcParser.LBRACE - 64))
                        | (1 << (YarcParser.LT - 64))
                        | (1 << (YarcParser.ID - 64))
                        | (1 << (YarcParser.SETTING_ID - 64))
                        | (1 << (YarcParser.STRING - 64))
                        | (1 << (YarcParser.INTEGER - 64))
                        | (1 << (YarcParser.FLOAT_NUMBER - 64))
                    )
                )
                != 0
            ):
                self.state = 389
                self.test()

            self.state = 392
            _la = self._input.LA(1)
            if not (_la == YarcParser.FRAMES or _la == YarcParser.TIME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Behavior_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def aug_expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Aug_expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Aug_expr_stmtContext, i)

        def edit_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Edit_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Edit_stmtContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_block

    def behavior_block(self):
        localctx = YarcParser.Behavior_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_behavior_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(YarcParser.COLON)
            self.state = 395
            self.match(YarcParser.NEWLINE)
            self.state = 396
            self.match(YarcParser.INDENT)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 399
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.CREATE,
                    YarcParser.GROUP,
                    YarcParser.INSTANTIATE,
                    YarcParser.GET,
                    YarcParser.UNIFORM,
                    YarcParser.NORMAL,
                    YarcParser.CHOICE,
                    YarcParser.SEQUENCE,
                    YarcParser.LOG_UNIFORM,
                    YarcParser.FALSE,
                    YarcParser.NONE,
                    YarcParser.NOT,
                    YarcParser.TRUE,
                    YarcParser.UNDERSCORE,
                    YarcParser.BIT_NOT,
                    YarcParser.PLUS,
                    YarcParser.MINUS,
                    YarcParser.LPAREN,
                    YarcParser.LBRACK,
                    YarcParser.LBRACE,
                    YarcParser.LT,
                    YarcParser.ID,
                    YarcParser.SETTING_ID,
                    YarcParser.STRING,
                    YarcParser.INTEGER,
                    YarcParser.FLOAT_NUMBER,
                ]:
                    self.state = 397
                    self.aug_expr_stmt()
                elif token in [YarcParser.EDIT]:
                    self.state = 398
                    self.edit_stmt()
                else:
                    raise NoViableAltException(self)

                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.CREATE)
                                | (1 << YarcParser.GROUP)
                                | (1 << YarcParser.INSTANTIATE)
                                | (1 << YarcParser.GET)
                                | (1 << YarcParser.EDIT)
                                | (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 64) & ~0x3F) == 0
                        and (
                            (1 << (_la - 64))
                            & (
                                (1 << (YarcParser.TRUE - 64))
                                | (1 << (YarcParser.UNDERSCORE - 64))
                                | (1 << (YarcParser.BIT_NOT - 64))
                                | (1 << (YarcParser.PLUS - 64))
                                | (1 << (YarcParser.MINUS - 64))
                                | (1 << (YarcParser.LPAREN - 64))
                                | (1 << (YarcParser.LBRACK - 64))
                                | (1 << (YarcParser.LBRACE - 64))
                                | (1 << (YarcParser.LT - 64))
                                | (1 << (YarcParser.ID - 64))
                                | (1 << (YarcParser.SETTING_ID - 64))
                                | (1 << (YarcParser.STRING - 64))
                                | (1 << (YarcParser.INTEGER - 64))
                                | (1 << (YarcParser.FLOAT_NUMBER - 64))
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 403
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testlist(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestlistContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestlistContext, i)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def aug_assign(self):
            return self.getTypedRuleContext(YarcParser.Aug_assignContext, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def fetch_expr(self):
            return self.getTypedRuleContext(YarcParser.Fetch_exprContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_expr_stmt

    def expr_stmt(self):
        localctx = YarcParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.testlist()
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.ADD_ASSIGN,
                YarcParser.SUB_ASSIGN,
                YarcParser.MULT_ASSIGN,
                YarcParser.DIV_ASSIGN,
                YarcParser.MOD_ASSIGN,
                YarcParser.AND_ASSIGN,
                YarcParser.OR_ASSIGN,
                YarcParser.XOR_ASSIGN,
                YarcParser.LSHIFT_ASSIGN,
                YarcParser.RSHIFT_ASSIGN,
                YarcParser.POWER_ASSIGN,
                YarcParser.IDIV_ASSIGN,
            ]:
                self.state = 406
                self.aug_assign()
            elif token in [YarcParser.ASSIGN]:
                self.state = 407
                self.match(YarcParser.ASSIGN)
            else:
                raise NoViableAltException(self)

            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.state = 410
                self.testlist()
            elif token in [YarcParser.FETCH]:
                self.state = 411
                self.fetch_expr()
            else:
                raise NoViableAltException(self)

            self.state = 414
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Aug_expr_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testlist(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestlistContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestlistContext, i)

        def aug_assign(self):
            return self.getTypedRuleContext(YarcParser.Aug_assignContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def create_expr(self):
            return self.getTypedRuleContext(YarcParser.Create_exprContext, 0)

        def instantiate_expr(self):
            return self.getTypedRuleContext(YarcParser.Instantiate_exprContext, 0)

        def get_expr(self):
            return self.getTypedRuleContext(YarcParser.Get_exprContext, 0)

        def group_expr(self):
            return self.getTypedRuleContext(YarcParser.Group_exprContext, 0)

        def fetch_expr(self):
            return self.getTypedRuleContext(YarcParser.Fetch_exprContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_aug_expr_stmt

    def aug_expr_stmt(self):
        localctx = YarcParser.Aug_expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_aug_expr_stmt)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.testlist()
                self.state = 437
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.ADD_ASSIGN,
                    YarcParser.SUB_ASSIGN,
                    YarcParser.MULT_ASSIGN,
                    YarcParser.DIV_ASSIGN,
                    YarcParser.MOD_ASSIGN,
                    YarcParser.AND_ASSIGN,
                    YarcParser.OR_ASSIGN,
                    YarcParser.XOR_ASSIGN,
                    YarcParser.LSHIFT_ASSIGN,
                    YarcParser.RSHIFT_ASSIGN,
                    YarcParser.POWER_ASSIGN,
                    YarcParser.IDIV_ASSIGN,
                ]:
                    self.state = 417
                    self.aug_assign()
                    self.state = 420
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [
                        YarcParser.UNIFORM,
                        YarcParser.NORMAL,
                        YarcParser.CHOICE,
                        YarcParser.SEQUENCE,
                        YarcParser.LOG_UNIFORM,
                        YarcParser.FALSE,
                        YarcParser.NONE,
                        YarcParser.NOT,
                        YarcParser.TRUE,
                        YarcParser.UNDERSCORE,
                        YarcParser.BIT_NOT,
                        YarcParser.PLUS,
                        YarcParser.MINUS,
                        YarcParser.LPAREN,
                        YarcParser.LBRACK,
                        YarcParser.LBRACE,
                        YarcParser.LT,
                        YarcParser.ID,
                        YarcParser.SETTING_ID,
                        YarcParser.STRING,
                        YarcParser.INTEGER,
                        YarcParser.FLOAT_NUMBER,
                    ]:
                        self.state = 418
                        self.testlist()
                    elif token in [YarcParser.FETCH]:
                        self.state = 419
                        self.fetch_expr()
                    elif token in [YarcParser.NEWLINE]:
                        pass
                    else:
                        pass
                    self.state = 422
                    self.match(YarcParser.NEWLINE)
                elif token in [YarcParser.ASSIGN]:
                    self.state = 424
                    self.match(YarcParser.ASSIGN)
                    self.state = 435
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [
                        YarcParser.FETCH,
                        YarcParser.UNIFORM,
                        YarcParser.NORMAL,
                        YarcParser.CHOICE,
                        YarcParser.SEQUENCE,
                        YarcParser.LOG_UNIFORM,
                        YarcParser.FALSE,
                        YarcParser.NONE,
                        YarcParser.NOT,
                        YarcParser.TRUE,
                        YarcParser.UNDERSCORE,
                        YarcParser.BIT_NOT,
                        YarcParser.PLUS,
                        YarcParser.MINUS,
                        YarcParser.LPAREN,
                        YarcParser.LBRACK,
                        YarcParser.LBRACE,
                        YarcParser.LT,
                        YarcParser.ID,
                        YarcParser.SETTING_ID,
                        YarcParser.STRING,
                        YarcParser.INTEGER,
                        YarcParser.FLOAT_NUMBER,
                    ]:
                        self.state = 427
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [
                            YarcParser.UNIFORM,
                            YarcParser.NORMAL,
                            YarcParser.CHOICE,
                            YarcParser.SEQUENCE,
                            YarcParser.LOG_UNIFORM,
                            YarcParser.FALSE,
                            YarcParser.NONE,
                            YarcParser.NOT,
                            YarcParser.TRUE,
                            YarcParser.UNDERSCORE,
                            YarcParser.BIT_NOT,
                            YarcParser.PLUS,
                            YarcParser.MINUS,
                            YarcParser.LPAREN,
                            YarcParser.LBRACK,
                            YarcParser.LBRACE,
                            YarcParser.LT,
                            YarcParser.ID,
                            YarcParser.SETTING_ID,
                            YarcParser.STRING,
                            YarcParser.INTEGER,
                            YarcParser.FLOAT_NUMBER,
                        ]:
                            self.state = 425
                            self.testlist()
                        elif token in [YarcParser.FETCH]:
                            self.state = 426
                            self.fetch_expr()
                        else:
                            raise NoViableAltException(self)

                        self.state = 429
                        self.match(YarcParser.NEWLINE)
                    elif token in [YarcParser.CREATE]:
                        self.state = 431
                        self.create_expr()
                    elif token in [YarcParser.INSTANTIATE]:
                        self.state = 432
                        self.instantiate_expr()
                    elif token in [YarcParser.GET]:
                        self.state = 433
                        self.get_expr()
                    elif token in [YarcParser.GROUP]:
                        self.state = 434
                        self.group_expr()
                    else:
                        raise NoViableAltException(self)

                else:
                    raise NoViableAltException(self)

            elif token in [YarcParser.CREATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.create_expr()
            elif token in [YarcParser.INSTANTIATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.instantiate_expr()
            elif token in [YarcParser.GET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 441
                self.get_expr()
            elif token in [YarcParser.GROUP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 442
                self.group_expr()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FETCH(self):
            return self.getToken(YarcParser.FETCH, 0)

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def FROM(self):
            return self.getToken(YarcParser.FROM, 0)

        def MATCH(self):
            return self.getToken(YarcParser.MATCH, 0)

        def LIMIT(self):
            return self.getToken(YarcParser.LIMIT, 0)

        def RECURSIVE(self):
            return self.getToken(YarcParser.RECURSIVE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_fetch_expr

    def fetch_expr(self):
        localctx = YarcParser.Fetch_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_fetch_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(YarcParser.FETCH)
            self.state = 446
            self.test()
            self.state = 447
            self.match(YarcParser.FROM)
            self.state = 448
            self.test()
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.MATCH:
                self.state = 449
                self.match(YarcParser.MATCH)
                self.state = 450
                self.test()

            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.LIMIT:
                self.state = 453
                self.match(YarcParser.LIMIT)
                self.state = 454
                self.test()

            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.RECURSIVE:
                self.state = 457
                self.match(YarcParser.RECURSIVE)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Aug_assignContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_ASSIGN(self):
            return self.getToken(YarcParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(YarcParser.SUB_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(YarcParser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(YarcParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(YarcParser.MOD_ASSIGN, 0)

        def AND_ASSIGN(self):
            return self.getToken(YarcParser.AND_ASSIGN, 0)

        def OR_ASSIGN(self):
            return self.getToken(YarcParser.OR_ASSIGN, 0)

        def XOR_ASSIGN(self):
            return self.getToken(YarcParser.XOR_ASSIGN, 0)

        def LSHIFT_ASSIGN(self):
            return self.getToken(YarcParser.LSHIFT_ASSIGN, 0)

        def RSHIFT_ASSIGN(self):
            return self.getToken(YarcParser.RSHIFT_ASSIGN, 0)

        def POWER_ASSIGN(self):
            return self.getToken(YarcParser.POWER_ASSIGN, 0)

        def IDIV_ASSIGN(self):
            return self.getToken(YarcParser.IDIV_ASSIGN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_aug_assign

    def aug_assign(self):
        localctx = YarcParser.Aug_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_aug_assign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            _la = self._input.LA(1)
            if not (
                ((_la - 98) & ~0x3F) == 0
                and (
                    (1 << (_la - 98))
                    & (
                        (1 << (YarcParser.ADD_ASSIGN - 98))
                        | (1 << (YarcParser.SUB_ASSIGN - 98))
                        | (1 << (YarcParser.MULT_ASSIGN - 98))
                        | (1 << (YarcParser.DIV_ASSIGN - 98))
                        | (1 << (YarcParser.MOD_ASSIGN - 98))
                        | (1 << (YarcParser.AND_ASSIGN - 98))
                        | (1 << (YarcParser.OR_ASSIGN - 98))
                        | (1 << (YarcParser.XOR_ASSIGN - 98))
                        | (1 << (YarcParser.LSHIFT_ASSIGN - 98))
                        | (1 << (YarcParser.RSHIFT_ASSIGN - 98))
                        | (1 << (YarcParser.POWER_ASSIGN - 98))
                        | (1 << (YarcParser.IDIV_ASSIGN - 98))
                    )
                )
                != 0
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TestContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Or_testContext)
            else:
                return self.getTypedRuleContext(YarcParser.Or_testContext, i)

        def IF(self):
            return self.getToken(YarcParser.IF, 0)

        def ELSE(self):
            return self.getToken(YarcParser.ELSE, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_test

    def test(self):
        localctx = YarcParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.or_test()
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.IF:
                self.state = 463
                self.match(YarcParser.IF)
                self.state = 464
                self.or_test()
                self.state = 465
                self.match(YarcParser.ELSE)
                self.state = 466
                self.test()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Test_nocondContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self):
            return self.getTypedRuleContext(YarcParser.Or_testContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_test_nocond

    def test_nocond(self):
        localctx = YarcParser.Test_nocondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_test_nocond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.or_test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_testContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.And_testContext)
            else:
                return self.getTypedRuleContext(YarcParser.And_testContext, i)

        def OR(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.OR)
            else:
                return self.getToken(YarcParser.OR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_or_test

    def or_test(self):
        localctx = YarcParser.Or_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_or_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.and_test()
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.OR:
                self.state = 473
                self.match(YarcParser.OR)
                self.state = 474
                self.and_test()
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_testContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Not_testContext)
            else:
                return self.getTypedRuleContext(YarcParser.Not_testContext, i)

        def AND(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.AND)
            else:
                return self.getToken(YarcParser.AND, i)

        def getRuleIndex(self):
            return YarcParser.RULE_and_test

    def and_test(self):
        localctx = YarcParser.And_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_and_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.not_test()
            self.state = 485
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.AND:
                self.state = 481
                self.match(YarcParser.AND)
                self.state = 482
                self.not_test()
                self.state = 487
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Not_testContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(YarcParser.NOT, 0)

        def not_test(self):
            return self.getTypedRuleContext(YarcParser.Not_testContext, 0)

        def comparison(self):
            return self.getTypedRuleContext(YarcParser.ComparisonContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_not_test

    def not_test(self):
        localctx = YarcParser.Not_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_not_test)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.match(YarcParser.NOT)
                self.state = 489
                self.not_test()
            elif token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.comparison()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.ExprContext)
            else:
                return self.getTypedRuleContext(YarcParser.ExprContext, i)

        def comp_op(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Comp_opContext)
            else:
                return self.getTypedRuleContext(YarcParser.Comp_opContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_comparison

    def comparison(self):
        localctx = YarcParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_comparison)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.expr()
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la - 58) & ~0x3F) == 0 and (
                (1 << (_la - 58))
                & (
                    (1 << (YarcParser.IN - 58))
                    | (1 << (YarcParser.IS - 58))
                    | (1 << (YarcParser.NOT - 58))
                    | (1 << (YarcParser.LT - 58))
                    | (1 << (YarcParser.GT - 58))
                    | (1 << (YarcParser.EQUALS - 58))
                    | (1 << (YarcParser.GT_EQ - 58))
                    | (1 << (YarcParser.LT_EQ - 58))
                    | (1 << (YarcParser.NOT_EQ - 58))
                )
            ) != 0:
                self.state = 494
                self.comp_op()
                self.state = 495
                self.expr()
                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_opContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(YarcParser.LT, 0)

        def GT(self):
            return self.getToken(YarcParser.GT, 0)

        def EQUALS(self):
            return self.getToken(YarcParser.EQUALS, 0)

        def GT_EQ(self):
            return self.getToken(YarcParser.GT_EQ, 0)

        def LT_EQ(self):
            return self.getToken(YarcParser.LT_EQ, 0)

        def NOT_EQ(self):
            return self.getToken(YarcParser.NOT_EQ, 0)

        def IN(self):
            return self.getToken(YarcParser.IN, 0)

        def NOT(self):
            return self.getToken(YarcParser.NOT, 0)

        def IS(self):
            return self.getToken(YarcParser.IS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_comp_op

    def comp_op(self):
        localctx = YarcParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_comp_op)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 56, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.match(YarcParser.LT)

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(YarcParser.GT)

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 504
                self.match(YarcParser.EQUALS)

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 505
                self.match(YarcParser.GT_EQ)

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 506
                self.match(YarcParser.LT_EQ)

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 507
                self.match(YarcParser.NOT_EQ)

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 508
                self.match(YarcParser.IN)

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 509
                self.match(YarcParser.NOT)
                self.state = 510
                self.match(YarcParser.IN)

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 511
                self.match(YarcParser.IS)

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 512
                self.match(YarcParser.IS)
                self.state = 513
                self.match(YarcParser.NOT)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xor_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Xor_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Xor_exprContext, i)

        def BIT_OR(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.BIT_OR)
            else:
                return self.getToken(YarcParser.BIT_OR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_expr

    def expr(self):
        localctx = YarcParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.xor_expr()
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_OR:
                self.state = 517
                self.match(YarcParser.BIT_OR)
                self.state = 518
                self.xor_expr()
                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xor_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.And_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.And_exprContext, i)

        def XOR(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.XOR)
            else:
                return self.getToken(YarcParser.XOR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_xor_expr

    def xor_expr(self):
        localctx = YarcParser.Xor_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_xor_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.and_expr()
            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.XOR:
                self.state = 525
                self.match(YarcParser.XOR)
                self.state = 526
                self.and_expr()
                self.state = 531
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Shift_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Shift_exprContext, i)

        def BIT_AND(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.BIT_AND)
            else:
                return self.getToken(YarcParser.BIT_AND, i)

        def getRuleIndex(self):
            return YarcParser.RULE_and_expr

    def and_expr(self):
        localctx = YarcParser.And_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_and_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.shift_expr()
            self.state = 537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_AND:
                self.state = 533
                self.match(YarcParser.BIT_AND)
                self.state = 534
                self.shift_expr()
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Shift_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Arith_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Arith_exprContext, i)

        def LSHIFT(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.LSHIFT)
            else:
                return self.getToken(YarcParser.LSHIFT, i)

        def RSHIFT(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.RSHIFT)
            else:
                return self.getToken(YarcParser.RSHIFT, i)

        def getRuleIndex(self):
            return YarcParser.RULE_shift_expr

    def shift_expr(self):
        localctx = YarcParser.Shift_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_shift_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.arith_expr()
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT:
                self.state = 541
                _la = self._input.LA(1)
                if not (_la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 542
                self.arith_expr()
                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arith_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TermContext)
            else:
                return self.getTypedRuleContext(YarcParser.TermContext, i)

        def PLUS(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.PLUS)
            else:
                return self.getToken(YarcParser.PLUS, i)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.MINUS)
            else:
                return self.getToken(YarcParser.MINUS, i)

        def getRuleIndex(self):
            return YarcParser.RULE_arith_expr

    def arith_expr(self):
        localctx = YarcParser.Arith_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arith_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.term()
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.PLUS or _la == YarcParser.MINUS:
                self.state = 549
                _la = self._input.LA(1)
                if not (_la == YarcParser.PLUS or _la == YarcParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 550
                self.term()
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.FactorContext)
            else:
                return self.getTypedRuleContext(YarcParser.FactorContext, i)

        def MUL(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.MUL)
            else:
                return self.getToken(YarcParser.MUL, i)

        def DIV(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.DIV)
            else:
                return self.getToken(YarcParser.DIV, i)

        def MOD(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.MOD)
            else:
                return self.getToken(YarcParser.MOD, i)

        def IDIV(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.IDIV)
            else:
                return self.getToken(YarcParser.IDIV, i)

        def getRuleIndex(self):
            return YarcParser.RULE_term

    def term(self):
        localctx = YarcParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_term)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.factor()
            self.state = 561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la - 81) & ~0x3F) == 0 and (
                (1 << (_la - 81))
                & (
                    (1 << (YarcParser.DIV - 81))
                    | (1 << (YarcParser.MUL - 81))
                    | (1 << (YarcParser.MOD - 81))
                    | (1 << (YarcParser.IDIV - 81))
                )
            ) != 0:
                self.state = 557
                _la = self._input.LA(1)
                if not (
                    ((_la - 81) & ~0x3F) == 0
                    and (
                        (1 << (_la - 81))
                        & (
                            (1 << (YarcParser.DIV - 81))
                            | (1 << (YarcParser.MUL - 81))
                            | (1 << (YarcParser.MOD - 81))
                            | (1 << (YarcParser.IDIV - 81))
                        )
                    )
                    != 0
                ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 558
                self.factor()
                self.state = 563
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(YarcParser.FactorContext, 0)

        def PLUS(self):
            return self.getToken(YarcParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(YarcParser.MINUS, 0)

        def BIT_NOT(self):
            return self.getToken(YarcParser.BIT_NOT, 0)

        def power(self):
            return self.getTypedRuleContext(YarcParser.PowerContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_factor

    def factor(self):
        localctx = YarcParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_factor)
        self._la = 0  # Token type
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.BIT_NOT, YarcParser.PLUS, YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                _la = self._input.LA(1)
                if not (
                    ((_la - 76) & ~0x3F) == 0
                    and (
                        (1 << (_la - 76))
                        & (
                            (1 << (YarcParser.BIT_NOT - 76))
                            | (1 << (YarcParser.PLUS - 76))
                            | (1 << (YarcParser.MINUS - 76))
                        )
                    )
                    != 0
                ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 565
                self.factor()
            elif token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.power()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PowerContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_expr(self):
            return self.getTypedRuleContext(YarcParser.Atom_exprContext, 0)

        def POWER(self):
            return self.getToken(YarcParser.POWER, 0)

        def factor(self):
            return self.getTypedRuleContext(YarcParser.FactorContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_power

    def power(self):
        localctx = YarcParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_power)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.atom_expr()
            self.state = 572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.POWER:
                self.state = 570
                self.match(YarcParser.POWER)
                self.state = 571
                self.factor()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(YarcParser.AtomContext, 0)

        def trailer(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TrailerContext)
            else:
                return self.getTypedRuleContext(YarcParser.TrailerContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_atom_expr

    def atom_expr(self):
        localctx = YarcParser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_atom_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.atom()
            self.state = 578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.DOT or _la == YarcParser.LBRACK:
                self.state = 575
                self.trailer()
                self.state = 580
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def RANGE(self):
            return self.getToken(YarcParser.RANGE, 0)

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.INTEGER)
            else:
                return self.getToken(YarcParser.INTEGER, i)

        def testlist_comp(self):
            return self.getTypedRuleContext(YarcParser.Testlist_compContext, 0)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.MINUS)
            else:
                return self.getToken(YarcParser.MINUS, i)

        def LT(self):
            return self.getToken(YarcParser.LT, 0)

        def GT(self):
            return self.getToken(YarcParser.GT, 0)

        def vector_comp(self):
            return self.getTypedRuleContext(YarcParser.Vector_compContext, 0)

        def LBRACE(self):
            return self.getToken(YarcParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YarcParser.RBRACE, 0)

        def dict_or_set_maker(self):
            return self.getTypedRuleContext(YarcParser.Dict_or_set_makerContext, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def SETTING_ID(self):
            return self.getToken(YarcParser.SETTING_ID, 0)

        def distribution_expr(self):
            return self.getTypedRuleContext(YarcParser.Distribution_exprContext, 0)

        def FLOAT_NUMBER(self):
            return self.getToken(YarcParser.FLOAT_NUMBER, 0)

        def STRING(self):
            return self.getToken(YarcParser.STRING, 0)

        def NONE(self):
            return self.getToken(YarcParser.NONE, 0)

        def TRUE(self):
            return self.getToken(YarcParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(YarcParser.FALSE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_atom

    def atom(self):
        localctx = YarcParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_atom)
        self._la = 0  # Token type
        try:
            self.state = 621
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(YarcParser.LPAREN)
                self.state = 582
                self.test()
                self.state = 583
                self.match(YarcParser.RPAREN)
            elif token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
                self.match(YarcParser.LBRACK)
                self.state = 599
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 69, self._ctx)
                if la_ == 1:
                    self.state = 587
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                            )
                        )
                        != 0
                    ) or (
                        ((_la - 64) & ~0x3F) == 0
                        and (
                            (1 << (_la - 64))
                            & (
                                (1 << (YarcParser.TRUE - 64))
                                | (1 << (YarcParser.UNDERSCORE - 64))
                                | (1 << (YarcParser.BIT_NOT - 64))
                                | (1 << (YarcParser.PLUS - 64))
                                | (1 << (YarcParser.MINUS - 64))
                                | (1 << (YarcParser.LPAREN - 64))
                                | (1 << (YarcParser.LBRACK - 64))
                                | (1 << (YarcParser.LBRACE - 64))
                                | (1 << (YarcParser.LT - 64))
                                | (1 << (YarcParser.ID - 64))
                                | (1 << (YarcParser.SETTING_ID - 64))
                                | (1 << (YarcParser.STRING - 64))
                                | (1 << (YarcParser.INTEGER - 64))
                                | (1 << (YarcParser.FLOAT_NUMBER - 64))
                            )
                        )
                        != 0
                    ):
                        self.state = 586
                        self.testlist_comp()

                elif la_ == 2:
                    self.state = 590
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.MINUS:
                        self.state = 589
                        self.match(YarcParser.MINUS)

                    self.state = 592
                    self.match(YarcParser.INTEGER)
                    self.state = 594
                    self.match(YarcParser.RANGE)

                    self.state = 596
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.MINUS:
                        self.state = 595
                        self.match(YarcParser.MINUS)

                    self.state = 598
                    self.match(YarcParser.INTEGER)

                self.state = 601
                self.match(YarcParser.RBRACK)
            elif token in [YarcParser.LT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 602
                self.match(YarcParser.LT)
                self.state = 604
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.UNIFORM)
                            | (1 << YarcParser.NORMAL)
                            | (1 << YarcParser.CHOICE)
                            | (1 << YarcParser.SEQUENCE)
                            | (1 << YarcParser.LOG_UNIFORM)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 64) & ~0x3F) == 0
                    and (
                        (1 << (_la - 64))
                        & (
                            (1 << (YarcParser.TRUE - 64))
                            | (1 << (YarcParser.UNDERSCORE - 64))
                            | (1 << (YarcParser.BIT_NOT - 64))
                            | (1 << (YarcParser.PLUS - 64))
                            | (1 << (YarcParser.MINUS - 64))
                            | (1 << (YarcParser.LPAREN - 64))
                            | (1 << (YarcParser.LBRACK - 64))
                            | (1 << (YarcParser.LBRACE - 64))
                            | (1 << (YarcParser.LT - 64))
                            | (1 << (YarcParser.ID - 64))
                            | (1 << (YarcParser.SETTING_ID - 64))
                            | (1 << (YarcParser.STRING - 64))
                            | (1 << (YarcParser.INTEGER - 64))
                            | (1 << (YarcParser.FLOAT_NUMBER - 64))
                        )
                    )
                    != 0
                ):
                    self.state = 603
                    self.vector_comp()

                self.state = 606
                self.match(YarcParser.GT)
            elif token in [YarcParser.LBRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 607
                self.match(YarcParser.LBRACE)
                self.state = 609
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.UNIFORM)
                            | (1 << YarcParser.NORMAL)
                            | (1 << YarcParser.CHOICE)
                            | (1 << YarcParser.SEQUENCE)
                            | (1 << YarcParser.LOG_UNIFORM)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 64) & ~0x3F) == 0
                    and (
                        (1 << (_la - 64))
                        & (
                            (1 << (YarcParser.TRUE - 64))
                            | (1 << (YarcParser.UNDERSCORE - 64))
                            | (1 << (YarcParser.BIT_NOT - 64))
                            | (1 << (YarcParser.PLUS - 64))
                            | (1 << (YarcParser.MINUS - 64))
                            | (1 << (YarcParser.LPAREN - 64))
                            | (1 << (YarcParser.LBRACK - 64))
                            | (1 << (YarcParser.LBRACE - 64))
                            | (1 << (YarcParser.LT - 64))
                            | (1 << (YarcParser.ID - 64))
                            | (1 << (YarcParser.SETTING_ID - 64))
                            | (1 << (YarcParser.STRING - 64))
                            | (1 << (YarcParser.INTEGER - 64))
                            | (1 << (YarcParser.FLOAT_NUMBER - 64))
                        )
                    )
                    != 0
                ):
                    self.state = 608
                    self.dict_or_set_maker()

                self.state = 611
                self.match(YarcParser.RBRACE)
            elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 612
                self.name()
            elif token in [YarcParser.SETTING_ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 613
                self.match(YarcParser.SETTING_ID)
            elif token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
            ]:
                self.enterOuterAlt(localctx, 7)
                self.state = 614
                self.distribution_expr()
            elif token in [YarcParser.INTEGER]:
                self.enterOuterAlt(localctx, 8)
                self.state = 615
                self.match(YarcParser.INTEGER)
            elif token in [YarcParser.FLOAT_NUMBER]:
                self.enterOuterAlt(localctx, 9)
                self.state = 616
                self.match(YarcParser.FLOAT_NUMBER)
            elif token in [YarcParser.STRING]:
                self.enterOuterAlt(localctx, 10)
                self.state = 617
                self.match(YarcParser.STRING)
            elif token in [YarcParser.NONE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 618
                self.match(YarcParser.NONE)
            elif token in [YarcParser.TRUE]:
                self.enterOuterAlt(localctx, 12)
                self.state = 619
                self.match(YarcParser.TRUE)
            elif token in [YarcParser.FALSE]:
                self.enterOuterAlt(localctx, 13)
                self.state = 620
                self.match(YarcParser.FALSE)
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YarcParser.ID, 0)

        def UNDERSCORE(self):
            return self.getToken(YarcParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_name

    def name(self):
        localctx = YarcParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            _la = self._input.LA(1)
            if not (_la == YarcParser.UNDERSCORE or _la == YarcParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Distribution_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distribution(self):
            return self.getTypedRuleContext(YarcParser.DistributionContext, 0)

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(YarcParser.ArglistContext, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_distribution_expr

    def distribution_expr(self):
        localctx = YarcParser.Distribution_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_distribution_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.distribution()
            self.state = 626
            self.match(YarcParser.LPAREN)
            self.state = 627
            self.arglist()
            self.state = 628
            self.match(YarcParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DistributionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIFORM(self):
            return self.getToken(YarcParser.UNIFORM, 0)

        def NORMAL(self):
            return self.getToken(YarcParser.NORMAL, 0)

        def CHOICE(self):
            return self.getToken(YarcParser.CHOICE, 0)

        def SEQUENCE(self):
            return self.getToken(YarcParser.SEQUENCE, 0)

        def LOG_UNIFORM(self):
            return self.getToken(YarcParser.LOG_UNIFORM, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_distribution

    def distribution(self):
        localctx = YarcParser.DistributionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_distribution)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            _la = self._input.LA(1)
            if not (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                    )
                )
                != 0
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Testlist_compContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def comp_for(self):
            return self.getTypedRuleContext(YarcParser.Comp_forContext, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_testlist_comp

    def testlist_comp(self):
        localctx = YarcParser.Testlist_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_testlist_comp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.test()
            self.state = 641
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.state = 633
                self.comp_for()
            elif token in [YarcParser.COMMA, YarcParser.RBRACK]:
                self.state = 638
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == YarcParser.COMMA:
                    self.state = 634
                    self.match(YarcParser.COMMA)
                    self.state = 635
                    self.test()
                    self.state = 640
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vector_compContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.ExprContext)
            else:
                return self.getTypedRuleContext(YarcParser.ExprContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_vector_comp

    def vector_comp(self):
        localctx = YarcParser.Vector_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_vector_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.expr()
            self.state = 644
            self.match(YarcParser.COMMA)
            self.state = 645
            self.expr()
            self.state = 646
            self.match(YarcParser.COMMA)
            self.state = 647
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrailerContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def subscriptlist(self):
            return self.getTypedRuleContext(YarcParser.SubscriptlistContext, 0)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(YarcParser.DOT, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_trailer

    def trailer(self):
        localctx = YarcParser.TrailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_trailer)
        try:
            self.state = 655
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 649
                self.match(YarcParser.LBRACK)
                self.state = 650
                self.subscriptlist()
                self.state = 651
                self.match(YarcParser.RBRACK)
            elif token in [YarcParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 653
                self.match(YarcParser.DOT)
                self.state = 654
                self.name()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArglistContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(YarcParser.ArgumentContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_arglist

    def arglist(self):
        localctx = YarcParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arglist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.argument()
            self.state = 662
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 658
                self.match(YarcParser.COMMA)
                self.state = 659
                self.argument()
                self.state = 664
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def comp_for(self):
            return self.getTypedRuleContext(YarcParser.Comp_forContext, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_argument

    def argument(self):
        localctx = YarcParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.test()
            self.state = 669
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.state = 666
                self.comp_for()
            elif token in [YarcParser.ASSIGN]:
                self.state = 667
                self.match(YarcParser.ASSIGN)
                self.state = 668
                self.test()
            elif token in [YarcParser.COMMA, YarcParser.RPAREN]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptlistContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subscript_(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Subscript_Context)
            else:
                return self.getTypedRuleContext(YarcParser.Subscript_Context, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_subscriptlist

    def subscriptlist(self):
        localctx = YarcParser.SubscriptlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_subscriptlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
            self.subscript_()
            self.state = 676
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 672
                self.match(YarcParser.COMMA)
                self.state = 673
                self.subscript_()
                self.state = 678
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Subscript_Context(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def sliceop(self):
            return self.getTypedRuleContext(YarcParser.SliceopContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_subscript_

    def subscript_(self):
        localctx = YarcParser.Subscript_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_subscript_)
        self._la = 0  # Token type
        try:
            self.state = 696
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
                self.test()
                self.state = 687
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COLON:
                    self.state = 680
                    self.match(YarcParser.COLON)
                    self.state = 682
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                            )
                        )
                        != 0
                    ) or (
                        ((_la - 64) & ~0x3F) == 0
                        and (
                            (1 << (_la - 64))
                            & (
                                (1 << (YarcParser.TRUE - 64))
                                | (1 << (YarcParser.UNDERSCORE - 64))
                                | (1 << (YarcParser.BIT_NOT - 64))
                                | (1 << (YarcParser.PLUS - 64))
                                | (1 << (YarcParser.MINUS - 64))
                                | (1 << (YarcParser.LPAREN - 64))
                                | (1 << (YarcParser.LBRACK - 64))
                                | (1 << (YarcParser.LBRACE - 64))
                                | (1 << (YarcParser.LT - 64))
                                | (1 << (YarcParser.ID - 64))
                                | (1 << (YarcParser.SETTING_ID - 64))
                                | (1 << (YarcParser.STRING - 64))
                                | (1 << (YarcParser.INTEGER - 64))
                                | (1 << (YarcParser.FLOAT_NUMBER - 64))
                            )
                        )
                        != 0
                    ):
                        self.state = 681
                        self.test()

                    self.state = 685
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.COLON:
                        self.state = 684
                        self.sliceop()

            elif token in [YarcParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 689
                self.match(YarcParser.COLON)
                self.state = 691
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.UNIFORM)
                            | (1 << YarcParser.NORMAL)
                            | (1 << YarcParser.CHOICE)
                            | (1 << YarcParser.SEQUENCE)
                            | (1 << YarcParser.LOG_UNIFORM)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 64) & ~0x3F) == 0
                    and (
                        (1 << (_la - 64))
                        & (
                            (1 << (YarcParser.TRUE - 64))
                            | (1 << (YarcParser.UNDERSCORE - 64))
                            | (1 << (YarcParser.BIT_NOT - 64))
                            | (1 << (YarcParser.PLUS - 64))
                            | (1 << (YarcParser.MINUS - 64))
                            | (1 << (YarcParser.LPAREN - 64))
                            | (1 << (YarcParser.LBRACK - 64))
                            | (1 << (YarcParser.LBRACE - 64))
                            | (1 << (YarcParser.LT - 64))
                            | (1 << (YarcParser.ID - 64))
                            | (1 << (YarcParser.SETTING_ID - 64))
                            | (1 << (YarcParser.STRING - 64))
                            | (1 << (YarcParser.INTEGER - 64))
                            | (1 << (YarcParser.FLOAT_NUMBER - 64))
                        )
                    )
                    != 0
                ):
                    self.state = 690
                    self.test()

                self.state = 694
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COLON:
                    self.state = 693
                    self.sliceop()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SliceopContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_sliceop

    def sliceop(self):
        localctx = YarcParser.SliceopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_sliceop)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.match(YarcParser.COLON)
            self.state = 700
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                    )
                )
                != 0
            ) or (
                ((_la - 64) & ~0x3F) == 0
                and (
                    (1 << (_la - 64))
                    & (
                        (1 << (YarcParser.TRUE - 64))
                        | (1 << (YarcParser.UNDERSCORE - 64))
                        | (1 << (YarcParser.BIT_NOT - 64))
                        | (1 << (YarcParser.PLUS - 64))
                        | (1 << (YarcParser.MINUS - 64))
                        | (1 << (YarcParser.LPAREN - 64))
                        | (1 << (YarcParser.LBRACK - 64))
                        | (1 << (YarcParser.LBRACE - 64))
                        | (1 << (YarcParser.LT - 64))
                        | (1 << (YarcParser.ID - 64))
                        | (1 << (YarcParser.SETTING_ID - 64))
                        | (1 << (YarcParser.STRING - 64))
                        | (1 << (YarcParser.INTEGER - 64))
                        | (1 << (YarcParser.FLOAT_NUMBER - 64))
                    )
                )
                != 0
            ):
                self.state = 699
                self.test()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprlistContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.ExprContext)
            else:
                return self.getTypedRuleContext(YarcParser.ExprContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_exprlist

    def exprlist(self):
        localctx = YarcParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_exprlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.expr()
            self.state = 707
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 703
                self.match(YarcParser.COMMA)
                self.state = 704
                self.expr()
                self.state = 709
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TestlistContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_testlist

    def testlist(self):
        localctx = YarcParser.TestlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_testlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
            self.test()
            self.state = 715
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 711
                self.match(YarcParser.COMMA)
                self.state = 712
                self.test()
                self.state = 717
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_or_set_makerContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def COLON(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COLON)
            else:
                return self.getToken(YarcParser.COLON, i)

        def comp_for(self):
            return self.getTypedRuleContext(YarcParser.Comp_forContext, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_dict_or_set_maker

    def dict_or_set_maker(self):
        localctx = YarcParser.Dict_or_set_makerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_dict_or_set_maker)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
            self.test()
            self.state = 744
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 719
                self.match(YarcParser.COLON)
                self.state = 720
                self.test()
                self.state = 732
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 721
                    self.comp_for()
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 729
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == YarcParser.COMMA:
                        self.state = 722
                        self.match(YarcParser.COMMA)
                        self.state = 723
                        self.test()
                        self.state = 724
                        self.match(YarcParser.COLON)
                        self.state = 725
                        self.test()
                        self.state = 731
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                else:
                    raise NoViableAltException(self)

            elif token in [YarcParser.FOR, YarcParser.COMMA, YarcParser.RBRACE]:
                self.state = 742
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 734
                    self.comp_for()
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 739
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == YarcParser.COMMA:
                        self.state = 735
                        self.match(YarcParser.COMMA)
                        self.state = 736
                        self.test()
                        self.state = 741
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                else:
                    raise NoViableAltException(self)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_iterContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp_for(self):
            return self.getTypedRuleContext(YarcParser.Comp_forContext, 0)

        def comp_if(self):
            return self.getTypedRuleContext(YarcParser.Comp_ifContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_comp_iter

    def comp_iter(self):
        localctx = YarcParser.Comp_iterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_comp_iter)
        try:
            self.state = 748
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 746
                self.comp_for()
            elif token in [YarcParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 747
                self.comp_if()
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_forContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(YarcParser.FOR, 0)

        def exprlist(self):
            return self.getTypedRuleContext(YarcParser.ExprlistContext, 0)

        def IN(self):
            return self.getToken(YarcParser.IN, 0)

        def or_test(self):
            return self.getTypedRuleContext(YarcParser.Or_testContext, 0)

        def comp_iter(self):
            return self.getTypedRuleContext(YarcParser.Comp_iterContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_comp_for

    def comp_for(self):
        localctx = YarcParser.Comp_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_comp_for)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            self.match(YarcParser.FOR)
            self.state = 751
            self.exprlist()
            self.state = 752
            self.match(YarcParser.IN)
            self.state = 753
            self.or_test()
            self.state = 755
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 754
                self.comp_iter()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_ifContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(YarcParser.IF, 0)

        def test_nocond(self):
            return self.getTypedRuleContext(YarcParser.Test_nocondContext, 0)

        def comp_iter(self):
            return self.getTypedRuleContext(YarcParser.Comp_iterContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_comp_if

    def comp_if(self):
        localctx = YarcParser.Comp_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_comp_if)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.match(YarcParser.IF)
            self.state = 758
            self.test_nocond()
            self.state = 760
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 759
                self.comp_iter()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
