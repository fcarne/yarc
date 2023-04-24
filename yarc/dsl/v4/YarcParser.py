# Generated from c:\Users\feder\Desktop\University\Magistrale\Secondo_Anno\1_Linguaggi\Progetto\yarc\yarc\dsl\v4\YarcParser.g4 by ANTLR 4.9.2
import sys
from io import StringIO

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

if __name__ is not None and "." in __name__:
    from .YarcParserBase import YarcParserBase
else:
    from YarcParserBase import YarcParserBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3x")
        buf.write("\u02df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write('\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%\4&\t')
        buf.write("&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0092\n")
        buf.write("\4\f\4\16\4\u0095\13\4\3\5\5\5\u0098\n\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\7\5\u009f\n\5\f\5\16\5\u00a2\13\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\6\6\u00a9\n\6\r\6\16\6\u00aa\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u00b5\n\7\3\b\3\b\3\b\3\b\3\b\3\b\6")
        buf.write("\b\u00bd\n\b\r\b\16\b\u00be\3\b\3\b\5\b\u00c3\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u00d1")
        buf.write("\n\13\3\13\3\13\3\13\3\13\5\13\u00d7\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\5\r\u00df\n\r\3\r\3\r\5\r\u00e3\n\r\3\16")
        buf.write("\3\16\5\16\u00e7\n\16\3\16\3\16\5\16\u00eb\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\7\17\u00f2\n\17\f\17\16\17\u00f5\13")
        buf.write("\17\3\17\5\17\u00f8\n\17\3\17\3\17\5\17\u00fc\n\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\6\20\u0106\n\20\r")
        buf.write("\20\16\20\u0107\3\20\3\20\5\20\u010c\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\6\21\u0113\n\21\r\21\16\21\u0114\3\21\3")
        buf.write("\21\3\22\3\22\3\22\5\22\u011c\n\22\3\23\3\23\5\23\u0120")
        buf.write("\n\23\3\24\3\24\3\24\5\24\u0125\n\24\3\24\5\24\u0128\n")
        buf.write("\24\3\24\3\24\3\25\3\25\3\26\3\26\5\26\u0130\n\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u013a\n\26\3")
        buf.write("\26\3\26\5\26\u013e\n\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u014a\n\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\6\30\u0155\n\30\r\30\16\30")
        buf.write("\u0156\3\30\3\30\3\31\3\31\5\31\u015d\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\34\3\34\5\34\u0168\n\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\6\35\u0173\n")
        buf.write("\35\r\35\16\35\u0174\3\35\3\35\3\36\3\36\3\36\5\36\u017c")
        buf.write("\n\36\3\36\3\36\5\36\u0180\n\36\3\36\3\36\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u018c\n \3!\3!\3!\3!\3!\3!\5!\u0194")
        buf.write('\n!\3"\3"\3#\3#\3#\7#\u019b\n#\f#\16#\u019e\13#\3$\3')
        buf.write("$\3$\7$\u01a3\n$\f$\16$\u01a6\13$\3%\3%\3%\5%\u01ab\n")
        buf.write("%\3&\3&\3&\3&\7&\u01b1\n&\f&\16&\u01b4\13&\3'\3'\3'")
        buf.write("\3'\3'\3'\3'\3'\3'\3'\3'\3'\5'\u01c2\n'\3(")
        buf.write("\3(\3(\7(\u01c7\n(\f(\16(\u01ca\13(\3)\3)\3)\7)\u01cf")
        buf.write("\n)\f)\16)\u01d2\13)\3*\3*\3*\7*\u01d7\n*\f*\16*\u01da")
        buf.write("\13*\3+\3+\3+\7+\u01df\n+\f+\16+\u01e2\13+\3,\3,\3,\7")
        buf.write(",\u01e7\n,\f,\16,\u01ea\13,\3-\3-\3-\7-\u01ef\n-\f-\16")
        buf.write("-\u01f2\13-\3.\3.\3.\5.\u01f7\n.\3/\3/\3/\5/\u01fc\n/")
        buf.write("\3\60\3\60\7\60\u0200\n\60\f\60\16\60\u0203\13\60\3\61")
        buf.write("\3\61\5\61\u0207\n\61\3\61\3\61\3\61\5\61\u020c\n\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0217")
        buf.write("\n\61\3\61\3\61\3\61\5\61\u021c\n\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\5\61\u0225\n\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0231\n\62\3\63\3")
        buf.write("\63\5\63\u0235\n\63\3\63\3\63\3\63\5\63\u023a\n\63\3\64")
        buf.write("\3\64\3\64\5\64\u023f\n\64\3\65\3\65\3\65\3\65\7\65\u0245")
        buf.write("\n\65\f\65\16\65\u0248\13\65\3\65\5\65\u024b\n\65\5\65")
        buf.write("\u024d\n\65\3\66\3\66\3\66\3\66\7\66\u0253\n\66\f\66\16")
        buf.write("\66\u0256\13\66\3\66\5\66\u0259\n\66\5\66\u025b\n\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\5\67\u0263\n\67\38\38\38")
        buf.write("\78\u0268\n8\f8\168\u026b\138\38\58\u026e\n8\39\39\59")
        buf.write("\u0272\n9\39\39\39\39\59\u0278\n9\3:\3:\3:\7:\u027d\n")
        buf.write(":\f:\16:\u0280\13:\3:\5:\u0283\n:\3;\3;\5;\u0287\n;\3")
        buf.write(";\3;\5;\u028b\n;\3;\5;\u028e\n;\5;\u0290\n;\3<\3<\5<\u0294")
        buf.write("\n<\3=\3=\3=\7=\u0299\n=\f=\16=\u029c\13=\3=\5=\u029f")
        buf.write("\n=\3>\3>\3>\7>\u02a4\n>\f>\16>\u02a7\13>\3>\5>\u02aa")
        buf.write("\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\7?\u02b5\n?\f?\16?\u02b8")
        buf.write("\13?\3?\5?\u02bb\n?\5?\u02bd\n?\3?\3?\3?\3?\7?\u02c3\n")
        buf.write("?\f?\16?\u02c6\13?\3?\5?\u02c9\n?\5?\u02cb\n?\5?\u02cd")
        buf.write("\n?\3@\3@\5@\u02d1\n@\3A\3A\3A\3A\3A\5A\u02d8\nA\3B\3")
        buf.write("B\3B\5B\u02dd\nB\3B\2\2C\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write('\32\34\36 "$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b')
        buf.write("dfhjlnprtvxz|~\u0080\u0082\2\t\3\2(,\3\2&'\3\2_j\3\2")
        buf.write("JK\3\2LM\3\2NQ\4\2IILM\2\u0325\2\u0084\3\2\2\2\4\u0089")
        buf.write("\3\2\2\2\6\u0093\3\2\2\2\b\u0097\3\2\2\2\n\u00a3\3\2\2")
        buf.write("\2\f\u00b4\3\2\2\2\16\u00b6\3\2\2\2\20\u00c4\3\2\2\2\22")
        buf.write("\u00c9\3\2\2\2\24\u00d0\3\2\2\2\26\u00d8\3\2\2\2\30\u00dc")
        buf.write("\3\2\2\2\32\u00e4\3\2\2\2\34\u00ec\3\2\2\2\36\u00fd\3")
        buf.write('\2\2\2 \u010d\3\2\2\2"\u011b\3\2\2\2$\u011f\3\2\2\2&')
        buf.write("\u0121\3\2\2\2(\u012b\3\2\2\2*\u0149\3\2\2\2,\u014d\3")
        buf.write("\2\2\2.\u0150\3\2\2\2\60\u015c\3\2\2\2\62\u015e\3\2\2")
        buf.write("\2\64\u0163\3\2\2\2\66\u0165\3\2\2\28\u016c\3\2\2\2:\u0178")
        buf.write("\3\2\2\2<\u0183\3\2\2\2>\u0185\3\2\2\2@\u018d\3\2\2\2")
        buf.write("B\u0195\3\2\2\2D\u0197\3\2\2\2F\u019f\3\2\2\2H\u01aa\3")
        buf.write("\2\2\2J\u01ac\3\2\2\2L\u01c1\3\2\2\2N\u01c3\3\2\2\2P\u01cb")
        buf.write("\3\2\2\2R\u01d3\3\2\2\2T\u01db\3\2\2\2V\u01e3\3\2\2\2")
        buf.write("X\u01eb\3\2\2\2Z\u01f6\3\2\2\2\\\u01f8\3\2\2\2^\u01fd")
        buf.write("\3\2\2\2`\u0224\3\2\2\2b\u0230\3\2\2\2d\u0239\3\2\2\2")
        buf.write("f\u023e\3\2\2\2h\u0240\3\2\2\2j\u024e\3\2\2\2l\u0262\3")
        buf.write("\2\2\2n\u0264\3\2\2\2p\u0277\3\2\2\2r\u0279\3\2\2\2t\u028f")
        buf.write("\3\2\2\2v\u0291\3\2\2\2x\u0295\3\2\2\2z\u02a0\3\2\2\2")
        buf.write("|\u02cc\3\2\2\2~\u02d0\3\2\2\2\u0080\u02d2\3\2\2\2\u0082")
        buf.write("\u02d9\3\2\2\2\u0084\u0085\5\4\3\2\u0085\u0086\5\6\4\2")
        buf.write("\u0086\u0087\5\b\5\2\u0087\u0088\7\2\2\3\u0088\3\3\2\2")
        buf.write("\2\u0089\u008a\7\5\2\2\u008a\u008b\5b\62\2\u008b\u008c")
        buf.write("\7v\2\2\u008c\5\3\2\2\2\u008d\u0092\5\n\6\2\u008e\u0092")
        buf.write("\5:\36\2\u008f\u0092\5\16\b\2\u0090\u0092\7v\2\2\u0091")
        buf.write("\u008d\3\2\2\2\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\7\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0096\u0098\5\22\n\2\u0097\u0096\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u00a0\3\2\2\2\u0099\u009f\5\24\13")
        buf.write("\2\u009a\u009f\5\26\f\2\u009b\u009f\5\66\34\2\u009c\u009f")
        buf.write("\5:\36\2\u009d\u009f\7v\2\2\u009e\u0099\3\2\2\2\u009e")
        buf.write("\u009a\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009d\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3")
        buf.write("\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\t\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a3\u00a4\7\6\2\2\u00a4\u00a5\7C\2\2\u00a5")
        buf.write("\u00a6\7v\2\2\u00a6\u00a8\7\3\2\2\u00a7\u00a9\5\f\7\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad")
        buf.write("\7\4\2\2\u00ad\13\3\2\2\2\u00ae\u00af\7\b\2\2\u00af\u00b0")
        buf.write("\7E\2\2\u00b0\u00b1\5@!\2\u00b1\u00b2\7v\2\2\u00b2\u00b5")
        buf.write("\3\2\2\2\u00b3\u00b5\5\20\t\2\u00b4\u00ae\3\2\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\r\3\2\2\2\u00b6\u00b7\7\7\2\2\u00b7")
        buf.write("\u00c2\7k\2\2\u00b8\u00b9\7C\2\2\u00b9\u00ba\7v\2\2\u00ba")
        buf.write("\u00bc\7\3\2\2\u00bb\u00bd\5\20\t\2\u00bc\u00bb\3\2\2")
        buf.write("\2\u00bd\u00be\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\7\4\2\2\u00c1")
        buf.write("\u00c3\3\2\2\2\u00c2\u00b8\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\17\3\2\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7E\2")
        buf.write("\2\u00c6\u00c7\5@!\2\u00c7\u00c8\7v\2\2\u00c8\21\3\2\2")
        buf.write("\2\u00c9\u00ca\7\17\2\2\u00ca\u00cb\5@!\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\23\3\2\2\2\u00cd\u00ce\5b\62\2\u00ce\u00cf")
        buf.write("\7E\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00cd\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00d6\3\2\2\2\u00d2\u00d7\5\30\r")
        buf.write("\2\u00d3\u00d7\5\32\16\2\u00d4\u00d7\5\36\20\2\u00d5\u00d7")
        buf.write("\5\34\17\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\25\3\2\2\2\u00d8")
        buf.write("\u00d9\7\24\2\2\u00d9\u00da\5b\62\2\u00da\u00db\5 \21")
        buf.write("\2\u00db\27\3\2\2\2\u00dc\u00de\7\20\2\2\u00dd\u00df\5")
        buf.write("@!\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e2\5@!\2\u00e1\u00e3\5 \21\2\u00e2\u00e1")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\31\3\2\2\2\u00e4\u00e6")
        buf.write("\7\22\2\2\u00e5\u00e7\5\60\31\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\5@!\2\u00e9")
        buf.write("\u00eb\5 \21\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\33\3\2\2\2\u00ec\u00ed\7\21\2\2\u00ed\u00ee\7U")
        buf.write("\2\2\u00ee\u00f3\5b\62\2\u00ef\u00f0\7B\2\2\u00f0\u00f2")
        buf.write("\5b\62\2\u00f1\u00ef\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f7\3\2\2\2")
        buf.write("\u00f5\u00f3\3\2\2\2\u00f6\u00f8\7B\2\2\u00f7\u00f6\3")
        buf.write("\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb")
        buf.write("\7V\2\2\u00fa\u00fc\5 \21\2\u00fb\u00fa\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\35\3\2\2\2\u00fd\u00fe\7\23\2\2\u00fe")
        buf.write("\u00ff\5b\62\2\u00ff\u0100\7\60\2\2\u0100\u010b\5@!\2")
        buf.write("\u0101\u0102\7C\2\2\u0102\u0103\7v\2\2\u0103\u0105\7\3")
        buf.write("\2\2\u0104\u0106\5$\23\2\u0105\u0104\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010a\7\4\2\2\u010a\u010c\3\2\2\2")
        buf.write("\u010b\u0101\3\2\2\2\u010b\u010c\3\2\2\2\u010c\37\3\2")
        buf.write("\2\2\u010d\u010e\7C\2\2\u010e\u010f\7v\2\2\u010f\u0112")
        buf.write('\7\3\2\2\u0110\u0113\5"\22\2\u0111\u0113\5,\27\2\u0112')
        buf.write("\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3")
        buf.write("\2\2\2\u0116\u0117\7\4\2\2\u0117!\3\2\2\2\u0118\u011c")
        buf.write("\5$\23\2\u0119\u011c\5(\25\2\u011a\u011c\5*\26\2\u011b")
        buf.write("\u0118\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c#\3\2\2\2\u011d\u0120\5:\36\2\u011e\u0120\5&\24")
        buf.write("\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120%\3\2")
        buf.write("\2\2\u0121\u0124\5b\62\2\u0122\u0123\7C\2\2\u0123\u0125")
        buf.write("\5b\62\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0127\3\2\2\2\u0126\u0128\5\60\31\2\u0127\u0126\3\2\2")
        buf.write("\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a")
        buf.write("\7v\2\2\u012a'\3\2\2\2\u012b\u012c\7!\2\2\u012c)\3\2")
        buf.write("\2\2\u012d\u012f\7\27\2\2\u012e\u0130\7\37\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u0132\7.\2\2\u0132\u014a\5\60\31\2\u0133\u0134\7\n\2")
        buf.write("\2\u0134\u0135\7\27\2\2\u0135\u0136\7.\2\2\u0136\u014a")
        buf.write("\5\60\31\2\u0137\u0139\7\30\2\2\u0138\u013a\7\37\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013d\5\60\31\2\u013c\u013e\7 \2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u014a\3\2\2\2\u013f")
        buf.write("\u0140\7\31\2\2\u0140\u014a\5\60\31\2\u0141\u0142\7\35")
        buf.write("\2\2\u0142\u014a\5\60\31\2\u0143\u0144\7\34\2\2\u0144")
        buf.write("\u014a\5\60\31\2\u0145\u0146\7\32\2\2\u0146\u014a\5\60")
        buf.write("\31\2\u0147\u0148\7\33\2\2\u0148\u014a\5\60\31\2\u0149")
        buf.write("\u012d\3\2\2\2\u0149\u0133\3\2\2\2\u0149\u0137\3\2\2\2")
        buf.write("\u0149\u013f\3\2\2\2\u0149\u0141\3\2\2\2\u0149\u0143\3")
        buf.write("\2\2\2\u0149\u0145\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\u014c\7v\2\2\u014c+\3\2\2\2\u014d\u014e")
        buf.write("\5\66\34\2\u014e\u014f\5.\30\2\u014f-\3\2\2\2\u0150\u0151")
        buf.write("\7C\2\2\u0151\u0152\7v\2\2\u0152\u0154\7\3\2\2\u0153\u0155")
        buf.write('\5"\22\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156')
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u0159\7\4\2\2\u0159/\3\2\2\2\u015a\u015d\5@!\2")
        buf.write("\u015b\u015d\5\62\32\2\u015c\u015a\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d\61\3\2\2\2\u015e\u015f\5\64\33\2\u015f")
        buf.write("\u0160\7S\2\2\u0160\u0161\5n8\2\u0161\u0162\7T\2\2\u0162")
        buf.write("\63\3\2\2\2\u0163\u0164\t\2\2\2\u0164\65\3\2\2\2\u0165")
        buf.write("\u0167\7%\2\2\u0166\u0168\7p\2\2\u0167\u0166\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\t\3\2\2")
        buf.write("\u016a\u016b\58\35\2\u016b\67\3\2\2\2\u016c\u016d\7C\2")
        buf.write("\2\u016d\u016e\7v\2\2\u016e\u0172\7\3\2\2\u016f\u0173")
        buf.write("\5:\36\2\u0170\u0173\5\26\f\2\u0171\u0173\5\24\13\2\u0172")
        buf.write("\u016f\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\7\4\2\2\u01779")
        buf.write("\3\2\2\2\u0178\u017b\5z>\2\u0179\u017c\5<\37\2\u017a\u017c")
        buf.write("\7E\2\2\u017b\u0179\3\2\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017f\3\2\2\2\u017d\u0180\5z>\2\u017e\u0180\5> \2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\7v\2\2\u0182;\3\2\2\2\u0183\u0184\t\4\2\2")
        buf.write("\u0184=\3\2\2\2\u0185\u0186\7\25\2\2\u0186\u0187\5@!\2")
        buf.write("\u0187\u0188\7\67\2\2\u0188\u018b\5@!\2\u0189\u018a\7")
        buf.write("\26\2\2\u018a\u018c\5@!\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c?\3\2\2\2\u018d\u0193\5D#\2\u018e\u018f")
        buf.write("\7\66\2\2\u018f\u0190\5D#\2\u0190\u0191\7\63\2\2\u0191")
        buf.write("\u0192\5@!\2\u0192\u0194\3\2\2\2\u0193\u018e\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194A\3\2\2\2\u0195\u0196\5D#\2\u0196")
        buf.write("C\3\2\2\2\u0197\u019c\5F$\2\u0198\u0199\7;\2\2\u0199\u019b")
        buf.write("\5F$\2\u019a\u0198\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019dE\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019f\u01a4\5H%\2\u01a0\u01a1\7\61\2\2\u01a1")
        buf.write("\u01a3\5H%\2\u01a2\u01a0\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5G\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01a8\7:\2\2\u01a8\u01ab\5H%\2\u01a9")
        buf.write("\u01ab\5J&\2\u01aa\u01a7\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("I\3\2\2\2\u01ac\u01b2\5N(\2\u01ad\u01ae\5L'\2\u01ae\u01af")
        buf.write("\5N(\2\u01af\u01b1\3\2\2\2\u01b0\u01ad\3\2\2\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("K\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01c2\7Y\2\2\u01b6")
        buf.write("\u01c2\7Z\2\2\u01b7\u01c2\7[\2\2\u01b8\u01c2\7\\\2\2\u01b9")
        buf.write("\u01c2\7]\2\2\u01ba\u01c2\7^\2\2\u01bb\u01c2\7\67\2\2")
        buf.write("\u01bc\u01bd\7:\2\2\u01bd\u01c2\7\67\2\2\u01be\u01c2\7")
        buf.write("8\2\2\u01bf\u01c0\78\2\2\u01c0\u01c2\7:\2\2\u01c1\u01b5")
        buf.write("\3\2\2\2\u01c1\u01b6\3\2\2\2\u01c1\u01b7\3\2\2\2\u01c1")
        buf.write("\u01b8\3\2\2\2\u01c1\u01b9\3\2\2\2\u01c1\u01ba\3\2\2\2")
        buf.write("\u01c1\u01bb\3\2\2\2\u01c1\u01bc\3\2\2\2\u01c1\u01be\3")
        buf.write("\2\2\2\u01c1\u01bf\3\2\2\2\u01c2M\3\2\2\2\u01c3\u01c8")
        buf.write("\5P)\2\u01c4\u01c5\7F\2\2\u01c5\u01c7\5P)\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9O\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write("\u01d0\5R*\2\u01cc\u01cd\7G\2\2\u01cd\u01cf\5R*\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1Q\3\2\2\2\u01d2\u01d0\3\2\2")
        buf.write("\2\u01d3\u01d8\5T+\2\u01d4\u01d5\7H\2\2\u01d5\u01d7\5")
        buf.write("T+\2\u01d6\u01d4\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9S\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01db\u01e0\5V,\2\u01dc\u01dd\t\5\2\2\u01dd\u01df")
        buf.write("\5V,\2\u01de\u01dc\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de")
        buf.write("\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1U\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e3\u01e8\5X-\2\u01e4\u01e5\t\6\2\2\u01e5\u01e7")
        buf.write("\5X-\2\u01e6\u01e4\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9W\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01eb\u01f0\5Z.\2\u01ec\u01ed\t\7\2\2\u01ed\u01ef")
        buf.write("\5Z.\2\u01ee\u01ec\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1Y\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f3\u01f4\t\b\2\2\u01f4\u01f7\5Z.\2\u01f5\u01f7")
        buf.write("\5\\/\2\u01f6\u01f3\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7")
        buf.write("[\3\2\2\2\u01f8\u01fb\5^\60\2\u01f9\u01fa\7R\2\2\u01fa")
        buf.write("\u01fc\5Z.\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("]\3\2\2\2\u01fd\u0201\5`\61\2\u01fe\u0200\5l\67\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0201\u0202\3\2\2\2\u0202_\3\2\2\2\u0203\u0201\3\2\2")
        buf.write("\2\u0204\u0206\7S\2\2\u0205\u0207\5h\65\2\u0206\u0205")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\u0225\7T\2\2\u0209\u020b\7U\2\2\u020a\u020c\5h\65\2\u020b")
        buf.write("\u020a\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u0225\7V\2\2\u020e\u020f\7U\2\2\u020f\u0210\5f")
        buf.write("\64\2\u0210\u0211\7@\2\2\u0211\u0212\5f\64\2\u0212\u0213")
        buf.write("\7V\2\2\u0213\u0225\3\2\2\2\u0214\u0216\7Y\2\2\u0215\u0217")
        buf.write("\5j\66\2\u0216\u0215\3\2\2\2\u0216\u0217\3\2\2\2\u0217")
        buf.write("\u0218\3\2\2\2\u0218\u0225\7Z\2\2\u0219\u021b\7W\2\2\u021a")
        buf.write("\u021c\5|?\2\u021b\u021a\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u021d\3\2\2\2\u021d\u0225\7X\2\2\u021e\u0225\5b\62\2")
        buf.write("\u021f\u0225\5f\64\2\u0220\u0225\7m\2\2\u0221\u0225\7")
        buf.write("9\2\2\u0222\u0225\7=\2\2\u0223\u0225\7\64\2\2\u0224\u0204")
        buf.write("\3\2\2\2\u0224\u0209\3\2\2\2\u0224\u020e\3\2\2\2\u0224")
        buf.write("\u0214\3\2\2\2\u0224\u0219\3\2\2\2\u0224\u021e\3\2\2\2")
        buf.write("\u0224\u021f\3\2\2\2\u0224\u0220\3\2\2\2\u0224\u0221\3")
        buf.write("\2\2\2\u0224\u0222\3\2\2\2\u0224\u0223\3\2\2\2\u0225a")
        buf.write("\3\2\2\2\u0226\u0231\7k\2\2\u0227\u0231\7>\2\2\u0228\u0231")
        buf.write("\5d\63\2\u0229\u0231\7\33\2\2\u022a\u0231\7\34\2\2\u022b")
        buf.write("\u0231\7\35\2\2\u022c\u0231\7\36\2\2\u022d\u0231\7\32")
        buf.write("\2\2\u022e\u0231\7$\2\2\u022f\u0231\7 \2\2\u0230\u0226")
        buf.write("\3\2\2\2\u0230\u0227\3\2\2\2\u0230\u0228\3\2\2\2\u0230")
        buf.write("\u0229\3\2\2\2\u0230\u022a\3\2\2\2\u0230\u022b\3\2\2\2")
        buf.write("\u0230\u022c\3\2\2\2\u0230\u022d\3\2\2\2\u0230\u022e\3")
        buf.write("\2\2\2\u0230\u022f\3\2\2\2\u0231c\3\2\2\2\u0232\u023a")
        buf.write("\7\t\2\2\u0233\u0235\7\f\2\2\u0234\u0233\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u023a\7\n\2\2")
        buf.write("\u0237\u023a\7\13\2\2\u0238\u023a\7\r\2\2\u0239\u0232")
        buf.write("\3\2\2\2\u0239\u0234\3\2\2\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u0238\3\2\2\2\u023ae\3\2\2\2\u023b\u023f\7n\2\2\u023c")
        buf.write("\u023d\7M\2\2\u023d\u023f\7n\2\2\u023e\u023b\3\2\2\2\u023e")
        buf.write("\u023c\3\2\2\2\u023fg\3\2\2\2\u0240\u024c\5@!\2\u0241")
        buf.write("\u024d\5\u0080A\2\u0242\u0243\7B\2\2\u0243\u0245\5@!\2")
        buf.write("\u0244\u0242\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3")
        buf.write("\2\2\2\u0246\u0247\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246")
        buf.write("\3\2\2\2\u0249\u024b\7B\2\2\u024a\u0249\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u024d\3\2\2\2\u024c\u0241\3\2\2\2")
        buf.write("\u024c\u0246\3\2\2\2\u024di\3\2\2\2\u024e\u025a\5N(\2")
        buf.write("\u024f\u025b\5\u0080A\2\u0250\u0251\7B\2\2\u0251\u0253")
        buf.write("\5N(\2\u0252\u0250\3\2\2\2\u0253\u0256\3\2\2\2\u0254\u0252")
        buf.write("\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0258\3\2\2\2\u0256")
        buf.write("\u0254\3\2\2\2\u0257\u0259\7B\2\2\u0258\u0257\3\2\2\2")
        buf.write("\u0258\u0259\3\2\2\2\u0259\u025b\3\2\2\2\u025a\u024f\3")
        buf.write("\2\2\2\u025a\u0254\3\2\2\2\u025bk\3\2\2\2\u025c\u025d")
        buf.write("\7U\2\2\u025d\u025e\5r:\2\u025e\u025f\7V\2\2\u025f\u0263")
        buf.write("\3\2\2\2\u0260\u0261\7?\2\2\u0261\u0263\5b\62\2\u0262")
        buf.write("\u025c\3\2\2\2\u0262\u0260\3\2\2\2\u0263m\3\2\2\2\u0264")
        buf.write("\u0269\5p9\2\u0265\u0266\7B\2\2\u0266\u0268\5p9\2\u0267")
        buf.write("\u0265\3\2\2\2\u0268\u026b\3\2\2\2\u0269\u0267\3\2\2\2")
        buf.write("\u0269\u026a\3\2\2\2\u026a\u026d\3\2\2\2\u026b\u0269\3")
        buf.write("\2\2\2\u026c\u026e\7B\2\2\u026d\u026c\3\2\2\2\u026d\u026e")
        buf.write("\3\2\2\2\u026eo\3\2\2\2\u026f\u0271\5@!\2\u0270\u0272")
        buf.write("\5\u0080A\2\u0271\u0270\3\2\2\2\u0271\u0272\3\2\2\2\u0272")
        buf.write("\u0278\3\2\2\2\u0273\u0274\5@!\2\u0274\u0275\7E\2\2\u0275")
        buf.write("\u0276\5@!\2\u0276\u0278\3\2\2\2\u0277\u026f\3\2\2\2\u0277")
        buf.write("\u0273\3\2\2\2\u0278q\3\2\2\2\u0279\u027e\5t;\2\u027a")
        buf.write("\u027b\7B\2\2\u027b\u027d\5t;\2\u027c\u027a\3\2\2\2\u027d")
        buf.write("\u0280\3\2\2\2\u027e\u027c\3\2\2\2\u027e\u027f\3\2\2\2")
        buf.write("\u027f\u0282\3\2\2\2\u0280\u027e\3\2\2\2\u0281\u0283\7")
        buf.write("B\2\2\u0282\u0281\3\2\2\2\u0282\u0283\3\2\2\2\u0283s\3")
        buf.write("\2\2\2\u0284\u0290\5@!\2\u0285\u0287\5@!\2\u0286\u0285")
        buf.write("\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0288\3\2\2\2\u0288")
        buf.write("\u028a\7C\2\2\u0289\u028b\5@!\2\u028a\u0289\3\2\2\2\u028a")
        buf.write("\u028b\3\2\2\2\u028b\u028d\3\2\2\2\u028c\u028e\5v<\2\u028d")
        buf.write("\u028c\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u0290\3\2\2\2")
        buf.write("\u028f\u0284\3\2\2\2\u028f\u0286\3\2\2\2\u0290u\3\2\2")
        buf.write("\2\u0291\u0293\7C\2\2\u0292\u0294\5@!\2\u0293\u0292\3")
        buf.write("\2\2\2\u0293\u0294\3\2\2\2\u0294w\3\2\2\2\u0295\u029a")
        buf.write("\5N(\2\u0296\u0297\7B\2\2\u0297\u0299\5N(\2\u0298\u0296")
        buf.write("\3\2\2\2\u0299\u029c\3\2\2\2\u029a\u0298\3\2\2\2\u029a")
        buf.write("\u029b\3\2\2\2\u029b\u029e\3\2\2\2\u029c\u029a\3\2\2\2")
        buf.write("\u029d\u029f\7B\2\2\u029e\u029d\3\2\2\2\u029e\u029f\3")
        buf.write("\2\2\2\u029fy\3\2\2\2\u02a0\u02a5\5@!\2\u02a1\u02a2\7")
        buf.write("B\2\2\u02a2\u02a4\5@!\2\u02a3\u02a1\3\2\2\2\u02a4\u02a7")
        buf.write("\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a5\u02a6\3\2\2\2\u02a6")
        buf.write("\u02a9\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a8\u02aa\7B\2\2")
        buf.write("\u02a9\u02a8\3\2\2\2\u02a9\u02aa\3\2\2\2\u02aa{\3\2\2")
        buf.write("\2\u02ab\u02ac\5@!\2\u02ac\u02ad\7C\2\2\u02ad\u02bc\5")
        buf.write("@!\2\u02ae\u02bd\5\u0080A\2\u02af\u02b0\7B\2\2\u02b0\u02b1")
        buf.write("\5@!\2\u02b1\u02b2\7C\2\2\u02b2\u02b3\5@!\2\u02b3\u02b5")
        buf.write("\3\2\2\2\u02b4\u02af\3\2\2\2\u02b5\u02b8\3\2\2\2\u02b6")
        buf.write("\u02b4\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u02ba\3\2\2\2")
        buf.write("\u02b8\u02b6\3\2\2\2\u02b9\u02bb\7B\2\2\u02ba\u02b9\3")
        buf.write("\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02bd\3\2\2\2\u02bc\u02ae")
        buf.write("\3\2\2\2\u02bc\u02b6\3\2\2\2\u02bd\u02cd\3\2\2\2\u02be")
        buf.write("\u02ca\5@!\2\u02bf\u02cb\5\u0080A\2\u02c0\u02c1\7B\2\2")
        buf.write("\u02c1\u02c3\5@!\2\u02c2\u02c0\3\2\2\2\u02c3\u02c6\3\2")
        buf.write("\2\2\u02c4\u02c2\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5\u02c8")
        buf.write("\3\2\2\2\u02c6\u02c4\3\2\2\2\u02c7\u02c9\7B\2\2\u02c8")
        buf.write("\u02c7\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02cb\3\2\2\2")
        buf.write("\u02ca\u02bf\3\2\2\2\u02ca\u02c4\3\2\2\2\u02cb\u02cd\3")
        buf.write("\2\2\2\u02cc\u02ab\3\2\2\2\u02cc\u02be\3\2\2\2\u02cd}")
        buf.write("\3\2\2\2\u02ce\u02d1\5\u0080A\2\u02cf\u02d1\5\u0082B\2")
        buf.write("\u02d0\u02ce\3\2\2\2\u02d0\u02cf\3\2\2\2\u02d1\177\3\2")
        buf.write("\2\2\u02d2\u02d3\7\65\2\2\u02d3\u02d4\5x=\2\u02d4\u02d5")
        buf.write("\7\67\2\2\u02d5\u02d7\5D#\2\u02d6\u02d8\5~@\2\u02d7\u02d6")
        buf.write("\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8\u0081\3\2\2\2\u02d9")
        buf.write('\u02da\7\66\2\2\u02da\u02dc\5B"\2\u02db\u02dd\5~@\2\u02dc')
        buf.write("\u02db\3\2\2\2\u02dc\u02dd\3\2\2\2\u02dd\u0083\3\2\2\2")
        buf.write("`\u0091\u0093\u0097\u009e\u00a0\u00aa\u00b4\u00be\u00c2")
        buf.write("\u00d0\u00d6\u00de\u00e2\u00e6\u00ea\u00f3\u00f7\u00fb")
        buf.write("\u0107\u010b\u0112\u0114\u011b\u011f\u0124\u0127\u012f")
        buf.write("\u0139\u013d\u0149\u0156\u015c\u0167\u0172\u0174\u017b")
        buf.write("\u017f\u018b\u0193\u019c\u01a4\u01aa\u01b2\u01c1\u01c8")
        buf.write("\u01d0\u01d8\u01e0\u01e8\u01f0\u01f6\u01fb\u0201\u0206")
        buf.write("\u020b\u0216\u021b\u0224\u0230\u0234\u0239\u023e\u0246")
        buf.write("\u024a\u024c\u0254\u0258\u025a\u0262\u0269\u026d\u0271")
        buf.write("\u0277\u027e\u0282\u0286\u028a\u028d\u028f\u0293\u029a")
        buf.write("\u029e\u02a5\u02a9\u02b6\u02ba\u02bc\u02c4\u02c8\u02ca")
        buf.write("\u02cc\u02d0\u02d7\u02dc")
        return buf.getvalue()


class YarcParser(YarcParserBase):
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
        "'writer'",
        "<INVALID>",
        "<INVALID>",
        "'camera'",
        "'light'",
        "'stereo'",
        "'material'",
        "'timeline'",
        "'open'",
        "'create'",
        "'group'",
        "'instantiate'",
        "'get'",
        "'edit'",
        "'fetch'",
        "'match'",
        "'translate'",
        "'rotate'",
        "'scale'",
        "'semantics'",
        "'visible'",
        "'size'",
        "'look_at'",
        "'up_axis'",
        "<INVALID>",
        "<INVALID>",
        "'scatter'",
        "<INVALID>",
        "'around'",
        "'texture'",
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
        "WRITER",
        "LIB",
        "SHAPES",
        "CAMERA",
        "LIGHT",
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
        "TRANSLATE",
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
        "SCATTER_TYPE",
        "AROUND",
        "TEXTURE",
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
        "ADD",
        "MINUS",
        "DIV",
        "STAR",
        "MOD",
        "IDIV",
        "POWER",
        "LPAREN",
        "RPAREN",
        "LBRACK",
        "RBRACK",
        "LBRACE",
        "RBRACE",
        "LESS_THAN",
        "GREATER_THAN",
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
        "OPTION_ID",
        "STRING",
        "NUMBER",
        "STRING_LITERAL",
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

    RULE_scene = 0
    RULE_declaration = 1
    RULE_header = 2
    RULE_stmts = 3
    RULE_settings = 4
    RULE_setting = 5
    RULE_writer = 6
    RULE_option = 7
    RULE_open_stmt = 8
    RULE_create_stmt = 9
    RULE_edit_stmt = 10
    RULE_create_expr = 11
    RULE_instantiate_expr = 12
    RULE_group_expr = 13
    RULE_get_expr = 14
    RULE_edit_block = 15
    RULE_attr = 16
    RULE_simple_attr = 17
    RULE_modifier = 18
    RULE_compound_attr = 19
    RULE_modify_attr = 20
    RULE_inner_behavior_stmt = 21
    RULE_inner_behavior_block = 22
    RULE_test_or_distribution = 23
    RULE_distribution_expr = 24
    RULE_distribution = 25
    RULE_behavior_stmt = 26
    RULE_behavior_block = 27
    RULE_expr_stmt = 28
    RULE_aug_assign = 29
    RULE_fetch_expr = 30
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
    RULE_primitives = 49
    RULE_signed_number = 50
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
        "scene",
        "declaration",
        "header",
        "stmts",
        "settings",
        "setting",
        "writer",
        "option",
        "open_stmt",
        "create_stmt",
        "edit_stmt",
        "create_expr",
        "instantiate_expr",
        "group_expr",
        "get_expr",
        "edit_block",
        "attr",
        "simple_attr",
        "modifier",
        "compound_attr",
        "modify_attr",
        "inner_behavior_stmt",
        "inner_behavior_block",
        "test_or_distribution",
        "distribution_expr",
        "distribution",
        "behavior_stmt",
        "behavior_block",
        "expr_stmt",
        "aug_assign",
        "fetch_expr",
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
        "primitives",
        "signed_number",
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
    WRITER = 5
    LIB = 6
    SHAPES = 7
    CAMERA = 8
    LIGHT = 9
    STEREO = 10
    MATERIAL = 11
    TIMELINE = 12
    OPEN = 13
    CREATE = 14
    GROUP = 15
    INSTANTIATE = 16
    GET = 17
    EDIT = 18
    FETCH = 19
    MATCH = 20
    TRANSLATE = 21
    ROTATE = 22
    SCALE = 23
    SEMANTICS = 24
    VISIBLE = 25
    SIZE = 26
    LOOK_AT = 27
    UP_AXIS = 28
    AXIS = 29
    ORDER = 30
    SCATTER = 31
    SCATTER_TYPE = 32
    AROUND = 33
    TEXTURE = 34
    EVERY = 35
    FRAMES = 36
    TIME = 37
    UNIFORM = 38
    NORMAL = 39
    CHOICE = 40
    SEQUENCE = 41
    LOG_UNIFORM = 42
    SNIPPET = 43
    TO = 44
    ON = 45
    AT = 46
    AND = 47
    DEF = 48
    ELSE = 49
    FALSE = 50
    FOR = 51
    IF = 52
    IN = 53
    IS = 54
    NONE = 55
    NOT = 56
    OR = 57
    RETURN = 58
    TRUE = 59
    UNDERSCORE = 60
    DOT = 61
    RANGE = 62
    ELLIPSIS = 63
    COMMA = 64
    COLON = 65
    SEMI = 66
    ASSIGN = 67
    BIT_OR = 68
    XOR = 69
    BIT_AND = 70
    BIT_NOT = 71
    LSHIFT = 72
    RSHIFT = 73
    ADD = 74
    MINUS = 75
    DIV = 76
    STAR = 77
    MOD = 78
    IDIV = 79
    POWER = 80
    LPAREN = 81
    RPAREN = 82
    LBRACK = 83
    RBRACK = 84
    LBRACE = 85
    RBRACE = 86
    LESS_THAN = 87
    GREATER_THAN = 88
    EQUALS = 89
    GT_EQ = 90
    LT_EQ = 91
    NOT_EQ = 92
    ADD_ASSIGN = 93
    SUB_ASSIGN = 94
    MULT_ASSIGN = 95
    DIV_ASSIGN = 96
    MOD_ASSIGN = 97
    AND_ASSIGN = 98
    OR_ASSIGN = 99
    XOR_ASSIGN = 100
    LSHIFT_ASSIGN = 101
    RSHIFT_ASSIGN = 102
    POWER_ASSIGN = 103
    IDIV_ASSIGN = 104
    ID = 105
    OPTION_ID = 106
    STRING = 107
    NUMBER = 108
    STRING_LITERAL = 109
    INTEGER = 110
    DEC_INTEGER = 111
    OCT_INTEGER = 112
    HEX_INTEGER = 113
    BIN_INTEGER = 114
    FLOAT_NUMBER = 115
    NEWLINE = 116
    SKIP_ = 117
    UNKNOWN = 118

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class SceneContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(YarcParser.DeclarationContext, 0)

        def header(self):
            return self.getTypedRuleContext(YarcParser.HeaderContext, 0)

        def stmts(self):
            return self.getTypedRuleContext(YarcParser.StmtsContext, 0)

        def EOF(self):
            return self.getToken(YarcParser.EOF, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_scene

    def scene(self):
        localctx = YarcParser.SceneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_scene)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.declaration()
            self.state = 131
            self.header()
            self.state = 132
            self.stmts()
            self.state = 133
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

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_declaration

    def declaration(self):
        localctx = YarcParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(YarcParser.SCENARIO)
            self.state = 136
            self.name()
            self.state = 137
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeaderContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def settings(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.SettingsContext)
            else:
                return self.getTypedRuleContext(YarcParser.SettingsContext, i)

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

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.NEWLINE)
            else:
                return self.getToken(YarcParser.NEWLINE, i)

        def getRuleIndex(self):
            return YarcParser.RULE_header

    def header(self):
        localctx = YarcParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 1, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 143
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [YarcParser.SETTINGS]:
                        self.state = 139
                        self.settings()
                        pass
                    elif token in [
                        YarcParser.SHAPES,
                        YarcParser.CAMERA,
                        YarcParser.LIGHT,
                        YarcParser.STEREO,
                        YarcParser.MATERIAL,
                        YarcParser.SEMANTICS,
                        YarcParser.VISIBLE,
                        YarcParser.SIZE,
                        YarcParser.LOOK_AT,
                        YarcParser.UP_AXIS,
                        YarcParser.ORDER,
                        YarcParser.TEXTURE,
                        YarcParser.FALSE,
                        YarcParser.NONE,
                        YarcParser.NOT,
                        YarcParser.TRUE,
                        YarcParser.UNDERSCORE,
                        YarcParser.BIT_NOT,
                        YarcParser.ADD,
                        YarcParser.MINUS,
                        YarcParser.LPAREN,
                        YarcParser.LBRACK,
                        YarcParser.LBRACE,
                        YarcParser.LESS_THAN,
                        YarcParser.ID,
                        YarcParser.STRING,
                        YarcParser.NUMBER,
                    ]:
                        self.state = 140
                        self.expr_stmt()
                        pass
                    elif token in [YarcParser.WRITER]:
                        self.state = 141
                        self.writer()
                        pass
                    elif token in [YarcParser.NEWLINE]:
                        self.state = 142
                        self.match(YarcParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)

                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 1, self._ctx)

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

        def create_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Create_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Create_stmtContext, i)

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

        def expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Expr_stmtContext, i)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.NEWLINE)
            else:
                return self.getToken(YarcParser.NEWLINE, i)

        def getRuleIndex(self):
            return YarcParser.RULE_stmts

    def stmts(self):
        localctx = YarcParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmts)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.OPEN:
                self.state = 148
                self.open_stmt()

            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.SHAPES)
                        | (1 << YarcParser.CAMERA)
                        | (1 << YarcParser.LIGHT)
                        | (1 << YarcParser.STEREO)
                        | (1 << YarcParser.MATERIAL)
                        | (1 << YarcParser.CREATE)
                        | (1 << YarcParser.GROUP)
                        | (1 << YarcParser.INSTANTIATE)
                        | (1 << YarcParser.GET)
                        | (1 << YarcParser.EDIT)
                        | (1 << YarcParser.SEMANTICS)
                        | (1 << YarcParser.VISIBLE)
                        | (1 << YarcParser.SIZE)
                        | (1 << YarcParser.LOOK_AT)
                        | (1 << YarcParser.UP_AXIS)
                        | (1 << YarcParser.ORDER)
                        | (1 << YarcParser.TEXTURE)
                        | (1 << YarcParser.EVERY)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or (
                ((_la - 71) & ~0x3F) == 0
                and (
                    (1 << (_la - 71))
                    & (
                        (1 << (YarcParser.BIT_NOT - 71))
                        | (1 << (YarcParser.ADD - 71))
                        | (1 << (YarcParser.MINUS - 71))
                        | (1 << (YarcParser.LPAREN - 71))
                        | (1 << (YarcParser.LBRACK - 71))
                        | (1 << (YarcParser.LBRACE - 71))
                        | (1 << (YarcParser.LESS_THAN - 71))
                        | (1 << (YarcParser.ID - 71))
                        | (1 << (YarcParser.STRING - 71))
                        | (1 << (YarcParser.NUMBER - 71))
                        | (1 << (YarcParser.NEWLINE - 71))
                    )
                )
                != 0
            ):
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
                if la_ == 1:
                    self.state = 151
                    self.create_stmt()
                    pass

                elif la_ == 2:
                    self.state = 152
                    self.edit_stmt()
                    pass

                elif la_ == 3:
                    self.state = 153
                    self.behavior_stmt()
                    pass

                elif la_ == 4:
                    self.state = 154
                    self.expr_stmt()
                    pass

                elif la_ == 5:
                    self.state = 155
                    self.match(YarcParser.NEWLINE)
                    pass

                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def setting(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.SettingContext)
            else:
                return self.getTypedRuleContext(YarcParser.SettingContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_settings

    def settings(self):
        localctx = YarcParser.SettingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_settings)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(YarcParser.SETTINGS)
            self.state = 162
            self.match(YarcParser.COLON)
            self.state = 163
            self.match(YarcParser.NEWLINE)
            self.state = 164
            self.match(YarcParser.INDENT)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 165
                self.setting()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.LIB or _la == YarcParser.ID):
                    break

            self.state = 170
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SettingContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIB(self):
            return self.getToken(YarcParser.LIB, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def option(self):
            return self.getTypedRuleContext(YarcParser.OptionContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_setting

    def setting(self):
        localctx = YarcParser.SettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_setting)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LIB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(YarcParser.LIB)
                self.state = 173
                self.match(YarcParser.ASSIGN)
                self.state = 174
                self.test()
                self.state = 175
                self.match(YarcParser.NEWLINE)
                pass
            elif token in [YarcParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.option()
                pass
            else:
                raise NoViableAltException(self)

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

        def WRITER(self):
            return self.getToken(YarcParser.WRITER, 0)

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
        self.enterRule(localctx, 12, self.RULE_writer)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(YarcParser.WRITER)
            self.state = 181
            self.match(YarcParser.ID)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 182
                self.match(YarcParser.COLON)
                self.state = 183
                self.match(YarcParser.NEWLINE)
                self.state = 184
                self.match(YarcParser.INDENT)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 185
                    self.option()
                    self.state = 188
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == YarcParser.ID):
                        break

                self.state = 190
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
        self.enterRule(localctx, 14, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(YarcParser.ID)
            self.state = 195
            self.match(YarcParser.ASSIGN)
            self.state = 196
            self.test()
            self.state = 197
            self.match(YarcParser.NEWLINE)
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
            self.state = 199
            self.match(YarcParser.OPEN)
            self.state = 200
            self.test()
            self.state = 201
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Create_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_expr(self):
            return self.getTypedRuleContext(YarcParser.Create_exprContext, 0)

        def instantiate_expr(self):
            return self.getTypedRuleContext(YarcParser.Instantiate_exprContext, 0)

        def get_expr(self):
            return self.getTypedRuleContext(YarcParser.Get_exprContext, 0)

        def group_expr(self):
            return self.getTypedRuleContext(YarcParser.Group_exprContext, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_create_stmt

    def create_stmt(self):
        localctx = YarcParser.Create_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_create_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.SHAPES)
                        | (1 << YarcParser.CAMERA)
                        | (1 << YarcParser.LIGHT)
                        | (1 << YarcParser.STEREO)
                        | (1 << YarcParser.MATERIAL)
                        | (1 << YarcParser.SEMANTICS)
                        | (1 << YarcParser.VISIBLE)
                        | (1 << YarcParser.SIZE)
                        | (1 << YarcParser.LOOK_AT)
                        | (1 << YarcParser.UP_AXIS)
                        | (1 << YarcParser.ORDER)
                        | (1 << YarcParser.TEXTURE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or _la == YarcParser.ID:
                self.state = 203
                self.name()
                self.state = 204
                self.match(YarcParser.ASSIGN)

            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.CREATE]:
                self.state = 208
                self.create_expr()
                pass
            elif token in [YarcParser.INSTANTIATE]:
                self.state = 209
                self.instantiate_expr()
                pass
            elif token in [YarcParser.GET]:
                self.state = 210
                self.get_expr()
                pass
            elif token in [YarcParser.GROUP]:
                self.state = 211
                self.group_expr()
                pass
            else:
                raise NoViableAltException(self)

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

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_edit_stmt

    def edit_stmt(self):
        localctx = YarcParser.Edit_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_edit_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(YarcParser.EDIT)
            self.state = 215
            self.name()
            self.state = 216
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

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_create_expr

    def create_expr(self):
        localctx = YarcParser.Create_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_create_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(YarcParser.CREATE)
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 11, self._ctx)
            if la_ == 1:
                self.state = 219
                self.test()

            self.state = 222
            self.test()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 223
                self.edit_block()

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

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def test_or_distribution(self):
            return self.getTypedRuleContext(YarcParser.Test_or_distributionContext, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_instantiate_expr

    def instantiate_expr(self):
        localctx = YarcParser.Instantiate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_instantiate_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(YarcParser.INSTANTIATE)
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 13, self._ctx)
            if la_ == 1:
                self.state = 227
                self.test_or_distribution()

            self.state = 230
            self.test()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 231
                self.edit_block()

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

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_group_expr

    def group_expr(self):
        localctx = YarcParser.Group_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_group_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(YarcParser.GROUP)
            self.state = 235
            self.match(YarcParser.LBRACK)
            self.state = 236
            self.name()
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 15, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 237
                    self.match(YarcParser.COMMA)
                    self.state = 238
                    self.name()
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 15, self._ctx)

            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 244
                self.match(YarcParser.COMMA)

            self.state = 247
            self.match(YarcParser.RBRACK)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 248
                self.edit_block()

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

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def AT(self):
            return self.getToken(YarcParser.AT, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

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
            return YarcParser.RULE_get_expr

    def get_expr(self):
        localctx = YarcParser.Get_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_get_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(YarcParser.GET)
            self.state = 252
            self.name()
            self.state = 253
            self.match(YarcParser.AT)
            self.state = 254
            self.test()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 255
                self.match(YarcParser.COLON)
                self.state = 256
                self.match(YarcParser.NEWLINE)
                self.state = 257
                self.match(YarcParser.INDENT)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 258
                    self.simple_attr()
                    self.state = 261
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (
                        (
                            ((_la) & ~0x3F) == 0
                            and (
                                (1 << _la)
                                & (
                                    (1 << YarcParser.SHAPES)
                                    | (1 << YarcParser.CAMERA)
                                    | (1 << YarcParser.LIGHT)
                                    | (1 << YarcParser.STEREO)
                                    | (1 << YarcParser.MATERIAL)
                                    | (1 << YarcParser.SEMANTICS)
                                    | (1 << YarcParser.VISIBLE)
                                    | (1 << YarcParser.SIZE)
                                    | (1 << YarcParser.LOOK_AT)
                                    | (1 << YarcParser.UP_AXIS)
                                    | (1 << YarcParser.ORDER)
                                    | (1 << YarcParser.TEXTURE)
                                    | (1 << YarcParser.FALSE)
                                    | (1 << YarcParser.NONE)
                                    | (1 << YarcParser.NOT)
                                    | (1 << YarcParser.TRUE)
                                    | (1 << YarcParser.UNDERSCORE)
                                )
                            )
                            != 0
                        )
                        or (
                            ((_la - 71) & ~0x3F) == 0
                            and (
                                (1 << (_la - 71))
                                & (
                                    (1 << (YarcParser.BIT_NOT - 71))
                                    | (1 << (YarcParser.ADD - 71))
                                    | (1 << (YarcParser.MINUS - 71))
                                    | (1 << (YarcParser.LPAREN - 71))
                                    | (1 << (YarcParser.LBRACK - 71))
                                    | (1 << (YarcParser.LBRACE - 71))
                                    | (1 << (YarcParser.LESS_THAN - 71))
                                    | (1 << (YarcParser.ID - 71))
                                    | (1 << (YarcParser.STRING - 71))
                                    | (1 << (YarcParser.NUMBER - 71))
                                )
                            )
                            != 0
                        )
                    ):
                        break

                self.state = 263
                self.match(YarcParser.DEDENT)

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
        self.enterRule(localctx, 30, self.RULE_edit_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(YarcParser.COLON)
            self.state = 268
            self.match(YarcParser.NEWLINE)
            self.state = 269
            self.match(YarcParser.INDENT)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 272
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.SHAPES,
                    YarcParser.CAMERA,
                    YarcParser.LIGHT,
                    YarcParser.STEREO,
                    YarcParser.MATERIAL,
                    YarcParser.TRANSLATE,
                    YarcParser.ROTATE,
                    YarcParser.SCALE,
                    YarcParser.SEMANTICS,
                    YarcParser.VISIBLE,
                    YarcParser.SIZE,
                    YarcParser.LOOK_AT,
                    YarcParser.UP_AXIS,
                    YarcParser.ORDER,
                    YarcParser.SCATTER,
                    YarcParser.TEXTURE,
                    YarcParser.FALSE,
                    YarcParser.NONE,
                    YarcParser.NOT,
                    YarcParser.TRUE,
                    YarcParser.UNDERSCORE,
                    YarcParser.BIT_NOT,
                    YarcParser.ADD,
                    YarcParser.MINUS,
                    YarcParser.LPAREN,
                    YarcParser.LBRACK,
                    YarcParser.LBRACE,
                    YarcParser.LESS_THAN,
                    YarcParser.ID,
                    YarcParser.STRING,
                    YarcParser.NUMBER,
                ]:
                    self.state = 270
                    self.attr()
                    pass
                elif token in [YarcParser.EVERY]:
                    self.state = 271
                    self.inner_behavior_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.SHAPES)
                                | (1 << YarcParser.CAMERA)
                                | (1 << YarcParser.LIGHT)
                                | (1 << YarcParser.STEREO)
                                | (1 << YarcParser.MATERIAL)
                                | (1 << YarcParser.TRANSLATE)
                                | (1 << YarcParser.ROTATE)
                                | (1 << YarcParser.SCALE)
                                | (1 << YarcParser.SEMANTICS)
                                | (1 << YarcParser.VISIBLE)
                                | (1 << YarcParser.SIZE)
                                | (1 << YarcParser.LOOK_AT)
                                | (1 << YarcParser.UP_AXIS)
                                | (1 << YarcParser.ORDER)
                                | (1 << YarcParser.SCATTER)
                                | (1 << YarcParser.TEXTURE)
                                | (1 << YarcParser.EVERY)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 71) & ~0x3F) == 0
                        and (
                            (1 << (_la - 71))
                            & (
                                (1 << (YarcParser.BIT_NOT - 71))
                                | (1 << (YarcParser.ADD - 71))
                                | (1 << (YarcParser.MINUS - 71))
                                | (1 << (YarcParser.LPAREN - 71))
                                | (1 << (YarcParser.LBRACK - 71))
                                | (1 << (YarcParser.LBRACE - 71))
                                | (1 << (YarcParser.LESS_THAN - 71))
                                | (1 << (YarcParser.ID - 71))
                                | (1 << (YarcParser.STRING - 71))
                                | (1 << (YarcParser.NUMBER - 71))
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 276
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

        def simple_attr(self):
            return self.getTypedRuleContext(YarcParser.Simple_attrContext, 0)

        def compound_attr(self):
            return self.getTypedRuleContext(YarcParser.Compound_attrContext, 0)

        def modify_attr(self):
            return self.getTypedRuleContext(YarcParser.Modify_attrContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_attr

    def attr(self):
        localctx = YarcParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attr)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 22, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.simple_attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.compound_attr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.modify_attr()
                pass

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

        def expr_stmt(self):
            return self.getTypedRuleContext(YarcParser.Expr_stmtContext, 0)

        def modifier(self):
            return self.getTypedRuleContext(YarcParser.ModifierContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_attr

    def simple_attr(self):
        localctx = YarcParser.Simple_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_simple_attr)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 23, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.expr_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.modifier()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModifierContext(ParserRuleContext):
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

        def test_or_distribution(self):
            return self.getTypedRuleContext(YarcParser.Test_or_distributionContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_modifier

    def modifier(self):
        localctx = YarcParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_modifier)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.name()
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 288
                self.match(YarcParser.COLON)
                self.state = 289
                self.name()

            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.SHAPES)
                        | (1 << YarcParser.CAMERA)
                        | (1 << YarcParser.LIGHT)
                        | (1 << YarcParser.STEREO)
                        | (1 << YarcParser.MATERIAL)
                        | (1 << YarcParser.SEMANTICS)
                        | (1 << YarcParser.VISIBLE)
                        | (1 << YarcParser.SIZE)
                        | (1 << YarcParser.LOOK_AT)
                        | (1 << YarcParser.UP_AXIS)
                        | (1 << YarcParser.ORDER)
                        | (1 << YarcParser.TEXTURE)
                        | (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or (
                ((_la - 71) & ~0x3F) == 0
                and (
                    (1 << (_la - 71))
                    & (
                        (1 << (YarcParser.BIT_NOT - 71))
                        | (1 << (YarcParser.ADD - 71))
                        | (1 << (YarcParser.MINUS - 71))
                        | (1 << (YarcParser.LPAREN - 71))
                        | (1 << (YarcParser.LBRACK - 71))
                        | (1 << (YarcParser.LBRACE - 71))
                        | (1 << (YarcParser.LESS_THAN - 71))
                        | (1 << (YarcParser.ID - 71))
                        | (1 << (YarcParser.STRING - 71))
                        | (1 << (YarcParser.NUMBER - 71))
                    )
                )
                != 0
            ):
                self.state = 292
                self.test_or_distribution()

            self.state = 295
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

        def getRuleIndex(self):
            return YarcParser.RULE_compound_attr

    def compound_attr(self):
        localctx = YarcParser.Compound_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_compound_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(YarcParser.SCATTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Modify_attrContext(ParserRuleContext):
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

        def test_or_distribution(self):
            return self.getTypedRuleContext(YarcParser.Test_or_distributionContext, 0)

        def CAMERA(self):
            return self.getToken(YarcParser.CAMERA, 0)

        def ROTATE(self):
            return self.getToken(YarcParser.ROTATE, 0)

        def SCALE(self):
            return self.getToken(YarcParser.SCALE, 0)

        def LOOK_AT(self):
            return self.getToken(YarcParser.LOOK_AT, 0)

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
            return YarcParser.RULE_modify_attr

    def modify_attr(self):
        localctx = YarcParser.Modify_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_modify_attr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.TRANSLATE]:
                self.state = 299
                self.match(YarcParser.TRANSLATE)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.AXIS:
                    self.state = 300
                    self.match(YarcParser.AXIS)

                self.state = 303
                self.match(YarcParser.TO)
                self.state = 304
                self.test_or_distribution()
                pass
            elif token in [YarcParser.CAMERA]:
                self.state = 305
                self.match(YarcParser.CAMERA)
                self.state = 306
                self.match(YarcParser.TRANSLATE)
                self.state = 307
                self.match(YarcParser.TO)
                self.state = 308
                self.test_or_distribution()
                pass
            elif token in [YarcParser.ROTATE]:
                self.state = 309
                self.match(YarcParser.ROTATE)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.AXIS:
                    self.state = 310
                    self.match(YarcParser.AXIS)

                self.state = 313
                self.test_or_distribution()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.ORDER:
                    self.state = 314
                    self.match(YarcParser.ORDER)

                pass
            elif token in [YarcParser.SCALE]:
                self.state = 317
                self.match(YarcParser.SCALE)
                self.state = 318
                self.test_or_distribution()
                pass
            elif token in [YarcParser.LOOK_AT]:
                self.state = 319
                self.match(YarcParser.LOOK_AT)
                self.state = 320
                self.test_or_distribution()
                pass
            elif token in [YarcParser.SIZE]:
                self.state = 321
                self.match(YarcParser.SIZE)
                self.state = 322
                self.test_or_distribution()
                pass
            elif token in [YarcParser.SEMANTICS]:
                self.state = 323
                self.match(YarcParser.SEMANTICS)
                self.state = 324
                self.test_or_distribution()
                pass
            elif token in [YarcParser.VISIBLE]:
                self.state = 325
                self.match(YarcParser.VISIBLE)
                self.state = 326
                self.test_or_distribution()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 329
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

        def behavior_stmt(self):
            return self.getTypedRuleContext(YarcParser.Behavior_stmtContext, 0)

        def inner_behavior_block(self):
            return self.getTypedRuleContext(YarcParser.Inner_behavior_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_inner_behavior_stmt

    def inner_behavior_stmt(self):
        localctx = YarcParser.Inner_behavior_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_inner_behavior_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.behavior_stmt()
            self.state = 332
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
        self.enterRule(localctx, 44, self.RULE_inner_behavior_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(YarcParser.COLON)
            self.state = 335
            self.match(YarcParser.NEWLINE)
            self.state = 336
            self.match(YarcParser.INDENT)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 337
                self.attr()
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.SHAPES)
                                | (1 << YarcParser.CAMERA)
                                | (1 << YarcParser.LIGHT)
                                | (1 << YarcParser.STEREO)
                                | (1 << YarcParser.MATERIAL)
                                | (1 << YarcParser.TRANSLATE)
                                | (1 << YarcParser.ROTATE)
                                | (1 << YarcParser.SCALE)
                                | (1 << YarcParser.SEMANTICS)
                                | (1 << YarcParser.VISIBLE)
                                | (1 << YarcParser.SIZE)
                                | (1 << YarcParser.LOOK_AT)
                                | (1 << YarcParser.UP_AXIS)
                                | (1 << YarcParser.ORDER)
                                | (1 << YarcParser.SCATTER)
                                | (1 << YarcParser.TEXTURE)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 71) & ~0x3F) == 0
                        and (
                            (1 << (_la - 71))
                            & (
                                (1 << (YarcParser.BIT_NOT - 71))
                                | (1 << (YarcParser.ADD - 71))
                                | (1 << (YarcParser.MINUS - 71))
                                | (1 << (YarcParser.LPAREN - 71))
                                | (1 << (YarcParser.LBRACK - 71))
                                | (1 << (YarcParser.LBRACE - 71))
                                | (1 << (YarcParser.LESS_THAN - 71))
                                | (1 << (YarcParser.ID - 71))
                                | (1 << (YarcParser.STRING - 71))
                                | (1 << (YarcParser.NUMBER - 71))
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 342
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Test_or_distributionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def distribution_expr(self):
            return self.getTypedRuleContext(YarcParser.Distribution_exprContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_test_or_distribution

    def test_or_distribution(self):
        localctx = YarcParser.Test_or_distributionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_test_or_distribution)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.SHAPES,
                YarcParser.CAMERA,
                YarcParser.LIGHT,
                YarcParser.STEREO,
                YarcParser.MATERIAL,
                YarcParser.SEMANTICS,
                YarcParser.VISIBLE,
                YarcParser.SIZE,
                YarcParser.LOOK_AT,
                YarcParser.UP_AXIS,
                YarcParser.ORDER,
                YarcParser.TEXTURE,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LESS_THAN,
                YarcParser.ID,
                YarcParser.STRING,
                YarcParser.NUMBER,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.test()
                pass
            elif token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.distribution_expr()
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 48, self.RULE_distribution_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.distribution()
            self.state = 349
            self.match(YarcParser.LPAREN)
            self.state = 350
            self.arglist()
            self.state = 351
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
        self.enterRule(localctx, 50, self.RULE_distribution)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
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

    class Behavior_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVERY(self):
            return self.getToken(YarcParser.EVERY, 0)

        def behavior_block(self):
            return self.getTypedRuleContext(YarcParser.Behavior_blockContext, 0)

        def FRAMES(self):
            return self.getToken(YarcParser.FRAMES, 0)

        def TIME(self):
            return self.getToken(YarcParser.TIME, 0)

        def INTEGER(self):
            return self.getToken(YarcParser.INTEGER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_stmt

    def behavior_stmt(self):
        localctx = YarcParser.Behavior_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_behavior_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(YarcParser.EVERY)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.INTEGER:
                self.state = 356
                self.match(YarcParser.INTEGER)

            self.state = 359
            _la = self._input.LA(1)
            if not (_la == YarcParser.FRAMES or _la == YarcParser.TIME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 360
            self.behavior_block()
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

        def expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Expr_stmtContext, i)

        def edit_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Edit_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Edit_stmtContext, i)

        def create_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Create_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Create_stmtContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_block

    def behavior_block(self):
        localctx = YarcParser.Behavior_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_behavior_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(YarcParser.COLON)
            self.state = 363
            self.match(YarcParser.NEWLINE)
            self.state = 364
            self.match(YarcParser.INDENT)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 368
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 33, self._ctx)
                if la_ == 1:
                    self.state = 365
                    self.expr_stmt()
                    pass

                elif la_ == 2:
                    self.state = 366
                    self.edit_stmt()
                    pass

                elif la_ == 3:
                    self.state = 367
                    self.create_stmt()
                    pass

                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.SHAPES)
                                | (1 << YarcParser.CAMERA)
                                | (1 << YarcParser.LIGHT)
                                | (1 << YarcParser.STEREO)
                                | (1 << YarcParser.MATERIAL)
                                | (1 << YarcParser.CREATE)
                                | (1 << YarcParser.GROUP)
                                | (1 << YarcParser.INSTANTIATE)
                                | (1 << YarcParser.GET)
                                | (1 << YarcParser.EDIT)
                                | (1 << YarcParser.SEMANTICS)
                                | (1 << YarcParser.VISIBLE)
                                | (1 << YarcParser.SIZE)
                                | (1 << YarcParser.LOOK_AT)
                                | (1 << YarcParser.UP_AXIS)
                                | (1 << YarcParser.ORDER)
                                | (1 << YarcParser.TEXTURE)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 71) & ~0x3F) == 0
                        and (
                            (1 << (_la - 71))
                            & (
                                (1 << (YarcParser.BIT_NOT - 71))
                                | (1 << (YarcParser.ADD - 71))
                                | (1 << (YarcParser.MINUS - 71))
                                | (1 << (YarcParser.LPAREN - 71))
                                | (1 << (YarcParser.LBRACK - 71))
                                | (1 << (YarcParser.LBRACE - 71))
                                | (1 << (YarcParser.LESS_THAN - 71))
                                | (1 << (YarcParser.ID - 71))
                                | (1 << (YarcParser.STRING - 71))
                                | (1 << (YarcParser.NUMBER - 71))
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 372
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
        self.enterRule(localctx, 56, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.testlist()
            self.state = 377
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
                self.state = 375
                self.aug_assign()
                pass
            elif token in [YarcParser.ASSIGN]:
                self.state = 376
                self.match(YarcParser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.SHAPES,
                YarcParser.CAMERA,
                YarcParser.LIGHT,
                YarcParser.STEREO,
                YarcParser.MATERIAL,
                YarcParser.SEMANTICS,
                YarcParser.VISIBLE,
                YarcParser.SIZE,
                YarcParser.LOOK_AT,
                YarcParser.UP_AXIS,
                YarcParser.ORDER,
                YarcParser.TEXTURE,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LESS_THAN,
                YarcParser.ID,
                YarcParser.STRING,
                YarcParser.NUMBER,
            ]:
                self.state = 379
                self.testlist()
                pass
            elif token in [YarcParser.FETCH]:
                self.state = 380
                self.fetch_expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 383
            self.match(YarcParser.NEWLINE)
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
        self.enterRule(localctx, 58, self.RULE_aug_assign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            _la = self._input.LA(1)
            if not (
                ((_la - 93) & ~0x3F) == 0
                and (
                    (1 << (_la - 93))
                    & (
                        (1 << (YarcParser.ADD_ASSIGN - 93))
                        | (1 << (YarcParser.SUB_ASSIGN - 93))
                        | (1 << (YarcParser.MULT_ASSIGN - 93))
                        | (1 << (YarcParser.DIV_ASSIGN - 93))
                        | (1 << (YarcParser.MOD_ASSIGN - 93))
                        | (1 << (YarcParser.AND_ASSIGN - 93))
                        | (1 << (YarcParser.OR_ASSIGN - 93))
                        | (1 << (YarcParser.XOR_ASSIGN - 93))
                        | (1 << (YarcParser.LSHIFT_ASSIGN - 93))
                        | (1 << (YarcParser.RSHIFT_ASSIGN - 93))
                        | (1 << (YarcParser.POWER_ASSIGN - 93))
                        | (1 << (YarcParser.IDIV_ASSIGN - 93))
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

        def IN(self):
            return self.getToken(YarcParser.IN, 0)

        def MATCH(self):
            return self.getToken(YarcParser.MATCH, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_fetch_expr

    def fetch_expr(self):
        localctx = YarcParser.Fetch_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_fetch_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(YarcParser.FETCH)
            self.state = 388
            self.test()
            self.state = 389
            self.match(YarcParser.IN)
            self.state = 390
            self.test()
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.MATCH:
                self.state = 391
                self.match(YarcParser.MATCH)
                self.state = 392
                self.test()

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
            self.state = 395
            self.or_test()
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.IF:
                self.state = 396
                self.match(YarcParser.IF)
                self.state = 397
                self.or_test()
                self.state = 398
                self.match(YarcParser.ELSE)
                self.state = 399
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
            self.state = 403
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
            self.state = 405
            self.and_test()
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.OR:
                self.state = 406
                self.match(YarcParser.OR)
                self.state = 407
                self.and_test()
                self.state = 412
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
            self.state = 413
            self.not_test()
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.AND:
                self.state = 414
                self.match(YarcParser.AND)
                self.state = 415
                self.not_test()
                self.state = 420
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
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(YarcParser.NOT)
                self.state = 422
                self.not_test()
                pass
            elif token in [
                YarcParser.SHAPES,
                YarcParser.CAMERA,
                YarcParser.LIGHT,
                YarcParser.STEREO,
                YarcParser.MATERIAL,
                YarcParser.SEMANTICS,
                YarcParser.VISIBLE,
                YarcParser.SIZE,
                YarcParser.LOOK_AT,
                YarcParser.UP_AXIS,
                YarcParser.ORDER,
                YarcParser.TEXTURE,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LESS_THAN,
                YarcParser.ID,
                YarcParser.STRING,
                YarcParser.NUMBER,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.comparison()
                pass
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.expr()
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 42, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 427
                    self.comp_op()
                    self.state = 428
                    self.expr()
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 42, self._ctx)

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

        def LESS_THAN(self):
            return self.getToken(YarcParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(YarcParser.GREATER_THAN, 0)

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
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 43, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(YarcParser.LESS_THAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(YarcParser.GREATER_THAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(YarcParser.EQUALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
                self.match(YarcParser.GT_EQ)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.match(YarcParser.LT_EQ)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 440
                self.match(YarcParser.NOT_EQ)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 441
                self.match(YarcParser.IN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 442
                self.match(YarcParser.NOT)
                self.state = 443
                self.match(YarcParser.IN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 444
                self.match(YarcParser.IS)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 445
                self.match(YarcParser.IS)
                self.state = 446
                self.match(YarcParser.NOT)
                pass

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
            self.state = 449
            self.xor_expr()
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_OR:
                self.state = 450
                self.match(YarcParser.BIT_OR)
                self.state = 451
                self.xor_expr()
                self.state = 456
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
            self.state = 457
            self.and_expr()
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.XOR:
                self.state = 458
                self.match(YarcParser.XOR)
                self.state = 459
                self.and_expr()
                self.state = 464
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
            self.state = 465
            self.shift_expr()
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_AND:
                self.state = 466
                self.match(YarcParser.BIT_AND)
                self.state = 467
                self.shift_expr()
                self.state = 472
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
            self.state = 473
            self.arith_expr()
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT:
                self.state = 474
                _la = self._input.LA(1)
                if not (_la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 475
                self.arith_expr()
                self.state = 480
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

        def ADD(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.ADD)
            else:
                return self.getToken(YarcParser.ADD, i)

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
            self.state = 481
            self.term()
            self.state = 486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 48, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 482
                    _la = self._input.LA(1)
                    if not (_la == YarcParser.ADD or _la == YarcParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 483
                    self.term()
                self.state = 488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 48, self._ctx)

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

        def STAR(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.STAR)
            else:
                return self.getToken(YarcParser.STAR, i)

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
            self.state = 489
            self.factor()
            self.state = 494
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la - 76) & ~0x3F) == 0 and (
                (1 << (_la - 76))
                & (
                    (1 << (YarcParser.DIV - 76))
                    | (1 << (YarcParser.STAR - 76))
                    | (1 << (YarcParser.MOD - 76))
                    | (1 << (YarcParser.IDIV - 76))
                )
            ) != 0:
                self.state = 490
                _la = self._input.LA(1)
                if not (
                    ((_la - 76) & ~0x3F) == 0
                    and (
                        (1 << (_la - 76))
                        & (
                            (1 << (YarcParser.DIV - 76))
                            | (1 << (YarcParser.STAR - 76))
                            | (1 << (YarcParser.MOD - 76))
                            | (1 << (YarcParser.IDIV - 76))
                        )
                    )
                    != 0
                ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 491
                self.factor()
                self.state = 496
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

        def ADD(self):
            return self.getToken(YarcParser.ADD, 0)

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
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 50, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                _la = self._input.LA(1)
                if not (
                    ((_la - 71) & ~0x3F) == 0
                    and (
                        (1 << (_la - 71))
                        & (
                            (1 << (YarcParser.BIT_NOT - 71))
                            | (1 << (YarcParser.ADD - 71))
                            | (1 << (YarcParser.MINUS - 71))
                        )
                    )
                    != 0
                ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 498
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.power()
                pass

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
            self.state = 502
            self.atom_expr()
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.POWER:
                self.state = 503
                self.match(YarcParser.POWER)
                self.state = 504
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.atom()
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 52, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 508
                    self.trailer()
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 52, self._ctx)

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

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def testlist_comp(self):
            return self.getTypedRuleContext(YarcParser.Testlist_compContext, 0)

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def signed_number(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Signed_numberContext)
            else:
                return self.getTypedRuleContext(YarcParser.Signed_numberContext, i)

        def RANGE(self):
            return self.getToken(YarcParser.RANGE, 0)

        def LESS_THAN(self):
            return self.getToken(YarcParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(YarcParser.GREATER_THAN, 0)

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
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 57, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(YarcParser.LPAREN)
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.SHAPES)
                            | (1 << YarcParser.CAMERA)
                            | (1 << YarcParser.LIGHT)
                            | (1 << YarcParser.STEREO)
                            | (1 << YarcParser.MATERIAL)
                            | (1 << YarcParser.SEMANTICS)
                            | (1 << YarcParser.VISIBLE)
                            | (1 << YarcParser.SIZE)
                            | (1 << YarcParser.LOOK_AT)
                            | (1 << YarcParser.UP_AXIS)
                            | (1 << YarcParser.ORDER)
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 71) & ~0x3F) == 0
                    and (
                        (1 << (_la - 71))
                        & (
                            (1 << (YarcParser.BIT_NOT - 71))
                            | (1 << (YarcParser.ADD - 71))
                            | (1 << (YarcParser.MINUS - 71))
                            | (1 << (YarcParser.LPAREN - 71))
                            | (1 << (YarcParser.LBRACK - 71))
                            | (1 << (YarcParser.LBRACE - 71))
                            | (1 << (YarcParser.LESS_THAN - 71))
                            | (1 << (YarcParser.ID - 71))
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 515
                    self.testlist_comp()

                self.state = 518
                self.match(YarcParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.match(YarcParser.LBRACK)
                self.state = 521
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.SHAPES)
                            | (1 << YarcParser.CAMERA)
                            | (1 << YarcParser.LIGHT)
                            | (1 << YarcParser.STEREO)
                            | (1 << YarcParser.MATERIAL)
                            | (1 << YarcParser.SEMANTICS)
                            | (1 << YarcParser.VISIBLE)
                            | (1 << YarcParser.SIZE)
                            | (1 << YarcParser.LOOK_AT)
                            | (1 << YarcParser.UP_AXIS)
                            | (1 << YarcParser.ORDER)
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 71) & ~0x3F) == 0
                    and (
                        (1 << (_la - 71))
                        & (
                            (1 << (YarcParser.BIT_NOT - 71))
                            | (1 << (YarcParser.ADD - 71))
                            | (1 << (YarcParser.MINUS - 71))
                            | (1 << (YarcParser.LPAREN - 71))
                            | (1 << (YarcParser.LBRACK - 71))
                            | (1 << (YarcParser.LBRACE - 71))
                            | (1 << (YarcParser.LESS_THAN - 71))
                            | (1 << (YarcParser.ID - 71))
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 520
                    self.testlist_comp()

                self.state = 523
                self.match(YarcParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 524
                self.match(YarcParser.LBRACK)
                self.state = 525
                self.signed_number()
                self.state = 526
                self.match(YarcParser.RANGE)
                self.state = 527
                self.signed_number()
                self.state = 528
                self.match(YarcParser.RBRACK)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 530
                self.match(YarcParser.LESS_THAN)
                self.state = 532
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.SHAPES)
                            | (1 << YarcParser.CAMERA)
                            | (1 << YarcParser.LIGHT)
                            | (1 << YarcParser.STEREO)
                            | (1 << YarcParser.MATERIAL)
                            | (1 << YarcParser.SEMANTICS)
                            | (1 << YarcParser.VISIBLE)
                            | (1 << YarcParser.SIZE)
                            | (1 << YarcParser.LOOK_AT)
                            | (1 << YarcParser.UP_AXIS)
                            | (1 << YarcParser.ORDER)
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 71) & ~0x3F) == 0
                    and (
                        (1 << (_la - 71))
                        & (
                            (1 << (YarcParser.BIT_NOT - 71))
                            | (1 << (YarcParser.ADD - 71))
                            | (1 << (YarcParser.MINUS - 71))
                            | (1 << (YarcParser.LPAREN - 71))
                            | (1 << (YarcParser.LBRACK - 71))
                            | (1 << (YarcParser.LBRACE - 71))
                            | (1 << (YarcParser.LESS_THAN - 71))
                            | (1 << (YarcParser.ID - 71))
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 531
                    self.vector_comp()

                self.state = 534
                self.match(YarcParser.GREATER_THAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 535
                self.match(YarcParser.LBRACE)
                self.state = 537
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.SHAPES)
                            | (1 << YarcParser.CAMERA)
                            | (1 << YarcParser.LIGHT)
                            | (1 << YarcParser.STEREO)
                            | (1 << YarcParser.MATERIAL)
                            | (1 << YarcParser.SEMANTICS)
                            | (1 << YarcParser.VISIBLE)
                            | (1 << YarcParser.SIZE)
                            | (1 << YarcParser.LOOK_AT)
                            | (1 << YarcParser.UP_AXIS)
                            | (1 << YarcParser.ORDER)
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 71) & ~0x3F) == 0
                    and (
                        (1 << (_la - 71))
                        & (
                            (1 << (YarcParser.BIT_NOT - 71))
                            | (1 << (YarcParser.ADD - 71))
                            | (1 << (YarcParser.MINUS - 71))
                            | (1 << (YarcParser.LPAREN - 71))
                            | (1 << (YarcParser.LBRACK - 71))
                            | (1 << (YarcParser.LBRACE - 71))
                            | (1 << (YarcParser.LESS_THAN - 71))
                            | (1 << (YarcParser.ID - 71))
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 536
                    self.dict_or_set_maker()

                self.state = 539
                self.match(YarcParser.RBRACE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 540
                self.name()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 541
                self.signed_number()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 542
                self.match(YarcParser.STRING)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 543
                self.match(YarcParser.NONE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 544
                self.match(YarcParser.TRUE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 545
                self.match(YarcParser.FALSE)
                pass

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

        def primitives(self):
            return self.getTypedRuleContext(YarcParser.PrimitivesContext, 0)

        def VISIBLE(self):
            return self.getToken(YarcParser.VISIBLE, 0)

        def SIZE(self):
            return self.getToken(YarcParser.SIZE, 0)

        def LOOK_AT(self):
            return self.getToken(YarcParser.LOOK_AT, 0)

        def UP_AXIS(self):
            return self.getToken(YarcParser.UP_AXIS, 0)

        def SEMANTICS(self):
            return self.getToken(YarcParser.SEMANTICS, 0)

        def TEXTURE(self):
            return self.getToken(YarcParser.TEXTURE, 0)

        def ORDER(self):
            return self.getToken(YarcParser.ORDER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_name

    def name(self):
        localctx = YarcParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_name)
        try:
            self.state = 558
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.match(YarcParser.ID)
                pass
            elif token in [YarcParser.UNDERSCORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.match(YarcParser.UNDERSCORE)
                pass
            elif token in [
                YarcParser.SHAPES,
                YarcParser.CAMERA,
                YarcParser.LIGHT,
                YarcParser.STEREO,
                YarcParser.MATERIAL,
            ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 550
                self.primitives()
                pass
            elif token in [YarcParser.VISIBLE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 551
                self.match(YarcParser.VISIBLE)
                pass
            elif token in [YarcParser.SIZE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 552
                self.match(YarcParser.SIZE)
                pass
            elif token in [YarcParser.LOOK_AT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 553
                self.match(YarcParser.LOOK_AT)
                pass
            elif token in [YarcParser.UP_AXIS]:
                self.enterOuterAlt(localctx, 7)
                self.state = 554
                self.match(YarcParser.UP_AXIS)
                pass
            elif token in [YarcParser.SEMANTICS]:
                self.enterOuterAlt(localctx, 8)
                self.state = 555
                self.match(YarcParser.SEMANTICS)
                pass
            elif token in [YarcParser.TEXTURE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 556
                self.match(YarcParser.TEXTURE)
                pass
            elif token in [YarcParser.ORDER]:
                self.enterOuterAlt(localctx, 10)
                self.state = 557
                self.match(YarcParser.ORDER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimitivesContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHAPES(self):
            return self.getToken(YarcParser.SHAPES, 0)

        def CAMERA(self):
            return self.getToken(YarcParser.CAMERA, 0)

        def STEREO(self):
            return self.getToken(YarcParser.STEREO, 0)

        def LIGHT(self):
            return self.getToken(YarcParser.LIGHT, 0)

        def MATERIAL(self):
            return self.getToken(YarcParser.MATERIAL, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_primitives

    def primitives(self):
        localctx = YarcParser.PrimitivesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_primitives)
        self._la = 0  # Token type
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.SHAPES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.match(YarcParser.SHAPES)
                pass
            elif token in [YarcParser.CAMERA, YarcParser.STEREO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.STEREO:
                    self.state = 561
                    self.match(YarcParser.STEREO)

                self.state = 564
                self.match(YarcParser.CAMERA)
                pass
            elif token in [YarcParser.LIGHT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 565
                self.match(YarcParser.LIGHT)
                pass
            elif token in [YarcParser.MATERIAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 566
                self.match(YarcParser.MATERIAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Signed_numberContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YarcParser.NUMBER, 0)

        def MINUS(self):
            return self.getToken(YarcParser.MINUS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_signed_number

    def signed_number(self):
        localctx = YarcParser.Signed_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_signed_number)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 569
                self.match(YarcParser.NUMBER)
                pass
            elif token in [YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
                self.match(YarcParser.MINUS)
                self.state = 571
                self.match(YarcParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 574
            self.test()
            self.state = 586
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.state = 575
                self.comp_for()
                pass
            elif token in [YarcParser.COMMA, YarcParser.RPAREN, YarcParser.RBRACK]:
                self.state = 580
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 62, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 576
                        self.match(YarcParser.COMMA)
                        self.state = 577
                        self.test()
                    self.state = 582
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 62, self._ctx)

                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 583
                    self.match(YarcParser.COMMA)

                pass
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

        def comp_for(self):
            return self.getTypedRuleContext(YarcParser.Comp_forContext, 0)

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
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.expr()
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.state = 589
                self.comp_for()
                pass
            elif token in [YarcParser.COMMA, YarcParser.GREATER_THAN]:
                self.state = 594
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 65, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 590
                        self.match(YarcParser.COMMA)
                        self.state = 591
                        self.expr()
                    self.state = 596
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 65, self._ctx)

                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 597
                    self.match(YarcParser.COMMA)

                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 608
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 602
                self.match(YarcParser.LBRACK)
                self.state = 603
                self.subscriptlist()
                self.state = 604
                self.match(YarcParser.RBRACK)
                pass
            elif token in [YarcParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 606
                self.match(YarcParser.DOT)
                self.state = 607
                self.name()
                pass
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
            self.state = 610
            self.argument()
            self.state = 615
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 69, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 611
                    self.match(YarcParser.COMMA)
                    self.state = 612
                    self.argument()
                self.state = 617
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 69, self._ctx)

            self.state = 619
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 618
                self.match(YarcParser.COMMA)

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
        self._la = 0  # Token type
        try:
            self.state = 629
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 72, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self.test()
                self.state = 623
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.FOR:
                    self.state = 622
                    self.comp_for()

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.test()
                self.state = 626
                self.match(YarcParser.ASSIGN)
                self.state = 627
                self.test()
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
            self.state = 631
            self.subscript_()
            self.state = 636
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 73, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 632
                    self.match(YarcParser.COMMA)
                    self.state = 633
                    self.subscript_()
                self.state = 638
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 73, self._ctx)

            self.state = 640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 639
                self.match(YarcParser.COMMA)

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
            self.state = 653
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 78, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 642
                self.test()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 644
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.SHAPES)
                            | (1 << YarcParser.CAMERA)
                            | (1 << YarcParser.LIGHT)
                            | (1 << YarcParser.STEREO)
                            | (1 << YarcParser.MATERIAL)
                            | (1 << YarcParser.SEMANTICS)
                            | (1 << YarcParser.VISIBLE)
                            | (1 << YarcParser.SIZE)
                            | (1 << YarcParser.LOOK_AT)
                            | (1 << YarcParser.UP_AXIS)
                            | (1 << YarcParser.ORDER)
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 71) & ~0x3F) == 0
                    and (
                        (1 << (_la - 71))
                        & (
                            (1 << (YarcParser.BIT_NOT - 71))
                            | (1 << (YarcParser.ADD - 71))
                            | (1 << (YarcParser.MINUS - 71))
                            | (1 << (YarcParser.LPAREN - 71))
                            | (1 << (YarcParser.LBRACK - 71))
                            | (1 << (YarcParser.LBRACE - 71))
                            | (1 << (YarcParser.LESS_THAN - 71))
                            | (1 << (YarcParser.ID - 71))
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 643
                    self.test()

                self.state = 646
                self.match(YarcParser.COLON)
                self.state = 648
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.SHAPES)
                            | (1 << YarcParser.CAMERA)
                            | (1 << YarcParser.LIGHT)
                            | (1 << YarcParser.STEREO)
                            | (1 << YarcParser.MATERIAL)
                            | (1 << YarcParser.SEMANTICS)
                            | (1 << YarcParser.VISIBLE)
                            | (1 << YarcParser.SIZE)
                            | (1 << YarcParser.LOOK_AT)
                            | (1 << YarcParser.UP_AXIS)
                            | (1 << YarcParser.ORDER)
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 71) & ~0x3F) == 0
                    and (
                        (1 << (_la - 71))
                        & (
                            (1 << (YarcParser.BIT_NOT - 71))
                            | (1 << (YarcParser.ADD - 71))
                            | (1 << (YarcParser.MINUS - 71))
                            | (1 << (YarcParser.LPAREN - 71))
                            | (1 << (YarcParser.LBRACK - 71))
                            | (1 << (YarcParser.LBRACE - 71))
                            | (1 << (YarcParser.LESS_THAN - 71))
                            | (1 << (YarcParser.ID - 71))
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 647
                    self.test()

                self.state = 651
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COLON:
                    self.state = 650
                    self.sliceop()

                pass

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
            self.state = 655
            self.match(YarcParser.COLON)
            self.state = 657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.SHAPES)
                        | (1 << YarcParser.CAMERA)
                        | (1 << YarcParser.LIGHT)
                        | (1 << YarcParser.STEREO)
                        | (1 << YarcParser.MATERIAL)
                        | (1 << YarcParser.SEMANTICS)
                        | (1 << YarcParser.VISIBLE)
                        | (1 << YarcParser.SIZE)
                        | (1 << YarcParser.LOOK_AT)
                        | (1 << YarcParser.UP_AXIS)
                        | (1 << YarcParser.ORDER)
                        | (1 << YarcParser.TEXTURE)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or (
                ((_la - 71) & ~0x3F) == 0
                and (
                    (1 << (_la - 71))
                    & (
                        (1 << (YarcParser.BIT_NOT - 71))
                        | (1 << (YarcParser.ADD - 71))
                        | (1 << (YarcParser.MINUS - 71))
                        | (1 << (YarcParser.LPAREN - 71))
                        | (1 << (YarcParser.LBRACK - 71))
                        | (1 << (YarcParser.LBRACE - 71))
                        | (1 << (YarcParser.LESS_THAN - 71))
                        | (1 << (YarcParser.ID - 71))
                        | (1 << (YarcParser.STRING - 71))
                        | (1 << (YarcParser.NUMBER - 71))
                    )
                )
                != 0
            ):
                self.state = 656
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
            self.state = 659
            self.expr()
            self.state = 664
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 80, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 660
                    self.match(YarcParser.COMMA)
                    self.state = 661
                    self.expr()
                self.state = 666
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 80, self._ctx)

            self.state = 668
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 667
                self.match(YarcParser.COMMA)

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
            self.state = 670
            self.test()
            self.state = 675
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 82, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 671
                    self.match(YarcParser.COMMA)
                    self.state = 672
                    self.test()
                self.state = 677
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 82, self._ctx)

            self.state = 679
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 678
                self.match(YarcParser.COMMA)

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
            self.state = 714
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 90, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 681
                self.test()
                self.state = 682
                self.match(YarcParser.COLON)
                self.state = 683
                self.test()
                self.state = 698
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 684
                    self.comp_for()
                    pass
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 692
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 84, self._ctx)
                    while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 685
                            self.match(YarcParser.COMMA)
                            self.state = 686
                            self.test()
                            self.state = 687
                            self.match(YarcParser.COLON)
                            self.state = 688
                            self.test()
                        self.state = 694
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 84, self._ctx)

                    self.state = 696
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.COMMA:
                        self.state = 695
                        self.match(YarcParser.COMMA)

                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 700
                self.test()
                self.state = 712
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 701
                    self.comp_for()
                    pass
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 706
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 87, self._ctx)
                    while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 702
                            self.match(YarcParser.COMMA)
                            self.state = 703
                            self.test()
                        self.state = 708
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 87, self._ctx)

                    self.state = 710
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.COMMA:
                        self.state = 709
                        self.match(YarcParser.COMMA)

                    pass
                else:
                    raise NoViableAltException(self)

                pass

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
            self.state = 718
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.comp_for()
                pass
            elif token in [YarcParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 717
                self.comp_if()
                pass
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
            self.state = 720
            self.match(YarcParser.FOR)
            self.state = 721
            self.exprlist()
            self.state = 722
            self.match(YarcParser.IN)
            self.state = 723
            self.or_test()
            self.state = 725
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 724
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
            self.state = 727
            self.match(YarcParser.IF)
            self.state = 728
            self.test_nocond()
            self.state = 730
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 729
                self.comp_iter()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
