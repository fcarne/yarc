# Generated from /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v4/YarcParser.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3v")
        buf.write("\u02e3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write('\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%\4&\t')
        buf.write("&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\3\2\7\2\u00a0\n\2\f\2\16\2\u00a3\13\2\3")
        buf.write("\2\3\2\3\3\3\3\5\3\u00a9\n\3\3\4\3\4\3\4\7\4\u00ae\n\4")
        buf.write("\f\4\16\4\u00b1\13\4\3\4\5\4\u00b4\n\4\3\4\3\4\3\5\3\5")
        buf.write("\5\5\u00ba\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00c3\n")
        buf.write("\6\f\6\16\6\u00c6\13\6\5\6\u00c8\n\6\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u00ce\n\7\3\b\3\b\5\b\u00d2\n\b\3\b\3\b\3\b\5\b\u00d7")
        buf.write("\n\b\7\b\u00d9\n\b\f\b\16\b\u00dc\13\b\3\b\5\b\u00df\n")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\5\13\u00e7\n\13\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\16\7\16\u00f0\n\16\f\16\16\16\u00f3")
        buf.write("\13\16\3\16\5\16\u00f6\n\16\3\17\3\17\3\17\7\17\u00fb")
        buf.write("\n\17\f\17\16\17\u00fe\13\17\3\20\3\20\3\20\7\20\u0103")
        buf.write("\n\20\f\20\16\20\u0106\13\20\3\21\3\21\5\21\u010a\n\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0113\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u011e")
        buf.write("\n\23\3\24\3\24\3\24\3\24\6\24\u0124\n\24\r\24\16\24\u0125")
        buf.write("\3\24\3\24\5\24\u012a\n\24\3\25\3\25\3\25\5\25\u012f\n")
        buf.write("\25\3\25\5\25\u0132\n\25\3\26\3\26\6\26\u0136\n\26\r\26")
        buf.write("\16\26\u0137\3\26\5\26\u013b\n\26\3\27\3\27\3\27\5\27")
        buf.write("\u0140\n\27\3\30\3\30\3\30\3\31\3\31\5\31\u0147\n\31\3")
        buf.write("\32\3\32\3\33\3\33\3\33\7\33\u014e\n\33\f\33\16\33\u0151")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u015b")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0165")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u016f")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0179")
        buf.write('\n\37\3 \3 \3 \5 \u017e\n \3!\3!\3!\5!\u0183\n!\3"\3')
        buf.write("\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3'\3'\3'\3(\3(\3(\6(")
        buf.write("\u0196\n(\r(\16(\u0197\3)\3)\5)\u019c\n)\3*\3*\3*\3*\3")
        buf.write("+\3+\5+\u01a4\n+\3+\3+\3+\5+\u01a9\n+\3+\5+\u01ac\n+\3")
        buf.write(",\3,\3,\5,\u01b1\n,\3-\3-\3-\7-\u01b6\n-\f-\16-\u01b9")
        buf.write("\13-\3-\5-\u01bc\n-\3.\3.\5.\u01c0\n.\3/\3/\3/\3/\5/\u01c6")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\5\60\u01cd\n\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\5\60\u01d6\n\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u01dd\n\60\3\60\3\60\5\60\u01e1\n\60")
        buf.write("\3\61\3\61\3\61\7\61\u01e6\n\61\f\61\16\61\u01e9\13\61")
        buf.write("\3\62\3\62\5\62\u01ed\n\62\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01fd")
        buf.write("\n\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0205\n\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u020f\n\64")
        buf.write("\3\64\3\64\5\64\u0213\n\64\3\65\3\65\3\65\7\65\u0218\n")
        buf.write("\65\f\65\16\65\u021b\13\65\3\66\3\66\3\66\7\66\u0220\n")
        buf.write("\66\f\66\16\66\u0223\13\66\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\38\58\u022f\n8\39\39\3:\3:\3:\7:\u0236\n:\f:\16")
        buf.write(":\u0239\13:\3;\3;\3;\7;\u023e\n;\f;\16;\u0241\13;\3<\3")
        buf.write("<\3<\5<\u0246\n<\3=\3=\3=\3=\7=\u024c\n=\f=\16=\u024f")
        buf.write("\13=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u025d\n>\3")
        buf.write("?\3?\3?\3@\3@\3@\7@\u0265\n@\f@\16@\u0268\13@\3A\3A\3")
        buf.write("A\7A\u026d\nA\fA\16A\u0270\13A\3B\3B\3B\7B\u0275\nB\f")
        buf.write("B\16B\u0278\13B\3C\3C\3C\7C\u027d\nC\fC\16C\u0280\13C")
        buf.write("\3D\3D\3D\7D\u0285\nD\fD\16D\u0288\13D\3E\3E\3E\7E\u028d")
        buf.write("\nE\fE\16E\u0290\13E\3F\3F\3F\3G\3G\3G\6G\u0298\nG\rG")
        buf.write("\16G\u0299\3G\3G\3G\3G\5G\u02a0\nG\3H\3H\3I\3I\3I\7I\u02a7")
        buf.write("\nI\fI\16I\u02aa\13I\3I\5I\u02ad\nI\3J\3J\5J\u02b1\nJ")
        buf.write("\3J\3J\5J\u02b5\nJ\3J\5J\u02b8\nJ\5J\u02ba\nJ\3K\3K\5")
        buf.write("K\u02be\nK\3L\3L\5L\u02c2\nL\3L\3L\3L\5L\u02c7\nL\7L\u02c9")
        buf.write("\nL\fL\16L\u02cc\13L\3L\5L\u02cf\nL\3M\3M\3M\7M\u02d4")
        buf.write("\nM\fM\16M\u02d7\13M\3M\5M\u02da\nM\3N\3N\3O\6O\u02df")
        buf.write("\nO\rO\16O\u02e0\3O\2\2P\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write('\32\34\36 "$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b')
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\2\b\3")
        buf.write("\2\\h\3\2EF\3\2GH\4\2ILNN\4\2DDGH\4\299kk\2\u0309\2\u00a1")
        buf.write("\3\2\2\2\4\u00a8\3\2\2\2\6\u00aa\3\2\2\2\b\u00b9\3\2\2")
        buf.write("\2\n\u00bb\3\2\2\2\f\u00c9\3\2\2\2\16\u00d1\3\2\2\2\20")
        buf.write("\u00e0\3\2\2\2\22\u00e2\3\2\2\2\24\u00e4\3\2\2\2\26\u00e8")
        buf.write("\3\2\2\2\30\u00ea\3\2\2\2\32\u00ec\3\2\2\2\34\u00f7\3")
        buf.write('\2\2\2\36\u00ff\3\2\2\2 \u0109\3\2\2\2"\u010b\3\2\2\2')
        buf.write("$\u0114\3\2\2\2&\u0129\3\2\2\2(\u0131\3\2\2\2*\u0133\3")
        buf.write("\2\2\2,\u013f\3\2\2\2.\u0141\3\2\2\2\60\u0146\3\2\2\2")
        buf.write("\62\u0148\3\2\2\2\64\u014a\3\2\2\2\66\u015a\3\2\2\28\u0164")
        buf.write("\3\2\2\2:\u016e\3\2\2\2<\u0178\3\2\2\2>\u017d\3\2\2\2")
        buf.write("@\u0182\3\2\2\2B\u0184\3\2\2\2D\u0186\3\2\2\2F\u0188\3")
        buf.write("\2\2\2H\u018a\3\2\2\2J\u018d\3\2\2\2L\u018f\3\2\2\2N\u0192")
        buf.write("\3\2\2\2P\u019b\3\2\2\2R\u019d\3\2\2\2T\u01ab\3\2\2\2")
        buf.write("V\u01ad\3\2\2\2X\u01b2\3\2\2\2Z\u01bf\3\2\2\2\\\u01c5")
        buf.write("\3\2\2\2^\u01e0\3\2\2\2`\u01e2\3\2\2\2b\u01ec\3\2\2\2")
        buf.write("d\u01f1\3\2\2\2f\u0212\3\2\2\2h\u0214\3\2\2\2j\u021c\3")
        buf.write("\2\2\2l\u0224\3\2\2\2n\u0228\3\2\2\2p\u0230\3\2\2\2r\u0232")
        buf.write("\3\2\2\2t\u023a\3\2\2\2v\u0245\3\2\2\2x\u0247\3\2\2\2")
        buf.write("z\u025c\3\2\2\2|\u025e\3\2\2\2~\u0261\3\2\2\2\u0080\u0269")
        buf.write("\3\2\2\2\u0082\u0271\3\2\2\2\u0084\u0279\3\2\2\2\u0086")
        buf.write("\u0281\3\2\2\2\u0088\u0289\3\2\2\2\u008a\u0291\3\2\2\2")
        buf.write("\u008c\u029f\3\2\2\2\u008e\u02a1\3\2\2\2\u0090\u02a3\3")
        buf.write("\2\2\2\u0092\u02b9\3\2\2\2\u0094\u02bb\3\2\2\2\u0096\u02c1")
        buf.write("\3\2\2\2\u0098\u02d0\3\2\2\2\u009a\u02db\3\2\2\2\u009c")
        buf.write("\u02de\3\2\2\2\u009e\u00a0\7t\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5")
        buf.write("\7\2\2\3\u00a5\3\3\2\2\2\u00a6\u00a9\5\6\4\2\u00a7\u00a9")
        buf.write("\5 \21\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\5\3\2\2\2\u00aa\u00af\5\b\5\2\u00ab\u00ac\7?\2\2\u00ac")
        buf.write("\u00ae\5\b\5\2\u00ad\u00ab\3\2\2\2\u00ae\u00b1\3\2\2\2")
        buf.write("\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b3\3")
        buf.write("\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b4\7?\2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b6\7t\2\2\u00b6\7\3\2\2\2\u00b7\u00ba\5\n\6\2\u00b8")
        buf.write("\u00ba\5\22\n\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2")
        buf.write("\2\u00ba\t\3\2\2\2\u00bb\u00c7\5\16\b\2\u00bc\u00c8\5")
        buf.write("\f\7\2\u00bd\u00be\5\20\t\2\u00be\u00bf\5\u0098M\2\u00bf")
        buf.write("\u00c8\3\2\2\2\u00c0\u00c1\7@\2\2\u00c1\u00c3\5\16\b\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c7\u00bc\3\2\2\2\u00c7\u00bd\3\2\2\2\u00c7")
        buf.write("\u00c4\3\2\2\2\u00c8\13\3\2\2\2\u00c9\u00ca\7>\2\2\u00ca")
        buf.write("\u00cd\5n8\2\u00cb\u00cc\7@\2\2\u00cc\u00ce\5n8\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\r\3\2\2\2\u00cf")
        buf.write("\u00d2\5n8\2\u00d0\u00d2\5|?\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00da\3\2\2\2\u00d3\u00d6\7=\2\2")
        buf.write("\u00d4\u00d7\5n8\2\u00d5\u00d7\5|?\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d6\u00d5\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d3")
        buf.write("\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2")
        buf.write("\u00dd\u00df\7=\2\2\u00de\u00dd\3\2\2\2\u00de\u00df\3")
        buf.write("\2\2\2\u00df\17\3\2\2\2\u00e0\u00e1\t\2\2\2\u00e1\21\3")
        buf.write("\2\2\2\u00e2\u00e3\7<\2\2\u00e3\23\3\2\2\2\u00e4\u00e6")
        buf.write("\7\67\2\2\u00e5\u00e7\5\u0098M\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\25\3\2\2\2\u00e8\u00e9\5\u008eH\2")
        buf.write("\u00e9\27\3\2\2\2\u00ea\u00eb\5\36\20\2\u00eb\31\3\2\2")
        buf.write("\2\u00ec\u00f1\5\26\f\2\u00ed\u00ee\7=\2\2\u00ee\u00f0")
        buf.write("\5\26\f\2\u00ef\u00ed\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f5\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f4\u00f6\7=\2\2\u00f5\u00f4\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\33\3\2\2\2\u00f7\u00fc")
        buf.write("\5\30\r\2\u00f8\u00f9\7=\2\2\u00f9\u00fb\5\30\r\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\35\3\2\2\2\u00fe\u00fc\3\2")
        buf.write("\2\2\u00ff\u0104\5\u008eH\2\u0100\u0101\7:\2\2\u0101\u0103")
        buf.write("\5\u008eH\2\u0102\u0100\3\2\2\2\u0103\u0106\3\2\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\37\3\2\2\2\u0106")
        buf.write('\u0104\3\2\2\2\u0107\u010a\5"\22\2\u0108\u010a\5$\23')
        buf.write("\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a!\3\2")
        buf.write("\2\2\u010b\u010c\7\61\2\2\u010c\u010d\5n8\2\u010d\u010e")
        buf.write("\7>\2\2\u010e\u0112\5&\24\2\u010f\u0110\7.\2\2\u0110\u0111")
        buf.write("\7>\2\2\u0111\u0113\5&\24\2\u0112\u010f\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113#\3\2\2\2\u0114\u0115\7\60\2\2\u0115")
        buf.write("\u0116\5\u0096L\2\u0116\u0117\7\62\2\2\u0117\u0118\5\u0098")
        buf.write("M\2\u0118\u0119\7>\2\2\u0119\u011d\5&\24\2\u011a\u011b")
        buf.write("\7.\2\2\u011b\u011c\7>\2\2\u011c\u011e\5&\24\2\u011d\u011a")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e%\3\2\2\2\u011f\u012a")
        buf.write("\5\6\4\2\u0120\u0121\7t\2\2\u0121\u0123\7\3\2\2\u0122")
        buf.write("\u0124\5\4\3\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0128\7\4\2\2\u0128\u012a\3\2\2\2\u0129\u011f")
        buf.write("\3\2\2\2\u0129\u0120\3\2\2\2\u012a'\3\2\2\2\u012b\u012c")
        buf.write("\5,\27\2\u012c\u012e\7=\2\2\u012d\u012f\5*\26\2\u012e")
        buf.write("\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0132\3\2\2\2")
        buf.write("\u0130\u0132\5n8\2\u0131\u012b\3\2\2\2\u0131\u0130\3\2")
        buf.write("\2\2\u0132)\3\2\2\2\u0133\u0135\7=\2\2\u0134\u0136\5,")
        buf.write("\27\2\u0135\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u013b\7=\2\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b+\3\2\2\2\u013c\u013d\7J\2\2\u013d\u0140\5~@\2\u013e")
        buf.write("\u0140\5n8\2\u013f\u013c\3\2\2\2\u013f\u013e\3\2\2\2\u0140")
        buf.write("-\3\2\2\2\u0141\u0142\7\61\2\2\u0142\u0143\5n8\2\u0143")
        buf.write("/\3\2\2\2\u0144\u0147\5V,\2\u0145\u0147\5\62\32\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147\61\3\2\2\2\u0148")
        buf.write("\u0149\5\64\33\2\u0149\63\3\2\2\2\u014a\u014f\5\66\34")
        buf.write("\2\u014b\u014c\7A\2\2\u014c\u014e\5\66\34\2\u014d\u014b")
        buf.write("\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\65\3\2\2\2\u0151\u014f\3\2\2\2\u0152")
        buf.write("\u015b\58\35\2\u0153\u015b\5F$\2\u0154\u015b\5J&\2\u0155")
        buf.write("\u015b\5L'\2\u0156\u015b\5R*\2\u0157\u015b\5T+\2\u0158")
        buf.write("\u015b\5^\60\2\u0159\u015b\5f\64\2\u015a\u0152\3\2\2\2")
        buf.write("\u015a\u0153\3\2\2\2\u015a\u0154\3\2\2\2\u015a\u0155\3")
        buf.write("\2\2\2\u015a\u0156\3\2\2\2\u015a\u0157\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015a\u0159\3\2\2\2\u015b\67\3\2\2\2\u015c\u015d")
        buf.write("\5> \2\u015d\u015e\6\35\2\3\u015e\u0165\3\2\2\2\u015f")
        buf.write("\u0165\5<\37\2\u0160\u0165\5\u009cO\2\u0161\u0165\7\64")
        buf.write("\2\2\u0162\u0165\78\2\2\u0163\u0165\7/\2\2\u0164\u015c")
        buf.write("\3\2\2\2\u0164\u015f\3\2\2\2\u0164\u0160\3\2\2\2\u0164")
        buf.write("\u0161\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2")
        buf.write("\u01659\3\2\2\2\u0166\u0167\5> \2\u0167\u0168\6\36\3\3")
        buf.write("\u0168\u016f\3\2\2\2\u0169\u016f\5<\37\2\u016a\u016f\5")
        buf.write("\u009cO\2\u016b\u016f\7\64\2\2\u016c\u016f\78\2\2\u016d")
        buf.write("\u016f\7/\2\2\u016e\u0166\3\2\2\2\u016e\u0169\3\2\2\2")
        buf.write("\u016e\u016a\3\2\2\2\u016e\u016b\3\2\2\2\u016e\u016c\3")
        buf.write("\2\2\2\u016e\u016d\3\2\2\2\u016f;\3\2\2\2\u0170\u0171")
        buf.write("\5@!\2\u0171\u0172\7G\2\2\u0172\u0173\5D#\2\u0173\u0179")
        buf.write("\3\2\2\2\u0174\u0175\5@!\2\u0175\u0176\7H\2\2\u0176\u0177")
        buf.write("\5D#\2\u0177\u0179\3\2\2\2\u0178\u0170\3\2\2\2\u0178\u0174")
        buf.write("\3\2\2\2\u0179=\3\2\2\2\u017a\u017e\7j\2\2\u017b\u017c")
        buf.write("\7H\2\2\u017c\u017e\7j\2\2\u017d\u017a\3\2\2\2\u017d\u017b")
        buf.write('\3\2\2\2\u017e?\3\2\2\2\u017f\u0183\5B"\2\u0180\u0181')
        buf.write('\7H\2\2\u0181\u0183\5B"\2\u0182\u017f\3\2\2\2\u0182\u0180')
        buf.write("\3\2\2\2\u0183A\3\2\2\2\u0184\u0185\7j\2\2\u0185C\3\2")
        buf.write("\2\2\u0186\u0187\7j\2\2\u0187E\3\2\2\2\u0188\u0189\5H")
        buf.write("%\2\u0189G\3\2\2\2\u018a\u018b\5\u008eH\2\u018b\u018c")
        buf.write("\6%\4\3\u018cI\3\2\2\2\u018d\u018e\79\2\2\u018eK\3\2\2")
        buf.write("\2\u018f\u0190\5N(\2\u0190\u0191\6'\5\3\u0191M\3\2\2")
        buf.write("\2\u0192\u0195\5\u008eH\2\u0193\u0194\7:\2\2\u0194\u0196")
        buf.write("\5\u008eH\2\u0195\u0193\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198O\3\2\2\2\u0199")
        buf.write("\u019c\5N(\2\u019a\u019c\5\u008eH\2\u019b\u0199\3\2\2")
        buf.write("\2\u019b\u019a\3\2\2\2\u019cQ\3\2\2\2\u019d\u019e\7P\2")
        buf.write("\2\u019e\u019f\5\62\32\2\u019f\u01a0\7Q\2\2\u01a0S\3\2")
        buf.write("\2\2\u01a1\u01a3\7R\2\2\u01a2\u01a4\5X-\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01ac\7S\2\2\u01a6\u01a8\7P\2\2\u01a7\u01a9\5V,\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01aa\u01ac\7Q\2\2\u01ab\u01a1\3\2\2\2\u01ab\u01a6\3")
        buf.write("\2\2\2\u01acU\3\2\2\2\u01ad\u01ae\5Z.\2\u01ae\u01b0\7")
        buf.write("=\2\2\u01af\u01b1\5X-\2\u01b0\u01af\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1W\3\2\2\2\u01b2\u01b7\5Z.\2\u01b3\u01b4")
        buf.write("\7=\2\2\u01b4\u01b6\5Z.\2\u01b5\u01b3\3\2\2\2\u01b6\u01b9")
        buf.write("\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bc\7=\2\2")
        buf.write("\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bcY\3\2\2")
        buf.write("\2\u01bd\u01c0\5\\/\2\u01be\u01c0\5\62\32\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0[\3\2\2\2\u01c1\u01c2")
        buf.write("\7J\2\2\u01c2\u01c6\5H%\2\u01c3\u01c4\7J\2\2\u01c4\u01c6")
        buf.write("\5J&\2\u01c5\u01c1\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6]")
        buf.write("\3\2\2\2\u01c7\u01c8\7T\2\2\u01c8\u01e1\7U\2\2\u01c9\u01ca")
        buf.write("\7T\2\2\u01ca\u01cc\5d\63\2\u01cb\u01cd\7=\2\2\u01cc\u01cb")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01cf\7U\2\2\u01cf\u01e1\3\2\2\2\u01d0\u01d1\7T\2\2\u01d1")
        buf.write("\u01d2\5`\61\2\u01d2\u01d3\7=\2\2\u01d3\u01d5\5d\63\2")
        buf.write("\u01d4\u01d6\7=\2\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6\3")
        buf.write("\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\7U\2\2\u01d8\u01e1")
        buf.write("\3\2\2\2\u01d9\u01da\7T\2\2\u01da\u01dc\5`\61\2\u01db")
        buf.write("\u01dd\7=\2\2\u01dc\u01db\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01df\7U\2\2\u01df\u01e1\3")
        buf.write("\2\2\2\u01e0\u01c7\3\2\2\2\u01e0\u01c9\3\2\2\2\u01e0\u01d0")
        buf.write("\3\2\2\2\u01e0\u01d9\3\2\2\2\u01e1_\3\2\2\2\u01e2\u01e7")
        buf.write("\5b\62\2\u01e3\u01e4\7=\2\2\u01e4\u01e6\5b\62\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8a\3\2\2\2\u01e9\u01e7\3\2\2")
        buf.write("\2\u01ea\u01ed\5:\36\2\u01eb\u01ed\5N(\2\u01ec\u01ea\3")
        buf.write("\2\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef")
        buf.write("\7>\2\2\u01ef\u01f0\5\62\32\2\u01f0c\3\2\2\2\u01f1\u01f2")
        buf.write("\7M\2\2\u01f2\u01f3\5H%\2\u01f3e\3\2\2\2\u01f4\u01f5\5")
        buf.write("P)\2\u01f5\u01f6\7P\2\2\u01f6\u01f7\7Q\2\2\u01f7\u0213")
        buf.write("\3\2\2\2\u01f8\u01f9\5P)\2\u01f9\u01fa\7P\2\2\u01fa\u01fc")
        buf.write("\5h\65\2\u01fb\u01fd\7=\2\2\u01fc\u01fb\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\7Q\2\2")
        buf.write("\u01ff\u0213\3\2\2\2\u0200\u0201\5P)\2\u0201\u0202\7P")
        buf.write("\2\2\u0202\u0204\5j\66\2\u0203\u0205\7=\2\2\u0204\u0203")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write("\u0207\7Q\2\2\u0207\u0213\3\2\2\2\u0208\u0209\5P)\2\u0209")
        buf.write("\u020a\7P\2\2\u020a\u020b\5h\65\2\u020b\u020c\7=\2\2\u020c")
        buf.write("\u020e\5j\66\2\u020d\u020f\7=\2\2\u020e\u020d\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211\7")
        buf.write("Q\2\2\u0211\u0213\3\2\2\2\u0212\u01f4\3\2\2\2\u0212\u01f8")
        buf.write("\3\2\2\2\u0212\u0200\3\2\2\2\u0212\u0208\3\2\2\2\u0213")
        buf.write("g\3\2\2\2\u0214\u0219\5\62\32\2\u0215\u0216\7=\2\2\u0216")
        buf.write("\u0218\5\62\32\2\u0217\u0215\3\2\2\2\u0218\u021b\3\2\2")
        buf.write("\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021ai\3\2")
        buf.write("\2\2\u021b\u0219\3\2\2\2\u021c\u0221\5l\67\2\u021d\u021e")
        buf.write("\7=\2\2\u021e\u0220\5l\67\2\u021f\u021d\3\2\2\2\u0220")
        buf.write("\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2")
        buf.write("\u0222k\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0225\5\u008e")
        buf.write("H\2\u0225\u0226\7@\2\2\u0226\u0227\5\62\32\2\u0227m\3")
        buf.write("\2\2\2\u0228\u022e\5r:\2\u0229\u022a\7\61\2\2\u022a\u022b")
        buf.write("\5r:\2\u022b\u022c\7.\2\2\u022c\u022d\5n8\2\u022d\u022f")
        buf.write("\3\2\2\2\u022e\u0229\3\2\2\2\u022e\u022f\3\2\2\2\u022f")
        buf.write("o\3\2\2\2\u0230\u0231\5r:\2\u0231q\3\2\2\2\u0232\u0237")
        buf.write("\5t;\2\u0233\u0234\7\66\2\2\u0234\u0236\5t;\2\u0235\u0233")
        buf.write("\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238s\3\2\2\2\u0239\u0237\3\2\2\2\u023a")
        buf.write("\u023f\5v<\2\u023b\u023c\7,\2\2\u023c\u023e\5v<\2\u023d")
        buf.write("\u023b\3\2\2\2\u023e\u0241\3\2\2\2\u023f\u023d\3\2\2\2")
        buf.write("\u023f\u0240\3\2\2\2\u0240u\3\2\2\2\u0241\u023f\3\2\2")
        buf.write("\2\u0242\u0243\7\65\2\2\u0243\u0246\5v<\2\u0244\u0246")
        buf.write("\5x=\2\u0245\u0242\3\2\2\2\u0245\u0244\3\2\2\2\u0246w")
        buf.write("\3\2\2\2\u0247\u024d\5~@\2\u0248\u0249\5z>\2\u0249\u024a")
        buf.write("\5~@\2\u024a\u024c\3\2\2\2\u024b\u0248\3\2\2\2\u024c\u024f")
        buf.write("\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("y\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u025d\7V\2\2\u0251")
        buf.write("\u025d\7W\2\2\u0252\u025d\7X\2\2\u0253\u025d\7Y\2\2\u0254")
        buf.write("\u025d\7Z\2\2\u0255\u025d\7[\2\2\u0256\u025d\7\62\2\2")
        buf.write("\u0257\u0258\7\65\2\2\u0258\u025d\7\62\2\2\u0259\u025d")
        buf.write("\7\63\2\2\u025a\u025b\7\63\2\2\u025b\u025d\7\65\2\2\u025c")
        buf.write("\u0250\3\2\2\2\u025c\u0251\3\2\2\2\u025c\u0252\3\2\2\2")
        buf.write("\u025c\u0253\3\2\2\2\u025c\u0254\3\2\2\2\u025c\u0255\3")
        buf.write("\2\2\2\u025c\u0256\3\2\2\2\u025c\u0257\3\2\2\2\u025c\u0259")
        buf.write("\3\2\2\2\u025c\u025a\3\2\2\2\u025d{\3\2\2\2\u025e\u025f")
        buf.write("\7J\2\2\u025f\u0260\5~@\2\u0260}\3\2\2\2\u0261\u0266\5")
        buf.write("\u0080A\2\u0262\u0263\7A\2\2\u0263\u0265\5\u0080A\2\u0264")
        buf.write("\u0262\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0264\3\2\2\2")
        buf.write("\u0266\u0267\3\2\2\2\u0267\177\3\2\2\2\u0268\u0266\3\2")
        buf.write("\2\2\u0269\u026e\5\u0082B\2\u026a\u026b\7B\2\2\u026b\u026d")
        buf.write("\5\u0082B\2\u026c\u026a\3\2\2\2\u026d\u0270\3\2\2\2\u026e")
        buf.write("\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0081\3\2\2\2")
        buf.write("\u0270\u026e\3\2\2\2\u0271\u0276\5\u0084C\2\u0272\u0273")
        buf.write("\7C\2\2\u0273\u0275\5\u0084C\2\u0274\u0272\3\2\2\2\u0275")
        buf.write("\u0278\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0083\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u027e\5")
        buf.write("\u0086D\2\u027a\u027b\t\3\2\2\u027b\u027d\5\u0086D\2\u027c")
        buf.write("\u027a\3\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c\3\2\2\2")
        buf.write("\u027e\u027f\3\2\2\2\u027f\u0085\3\2\2\2\u0280\u027e\3")
        buf.write("\2\2\2\u0281\u0286\5\u0088E\2\u0282\u0283\t\4\2\2\u0283")
        buf.write("\u0285\5\u0088E\2\u0284\u0282\3\2\2\2\u0285\u0288\3\2")
        buf.write("\2\2\u0286\u0284\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0087")
        buf.write("\3\2\2\2\u0288\u0286\3\2\2\2\u0289\u028e\5\u008aF\2\u028a")
        buf.write("\u028b\t\5\2\2\u028b\u028d\5\u008aF\2\u028c\u028a\3\2")
        buf.write("\2\2\u028d\u0290\3\2\2\2\u028e\u028c\3\2\2\2\u028e\u028f")
        buf.write("\3\2\2\2\u028f\u0089\3\2\2\2\u0290\u028e\3\2\2\2\u0291")
        buf.write("\u0292\t\6\2\2\u0292\u0293\5\u008aF\2\u0293\u008b\3\2")
        buf.write("\2\2\u0294\u02a0\5\u008eH\2\u0295\u02a0\7j\2\2\u0296\u0298")
        buf.write("\7i\2\2\u0297\u0296\3\2\2\2\u0298\u0299\3\2\2\2\u0299")
        buf.write("\u0297\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u02a0\3\2\2\2")
        buf.write("\u029b\u02a0\7<\2\2\u029c\u02a0\7\64\2\2\u029d\u02a0\7")
        buf.write("8\2\2\u029e\u02a0\7/\2\2\u029f\u0294\3\2\2\2\u029f\u0295")
        buf.write("\3\2\2\2\u029f\u0297\3\2\2\2\u029f\u029b\3\2\2\2\u029f")
        buf.write("\u029c\3\2\2\2\u029f\u029d\3\2\2\2\u029f\u029e\3\2\2\2")
        buf.write("\u02a0\u008d\3\2\2\2\u02a1\u02a2\t\7\2\2\u02a2\u008f\3")
        buf.write("\2\2\2\u02a3\u02a8\5\u0092J\2\u02a4\u02a5\7=\2\2\u02a5")
        buf.write("\u02a7\5\u0092J\2\u02a6\u02a4\3\2\2\2\u02a7\u02aa\3\2")
        buf.write("\2\2\u02a8\u02a6\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ac")
        buf.write("\3\2\2\2\u02aa\u02a8\3\2\2\2\u02ab\u02ad\7=\2\2\u02ac")
        buf.write("\u02ab\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u0091\3\2\2\2")
        buf.write("\u02ae\u02ba\5n8\2\u02af\u02b1\5n8\2\u02b0\u02af\3\2\2")
        buf.write("\2\u02b0\u02b1\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b4")
        buf.write("\7>\2\2\u02b3\u02b5\5n8\2\u02b4\u02b3\3\2\2\2\u02b4\u02b5")
        buf.write("\3\2\2\2\u02b5\u02b7\3\2\2\2\u02b6\u02b8\5\u0094K\2\u02b7")
        buf.write("\u02b6\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02ba\3\2\2\2")
        buf.write("\u02b9\u02ae\3\2\2\2\u02b9\u02b0\3\2\2\2\u02ba\u0093\3")
        buf.write("\2\2\2\u02bb\u02bd\7>\2\2\u02bc\u02be\5n8\2\u02bd\u02bc")
        buf.write("\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u0095\3\2\2\2\u02bf")
        buf.write("\u02c2\5~@\2\u02c0\u02c2\5|?\2\u02c1\u02bf\3\2\2\2\u02c1")
        buf.write("\u02c0\3\2\2\2\u02c2\u02ca\3\2\2\2\u02c3\u02c6\7=\2\2")
        buf.write("\u02c4\u02c7\5~@\2\u02c5\u02c7\5|?\2\u02c6\u02c4\3\2\2")
        buf.write("\2\u02c6\u02c5\3\2\2\2\u02c7\u02c9\3\2\2\2\u02c8\u02c3")
        buf.write("\3\2\2\2\u02c9\u02cc\3\2\2\2\u02ca\u02c8\3\2\2\2\u02ca")
        buf.write("\u02cb\3\2\2\2\u02cb\u02ce\3\2\2\2\u02cc\u02ca\3\2\2\2")
        buf.write("\u02cd\u02cf\7=\2\2\u02ce\u02cd\3\2\2\2\u02ce\u02cf\3")
        buf.write("\2\2\2\u02cf\u0097\3\2\2\2\u02d0\u02d5\5n8\2\u02d1\u02d2")
        buf.write("\7=\2\2\u02d2\u02d4\5n8\2\u02d3\u02d1\3\2\2\2\u02d4\u02d7")
        buf.write("\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6")
        buf.write("\u02d9\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02da\7=\2\2")
        buf.write("\u02d9\u02d8\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u0099\3")
        buf.write("\2\2\2\u02db\u02dc\5\u008eH\2\u02dc\u009b\3\2\2\2\u02dd")
        buf.write("\u02df\7i\2\2\u02de\u02dd\3\2\2\2\u02df\u02e0\3\2\2\2")
        buf.write("\u02e0\u02de\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1\u009d\3")
        buf.write("\2\2\2W\u00a1\u00a8\u00af\u00b3\u00b9\u00c4\u00c7\u00cd")
        buf.write("\u00d1\u00d6\u00da\u00de\u00e6\u00f1\u00f5\u00fc\u0104")
        buf.write("\u0109\u0112\u011d\u0125\u0129\u012e\u0131\u0137\u013a")
        buf.write("\u013f\u0146\u014f\u015a\u0164\u016e\u0178\u017d\u0182")
        buf.write("\u0197\u019b\u01a3\u01a8\u01ab\u01b0\u01b7\u01bb\u01bf")
        buf.write("\u01c5\u01cc\u01d5\u01dc\u01e0\u01e7\u01ec\u01fc\u0204")
        buf.write("\u020e\u0212\u0219\u0221\u022e\u0237\u023f\u0245\u024d")
        buf.write("\u025c\u0266\u026e\u0276\u027e\u0286\u028e\u0299\u029f")
        buf.write("\u02a8\u02ac\u02b0\u02b4\u02b7\u02b9\u02bd\u02c1\u02c6")
        buf.write("\u02ca\u02ce\u02d5\u02d9\u02e0")
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
        "'Uniform'",
        "'Normal'",
        "'Choice'",
        "'Sequence'",
        "'LogUniform'",
        "'create'",
        "'instantiate'",
        "'group'",
        "'open'",
        "'get'",
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
        "'scatter'",
        "<INVALID>",
        "'around'",
        "'texture'",
        "'to'",
        "'on'",
        "'up'",
        "'every'",
        "<INVALID>",
        "<INVALID>",
        "'camera'",
        "'light'",
        "'stereo'",
        "'material'",
        "'timeline'",
        "<INVALID>",
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
        "'@'",
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
        "'@='",
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
        "UNIFORM",
        "NORMAL",
        "CHOICE",
        "SEQUENCE",
        "LOG_UNIFORM",
        "CREATE",
        "INSTANTIATE",
        "GROUP",
        "OPEN",
        "GET",
        "AXIS",
        "EDIT",
        "SET",
        "TRANSLATE",
        "ROTATE",
        "SCALE",
        "SEMANTICS",
        "VISIBLE",
        "SIZE",
        "LOOK_AT",
        "SCATTER",
        "SCATTER_TYPE",
        "AROUND",
        "TEXTURE",
        "TO",
        "ON",
        "UP",
        "EVERY",
        "FRAMES",
        "TIME",
        "CAMERA",
        "LIGHT",
        "STEREO",
        "MATERIAL",
        "TIMELINE",
        "SNIPPET",
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
        "AT",
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
        "AT_ASSIGN",
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
    RULE_stmt = 1
    RULE_simple_stmts = 2
    RULE_simple_stmt = 3
    RULE_expr_stmt = 4
    RULE_annassign = 5
    RULE_testlist_star_expr = 6
    RULE_augassign = 7
    RULE_pass_stmt = 8
    RULE_return_stmt = 9
    RULE_import_as_name = 10
    RULE_dotted_as_name = 11
    RULE_import_as_names = 12
    RULE_dotted_as_names = 13
    RULE_dotted_name = 14
    RULE_compound_stmt = 15
    RULE_if_stmt = 16
    RULE_for_stmt = 17
    RULE_block = 18
    RULE_subject_expr = 19
    RULE_star_named_expressions = 20
    RULE_star_named_expression = 21
    RULE_guard = 22
    RULE_patterns = 23
    RULE_pattern = 24
    RULE_or_pattern = 25
    RULE_closed_pattern = 26
    RULE_literal_pattern = 27
    RULE_literal_expr = 28
    RULE_complex_number = 29
    RULE_signed_number = 30
    RULE_signed_real_number = 31
    RULE_real_number = 32
    RULE_imaginary_number = 33
    RULE_capture_pattern = 34
    RULE_pattern_capture_target = 35
    RULE_wildcard_pattern = 36
    RULE_value_pattern = 37
    RULE_attr = 38
    RULE_name_or_attr = 39
    RULE_group_pattern = 40
    RULE_sequence_pattern = 41
    RULE_open_sequence_pattern = 42
    RULE_maybe_sequence_pattern = 43
    RULE_maybe_star_pattern = 44
    RULE_star_pattern = 45
    RULE_mapping_pattern = 46
    RULE_items_pattern = 47
    RULE_key_value_pattern = 48
    RULE_double_star_pattern = 49
    RULE_class_pattern = 50
    RULE_positional_patterns = 51
    RULE_keyword_patterns = 52
    RULE_keyword_pattern = 53
    RULE_test = 54
    RULE_test_nocond = 55
    RULE_or_test = 56
    RULE_and_test = 57
    RULE_not_test = 58
    RULE_comparison = 59
    RULE_comp_op = 60
    RULE_star_expr = 61
    RULE_expr = 62
    RULE_xor_expr = 63
    RULE_and_expr = 64
    RULE_shift_expr = 65
    RULE_arith_expr = 66
    RULE_term = 67
    RULE_factor = 68
    RULE_atom = 69
    RULE_name = 70
    RULE_subscriptlist = 71
    RULE_subscript_ = 72
    RULE_sliceop = 73
    RULE_exprlist = 74
    RULE_testlist = 75
    RULE_encoding_decl = 76
    RULE_strings = 77

    ruleNames = [
        "file_input",
        "stmt",
        "simple_stmts",
        "simple_stmt",
        "expr_stmt",
        "annassign",
        "testlist_star_expr",
        "augassign",
        "pass_stmt",
        "return_stmt",
        "import_as_name",
        "dotted_as_name",
        "import_as_names",
        "dotted_as_names",
        "dotted_name",
        "compound_stmt",
        "if_stmt",
        "for_stmt",
        "block",
        "subject_expr",
        "star_named_expressions",
        "star_named_expression",
        "guard",
        "patterns",
        "pattern",
        "or_pattern",
        "closed_pattern",
        "literal_pattern",
        "literal_expr",
        "complex_number",
        "signed_number",
        "signed_real_number",
        "real_number",
        "imaginary_number",
        "capture_pattern",
        "pattern_capture_target",
        "wildcard_pattern",
        "value_pattern",
        "attr",
        "name_or_attr",
        "group_pattern",
        "sequence_pattern",
        "open_sequence_pattern",
        "maybe_sequence_pattern",
        "maybe_star_pattern",
        "star_pattern",
        "mapping_pattern",
        "items_pattern",
        "key_value_pattern",
        "double_star_pattern",
        "class_pattern",
        "positional_patterns",
        "keyword_patterns",
        "keyword_pattern",
        "test",
        "test_nocond",
        "or_test",
        "and_test",
        "not_test",
        "comparison",
        "comp_op",
        "star_expr",
        "expr",
        "xor_expr",
        "and_expr",
        "shift_expr",
        "arith_expr",
        "term",
        "factor",
        "atom",
        "name",
        "subscriptlist",
        "subscript_",
        "sliceop",
        "exprlist",
        "testlist",
        "encoding_decl",
        "strings",
    ]

    EOF = Token.EOF
    INDENT = 1
    DEDENT = 2
    SCENARIO = 3
    SETTINGS = 4
    WRITER = 5
    UNIFORM = 6
    NORMAL = 7
    CHOICE = 8
    SEQUENCE = 9
    LOG_UNIFORM = 10
    CREATE = 11
    INSTANTIATE = 12
    GROUP = 13
    OPEN = 14
    GET = 15
    AXIS = 16
    EDIT = 17
    SET = 18
    TRANSLATE = 19
    ROTATE = 20
    SCALE = 21
    SEMANTICS = 22
    VISIBLE = 23
    SIZE = 24
    LOOK_AT = 25
    SCATTER = 26
    SCATTER_TYPE = 27
    AROUND = 28
    TEXTURE = 29
    TO = 30
    ON = 31
    UP = 32
    EVERY = 33
    FRAMES = 34
    TIME = 35
    CAMERA = 36
    LIGHT = 37
    STEREO = 38
    MATERIAL = 39
    TIMELINE = 40
    SNIPPET = 41
    AND = 42
    DEF = 43
    ELSE = 44
    FALSE = 45
    FOR = 46
    IF = 47
    IN = 48
    IS = 49
    NONE = 50
    NOT = 51
    OR = 52
    RETURN = 53
    TRUE = 54
    UNDERSCORE = 55
    DOT = 56
    RANGE = 57
    ELLIPSIS = 58
    COMMA = 59
    COLON = 60
    SEMI = 61
    ASSIGN = 62
    BIT_OR = 63
    XOR = 64
    BIT_AND = 65
    BIT_NOT = 66
    LSHIFT = 67
    RSHIFT = 68
    ADD = 69
    MINUS = 70
    DIV = 71
    STAR = 72
    MOD = 73
    IDIV = 74
    POWER = 75
    AT = 76
    ARROW = 77
    LPAREN = 78
    RPAREN = 79
    LBRACK = 80
    RBRACK = 81
    LBRACE = 82
    RBRACE = 83
    LESS_THAN = 84
    GREATER_THAN = 85
    EQUALS = 86
    GT_EQ = 87
    LT_EQ = 88
    NOT_EQ = 89
    ADD_ASSIGN = 90
    SUB_ASSIGN = 91
    MULT_ASSIGN = 92
    AT_ASSIGN = 93
    DIV_ASSIGN = 94
    MOD_ASSIGN = 95
    AND_ASSIGN = 96
    OR_ASSIGN = 97
    XOR_ASSIGN = 98
    LSHIFT_ASSIGN = 99
    RSHIFT_ASSIGN = 100
    POWER_ASSIGN = 101
    IDIV_ASSIGN = 102
    STRING = 103
    NUMBER = 104
    ID = 105
    OPTION_ID = 106
    STRING_LITERAL = 107
    INTEGER = 108
    DECIMAL_INTEGER = 109
    OCT_INTEGER = 110
    HEX_INTEGER = 111
    BIN_INTEGER = 112
    FLOAT_NUMBER = 113
    NEWLINE = 114
    SKIP_ = 115
    UNKNOWN = 116

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
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.NEWLINE:
                self.state = 156
                self.match(YarcParser.NEWLINE)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(YarcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmts(self):
            return self.getTypedRuleContext(YarcParser.Simple_stmtsContext, 0)

        def compound_stmt(self):
            return self.getTypedRuleContext(YarcParser.Compound_stmtContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_stmt

    def stmt(self):
        localctx = YarcParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.NOT,
                YarcParser.ELLIPSIS,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
                YarcParser.STAR,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.simple_stmts()
                pass
            elif token in [YarcParser.FOR, YarcParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.compound_stmt()
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

    class Simple_stmtsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Simple_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Simple_stmtContext, i)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def SEMI(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.SEMI)
            else:
                return self.getToken(YarcParser.SEMI, i)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_stmts

    def simple_stmts(self):
        localctx = YarcParser.Simple_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmts)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.simple_stmt()
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 169
                    self.match(YarcParser.SEMI)
                    self.state = 170
                    self.simple_stmt()
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.SEMI:
                self.state = 176
                self.match(YarcParser.SEMI)

            self.state = 179
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_stmt(self):
            return self.getTypedRuleContext(YarcParser.Expr_stmtContext, 0)

        def pass_stmt(self):
            return self.getTypedRuleContext(YarcParser.Pass_stmtContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_stmt

    def simple_stmt(self):
        localctx = YarcParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.NOT,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
                YarcParser.STAR,
            ]:
                self.state = 181
                self.expr_stmt()
                pass
            elif token in [YarcParser.ELLIPSIS]:
                self.state = 182
                self.pass_stmt()
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

    class Expr_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testlist_star_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Testlist_star_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Testlist_star_exprContext, i)

        def annassign(self):
            return self.getTypedRuleContext(YarcParser.AnnassignContext, 0)

        def augassign(self):
            return self.getTypedRuleContext(YarcParser.AugassignContext, 0)

        def testlist(self):
            return self.getTypedRuleContext(YarcParser.TestlistContext, 0)

        def ASSIGN(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.ASSIGN)
            else:
                return self.getToken(YarcParser.ASSIGN, i)

        def getRuleIndex(self):
            return YarcParser.RULE_expr_stmt

    def expr_stmt(self):
        localctx = YarcParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.testlist_star_expr()
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 186
                self.annassign()
                pass
            elif token in [
                YarcParser.ADD_ASSIGN,
                YarcParser.SUB_ASSIGN,
                YarcParser.MULT_ASSIGN,
                YarcParser.AT_ASSIGN,
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
                self.state = 187
                self.augassign()

                self.state = 188
                self.testlist()
                pass
            elif token in [YarcParser.SEMI, YarcParser.ASSIGN, YarcParser.NEWLINE]:
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == YarcParser.ASSIGN:
                    self.state = 190
                    self.match(YarcParser.ASSIGN)

                    self.state = 191
                    self.testlist_star_expr()
                    self.state = 196
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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

    class AnnassignContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_annassign

    def annassign(self):
        localctx = YarcParser.AnnassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_annassign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(YarcParser.COLON)
            self.state = 200
            self.test()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.ASSIGN:
                self.state = 201
                self.match(YarcParser.ASSIGN)
                self.state = 202
                self.test()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Testlist_star_exprContext(ParserRuleContext):
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

        def star_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Star_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Star_exprContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_testlist_star_expr

    def testlist_star_expr(self):
        localctx = YarcParser.Testlist_star_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_testlist_star_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.NOT,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
            ]:
                self.state = 205
                self.test()
                pass
            elif token in [YarcParser.STAR]:
                self.state = 206
                self.star_expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 10, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 209
                    self.match(YarcParser.COMMA)
                    self.state = 212
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [
                        YarcParser.NOT,
                        YarcParser.BIT_NOT,
                        YarcParser.ADD,
                        YarcParser.MINUS,
                    ]:
                        self.state = 210
                        self.test()
                        pass
                    elif token in [YarcParser.STAR]:
                        self.state = 211
                        self.star_expr()
                        pass
                    else:
                        raise NoViableAltException(self)

                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 10, self._ctx)

            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 219
                self.match(YarcParser.COMMA)

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

        def AT_ASSIGN(self):
            return self.getToken(YarcParser.AT_ASSIGN, 0)

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
        self.enterRule(localctx, 14, self.RULE_augassign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not (
                ((_la - 90) & ~0x3F) == 0
                and (
                    (1 << (_la - 90))
                    & (
                        (1 << (YarcParser.ADD_ASSIGN - 90))
                        | (1 << (YarcParser.SUB_ASSIGN - 90))
                        | (1 << (YarcParser.MULT_ASSIGN - 90))
                        | (1 << (YarcParser.AT_ASSIGN - 90))
                        | (1 << (YarcParser.DIV_ASSIGN - 90))
                        | (1 << (YarcParser.MOD_ASSIGN - 90))
                        | (1 << (YarcParser.AND_ASSIGN - 90))
                        | (1 << (YarcParser.OR_ASSIGN - 90))
                        | (1 << (YarcParser.XOR_ASSIGN - 90))
                        | (1 << (YarcParser.LSHIFT_ASSIGN - 90))
                        | (1 << (YarcParser.RSHIFT_ASSIGN - 90))
                        | (1 << (YarcParser.POWER_ASSIGN - 90))
                        | (1 << (YarcParser.IDIV_ASSIGN - 90))
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

    class Pass_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELLIPSIS(self):
            return self.getToken(YarcParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_pass_stmt

    def pass_stmt(self):
        localctx = YarcParser.Pass_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pass_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(YarcParser.ELLIPSIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(YarcParser.RETURN, 0)

        def testlist(self):
            return self.getTypedRuleContext(YarcParser.TestlistContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_return_stmt

    def return_stmt(self):
        localctx = YarcParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(YarcParser.RETURN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la - 51) & ~0x3F) == 0 and (
                (1 << (_la - 51))
                & (
                    (1 << (YarcParser.NOT - 51))
                    | (1 << (YarcParser.BIT_NOT - 51))
                    | (1 << (YarcParser.ADD - 51))
                    | (1 << (YarcParser.MINUS - 51))
                )
            ) != 0:
                self.state = 227
                self.testlist()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_as_nameContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_import_as_name

    def import_as_name(self):
        localctx = YarcParser.Import_as_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_import_as_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dotted_as_nameContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dotted_name(self):
            return self.getTypedRuleContext(YarcParser.Dotted_nameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_dotted_as_name

    def dotted_as_name(self):
        localctx = YarcParser.Dotted_as_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dotted_as_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.dotted_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_as_namesContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_as_name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Import_as_nameContext)
            else:
                return self.getTypedRuleContext(YarcParser.Import_as_nameContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_import_as_names

    def import_as_names(self):
        localctx = YarcParser.Import_as_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_import_as_names)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.import_as_name()
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 13, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 235
                    self.match(YarcParser.COMMA)
                    self.state = 236
                    self.import_as_name()
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 13, self._ctx)

            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 242
                self.match(YarcParser.COMMA)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dotted_as_namesContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dotted_as_name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Dotted_as_nameContext)
            else:
                return self.getTypedRuleContext(YarcParser.Dotted_as_nameContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_dotted_as_names

    def dotted_as_names(self):
        localctx = YarcParser.Dotted_as_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dotted_as_names)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.dotted_as_name()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 246
                self.match(YarcParser.COMMA)
                self.state = 247
                self.dotted_as_name()
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

    class Dotted_nameContext(ParserRuleContext):
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

        def DOT(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.DOT)
            else:
                return self.getToken(YarcParser.DOT, i)

        def getRuleIndex(self):
            return YarcParser.RULE_dotted_name

    def dotted_name(self):
        localctx = YarcParser.Dotted_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dotted_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.name()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.DOT:
                self.state = 254
                self.match(YarcParser.DOT)
                self.state = 255
                self.name()
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

    class Compound_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(YarcParser.If_stmtContext, 0)

        def for_stmt(self):
            return self.getTypedRuleContext(YarcParser.For_stmtContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_compound_stmt

    def compound_stmt(self):
        localctx = YarcParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compound_stmt)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.if_stmt()
                pass
            elif token in [YarcParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.for_stmt()
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

    class If_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(YarcParser.IF, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def COLON(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COLON)
            else:
                return self.getToken(YarcParser.COLON, i)

        def block(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.BlockContext)
            else:
                return self.getTypedRuleContext(YarcParser.BlockContext, i)

        def ELSE(self):
            return self.getToken(YarcParser.ELSE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_if_stmt

    def if_stmt(self):
        localctx = YarcParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(YarcParser.IF)
            self.state = 266
            self.test()
            self.state = 267
            self.match(YarcParser.COLON)
            self.state = 268
            self.block()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.ELSE:
                self.state = 269
                self.match(YarcParser.ELSE)
                self.state = 270
                self.match(YarcParser.COLON)
                self.state = 271
                self.block()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_stmtContext(ParserRuleContext):
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

        def testlist(self):
            return self.getTypedRuleContext(YarcParser.TestlistContext, 0)

        def COLON(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COLON)
            else:
                return self.getToken(YarcParser.COLON, i)

        def block(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.BlockContext)
            else:
                return self.getTypedRuleContext(YarcParser.BlockContext, i)

        def ELSE(self):
            return self.getToken(YarcParser.ELSE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_for_stmt

    def for_stmt(self):
        localctx = YarcParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(YarcParser.FOR)
            self.state = 275
            self.exprlist()
            self.state = 276
            self.match(YarcParser.IN)
            self.state = 277
            self.testlist()
            self.state = 278
            self.match(YarcParser.COLON)
            self.state = 279
            self.block()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.ELSE:
                self.state = 280
                self.match(YarcParser.ELSE)
                self.state = 281
                self.match(YarcParser.COLON)
                self.state = 282
                self.block()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmts(self):
            return self.getTypedRuleContext(YarcParser.Simple_stmtsContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.StmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.StmtContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_block

    def block(self):
        localctx = YarcParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block)
        self._la = 0  # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.NOT,
                YarcParser.ELLIPSIS,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
                YarcParser.STAR,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.simple_stmts()
                pass
            elif token in [YarcParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(YarcParser.NEWLINE)
                self.state = 287
                self.match(YarcParser.INDENT)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 288
                    self.stmt()
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (
                        ((_la - 46) & ~0x3F) == 0
                        and (
                            (1 << (_la - 46))
                            & (
                                (1 << (YarcParser.FOR - 46))
                                | (1 << (YarcParser.IF - 46))
                                | (1 << (YarcParser.NOT - 46))
                                | (1 << (YarcParser.ELLIPSIS - 46))
                                | (1 << (YarcParser.BIT_NOT - 46))
                                | (1 << (YarcParser.ADD - 46))
                                | (1 << (YarcParser.MINUS - 46))
                                | (1 << (YarcParser.STAR - 46))
                            )
                        )
                        != 0
                    ):
                        break

                self.state = 293
                self.match(YarcParser.DEDENT)
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

    class Subject_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_named_expression(self):
            return self.getTypedRuleContext(YarcParser.Star_named_expressionContext, 0)

        def COMMA(self):
            return self.getToken(YarcParser.COMMA, 0)

        def star_named_expressions(self):
            return self.getTypedRuleContext(YarcParser.Star_named_expressionsContext, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_subject_expr

    def subject_expr(self):
        localctx = YarcParser.Subject_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_subject_expr)
        self._la = 0  # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 23, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.star_named_expression()
                self.state = 298
                self.match(YarcParser.COMMA)
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 299
                    self.star_named_expressions()

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.test()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Star_named_expressionsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def star_named_expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    YarcParser.Star_named_expressionContext
                )
            else:
                return self.getTypedRuleContext(
                    YarcParser.Star_named_expressionContext, i
                )

        def getRuleIndex(self):
            return YarcParser.RULE_star_named_expressions

    def star_named_expressions(self):
        localctx = YarcParser.Star_named_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_star_named_expressions)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(YarcParser.COMMA)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 306
                self.star_named_expression()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    ((_la - 51) & ~0x3F) == 0
                    and (
                        (1 << (_la - 51))
                        & (
                            (1 << (YarcParser.NOT - 51))
                            | (1 << (YarcParser.BIT_NOT - 51))
                            | (1 << (YarcParser.ADD - 51))
                            | (1 << (YarcParser.MINUS - 51))
                            | (1 << (YarcParser.STAR - 51))
                        )
                    )
                    != 0
                ):
                    break

            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 311
                self.match(YarcParser.COMMA)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Star_named_expressionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(YarcParser.STAR, 0)

        def expr(self):
            return self.getTypedRuleContext(YarcParser.ExprContext, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_star_named_expression

    def star_named_expression(self):
        localctx = YarcParser.Star_named_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_star_named_expression)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(YarcParser.STAR)
                self.state = 315
                self.expr()
                pass
            elif token in [
                YarcParser.NOT,
                YarcParser.BIT_NOT,
                YarcParser.ADD,
                YarcParser.MINUS,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.test()
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

    class GuardContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(YarcParser.IF, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_guard

    def guard(self):
        localctx = YarcParser.GuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_guard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(YarcParser.IF)
            self.state = 320
            self.test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatternsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Open_sequence_patternContext, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_patterns

    def patterns(self):
        localctx = YarcParser.PatternsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_patterns)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 27, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.open_sequence_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.pattern()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_pattern(self):
            return self.getTypedRuleContext(YarcParser.Or_patternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_pattern

    def pattern(self):
        localctx = YarcParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.or_pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closed_pattern(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Closed_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Closed_patternContext, i)

        def BIT_OR(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.BIT_OR)
            else:
                return self.getToken(YarcParser.BIT_OR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_or_pattern

    def or_pattern(self):
        localctx = YarcParser.Or_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_or_pattern)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.closed_pattern()
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_OR:
                self.state = 329
                self.match(YarcParser.BIT_OR)
                self.state = 330
                self.closed_pattern()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closed_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_pattern(self):
            return self.getTypedRuleContext(YarcParser.Literal_patternContext, 0)

        def capture_pattern(self):
            return self.getTypedRuleContext(YarcParser.Capture_patternContext, 0)

        def wildcard_pattern(self):
            return self.getTypedRuleContext(YarcParser.Wildcard_patternContext, 0)

        def value_pattern(self):
            return self.getTypedRuleContext(YarcParser.Value_patternContext, 0)

        def group_pattern(self):
            return self.getTypedRuleContext(YarcParser.Group_patternContext, 0)

        def sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Sequence_patternContext, 0)

        def mapping_pattern(self):
            return self.getTypedRuleContext(YarcParser.Mapping_patternContext, 0)

        def class_pattern(self):
            return self.getTypedRuleContext(YarcParser.Class_patternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_closed_pattern

    def closed_pattern(self):
        localctx = YarcParser.Closed_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_closed_pattern)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 29, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.literal_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.capture_pattern()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.wildcard_pattern()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 339
                self.value_pattern()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 340
                self.group_pattern()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 341
                self.sequence_pattern()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 342
                self.mapping_pattern()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 343
                self.class_pattern()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_number(self):
            return self.getTypedRuleContext(YarcParser.Signed_numberContext, 0)

        def complex_number(self):
            return self.getTypedRuleContext(YarcParser.Complex_numberContext, 0)

        def strings(self):
            return self.getTypedRuleContext(YarcParser.StringsContext, 0)

        def NONE(self):
            return self.getToken(YarcParser.NONE, 0)

        def TRUE(self):
            return self.getToken(YarcParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(YarcParser.FALSE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_literal_pattern

    def literal_pattern(self):
        localctx = YarcParser.Literal_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_literal_pattern)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 30, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.signed_number()
                self.state = 347
                if not self.CannotBePlusMinus():
                    from antlr4.error.Errors import FailedPredicateException

                    raise FailedPredicateException(
                        self, " $parser.CannotBePlusMinus() "
                    )
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.complex_number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.strings()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.match(YarcParser.NONE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 352
                self.match(YarcParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 353
                self.match(YarcParser.FALSE)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_number(self):
            return self.getTypedRuleContext(YarcParser.Signed_numberContext, 0)

        def complex_number(self):
            return self.getTypedRuleContext(YarcParser.Complex_numberContext, 0)

        def strings(self):
            return self.getTypedRuleContext(YarcParser.StringsContext, 0)

        def NONE(self):
            return self.getToken(YarcParser.NONE, 0)

        def TRUE(self):
            return self.getToken(YarcParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(YarcParser.FALSE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_literal_expr

    def literal_expr(self):
        localctx = YarcParser.Literal_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_literal_expr)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 31, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.signed_number()
                self.state = 357
                if not self.CannotBePlusMinus():
                    from antlr4.error.Errors import FailedPredicateException

                    raise FailedPredicateException(
                        self, " $parser.CannotBePlusMinus() "
                    )
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.complex_number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.strings()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.match(YarcParser.NONE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 362
                self.match(YarcParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 363
                self.match(YarcParser.FALSE)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Complex_numberContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_real_number(self):
            return self.getTypedRuleContext(YarcParser.Signed_real_numberContext, 0)

        def ADD(self):
            return self.getToken(YarcParser.ADD, 0)

        def imaginary_number(self):
            return self.getTypedRuleContext(YarcParser.Imaginary_numberContext, 0)

        def MINUS(self):
            return self.getToken(YarcParser.MINUS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_complex_number

    def complex_number(self):
        localctx = YarcParser.Complex_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_complex_number)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 32, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.signed_real_number()
                self.state = 367
                self.match(YarcParser.ADD)
                self.state = 368
                self.imaginary_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.signed_real_number()
                self.state = 371
                self.match(YarcParser.MINUS)
                self.state = 372
                self.imaginary_number()
                pass

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
        self.enterRule(localctx, 60, self.RULE_signed_number)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(YarcParser.NUMBER)
                pass
            elif token in [YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(YarcParser.MINUS)
                self.state = 378
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

    class Signed_real_numberContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def real_number(self):
            return self.getTypedRuleContext(YarcParser.Real_numberContext, 0)

        def MINUS(self):
            return self.getToken(YarcParser.MINUS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_signed_real_number

    def signed_real_number(self):
        localctx = YarcParser.Signed_real_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_signed_real_number)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.real_number()
                pass
            elif token in [YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(YarcParser.MINUS)
                self.state = 383
                self.real_number()
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

    class Real_numberContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YarcParser.NUMBER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_real_number

    def real_number(self):
        localctx = YarcParser.Real_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_real_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(YarcParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Imaginary_numberContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YarcParser.NUMBER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_imaginary_number

    def imaginary_number(self):
        localctx = YarcParser.Imaginary_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_imaginary_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(YarcParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Capture_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern_capture_target(self):
            return self.getTypedRuleContext(YarcParser.Pattern_capture_targetContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_capture_pattern

    def capture_pattern(self):
        localctx = YarcParser.Capture_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_capture_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.pattern_capture_target()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_capture_targetContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_pattern_capture_target

    def pattern_capture_target(self):
        localctx = YarcParser.Pattern_capture_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_pattern_capture_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.name()
            self.state = 393
            if not self.CannotBeDotLpEq():
                from antlr4.error.Errors import FailedPredicateException

                raise FailedPredicateException(self, " $parser.CannotBeDotLpEq() ")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Wildcard_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(YarcParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_wildcard_pattern

    def wildcard_pattern(self):
        localctx = YarcParser.Wildcard_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_wildcard_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(YarcParser.UNDERSCORE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(YarcParser.AttrContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_value_pattern

    def value_pattern(self):
        localctx = YarcParser.Value_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_value_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.attr()
            self.state = 398
            if not self.CannotBeDotLpEq():
                from antlr4.error.Errors import FailedPredicateException

                raise FailedPredicateException(self, " $parser.CannotBeDotLpEq() ")
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

        def name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext, i)

        def DOT(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.DOT)
            else:
                return self.getToken(YarcParser.DOT, i)

        def getRuleIndex(self):
            return YarcParser.RULE_attr

    def attr(self):
        localctx = YarcParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.name()
            self.state = 403
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 401
                    self.match(YarcParser.DOT)
                    self.state = 402
                    self.name()

                else:
                    raise NoViableAltException(self)
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Name_or_attrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(YarcParser.AttrContext, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_name_or_attr

    def name_or_attr(self):
        localctx = YarcParser.Name_or_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_name_or_attr)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 36, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.name()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Group_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_group_pattern

    def group_pattern(self):
        localctx = YarcParser.Group_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_group_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(YarcParser.LPAREN)
            self.state = 412
            self.pattern()
            self.state = 413
            self.match(YarcParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sequence_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def maybe_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Maybe_sequence_patternContext, 0)

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def open_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Open_sequence_patternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_sequence_pattern

    def sequence_pattern(self):
        localctx = YarcParser.Sequence_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_sequence_pattern)
        self._la = 0  # Token type
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(YarcParser.LBRACK)
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la - 45) & ~0x3F) == 0 and (
                    (1 << (_la - 45))
                    & (
                        (1 << (YarcParser.FALSE - 45))
                        | (1 << (YarcParser.NONE - 45))
                        | (1 << (YarcParser.TRUE - 45))
                        | (1 << (YarcParser.UNDERSCORE - 45))
                        | (1 << (YarcParser.MINUS - 45))
                        | (1 << (YarcParser.STAR - 45))
                        | (1 << (YarcParser.LPAREN - 45))
                        | (1 << (YarcParser.LBRACK - 45))
                        | (1 << (YarcParser.LBRACE - 45))
                        | (1 << (YarcParser.STRING - 45))
                        | (1 << (YarcParser.NUMBER - 45))
                        | (1 << (YarcParser.ID - 45))
                    )
                ) != 0:
                    self.state = 416
                    self.maybe_sequence_pattern()

                self.state = 419
                self.match(YarcParser.RBRACK)
                pass
            elif token in [YarcParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(YarcParser.LPAREN)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la - 45) & ~0x3F) == 0 and (
                    (1 << (_la - 45))
                    & (
                        (1 << (YarcParser.FALSE - 45))
                        | (1 << (YarcParser.NONE - 45))
                        | (1 << (YarcParser.TRUE - 45))
                        | (1 << (YarcParser.UNDERSCORE - 45))
                        | (1 << (YarcParser.MINUS - 45))
                        | (1 << (YarcParser.STAR - 45))
                        | (1 << (YarcParser.LPAREN - 45))
                        | (1 << (YarcParser.LBRACK - 45))
                        | (1 << (YarcParser.LBRACE - 45))
                        | (1 << (YarcParser.STRING - 45))
                        | (1 << (YarcParser.NUMBER - 45))
                        | (1 << (YarcParser.ID - 45))
                    )
                ) != 0:
                    self.state = 421
                    self.open_sequence_pattern()

                self.state = 424
                self.match(YarcParser.RPAREN)
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

    class Open_sequence_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def maybe_star_pattern(self):
            return self.getTypedRuleContext(YarcParser.Maybe_star_patternContext, 0)

        def COMMA(self):
            return self.getToken(YarcParser.COMMA, 0)

        def maybe_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Maybe_sequence_patternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_open_sequence_pattern

    def open_sequence_pattern(self):
        localctx = YarcParser.Open_sequence_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_open_sequence_pattern)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.maybe_star_pattern()
            self.state = 428
            self.match(YarcParser.COMMA)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la - 45) & ~0x3F) == 0 and (
                (1 << (_la - 45))
                & (
                    (1 << (YarcParser.FALSE - 45))
                    | (1 << (YarcParser.NONE - 45))
                    | (1 << (YarcParser.TRUE - 45))
                    | (1 << (YarcParser.UNDERSCORE - 45))
                    | (1 << (YarcParser.MINUS - 45))
                    | (1 << (YarcParser.STAR - 45))
                    | (1 << (YarcParser.LPAREN - 45))
                    | (1 << (YarcParser.LBRACK - 45))
                    | (1 << (YarcParser.LBRACE - 45))
                    | (1 << (YarcParser.STRING - 45))
                    | (1 << (YarcParser.NUMBER - 45))
                    | (1 << (YarcParser.ID - 45))
                )
            ) != 0:
                self.state = 429
                self.maybe_sequence_pattern()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Maybe_sequence_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def maybe_star_pattern(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Maybe_star_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Maybe_star_patternContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_maybe_sequence_pattern

    def maybe_sequence_pattern(self):
        localctx = YarcParser.Maybe_sequence_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_maybe_sequence_pattern)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.maybe_star_pattern()
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 41, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 433
                    self.match(YarcParser.COMMA)
                    self.state = 434
                    self.maybe_star_pattern()
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 41, self._ctx)

            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 440
                self.match(YarcParser.COMMA)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Maybe_star_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_pattern(self):
            return self.getTypedRuleContext(YarcParser.Star_patternContext, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_maybe_star_pattern

    def maybe_star_pattern(self):
        localctx = YarcParser.Maybe_star_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_maybe_star_pattern)
        try:
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.star_pattern()
                pass
            elif token in [
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.STRING,
                YarcParser.NUMBER,
                YarcParser.ID,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.pattern()
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

    class Star_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(YarcParser.STAR, 0)

        def pattern_capture_target(self):
            return self.getTypedRuleContext(YarcParser.Pattern_capture_targetContext, 0)

        def wildcard_pattern(self):
            return self.getTypedRuleContext(YarcParser.Wildcard_patternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_star_pattern

    def star_pattern(self):
        localctx = YarcParser.Star_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_star_pattern)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 44, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(YarcParser.STAR)
                self.state = 448
                self.pattern_capture_target()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.match(YarcParser.STAR)
                self.state = 450
                self.wildcard_pattern()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mapping_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(YarcParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YarcParser.RBRACE, 0)

        def double_star_pattern(self):
            return self.getTypedRuleContext(YarcParser.Double_star_patternContext, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def items_pattern(self):
            return self.getTypedRuleContext(YarcParser.Items_patternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_mapping_pattern

    def mapping_pattern(self):
        localctx = YarcParser.Mapping_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_mapping_pattern)
        self._la = 0  # Token type
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 48, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(YarcParser.LBRACE)
                self.state = 454
                self.match(YarcParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.match(YarcParser.LBRACE)
                self.state = 456
                self.double_star_pattern()
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 457
                    self.match(YarcParser.COMMA)

                self.state = 460
                self.match(YarcParser.RBRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.match(YarcParser.LBRACE)
                self.state = 463
                self.items_pattern()
                self.state = 464
                self.match(YarcParser.COMMA)
                self.state = 465
                self.double_star_pattern()
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 466
                    self.match(YarcParser.COMMA)

                self.state = 469
                self.match(YarcParser.RBRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 471
                self.match(YarcParser.LBRACE)
                self.state = 472
                self.items_pattern()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 473
                    self.match(YarcParser.COMMA)

                self.state = 476
                self.match(YarcParser.RBRACE)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Items_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key_value_pattern(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Key_value_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Key_value_patternContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_items_pattern

    def items_pattern(self):
        localctx = YarcParser.Items_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_items_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.key_value_pattern()
            self.state = 485
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 49, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 481
                    self.match(YarcParser.COMMA)
                    self.state = 482
                    self.key_value_pattern()
                self.state = 487
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 49, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Key_value_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext, 0)

        def literal_expr(self):
            return self.getTypedRuleContext(YarcParser.Literal_exprContext, 0)

        def attr(self):
            return self.getTypedRuleContext(YarcParser.AttrContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_key_value_pattern

    def key_value_pattern(self):
        localctx = YarcParser.Key_value_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_key_value_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.MINUS,
                YarcParser.STRING,
                YarcParser.NUMBER,
            ]:
                self.state = 488
                self.literal_expr()
                pass
            elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.state = 489
                self.attr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 492
            self.match(YarcParser.COLON)
            self.state = 493
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Double_star_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POWER(self):
            return self.getToken(YarcParser.POWER, 0)

        def pattern_capture_target(self):
            return self.getTypedRuleContext(YarcParser.Pattern_capture_targetContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_double_star_pattern

    def double_star_pattern(self):
        localctx = YarcParser.Double_star_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_double_star_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(YarcParser.POWER)
            self.state = 496
            self.pattern_capture_target()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self):
            return self.getTypedRuleContext(YarcParser.Name_or_attrContext, 0)

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def positional_patterns(self):
            return self.getTypedRuleContext(YarcParser.Positional_patternsContext, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def keyword_patterns(self):
            return self.getTypedRuleContext(YarcParser.Keyword_patternsContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_class_pattern

    def class_pattern(self):
        localctx = YarcParser.Class_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_class_pattern)
        self._la = 0  # Token type
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 54, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.name_or_attr()
                self.state = 499
                self.match(YarcParser.LPAREN)
                self.state = 500
                self.match(YarcParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.name_or_attr()
                self.state = 503
                self.match(YarcParser.LPAREN)
                self.state = 504
                self.positional_patterns()
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 505
                    self.match(YarcParser.COMMA)

                self.state = 508
                self.match(YarcParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
                self.name_or_attr()
                self.state = 511
                self.match(YarcParser.LPAREN)
                self.state = 512
                self.keyword_patterns()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 513
                    self.match(YarcParser.COMMA)

                self.state = 516
                self.match(YarcParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 518
                self.name_or_attr()
                self.state = 519
                self.match(YarcParser.LPAREN)
                self.state = 520
                self.positional_patterns()
                self.state = 521
                self.match(YarcParser.COMMA)
                self.state = 522
                self.keyword_patterns()
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COMMA:
                    self.state = 523
                    self.match(YarcParser.COMMA)

                self.state = 526
                self.match(YarcParser.RPAREN)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Positional_patternsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.PatternContext)
            else:
                return self.getTypedRuleContext(YarcParser.PatternContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_positional_patterns

    def positional_patterns(self):
        localctx = YarcParser.Positional_patternsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_positional_patterns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.pattern()
            self.state = 535
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 55, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 531
                    self.match(YarcParser.COMMA)
                    self.state = 532
                    self.pattern()
                self.state = 537
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 55, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Keyword_patternsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword_pattern(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Keyword_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Keyword_patternContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_keyword_patterns

    def keyword_patterns(self):
        localctx = YarcParser.Keyword_patternsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_keyword_patterns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.keyword_pattern()
            self.state = 543
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 56, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 539
                    self.match(YarcParser.COMMA)
                    self.state = 540
                    self.keyword_pattern()
                self.state = 545
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 56, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Keyword_patternContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_keyword_pattern

    def keyword_pattern(self):
        localctx = YarcParser.Keyword_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_keyword_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.name()
            self.state = 547
            self.match(YarcParser.ASSIGN)
            self.state = 548
            self.pattern()
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
        self.enterRule(localctx, 108, self.RULE_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.or_test()
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.IF:
                self.state = 551
                self.match(YarcParser.IF)
                self.state = 552
                self.or_test()
                self.state = 553
                self.match(YarcParser.ELSE)
                self.state = 554
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
        self.enterRule(localctx, 110, self.RULE_test_nocond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
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
        self.enterRule(localctx, 112, self.RULE_or_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.and_test()
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.OR:
                self.state = 561
                self.match(YarcParser.OR)
                self.state = 562
                self.and_test()
                self.state = 567
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
        self.enterRule(localctx, 114, self.RULE_and_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.not_test()
            self.state = 573
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.AND:
                self.state = 569
                self.match(YarcParser.AND)
                self.state = 570
                self.not_test()
                self.state = 575
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
        self.enterRule(localctx, 116, self.RULE_not_test)
        try:
            self.state = 579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(YarcParser.NOT)
                self.state = 577
                self.not_test()
                pass
            elif token in [YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
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
        self.enterRule(localctx, 118, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.expr()
            self.state = 587
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 61, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 582
                    self.comp_op()
                    self.state = 583
                    self.expr()
                self.state = 589
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 61, self._ctx)

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
        self.enterRule(localctx, 120, self.RULE_comp_op)
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 62, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 590
                self.match(YarcParser.LESS_THAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 591
                self.match(YarcParser.GREATER_THAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 592
                self.match(YarcParser.EQUALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 593
                self.match(YarcParser.GT_EQ)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 594
                self.match(YarcParser.LT_EQ)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 595
                self.match(YarcParser.NOT_EQ)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 596
                self.match(YarcParser.IN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 597
                self.match(YarcParser.NOT)
                self.state = 598
                self.match(YarcParser.IN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 599
                self.match(YarcParser.IS)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 600
                self.match(YarcParser.IS)
                self.state = 601
                self.match(YarcParser.NOT)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Star_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(YarcParser.STAR, 0)

        def expr(self):
            return self.getTypedRuleContext(YarcParser.ExprContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_star_expr

    def star_expr(self):
        localctx = YarcParser.Star_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_star_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(YarcParser.STAR)
            self.state = 605
            self.expr()
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
        self.enterRule(localctx, 124, self.RULE_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.xor_expr()
            self.state = 612
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_OR:
                self.state = 608
                self.match(YarcParser.BIT_OR)
                self.state = 609
                self.xor_expr()
                self.state = 614
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
        self.enterRule(localctx, 126, self.RULE_xor_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.and_expr()
            self.state = 620
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.XOR:
                self.state = 616
                self.match(YarcParser.XOR)
                self.state = 617
                self.and_expr()
                self.state = 622
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
        self.enterRule(localctx, 128, self.RULE_and_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.shift_expr()
            self.state = 628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_AND:
                self.state = 624
                self.match(YarcParser.BIT_AND)
                self.state = 625
                self.shift_expr()
                self.state = 630
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
        self.enterRule(localctx, 130, self.RULE_shift_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self.arith_expr()
            self.state = 636
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT:
                self.state = 632
                _la = self._input.LA(1)
                if not (_la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 633
                self.arith_expr()
                self.state = 638
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
        self.enterRule(localctx, 132, self.RULE_arith_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.term()
            self.state = 644
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 67, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 640
                    _la = self._input.LA(1)
                    if not (_la == YarcParser.ADD or _la == YarcParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 641
                    self.term()
                self.state = 646
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 67, self._ctx)

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

        def AT(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.AT)
            else:
                return self.getToken(YarcParser.AT, i)

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
        self.enterRule(localctx, 134, self.RULE_term)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.factor()
            self.state = 652
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 68, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 648
                    _la = self._input.LA(1)
                    if not (
                        ((_la - 71) & ~0x3F) == 0
                        and (
                            (1 << (_la - 71))
                            & (
                                (1 << (YarcParser.DIV - 71))
                                | (1 << (YarcParser.STAR - 71))
                                | (1 << (YarcParser.MOD - 71))
                                | (1 << (YarcParser.IDIV - 71))
                                | (1 << (YarcParser.AT - 71))
                            )
                        )
                        != 0
                    ):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 649
                    self.factor()
                self.state = 654
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 68, self._ctx)

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

        def getRuleIndex(self):
            return YarcParser.RULE_factor

    def factor(self):
        localctx = YarcParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_factor)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655
            _la = self._input.LA(1)
            if not (
                ((_la - 66) & ~0x3F) == 0
                and (
                    (1 << (_la - 66))
                    & (
                        (1 << (YarcParser.BIT_NOT - 66))
                        | (1 << (YarcParser.ADD - 66))
                        | (1 << (YarcParser.MINUS - 66))
                    )
                )
                != 0
            ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 656
            self.factor()
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

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def NUMBER(self):
            return self.getToken(YarcParser.NUMBER, 0)

        def STRING(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.STRING)
            else:
                return self.getToken(YarcParser.STRING, i)

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
        self.enterRule(localctx, 138, self.RULE_atom)
        self._la = 0  # Token type
        try:
            self.state = 669
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 658
                self.name()
                pass
            elif token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.match(YarcParser.NUMBER)
                pass
            elif token in [YarcParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 661
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 660
                    self.match(YarcParser.STRING)
                    self.state = 663
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == YarcParser.STRING):
                        break

                pass
            elif token in [YarcParser.ELLIPSIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 665
                self.match(YarcParser.ELLIPSIS)
                pass
            elif token in [YarcParser.NONE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 666
                self.match(YarcParser.NONE)
                pass
            elif token in [YarcParser.TRUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 667
                self.match(YarcParser.TRUE)
                pass
            elif token in [YarcParser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 668
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

        def getRuleIndex(self):
            return YarcParser.RULE_name

    def name(self):
        localctx = YarcParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
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
        self.enterRule(localctx, 142, self.RULE_subscriptlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.subscript_()
            self.state = 678
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 71, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 674
                    self.match(YarcParser.COMMA)
                    self.state = 675
                    self.subscript_()
                self.state = 680
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 71, self._ctx)

            self.state = 682
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 681
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
        self.enterRule(localctx, 144, self.RULE_subscript_)
        self._la = 0  # Token type
        try:
            self.state = 695
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 76, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 684
                self.test()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 686
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la - 51) & ~0x3F) == 0 and (
                    (1 << (_la - 51))
                    & (
                        (1 << (YarcParser.NOT - 51))
                        | (1 << (YarcParser.BIT_NOT - 51))
                        | (1 << (YarcParser.ADD - 51))
                        | (1 << (YarcParser.MINUS - 51))
                    )
                ) != 0:
                    self.state = 685
                    self.test()

                self.state = 688
                self.match(YarcParser.COLON)
                self.state = 690
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la - 51) & ~0x3F) == 0 and (
                    (1 << (_la - 51))
                    & (
                        (1 << (YarcParser.NOT - 51))
                        | (1 << (YarcParser.BIT_NOT - 51))
                        | (1 << (YarcParser.ADD - 51))
                        | (1 << (YarcParser.MINUS - 51))
                    )
                ) != 0:
                    self.state = 689
                    self.test()

                self.state = 693
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COLON:
                    self.state = 692
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
        self.enterRule(localctx, 146, self.RULE_sliceop)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 697
            self.match(YarcParser.COLON)
            self.state = 699
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la - 51) & ~0x3F) == 0 and (
                (1 << (_la - 51))
                & (
                    (1 << (YarcParser.NOT - 51))
                    | (1 << (YarcParser.BIT_NOT - 51))
                    | (1 << (YarcParser.ADD - 51))
                    | (1 << (YarcParser.MINUS - 51))
                )
            ) != 0:
                self.state = 698
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

        def star_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Star_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Star_exprContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_exprlist

    def exprlist(self):
        localctx = YarcParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_exprlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                self.state = 701
                self.expr()
                pass
            elif token in [YarcParser.STAR]:
                self.state = 702
                self.star_expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 712
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 80, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 705
                    self.match(YarcParser.COMMA)
                    self.state = 708
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                        self.state = 706
                        self.expr()
                        pass
                    elif token in [YarcParser.STAR]:
                        self.state = 707
                        self.star_expr()
                        pass
                    else:
                        raise NoViableAltException(self)

                self.state = 714
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 80, self._ctx)

            self.state = 716
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 715
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
        self.enterRule(localctx, 150, self.RULE_testlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
            self.test()
            self.state = 723
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 82, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 719
                    self.match(YarcParser.COMMA)
                    self.state = 720
                    self.test()
                self.state = 725
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 82, self._ctx)

            self.state = 727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COMMA:
                self.state = 726
                self.match(YarcParser.COMMA)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Encoding_declContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_encoding_decl

    def encoding_decl(self):
        localctx = YarcParser.Encoding_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_encoding_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.STRING)
            else:
                return self.getToken(YarcParser.STRING, i)

        def getRuleIndex(self):
            return YarcParser.RULE_strings

    def strings(self):
        localctx = YarcParser.StringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_strings)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 731
                self.match(YarcParser.STRING)
                self.state = 734
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.STRING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.literal_pattern_sempred
        self._predicates[28] = self.literal_expr_sempred
        self._predicates[35] = self.pattern_capture_target_sempred
        self._predicates[37] = self.value_pattern_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def literal_pattern_sempred(self, localctx: Literal_patternContext, predIndex: int):
        if predIndex == 0:
            return self.CannotBePlusMinus()

    def literal_expr_sempred(self, localctx: Literal_exprContext, predIndex: int):
        if predIndex == 1:
            return self.CannotBePlusMinus()

    def pattern_capture_target_sempred(
        self, localctx: Pattern_capture_targetContext, predIndex: int
    ):
        if predIndex == 2:
            return self.CannotBeDotLpEq()

    def value_pattern_sempred(self, localctx: Value_patternContext, predIndex: int):
        if predIndex == 3:
            return self.CannotBeDotLpEq()
