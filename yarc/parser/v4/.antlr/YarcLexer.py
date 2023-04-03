# Generated from /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/parser/v4/YarcLexer.g4 by ANTLR 4.9.2
from typing import TextIO

import sys
from io import StringIO

from antlr4 import *

if __name__ is not None and "." in __name__:
    from .YarcLexerBase import YarcLexerBase
else:
    from YarcLexerBase import YarcLexerBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2W")
        buf.write("\u0294\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write('\t\36\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%')
        buf.write("\4&\t&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\7\6\u00f1\n\6\f\6\16\6\u00f4")
        buf.write("\13\6\5\6\u00f6\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3'\3'\3'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3")
        buf.write(">\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3")
        buf.write("D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3G\3G\3G\3G\3H\3H\3H\3")
        buf.write("H\3I\3I\3J\3J\5J\u01cf\nJ\3K\3K\7K\u01d3\nK\fK\16K\u01d6")
        buf.write("\13K\3L\3L\3L\5L\u01db\nL\3L\3L\5L\u01df\nL\3L\5L\u01e2")
        buf.write("\nL\5L\u01e4\nL\3L\3L\3M\3M\5M\u01ea\nM\3M\3M\5M\u01ee")
        buf.write("\nM\3M\5M\u01f1\nM\3M\3M\3N\3N\3N\3N\5N\u01f9\nN\3O\3")
        buf.write("O\7O\u01fd\nO\fO\16O\u0200\13O\3O\6O\u0203\nO\rO\16O\u0204")
        buf.write("\5O\u0207\nO\3P\3P\3P\6P\u020c\nP\rP\16P\u020d\3Q\3Q\3")
        buf.write("Q\6Q\u0213\nQ\rQ\16Q\u0214\3R\3R\3R\6R\u021a\nR\rR\16")
        buf.write("R\u021b\3S\3S\5S\u0220\nS\3T\3T\3T\5T\u0225\nT\3T\3T\3")
        buf.write("U\3U\3V\3V\3V\7V\u022e\nV\fV\16V\u0231\13V\3V\3V\3V\3")
        buf.write("V\7V\u0237\nV\fV\16V\u023a\13V\3V\5V\u023d\nV\3W\3W\3")
        buf.write("W\3W\5W\u0243\nW\3X\3X\3Y\3Y\3Z\3Z\3[\3[\5[\u024d\n[\3")
        buf.write("\\\3\\\3]\5]\u0252\n]\3]\3]\3]\3]\5]\u0258\n]\3^\3^\5")
        buf.write("^\u025c\n^\3^\3^\3_\6_\u0261\n_\r_\16_\u0262\3`\3`\6`")
        buf.write("\u0267\n`\r`\16`\u0268\3a\3a\5a\u026d\na\3a\6a\u0270\n")
        buf.write("a\ra\16a\u0271\3b\6b\u0275\nb\rb\16b\u0276\3c\3c\7c\u027b")
        buf.write("\nc\fc\16c\u027e\13c\3d\3d\5d\u0282\nd\3d\5d\u0285\nd")
        buf.write("\3d\3d\5d\u0289\nd\3e\3e\3f\3f\5f\u028f\nf\3g\3g\5g\u0293")
        buf.write("\ng\3\u00f2\2h\3\5\5\6\7\7\t\b\13\2\r\t\17\n\21\13\23")
        buf.write("\f\25\r\27\16\31\17\33\20\35\21\37\22!\23#\24%\25'\26")
        buf.write(')\27+\30-\31/\32\61\33\63\34\65\35\67\369\37; =!?"A#')
        buf.write("C$E%G&I'K(M)O*Q+S,U-W.Y/[\60]\61_\62a\63c\64e\65g\66")
        buf.write("i\67k8m9o:q;s<u=w>y?{@}A\177B\u0081C\u0083D\u0085E\u0087")
        buf.write("F\u0089G\u008bH\u008dI\u008fJ\u0091K\u0093L\u0095M\u0097")
        buf.write("N\u0099O\u009bP\u009dQ\u009fR\u00a1S\u00a3T\u00a5U\u00a7")
        buf.write("V\u00a9W\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5")
        buf.write("\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf\2\u00c1\2\u00c3")
        buf.write("\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd\2\3\2\20\4\2")
        buf.write("WWww\4\2HHhh\4\2TTtt\4\2QQqq\4\2ZZzz\4\2DDdd\6\2\f\f\16")
        buf.write("\17))^^\6\2\f\f\16\17$$^^\4\2CHch\4\2GGgg\4\2--//\4\2")
        buf.write('\13\13""\4\2\f\f\16\17\4\2C\\c|\2\u02ae\2\3\3\2\2\2')
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\3\u00cf\3\2\2\2\5\u00d8\3\2\2\2\7\u00e2\3\2\2")
        buf.write("\2\t\u00eb\3\2\2\2\13\u00ed\3\2\2\2\r\u00f9\3\2\2\2\17")
        buf.write("\u00fd\3\2\2\2\21\u0100\3\2\2\2\23\u0104\3\2\2\2\25\u0108")
        buf.write("\3\2\2\2\27\u010d\3\2\2\2\31\u0112\3\2\2\2\33\u0118\3")
        buf.write("\2\2\2\35\u011c\3\2\2\2\37\u011f\3\2\2\2!\u0122\3\2\2")
        buf.write("\2#\u0125\3\2\2\2%\u012a\3\2\2\2'\u012e\3\2\2\2)\u0131")
        buf.write("\3\2\2\2+\u0136\3\2\2\2-\u013d\3\2\2\2/\u0142\3\2\2\2")
        buf.write("\61\u0144\3\2\2\2\63\u0149\3\2\2\2\65\u014b\3\2\2\2\67")
        buf.write("\u014e\3\2\2\29\u0152\3\2\2\2;\u0154\3\2\2\2=\u0156\3")
        buf.write("\2\2\2?\u0158\3\2\2\2A\u015a\3\2\2\2C\u015c\3\2\2\2E\u015e")
        buf.write("\3\2\2\2G\u0160\3\2\2\2I\u0162\3\2\2\2K\u0164\3\2\2\2")
        buf.write("M\u0167\3\2\2\2O\u016a\3\2\2\2Q\u016c\3\2\2\2S\u016e\3")
        buf.write("\2\2\2U\u0170\3\2\2\2W\u0172\3\2\2\2Y\u0175\3\2\2\2[\u0178")
        buf.write("\3\2\2\2]\u017a\3\2\2\2_\u017d\3\2\2\2a\u0180\3\2\2\2")
        buf.write("c\u0183\3\2\2\2e\u0186\3\2\2\2g\u0189\3\2\2\2i\u018c\3")
        buf.write("\2\2\2k\u018f\3\2\2\2m\u0191\3\2\2\2o\u0193\3\2\2\2q\u0196")
        buf.write("\3\2\2\2s\u0199\3\2\2\2u\u019c\3\2\2\2w\u019f\3\2\2\2")
        buf.write("y\u01a2\3\2\2\2{\u01a5\3\2\2\2}\u01a8\3\2\2\2\177\u01ab")
        buf.write("\3\2\2\2\u0081\u01ae\3\2\2\2\u0083\u01b1\3\2\2\2\u0085")
        buf.write("\u01b4\3\2\2\2\u0087\u01b7\3\2\2\2\u0089\u01ba\3\2\2\2")
        buf.write("\u008b\u01be\3\2\2\2\u008d\u01c2\3\2\2\2\u008f\u01c6\3")
        buf.write("\2\2\2\u0091\u01ca\3\2\2\2\u0093\u01ce\3\2\2\2\u0095\u01d0")
        buf.write("\3\2\2\2\u0097\u01e3\3\2\2\2\u0099\u01f0\3\2\2\2\u009b")
        buf.write("\u01f8\3\2\2\2\u009d\u0206\3\2\2\2\u009f\u0208\3\2\2\2")
        buf.write("\u00a1\u020f\3\2\2\2\u00a3\u0216\3\2\2\2\u00a5\u021f\3")
        buf.write("\2\2\2\u00a7\u0224\3\2\2\2\u00a9\u0228\3\2\2\2\u00ab\u023c")
        buf.write("\3\2\2\2\u00ad\u0242\3\2\2\2\u00af\u0244\3\2\2\2\u00b1")
        buf.write("\u0246\3\2\2\2\u00b3\u0248\3\2\2\2\u00b5\u024c\3\2\2\2")
        buf.write("\u00b7\u024e\3\2\2\2\u00b9\u0257\3\2\2\2\u00bb\u025b\3")
        buf.write("\2\2\2\u00bd\u0260\3\2\2\2\u00bf\u0264\3\2\2\2\u00c1\u026a")
        buf.write("\3\2\2\2\u00c3\u0274\3\2\2\2\u00c5\u0278\3\2\2\2\u00c7")
        buf.write("\u027f\3\2\2\2\u00c9\u028a\3\2\2\2\u00cb\u028e\3\2\2\2")
        buf.write("\u00cd\u0292\3\2\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7")
        buf.write("e\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\4\3\2\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7r\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7u\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e1\5g\64\2\u00e1\6\3\2\2\2\u00e2\u00e3")
        buf.write("\7y\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00ea\5g\64\2\u00ea\b\3\2\2\2\u00eb\u00ec")
        buf.write("\5\13\6\2\u00ec\n\3\2\2\2\u00ed\u00f5\5g\64\2\u00ee\u00f6")
        buf.write("\5\13\6\2\u00ef\u00f1\13\2\2\2\u00f0\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f4\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00ee\3")
        buf.write("\2\2\2\u00f5\u00f2\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8")
        buf.write("\5i\65\2\u00f8\f\3\2\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb")
        buf.write("\7p\2\2\u00fb\u00fc\7f\2\2\u00fc\16\3\2\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7u\2\2\u00ff\20\3\2\2\2\u0100\u0101")
        buf.write("\7f\2\2\u0101\u0102\7g\2\2\u0102\u0103\7h\2\2\u0103\22")
        buf.write("\3\2\2\2\u0104\u0105\7f\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\24\3\2\2\2\u0108\u0109\7g\2\2\u0109\u010a")
        buf.write("\7n\2\2\u010a\u010b\7k\2\2\u010b\u010c\7h\2\2\u010c\26")
        buf.write("\3\2\2\2\u010d\u010e\7g\2\2\u010e\u010f\7n\2\2\u010f\u0110")
        buf.write("\7u\2\2\u0110\u0111\7g\2\2\u0111\30\3\2\2\2\u0112\u0113")
        buf.write("\7H\2\2\u0113\u0114\7c\2\2\u0114\u0115\7n\2\2\u0115\u0116")
        buf.write("\7u\2\2\u0116\u0117\7g\2\2\u0117\32\3\2\2\2\u0118\u0119")
        buf.write("\7h\2\2\u0119\u011a\7q\2\2\u011a\u011b\7t\2\2\u011b\34")
        buf.write("\3\2\2\2\u011c\u011d\7k\2\2\u011d\u011e\7h\2\2\u011e\36")
        buf.write("\3\2\2\2\u011f\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121 ")
        buf.write('\3\2\2\2\u0122\u0123\7k\2\2\u0123\u0124\7u\2\2\u0124"')
        buf.write("\3\2\2\2\u0125\u0126\7P\2\2\u0126\u0127\7q\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7g\2\2\u0129$\3\2\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7q\2\2\u012c\u012d\7v\2\2\u012d&\3")
        buf.write("\2\2\2\u012e\u012f\7q\2\2\u012f\u0130\7t\2\2\u0130(\3")
        buf.write("\2\2\2\u0131\u0132\7r\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7u\2\2\u0134\u0135\7u\2\2\u0135*\3\2\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7g\2\2\u0138\u0139\7v\2\2\u0139\u013a")
        buf.write("\7w\2\2\u013a\u013b\7t\2\2\u013b\u013c\7p\2\2\u013c,\3")
        buf.write("\2\2\2\u013d\u013e\7V\2\2\u013e\u013f\7t\2\2\u013f\u0140")
        buf.write("\7w\2\2\u0140\u0141\7g\2\2\u0141.\3\2\2\2\u0142\u0143")
        buf.write("\7a\2\2\u0143\60\3\2\2\2\u0144\u0145\7y\2\2\u0145\u0146")
        buf.write("\7k\2\2\u0146\u0147\7v\2\2\u0147\u0148\7j\2\2\u0148\62")
        buf.write("\3\2\2\2\u0149\u014a\7\60\2\2\u014a\64\3\2\2\2\u014b\u014c")
        buf.write("\7\60\2\2\u014c\u014d\7\60\2\2\u014d\66\3\2\2\2\u014e")
        buf.write("\u014f\7\60\2\2\u014f\u0150\7\60\2\2\u0150\u0151\7\60")
        buf.write("\2\2\u01518\3\2\2\2\u0152\u0153\7,\2\2\u0153:\3\2\2\2")
        buf.write("\u0154\u0155\7.\2\2\u0155<\3\2\2\2\u0156\u0157\7<\2\2")
        buf.write("\u0157>\3\2\2\2\u0158\u0159\7=\2\2\u0159@\3\2\2\2\u015a")
        buf.write("\u015b\7?\2\2\u015bB\3\2\2\2\u015c\u015d\7~\2\2\u015d")
        buf.write("D\3\2\2\2\u015e\u015f\7`\2\2\u015fF\3\2\2\2\u0160\u0161")
        buf.write("\7(\2\2\u0161H\3\2\2\2\u0162\u0163\7\u0080\2\2\u0163J")
        buf.write("\3\2\2\2\u0164\u0165\7>\2\2\u0165\u0166\7>\2\2\u0166L")
        buf.write("\3\2\2\2\u0167\u0168\7@\2\2\u0168\u0169\7@\2\2\u0169N")
        buf.write("\3\2\2\2\u016a\u016b\7-\2\2\u016bP\3\2\2\2\u016c\u016d")
        buf.write("\7/\2\2\u016dR\3\2\2\2\u016e\u016f\7\61\2\2\u016fT\3\2")
        buf.write("\2\2\u0170\u0171\7'\2\2\u0171V\3\2\2\2\u0172\u0173\7")
        buf.write("\61\2\2\u0173\u0174\7\61\2\2\u0174X\3\2\2\2\u0175\u0176")
        buf.write("\7,\2\2\u0176\u0177\7,\2\2\u0177Z\3\2\2\2\u0178\u0179")
        buf.write("\7B\2\2\u0179\\\3\2\2\2\u017a\u017b\7/\2\2\u017b\u017c")
        buf.write("\7@\2\2\u017c^\3\2\2\2\u017d\u017e\7*\2\2\u017e\u017f")
        buf.write("\b\60\2\2\u017f`\3\2\2\2\u0180\u0181\7+\2\2\u0181\u0182")
        buf.write("\b\61\3\2\u0182b\3\2\2\2\u0183\u0184\7]\2\2\u0184\u0185")
        buf.write("\b\62\4\2\u0185d\3\2\2\2\u0186\u0187\7_\2\2\u0187\u0188")
        buf.write("\b\63\5\2\u0188f\3\2\2\2\u0189\u018a\7}\2\2\u018a\u018b")
        buf.write("\b\64\6\2\u018bh\3\2\2\2\u018c\u018d\7\177\2\2\u018d\u018e")
        buf.write("\b\65\7\2\u018ej\3\2\2\2\u018f\u0190\7>\2\2\u0190l\3\2")
        buf.write("\2\2\u0191\u0192\7@\2\2\u0192n\3\2\2\2\u0193\u0194\7?")
        buf.write("\2\2\u0194\u0195\7?\2\2\u0195p\3\2\2\2\u0196\u0197\7@")
        buf.write("\2\2\u0197\u0198\7?\2\2\u0198r\3\2\2\2\u0199\u019a\7>")
        buf.write("\2\2\u019a\u019b\7?\2\2\u019bt\3\2\2\2\u019c\u019d\7#")
        buf.write("\2\2\u019d\u019e\7?\2\2\u019ev\3\2\2\2\u019f\u01a0\7-")
        buf.write("\2\2\u01a0\u01a1\7?\2\2\u01a1x\3\2\2\2\u01a2\u01a3\7/")
        buf.write("\2\2\u01a3\u01a4\7?\2\2\u01a4z\3\2\2\2\u01a5\u01a6\7,")
        buf.write("\2\2\u01a6\u01a7\7?\2\2\u01a7|\3\2\2\2\u01a8\u01a9\7B")
        buf.write("\2\2\u01a9\u01aa\7?\2\2\u01aa~\3\2\2\2\u01ab\u01ac\7\61")
        buf.write("\2\2\u01ac\u01ad\7?\2\2\u01ad\u0080\3\2\2\2\u01ae\u01af")
        buf.write("\7'\2\2\u01af\u01b0\7?\2\2\u01b0\u0082\3\2\2\2\u01b1")
        buf.write("\u01b2\7(\2\2\u01b2\u01b3\7?\2\2\u01b3\u0084\3\2\2\2\u01b4")
        buf.write("\u01b5\7~\2\2\u01b5\u01b6\7?\2\2\u01b6\u0086\3\2\2\2\u01b7")
        buf.write("\u01b8\7`\2\2\u01b8\u01b9\7?\2\2\u01b9\u0088\3\2\2\2\u01ba")
        buf.write("\u01bb\7>\2\2\u01bb\u01bc\7>\2\2\u01bc\u01bd\7?\2\2\u01bd")
        buf.write("\u008a\3\2\2\2\u01be\u01bf\7@\2\2\u01bf\u01c0\7@\2\2\u01c0")
        buf.write("\u01c1\7?\2\2\u01c1\u008c\3\2\2\2\u01c2\u01c3\7,\2\2\u01c3")
        buf.write("\u01c4\7,\2\2\u01c4\u01c5\7?\2\2\u01c5\u008e\3\2\2\2\u01c6")
        buf.write("\u01c7\7\61\2\2\u01c7\u01c8\7\61\2\2\u01c8\u01c9\7?\2")
        buf.write("\2\u01c9\u0090\3\2\2\2\u01ca\u01cb\5\u0099M\2\u01cb\u0092")
        buf.write("\3\2\2\2\u01cc\u01cf\5\u009bN\2\u01cd\u01cf\5\u00a5S\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\u0094\3")
        buf.write("\2\2\2\u01d0\u01d4\5\u00cbf\2\u01d1\u01d3\5\u00cdg\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5\u0096\3\2\2\2\u01d6\u01d4\3")
        buf.write("\2\2\2\u01d7\u01d8\6L\2\2\u01d8\u01e4\5\u00c3b\2\u01d9")
        buf.write("\u01db\7\17\2\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2")
        buf.write("\2\u01db\u01dc\3\2\2\2\u01dc\u01df\7\f\2\2\u01dd\u01df")
        buf.write("\4\16\17\2\u01de\u01da\3\2\2\2\u01de\u01dd\3\2\2\2\u01df")
        buf.write("\u01e1\3\2\2\2\u01e0\u01e2\5\u00c3b\2\u01e1\u01e0\3\2")
        buf.write("\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01d7")
        buf.write("\3\2\2\2\u01e3\u01de\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("\u01e6\bL\b\2\u01e6\u0098\3\2\2\2\u01e7\u01f1\t\2\2\2")
        buf.write("\u01e8\u01ea\t\3\2\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea\3")
        buf.write("\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01f1\t\4\2\2\u01ec\u01ee")
        buf.write("\t\4\2\2\u01ed\u01ec\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f1\t\3\2\2\u01f0\u01e7\3\2\2\2")
        buf.write("\u01f0\u01e9\3\2\2\2\u01f0\u01ed\3\2\2\2\u01f0\u01f1\3")
        buf.write("\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\5\u00abV\2\u01f3")
        buf.write("\u009a\3\2\2\2\u01f4\u01f9\5\u009dO\2\u01f5\u01f9\5\u009f")
        buf.write("P\2\u01f6\u01f9\5\u00a1Q\2\u01f7\u01f9\5\u00a3R\2\u01f8")
        buf.write("\u01f4\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f8\u01f6\3\2\2\2")
        buf.write("\u01f8\u01f7\3\2\2\2\u01f9\u009c\3\2\2\2\u01fa\u01fe\5")
        buf.write("\u00afX\2\u01fb\u01fd\5\u00b1Y\2\u01fc\u01fb\3\2\2\2\u01fd")
        buf.write("\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ff\u0207\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0203\7")
        buf.write("\62\2\2\u0202\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0207\3\2\2\2")
        buf.write("\u0206\u01fa\3\2\2\2\u0206\u0202\3\2\2\2\u0207\u009e\3")
        buf.write("\2\2\2\u0208\u0209\7\62\2\2\u0209\u020b\t\5\2\2\u020a")
        buf.write("\u020c\5\u00b3Z\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2")
        buf.write("\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u00a0")
        buf.write("\3\2\2\2\u020f\u0210\7\62\2\2\u0210\u0212\t\6\2\2\u0211")
        buf.write("\u0213\5\u00b5[\2\u0212\u0211\3\2\2\2\u0213\u0214\3\2")
        buf.write("\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u00a2")
        buf.write("\3\2\2\2\u0216\u0217\7\62\2\2\u0217\u0219\t\7\2\2\u0218")
        buf.write("\u021a\5\u00b7\\\2\u0219\u0218\3\2\2\2\u021a\u021b\3\2")
        buf.write("\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u00a4")
        buf.write("\3\2\2\2\u021d\u0220\5\u00b9]\2\u021e\u0220\5\u00bb^\2")
        buf.write("\u021f\u021d\3\2\2\2\u021f\u021e\3\2\2\2\u0220\u00a6\3")
        buf.write("\2\2\2\u0221\u0225\5\u00c3b\2\u0222\u0225\5\u00c5c\2\u0223")
        buf.write("\u0225\5\u00c7d\2\u0224\u0221\3\2\2\2\u0224\u0222\3\2")
        buf.write("\2\2\u0224\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227")
        buf.write("\bT\t\2\u0227\u00a8\3\2\2\2\u0228\u0229\13\2\2\2\u0229")
        buf.write("\u00aa\3\2\2\2\u022a\u022f\7)\2\2\u022b\u022e\5\u00ad")
        buf.write("W\2\u022c\u022e\n\b\2\2\u022d\u022b\3\2\2\2\u022d\u022c")
        buf.write("\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f")
        buf.write("\u0230\3\2\2\2\u0230\u0232\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0232\u023d\7)\2\2\u0233\u0238\7$\2\2\u0234\u0237\5\u00ad")
        buf.write("W\2\u0235\u0237\n\t\2\2\u0236\u0234\3\2\2\2\u0236\u0235")
        buf.write("\3\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0238")
        buf.write("\u0239\3\2\2\2\u0239\u023b\3\2\2\2\u023a\u0238\3\2\2\2")
        buf.write("\u023b\u023d\7$\2\2\u023c\u022a\3\2\2\2\u023c\u0233\3")
        buf.write("\2\2\2\u023d\u00ac\3\2\2\2\u023e\u023f\7^\2\2\u023f\u0243")
        buf.write("\13\2\2\2\u0240\u0241\7^\2\2\u0241\u0243\5\u0097L\2\u0242")
        buf.write("\u023e\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u00ae\3\2\2\2")
        buf.write("\u0244\u0245\4\63;\2\u0245\u00b0\3\2\2\2\u0246\u0247\4")
        buf.write("\62;\2\u0247\u00b2\3\2\2\2\u0248\u0249\4\629\2\u0249\u00b4")
        buf.write("\3\2\2\2\u024a\u024d\5\u00b1Y\2\u024b\u024d\t\n\2\2\u024c")
        buf.write("\u024a\3\2\2\2\u024c\u024b\3\2\2\2\u024d\u00b6\3\2\2\2")
        buf.write("\u024e\u024f\4\62\63\2\u024f\u00b8\3\2\2\2\u0250\u0252")
        buf.write("\5\u00bd_\2\u0251\u0250\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write("\u0253\3\2\2\2\u0253\u0258\5\u00bf`\2\u0254\u0255\5\u00bd")
        buf.write("_\2\u0255\u0256\7\60\2\2\u0256\u0258\3\2\2\2\u0257\u0251")
        buf.write("\3\2\2\2\u0257\u0254\3\2\2\2\u0258\u00ba\3\2\2\2\u0259")
        buf.write("\u025c\5\u00bd_\2\u025a\u025c\5\u00b9]\2\u025b\u0259\3")
        buf.write("\2\2\2\u025b\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e")
        buf.write("\5\u00c1a\2\u025e\u00bc\3\2\2\2\u025f\u0261\5\u00b1Y\2")
        buf.write("\u0260\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0260\3")
        buf.write("\2\2\2\u0262\u0263\3\2\2\2\u0263\u00be\3\2\2\2\u0264\u0266")
        buf.write("\7\60\2\2\u0265\u0267\5\u00b1Y\2\u0266\u0265\3\2\2\2\u0267")
        buf.write("\u0268\3\2\2\2\u0268\u0266\3\2\2\2\u0268\u0269\3\2\2\2")
        buf.write("\u0269\u00c0\3\2\2\2\u026a\u026c\t\13\2\2\u026b\u026d")
        buf.write("\t\f\2\2\u026c\u026b\3\2\2\2\u026c\u026d\3\2\2\2\u026d")
        buf.write("\u026f\3\2\2\2\u026e\u0270\5\u00b1Y\2\u026f\u026e\3\2")
        buf.write("\2\2\u0270\u0271\3\2\2\2\u0271\u026f\3\2\2\2\u0271\u0272")
        buf.write("\3\2\2\2\u0272\u00c2\3\2\2\2\u0273\u0275\t\r\2\2\u0274")
        buf.write("\u0273\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0274\3\2\2\2")
        buf.write("\u0276\u0277\3\2\2\2\u0277\u00c4\3\2\2\2\u0278\u027c\7")
        buf.write("%\2\2\u0279\u027b\n\16\2\2\u027a\u0279\3\2\2\2\u027b\u027e")
        buf.write("\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027d\3\2\2\2\u027d")
        buf.write("\u00c6\3\2\2\2\u027e\u027c\3\2\2\2\u027f\u0281\7^\2\2")
        buf.write("\u0280\u0282\5\u00c3b\2\u0281\u0280\3\2\2\2\u0281\u0282")
        buf.write("\3\2\2\2\u0282\u0288\3\2\2\2\u0283\u0285\7\17\2\2\u0284")
        buf.write("\u0283\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0286\3\2\2\2")
        buf.write("\u0286\u0289\7\f\2\2\u0287\u0289\4\16\17\2\u0288\u0284")
        buf.write("\3\2\2\2\u0288\u0287\3\2\2\2\u0289\u00c8\3\2\2\2\u028a")
        buf.write("\u028b\t\17\2\2\u028b\u00ca\3\2\2\2\u028c\u028f\5/\30")
        buf.write("\2\u028d\u028f\5\u00c9e\2\u028e\u028c\3\2\2\2\u028e\u028d")
        buf.write("\3\2\2\2\u028f\u00cc\3\2\2\2\u0290\u0293\5\u00cbf\2\u0291")
        buf.write("\u0293\5\u00b1Y\2\u0292\u0290\3\2\2\2\u0292\u0291\3\2")
        buf.write("\2\2\u0293\u00ce\3\2\2\2,\2\u00f2\u00f5\u01ce\u01d4\u01da")
        buf.write("\u01de\u01e1\u01e3\u01e9\u01ed\u01f0\u01f8\u01fe\u0204")
        buf.write("\u0206\u020d\u0214\u021b\u021f\u0224\u022d\u022f\u0236")
        buf.write("\u0238\u023c\u0242\u024c\u0251\u0257\u025b\u0262\u0268")
        buf.write("\u026c\u0271\u0276\u027c\u0281\u0284\u0288\u028e\u0292")
        buf.write("\n\3\60\2\3\61\3\3\62\4\3\63\5\3\64\6\3\65\7\3L\b\b\2")
        buf.write("\2")
        return buf.getvalue()


class YarcLexer(YarcLexerBase):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    INDENT = 1
    DEDENT = 2
    SCENARIO = 3
    OPTIONS = 4
    WRITER = 5
    SNIPPET = 6
    AND = 7
    AS = 8
    DEF = 9
    DEL = 10
    ELIF = 11
    ELSE = 12
    FALSE = 13
    FOR = 14
    IF = 15
    IN = 16
    IS = 17
    NONE = 18
    NOT = 19
    OR = 20
    PASS = 21
    RETURN = 22
    TRUE = 23
    UNDERSCORE = 24
    WITH = 25
    DOT = 26
    RANGE = 27
    ELLIPSIS = 28
    STAR = 29
    COMMA = 30
    COLON = 31
    SEMI_COLON = 32
    ASSIGN = 33
    OR_OP = 34
    XOR = 35
    AND_OP = 36
    NOT_OP = 37
    LEFT_SHIFT = 38
    RIGHT_SHIFT = 39
    ADD = 40
    MINUS = 41
    DIV = 42
    MOD = 43
    IDIV = 44
    POWER = 45
    AT = 46
    ARROW = 47
    OPEN_PAREN = 48
    CLOSE_PAREN = 49
    OPEN_BRACK = 50
    CLOSE_BRACK = 51
    OPEN_BRACE = 52
    CLOSE_BRACE = 53
    LESS_THAN = 54
    GREATER_THAN = 55
    EQUALS = 56
    GT_EQ = 57
    LT_EQ = 58
    NOT_EQ = 59
    ADD_ASSIGN = 60
    SUB_ASSIGN = 61
    MULT_ASSIGN = 62
    AT_ASSIGN = 63
    DIV_ASSIGN = 64
    MOD_ASSIGN = 65
    AND_ASSIGN = 66
    OR_ASSIGN = 67
    XOR_ASSIGN = 68
    LEFT_SHIFT_ASSIGN = 69
    RIGHT_SHIFT_ASSIGN = 70
    POWER_ASSIGN = 71
    IDIV_ASSIGN = 72
    STRING = 73
    NUMBER = 74
    NAME = 75
    NEWLINE = 76
    STRING_LITERAL = 77
    INTEGER = 78
    DECIMAL_INTEGER = 79
    OCT_INTEGER = 80
    HEX_INTEGER = 81
    BIN_INTEGER = 82
    FLOAT_NUMBER = 83
    SKIP_ = 84
    UNKNOWN_CHAR = 85

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = [
        "<INVALID>",
        "'scenario'",
        "'and'",
        "'as'",
        "'def'",
        "'del'",
        "'elif'",
        "'else'",
        "'False'",
        "'for'",
        "'if'",
        "'in'",
        "'is'",
        "'None'",
        "'not'",
        "'or'",
        "'pass'",
        "'return'",
        "'True'",
        "'_'",
        "'with'",
        "'.'",
        "'..'",
        "'...'",
        "'*'",
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
        "OPTIONS",
        "WRITER",
        "SNIPPET",
        "AND",
        "AS",
        "DEF",
        "DEL",
        "ELIF",
        "ELSE",
        "FALSE",
        "FOR",
        "IF",
        "IN",
        "IS",
        "NONE",
        "NOT",
        "OR",
        "PASS",
        "RETURN",
        "TRUE",
        "UNDERSCORE",
        "WITH",
        "DOT",
        "RANGE",
        "ELLIPSIS",
        "STAR",
        "COMMA",
        "COLON",
        "SEMI_COLON",
        "ASSIGN",
        "OR_OP",
        "XOR",
        "AND_OP",
        "NOT_OP",
        "LEFT_SHIFT",
        "RIGHT_SHIFT",
        "ADD",
        "MINUS",
        "DIV",
        "MOD",
        "IDIV",
        "POWER",
        "AT",
        "ARROW",
        "OPEN_PAREN",
        "CLOSE_PAREN",
        "OPEN_BRACK",
        "CLOSE_BRACK",
        "OPEN_BRACE",
        "CLOSE_BRACE",
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
        "LEFT_SHIFT_ASSIGN",
        "RIGHT_SHIFT_ASSIGN",
        "POWER_ASSIGN",
        "IDIV_ASSIGN",
        "STRING",
        "NUMBER",
        "NAME",
        "NEWLINE",
        "STRING_LITERAL",
        "INTEGER",
        "DECIMAL_INTEGER",
        "OCT_INTEGER",
        "HEX_INTEGER",
        "BIN_INTEGER",
        "FLOAT_NUMBER",
        "SKIP_",
        "UNKNOWN_CHAR",
    ]

    ruleNames = [
        "SCENARIO",
        "OPTIONS",
        "WRITER",
        "SNIPPET",
        "NESTED_CODE",
        "AND",
        "AS",
        "DEF",
        "DEL",
        "ELIF",
        "ELSE",
        "FALSE",
        "FOR",
        "IF",
        "IN",
        "IS",
        "NONE",
        "NOT",
        "OR",
        "PASS",
        "RETURN",
        "TRUE",
        "UNDERSCORE",
        "WITH",
        "DOT",
        "RANGE",
        "ELLIPSIS",
        "STAR",
        "COMMA",
        "COLON",
        "SEMI_COLON",
        "ASSIGN",
        "OR_OP",
        "XOR",
        "AND_OP",
        "NOT_OP",
        "LEFT_SHIFT",
        "RIGHT_SHIFT",
        "ADD",
        "MINUS",
        "DIV",
        "MOD",
        "IDIV",
        "POWER",
        "AT",
        "ARROW",
        "OPEN_PAREN",
        "CLOSE_PAREN",
        "OPEN_BRACK",
        "CLOSE_BRACK",
        "OPEN_BRACE",
        "CLOSE_BRACE",
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
        "LEFT_SHIFT_ASSIGN",
        "RIGHT_SHIFT_ASSIGN",
        "POWER_ASSIGN",
        "IDIV_ASSIGN",
        "STRING",
        "NUMBER",
        "NAME",
        "NEWLINE",
        "STRING_LITERAL",
        "INTEGER",
        "DECIMAL_INTEGER",
        "OCT_INTEGER",
        "HEX_INTEGER",
        "BIN_INTEGER",
        "FLOAT_NUMBER",
        "SKIP_",
        "UNKNOWN_CHAR",
        "SHORT_STRING",
        "STRING_ESCAPE_SEQ",
        "NON_ZERO_DIGIT",
        "DIGIT",
        "OCT_DIGIT",
        "HEX_DIGIT",
        "BIN_DIGIT",
        "POINT_FLOAT",
        "EXPONENT_FLOAT",
        "INT_PART",
        "FRACTION",
        "EXPONENT",
        "SPACES",
        "COMMENT",
        "LINE_JOINING",
        "LETTER",
        "ID_START",
        "ID_CONTINUE",
    ]

    grammarFileName = "YarcLexer.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache()
        )
        self._actions = None
        self._predicates = None

    def action(self, localctx: RuleContext, ruleIndex: int, actionIndex: int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.OPEN_PAREN_action
            actions[47] = self.CLOSE_PAREN_action
            actions[48] = self.OPEN_BRACK_action
            actions[49] = self.CLOSE_BRACK_action
            actions[50] = self.OPEN_BRACE_action
            actions[51] = self.CLOSE_BRACE_action
            actions[74] = self.NEWLINE_action
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def OPEN_PAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 0:
            self.openBrace()

    def CLOSE_PAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 1:
            self.closeBrace()

    def OPEN_BRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 2:
            self.openBrace()

    def CLOSE_BRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 3:
            self.closeBrace()

    def OPEN_BRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 4:
            self.openBrace()

    def CLOSE_BRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 5:
            self.closeBrace()

    def NEWLINE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 6:
            self.onNewLine()

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates is None:
            preds = dict()
            preds[74] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx: RuleContext, predIndex: int):
        if predIndex == 0:
            return self.atStartOfInput()
