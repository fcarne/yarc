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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3y")
        buf.write("\u01fe\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write('\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%\4&\t')
        buf.write("&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\7\2_\n\2\f\2\16\2b\13\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\7\3j\n\3\f\3\16\3m\13\3\3\3\5\3p\n\3\3\3\3\3\7\3t\n\3")
        buf.write("\f\3\16\3w\13\3\3\3\5\3z\n\3\3\4\7\4}\n\4\f\4\16\4\u0080")
        buf.write("\13\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\6\6\u008a\n\6\r")
        buf.write("\6\16\6\u008b\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0096")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\3\b\6\b\u009e\n\b\r\b\16\b\u009f")
        buf.write("\3\b\3\b\5\b\u00a4\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\6\13\u00ae\n\13\r\13\16\13\u00af\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00b8\n\f\3\r\3\r\3\16\3\16\3\16\7\16\u00bf\n")
        buf.write("\16\f\16\16\16\u00c2\13\16\3\17\3\17\3\17\7\17\u00c7\n")
        buf.write("\17\f\17\16\17\u00ca\13\17\3\20\3\20\3\20\5\20\u00cf\n")
        buf.write("\20\3\21\3\21\3\21\3\21\7\21\u00d5\n\21\f\21\16\21\u00d8")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00e6\n\22\3\23\3\23\3\23\7\23\u00eb")
        buf.write("\n\23\f\23\16\23\u00ee\13\23\3\24\3\24\3\24\7\24\u00f3")
        buf.write("\n\24\f\24\16\24\u00f6\13\24\3\25\3\25\3\25\7\25\u00fb")
        buf.write("\n\25\f\25\16\25\u00fe\13\25\3\26\3\26\3\26\7\26\u0103")
        buf.write("\n\26\f\26\16\26\u0106\13\26\3\27\3\27\3\27\7\27\u010b")
        buf.write("\n\27\f\27\16\27\u010e\13\27\3\30\3\30\3\30\7\30\u0113")
        buf.write("\n\30\f\30\16\30\u0116\13\30\3\31\3\31\3\31\5\31\u011b")
        buf.write("\n\31\3\32\3\32\3\32\5\32\u0120\n\32\3\33\3\33\7\33\u0124")
        buf.write("\n\33\f\33\16\33\u0127\13\33\3\34\3\34\5\34\u012b\n\34")
        buf.write("\3\34\3\34\3\34\5\34\u0130\n\34\3\34\3\34\3\34\5\34\u0135")
        buf.write("\n\34\3\34\3\34\3\34\5\34\u013a\n\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\5\34\u0144\n\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u014f\n\35\3\36\3")
        buf.write("\36\5\36\u0153\n\36\3\36\3\36\3\36\5\36\u0158\n\36\3\37")
        buf.write("\3\37\3\37\5\37\u015d\n\37\3 \3 \3 \3 \7 \u0163\n \f ")
        buf.write("\16 \u0166\13 \3 \5 \u0169\n \5 \u016b\n \3!\3!\5!\u016f")
        buf.write('\n!\3!\3!\3!\3!\3!\3!\3!\5!\u0178\n!\3"\3"\3"\7"\u017d')
        buf.write('\n"\f"\16"\u0180\13"\3"\5"\u0183\n"\3#\3#\5#\u0187')
        buf.write("\n#\3#\3#\3#\3#\5#\u018d\n#\3$\3$\3$\7$\u0192\n$\f$\16")
        buf.write("$\u0195\13$\3$\5$\u0198\n$\3%\3%\5%\u019c\n%\3%\3%\5%")
        buf.write("\u01a0\n%\3%\5%\u01a3\n%\5%\u01a5\n%\3&\3&\5&\u01a9\n")
        buf.write("&\3'\3'\3'\7'\u01ae\n'\f'\16'\u01b1\13'\3'\5")
        buf.write("'\u01b4\n'\3(\3(\3(\7(\u01b9\n(\f(\16(\u01bc\13(\3(")
        buf.write("\5(\u01bf\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u01ca\n)\f")
        buf.write(")\16)\u01cd\13)\3)\5)\u01d0\n)\5)\u01d2\n)\3)\3)\3)\3")
        buf.write(")\7)\u01d8\n)\f)\16)\u01db\13)\3)\5)\u01de\n)\5)\u01e0")
        buf.write("\n)\5)\u01e2\n)\3*\3*\5*\u01e6\n*\3+\3+\3+\3+\3+\5+\u01ed")
        buf.write("\n+\3,\3,\3,\5,\u01f2\n,\3-\3-\3-\5-\u01f7\n-\3-\3-\3")
        buf.write("-\3.\3.\3.\2\2/\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(' "$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\2\7\3\2JK\3\2')
        buf.write("LM\3\2NQ\4\2IILM\3\2`k\2\u022f\2\\\3\2\2\2\4f\3\2\2\2")
        buf.write("\6~\3\2\2\2\b\u0081\3\2\2\2\n\u0084\3\2\2\2\f\u0095\3")
        buf.write("\2\2\2\16\u0097\3\2\2\2\20\u00a5\3\2\2\2\22\u00a7\3\2")
        buf.write("\2\2\24\u00ad\3\2\2\2\26\u00b1\3\2\2\2\30\u00b9\3\2\2")
        buf.write("\2\32\u00bb\3\2\2\2\34\u00c3\3\2\2\2\36\u00ce\3\2\2\2")
        buf.write(' \u00d0\3\2\2\2"\u00e5\3\2\2\2$\u00e7\3\2\2\2&\u00ef')
        buf.write("\3\2\2\2(\u00f7\3\2\2\2*\u00ff\3\2\2\2,\u0107\3\2\2\2")
        buf.write(".\u010f\3\2\2\2\60\u011a\3\2\2\2\62\u011c\3\2\2\2\64\u0121")
        buf.write("\3\2\2\2\66\u0143\3\2\2\28\u014e\3\2\2\2:\u0157\3\2\2")
        buf.write("\2<\u015c\3\2\2\2>\u015e\3\2\2\2@\u0177\3\2\2\2B\u0179")
        buf.write("\3\2\2\2D\u018c\3\2\2\2F\u018e\3\2\2\2H\u01a4\3\2\2\2")
        buf.write("J\u01a6\3\2\2\2L\u01aa\3\2\2\2N\u01b5\3\2\2\2P\u01e1\3")
        buf.write("\2\2\2R\u01e5\3\2\2\2T\u01e7\3\2\2\2V\u01ee\3\2\2\2X\u01f3")
        buf.write("\3\2\2\2Z\u01fb\3\2\2\2\\`\5\4\3\2]_\7w\2\2^]\3\2\2\2")
        buf.write("_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2b`\3\2\2\2cd\5")
        buf.write("\6\4\2de\7\2\2\3e\3\3\2\2\2fk\5\b\5\2gj\5X-\2hj\7w\2\2")
        buf.write("ig\3\2\2\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2lo\3")
        buf.write("\2\2\2mk\3\2\2\2np\5\n\6\2on\3\2\2\2op\3\2\2\2pu\3\2\2")
        buf.write("\2qt\5X-\2rt\7w\2\2sq\3\2\2\2sr\3\2\2\2tw\3\2\2\2us\3")
        buf.write("\2\2\2uv\3\2\2\2vy\3\2\2\2wu\3\2\2\2xz\5\16\b\2yx\3\2")
        buf.write("\2\2yz\3\2\2\2z\5\3\2\2\2{}\5\24\13\2|{\3\2\2\2}\u0080")
        buf.write("\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\7\3\2\2\2\u0080~\3")
        buf.write("\2\2\2\u0081\u0082\7\5\2\2\u0082\u0083\58\35\2\u0083\t")
        buf.write("\3\2\2\2\u0084\u0085\7\6\2\2\u0085\u0086\7C\2\2\u0086")
        buf.write("\u0087\7w\2\2\u0087\u0089\7\3\2\2\u0088\u008a\5\f\7\2")
        buf.write("\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089\3")
        buf.write("\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e")
        buf.write("\7\4\2\2\u008e\13\3\2\2\2\u008f\u0096\5\22\n\2\u0090\u0091")
        buf.write("\7\b\2\2\u0091\u0092\7E\2\2\u0092\u0093\5\26\f\2\u0093")
        buf.write("\u0094\7w\2\2\u0094\u0096\3\2\2\2\u0095\u008f\3\2\2\2")
        buf.write("\u0095\u0090\3\2\2\2\u0096\r\3\2\2\2\u0097\u0098\7\7\2")
        buf.write("\2\u0098\u00a3\7n\2\2\u0099\u009a\7C\2\2\u009a\u009b\7")
        buf.write("w\2\2\u009b\u009d\7\3\2\2\u009c\u009e\5\20\t\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7\4\2\2")
        buf.write("\u00a2\u00a4\3\2\2\2\u00a3\u0099\3\2\2\2\u00a3\u00a4\3")
        buf.write("\2\2\2\u00a4\17\3\2\2\2\u00a5\u00a6\5\22\n\2\u00a6\21")
        buf.write("\3\2\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7E\2\2\u00a9\u00aa")
        buf.write("\5\26\f\2\u00aa\u00ab\7w\2\2\u00ab\23\3\2\2\2\u00ac\u00ae")
        buf.write("\7\\\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\25\3\2\2\2\u00b1")
        buf.write("\u00b7\5\32\16\2\u00b2\u00b3\7\66\2\2\u00b3\u00b4\5\32")
        buf.write("\16\2\u00b4\u00b5\7\63\2\2\u00b5\u00b6\5\26\f\2\u00b6")
        buf.write("\u00b8\3\2\2\2\u00b7\u00b2\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\27\3\2\2\2\u00b9\u00ba\5\32\16\2\u00ba\31\3\2\2")
        buf.write("\2\u00bb\u00c0\5\34\17\2\u00bc\u00bd\7;\2\2\u00bd\u00bf")
        buf.write("\5\34\17\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\33\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c8\5\36\20\2\u00c4\u00c5\7\61")
        buf.write("\2\2\u00c5\u00c7\5\36\20\2\u00c6\u00c4\3\2\2\2\u00c7\u00ca")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\35\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cc\7:\2\2\u00cc")
        buf.write("\u00cf\5\36\20\2\u00cd\u00cf\5 \21\2\u00ce\u00cb\3\2\2")
        buf.write("\2\u00ce\u00cd\3\2\2\2\u00cf\37\3\2\2\2\u00d0\u00d6\5")
        buf.write('$\23\2\u00d1\u00d2\5"\22\2\u00d2\u00d3\5$\23\2\u00d3')
        buf.write("\u00d5\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d5\u00d8\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7!\3\2\2")
        buf.write("\2\u00d8\u00d6\3\2\2\2\u00d9\u00e6\7Z\2\2\u00da\u00e6")
        buf.write("\7[\2\2\u00db\u00e6\7\\\2\2\u00dc\u00e6\7]\2\2\u00dd\u00e6")
        buf.write("\7^\2\2\u00de\u00e6\7_\2\2\u00df\u00e6\7\67\2\2\u00e0")
        buf.write("\u00e1\7:\2\2\u00e1\u00e6\7\67\2\2\u00e2\u00e6\78\2\2")
        buf.write("\u00e3\u00e4\78\2\2\u00e4\u00e6\7:\2\2\u00e5\u00d9\3\2")
        buf.write("\2\2\u00e5\u00da\3\2\2\2\u00e5\u00db\3\2\2\2\u00e5\u00dc")
        buf.write("\3\2\2\2\u00e5\u00dd\3\2\2\2\u00e5\u00de\3\2\2\2\u00e5")
        buf.write("\u00df\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e2\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e6#\3\2\2\2\u00e7\u00ec\5&\24")
        buf.write("\2\u00e8\u00e9\7F\2\2\u00e9\u00eb\5&\24\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed%\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef")
        buf.write("\u00f4\5(\25\2\u00f0\u00f1\7G\2\2\u00f1\u00f3\5(\25\2")
        buf.write("\u00f2\u00f0\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3")
        buf.write("\2\2\2\u00f4\u00f5\3\2\2\2\u00f5'\3\2\2\2\u00f6\u00f4")
        buf.write("\3\2\2\2\u00f7\u00fc\5*\26\2\u00f8\u00f9\7H\2\2\u00f9")
        buf.write("\u00fb\5*\26\2\u00fa\u00f8\3\2\2\2\u00fb\u00fe\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd)\3\2\2")
        buf.write("\2\u00fe\u00fc\3\2\2\2\u00ff\u0104\5,\27\2\u0100\u0101")
        buf.write("\t\2\2\2\u0101\u0103\5,\27\2\u0102\u0100\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105+\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u010c\5.\30")
        buf.write("\2\u0108\u0109\t\3\2\2\u0109\u010b\5.\30\2\u010a\u0108")
        buf.write("\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d-\3\2\2\2\u010e\u010c\3\2\2\2\u010f")
        buf.write("\u0114\5\60\31\2\u0110\u0111\t\4\2\2\u0111\u0113\5\60")
        buf.write("\31\2\u0112\u0110\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115/\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0117\u0118\t\5\2\2\u0118\u011b\5\60\31\2\u0119")
        buf.write("\u011b\5\62\32\2\u011a\u0117\3\2\2\2\u011a\u0119\3\2\2")
        buf.write("\2\u011b\61\3\2\2\2\u011c\u011f\5\64\33\2\u011d\u011e")
        buf.write("\7R\2\2\u011e\u0120\5\60\31\2\u011f\u011d\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\63\3\2\2\2\u0121\u0125\5\66\34\2")
        buf.write("\u0122\u0124\5@!\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2")
        buf.write("\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\65")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\7T\2\2\u0129")
        buf.write("\u012b\5> \2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\u012c\3\2\2\2\u012c\u0144\7U\2\2\u012d\u012f\7V\2\2\u012e")
        buf.write("\u0130\5> \2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0144\7W\2\2\u0132\u0134\7Z\2\2\u0133")
        buf.write("\u0135\5> \2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0144\7[\2\2\u0137\u0139\7X\2\2\u0138")
        buf.write("\u013a\5P)\2\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u0144\7Y\2\2\u013c\u0144\58\35\2")
        buf.write("\u013d\u0144\5<\37\2\u013e\u0144\7l\2\2\u013f\u0144\7")
        buf.write("A\2\2\u0140\u0144\79\2\2\u0141\u0144\7=\2\2\u0142\u0144")
        buf.write("\7\64\2\2\u0143\u0128\3\2\2\2\u0143\u012d\3\2\2\2\u0143")
        buf.write("\u0132\3\2\2\2\u0143\u0137\3\2\2\2\u0143\u013c\3\2\2\2")
        buf.write("\u0143\u013d\3\2\2\2\u0143\u013e\3\2\2\2\u0143\u013f\3")
        buf.write("\2\2\2\u0143\u0140\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0142")
        buf.write("\3\2\2\2\u0144\67\3\2\2\2\u0145\u014f\7n\2\2\u0146\u014f")
        buf.write("\7>\2\2\u0147\u014f\5:\36\2\u0148\u014f\7\34\2\2\u0149")
        buf.write("\u014f\7\35\2\2\u014a\u014f\7\36\2\2\u014b\u014f\7\37")
        buf.write("\2\2\u014c\u014f\7\33\2\2\u014d\u014f\7$\2\2\u014e\u0145")
        buf.write("\3\2\2\2\u014e\u0146\3\2\2\2\u014e\u0147\3\2\2\2\u014e")
        buf.write("\u0148\3\2\2\2\u014e\u0149\3\2\2\2\u014e\u014a\3\2\2\2")
        buf.write("\u014e\u014b\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3")
        buf.write("\2\2\2\u014f9\3\2\2\2\u0150\u0158\7\t\2\2\u0151\u0153")
        buf.write("\7\f\2\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0158\7\n\2\2\u0155\u0158\7\13\2")
        buf.write("\2\u0156\u0158\7\r\2\2\u0157\u0150\3\2\2\2\u0157\u0152")
        buf.write("\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write(";\3\2\2\2\u0159\u015d\7m\2\2\u015a\u015b\7M\2\2\u015b")
        buf.write("\u015d\7m\2\2\u015c\u0159\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015d=\3\2\2\2\u015e\u016a\5\26\f\2\u015f\u016b\5T+\2")
        buf.write("\u0160\u0161\7B\2\2\u0161\u0163\5\26\f\2\u0162\u0160\3")
        buf.write("\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0167")
        buf.write("\u0169\7B\2\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169\u016b\3\2\2\2\u016a\u015f\3\2\2\2\u016a\u0164\3")
        buf.write("\2\2\2\u016b?\3\2\2\2\u016c\u016e\7T\2\2\u016d\u016f\5")
        buf.write('B"\2\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170')
        buf.write("\3\2\2\2\u0170\u0178\7U\2\2\u0171\u0172\7V\2\2\u0172\u0173")
        buf.write("\5F$\2\u0173\u0174\7W\2\2\u0174\u0178\3\2\2\2\u0175\u0176")
        buf.write("\7?\2\2\u0176\u0178\58\35\2\u0177\u016c\3\2\2\2\u0177")
        buf.write("\u0171\3\2\2\2\u0177\u0175\3\2\2\2\u0178A\3\2\2\2\u0179")
        buf.write("\u017e\5D#\2\u017a\u017b\7B\2\2\u017b\u017d\5D#\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0181\u0183\7B\2\2\u0182\u0181\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183C\3\2\2\2\u0184\u0186\5\26\f\2\u0185\u0187")
        buf.write("\5T+\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u018d")
        buf.write("\3\2\2\2\u0188\u0189\5\26\f\2\u0189\u018a\7E\2\2\u018a")
        buf.write("\u018b\5\26\f\2\u018b\u018d\3\2\2\2\u018c\u0184\3\2\2")
        buf.write("\2\u018c\u0188\3\2\2\2\u018dE\3\2\2\2\u018e\u0193\5H%")
        buf.write("\2\u018f\u0190\7B\2\2\u0190\u0192\5H%\2\u0191\u018f\3")
        buf.write("\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194")
        buf.write("\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0196")
        buf.write("\u0198\7B\2\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198G\3\2\2\2\u0199\u01a5\5\26\f\2\u019a\u019c\5\26")
        buf.write("\f\2\u019b\u019a\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019f\7C\2\2\u019e\u01a0\5\26\f\2\u019f")
        buf.write("\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2")
        buf.write("\u01a1\u01a3\5J&\2\u01a2\u01a1\3\2\2\2\u01a2\u01a3\3\2")
        buf.write("\2\2\u01a3\u01a5\3\2\2\2\u01a4\u0199\3\2\2\2\u01a4\u019b")
        buf.write("\3\2\2\2\u01a5I\3\2\2\2\u01a6\u01a8\7C\2\2\u01a7\u01a9")
        buf.write("\5\26\f\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("K\3\2\2\2\u01aa\u01af\5$\23\2\u01ab\u01ac\7B\2\2\u01ac")
        buf.write("\u01ae\5$\23\2\u01ad\u01ab\3\2\2\2\u01ae\u01b1\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b3\3")
        buf.write("\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b4\7B\2\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4M\3\2\2\2\u01b5\u01ba")
        buf.write("\5\26\f\2\u01b6\u01b7\7B\2\2\u01b7\u01b9\5\26\f\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01ba\u01bb\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3")
        buf.write("\2\2\2\u01bd\u01bf\7B\2\2\u01be\u01bd\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bfO\3\2\2\2\u01c0\u01c1\5\26\f\2\u01c1\u01c2")
        buf.write("\7C\2\2\u01c2\u01d1\5\26\f\2\u01c3\u01d2\5T+\2\u01c4\u01c5")
        buf.write("\7B\2\2\u01c5\u01c6\5\26\f\2\u01c6\u01c7\7C\2\2\u01c7")
        buf.write("\u01c8\5\26\f\2\u01c8\u01ca\3\2\2\2\u01c9\u01c4\3\2\2")
        buf.write("\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc")
        buf.write("\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce")
        buf.write("\u01d0\7B\2\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u01d2\3\2\2\2\u01d1\u01c3\3\2\2\2\u01d1\u01cb\3")
        buf.write("\2\2\2\u01d2\u01e2\3\2\2\2\u01d3\u01df\5\26\f\2\u01d4")
        buf.write("\u01e0\5T+\2\u01d5\u01d6\7B\2\2\u01d6\u01d8\5\26\f\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3")
        buf.write("\2\2\2\u01dc\u01de\7B\2\2\u01dd\u01dc\3\2\2\2\u01dd\u01de")
        buf.write("\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01d4\3\2\2\2\u01df")
        buf.write("\u01d9\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01c0\3\2\2\2")
        buf.write("\u01e1\u01d3\3\2\2\2\u01e2Q\3\2\2\2\u01e3\u01e6\5T+\2")
        buf.write("\u01e4\u01e6\5V,\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4\3\2")
        buf.write("\2\2\u01e6S\3\2\2\2\u01e7\u01e8\7\65\2\2\u01e8\u01e9\5")
        buf.write("L'\2\u01e9\u01ea\7\67\2\2\u01ea\u01ec\5\32\16\2\u01eb")
        buf.write("\u01ed\5R*\2\u01ec\u01eb\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("U\3\2\2\2\u01ee\u01ef\7\66\2\2\u01ef\u01f1\5\30\r\2\u01f0")
        buf.write("\u01f2\5R*\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("W\3\2\2\2\u01f3\u01f6\5N(\2\u01f4\u01f7\5Z.\2\u01f5\u01f7")
        buf.write("\7E\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01f9\5N(\2\u01f9\u01fa\7w\2\2\u01fa")
        buf.write("Y\3\2\2\2\u01fb\u01fc\t\6\2\2\u01fc[\3\2\2\2F`ikosuy~")
        buf.write("\u008b\u0095\u009f\u00a3\u00af\u00b7\u00c0\u00c8\u00ce")
        buf.write("\u00d6\u00e5\u00ec\u00f4\u00fc\u0104\u010c\u0114\u011a")
        buf.write("\u011f\u0125\u012a\u012f\u0134\u0139\u0143\u014e\u0152")
        buf.write("\u0157\u015c\u0164\u0168\u016a\u016e\u0177\u017e\u0182")
        buf.write("\u0186\u018c\u0193\u0197\u019b\u019f\u01a2\u01a4\u01a8")
        buf.write("\u01af\u01b3\u01ba\u01be\u01cb\u01cf\u01d1\u01d9\u01dd")
        buf.write("\u01df\u01e1\u01e5\u01ec\u01f1\u01f6")
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
        "'create'",
        "'instantiate'",
        "'group'",
        "'open'",
        "'get'",
        "'fetch'",
        "<INVALID>",
        "<INVALID>",
        "'set'",
        "'translate'",
        "'rotate'",
        "'scale'",
        "'semantics'",
        "'visible'",
        "'size'",
        "'look_at'",
        "'up_axis'",
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
        "'->'",
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
        "CREATE",
        "INSTANTIATE",
        "GROUP",
        "OPEN",
        "GET",
        "FETCH",
        "MATCH",
        "EDIT",
        "SET",
        "TRANSLATE",
        "ROTATE",
        "SCALE",
        "SEMANTICS",
        "VISIBLE",
        "SIZE",
        "LOOK_AT",
        "UP_AXIS",
        "AXIS",
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
        "ARROW",
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
        "STRING",
        "NUMBER",
        "ID",
        "OPTION_ID",
        "STRING_LITERAL",
        "INTEGER",
        "DECIMAL_INTEGER",
        "OCT_INTEGER",
        "HEX_INTEGER",
        "BIN_INTEGER",
        "FLOAT_NUMBER",
        "NEWLINE",
        "SKIP_",
        "UNKNOWN",
    ]

    RULE_file_input = 0
    RULE_head = 1
    RULE_body = 2
    RULE_header = 3
    RULE_settings = 4
    RULE_setting = 5
    RULE_writer = 6
    RULE_writer_attr = 7
    RULE_option = 8
    RULE_stmts = 9
    RULE_test = 10
    RULE_test_nocond = 11
    RULE_or_test = 12
    RULE_and_test = 13
    RULE_not_test = 14
    RULE_comparison = 15
    RULE_comp_op = 16
    RULE_expr = 17
    RULE_xor_expr = 18
    RULE_and_expr = 19
    RULE_shift_expr = 20
    RULE_arith_expr = 21
    RULE_term = 22
    RULE_factor = 23
    RULE_power = 24
    RULE_atom_expr = 25
    RULE_atom = 26
    RULE_name = 27
    RULE_primitives = 28
    RULE_signed_number = 29
    RULE_testlist_comp = 30
    RULE_trailer = 31
    RULE_arglist = 32
    RULE_argument = 33
    RULE_subscriptlist = 34
    RULE_subscript_ = 35
    RULE_sliceop = 36
    RULE_exprlist = 37
    RULE_testlist = 38
    RULE_dictorsetmaker = 39
    RULE_comp_iter = 40
    RULE_comp_for = 41
    RULE_comp_if = 42
    RULE_expr_stmt = 43
    RULE_augassign = 44

    ruleNames = [
        "file_input",
        "head",
        "body",
        "header",
        "settings",
        "setting",
        "writer",
        "writer_attr",
        "option",
        "stmts",
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
        "trailer",
        "arglist",
        "argument",
        "subscriptlist",
        "subscript_",
        "sliceop",
        "exprlist",
        "testlist",
        "dictorsetmaker",
        "comp_iter",
        "comp_for",
        "comp_if",
        "expr_stmt",
        "augassign",
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
    CREATE = 13
    INSTANTIATE = 14
    GROUP = 15
    OPEN = 16
    GET = 17
    FETCH = 18
    MATCH = 19
    EDIT = 20
    SET = 21
    TRANSLATE = 22
    ROTATE = 23
    SCALE = 24
    SEMANTICS = 25
    VISIBLE = 26
    SIZE = 27
    LOOK_AT = 28
    UP_AXIS = 29
    AXIS = 30
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
    ARROW = 81
    LPAREN = 82
    RPAREN = 83
    LBRACK = 84
    RBRACK = 85
    LBRACE = 86
    RBRACE = 87
    LESS_THAN = 88
    GREATER_THAN = 89
    EQUALS = 90
    GT_EQ = 91
    LT_EQ = 92
    NOT_EQ = 93
    ADD_ASSIGN = 94
    SUB_ASSIGN = 95
    MULT_ASSIGN = 96
    DIV_ASSIGN = 97
    MOD_ASSIGN = 98
    AND_ASSIGN = 99
    OR_ASSIGN = 100
    XOR_ASSIGN = 101
    LSHIFT_ASSIGN = 102
    RSHIFT_ASSIGN = 103
    POWER_ASSIGN = 104
    IDIV_ASSIGN = 105
    STRING = 106
    NUMBER = 107
    ID = 108
    OPTION_ID = 109
    STRING_LITERAL = 110
    INTEGER = 111
    DECIMAL_INTEGER = 112
    OCT_INTEGER = 113
    HEX_INTEGER = 114
    BIN_INTEGER = 115
    FLOAT_NUMBER = 116
    NEWLINE = 117
    SKIP_ = 118
    UNKNOWN = 119

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class File_inputContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def head(self):
            return self.getTypedRuleContext(YarcParser.HeadContext, 0)

        def body(self):
            return self.getTypedRuleContext(YarcParser.BodyContext, 0)

        def EOF(self):
            return self.getToken(YarcParser.EOF, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.NEWLINE)
            else:
                return self.getToken(YarcParser.NEWLINE, i)

        def getRuleIndex(self):
            return YarcParser.RULE_file_input

    def file_input(self):
        localctx = YarcParser.File_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_input)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.head()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.NEWLINE:
                self.state = 91
                self.match(YarcParser.NEWLINE)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.body()
            self.state = 98
            self.match(YarcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeadContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(YarcParser.HeaderContext, 0)

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

        def settings(self):
            return self.getTypedRuleContext(YarcParser.SettingsContext, 0)

        def writer(self):
            return self.getTypedRuleContext(YarcParser.WriterContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_head

    def head(self):
        localctx = YarcParser.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_head)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.header()
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 103
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
                        YarcParser.TEXTURE,
                        YarcParser.FALSE,
                        YarcParser.NONE,
                        YarcParser.NOT,
                        YarcParser.TRUE,
                        YarcParser.UNDERSCORE,
                        YarcParser.ELLIPSIS,
                        YarcParser.BIT_NOT,
                        YarcParser.ADD,
                        YarcParser.MINUS,
                        YarcParser.LPAREN,
                        YarcParser.LBRACK,
                        YarcParser.LBRACE,
                        YarcParser.LESS_THAN,
                        YarcParser.STRING,
                        YarcParser.NUMBER,
                        YarcParser.ID,
                    ]:
                        self.state = 101
                        self.expr_stmt()
                        pass
                    elif token in [YarcParser.NEWLINE]:
                        self.state = 102
                        self.match(YarcParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)

                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.SETTINGS:
                self.state = 108
                self.settings()

            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
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
                        YarcParser.TEXTURE,
                        YarcParser.FALSE,
                        YarcParser.NONE,
                        YarcParser.NOT,
                        YarcParser.TRUE,
                        YarcParser.UNDERSCORE,
                        YarcParser.ELLIPSIS,
                        YarcParser.BIT_NOT,
                        YarcParser.ADD,
                        YarcParser.MINUS,
                        YarcParser.LPAREN,
                        YarcParser.LBRACK,
                        YarcParser.LBRACE,
                        YarcParser.LESS_THAN,
                        YarcParser.STRING,
                        YarcParser.NUMBER,
                        YarcParser.ID,
                    ]:
                        self.state = 111
                        self.expr_stmt()
                        pass
                    elif token in [YarcParser.NEWLINE]:
                        self.state = 112
                        self.match(YarcParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)

                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.WRITER:
                self.state = 118
                self.writer()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmts(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.StmtsContext)
            else:
                return self.getTypedRuleContext(YarcParser.StmtsContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_body

    def body(self):
        localctx = YarcParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.EQUALS:
                self.state = 121
                self.stmts()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def SCENARIO(self):
            return self.getToken(YarcParser.SCENARIO, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_header

    def header(self):
        localctx = YarcParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(YarcParser.SCENARIO)
            self.state = 128
            self.name()
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
            self.state = 130
            self.match(YarcParser.SETTINGS)
            self.state = 131
            self.match(YarcParser.COLON)
            self.state = 132
            self.match(YarcParser.NEWLINE)
            self.state = 133
            self.match(YarcParser.INDENT)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.setting()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.LIB or _la == YarcParser.ID):
                    break

            self.state = 139
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

        def option(self):
            return self.getTypedRuleContext(YarcParser.OptionContext, 0)

        def LIB(self):
            return self.getToken(YarcParser.LIB, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_setting

    def setting(self):
        localctx = YarcParser.SettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_setting)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.option()
                pass
            elif token in [YarcParser.LIB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(YarcParser.LIB)
                self.state = 143
                self.match(YarcParser.ASSIGN)
                self.state = 144
                self.test()
                self.state = 145
                self.match(YarcParser.NEWLINE)
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

        def writer_attr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Writer_attrContext)
            else:
                return self.getTypedRuleContext(YarcParser.Writer_attrContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_writer

    def writer(self):
        localctx = YarcParser.WriterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_writer)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(YarcParser.WRITER)
            self.state = 150
            self.match(YarcParser.ID)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 151
                self.match(YarcParser.COLON)
                self.state = 152
                self.match(YarcParser.NEWLINE)
                self.state = 153
                self.match(YarcParser.INDENT)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 154
                    self.writer_attr()
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == YarcParser.ID):
                        break

                self.state = 159
                self.match(YarcParser.DEDENT)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Writer_attrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option(self):
            return self.getTypedRuleContext(YarcParser.OptionContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_writer_attr

    def writer_attr(self):
        localctx = YarcParser.Writer_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_writer_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.option()
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
        self.enterRule(localctx, 16, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(YarcParser.ID)
            self.state = 166
            self.match(YarcParser.ASSIGN)
            self.state = 167
            self.test()
            self.state = 168
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

        def EQUALS(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.EQUALS)
            else:
                return self.getToken(YarcParser.EQUALS, i)

        def getRuleIndex(self):
            return YarcParser.RULE_stmts

    def stmts(self):
        localctx = YarcParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 170
                    self.match(YarcParser.EQUALS)

                else:
                    raise NoViableAltException(self)
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 12, self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.or_test()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.IF:
                self.state = 176
                self.match(YarcParser.IF)
                self.state = 177
                self.or_test()
                self.state = 178
                self.match(YarcParser.ELSE)
                self.state = 179
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
        self.enterRule(localctx, 22, self.RULE_test_nocond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
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
        self.enterRule(localctx, 24, self.RULE_or_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.and_test()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.OR:
                self.state = 186
                self.match(YarcParser.OR)
                self.state = 187
                self.and_test()
                self.state = 192
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
        self.enterRule(localctx, 26, self.RULE_and_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.not_test()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.AND:
                self.state = 194
                self.match(YarcParser.AND)
                self.state = 195
                self.not_test()
                self.state = 200
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
        self.enterRule(localctx, 28, self.RULE_not_test)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(YarcParser.NOT)
                self.state = 202
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
                YarcParser.TEXTURE,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.ELLIPSIS,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LESS_THAN,
                YarcParser.STRING,
                YarcParser.NUMBER,
                YarcParser.ID,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
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
        self.enterRule(localctx, 30, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expr()
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 17, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 207
                    self.comp_op()
                    self.state = 208
                    self.expr()
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 17, self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_comp_op)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 18, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(YarcParser.LESS_THAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(YarcParser.GREATER_THAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.match(YarcParser.EQUALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 218
                self.match(YarcParser.GT_EQ)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 219
                self.match(YarcParser.LT_EQ)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 220
                self.match(YarcParser.NOT_EQ)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 221
                self.match(YarcParser.IN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 222
                self.match(YarcParser.NOT)
                self.state = 223
                self.match(YarcParser.IN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 224
                self.match(YarcParser.IS)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 225
                self.match(YarcParser.IS)
                self.state = 226
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
        self.enterRule(localctx, 34, self.RULE_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.xor_expr()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_OR:
                self.state = 230
                self.match(YarcParser.BIT_OR)
                self.state = 231
                self.xor_expr()
                self.state = 236
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
        self.enterRule(localctx, 36, self.RULE_xor_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.and_expr()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.XOR:
                self.state = 238
                self.match(YarcParser.XOR)
                self.state = 239
                self.and_expr()
                self.state = 244
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
        self.enterRule(localctx, 38, self.RULE_and_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.shift_expr()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_AND:
                self.state = 246
                self.match(YarcParser.BIT_AND)
                self.state = 247
                self.shift_expr()
                self.state = 252
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
        self.enterRule(localctx, 40, self.RULE_shift_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.arith_expr()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT:
                self.state = 254
                _la = self._input.LA(1)
                if not (_la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.arith_expr()
                self.state = 260
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
        self.enterRule(localctx, 42, self.RULE_arith_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.term()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.ADD or _la == YarcParser.MINUS:
                self.state = 262
                _la = self._input.LA(1)
                if not (_la == YarcParser.ADD or _la == YarcParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.term()
                self.state = 268
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
        self.enterRule(localctx, 44, self.RULE_term)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.factor()
            self.state = 274
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
                self.state = 270
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
                self.state = 271
                self.factor()
                self.state = 276
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
        self.enterRule(localctx, 46, self.RULE_factor)
        self._la = 0  # Token type
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 25, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
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
                self.state = 278
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
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
        self.enterRule(localctx, 48, self.RULE_power)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.atom_expr()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.POWER:
                self.state = 283
                self.match(YarcParser.POWER)
                self.state = 284
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
        self.enterRule(localctx, 50, self.RULE_atom_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.atom()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la - 61) & ~0x3F) == 0 and (
                (1 << (_la - 61))
                & (
                    (1 << (YarcParser.DOT - 61))
                    | (1 << (YarcParser.LPAREN - 61))
                    | (1 << (YarcParser.LBRACK - 61))
                )
            ) != 0:
                self.state = 288
                self.trailer()
                self.state = 293
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

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def testlist_comp(self):
            return self.getTypedRuleContext(YarcParser.Testlist_compContext, 0)

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def LESS_THAN(self):
            return self.getToken(YarcParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(YarcParser.GREATER_THAN, 0)

        def LBRACE(self):
            return self.getToken(YarcParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YarcParser.RBRACE, 0)

        def dictorsetmaker(self):
            return self.getTypedRuleContext(YarcParser.DictorsetmakerContext, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def signed_number(self):
            return self.getTypedRuleContext(YarcParser.Signed_numberContext, 0)

        def STRING(self):
            return self.getToken(YarcParser.STRING, 0)

        def ELLIPSIS(self):
            return self.getToken(YarcParser.ELLIPSIS, 0)

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
        self.enterRule(localctx, 52, self.RULE_atom)
        self._la = 0  # Token type
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(YarcParser.LPAREN)
                self.state = 296
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
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                            | (1 << YarcParser.ELLIPSIS)
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
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                            | (1 << (YarcParser.ID - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 295
                    self.testlist_comp()

                self.state = 298
                self.match(YarcParser.RPAREN)
                pass
            elif token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(YarcParser.LBRACK)
                self.state = 301
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
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                            | (1 << YarcParser.ELLIPSIS)
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
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                            | (1 << (YarcParser.ID - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 300
                    self.testlist_comp()

                self.state = 303
                self.match(YarcParser.RBRACK)
                pass
            elif token in [YarcParser.LESS_THAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.match(YarcParser.LESS_THAN)
                self.state = 306
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
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                            | (1 << YarcParser.ELLIPSIS)
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
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                            | (1 << (YarcParser.ID - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 305
                    self.testlist_comp()

                self.state = 308
                self.match(YarcParser.GREATER_THAN)
                pass
            elif token in [YarcParser.LBRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.match(YarcParser.LBRACE)
                self.state = 311
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
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                            | (1 << YarcParser.ELLIPSIS)
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
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                            | (1 << (YarcParser.ID - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 310
                    self.dictorsetmaker()

                self.state = 313
                self.match(YarcParser.RBRACE)
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
                YarcParser.TEXTURE,
                YarcParser.UNDERSCORE,
                YarcParser.ID,
            ]:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.name()
                pass
            elif token in [YarcParser.MINUS, YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 315
                self.signed_number()
                pass
            elif token in [YarcParser.STRING]:
                self.enterOuterAlt(localctx, 7)
                self.state = 316
                self.match(YarcParser.STRING)
                pass
            elif token in [YarcParser.ELLIPSIS]:
                self.enterOuterAlt(localctx, 8)
                self.state = 317
                self.match(YarcParser.ELLIPSIS)
                pass
            elif token in [YarcParser.NONE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 318
                self.match(YarcParser.NONE)
                pass
            elif token in [YarcParser.TRUE]:
                self.enterOuterAlt(localctx, 10)
                self.state = 319
                self.match(YarcParser.TRUE)
                pass
            elif token in [YarcParser.FALSE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 320
                self.match(YarcParser.FALSE)
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

        def getRuleIndex(self):
            return YarcParser.RULE_name

    def name(self):
        localctx = YarcParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_name)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(YarcParser.ID)
                pass
            elif token in [YarcParser.UNDERSCORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
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
                self.state = 325
                self.primitives()
                pass
            elif token in [YarcParser.VISIBLE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.match(YarcParser.VISIBLE)
                pass
            elif token in [YarcParser.SIZE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 327
                self.match(YarcParser.SIZE)
                pass
            elif token in [YarcParser.LOOK_AT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.match(YarcParser.LOOK_AT)
                pass
            elif token in [YarcParser.UP_AXIS]:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
                self.match(YarcParser.UP_AXIS)
                pass
            elif token in [YarcParser.SEMANTICS]:
                self.enterOuterAlt(localctx, 8)
                self.state = 330
                self.match(YarcParser.SEMANTICS)
                pass
            elif token in [YarcParser.TEXTURE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 331
                self.match(YarcParser.TEXTURE)
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
        self.enterRule(localctx, 56, self.RULE_primitives)
        self._la = 0  # Token type
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.SHAPES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(YarcParser.SHAPES)
                pass
            elif token in [YarcParser.CAMERA, YarcParser.STEREO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.STEREO:
                    self.state = 335
                    self.match(YarcParser.STEREO)

                self.state = 338
                self.match(YarcParser.CAMERA)
                pass
            elif token in [YarcParser.LIGHT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.match(YarcParser.LIGHT)
                pass
            elif token in [YarcParser.MATERIAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 340
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
        self.enterRule(localctx, 58, self.RULE_signed_number)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(YarcParser.NUMBER)
                pass
            elif token in [YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(YarcParser.MINUS)
                self.state = 345
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
        self.enterRule(localctx, 60, self.RULE_testlist_comp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.test()
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.state = 349
                self.comp_for()
                pass
            elif token in [
                YarcParser.COMMA,
                YarcParser.RPAREN,
                YarcParser.RBRACK,
                YarcParser.GREATER_THAN,
            ]:
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 37, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 350
                        self.match(YarcParser.COMMA)
                        self.state = 351
                        self.test()
                    self.state = 356
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 37, self._ctx)

                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 357
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

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(YarcParser.ArglistContext, 0)

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
        self.enterRule(localctx, 62, self.RULE_trailer)
        self._la = 0  # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(YarcParser.LPAREN)
                self.state = 364
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
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                            | (1 << YarcParser.ELLIPSIS)
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
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                            | (1 << (YarcParser.ID - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 363
                    self.arglist()

                self.state = 366
                self.match(YarcParser.RPAREN)
                pass
            elif token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(YarcParser.LBRACK)
                self.state = 368
                self.subscriptlist()
                self.state = 369
                self.match(YarcParser.RBRACK)
                pass
            elif token in [YarcParser.DOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.match(YarcParser.DOT)
                self.state = 372
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
        self.enterRule(localctx, 64, self.RULE_arglist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.argument()
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 42, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 376
                    self.match(YarcParser.COMMA)
                    self.state = 377
                    self.argument()
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 42, self._ctx)

            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 383
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
        self.enterRule(localctx, 66, self.RULE_argument)
        self._la = 0  # Token type
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 45, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.test()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.FOR:
                    self.state = 387
                    self.comp_for()

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.test()
                self.state = 391
                self.match(YarcParser.ASSIGN)
                self.state = 392
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
        self.enterRule(localctx, 68, self.RULE_subscriptlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.subscript_()
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 46, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 397
                    self.match(YarcParser.COMMA)
                    self.state = 398
                    self.subscript_()
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 46, self._ctx)

            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 404
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
        self.enterRule(localctx, 70, self.RULE_subscript_)
        self._la = 0  # Token type
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 51, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.test()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                            | (1 << YarcParser.ELLIPSIS)
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
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                            | (1 << (YarcParser.ID - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 408
                    self.test()

                self.state = 411
                self.match(YarcParser.COLON)
                self.state = 413
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
                            | (1 << YarcParser.TEXTURE)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                            | (1 << YarcParser.ELLIPSIS)
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
                            | (1 << (YarcParser.STRING - 71))
                            | (1 << (YarcParser.NUMBER - 71))
                            | (1 << (YarcParser.ID - 71))
                        )
                    )
                    != 0
                ):
                    self.state = 412
                    self.test()

                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COLON:
                    self.state = 415
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
        self.enterRule(localctx, 72, self.RULE_sliceop)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(YarcParser.COLON)
            self.state = 422
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
                        | (1 << YarcParser.TEXTURE)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                        | (1 << YarcParser.ELLIPSIS)
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
                        | (1 << (YarcParser.STRING - 71))
                        | (1 << (YarcParser.NUMBER - 71))
                        | (1 << (YarcParser.ID - 71))
                    )
                )
                != 0
            ):
                self.state = 421
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
        self.enterRule(localctx, 74, self.RULE_exprlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expr()
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 53, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 425
                    self.match(YarcParser.COMMA)
                    self.state = 426
                    self.expr()
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 53, self._ctx)

            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 432
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
        self.enterRule(localctx, 76, self.RULE_testlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.test()
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 55, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 436
                    self.match(YarcParser.COMMA)
                    self.state = 437
                    self.test()
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 55, self._ctx)

            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 443
                self.match(YarcParser.COMMA)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DictorsetmakerContext(ParserRuleContext):
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
            return YarcParser.RULE_dictorsetmaker

    def dictorsetmaker(self):
        localctx = YarcParser.DictorsetmakerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_dictorsetmaker)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 63, self._ctx)
            if la_ == 1:
                self.state = 446
                self.test()
                self.state = 447
                self.match(YarcParser.COLON)
                self.state = 448
                self.test()
                self.state = 463
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 449
                    self.comp_for()
                    pass
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 457
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 57, self._ctx)
                    while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 450
                            self.match(YarcParser.COMMA)
                            self.state = 451
                            self.test()
                            self.state = 452
                            self.match(YarcParser.COLON)
                            self.state = 453
                            self.test()
                        self.state = 459
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 57, self._ctx)

                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.COMMA:
                        self.state = 460
                        self.match(YarcParser.COMMA)

                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 465
                self.test()
                self.state = 477
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 466
                    self.comp_for()
                    pass
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 471
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 60, self._ctx)
                    while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 467
                            self.match(YarcParser.COMMA)
                            self.state = 468
                            self.test()
                        self.state = 473
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 60, self._ctx)

                    self.state = 475
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.COMMA:
                        self.state = 474
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
        self.enterRule(localctx, 80, self.RULE_comp_iter)
        try:
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.comp_for()
                pass
            elif token in [YarcParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
        self.enterRule(localctx, 82, self.RULE_comp_for)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(YarcParser.FOR)
            self.state = 486
            self.exprlist()
            self.state = 487
            self.match(YarcParser.IN)
            self.state = 488
            self.or_test()
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 489
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
        self.enterRule(localctx, 84, self.RULE_comp_if)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(YarcParser.IF)
            self.state = 493
            self.test_nocond()
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 494
                self.comp_iter()

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

        def augassign(self):
            return self.getTypedRuleContext(YarcParser.AugassignContext, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_expr_stmt

    def expr_stmt(self):
        localctx = YarcParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.testlist()
            self.state = 500
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
                self.state = 498
                self.augassign()
                pass
            elif token in [YarcParser.ASSIGN]:
                self.state = 499
                self.match(YarcParser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 502
            self.testlist()
            self.state = 503
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AugassignContext(ParserRuleContext):
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
            return YarcParser.RULE_augassign

    def augassign(self):
        localctx = YarcParser.AugassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_augassign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            _la = self._input.LA(1)
            if not (
                ((_la - 94) & ~0x3F) == 0
                and (
                    (1 << (_la - 94))
                    & (
                        (1 << (YarcParser.ADD_ASSIGN - 94))
                        | (1 << (YarcParser.SUB_ASSIGN - 94))
                        | (1 << (YarcParser.MULT_ASSIGN - 94))
                        | (1 << (YarcParser.DIV_ASSIGN - 94))
                        | (1 << (YarcParser.MOD_ASSIGN - 94))
                        | (1 << (YarcParser.AND_ASSIGN - 94))
                        | (1 << (YarcParser.OR_ASSIGN - 94))
                        | (1 << (YarcParser.XOR_ASSIGN - 94))
                        | (1 << (YarcParser.LSHIFT_ASSIGN - 94))
                        | (1 << (YarcParser.RSHIFT_ASSIGN - 94))
                        | (1 << (YarcParser.POWER_ASSIGN - 94))
                        | (1 << (YarcParser.IDIV_ASSIGN - 94))
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
