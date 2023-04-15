# Generated from c:\Users\feder\Desktop\University\Magistrale\Secondo_Anno\1_Linguaggi\Progetto\yarc\yarc\dsl\v4\YarcLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2k")
        buf.write("\u0363\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0170\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u01a3\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u01b2\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u01bd\n\32\5\32\u01bf\n\32\3\33\3\33\3\33")
        buf.write("\7\33\u01c4\n\33\f\33\16\33\u01c7\13\33\5\33\u01c9\n\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)")
        buf.write("\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>")
        buf.write("\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3")
        buf.write("E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3K\3K\3")
        buf.write("L\3L\3L\3M\3M\3M\3N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3")
        buf.write("R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3W\3")
        buf.write("X\3X\3X\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3[\3[\3[\3[\3\\\3\\\3")
        buf.write("\\\3\\\3]\3]\3^\3^\5^\u029e\n^\3_\3_\7_\u02a2\n_\f_\16")
        buf.write("_\u02a5\13_\3`\3`\5`\u02a9\n`\3`\3`\5`\u02ad\n`\3`\5`")
        buf.write("\u02b0\n`\3`\3`\3a\3a\3a\3a\5a\u02b8\na\3b\3b\7b\u02bc")
        buf.write("\nb\fb\16b\u02bf\13b\3b\6b\u02c2\nb\rb\16b\u02c3\5b\u02c6")
        buf.write("\nb\3c\3c\3c\6c\u02cb\nc\rc\16c\u02cc\3d\3d\3d\6d\u02d2")
        buf.write("\nd\rd\16d\u02d3\3e\3e\3e\6e\u02d9\ne\re\16e\u02da\3f")
        buf.write("\3f\5f\u02df\nf\3g\3g\3g\5g\u02e4\ng\3g\3g\5g\u02e8\n")
        buf.write("g\3g\5g\u02eb\ng\5g\u02ed\ng\3g\3g\3h\3h\3h\5h\u02f4\n")
        buf.write("h\3h\3h\3i\3i\3j\3j\3j\7j\u02fd\nj\fj\16j\u0300\13j\3")
        buf.write("j\3j\3j\3j\7j\u0306\nj\fj\16j\u0309\13j\3j\5j\u030c\n")
        buf.write("j\3k\3k\3k\3k\5k\u0312\nk\3l\3l\3m\3m\3n\3n\3o\3o\5o\u031c")
        buf.write("\no\3p\3p\3q\5q\u0321\nq\3q\3q\3q\3q\5q\u0327\nq\3r\3")
        buf.write("r\5r\u032b\nr\3r\3r\3s\6s\u0330\ns\rs\16s\u0331\3t\3t")
        buf.write("\6t\u0336\nt\rt\16t\u0337\3u\3u\5u\u033c\nu\3u\6u\u033f")
        buf.write("\nu\ru\16u\u0340\3v\3v\5v\u0345\nv\3w\3w\5w\u0349\nw\3")
        buf.write("x\3x\3y\6y\u034e\ny\ry\16y\u034f\3z\3z\7z\u0354\nz\fz")
        buf.write("\16z\u0357\13z\3{\3{\5{\u035b\n{\3{\5{\u035e\n{\3{\3{")
        buf.write("\5{\u0362\n{\3\u01c5\2|\3\5\5\6\7\7\t\b\13\t\r\n\17\13")
        buf.write("\21\f\23\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25")
        buf.write("%\26\'\27)\30+\31-\32/\33\61\34\63\35\65\2\67\369\37;")
        buf.write(" =!?\"A#C$E%G&I\'K(M)O*Q+S,U-W.Y/[\60]\61_\62a\63c\64")
        buf.write("e\65g\66i\67k8m9o:q;s<u=w>y?{@}A\177B\u0081C\u0083D\u0085")
        buf.write("E\u0087F\u0089G\u008bH\u008dI\u008fJ\u0091K\u0093L\u0095")
        buf.write("M\u0097N\u0099O\u009bP\u009dQ\u009fR\u00a1S\u00a3T\u00a5")
        buf.write("U\u00a7V\u00a9W\u00abX\u00adY\u00afZ\u00b1[\u00b3\\\u00b5")
        buf.write("]\u00b7^\u00b9_\u00bb`\u00bda\u00bfb\u00c1c\u00c3d\u00c5")
        buf.write("e\u00c7f\u00c9g\u00cbh\u00cdi\u00cfj\u00d1k\u00d3\2\u00d5")
        buf.write("\2\u00d7\2\u00d9\2\u00db\2\u00dd\2\u00df\2\u00e1\2\u00e3")
        buf.write("\2\u00e5\2\u00e7\2\u00e9\2\u00eb\2\u00ed\2\u00ef\2\u00f1")
        buf.write("\2\u00f3\2\u00f5\2\3\2\20\4\2WWww\4\2HHhh\4\2TTtt\4\2")
        buf.write("QQqq\4\2ZZzz\4\2DDdd\6\2\f\f\16\17))^^\6\2\f\f\16\17$")
        buf.write("$^^\4\2CHch\4\2GGgg\4\2--//\4\2C\\c|\4\2\13\13\"\"\4\2")
        buf.write("\f\f\16\17\2\u0383\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1")
        buf.write("\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2")
        buf.write("\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf")
        buf.write("\3\2\2\2\2\u00d1\3\2\2\2\3\u00f7\3\2\2\2\5\u0100\3\2\2")
        buf.write("\2\7\u010b\3\2\2\2\t\u0112\3\2\2\2\13\u0114\3\2\2\2\r")
        buf.write("\u011e\3\2\2\2\17\u0127\3\2\2\2\21\u0130\3\2\2\2\23\u013b")
        buf.write("\3\2\2\2\25\u0148\3\2\2\2\27\u014f\3\2\2\2\31\u015b\3")
        buf.write("\2\2\2\33\u015f\3\2\2\2\35\u0161\3\2\2\2\37\u0163\3\2")
        buf.write("\2\2!\u016f\3\2\2\2#\u0171\3\2\2\2%\u0175\3\2\2\2\'\u017f")
        buf.write("\3\2\2\2)\u0186\3\2\2\2+\u018c\3\2\2\2-\u0196\3\2\2\2")
        buf.write("/\u01a4\3\2\2\2\61\u01aa\3\2\2\2\63\u01b3\3\2\2\2\65\u01c0")
        buf.write("\3\2\2\2\67\u01cc\3\2\2\29\u01d0\3\2\2\2;\u01d3\3\2\2")
        buf.write("\2=\u01d7\3\2\2\2?\u01dc\3\2\2\2A\u01e1\3\2\2\2C\u01e7")
        buf.write("\3\2\2\2E\u01eb\3\2\2\2G\u01ee\3\2\2\2I\u01f1\3\2\2\2")
        buf.write("K\u01f4\3\2\2\2M\u01f9\3\2\2\2O\u01fd\3\2\2\2Q\u0200\3")
        buf.write("\2\2\2S\u0205\3\2\2\2U\u020c\3\2\2\2W\u0211\3\2\2\2Y\u0213")
        buf.write("\3\2\2\2[\u0218\3\2\2\2]\u021a\3\2\2\2_\u021d\3\2\2\2")
        buf.write("a\u0221\3\2\2\2c\u0223\3\2\2\2e\u0225\3\2\2\2g\u0227\3")
        buf.write("\2\2\2i\u0229\3\2\2\2k\u022b\3\2\2\2m\u022d\3\2\2\2o\u022f")
        buf.write("\3\2\2\2q\u0231\3\2\2\2s\u0234\3\2\2\2u\u0237\3\2\2\2")
        buf.write("w\u0239\3\2\2\2y\u023b\3\2\2\2{\u023d\3\2\2\2}\u023f\3")
        buf.write("\2\2\2\177\u0241\3\2\2\2\u0081\u0244\3\2\2\2\u0083\u0247")
        buf.write("\3\2\2\2\u0085\u0249\3\2\2\2\u0087\u024c\3\2\2\2\u0089")
        buf.write("\u024f\3\2\2\2\u008b\u0252\3\2\2\2\u008d\u0255\3\2\2\2")
        buf.write("\u008f\u0258\3\2\2\2\u0091\u025b\3\2\2\2\u0093\u025e\3")
        buf.write("\2\2\2\u0095\u0260\3\2\2\2\u0097\u0262\3\2\2\2\u0099\u0265")
        buf.write("\3\2\2\2\u009b\u0268\3\2\2\2\u009d\u026b\3\2\2\2\u009f")
        buf.write("\u026e\3\2\2\2\u00a1\u0271\3\2\2\2\u00a3\u0274\3\2\2\2")
        buf.write("\u00a5\u0277\3\2\2\2\u00a7\u027a\3\2\2\2\u00a9\u027d\3")
        buf.write("\2\2\2\u00ab\u0280\3\2\2\2\u00ad\u0283\3\2\2\2\u00af\u0286")
        buf.write("\3\2\2\2\u00b1\u0289\3\2\2\2\u00b3\u028d\3\2\2\2\u00b5")
        buf.write("\u0291\3\2\2\2\u00b7\u0295\3\2\2\2\u00b9\u0299\3\2\2\2")
        buf.write("\u00bb\u029d\3\2\2\2\u00bd\u029f\3\2\2\2\u00bf\u02af\3")
        buf.write("\2\2\2\u00c1\u02b7\3\2\2\2\u00c3\u02c5\3\2\2\2\u00c5\u02c7")
        buf.write("\3\2\2\2\u00c7\u02ce\3\2\2\2\u00c9\u02d5\3\2\2\2\u00cb")
        buf.write("\u02de\3\2\2\2\u00cd\u02ec\3\2\2\2\u00cf\u02f3\3\2\2\2")
        buf.write("\u00d1\u02f7\3\2\2\2\u00d3\u030b\3\2\2\2\u00d5\u0311\3")
        buf.write("\2\2\2\u00d7\u0313\3\2\2\2\u00d9\u0315\3\2\2\2\u00db\u0317")
        buf.write("\3\2\2\2\u00dd\u031b\3\2\2\2\u00df\u031d\3\2\2\2\u00e1")
        buf.write("\u0326\3\2\2\2\u00e3\u032a\3\2\2\2\u00e5\u032f\3\2\2\2")
        buf.write("\u00e7\u0333\3\2\2\2\u00e9\u0339\3\2\2\2\u00eb\u0344\3")
        buf.write("\2\2\2\u00ed\u0348\3\2\2\2\u00ef\u034a\3\2\2\2\u00f1\u034d")
        buf.write("\3\2\2\2\u00f3\u0351\3\2\2\2\u00f5\u0358\3\2\2\2\u00f7")
        buf.write("\u00f8\7u\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa\7g\2\2\u00fa")
        buf.write("\u00fb\7p\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\u00fe\7k\2\2\u00fe\u00ff\7q\2\2\u00ff\4\3\2\2\2\u0100")
        buf.write("\u0101\7u\2\2\u0101\u0102\7g\2\2\u0102\u0103\7v\2\2\u0103")
        buf.write("\u0104\7v\2\2\u0104\u0105\7k\2\2\u0105\u0106\7p\2\2\u0106")
        buf.write("\u0107\7i\2\2\u0107\u0108\7u\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\u010a\5c\62\2\u010a\6\3\2\2\2\u010b\u010c\7y\2\2\u010c")
        buf.write("\u010d\7t\2\2\u010d\u010e\7k\2\2\u010e\u010f\7v\2\2\u010f")
        buf.write("\u0110\7g\2\2\u0110\u0111\7t\2\2\u0111\b\3\2\2\2\u0112")
        buf.write("\u0113\5\65\33\2\u0113\n\3\2\2\2\u0114\u0115\7W\2\2\u0115")
        buf.write("\u0116\7p\2\2\u0116\u0117\7k\2\2\u0117\u0118\7h\2\2\u0118")
        buf.write("\u0119\7q\2\2\u0119\u011a\7t\2\2\u011a\u011b\7o\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\5\u0087D\2\u011d\f\3\2\2\2")
        buf.write("\u011e\u011f\7P\2\2\u011f\u0120\7q\2\2\u0120\u0121\7t")
        buf.write("\2\2\u0121\u0122\7o\2\2\u0122\u0123\7c\2\2\u0123\u0124")
        buf.write("\7n\2\2\u0124\u0125\3\2\2\2\u0125\u0126\5\u0087D\2\u0126")
        buf.write("\16\3\2\2\2\u0127\u0128\7E\2\2\u0128\u0129\7j\2\2\u0129")
        buf.write("\u012a\7q\2\2\u012a\u012b\7k\2\2\u012b\u012c\7e\2\2\u012c")
        buf.write("\u012d\7g\2\2\u012d\u012e\3\2\2\2\u012e\u012f\5\u0087")
        buf.write("D\2\u012f\20\3\2\2\2\u0130\u0131\7U\2\2\u0131\u0132\7")
        buf.write("g\2\2\u0132\u0133\7s\2\2\u0133\u0134\7w\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135\u0136\7p\2\2\u0136\u0137\7e\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138\u0139\3\2\2\2\u0139\u013a\5\u0087D\2\u013a")
        buf.write("\22\3\2\2\2\u013b\u013c\7N\2\2\u013c\u013d\7q\2\2\u013d")
        buf.write("\u013e\7i\2\2\u013e\u013f\7W\2\2\u013f\u0140\7p\2\2\u0140")
        buf.write("\u0141\7k\2\2\u0141\u0142\7h\2\2\u0142\u0143\7q\2\2\u0143")
        buf.write("\u0144\7t\2\2\u0144\u0145\7o\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0147\5\u0087D\2\u0147\24\3\2\2\2\u0148\u0149\7e\2\2")
        buf.write("\u0149\u014a\7t\2\2\u014a\u014b\7g\2\2\u014b\u014c\7c")
        buf.write("\2\2\u014c\u014d\7v\2\2\u014d\u014e\7g\2\2\u014e\26\3")
        buf.write("\2\2\2\u014f\u0150\7k\2\2\u0150\u0151\7p\2\2\u0151\u0152")
        buf.write("\7u\2\2\u0152\u0153\7v\2\2\u0153\u0154\7c\2\2\u0154\u0155")
        buf.write("\7p\2\2\u0155\u0156\7v\2\2\u0156\u0157\7k\2\2\u0157\u0158")
        buf.write("\7c\2\2\u0158\u0159\7v\2\2\u0159\u015a\7g\2\2\u015a\30")
        buf.write("\3\2\2\2\u015b\u015c\7i\2\2\u015c\u015d\7g\2\2\u015d\u015e")
        buf.write("\7v\2\2\u015e\32\3\2\2\2\u015f\u0160\7z\2\2\u0160\34\3")
        buf.write("\2\2\2\u0161\u0162\7{\2\2\u0162\36\3\2\2\2\u0163\u0164")
        buf.write("\7|\2\2\u0164 \3\2\2\2\u0165\u0166\7g\2\2\u0166\u0167")
        buf.write("\7f\2\2\u0167\u0168\7k\2\2\u0168\u0170\7v\2\2\u0169\u016a")
        buf.write("\7o\2\2\u016a\u016b\7q\2\2\u016b\u016c\7f\2\2\u016c\u016d")
        buf.write("\7k\2\2\u016d\u016e\7h\2\2\u016e\u0170\7{\2\2\u016f\u0165")
        buf.write("\3\2\2\2\u016f\u0169\3\2\2\2\u0170\"\3\2\2\2\u0171\u0172")
        buf.write("\7u\2\2\u0172\u0173\7g\2\2\u0173\u0174\7v\2\2\u0174$\3")
        buf.write("\2\2\2\u0175\u0176\7v\2\2\u0176\u0177\7t\2\2\u0177\u0178")
        buf.write("\7c\2\2\u0178\u0179\7p\2\2\u0179\u017a\7u\2\2\u017a\u017b")
        buf.write("\7n\2\2\u017b\u017c\7c\2\2\u017c\u017d\7v\2\2\u017d\u017e")
        buf.write("\7g\2\2\u017e&\3\2\2\2\u017f\u0180\7t\2\2\u0180\u0181")
        buf.write("\7q\2\2\u0181\u0182\7v\2\2\u0182\u0183\7c\2\2\u0183\u0184")
        buf.write("\7v\2\2\u0184\u0185\7g\2\2\u0185(\3\2\2\2\u0186\u0187")
        buf.write("\7u\2\2\u0187\u0188\7e\2\2\u0188\u0189\7c\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018a\u018b\7g\2\2\u018b*\3\2\2\2\u018c\u018d")
        buf.write("\7u\2\2\u018d\u018e\7g\2\2\u018e\u018f\7o\2\2\u018f\u0190")
        buf.write("\7c\2\2\u0190\u0191\7p\2\2\u0191\u0192\7v\2\2\u0192\u0193")
        buf.write("\7k\2\2\u0193\u0194\7e\2\2\u0194\u0195\7u\2\2\u0195,\3")
        buf.write("\2\2\2\u0196\u0197\7u\2\2\u0197\u0198\7e\2\2\u0198\u0199")
        buf.write("\7c\2\2\u0199\u019a\7v\2\2\u019a\u019b\7v\2\2\u019b\u019c")
        buf.write("\7g\2\2\u019c\u019d\7t\2\2\u019d\u01a2\3\2\2\2\u019e\u019f")
        buf.write("\7\64\2\2\u019f\u01a3\7f\2\2\u01a0\u01a1\7\65\2\2\u01a1")
        buf.write("\u01a3\7f\2\2\u01a2\u019e\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3.\3\2\2\2\u01a4\u01a5\7g\2\2")
        buf.write("\u01a5\u01a6\7x\2\2\u01a6\u01a7\7g\2\2\u01a7\u01a8\7t")
        buf.write("\2\2\u01a8\u01a9\7{\2\2\u01a9\60\3\2\2\2\u01aa\u01ab\7")
        buf.write("h\2\2\u01ab\u01ac\7t\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae")
        buf.write("\7o\2\2\u01ae\u01af\7g\2\2\u01af\u01b1\3\2\2\2\u01b0\u01b2")
        buf.write("\7u\2\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\62\3\2\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5\7g\2\2\u01b5")
        buf.write("\u01b6\7e\2\2\u01b6\u01be\3\2\2\2\u01b7\u01b8\7q\2\2\u01b8")
        buf.write("\u01b9\7p\2\2\u01b9\u01ba\7f\2\2\u01ba\u01bc\3\2\2\2\u01bb")
        buf.write("\u01bd\7u\2\2\u01bc\u01bb\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01bf\3\2\2\2\u01be\u01b7\3\2\2\2\u01be\u01bf\3")
        buf.write("\2\2\2\u01bf\64\3\2\2\2\u01c0\u01c8\5\u008fH\2\u01c1\u01c9")
        buf.write("\5\65\33\2\u01c2\u01c4\13\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c1\3")
        buf.write("\2\2\2\u01c8\u01c5\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write("\5\u0091I\2\u01cb\66\3\2\2\2\u01cc\u01cd\7c\2\2\u01cd")
        buf.write("\u01ce\7p\2\2\u01ce\u01cf\7f\2\2\u01cf8\3\2\2\2\u01d0")
        buf.write("\u01d1\7c\2\2\u01d1\u01d2\7u\2\2\u01d2:\3\2\2\2\u01d3")
        buf.write("\u01d4\7f\2\2\u01d4\u01d5\7g\2\2\u01d5\u01d6\7h\2\2\u01d6")
        buf.write("<\3\2\2\2\u01d7\u01d8\7g\2\2\u01d8\u01d9\7n\2\2\u01d9")
        buf.write("\u01da\7k\2\2\u01da\u01db\7h\2\2\u01db>\3\2\2\2\u01dc")
        buf.write("\u01dd\7g\2\2\u01dd\u01de\7n\2\2\u01de\u01df\7u\2\2\u01df")
        buf.write("\u01e0\7g\2\2\u01e0@\3\2\2\2\u01e1\u01e2\7H\2\2\u01e2")
        buf.write("\u01e3\7c\2\2\u01e3\u01e4\7n\2\2\u01e4\u01e5\7u\2\2\u01e5")
        buf.write("\u01e6\7g\2\2\u01e6B\3\2\2\2\u01e7\u01e8\7h\2\2\u01e8")
        buf.write("\u01e9\7q\2\2\u01e9\u01ea\7t\2\2\u01eaD\3\2\2\2\u01eb")
        buf.write("\u01ec\7k\2\2\u01ec\u01ed\7h\2\2\u01edF\3\2\2\2\u01ee")
        buf.write("\u01ef\7k\2\2\u01ef\u01f0\7p\2\2\u01f0H\3\2\2\2\u01f1")
        buf.write("\u01f2\7k\2\2\u01f2\u01f3\7u\2\2\u01f3J\3\2\2\2\u01f4")
        buf.write("\u01f5\7P\2\2\u01f5\u01f6\7q\2\2\u01f6\u01f7\7p\2\2\u01f7")
        buf.write("\u01f8\7g\2\2\u01f8L\3\2\2\2\u01f9\u01fa\7p\2\2\u01fa")
        buf.write("\u01fb\7q\2\2\u01fb\u01fc\7v\2\2\u01fcN\3\2\2\2\u01fd")
        buf.write("\u01fe\7q\2\2\u01fe\u01ff\7t\2\2\u01ffP\3\2\2\2\u0200")
        buf.write("\u0201\7r\2\2\u0201\u0202\7c\2\2\u0202\u0203\7u\2\2\u0203")
        buf.write("\u0204\7u\2\2\u0204R\3\2\2\2\u0205\u0206\7t\2\2\u0206")
        buf.write("\u0207\7g\2\2\u0207\u0208\7v\2\2\u0208\u0209\7w\2\2\u0209")
        buf.write("\u020a\7t\2\2\u020a\u020b\7p\2\2\u020bT\3\2\2\2\u020c")
        buf.write("\u020d\7V\2\2\u020d\u020e\7t\2\2\u020e\u020f\7w\2\2\u020f")
        buf.write("\u0210\7g\2\2\u0210V\3\2\2\2\u0211\u0212\7a\2\2\u0212")
        buf.write("X\3\2\2\2\u0213\u0214\7y\2\2\u0214\u0215\7k\2\2\u0215")
        buf.write("\u0216\7v\2\2\u0216\u0217\7j\2\2\u0217Z\3\2\2\2\u0218")
        buf.write("\u0219\7\60\2\2\u0219\\\3\2\2\2\u021a\u021b\7\60\2\2\u021b")
        buf.write("\u021c\7\60\2\2\u021c^\3\2\2\2\u021d\u021e\7\60\2\2\u021e")
        buf.write("\u021f\7\60\2\2\u021f\u0220\7\60\2\2\u0220`\3\2\2\2\u0221")
        buf.write("\u0222\7.\2\2\u0222b\3\2\2\2\u0223\u0224\7<\2\2\u0224")
        buf.write("d\3\2\2\2\u0225\u0226\7=\2\2\u0226f\3\2\2\2\u0227\u0228")
        buf.write("\7?\2\2\u0228h\3\2\2\2\u0229\u022a\7~\2\2\u022aj\3\2\2")
        buf.write("\2\u022b\u022c\7`\2\2\u022cl\3\2\2\2\u022d\u022e\7(\2")
        buf.write("\2\u022en\3\2\2\2\u022f\u0230\7\u0080\2\2\u0230p\3\2\2")
        buf.write("\2\u0231\u0232\7>\2\2\u0232\u0233\7>\2\2\u0233r\3\2\2")
        buf.write("\2\u0234\u0235\7@\2\2\u0235\u0236\7@\2\2\u0236t\3\2\2")
        buf.write("\2\u0237\u0238\7-\2\2\u0238v\3\2\2\2\u0239\u023a\7/\2")
        buf.write("\2\u023ax\3\2\2\2\u023b\u023c\7\61\2\2\u023cz\3\2\2\2")
        buf.write("\u023d\u023e\7,\2\2\u023e|\3\2\2\2\u023f\u0240\7\'\2\2")
        buf.write("\u0240~\3\2\2\2\u0241\u0242\7\61\2\2\u0242\u0243\7\61")
        buf.write("\2\2\u0243\u0080\3\2\2\2\u0244\u0245\7,\2\2\u0245\u0246")
        buf.write("\7,\2\2\u0246\u0082\3\2\2\2\u0247\u0248\7B\2\2\u0248\u0084")
        buf.write("\3\2\2\2\u0249\u024a\7/\2\2\u024a\u024b\7@\2\2\u024b\u0086")
        buf.write("\3\2\2\2\u024c\u024d\7*\2\2\u024d\u024e\bD\2\2\u024e\u0088")
        buf.write("\3\2\2\2\u024f\u0250\7+\2\2\u0250\u0251\bE\3\2\u0251\u008a")
        buf.write("\3\2\2\2\u0252\u0253\7]\2\2\u0253\u0254\bF\4\2\u0254\u008c")
        buf.write("\3\2\2\2\u0255\u0256\7_\2\2\u0256\u0257\bG\5\2\u0257\u008e")
        buf.write("\3\2\2\2\u0258\u0259\7}\2\2\u0259\u025a\bH\6\2\u025a\u0090")
        buf.write("\3\2\2\2\u025b\u025c\7\177\2\2\u025c\u025d\bI\7\2\u025d")
        buf.write("\u0092\3\2\2\2\u025e\u025f\7>\2\2\u025f\u0094\3\2\2\2")
        buf.write("\u0260\u0261\7@\2\2\u0261\u0096\3\2\2\2\u0262\u0263\7")
        buf.write("?\2\2\u0263\u0264\7?\2\2\u0264\u0098\3\2\2\2\u0265\u0266")
        buf.write("\7@\2\2\u0266\u0267\7?\2\2\u0267\u009a\3\2\2\2\u0268\u0269")
        buf.write("\7>\2\2\u0269\u026a\7?\2\2\u026a\u009c\3\2\2\2\u026b\u026c")
        buf.write("\7#\2\2\u026c\u026d\7?\2\2\u026d\u009e\3\2\2\2\u026e\u026f")
        buf.write("\7-\2\2\u026f\u0270\7?\2\2\u0270\u00a0\3\2\2\2\u0271\u0272")
        buf.write("\7/\2\2\u0272\u0273\7?\2\2\u0273\u00a2\3\2\2\2\u0274\u0275")
        buf.write("\7,\2\2\u0275\u0276\7?\2\2\u0276\u00a4\3\2\2\2\u0277\u0278")
        buf.write("\7B\2\2\u0278\u0279\7?\2\2\u0279\u00a6\3\2\2\2\u027a\u027b")
        buf.write("\7\61\2\2\u027b\u027c\7?\2\2\u027c\u00a8\3\2\2\2\u027d")
        buf.write("\u027e\7\'\2\2\u027e\u027f\7?\2\2\u027f\u00aa\3\2\2\2")
        buf.write("\u0280\u0281\7(\2\2\u0281\u0282\7?\2\2\u0282\u00ac\3\2")
        buf.write("\2\2\u0283\u0284\7~\2\2\u0284\u0285\7?\2\2\u0285\u00ae")
        buf.write("\3\2\2\2\u0286\u0287\7`\2\2\u0287\u0288\7?\2\2\u0288\u00b0")
        buf.write("\3\2\2\2\u0289\u028a\7>\2\2\u028a\u028b\7>\2\2\u028b\u028c")
        buf.write("\7?\2\2\u028c\u00b2\3\2\2\2\u028d\u028e\7@\2\2\u028e\u028f")
        buf.write("\7@\2\2\u028f\u0290\7?\2\2\u0290\u00b4\3\2\2\2\u0291\u0292")
        buf.write("\7,\2\2\u0292\u0293\7,\2\2\u0293\u0294\7?\2\2\u0294\u00b6")
        buf.write("\3\2\2\2\u0295\u0296\7\61\2\2\u0296\u0297\7\61\2\2\u0297")
        buf.write("\u0298\7?\2\2\u0298\u00b8\3\2\2\2\u0299\u029a\5\u00bf")
        buf.write("`\2\u029a\u00ba\3\2\2\2\u029b\u029e\5\u00c1a\2\u029c\u029e")
        buf.write("\5\u00cbf\2\u029d\u029b\3\2\2\2\u029d\u029c\3\2\2\2\u029e")
        buf.write("\u00bc\3\2\2\2\u029f\u02a3\5\u00ebv\2\u02a0\u02a2\5\u00ed")
        buf.write("w\2\u02a1\u02a0\3\2\2\2\u02a2\u02a5\3\2\2\2\u02a3\u02a1")
        buf.write("\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u00be\3\2\2\2\u02a5")
        buf.write("\u02a3\3\2\2\2\u02a6\u02b0\t\2\2\2\u02a7\u02a9\t\3\2\2")
        buf.write("\u02a8\u02a7\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02aa\3")
        buf.write("\2\2\2\u02aa\u02b0\t\4\2\2\u02ab\u02ad\t\4\2\2\u02ac\u02ab")
        buf.write("\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae")
        buf.write("\u02b0\t\3\2\2\u02af\u02a6\3\2\2\2\u02af\u02a8\3\2\2\2")
        buf.write("\u02af\u02ac\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0\u02b1\3")
        buf.write("\2\2\2\u02b1\u02b2\5\u00d3j\2\u02b2\u00c0\3\2\2\2\u02b3")
        buf.write("\u02b8\5\u00c3b\2\u02b4\u02b8\5\u00c5c\2\u02b5\u02b8\5")
        buf.write("\u00c7d\2\u02b6\u02b8\5\u00c9e\2\u02b7\u02b3\3\2\2\2\u02b7")
        buf.write("\u02b4\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b7\u02b6\3\2\2\2")
        buf.write("\u02b8\u00c2\3\2\2\2\u02b9\u02bd\5\u00d7l\2\u02ba\u02bc")
        buf.write("\5\u00d9m\2\u02bb\u02ba\3\2\2\2\u02bc\u02bf\3\2\2\2\u02bd")
        buf.write("\u02bb\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02c6\3\2\2\2")
        buf.write("\u02bf\u02bd\3\2\2\2\u02c0\u02c2\7\62\2\2\u02c1\u02c0")
        buf.write("\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3")
        buf.write("\u02c4\3\2\2\2\u02c4\u02c6\3\2\2\2\u02c5\u02b9\3\2\2\2")
        buf.write("\u02c5\u02c1\3\2\2\2\u02c6\u00c4\3\2\2\2\u02c7\u02c8\7")
        buf.write("\62\2\2\u02c8\u02ca\t\5\2\2\u02c9\u02cb\5\u00dbn\2\u02ca")
        buf.write("\u02c9\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u02ca\3\2\2\2")
        buf.write("\u02cc\u02cd\3\2\2\2\u02cd\u00c6\3\2\2\2\u02ce\u02cf\7")
        buf.write("\62\2\2\u02cf\u02d1\t\6\2\2\u02d0\u02d2\5\u00ddo\2\u02d1")
        buf.write("\u02d0\3\2\2\2\u02d2\u02d3\3\2\2\2\u02d3\u02d1\3\2\2\2")
        buf.write("\u02d3\u02d4\3\2\2\2\u02d4\u00c8\3\2\2\2\u02d5\u02d6\7")
        buf.write("\62\2\2\u02d6\u02d8\t\7\2\2\u02d7\u02d9\5\u00dfp\2\u02d8")
        buf.write("\u02d7\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u02d8\3\2\2\2")
        buf.write("\u02da\u02db\3\2\2\2\u02db\u00ca\3\2\2\2\u02dc\u02df\5")
        buf.write("\u00e1q\2\u02dd\u02df\5\u00e3r\2\u02de\u02dc\3\2\2\2\u02de")
        buf.write("\u02dd\3\2\2\2\u02df\u00cc\3\2\2\2\u02e0\u02e1\6g\2\2")
        buf.write("\u02e1\u02ed\5\u00f1y\2\u02e2\u02e4\7\17\2\2\u02e3\u02e2")
        buf.write("\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5")
        buf.write("\u02e8\7\f\2\2\u02e6\u02e8\4\16\17\2\u02e7\u02e3\3\2\2")
        buf.write("\2\u02e7\u02e6\3\2\2\2\u02e8\u02ea\3\2\2\2\u02e9\u02eb")
        buf.write("\5\u00f1y\2\u02ea\u02e9\3\2\2\2\u02ea\u02eb\3\2\2\2\u02eb")
        buf.write("\u02ed\3\2\2\2\u02ec\u02e0\3\2\2\2\u02ec\u02e7\3\2\2\2")
        buf.write("\u02ed\u02ee\3\2\2\2\u02ee\u02ef\bg\b\2\u02ef\u00ce\3")
        buf.write("\2\2\2\u02f0\u02f4\5\u00f1y\2\u02f1\u02f4\5\u00f3z\2\u02f2")
        buf.write("\u02f4\5\u00f5{\2\u02f3\u02f0\3\2\2\2\u02f3\u02f1\3\2")
        buf.write("\2\2\u02f3\u02f2\3\2\2\2\u02f4\u02f5\3\2\2\2\u02f5\u02f6")
        buf.write("\bh\t\2\u02f6\u00d0\3\2\2\2\u02f7\u02f8\13\2\2\2\u02f8")
        buf.write("\u00d2\3\2\2\2\u02f9\u02fe\7)\2\2\u02fa\u02fd\5\u00d5")
        buf.write("k\2\u02fb\u02fd\n\b\2\2\u02fc\u02fa\3\2\2\2\u02fc\u02fb")
        buf.write("\3\2\2\2\u02fd\u0300\3\2\2\2\u02fe\u02fc\3\2\2\2\u02fe")
        buf.write("\u02ff\3\2\2\2\u02ff\u0301\3\2\2\2\u0300\u02fe\3\2\2\2")
        buf.write("\u0301\u030c\7)\2\2\u0302\u0307\7$\2\2\u0303\u0306\5\u00d5")
        buf.write("k\2\u0304\u0306\n\t\2\2\u0305\u0303\3\2\2\2\u0305\u0304")
        buf.write("\3\2\2\2\u0306\u0309\3\2\2\2\u0307\u0305\3\2\2\2\u0307")
        buf.write("\u0308\3\2\2\2\u0308\u030a\3\2\2\2\u0309\u0307\3\2\2\2")
        buf.write("\u030a\u030c\7$\2\2\u030b\u02f9\3\2\2\2\u030b\u0302\3")
        buf.write("\2\2\2\u030c\u00d4\3\2\2\2\u030d\u030e\7^\2\2\u030e\u0312")
        buf.write("\13\2\2\2\u030f\u0310\7^\2\2\u0310\u0312\5\u00cdg\2\u0311")
        buf.write("\u030d\3\2\2\2\u0311\u030f\3\2\2\2\u0312\u00d6\3\2\2\2")
        buf.write("\u0313\u0314\4\63;\2\u0314\u00d8\3\2\2\2\u0315\u0316\4")
        buf.write("\62;\2\u0316\u00da\3\2\2\2\u0317\u0318\4\629\2\u0318\u00dc")
        buf.write("\3\2\2\2\u0319\u031c\5\u00d9m\2\u031a\u031c\t\n\2\2\u031b")
        buf.write("\u0319\3\2\2\2\u031b\u031a\3\2\2\2\u031c\u00de\3\2\2\2")
        buf.write("\u031d\u031e\4\62\63\2\u031e\u00e0\3\2\2\2\u031f\u0321")
        buf.write("\5\u00e5s\2\u0320\u031f\3\2\2\2\u0320\u0321\3\2\2\2\u0321")
        buf.write("\u0322\3\2\2\2\u0322\u0327\5\u00e7t\2\u0323\u0324\5\u00e5")
        buf.write("s\2\u0324\u0325\7\60\2\2\u0325\u0327\3\2\2\2\u0326\u0320")
        buf.write("\3\2\2\2\u0326\u0323\3\2\2\2\u0327\u00e2\3\2\2\2\u0328")
        buf.write("\u032b\5\u00e5s\2\u0329\u032b\5\u00e1q\2\u032a\u0328\3")
        buf.write("\2\2\2\u032a\u0329\3\2\2\2\u032b\u032c\3\2\2\2\u032c\u032d")
        buf.write("\5\u00e9u\2\u032d\u00e4\3\2\2\2\u032e\u0330\5\u00d9m\2")
        buf.write("\u032f\u032e\3\2\2\2\u0330\u0331\3\2\2\2\u0331\u032f\3")
        buf.write("\2\2\2\u0331\u0332\3\2\2\2\u0332\u00e6\3\2\2\2\u0333\u0335")
        buf.write("\7\60\2\2\u0334\u0336\5\u00d9m\2\u0335\u0334\3\2\2\2\u0336")
        buf.write("\u0337\3\2\2\2\u0337\u0335\3\2\2\2\u0337\u0338\3\2\2\2")
        buf.write("\u0338\u00e8\3\2\2\2\u0339\u033b\t\13\2\2\u033a\u033c")
        buf.write("\t\f\2\2\u033b\u033a\3\2\2\2\u033b\u033c\3\2\2\2\u033c")
        buf.write("\u033e\3\2\2\2\u033d\u033f\5\u00d9m\2\u033e\u033d\3\2")
        buf.write("\2\2\u033f\u0340\3\2\2\2\u0340\u033e\3\2\2\2\u0340\u0341")
        buf.write("\3\2\2\2\u0341\u00ea\3\2\2\2\u0342\u0345\5W,\2\u0343\u0345")
        buf.write("\5\u00efx\2\u0344\u0342\3\2\2\2\u0344\u0343\3\2\2\2\u0345")
        buf.write("\u00ec\3\2\2\2\u0346\u0349\5\u00ebv\2\u0347\u0349\5\u00d9")
        buf.write("m\2\u0348\u0346\3\2\2\2\u0348\u0347\3\2\2\2\u0349\u00ee")
        buf.write("\3\2\2\2\u034a\u034b\t\r\2\2\u034b\u00f0\3\2\2\2\u034c")
        buf.write("\u034e\t\16\2\2\u034d\u034c\3\2\2\2\u034e\u034f\3\2\2")
        buf.write("\2\u034f\u034d\3\2\2\2\u034f\u0350\3\2\2\2\u0350\u00f2")
        buf.write("\3\2\2\2\u0351\u0355\7%\2\2\u0352\u0354\n\17\2\2\u0353")
        buf.write("\u0352\3\2\2\2\u0354\u0357\3\2\2\2\u0355\u0353\3\2\2\2")
        buf.write("\u0355\u0356\3\2\2\2\u0356\u00f4\3\2\2\2\u0357\u0355\3")
        buf.write("\2\2\2\u0358\u035a\7^\2\2\u0359\u035b\5\u00f1y\2\u035a")
        buf.write("\u0359\3\2\2\2\u035a\u035b\3\2\2\2\u035b\u0361\3\2\2\2")
        buf.write("\u035c\u035e\7\17\2\2\u035d\u035c\3\2\2\2\u035d\u035e")
        buf.write("\3\2\2\2\u035e\u035f\3\2\2\2\u035f\u0362\7\f\2\2\u0360")
        buf.write("\u0362\4\16\17\2\u0361\u035d\3\2\2\2\u0361\u0360\3\2\2")
        buf.write("\2\u0362\u00f6\3\2\2\2\61\2\u016f\u01a2\u01b1\u01bc\u01be")
        buf.write("\u01c5\u01c8\u029d\u02a3\u02a8\u02ac\u02af\u02b7\u02bd")
        buf.write("\u02c3\u02c5\u02cc\u02d3\u02da\u02de\u02e3\u02e7\u02ea")
        buf.write("\u02ec\u02f3\u02fc\u02fe\u0305\u0307\u030b\u0311\u031b")
        buf.write("\u0320\u0326\u032a\u0331\u0337\u033b\u0340\u0344\u0348")
        buf.write("\u034f\u0355\u035a\u035d\u0361\n\3D\2\3E\3\3F\4\3G\5\3")
        buf.write("H\6\3I\7\3g\b\b\2\2")
        return buf.getvalue()


class YarcLexer(YarcLexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    SCENARIO = 3
    SETTINGS = 4
    WRITER = 5
    SNIPPET = 6
    UNIFORM = 7
    NORMAL = 8
    CHOICE = 9
    SEQUENCE = 10
    LOG_UNIFORM = 11
    CREATE = 12
    INSTANTIATE = 13
    GET = 14
    X = 15
    Y = 16
    Z = 17
    EDIT = 18
    SET = 19
    TRANSLATE = 20
    ROTATE = 21
    SCALE = 22
    SEMANTICS = 23
    SCATTER = 24
    EVERY = 25
    FRAMES = 26
    TIME = 27
    AND = 28
    AS = 29
    DEF = 30
    ELIF = 31
    ELSE = 32
    FALSE = 33
    FOR = 34
    IF = 35
    IN = 36
    IS = 37
    NONE = 38
    NOT = 39
    OR = 40
    PASS = 41
    RETURN = 42
    TRUE = 43
    UNDERSCORE = 44
    WITH = 45
    DOT = 46
    RANGE = 47
    ELLIPSIS = 48
    COMMA = 49
    COLON = 50
    SEMI_COLON = 51
    ASSIGN = 52
    BIT_OR = 53
    XOR = 54
    BIT_AND = 55
    BIT_NOT = 56
    LEFT_SHIFT = 57
    RIGHT_SHIFT = 58
    ADD = 59
    MINUS = 60
    DIV = 61
    STAR = 62
    MOD = 63
    IDIV = 64
    POWER = 65
    AT = 66
    ARROW = 67
    LPAREN = 68
    RPAREN = 69
    LBRACK = 70
    RBRACK = 71
    LBRACE = 72
    RBRACE = 73
    LESS_THAN = 74
    GREATER_THAN = 75
    EQUALS = 76
    GT_EQ = 77
    LT_EQ = 78
    NOT_EQ = 79
    ADD_ASSIGN = 80
    SUB_ASSIGN = 81
    MULT_ASSIGN = 82
    AT_ASSIGN = 83
    DIV_ASSIGN = 84
    MOD_ASSIGN = 85
    AND_ASSIGN = 86
    OR_ASSIGN = 87
    XOR_ASSIGN = 88
    LSHIFT_ASSIGN = 89
    RSHIFT_ASSIGN = 90
    POWER_ASSIGN = 91
    IDIV_ASSIGN = 92
    STRING = 93
    NUMBER = 94
    NAME = 95
    STRING_LITERAL = 96
    INTEGER = 97
    DECIMAL_INTEGER = 98
    OCT_INTEGER = 99
    HEX_INTEGER = 100
    BIN_INTEGER = 101
    FLOAT_NUMBER = 102
    NEWLINE = 103
    SKIP_ = 104
    UNKNOWN = 105

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'scenario'", "'writer'", "'create'", "'instantiate'", "'get'", 
            "'x'", "'y'", "'z'", "'set'", "'translate'", "'rotate'", "'scale'", 
            "'semantics'", "'every'", "'and'", "'as'", "'def'", "'elif'", 
            "'else'", "'False'", "'for'", "'if'", "'in'", "'is'", "'None'", 
            "'not'", "'or'", "'pass'", "'return'", "'True'", "'_'", "'with'", 
            "'.'", "'..'", "'...'", "','", "':'", "';'", "'='", "'|'", "'^'", 
            "'&'", "'~'", "'<<'", "'>>'", "'+'", "'-'", "'/'", "'*'", "'%'", 
            "'//'", "'**'", "'@'", "'->'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'<'", "'>'", "'=='", "'>='", "'<='", "'!='", "'+='", 
            "'-='", "'*='", "'@='", "'/='", "'%='", "'&='", "'|='", "'^='", 
            "'<<='", "'>>='", "'**='", "'//='" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "SCENARIO", "SETTINGS", "WRITER", "SNIPPET", 
            "UNIFORM", "NORMAL", "CHOICE", "SEQUENCE", "LOG_UNIFORM", "CREATE", 
            "INSTANTIATE", "GET", "X", "Y", "Z", "EDIT", "SET", "TRANSLATE", 
            "ROTATE", "SCALE", "SEMANTICS", "SCATTER", "EVERY", "FRAMES", 
            "TIME", "AND", "AS", "DEF", "ELIF", "ELSE", "FALSE", "FOR", 
            "IF", "IN", "IS", "NONE", "NOT", "OR", "PASS", "RETURN", "TRUE", 
            "UNDERSCORE", "WITH", "DOT", "RANGE", "ELLIPSIS", "COMMA", "COLON", 
            "SEMI_COLON", "ASSIGN", "BIT_OR", "XOR", "BIT_AND", "BIT_NOT", 
            "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "STAR", 
            "MOD", "IDIV", "POWER", "AT", "ARROW", "LPAREN", "RPAREN", "LBRACK", 
            "RBRACK", "LBRACE", "RBRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", 
            "GT_EQ", "LT_EQ", "NOT_EQ", "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", 
            "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", 
            "XOR_ASSIGN", "LSHIFT_ASSIGN", "RSHIFT_ASSIGN", "POWER_ASSIGN", 
            "IDIV_ASSIGN", "STRING", "NUMBER", "NAME", "STRING_LITERAL", 
            "INTEGER", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
            "BIN_INTEGER", "FLOAT_NUMBER", "NEWLINE", "SKIP_", "UNKNOWN" ]

    ruleNames = [ "SCENARIO", "SETTINGS", "WRITER", "SNIPPET", "UNIFORM", 
                  "NORMAL", "CHOICE", "SEQUENCE", "LOG_UNIFORM", "CREATE", 
                  "INSTANTIATE", "GET", "X", "Y", "Z", "EDIT", "SET", "TRANSLATE", 
                  "ROTATE", "SCALE", "SEMANTICS", "SCATTER", "EVERY", "FRAMES", 
                  "TIME", "NESTED_CODE", "AND", "AS", "DEF", "ELIF", "ELSE", 
                  "FALSE", "FOR", "IF", "IN", "IS", "NONE", "NOT", "OR", 
                  "PASS", "RETURN", "TRUE", "UNDERSCORE", "WITH", "DOT", 
                  "RANGE", "ELLIPSIS", "COMMA", "COLON", "SEMI_COLON", "ASSIGN", 
                  "BIT_OR", "XOR", "BIT_AND", "BIT_NOT", "LEFT_SHIFT", "RIGHT_SHIFT", 
                  "ADD", "MINUS", "DIV", "STAR", "MOD", "IDIV", "POWER", 
                  "AT", "ARROW", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                  "LBRACE", "RBRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LSHIFT_ASSIGN", 
                  "RSHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "STRING", 
                  "NUMBER", "NAME", "STRING_LITERAL", "INTEGER", "DECIMAL_INTEGER", 
                  "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
                  "NEWLINE", "SKIP_", "UNKNOWN", "SHORT_STRING", "STRING_ESCAPE_SEQ", 
                  "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", 
                  "POINT_FLOAT", "EXPONENT_FLOAT", "INT_PART", "FRACTION", 
                  "EXPONENT", "ID_START", "ID_CONTINUE", "LETTER", "SPACES", 
                  "COMMENT", "LINE_JOINING" ]

    grammarFileName = "YarcLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.LPAREN_action 
            actions[67] = self.RPAREN_action 
            actions[68] = self.LBRACK_action 
            actions[69] = self.RBRACK_action 
            actions[70] = self.LBRACE_action 
            actions[71] = self.RBRACE_action 
            actions[101] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.openBrace();
     

    def RPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.closeBrace();
     

    def LBRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.openBrace();
     

    def RBRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.closeBrace();
     

    def LBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.openBrace();
     

    def RBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.closeBrace();
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.onNewLine();
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[101] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


