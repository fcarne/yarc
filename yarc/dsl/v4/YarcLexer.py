# Generated from /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/dsl/v4/YarcLexer.g4 by ANTLR 4.9.2
import sys
from io import StringIO

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if __name__ is not None and "." in __name__:
    from .YarcLexerBase import YarcLexerBase
else:
    from YarcLexerBase import YarcLexerBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2v")
        buf.write("\u03bb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write("\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u017f")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\5\32\u01c7\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\5!\u01ee\n!\3")
        buf.write('"\3"\3"\3"\3"\3"\3"\3"\3"\5"\u01f9\n"\5"\u01fb')
        buf.write('\n"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3')
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3'\3'\3'\3'")
        buf.write("\3'\3'\3'\3'\3'\3(\3(\3(\3(\3(\3)\3)\3)\3)\7)\u022c")
        buf.write("\n)\f)\16)\u022f\13)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+")
        buf.write("\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\39\3:\3:\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3M\3M\3M\3N\3")
        buf.write("N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3")
        buf.write("T\3U\3U\3V\3V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3")
        buf.write("[\3[\3[\3\\\3\\\3\\\3]\3]\3]\3^\3^\3^\3_\3_\3_\3`\3`\3")
        buf.write("`\3a\3a\3a\3b\3b\3b\3c\3c\3c\3c\3d\3d\3d\3d\3e\3e\3e\3")
        buf.write("e\3f\3f\3f\3f\3g\3g\3h\3h\5h\u02f3\nh\3i\3i\7i\u02f7\n")
        buf.write("i\fi\16i\u02fa\13i\3j\3j\3j\3k\3k\5k\u0301\nk\3k\3k\5")
        buf.write("k\u0305\nk\3k\5k\u0308\nk\3k\3k\3l\3l\3l\3l\5l\u0310\n")
        buf.write("l\3m\3m\7m\u0314\nm\fm\16m\u0317\13m\3m\6m\u031a\nm\r")
        buf.write("m\16m\u031b\5m\u031e\nm\3n\3n\3n\6n\u0323\nn\rn\16n\u0324")
        buf.write("\3o\3o\3o\6o\u032a\no\ro\16o\u032b\3p\3p\3p\6p\u0331\n")
        buf.write("p\rp\16p\u0332\3q\3q\5q\u0337\nq\3r\3r\3r\5r\u033c\nr")
        buf.write("\3r\3r\5r\u0340\nr\3r\5r\u0343\nr\5r\u0345\nr\3r\3r\3")
        buf.write("s\3s\3s\5s\u034c\ns\3s\3s\3t\3t\3u\3u\3u\7u\u0355\nu\f")
        buf.write("u\16u\u0358\13u\3u\3u\3u\3u\7u\u035e\nu\fu\16u\u0361\13")
        buf.write("u\3u\5u\u0364\nu\3v\3v\3v\3v\5v\u036a\nv\3w\3w\3x\3x\3")
        buf.write("y\3y\3z\3z\5z\u0374\nz\3{\3{\3|\5|\u0379\n|\3|\3|\3|\3")
        buf.write("|\5|\u037f\n|\3}\3}\5}\u0383\n}\3}\3}\3~\6~\u0388\n~\r")
        buf.write("~\16~\u0389\3\177\3\177\6\177\u038e\n\177\r\177\16\177")
        buf.write("\u038f\3\u0080\3\u0080\5\u0080\u0394\n\u0080\3\u0080\6")
        buf.write("\u0080\u0397\n\u0080\r\u0080\16\u0080\u0398\3\u0081\3")
        buf.write("\u0081\5\u0081\u039d\n\u0081\3\u0082\3\u0082\5\u0082\u03a1")
        buf.write("\n\u0082\3\u0083\3\u0083\3\u0084\6\u0084\u03a6\n\u0084")
        buf.write("\r\u0084\16\u0084\u03a7\3\u0085\3\u0085\7\u0085\u03ac")
        buf.write("\n\u0085\f\u0085\16\u0085\u03af\13\u0085\3\u0086\3\u0086")
        buf.write("\5\u0086\u03b3\n\u0086\3\u0086\5\u0086\u03b6\n\u0086\3")
        buf.write("\u0086\3\u0086\5\u0086\u03ba\n\u0086\3\u022d\2\u0087\3")
        buf.write("\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31")
        buf.write("\20\33\21\35\22\37\23!\24#\25%\26'\27)\30+\31-\32/\33")
        buf.write("\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G'I(K)M*O+Q\2")
        buf.write("S,U-W.Y/[\60]\61_\62a\63c\64e\65g\66i\67k8m9o:q;s<u=w")
        buf.write(">y?{@}A\177B\u0081C\u0083D\u0085E\u0087F\u0089G\u008b")
        buf.write("H\u008dI\u008fJ\u0091K\u0093L\u0095M\u0097N\u0099O\u009b")
        buf.write("P\u009dQ\u009fR\u00a1S\u00a3T\u00a5U\u00a7V\u00a9W\u00ab")
        buf.write("X\u00adY\u00afZ\u00b1[\u00b3\\\u00b5]\u00b7^\u00b9_\u00bb")
        buf.write("`\u00bda\u00bfb\u00c1c\u00c3d\u00c5e\u00c7f\u00c9g\u00cb")
        buf.write("h\u00cdi\u00cfj\u00d1k\u00d3l\u00d5m\u00d7n\u00d9o\u00db")
        buf.write("p\u00ddq\u00dfr\u00e1s\u00e3t\u00e5u\u00e7v\u00e9\2\u00eb")
        buf.write("\2\u00ed\2\u00ef\2\u00f1\2\u00f3\2\u00f5\2\u00f7\2\u00f9")
        buf.write("\2\u00fb\2\u00fd\2\u00ff\2\u0101\2\u0103\2\u0105\2\u0107")
        buf.write("\2\u0109\2\u010b\2\3\2\21\4\2Z\\z|\4\2WWww\4\2HHhh\4\2")
        buf.write("TTtt\4\2QQqq\4\2ZZzz\4\2DDdd\6\2\f\f\16\17))^^\6\2\f\f")
        buf.write("\16\17$$^^\4\2CHch\4\2GGgg\4\2--//\4\2C\\c|\4\2\13\13")
        buf.write('""\4\2\f\f\16\17\2\u03da\2\3\3\2\2\2\2\5\3\2\2\2\2\7')
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[")
        buf.write("\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2")
        buf.write("\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7")
        buf.write("\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2")
        buf.write("\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5")
        buf.write("\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2")
        buf.write("\2\2\u00dd\3\2\2\2\2\u00df\3\2\2\2\2\u00e1\3\2\2\2\2\u00e3")
        buf.write("\3\2\2\2\2\u00e5\3\2\2\2\2\u00e7\3\2\2\2\3\u010d\3\2\2")
        buf.write("\2\5\u0116\3\2\2\2\7\u011f\3\2\2\2\t\u0126\3\2\2\2\13")
        buf.write("\u012e\3\2\2\2\r\u0135\3\2\2\2\17\u013c\3\2\2\2\21\u0145")
        buf.write("\3\2\2\2\23\u0150\3\2\2\2\25\u0157\3\2\2\2\27\u0163\3")
        buf.write("\2\2\2\31\u0169\3\2\2\2\33\u016e\3\2\2\2\35\u0172\3\2")
        buf.write("\2\2\37\u017e\3\2\2\2!\u0180\3\2\2\2#\u0184\3\2\2\2%\u018e")
        buf.write("\3\2\2\2'\u0195\3\2\2\2)\u019b\3\2\2\2+\u01a5\3\2\2\2")
        buf.write("-\u01ad\3\2\2\2/\u01b2\3\2\2\2\61\u01ba\3\2\2\2\63\u01c6")
        buf.write("\3\2\2\2\65\u01c8\3\2\2\2\67\u01cf\3\2\2\29\u01d7\3\2")
        buf.write("\2\2;\u01da\3\2\2\2=\u01dd\3\2\2\2?\u01e0\3\2\2\2A\u01e6")
        buf.write("\3\2\2\2C\u01ef\3\2\2\2E\u01fc\3\2\2\2G\u0203\3\2\2\2")
        buf.write("I\u0209\3\2\2\2K\u0210\3\2\2\2M\u0219\3\2\2\2O\u0222\3")
        buf.write("\2\2\2Q\u0227\3\2\2\2S\u0233\3\2\2\2U\u0237\3\2\2\2W\u023b")
        buf.write("\3\2\2\2Y\u0240\3\2\2\2[\u0246\3\2\2\2]\u024a\3\2\2\2")
        buf.write("_\u024d\3\2\2\2a\u0250\3\2\2\2c\u0253\3\2\2\2e\u0258\3")
        buf.write("\2\2\2g\u025c\3\2\2\2i\u025f\3\2\2\2k\u0266\3\2\2\2m\u026b")
        buf.write("\3\2\2\2o\u026d\3\2\2\2q\u026f\3\2\2\2s\u0272\3\2\2\2")
        buf.write("u\u0276\3\2\2\2w\u0278\3\2\2\2y\u027a\3\2\2\2{\u027c\3")
        buf.write("\2\2\2}\u027e\3\2\2\2\177\u0280\3\2\2\2\u0081\u0282\3")
        buf.write("\2\2\2\u0083\u0284\3\2\2\2\u0085\u0286\3\2\2\2\u0087\u0289")
        buf.write("\3\2\2\2\u0089\u028c\3\2\2\2\u008b\u028e\3\2\2\2\u008d")
        buf.write("\u0290\3\2\2\2\u008f\u0292\3\2\2\2\u0091\u0294\3\2\2\2")
        buf.write("\u0093\u0296\3\2\2\2\u0095\u0299\3\2\2\2\u0097\u029c\3")
        buf.write("\2\2\2\u0099\u029e\3\2\2\2\u009b\u02a1\3\2\2\2\u009d\u02a4")
        buf.write("\3\2\2\2\u009f\u02a7\3\2\2\2\u00a1\u02aa\3\2\2\2\u00a3")
        buf.write("\u02ad\3\2\2\2\u00a5\u02b0\3\2\2\2\u00a7\u02b3\3\2\2\2")
        buf.write("\u00a9\u02b5\3\2\2\2\u00ab\u02b7\3\2\2\2\u00ad\u02ba\3")
        buf.write("\2\2\2\u00af\u02bd\3\2\2\2\u00b1\u02c0\3\2\2\2\u00b3\u02c3")
        buf.write("\3\2\2\2\u00b5\u02c6\3\2\2\2\u00b7\u02c9\3\2\2\2\u00b9")
        buf.write("\u02cc\3\2\2\2\u00bb\u02cf\3\2\2\2\u00bd\u02d2\3\2\2\2")
        buf.write("\u00bf\u02d5\3\2\2\2\u00c1\u02d8\3\2\2\2\u00c3\u02db\3")
        buf.write("\2\2\2\u00c5\u02de\3\2\2\2\u00c7\u02e2\3\2\2\2\u00c9\u02e6")
        buf.write("\3\2\2\2\u00cb\u02ea\3\2\2\2\u00cd\u02ee\3\2\2\2\u00cf")
        buf.write("\u02f2\3\2\2\2\u00d1\u02f4\3\2\2\2\u00d3\u02fb\3\2\2\2")
        buf.write("\u00d5\u0307\3\2\2\2\u00d7\u030f\3\2\2\2\u00d9\u031d\3")
        buf.write("\2\2\2\u00db\u031f\3\2\2\2\u00dd\u0326\3\2\2\2\u00df\u032d")
        buf.write("\3\2\2\2\u00e1\u0336\3\2\2\2\u00e3\u0344\3\2\2\2\u00e5")
        buf.write("\u034b\3\2\2\2\u00e7\u034f\3\2\2\2\u00e9\u0363\3\2\2\2")
        buf.write("\u00eb\u0369\3\2\2\2\u00ed\u036b\3\2\2\2\u00ef\u036d\3")
        buf.write("\2\2\2\u00f1\u036f\3\2\2\2\u00f3\u0373\3\2\2\2\u00f5\u0375")
        buf.write("\3\2\2\2\u00f7\u037e\3\2\2\2\u00f9\u0382\3\2\2\2\u00fb")
        buf.write("\u0387\3\2\2\2\u00fd\u038b\3\2\2\2\u00ff\u0391\3\2\2\2")
        buf.write("\u0101\u039c\3\2\2\2\u0103\u03a0\3\2\2\2\u0105\u03a2\3")
        buf.write("\2\2\2\u0107\u03a5\3\2\2\2\u0109\u03a9\3\2\2\2\u010b\u03b0")
        buf.write("\3\2\2\2\u010d\u010e\7u\2\2\u010e\u010f\7e\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110\u0111\7p\2\2\u0111\u0112\7c\2\2\u0112\u0113")
        buf.write("\7t\2\2\u0113\u0114\7k\2\2\u0114\u0115\7q\2\2\u0115\4")
        buf.write("\3\2\2\2\u0116\u0117\7u\2\2\u0117\u0118\7g\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\u011a\7v\2\2\u011a\u011b\7k\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c\u011d\7i\2\2\u011d\u011e\7u\2\2\u011e\6")
        buf.write("\3\2\2\2\u011f\u0120\7y\2\2\u0120\u0121\7t\2\2\u0121\u0122")
        buf.write("\7k\2\2\u0122\u0123\7v\2\2\u0123\u0124\7g\2\2\u0124\u0125")
        buf.write("\7t\2\2\u0125\b\3\2\2\2\u0126\u0127\7W\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7k\2\2\u0129\u012a\7h\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7t\2\2\u012c\u012d\7o\2\2\u012d\n")
        buf.write("\3\2\2\2\u012e\u012f\7P\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131\u0132\7o\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7n\2\2\u0134\f\3\2\2\2\u0135\u0136\7E\2\2\u0136\u0137")
        buf.write("\7j\2\2\u0137\u0138\7q\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7e\2\2\u013a\u013b\7g\2\2\u013b\16\3\2\2\2\u013c\u013d")
        buf.write("\7U\2\2\u013d\u013e\7g\2\2\u013e\u013f\7s\2\2\u013f\u0140")
        buf.write("\7w\2\2\u0140\u0141\7g\2\2\u0141\u0142\7p\2\2\u0142\u0143")
        buf.write("\7e\2\2\u0143\u0144\7g\2\2\u0144\20\3\2\2\2\u0145\u0146")
        buf.write("\7N\2\2\u0146\u0147\7q\2\2\u0147\u0148\7i\2\2\u0148\u0149")
        buf.write("\7W\2\2\u0149\u014a\7p\2\2\u014a\u014b\7k\2\2\u014b\u014c")
        buf.write("\7h\2\2\u014c\u014d\7q\2\2\u014d\u014e\7t\2\2\u014e\u014f")
        buf.write("\7o\2\2\u014f\22\3\2\2\2\u0150\u0151\7e\2\2\u0151\u0152")
        buf.write("\7t\2\2\u0152\u0153\7g\2\2\u0153\u0154\7c\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155\u0156\7g\2\2\u0156\24\3\2\2\2\u0157\u0158")
        buf.write("\7k\2\2\u0158\u0159\7p\2\2\u0159\u015a\7u\2\2\u015a\u015b")
        buf.write("\7v\2\2\u015b\u015c\7c\2\2\u015c\u015d\7p\2\2\u015d\u015e")
        buf.write("\7v\2\2\u015e\u015f\7k\2\2\u015f\u0160\7c\2\2\u0160\u0161")
        buf.write("\7v\2\2\u0161\u0162\7g\2\2\u0162\26\3\2\2\2\u0163\u0164")
        buf.write("\7i\2\2\u0164\u0165\7t\2\2\u0165\u0166\7q\2\2\u0166\u0167")
        buf.write("\7w\2\2\u0167\u0168\7r\2\2\u0168\30\3\2\2\2\u0169\u016a")
        buf.write("\7q\2\2\u016a\u016b\7r\2\2\u016b\u016c\7g\2\2\u016c\u016d")
        buf.write("\7p\2\2\u016d\32\3\2\2\2\u016e\u016f\7i\2\2\u016f\u0170")
        buf.write("\7g\2\2\u0170\u0171\7v\2\2\u0171\34\3\2\2\2\u0172\u0173")
        buf.write("\t\2\2\2\u0173\36\3\2\2\2\u0174\u0175\7g\2\2\u0175\u0176")
        buf.write("\7f\2\2\u0176\u0177\7k\2\2\u0177\u017f\7v\2\2\u0178\u0179")
        buf.write("\7o\2\2\u0179\u017a\7q\2\2\u017a\u017b\7f\2\2\u017b\u017c")
        buf.write("\7k\2\2\u017c\u017d\7h\2\2\u017d\u017f\7{\2\2\u017e\u0174")
        buf.write("\3\2\2\2\u017e\u0178\3\2\2\2\u017f \3\2\2\2\u0180\u0181")
        buf.write('\7u\2\2\u0181\u0182\7g\2\2\u0182\u0183\7v\2\2\u0183"')
        buf.write("\3\2\2\2\u0184\u0185\7v\2\2\u0185\u0186\7t\2\2\u0186\u0187")
        buf.write("\7c\2\2\u0187\u0188\7p\2\2\u0188\u0189\7u\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018a\u018b\7c\2\2\u018b\u018c\7v\2\2\u018c\u018d")
        buf.write("\7g\2\2\u018d$\3\2\2\2\u018e\u018f\7t\2\2\u018f\u0190")
        buf.write("\7q\2\2\u0190\u0191\7v\2\2\u0191\u0192\7c\2\2\u0192\u0193")
        buf.write("\7v\2\2\u0193\u0194\7g\2\2\u0194&\3\2\2\2\u0195\u0196")
        buf.write("\7u\2\2\u0196\u0197\7e\2\2\u0197\u0198\7c\2\2\u0198\u0199")
        buf.write("\7n\2\2\u0199\u019a\7g\2\2\u019a(\3\2\2\2\u019b\u019c")
        buf.write("\7u\2\2\u019c\u019d\7g\2\2\u019d\u019e\7o\2\2\u019e\u019f")
        buf.write("\7c\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2")
        buf.write("\7k\2\2\u01a2\u01a3\7e\2\2\u01a3\u01a4\7u\2\2\u01a4*\3")
        buf.write("\2\2\2\u01a5\u01a6\7x\2\2\u01a6\u01a7\7k\2\2\u01a7\u01a8")
        buf.write("\7u\2\2\u01a8\u01a9\7k\2\2\u01a9\u01aa\7d\2\2\u01aa\u01ab")
        buf.write("\7n\2\2\u01ab\u01ac\7g\2\2\u01ac,\3\2\2\2\u01ad\u01ae")
        buf.write("\7u\2\2\u01ae\u01af\7k\2\2\u01af\u01b0\7|\2\2\u01b0\u01b1")
        buf.write("\7g\2\2\u01b1.\3\2\2\2\u01b2\u01b3\7n\2\2\u01b3\u01b4")
        buf.write("\7q\2\2\u01b4\u01b5\7q\2\2\u01b5\u01b6\7m\2\2\u01b6\u01b7")
        buf.write("\7a\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9\7v\2\2\u01b9\60")
        buf.write("\3\2\2\2\u01ba\u01bb\7u\2\2\u01bb\u01bc\7e\2\2\u01bc\u01bd")
        buf.write("\7c\2\2\u01bd\u01be\7v\2\2\u01be\u01bf\7v\2\2\u01bf\u01c0")
        buf.write("\7g\2\2\u01c0\u01c1\7t\2\2\u01c1\62\3\2\2\2\u01c2\u01c3")
        buf.write("\7\64\2\2\u01c3\u01c7\7f\2\2\u01c4\u01c5\7\65\2\2\u01c5")
        buf.write("\u01c7\7f\2\2\u01c6\u01c2\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c7\64\3\2\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca\7t\2")
        buf.write("\2\u01ca\u01cb\7q\2\2\u01cb\u01cc\7w\2\2\u01cc\u01cd\7")
        buf.write("p\2\2\u01cd\u01ce\7f\2\2\u01ce\66\3\2\2\2\u01cf\u01d0")
        buf.write("\7v\2\2\u01d0\u01d1\7g\2\2\u01d1\u01d2\7z\2\2\u01d2\u01d3")
        buf.write("\7v\2\2\u01d3\u01d4\7w\2\2\u01d4\u01d5\7t\2\2\u01d5\u01d6")
        buf.write("\7g\2\2\u01d68\3\2\2\2\u01d7\u01d8\7v\2\2\u01d8\u01d9")
        buf.write("\7q\2\2\u01d9:\3\2\2\2\u01da\u01db\7q\2\2\u01db\u01dc")
        buf.write("\7p\2\2\u01dc<\3\2\2\2\u01dd\u01de\7w\2\2\u01de\u01df")
        buf.write("\7r\2\2\u01df>\3\2\2\2\u01e0\u01e1\7g\2\2\u01e1\u01e2")
        buf.write("\7x\2\2\u01e2\u01e3\7g\2\2\u01e3\u01e4\7t\2\2\u01e4\u01e5")
        buf.write("\7{\2\2\u01e5@\3\2\2\2\u01e6\u01e7\7h\2\2\u01e7\u01e8")
        buf.write("\7t\2\2\u01e8\u01e9\7c\2\2\u01e9\u01ea\7o\2\2\u01ea\u01eb")
        buf.write("\7g\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01ee\7u\2\2\u01ed\u01ec")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01eeB\3\2\2\2\u01ef\u01f0")
        buf.write("\7u\2\2\u01f0\u01f1\7g\2\2\u01f1\u01f2\7e\2\2\u01f2\u01fa")
        buf.write("\3\2\2\2\u01f3\u01f4\7q\2\2\u01f4\u01f5\7p\2\2\u01f5\u01f6")
        buf.write("\7f\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f9\7u\2\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa")
        buf.write("\u01f3\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fbD\3\2\2\2\u01fc")
        buf.write("\u01fd\7e\2\2\u01fd\u01fe\7c\2\2\u01fe\u01ff\7o\2\2\u01ff")
        buf.write("\u0200\7g\2\2\u0200\u0201\7t\2\2\u0201\u0202\7c\2\2\u0202")
        buf.write("F\3\2\2\2\u0203\u0204\7n\2\2\u0204\u0205\7k\2\2\u0205")
        buf.write("\u0206\7i\2\2\u0206\u0207\7j\2\2\u0207\u0208\7v\2\2\u0208")
        buf.write("H\3\2\2\2\u0209\u020a\7u\2\2\u020a\u020b\7v\2\2\u020b")
        buf.write("\u020c\7g\2\2\u020c\u020d\7t\2\2\u020d\u020e\7g\2\2\u020e")
        buf.write("\u020f\7q\2\2\u020fJ\3\2\2\2\u0210\u0211\7o\2\2\u0211")
        buf.write("\u0212\7c\2\2\u0212\u0213\7v\2\2\u0213\u0214\7g\2\2\u0214")
        buf.write("\u0215\7t\2\2\u0215\u0216\7k\2\2\u0216\u0217\7c\2\2\u0217")
        buf.write("\u0218\7n\2\2\u0218L\3\2\2\2\u0219\u021a\7v\2\2\u021a")
        buf.write("\u021b\7k\2\2\u021b\u021c\7o\2\2\u021c\u021d\7g\2\2\u021d")
        buf.write("\u021e\7n\2\2\u021e\u021f\7k\2\2\u021f\u0220\7p\2\2\u0220")
        buf.write("\u0221\7g\2\2\u0221N\3\2\2\2\u0222\u0223\5Q)\2\u0223\u0224")
        buf.write("\b(\2\2\u0224\u0225\3\2\2\2\u0225\u0226\b(\3\2\u0226P")
        buf.write("\3\2\2\2\u0227\u0228\5\u00a3R\2\u0228\u022d\5\u00a3R\2")
        buf.write("\u0229\u022c\5Q)\2\u022a\u022c\13\2\2\2\u022b\u0229\3")
        buf.write("\2\2\2\u022b\u022a\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u0230\3\2\2\2\u022f")
        buf.write("\u022d\3\2\2\2\u0230\u0231\5\u00a5S\2\u0231\u0232\5\u00a5")
        buf.write("S\2\u0232R\3\2\2\2\u0233\u0234\7c\2\2\u0234\u0235\7p\2")
        buf.write("\2\u0235\u0236\7f\2\2\u0236T\3\2\2\2\u0237\u0238\7f\2")
        buf.write("\2\u0238\u0239\7g\2\2\u0239\u023a\7h\2\2\u023aV\3\2\2")
        buf.write("\2\u023b\u023c\7g\2\2\u023c\u023d\7n\2\2\u023d\u023e\7")
        buf.write("u\2\2\u023e\u023f\7g\2\2\u023fX\3\2\2\2\u0240\u0241\7")
        buf.write("h\2\2\u0241\u0242\7c\2\2\u0242\u0243\7n\2\2\u0243\u0244")
        buf.write("\7u\2\2\u0244\u0245\7g\2\2\u0245Z\3\2\2\2\u0246\u0247")
        buf.write("\7h\2\2\u0247\u0248\7q\2\2\u0248\u0249\7t\2\2\u0249\\")
        buf.write("\3\2\2\2\u024a\u024b\7k\2\2\u024b\u024c\7h\2\2\u024c^")
        buf.write("\3\2\2\2\u024d\u024e\7k\2\2\u024e\u024f\7p\2\2\u024f`")
        buf.write("\3\2\2\2\u0250\u0251\7k\2\2\u0251\u0252\7u\2\2\u0252b")
        buf.write("\3\2\2\2\u0253\u0254\7p\2\2\u0254\u0255\7q\2\2\u0255\u0256")
        buf.write("\7p\2\2\u0256\u0257\7g\2\2\u0257d\3\2\2\2\u0258\u0259")
        buf.write("\7p\2\2\u0259\u025a\7q\2\2\u025a\u025b\7v\2\2\u025bf\3")
        buf.write("\2\2\2\u025c\u025d\7q\2\2\u025d\u025e\7t\2\2\u025eh\3")
        buf.write("\2\2\2\u025f\u0260\7t\2\2\u0260\u0261\7g\2\2\u0261\u0262")
        buf.write("\7v\2\2\u0262\u0263\7w\2\2\u0263\u0264\7t\2\2\u0264\u0265")
        buf.write("\7p\2\2\u0265j\3\2\2\2\u0266\u0267\7v\2\2\u0267\u0268")
        buf.write("\7t\2\2\u0268\u0269\7w\2\2\u0269\u026a\7g\2\2\u026al\3")
        buf.write("\2\2\2\u026b\u026c\7a\2\2\u026cn\3\2\2\2\u026d\u026e\7")
        buf.write("\60\2\2\u026ep\3\2\2\2\u026f\u0270\7\60\2\2\u0270\u0271")
        buf.write("\7\60\2\2\u0271r\3\2\2\2\u0272\u0273\7\60\2\2\u0273\u0274")
        buf.write("\7\60\2\2\u0274\u0275\7\60\2\2\u0275t\3\2\2\2\u0276\u0277")
        buf.write("\7.\2\2\u0277v\3\2\2\2\u0278\u0279\7<\2\2\u0279x\3\2\2")
        buf.write("\2\u027a\u027b\7=\2\2\u027bz\3\2\2\2\u027c\u027d\7?\2")
        buf.write("\2\u027d|\3\2\2\2\u027e\u027f\7~\2\2\u027f~\3\2\2\2\u0280")
        buf.write("\u0281\7`\2\2\u0281\u0080\3\2\2\2\u0282\u0283\7(\2\2\u0283")
        buf.write("\u0082\3\2\2\2\u0284\u0285\7\u0080\2\2\u0285\u0084\3\2")
        buf.write("\2\2\u0286\u0287\7>\2\2\u0287\u0288\7>\2\2\u0288\u0086")
        buf.write("\3\2\2\2\u0289\u028a\7@\2\2\u028a\u028b\7@\2\2\u028b\u0088")
        buf.write("\3\2\2\2\u028c\u028d\7-\2\2\u028d\u008a\3\2\2\2\u028e")
        buf.write("\u028f\7/\2\2\u028f\u008c\3\2\2\2\u0290\u0291\7\61\2\2")
        buf.write("\u0291\u008e\3\2\2\2\u0292\u0293\7,\2\2\u0293\u0090\3")
        buf.write("\2\2\2\u0294\u0295\7'\2\2\u0295\u0092\3\2\2\2\u0296\u0297")
        buf.write("\7\61\2\2\u0297\u0298\7\61\2\2\u0298\u0094\3\2\2\2\u0299")
        buf.write("\u029a\7,\2\2\u029a\u029b\7,\2\2\u029b\u0096\3\2\2\2\u029c")
        buf.write("\u029d\7B\2\2\u029d\u0098\3\2\2\2\u029e\u029f\7/\2\2\u029f")
        buf.write("\u02a0\7@\2\2\u02a0\u009a\3\2\2\2\u02a1\u02a2\7*\2\2\u02a2")
        buf.write("\u02a3\bN\4\2\u02a3\u009c\3\2\2\2\u02a4\u02a5\7+\2\2\u02a5")
        buf.write("\u02a6\bO\5\2\u02a6\u009e\3\2\2\2\u02a7\u02a8\7]\2\2\u02a8")
        buf.write("\u02a9\bP\6\2\u02a9\u00a0\3\2\2\2\u02aa\u02ab\7_\2\2\u02ab")
        buf.write("\u02ac\bQ\7\2\u02ac\u00a2\3\2\2\2\u02ad\u02ae\7}\2\2\u02ae")
        buf.write("\u02af\bR\b\2\u02af\u00a4\3\2\2\2\u02b0\u02b1\7\177\2")
        buf.write("\2\u02b1\u02b2\bS\t\2\u02b2\u00a6\3\2\2\2\u02b3\u02b4")
        buf.write("\7>\2\2\u02b4\u00a8\3\2\2\2\u02b5\u02b6\7@\2\2\u02b6\u00aa")
        buf.write("\3\2\2\2\u02b7\u02b8\7?\2\2\u02b8\u02b9\7?\2\2\u02b9\u00ac")
        buf.write("\3\2\2\2\u02ba\u02bb\7@\2\2\u02bb\u02bc\7?\2\2\u02bc\u00ae")
        buf.write("\3\2\2\2\u02bd\u02be\7>\2\2\u02be\u02bf\7?\2\2\u02bf\u00b0")
        buf.write("\3\2\2\2\u02c0\u02c1\7#\2\2\u02c1\u02c2\7?\2\2\u02c2\u00b2")
        buf.write("\3\2\2\2\u02c3\u02c4\7-\2\2\u02c4\u02c5\7?\2\2\u02c5\u00b4")
        buf.write("\3\2\2\2\u02c6\u02c7\7/\2\2\u02c7\u02c8\7?\2\2\u02c8\u00b6")
        buf.write("\3\2\2\2\u02c9\u02ca\7,\2\2\u02ca\u02cb\7?\2\2\u02cb\u00b8")
        buf.write("\3\2\2\2\u02cc\u02cd\7B\2\2\u02cd\u02ce\7?\2\2\u02ce\u00ba")
        buf.write("\3\2\2\2\u02cf\u02d0\7\61\2\2\u02d0\u02d1\7?\2\2\u02d1")
        buf.write("\u00bc\3\2\2\2\u02d2\u02d3\7'\2\2\u02d3\u02d4\7?\2\2")
        buf.write("\u02d4\u00be\3\2\2\2\u02d5\u02d6\7(\2\2\u02d6\u02d7\7")
        buf.write("?\2\2\u02d7\u00c0\3\2\2\2\u02d8\u02d9\7~\2\2\u02d9\u02da")
        buf.write("\7?\2\2\u02da\u00c2\3\2\2\2\u02db\u02dc\7`\2\2\u02dc\u02dd")
        buf.write("\7?\2\2\u02dd\u00c4\3\2\2\2\u02de\u02df\7>\2\2\u02df\u02e0")
        buf.write("\7>\2\2\u02e0\u02e1\7?\2\2\u02e1\u00c6\3\2\2\2\u02e2\u02e3")
        buf.write("\7@\2\2\u02e3\u02e4\7@\2\2\u02e4\u02e5\7?\2\2\u02e5\u00c8")
        buf.write("\3\2\2\2\u02e6\u02e7\7,\2\2\u02e7\u02e8\7,\2\2\u02e8\u02e9")
        buf.write("\7?\2\2\u02e9\u00ca\3\2\2\2\u02ea\u02eb\7\61\2\2\u02eb")
        buf.write("\u02ec\7\61\2\2\u02ec\u02ed\7?\2\2\u02ed\u00cc\3\2\2\2")
        buf.write("\u02ee\u02ef\5\u00d5k\2\u02ef\u00ce\3\2\2\2\u02f0\u02f3")
        buf.write("\5\u00d7l\2\u02f1\u02f3\5\u00e1q\2\u02f2\u02f0\3\2\2\2")
        buf.write("\u02f2\u02f1\3\2\2\2\u02f3\u00d0\3\2\2\2\u02f4\u02f8\5")
        buf.write("\u0101\u0081\2\u02f5\u02f7\5\u0103\u0082\2\u02f6\u02f5")
        buf.write("\3\2\2\2\u02f7\u02fa\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f8")
        buf.write("\u02f9\3\2\2\2\u02f9\u00d2\3\2\2\2\u02fa\u02f8\3\2\2\2")
        buf.write("\u02fb\u02fc\7&\2\2\u02fc\u02fd\5\u00d1i\2\u02fd\u00d4")
        buf.write("\3\2\2\2\u02fe\u0308\t\3\2\2\u02ff\u0301\t\4\2\2\u0300")
        buf.write("\u02ff\3\2\2\2\u0300\u0301\3\2\2\2\u0301\u0302\3\2\2\2")
        buf.write("\u0302\u0308\t\5\2\2\u0303\u0305\t\5\2\2\u0304\u0303\3")
        buf.write("\2\2\2\u0304\u0305\3\2\2\2\u0305\u0306\3\2\2\2\u0306\u0308")
        buf.write("\t\4\2\2\u0307\u02fe\3\2\2\2\u0307\u0300\3\2\2\2\u0307")
        buf.write("\u0304\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u0309\3\2\2\2")
        buf.write("\u0309\u030a\5\u00e9u\2\u030a\u00d6\3\2\2\2\u030b\u0310")
        buf.write("\5\u00d9m\2\u030c\u0310\5\u00dbn\2\u030d\u0310\5\u00dd")
        buf.write("o\2\u030e\u0310\5\u00dfp\2\u030f\u030b\3\2\2\2\u030f\u030c")
        buf.write("\3\2\2\2\u030f\u030d\3\2\2\2\u030f\u030e\3\2\2\2\u0310")
        buf.write("\u00d8\3\2\2\2\u0311\u0315\5\u00edw\2\u0312\u0314\5\u00ef")
        buf.write("x\2\u0313\u0312\3\2\2\2\u0314\u0317\3\2\2\2\u0315\u0313")
        buf.write("\3\2\2\2\u0315\u0316\3\2\2\2\u0316\u031e\3\2\2\2\u0317")
        buf.write("\u0315\3\2\2\2\u0318\u031a\7\62\2\2\u0319\u0318\3\2\2")
        buf.write("\2\u031a\u031b\3\2\2\2\u031b\u0319\3\2\2\2\u031b\u031c")
        buf.write("\3\2\2\2\u031c\u031e\3\2\2\2\u031d\u0311\3\2\2\2\u031d")
        buf.write("\u0319\3\2\2\2\u031e\u00da\3\2\2\2\u031f\u0320\7\62\2")
        buf.write("\2\u0320\u0322\t\6\2\2\u0321\u0323\5\u00f1y\2\u0322\u0321")
        buf.write("\3\2\2\2\u0323\u0324\3\2\2\2\u0324\u0322\3\2\2\2\u0324")
        buf.write("\u0325\3\2\2\2\u0325\u00dc\3\2\2\2\u0326\u0327\7\62\2")
        buf.write("\2\u0327\u0329\t\7\2\2\u0328\u032a\5\u00f3z\2\u0329\u0328")
        buf.write("\3\2\2\2\u032a\u032b\3\2\2\2\u032b\u0329\3\2\2\2\u032b")
        buf.write("\u032c\3\2\2\2\u032c\u00de\3\2\2\2\u032d\u032e\7\62\2")
        buf.write("\2\u032e\u0330\t\b\2\2\u032f\u0331\5\u00f5{\2\u0330\u032f")
        buf.write("\3\2\2\2\u0331\u0332\3\2\2\2\u0332\u0330\3\2\2\2\u0332")
        buf.write("\u0333\3\2\2\2\u0333\u00e0\3\2\2\2\u0334\u0337\5\u00f7")
        buf.write("|\2\u0335\u0337\5\u00f9}\2\u0336\u0334\3\2\2\2\u0336\u0335")
        buf.write("\3\2\2\2\u0337\u00e2\3\2\2\2\u0338\u0339\6r\2\2\u0339")
        buf.write("\u0345\5\u0107\u0084\2\u033a\u033c\7\17\2\2\u033b\u033a")
        buf.write("\3\2\2\2\u033b\u033c\3\2\2\2\u033c\u033d\3\2\2\2\u033d")
        buf.write("\u0340\7\f\2\2\u033e\u0340\4\16\17\2\u033f\u033b\3\2\2")
        buf.write("\2\u033f\u033e\3\2\2\2\u0340\u0342\3\2\2\2\u0341\u0343")
        buf.write("\5\u0107\u0084\2\u0342\u0341\3\2\2\2\u0342\u0343\3\2\2")
        buf.write("\2\u0343\u0345\3\2\2\2\u0344\u0338\3\2\2\2\u0344\u033f")
        buf.write("\3\2\2\2\u0345\u0346\3\2\2\2\u0346\u0347\br\n\2\u0347")
        buf.write("\u00e4\3\2\2\2\u0348\u034c\5\u0107\u0084\2\u0349\u034c")
        buf.write("\5\u0109\u0085\2\u034a\u034c\5\u010b\u0086\2\u034b\u0348")
        buf.write("\3\2\2\2\u034b\u0349\3\2\2\2\u034b\u034a\3\2\2\2\u034c")
        buf.write("\u034d\3\2\2\2\u034d\u034e\bs\3\2\u034e\u00e6\3\2\2\2")
        buf.write("\u034f\u0350\13\2\2\2\u0350\u00e8\3\2\2\2\u0351\u0356")
        buf.write("\7)\2\2\u0352\u0355\5\u00ebv\2\u0353\u0355\n\t\2\2\u0354")
        buf.write("\u0352\3\2\2\2\u0354\u0353\3\2\2\2\u0355\u0358\3\2\2\2")
        buf.write("\u0356\u0354\3\2\2\2\u0356\u0357\3\2\2\2\u0357\u0359\3")
        buf.write("\2\2\2\u0358\u0356\3\2\2\2\u0359\u0364\7)\2\2\u035a\u035f")
        buf.write("\7$\2\2\u035b\u035e\5\u00ebv\2\u035c\u035e\n\n\2\2\u035d")
        buf.write("\u035b\3\2\2\2\u035d\u035c\3\2\2\2\u035e\u0361\3\2\2\2")
        buf.write("\u035f\u035d\3\2\2\2\u035f\u0360\3\2\2\2\u0360\u0362\3")
        buf.write("\2\2\2\u0361\u035f\3\2\2\2\u0362\u0364\7$\2\2\u0363\u0351")
        buf.write("\3\2\2\2\u0363\u035a\3\2\2\2\u0364\u00ea\3\2\2\2\u0365")
        buf.write("\u0366\7^\2\2\u0366\u036a\13\2\2\2\u0367\u0368\7^\2\2")
        buf.write("\u0368\u036a\5\u00e3r\2\u0369\u0365\3\2\2\2\u0369\u0367")
        buf.write("\3\2\2\2\u036a\u00ec\3\2\2\2\u036b\u036c\4\63;\2\u036c")
        buf.write("\u00ee\3\2\2\2\u036d\u036e\4\62;\2\u036e\u00f0\3\2\2\2")
        buf.write("\u036f\u0370\4\629\2\u0370\u00f2\3\2\2\2\u0371\u0374\5")
        buf.write("\u00efx\2\u0372\u0374\t\13\2\2\u0373\u0371\3\2\2\2\u0373")
        buf.write("\u0372\3\2\2\2\u0374\u00f4\3\2\2\2\u0375\u0376\4\62\63")
        buf.write("\2\u0376\u00f6\3\2\2\2\u0377\u0379\5\u00fb~\2\u0378\u0377")
        buf.write("\3\2\2\2\u0378\u0379\3\2\2\2\u0379\u037a\3\2\2\2\u037a")
        buf.write("\u037f\5\u00fd\177\2\u037b\u037c\5\u00fb~\2\u037c\u037d")
        buf.write("\7\60\2\2\u037d\u037f\3\2\2\2\u037e\u0378\3\2\2\2\u037e")
        buf.write("\u037b\3\2\2\2\u037f\u00f8\3\2\2\2\u0380\u0383\5\u00fb")
        buf.write("~\2\u0381\u0383\5\u00f7|\2\u0382\u0380\3\2\2\2\u0382\u0381")
        buf.write("\3\2\2\2\u0383\u0384\3\2\2\2\u0384\u0385\5\u00ff\u0080")
        buf.write("\2\u0385\u00fa\3\2\2\2\u0386\u0388\5\u00efx\2\u0387\u0386")
        buf.write("\3\2\2\2\u0388\u0389\3\2\2\2\u0389\u0387\3\2\2\2\u0389")
        buf.write("\u038a\3\2\2\2\u038a\u00fc\3\2\2\2\u038b\u038d\7\60\2")
        buf.write("\2\u038c\u038e\5\u00efx\2\u038d\u038c\3\2\2\2\u038e\u038f")
        buf.write("\3\2\2\2\u038f\u038d\3\2\2\2\u038f\u0390\3\2\2\2\u0390")
        buf.write("\u00fe\3\2\2\2\u0391\u0393\t\f\2\2\u0392\u0394\t\r\2\2")
        buf.write("\u0393\u0392\3\2\2\2\u0393\u0394\3\2\2\2\u0394\u0396\3")
        buf.write("\2\2\2\u0395\u0397\5\u00efx\2\u0396\u0395\3\2\2\2\u0397")
        buf.write("\u0398\3\2\2\2\u0398\u0396\3\2\2\2\u0398\u0399\3\2\2\2")
        buf.write("\u0399\u0100\3\2\2\2\u039a\u039d\5m\67\2\u039b\u039d\5")
        buf.write("\u0105\u0083\2\u039c\u039a\3\2\2\2\u039c\u039b\3\2\2\2")
        buf.write("\u039d\u0102\3\2\2\2\u039e\u03a1\5\u0101\u0081\2\u039f")
        buf.write("\u03a1\5\u00efx\2\u03a0\u039e\3\2\2\2\u03a0\u039f\3\2")
        buf.write("\2\2\u03a1\u0104\3\2\2\2\u03a2\u03a3\t\16\2\2\u03a3\u0106")
        buf.write("\3\2\2\2\u03a4\u03a6\t\17\2\2\u03a5\u03a4\3\2\2\2\u03a6")
        buf.write("\u03a7\3\2\2\2\u03a7\u03a5\3\2\2\2\u03a7\u03a8\3\2\2\2")
        buf.write("\u03a8\u0108\3\2\2\2\u03a9\u03ad\7%\2\2\u03aa\u03ac\n")
        buf.write("\20\2\2\u03ab\u03aa\3\2\2\2\u03ac\u03af\3\2\2\2\u03ad")
        buf.write("\u03ab\3\2\2\2\u03ad\u03ae\3\2\2\2\u03ae\u010a\3\2\2\2")
        buf.write("\u03af\u03ad\3\2\2\2\u03b0\u03b2\7^\2\2\u03b1\u03b3\5")
        buf.write("\u0107\u0084\2\u03b2\u03b1\3\2\2\2\u03b2\u03b3\3\2\2\2")
        buf.write("\u03b3\u03b9\3\2\2\2\u03b4\u03b6\7\17\2\2\u03b5\u03b4")
        buf.write("\3\2\2\2\u03b5\u03b6\3\2\2\2\u03b6\u03b7\3\2\2\2\u03b7")
        buf.write("\u03ba\7\f\2\2\u03b8\u03ba\4\16\17\2\u03b9\u03b5\3\2\2")
        buf.write("\2\u03b9\u03b8\3\2\2\2\u03ba\u010c\3\2\2\2\61\2\u017e")
        buf.write("\u01c6\u01ed\u01f8\u01fa\u022b\u022d\u02f2\u02f8\u0300")
        buf.write("\u0304\u0307\u030f\u0315\u031b\u031d\u0324\u032b\u0332")
        buf.write("\u0336\u033b\u033f\u0342\u0344\u034b\u0354\u0356\u035d")
        buf.write("\u035f\u0363\u0369\u0373\u0378\u037e\u0382\u0389\u038f")
        buf.write("\u0393\u0398\u039c\u03a0\u03a7\u03ad\u03b2\u03b5\u03b9")
        buf.write("\13\3(\2\b\2\2\3N\3\3O\4\3P\5\3Q\6\3R\7\3S\b\3r\t")
        return buf.getvalue()


class YarcLexer(YarcLexerBase):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = [
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
        "'set'",
        "'translate'",
        "'rotate'",
        "'scale'",
        "'semantics'",
        "'visible'",
        "'size'",
        "'look_at'",
        "'scatter'",
        "'around'",
        "'texture'",
        "'to'",
        "'on'",
        "'up'",
        "'every'",
        "'camera'",
        "'light'",
        "'stereo'",
        "'material'",
        "'timeline'",
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

    ruleNames = [
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
        "NESTED_CODE",
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
        "ID_START",
        "ID_CONTINUE",
        "LETTER",
        "SPACES",
        "COMMENT",
        "LINE_JOINING",
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
            actions[38] = self.SNIPPET_action
            actions[76] = self.LPAREN_action
            actions[77] = self.RPAREN_action
            actions[78] = self.LBRACK_action
            actions[79] = self.RBRACK_action
            actions[80] = self.LBRACE_action
            actions[81] = self.RBRACE_action
            actions[112] = self.NEWLINE_action
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def SNIPPET_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 0:
            print("FOUND SNIPPET CODE!")

    def LPAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 1:
            self.openBrace()

    def RPAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 2:
            self.closeBrace()

    def LBRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 3:
            self.openBrace()

    def RBRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 4:
            self.closeBrace()

    def LBRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 5:
            self.openBrace()

    def RBRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 6:
            self.closeBrace()

    def NEWLINE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 7:
            self.onNewLine()

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates is None:
            preds = dict()
            preds[112] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx: RuleContext, predIndex: int):
        if predIndex == 0:
            return self.atStartOfInput()
