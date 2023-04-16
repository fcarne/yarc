# Generated from c:\Users\feder\Desktop\University\Magistrale\Secondo_Anno\1_Linguaggi\Progetto\yarc\yarc\dsl\v4\YarcLexer.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2y")
        buf.write("\u0405\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087")
        buf.write("\t\u0087\4\u0088\t\u0088\4\u0089\t\u0089\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u0135\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u015b\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u01b4\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u01c0")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0212\n\37\3 \3 \3 \3 \3 \3")
        buf.write(' \3 \3!\3!\3!\3!\3!\3!\3!\3!\3"\3"\3"\3"\3"\3"\3')
        buf.write("#\3#\3#\3#\3#\3#\3#\5#\u0230\n#\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\5$\u023b\n$\5$\u023d\n$\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3'\3'\3'\3'\3'\3'\3'\3(\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3+\3+\3+\3+\7+\u0272\n+\f+\16+\u0275")
        buf.write("\13+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\3I\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3")
        buf.write("R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3W\3")
        buf.write("X\3X\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\3\\\3]\3]\3]\3^\3")
        buf.write("^\3^\3_\3_\3_\3`\3`\3`\3a\3a\3a\3b\3b\3b\3c\3c\3c\3d\3")
        buf.write("d\3d\3e\3e\3e\3f\3f\3f\3f\3g\3g\3g\3g\3h\3h\3h\3h\3i\3")
        buf.write("i\3i\3i\3j\3j\3k\3k\5k\u033d\nk\3l\3l\7l\u0341\nl\fl\16")
        buf.write("l\u0344\13l\3m\3m\3m\3n\3n\5n\u034b\nn\3n\3n\5n\u034f")
        buf.write("\nn\3n\5n\u0352\nn\3n\3n\3o\3o\3o\3o\5o\u035a\no\3p\3")
        buf.write("p\7p\u035e\np\fp\16p\u0361\13p\3p\6p\u0364\np\rp\16p\u0365")
        buf.write("\5p\u0368\np\3q\3q\3q\6q\u036d\nq\rq\16q\u036e\3r\3r\3")
        buf.write("r\6r\u0374\nr\rr\16r\u0375\3s\3s\3s\6s\u037b\ns\rs\16")
        buf.write("s\u037c\3t\3t\5t\u0381\nt\3u\3u\3u\5u\u0386\nu\3u\3u\5")
        buf.write("u\u038a\nu\3u\5u\u038d\nu\5u\u038f\nu\3u\3u\3v\3v\3v\5")
        buf.write("v\u0396\nv\3v\3v\3w\3w\3x\3x\3x\7x\u039f\nx\fx\16x\u03a2")
        buf.write("\13x\3x\3x\3x\3x\7x\u03a8\nx\fx\16x\u03ab\13x\3x\5x\u03ae")
        buf.write("\nx\3y\3y\3y\3y\5y\u03b4\ny\3z\3z\3{\3{\3|\3|\3}\3}\5")
        buf.write("}\u03be\n}\3~\3~\3\177\5\177\u03c3\n\177\3\177\3\177\3")
        buf.write("\177\3\177\5\177\u03c9\n\177\3\u0080\3\u0080\5\u0080\u03cd")
        buf.write("\n\u0080\3\u0080\3\u0080\3\u0081\6\u0081\u03d2\n\u0081")
        buf.write("\r\u0081\16\u0081\u03d3\3\u0082\3\u0082\6\u0082\u03d8")
        buf.write("\n\u0082\r\u0082\16\u0082\u03d9\3\u0083\3\u0083\5\u0083")
        buf.write("\u03de\n\u0083\3\u0083\6\u0083\u03e1\n\u0083\r\u0083\16")
        buf.write("\u0083\u03e2\3\u0084\3\u0084\5\u0084\u03e7\n\u0084\3\u0085")
        buf.write("\3\u0085\5\u0085\u03eb\n\u0085\3\u0086\3\u0086\3\u0087")
        buf.write("\6\u0087\u03f0\n\u0087\r\u0087\16\u0087\u03f1\3\u0088")
        buf.write("\3\u0088\7\u0088\u03f6\n\u0088\f\u0088\16\u0088\u03f9")
        buf.write("\13\u0088\3\u0089\3\u0089\5\u0089\u03fd\n\u0089\3\u0089")
        buf.write("\5\u0089\u0400\n\u0089\3\u0089\3\u0089\5\u0089\u0404\n")
        buf.write("\u0089\3\u0273\2\u008a\3\5\5\6\7\7\t\b\13\t\r\n\17\13")
        buf.write("\21\f\23\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25")
        buf.write("%\26'\27)\30+\31-\32/\33\61\34\63\35\65\36\67\379 ;!")
        buf.write("=\"?#A$C%E&G'I(K)M*O+Q,S-U\2W.Y/[\60]\61_\62a\63c\64")
        buf.write("e\65g\66i\67k8m9o:q;s<u=w>y?{@}A\177B\u0081C\u0083D\u0085")
        buf.write("E\u0087F\u0089G\u008bH\u008dI\u008fJ\u0091K\u0093L\u0095")
        buf.write("M\u0097N\u0099O\u009bP\u009dQ\u009fR\u00a1S\u00a3T\u00a5")
        buf.write("U\u00a7V\u00a9W\u00abX\u00adY\u00afZ\u00b1[\u00b3\\\u00b5")
        buf.write("]\u00b7^\u00b9_\u00bb`\u00bda\u00bfb\u00c1c\u00c3d\u00c5")
        buf.write("e\u00c7f\u00c9g\u00cbh\u00cdi\u00cfj\u00d1k\u00d3l\u00d5")
        buf.write("m\u00d7n\u00d9o\u00dbp\u00ddq\u00dfr\u00e1s\u00e3t\u00e5")
        buf.write("u\u00e7v\u00e9w\u00ebx\u00edy\u00ef\2\u00f1\2\u00f3\2")
        buf.write("\u00f5\2\u00f7\2\u00f9\2\u00fb\2\u00fd\2\u00ff\2\u0101")
        buf.write("\2\u0103\2\u0105\2\u0107\2\u0109\2\u010b\2\u010d\2\u010f")
        buf.write("\2\u0111\2\3\2\21\4\2Z\\z|\4\2WWww\4\2HHhh\4\2TTtt\4\2")
        buf.write("QQqq\4\2ZZzz\4\2DDdd\6\2\f\f\16\17))^^\6\2\f\f\16\17$")
        buf.write('$^^\4\2CHch\4\2GGgg\4\2--//\4\2C\\c|\4\2\13\13""\4\2')
        buf.write("\f\f\16\17\2\u042c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
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
        buf.write("\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2")
        buf.write("\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2\2\2\u00dd")
        buf.write("\3\2\2\2\2\u00df\3\2\2\2\2\u00e1\3\2\2\2\2\u00e3\3\2\2")
        buf.write("\2\2\u00e5\3\2\2\2\2\u00e7\3\2\2\2\2\u00e9\3\2\2\2\2\u00eb")
        buf.write("\3\2\2\2\2\u00ed\3\2\2\2\3\u0113\3\2\2\2\5\u011c\3\2\2")
        buf.write("\2\7\u0125\3\2\2\2\t\u012c\3\2\2\2\13\u015a\3\2\2\2\r")
        buf.write("\u015c\3\2\2\2\17\u0163\3\2\2\2\21\u0169\3\2\2\2\23\u0170")
        buf.write("\3\2\2\2\25\u0179\3\2\2\2\27\u0182\3\2\2\2\31\u0189\3")
        buf.write("\2\2\2\33\u0195\3\2\2\2\35\u019b\3\2\2\2\37\u01a0\3\2")
        buf.write("\2\2!\u01a4\3\2\2\2#\u01b3\3\2\2\2%\u01bf\3\2\2\2'\u01c1")
        buf.write("\3\2\2\2)\u01c5\3\2\2\2+\u01cf\3\2\2\2-\u01d6\3\2\2\2")
        buf.write("/\u01dc\3\2\2\2\61\u01e6\3\2\2\2\63\u01ee\3\2\2\2\65\u01f3")
        buf.write("\3\2\2\2\67\u01fb\3\2\2\29\u0203\3\2\2\2;\u0205\3\2\2")
        buf.write("\2=\u0211\3\2\2\2?\u0213\3\2\2\2A\u021a\3\2\2\2C\u0222")
        buf.write("\3\2\2\2E\u0228\3\2\2\2G\u0231\3\2\2\2I\u023e\3\2\2\2")
        buf.write("K\u0246\3\2\2\2M\u024d\3\2\2\2O\u0254\3\2\2\2Q\u025d\3")
        buf.write("\2\2\2S\u0268\3\2\2\2U\u026d\3\2\2\2W\u0279\3\2\2\2Y\u027c")
        buf.write("\3\2\2\2[\u027f\3\2\2\2]\u0282\3\2\2\2_\u0286\3\2\2\2")
        buf.write("a\u028a\3\2\2\2c\u028f\3\2\2\2e\u0295\3\2\2\2g\u0299\3")
        buf.write("\2\2\2i\u029c\3\2\2\2k\u029f\3\2\2\2m\u02a2\3\2\2\2o\u02a7")
        buf.write("\3\2\2\2q\u02ab\3\2\2\2s\u02ae\3\2\2\2u\u02b5\3\2\2\2")
        buf.write("w\u02ba\3\2\2\2y\u02bc\3\2\2\2{\u02be\3\2\2\2}\u02c1\3")
        buf.write("\2\2\2\177\u02c5\3\2\2\2\u0081\u02c7\3\2\2\2\u0083\u02c9")
        buf.write("\3\2\2\2\u0085\u02cb\3\2\2\2\u0087\u02cd\3\2\2\2\u0089")
        buf.write("\u02cf\3\2\2\2\u008b\u02d1\3\2\2\2\u008d\u02d3\3\2\2\2")
        buf.write("\u008f\u02d5\3\2\2\2\u0091\u02d8\3\2\2\2\u0093\u02db\3")
        buf.write("\2\2\2\u0095\u02dd\3\2\2\2\u0097\u02df\3\2\2\2\u0099\u02e1")
        buf.write("\3\2\2\2\u009b\u02e3\3\2\2\2\u009d\u02e5\3\2\2\2\u009f")
        buf.write("\u02e8\3\2\2\2\u00a1\u02eb\3\2\2\2\u00a3\u02ee\3\2\2\2")
        buf.write("\u00a5\u02f1\3\2\2\2\u00a7\u02f4\3\2\2\2\u00a9\u02f7\3")
        buf.write("\2\2\2\u00ab\u02fa\3\2\2\2\u00ad\u02fd\3\2\2\2\u00af\u0300")
        buf.write("\3\2\2\2\u00b1\u0302\3\2\2\2\u00b3\u0304\3\2\2\2\u00b5")
        buf.write("\u0307\3\2\2\2\u00b7\u030a\3\2\2\2\u00b9\u030d\3\2\2\2")
        buf.write("\u00bb\u0310\3\2\2\2\u00bd\u0313\3\2\2\2\u00bf\u0316\3")
        buf.write("\2\2\2\u00c1\u0319\3\2\2\2\u00c3\u031c\3\2\2\2\u00c5\u031f")
        buf.write("\3\2\2\2\u00c7\u0322\3\2\2\2\u00c9\u0325\3\2\2\2\u00cb")
        buf.write("\u0328\3\2\2\2\u00cd\u032c\3\2\2\2\u00cf\u0330\3\2\2\2")
        buf.write("\u00d1\u0334\3\2\2\2\u00d3\u0338\3\2\2\2\u00d5\u033c\3")
        buf.write("\2\2\2\u00d7\u033e\3\2\2\2\u00d9\u0345\3\2\2\2\u00db\u0351")
        buf.write("\3\2\2\2\u00dd\u0359\3\2\2\2\u00df\u0367\3\2\2\2\u00e1")
        buf.write("\u0369\3\2\2\2\u00e3\u0370\3\2\2\2\u00e5\u0377\3\2\2\2")
        buf.write("\u00e7\u0380\3\2\2\2\u00e9\u038e\3\2\2\2\u00eb\u0395\3")
        buf.write("\2\2\2\u00ed\u0399\3\2\2\2\u00ef\u03ad\3\2\2\2\u00f1\u03b3")
        buf.write("\3\2\2\2\u00f3\u03b5\3\2\2\2\u00f5\u03b7\3\2\2\2\u00f7")
        buf.write("\u03b9\3\2\2\2\u00f9\u03bd\3\2\2\2\u00fb\u03bf\3\2\2\2")
        buf.write("\u00fd\u03c8\3\2\2\2\u00ff\u03cc\3\2\2\2\u0101\u03d1\3")
        buf.write("\2\2\2\u0103\u03d5\3\2\2\2\u0105\u03db\3\2\2\2\u0107\u03e6")
        buf.write("\3\2\2\2\u0109\u03ea\3\2\2\2\u010b\u03ec\3\2\2\2\u010d")
        buf.write("\u03ef\3\2\2\2\u010f\u03f3\3\2\2\2\u0111\u03fa\3\2\2\2")
        buf.write("\u0113\u0114\7u\2\2\u0114\u0115\7e\2\2\u0115\u0116\7g")
        buf.write("\2\2\u0116\u0117\7p\2\2\u0117\u0118\7c\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\u011a\7k\2\2\u011a\u011b\7q\2\2\u011b\4")
        buf.write("\3\2\2\2\u011c\u011d\7u\2\2\u011d\u011e\7g\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7v\2\2\u0120\u0121\7k\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7i\2\2\u0123\u0124\7u\2\2\u0124\6")
        buf.write("\3\2\2\2\u0125\u0126\7y\2\2\u0126\u0127\7t\2\2\u0127\u0128")
        buf.write("\7k\2\2\u0128\u0129\7v\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\b\3\2\2\2\u012c\u012d\7n\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7d\2\2\u012f\u0134\3\2\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131\u0132\7c\2\2\u0132\u0133\7t\2\2\u0133\u0135")
        buf.write("\7{\2\2\u0134\u0130\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\n\3\2\2\2\u0136\u0137\7r\2\2\u0137\u0138\7n\2\2\u0138")
        buf.write("\u0139\7c\2\2\u0139\u013a\7p\2\2\u013a\u015b\7g\2\2\u013b")
        buf.write("\u013c\7e\2\2\u013c\u013d\7w\2\2\u013d\u013e\7d\2\2\u013e")
        buf.write("\u015b\7g\2\2\u013f\u0140\7u\2\2\u0140\u0141\7r\2\2\u0141")
        buf.write("\u0142\7j\2\2\u0142\u0143\7g\2\2\u0143\u0144\7t\2\2\u0144")
        buf.write("\u015b\7g\2\2\u0145\u0146\7e\2\2\u0146\u0147\7{\2\2\u0147")
        buf.write("\u0148\7n\2\2\u0148\u0149\7k\2\2\u0149\u014a\7p\2\2\u014a")
        buf.write("\u014b\7f\2\2\u014b\u014c\7g\2\2\u014c\u015b\7t\2\2\u014d")
        buf.write("\u014e\7e\2\2\u014e\u014f\7q\2\2\u014f\u0150\7p\2\2\u0150")
        buf.write("\u015b\7g\2\2\u0151\u0152\7v\2\2\u0152\u0153\7q\2\2\u0153")
        buf.write("\u0154\7t\2\2\u0154\u0155\7w\2\2\u0155\u015b\7u\2\2\u0156")
        buf.write("\u0157\7f\2\2\u0157\u0158\7k\2\2\u0158\u0159\7u\2\2\u0159")
        buf.write("\u015b\7m\2\2\u015a\u0136\3\2\2\2\u015a\u013b\3\2\2\2")
        buf.write("\u015a\u013f\3\2\2\2\u015a\u0145\3\2\2\2\u015a\u014d\3")
        buf.write("\2\2\2\u015a\u0151\3\2\2\2\u015a\u0156\3\2\2\2\u015b\f")
        buf.write("\3\2\2\2\u015c\u015d\7e\2\2\u015d\u015e\7c\2\2\u015e\u015f")
        buf.write("\7o\2\2\u015f\u0160\7g\2\2\u0160\u0161\7t\2\2\u0161\u0162")
        buf.write("\7c\2\2\u0162\16\3\2\2\2\u0163\u0164\7n\2\2\u0164\u0165")
        buf.write("\7k\2\2\u0165\u0166\7i\2\2\u0166\u0167\7j\2\2\u0167\u0168")
        buf.write("\7v\2\2\u0168\20\3\2\2\2\u0169\u016a\7u\2\2\u016a\u016b")
        buf.write("\7v\2\2\u016b\u016c\7g\2\2\u016c\u016d\7t\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7q\2\2\u016f\22\3\2\2\2\u0170\u0171")
        buf.write("\7o\2\2\u0171\u0172\7c\2\2\u0172\u0173\7v\2\2\u0173\u0174")
        buf.write("\7g\2\2\u0174\u0175\7t\2\2\u0175\u0176\7k\2\2\u0176\u0177")
        buf.write("\7c\2\2\u0177\u0178\7n\2\2\u0178\24\3\2\2\2\u0179\u017a")
        buf.write("\7v\2\2\u017a\u017b\7k\2\2\u017b\u017c\7o\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\u017e\7n\2\2\u017e\u017f\7k\2\2\u017f\u0180")
        buf.write("\7p\2\2\u0180\u0181\7g\2\2\u0181\26\3\2\2\2\u0182\u0183")
        buf.write("\7e\2\2\u0183\u0184\7t\2\2\u0184\u0185\7g\2\2\u0185\u0186")
        buf.write("\7c\2\2\u0186\u0187\7v\2\2\u0187\u0188\7g\2\2\u0188\30")
        buf.write("\3\2\2\2\u0189\u018a\7k\2\2\u018a\u018b\7p\2\2\u018b\u018c")
        buf.write("\7u\2\2\u018c\u018d\7v\2\2\u018d\u018e\7c\2\2\u018e\u018f")
        buf.write("\7p\2\2\u018f\u0190\7v\2\2\u0190\u0191\7k\2\2\u0191\u0192")
        buf.write("\7c\2\2\u0192\u0193\7v\2\2\u0193\u0194\7g\2\2\u0194\32")
        buf.write("\3\2\2\2\u0195\u0196\7i\2\2\u0196\u0197\7t\2\2\u0197\u0198")
        buf.write("\7q\2\2\u0198\u0199\7w\2\2\u0199\u019a\7r\2\2\u019a\34")
        buf.write("\3\2\2\2\u019b\u019c\7q\2\2\u019c\u019d\7r\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019e\u019f\7p\2\2\u019f\36\3\2\2\2\u01a0\u01a1")
        buf.write("\7i\2\2\u01a1\u01a2\7g\2\2\u01a2\u01a3\7v\2\2\u01a3 \3")
        buf.write("\2\2\2\u01a4\u01a5\7h\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7")
        buf.write('\7v\2\2\u01a7\u01a8\7e\2\2\u01a8\u01a9\7j\2\2\u01a9"')
        buf.write("\3\2\2\2\u01aa\u01ab\7o\2\2\u01ab\u01ac\7c\2\2\u01ac\u01ad")
        buf.write("\7v\2\2\u01ad\u01ae\7e\2\2\u01ae\u01b4\7j\2\2\u01af\u01b0")
        buf.write("\7n\2\2\u01b0\u01b1\7k\2\2\u01b1\u01b2\7m\2\2\u01b2\u01b4")
        buf.write("\7g\2\2\u01b3\u01aa\3\2\2\2\u01b3\u01af\3\2\2\2\u01b4")
        buf.write("$\3\2\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7\7f\2\2\u01b7")
        buf.write("\u01b8\7k\2\2\u01b8\u01c0\7v\2\2\u01b9\u01ba\7o\2\2\u01ba")
        buf.write("\u01bb\7q\2\2\u01bb\u01bc\7f\2\2\u01bc\u01bd\7k\2\2\u01bd")
        buf.write("\u01be\7h\2\2\u01be\u01c0\7{\2\2\u01bf\u01b5\3\2\2\2\u01bf")
        buf.write("\u01b9\3\2\2\2\u01c0&\3\2\2\2\u01c1\u01c2\7u\2\2\u01c2")
        buf.write("\u01c3\7g\2\2\u01c3\u01c4\7v\2\2\u01c4(\3\2\2\2\u01c5")
        buf.write("\u01c6\7v\2\2\u01c6\u01c7\7t\2\2\u01c7\u01c8\7c\2\2\u01c8")
        buf.write("\u01c9\7p\2\2\u01c9\u01ca\7u\2\2\u01ca\u01cb\7n\2\2\u01cb")
        buf.write("\u01cc\7c\2\2\u01cc\u01cd\7v\2\2\u01cd\u01ce\7g\2\2\u01ce")
        buf.write("*\3\2\2\2\u01cf\u01d0\7t\2\2\u01d0\u01d1\7q\2\2\u01d1")
        buf.write("\u01d2\7v\2\2\u01d2\u01d3\7c\2\2\u01d3\u01d4\7v\2\2\u01d4")
        buf.write("\u01d5\7g\2\2\u01d5,\3\2\2\2\u01d6\u01d7\7u\2\2\u01d7")
        buf.write("\u01d8\7e\2\2\u01d8\u01d9\7c\2\2\u01d9\u01da\7n\2\2\u01da")
        buf.write("\u01db\7g\2\2\u01db.\3\2\2\2\u01dc\u01dd\7u\2\2\u01dd")
        buf.write("\u01de\7g\2\2\u01de\u01df\7o\2\2\u01df\u01e0\7c\2\2\u01e0")
        buf.write("\u01e1\7p\2\2\u01e1\u01e2\7v\2\2\u01e2\u01e3\7k\2\2\u01e3")
        buf.write("\u01e4\7e\2\2\u01e4\u01e5\7u\2\2\u01e5\60\3\2\2\2\u01e6")
        buf.write("\u01e7\7x\2\2\u01e7\u01e8\7k\2\2\u01e8\u01e9\7u\2\2\u01e9")
        buf.write("\u01ea\7k\2\2\u01ea\u01eb\7d\2\2\u01eb\u01ec\7n\2\2\u01ec")
        buf.write("\u01ed\7g\2\2\u01ed\62\3\2\2\2\u01ee\u01ef\7u\2\2\u01ef")
        buf.write("\u01f0\7k\2\2\u01f0\u01f1\7|\2\2\u01f1\u01f2\7g\2\2\u01f2")
        buf.write("\64\3\2\2\2\u01f3\u01f4\7n\2\2\u01f4\u01f5\7q\2\2\u01f5")
        buf.write("\u01f6\7q\2\2\u01f6\u01f7\7m\2\2\u01f7\u01f8\7a\2\2\u01f8")
        buf.write("\u01f9\7c\2\2\u01f9\u01fa\7v\2\2\u01fa\66\3\2\2\2\u01fb")
        buf.write("\u01fc\7w\2\2\u01fc\u01fd\7r\2\2\u01fd\u01fe\7a\2\2\u01fe")
        buf.write("\u01ff\7c\2\2\u01ff\u0200\7z\2\2\u0200\u0201\7k\2\2\u0201")
        buf.write("\u0202\7u\2\2\u02028\3\2\2\2\u0203\u0204\t\2\2\2\u0204")
        buf.write(":\3\2\2\2\u0205\u0206\7u\2\2\u0206\u0207\7e\2\2\u0207")
        buf.write("\u0208\7c\2\2\u0208\u0209\7v\2\2\u0209\u020a\7v\2\2\u020a")
        buf.write("\u020b\7g\2\2\u020b\u020c\7t\2\2\u020c<\3\2\2\2\u020d")
        buf.write("\u020e\7\64\2\2\u020e\u0212\7f\2\2\u020f\u0210\7\65\2")
        buf.write("\2\u0210\u0212\7f\2\2\u0211\u020d\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0212>\3\2\2\2\u0213\u0214\7c\2\2\u0214\u0215")
        buf.write("\7t\2\2\u0215\u0216\7q\2\2\u0216\u0217\7w\2\2\u0217\u0218")
        buf.write("\7p\2\2\u0218\u0219\7f\2\2\u0219@\3\2\2\2\u021a\u021b")
        buf.write("\7v\2\2\u021b\u021c\7g\2\2\u021c\u021d\7z\2\2\u021d\u021e")
        buf.write("\7v\2\2\u021e\u021f\7w\2\2\u021f\u0220\7t\2\2\u0220\u0221")
        buf.write("\7g\2\2\u0221B\3\2\2\2\u0222\u0223\7g\2\2\u0223\u0224")
        buf.write("\7x\2\2\u0224\u0225\7g\2\2\u0225\u0226\7t\2\2\u0226\u0227")
        buf.write("\7{\2\2\u0227D\3\2\2\2\u0228\u0229\7h\2\2\u0229\u022a")
        buf.write("\7t\2\2\u022a\u022b\7c\2\2\u022b\u022c\7o\2\2\u022c\u022d")
        buf.write("\7g\2\2\u022d\u022f\3\2\2\2\u022e\u0230\7u\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u022f\u0230\3\2\2\2\u0230F\3\2\2\2\u0231\u0232")
        buf.write("\7u\2\2\u0232\u0233\7g\2\2\u0233\u0234\7e\2\2\u0234\u023c")
        buf.write("\3\2\2\2\u0235\u0236\7q\2\2\u0236\u0237\7p\2\2\u0237\u0238")
        buf.write("\7f\2\2\u0238\u023a\3\2\2\2\u0239\u023b\7u\2\2\u023a\u0239")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023d\3\2\2\2\u023c")
        buf.write("\u0235\3\2\2\2\u023c\u023d\3\2\2\2\u023dH\3\2\2\2\u023e")
        buf.write("\u023f\7W\2\2\u023f\u0240\7p\2\2\u0240\u0241\7k\2\2\u0241")
        buf.write("\u0242\7h\2\2\u0242\u0243\7q\2\2\u0243\u0244\7t\2\2\u0244")
        buf.write("\u0245\7o\2\2\u0245J\3\2\2\2\u0246\u0247\7P\2\2\u0247")
        buf.write("\u0248\7q\2\2\u0248\u0249\7t\2\2\u0249\u024a\7o\2\2\u024a")
        buf.write("\u024b\7c\2\2\u024b\u024c\7n\2\2\u024cL\3\2\2\2\u024d")
        buf.write("\u024e\7E\2\2\u024e\u024f\7j\2\2\u024f\u0250\7q\2\2\u0250")
        buf.write("\u0251\7k\2\2\u0251\u0252\7e\2\2\u0252\u0253\7g\2\2\u0253")
        buf.write("N\3\2\2\2\u0254\u0255\7U\2\2\u0255\u0256\7g\2\2\u0256")
        buf.write("\u0257\7s\2\2\u0257\u0258\7w\2\2\u0258\u0259\7g\2\2\u0259")
        buf.write("\u025a\7p\2\2\u025a\u025b\7e\2\2\u025b\u025c\7g\2\2\u025c")
        buf.write("P\3\2\2\2\u025d\u025e\7N\2\2\u025e\u025f\7q\2\2\u025f")
        buf.write("\u0260\7i\2\2\u0260\u0261\7W\2\2\u0261\u0262\7p\2\2\u0262")
        buf.write("\u0263\7k\2\2\u0263\u0264\7h\2\2\u0264\u0265\7q\2\2\u0265")
        buf.write("\u0266\7t\2\2\u0266\u0267\7o\2\2\u0267R\3\2\2\2\u0268")
        buf.write("\u0269\5U+\2\u0269\u026a\b*\2\2\u026a\u026b\3\2\2\2\u026b")
        buf.write("\u026c\b*\3\2\u026cT\3\2\2\2\u026d\u026e\5\u00abV\2\u026e")
        buf.write("\u0273\5\u00abV\2\u026f\u0272\5U+\2\u0270\u0272\13\2\2")
        buf.write("\2\u0271\u026f\3\2\2\2\u0271\u0270\3\2\2\2\u0272\u0275")
        buf.write("\3\2\2\2\u0273\u0274\3\2\2\2\u0273\u0271\3\2\2\2\u0274")
        buf.write("\u0276\3\2\2\2\u0275\u0273\3\2\2\2\u0276\u0277\5\u00ad")
        buf.write("W\2\u0277\u0278\5\u00adW\2\u0278V\3\2\2\2\u0279\u027a")
        buf.write("\7v\2\2\u027a\u027b\7q\2\2\u027bX\3\2\2\2\u027c\u027d")
        buf.write("\7q\2\2\u027d\u027e\7p\2\2\u027eZ\3\2\2\2\u027f\u0280")
        buf.write("\7c\2\2\u0280\u0281\7v\2\2\u0281\\\3\2\2\2\u0282\u0283")
        buf.write("\7c\2\2\u0283\u0284\7p\2\2\u0284\u0285\7f\2\2\u0285^\3")
        buf.write("\2\2\2\u0286\u0287\7f\2\2\u0287\u0288\7g\2\2\u0288\u0289")
        buf.write("\7h\2\2\u0289`\3\2\2\2\u028a\u028b\7g\2\2\u028b\u028c")
        buf.write("\7n\2\2\u028c\u028d\7u\2\2\u028d\u028e\7g\2\2\u028eb\3")
        buf.write("\2\2\2\u028f\u0290\7h\2\2\u0290\u0291\7c\2\2\u0291\u0292")
        buf.write("\7n\2\2\u0292\u0293\7u\2\2\u0293\u0294\7g\2\2\u0294d\3")
        buf.write("\2\2\2\u0295\u0296\7h\2\2\u0296\u0297\7q\2\2\u0297\u0298")
        buf.write("\7t\2\2\u0298f\3\2\2\2\u0299\u029a\7k\2\2\u029a\u029b")
        buf.write("\7h\2\2\u029bh\3\2\2\2\u029c\u029d\7k\2\2\u029d\u029e")
        buf.write("\7p\2\2\u029ej\3\2\2\2\u029f\u02a0\7k\2\2\u02a0\u02a1")
        buf.write("\7u\2\2\u02a1l\3\2\2\2\u02a2\u02a3\7p\2\2\u02a3\u02a4")
        buf.write("\7q\2\2\u02a4\u02a5\7p\2\2\u02a5\u02a6\7g\2\2\u02a6n\3")
        buf.write("\2\2\2\u02a7\u02a8\7p\2\2\u02a8\u02a9\7q\2\2\u02a9\u02aa")
        buf.write("\7v\2\2\u02aap\3\2\2\2\u02ab\u02ac\7q\2\2\u02ac\u02ad")
        buf.write("\7t\2\2\u02adr\3\2\2\2\u02ae\u02af\7t\2\2\u02af\u02b0")
        buf.write("\7g\2\2\u02b0\u02b1\7v\2\2\u02b1\u02b2\7w\2\2\u02b2\u02b3")
        buf.write("\7t\2\2\u02b3\u02b4\7p\2\2\u02b4t\3\2\2\2\u02b5\u02b6")
        buf.write("\7v\2\2\u02b6\u02b7\7t\2\2\u02b7\u02b8\7w\2\2\u02b8\u02b9")
        buf.write("\7g\2\2\u02b9v\3\2\2\2\u02ba\u02bb\7a\2\2\u02bbx\3\2\2")
        buf.write("\2\u02bc\u02bd\7\60\2\2\u02bdz\3\2\2\2\u02be\u02bf\7\60")
        buf.write("\2\2\u02bf\u02c0\7\60\2\2\u02c0|\3\2\2\2\u02c1\u02c2\7")
        buf.write("\60\2\2\u02c2\u02c3\7\60\2\2\u02c3\u02c4\7\60\2\2\u02c4")
        buf.write("~\3\2\2\2\u02c5\u02c6\7.\2\2\u02c6\u0080\3\2\2\2\u02c7")
        buf.write("\u02c8\7<\2\2\u02c8\u0082\3\2\2\2\u02c9\u02ca\7=\2\2\u02ca")
        buf.write("\u0084\3\2\2\2\u02cb\u02cc\7?\2\2\u02cc\u0086\3\2\2\2")
        buf.write("\u02cd\u02ce\7~\2\2\u02ce\u0088\3\2\2\2\u02cf\u02d0\7")
        buf.write("`\2\2\u02d0\u008a\3\2\2\2\u02d1\u02d2\7(\2\2\u02d2\u008c")
        buf.write("\3\2\2\2\u02d3\u02d4\7\u0080\2\2\u02d4\u008e\3\2\2\2\u02d5")
        buf.write("\u02d6\7>\2\2\u02d6\u02d7\7>\2\2\u02d7\u0090\3\2\2\2\u02d8")
        buf.write("\u02d9\7@\2\2\u02d9\u02da\7@\2\2\u02da\u0092\3\2\2\2\u02db")
        buf.write("\u02dc\7-\2\2\u02dc\u0094\3\2\2\2\u02dd\u02de\7/\2\2\u02de")
        buf.write("\u0096\3\2\2\2\u02df\u02e0\7\61\2\2\u02e0\u0098\3\2\2")
        buf.write("\2\u02e1\u02e2\7,\2\2\u02e2\u009a\3\2\2\2\u02e3\u02e4")
        buf.write("\7'\2\2\u02e4\u009c\3\2\2\2\u02e5\u02e6\7\61\2\2\u02e6")
        buf.write("\u02e7\7\61\2\2\u02e7\u009e\3\2\2\2\u02e8\u02e9\7,\2\2")
        buf.write("\u02e9\u02ea\7,\2\2\u02ea\u00a0\3\2\2\2\u02eb\u02ec\7")
        buf.write("/\2\2\u02ec\u02ed\7@\2\2\u02ed\u00a2\3\2\2\2\u02ee\u02ef")
        buf.write("\7*\2\2\u02ef\u02f0\bR\4\2\u02f0\u00a4\3\2\2\2\u02f1\u02f2")
        buf.write("\7+\2\2\u02f2\u02f3\bS\5\2\u02f3\u00a6\3\2\2\2\u02f4\u02f5")
        buf.write("\7]\2\2\u02f5\u02f6\bT\6\2\u02f6\u00a8\3\2\2\2\u02f7\u02f8")
        buf.write("\7_\2\2\u02f8\u02f9\bU\7\2\u02f9\u00aa\3\2\2\2\u02fa\u02fb")
        buf.write("\7}\2\2\u02fb\u02fc\bV\b\2\u02fc\u00ac\3\2\2\2\u02fd\u02fe")
        buf.write("\7\177\2\2\u02fe\u02ff\bW\t\2\u02ff\u00ae\3\2\2\2\u0300")
        buf.write("\u0301\7>\2\2\u0301\u00b0\3\2\2\2\u0302\u0303\7@\2\2\u0303")
        buf.write("\u00b2\3\2\2\2\u0304\u0305\7?\2\2\u0305\u0306\7?\2\2\u0306")
        buf.write("\u00b4\3\2\2\2\u0307\u0308\7@\2\2\u0308\u0309\7?\2\2\u0309")
        buf.write("\u00b6\3\2\2\2\u030a\u030b\7>\2\2\u030b\u030c\7?\2\2\u030c")
        buf.write("\u00b8\3\2\2\2\u030d\u030e\7#\2\2\u030e\u030f\7?\2\2\u030f")
        buf.write("\u00ba\3\2\2\2\u0310\u0311\7-\2\2\u0311\u0312\7?\2\2\u0312")
        buf.write("\u00bc\3\2\2\2\u0313\u0314\7/\2\2\u0314\u0315\7?\2\2\u0315")
        buf.write("\u00be\3\2\2\2\u0316\u0317\7,\2\2\u0317\u0318\7?\2\2\u0318")
        buf.write("\u00c0\3\2\2\2\u0319\u031a\7\61\2\2\u031a\u031b\7?\2\2")
        buf.write("\u031b\u00c2\3\2\2\2\u031c\u031d\7'\2\2\u031d\u031e\7")
        buf.write("?\2\2\u031e\u00c4\3\2\2\2\u031f\u0320\7(\2\2\u0320\u0321")
        buf.write("\7?\2\2\u0321\u00c6\3\2\2\2\u0322\u0323\7~\2\2\u0323\u0324")
        buf.write("\7?\2\2\u0324\u00c8\3\2\2\2\u0325\u0326\7`\2\2\u0326\u0327")
        buf.write("\7?\2\2\u0327\u00ca\3\2\2\2\u0328\u0329\7>\2\2\u0329\u032a")
        buf.write("\7>\2\2\u032a\u032b\7?\2\2\u032b\u00cc\3\2\2\2\u032c\u032d")
        buf.write("\7@\2\2\u032d\u032e\7@\2\2\u032e\u032f\7?\2\2\u032f\u00ce")
        buf.write("\3\2\2\2\u0330\u0331\7,\2\2\u0331\u0332\7,\2\2\u0332\u0333")
        buf.write("\7?\2\2\u0333\u00d0\3\2\2\2\u0334\u0335\7\61\2\2\u0335")
        buf.write("\u0336\7\61\2\2\u0336\u0337\7?\2\2\u0337\u00d2\3\2\2\2")
        buf.write("\u0338\u0339\5\u00dbn\2\u0339\u00d4\3\2\2\2\u033a\u033d")
        buf.write("\5\u00ddo\2\u033b\u033d\5\u00e7t\2\u033c\u033a\3\2\2\2")
        buf.write("\u033c\u033b\3\2\2\2\u033d\u00d6\3\2\2\2\u033e\u0342\5")
        buf.write("\u0107\u0084\2\u033f\u0341\5\u0109\u0085\2\u0340\u033f")
        buf.write("\3\2\2\2\u0341\u0344\3\2\2\2\u0342\u0340\3\2\2\2\u0342")
        buf.write("\u0343\3\2\2\2\u0343\u00d8\3\2\2\2\u0344\u0342\3\2\2\2")
        buf.write("\u0345\u0346\7&\2\2\u0346\u0347\5\u00d7l\2\u0347\u00da")
        buf.write("\3\2\2\2\u0348\u0352\t\3\2\2\u0349\u034b\t\4\2\2\u034a")
        buf.write("\u0349\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u034c\3\2\2\2")
        buf.write("\u034c\u0352\t\5\2\2\u034d\u034f\t\5\2\2\u034e\u034d\3")
        buf.write("\2\2\2\u034e\u034f\3\2\2\2\u034f\u0350\3\2\2\2\u0350\u0352")
        buf.write("\t\4\2\2\u0351\u0348\3\2\2\2\u0351\u034a\3\2\2\2\u0351")
        buf.write("\u034e\3\2\2\2\u0351\u0352\3\2\2\2\u0352\u0353\3\2\2\2")
        buf.write("\u0353\u0354\5\u00efx\2\u0354\u00dc\3\2\2\2\u0355\u035a")
        buf.write("\5\u00dfp\2\u0356\u035a\5\u00e1q\2\u0357\u035a\5\u00e3")
        buf.write("r\2\u0358\u035a\5\u00e5s\2\u0359\u0355\3\2\2\2\u0359\u0356")
        buf.write("\3\2\2\2\u0359\u0357\3\2\2\2\u0359\u0358\3\2\2\2\u035a")
        buf.write("\u00de\3\2\2\2\u035b\u035f\5\u00f3z\2\u035c\u035e\5\u00f5")
        buf.write("{\2\u035d\u035c\3\2\2\2\u035e\u0361\3\2\2\2\u035f\u035d")
        buf.write("\3\2\2\2\u035f\u0360\3\2\2\2\u0360\u0368\3\2\2\2\u0361")
        buf.write("\u035f\3\2\2\2\u0362\u0364\7\62\2\2\u0363\u0362\3\2\2")
        buf.write("\2\u0364\u0365\3\2\2\2\u0365\u0363\3\2\2\2\u0365\u0366")
        buf.write("\3\2\2\2\u0366\u0368\3\2\2\2\u0367\u035b\3\2\2\2\u0367")
        buf.write("\u0363\3\2\2\2\u0368\u00e0\3\2\2\2\u0369\u036a\7\62\2")
        buf.write("\2\u036a\u036c\t\6\2\2\u036b\u036d\5\u00f7|\2\u036c\u036b")
        buf.write("\3\2\2\2\u036d\u036e\3\2\2\2\u036e\u036c\3\2\2\2\u036e")
        buf.write("\u036f\3\2\2\2\u036f\u00e2\3\2\2\2\u0370\u0371\7\62\2")
        buf.write("\2\u0371\u0373\t\7\2\2\u0372\u0374\5\u00f9}\2\u0373\u0372")
        buf.write("\3\2\2\2\u0374\u0375\3\2\2\2\u0375\u0373\3\2\2\2\u0375")
        buf.write("\u0376\3\2\2\2\u0376\u00e4\3\2\2\2\u0377\u0378\7\62\2")
        buf.write("\2\u0378\u037a\t\b\2\2\u0379\u037b\5\u00fb~\2\u037a\u0379")
        buf.write("\3\2\2\2\u037b\u037c\3\2\2\2\u037c\u037a\3\2\2\2\u037c")
        buf.write("\u037d\3\2\2\2\u037d\u00e6\3\2\2\2\u037e\u0381\5\u00fd")
        buf.write("\177\2\u037f\u0381\5\u00ff\u0080\2\u0380\u037e\3\2\2\2")
        buf.write("\u0380\u037f\3\2\2\2\u0381\u00e8\3\2\2\2\u0382\u0383\6")
        buf.write("u\2\2\u0383\u038f\5\u010d\u0087\2\u0384\u0386\7\17\2\2")
        buf.write("\u0385\u0384\3\2\2\2\u0385\u0386\3\2\2\2\u0386\u0387\3")
        buf.write("\2\2\2\u0387\u038a\7\f\2\2\u0388\u038a\4\16\17\2\u0389")
        buf.write("\u0385\3\2\2\2\u0389\u0388\3\2\2\2\u038a\u038c\3\2\2\2")
        buf.write("\u038b\u038d\5\u010d\u0087\2\u038c\u038b\3\2\2\2\u038c")
        buf.write("\u038d\3\2\2\2\u038d\u038f\3\2\2\2\u038e\u0382\3\2\2\2")
        buf.write("\u038e\u0389\3\2\2\2\u038f\u0390\3\2\2\2\u0390\u0391\b")
        buf.write("u\n\2\u0391\u00ea\3\2\2\2\u0392\u0396\5\u010d\u0087\2")
        buf.write("\u0393\u0396\5\u010f\u0088\2\u0394\u0396\5\u0111\u0089")
        buf.write("\2\u0395\u0392\3\2\2\2\u0395\u0393\3\2\2\2\u0395\u0394")
        buf.write("\3\2\2\2\u0396\u0397\3\2\2\2\u0397\u0398\bv\3\2\u0398")
        buf.write("\u00ec\3\2\2\2\u0399\u039a\13\2\2\2\u039a\u00ee\3\2\2")
        buf.write("\2\u039b\u03a0\7)\2\2\u039c\u039f\5\u00f1y\2\u039d\u039f")
        buf.write("\n\t\2\2\u039e\u039c\3\2\2\2\u039e\u039d\3\2\2\2\u039f")
        buf.write("\u03a2\3\2\2\2\u03a0\u039e\3\2\2\2\u03a0\u03a1\3\2\2\2")
        buf.write("\u03a1\u03a3\3\2\2\2\u03a2\u03a0\3\2\2\2\u03a3\u03ae\7")
        buf.write(")\2\2\u03a4\u03a9\7$\2\2\u03a5\u03a8\5\u00f1y\2\u03a6")
        buf.write("\u03a8\n\n\2\2\u03a7\u03a5\3\2\2\2\u03a7\u03a6\3\2\2\2")
        buf.write("\u03a8\u03ab\3\2\2\2\u03a9\u03a7\3\2\2\2\u03a9\u03aa\3")
        buf.write("\2\2\2\u03aa\u03ac\3\2\2\2\u03ab\u03a9\3\2\2\2\u03ac\u03ae")
        buf.write("\7$\2\2\u03ad\u039b\3\2\2\2\u03ad\u03a4\3\2\2\2\u03ae")
        buf.write("\u00f0\3\2\2\2\u03af\u03b0\7^\2\2\u03b0\u03b4\13\2\2\2")
        buf.write("\u03b1\u03b2\7^\2\2\u03b2\u03b4\5\u00e9u\2\u03b3\u03af")
        buf.write("\3\2\2\2\u03b3\u03b1\3\2\2\2\u03b4\u00f2\3\2\2\2\u03b5")
        buf.write("\u03b6\4\63;\2\u03b6\u00f4\3\2\2\2\u03b7\u03b8\4\62;\2")
        buf.write("\u03b8\u00f6\3\2\2\2\u03b9\u03ba\4\629\2\u03ba\u00f8\3")
        buf.write("\2\2\2\u03bb\u03be\5\u00f5{\2\u03bc\u03be\t\13\2\2\u03bd")
        buf.write("\u03bb\3\2\2\2\u03bd\u03bc\3\2\2\2\u03be\u00fa\3\2\2\2")
        buf.write("\u03bf\u03c0\4\62\63\2\u03c0\u00fc\3\2\2\2\u03c1\u03c3")
        buf.write("\5\u0101\u0081\2\u03c2\u03c1\3\2\2\2\u03c2\u03c3\3\2\2")
        buf.write("\2\u03c3\u03c4\3\2\2\2\u03c4\u03c9\5\u0103\u0082\2\u03c5")
        buf.write("\u03c6\5\u0101\u0081\2\u03c6\u03c7\7\60\2\2\u03c7\u03c9")
        buf.write("\3\2\2\2\u03c8\u03c2\3\2\2\2\u03c8\u03c5\3\2\2\2\u03c9")
        buf.write("\u00fe\3\2\2\2\u03ca\u03cd\5\u0101\u0081\2\u03cb\u03cd")
        buf.write("\5\u00fd\177\2\u03cc\u03ca\3\2\2\2\u03cc\u03cb\3\2\2\2")
        buf.write("\u03cd\u03ce\3\2\2\2\u03ce\u03cf\5\u0105\u0083\2\u03cf")
        buf.write("\u0100\3\2\2\2\u03d0\u03d2\5\u00f5{\2\u03d1\u03d0\3\2")
        buf.write("\2\2\u03d2\u03d3\3\2\2\2\u03d3\u03d1\3\2\2\2\u03d3\u03d4")
        buf.write("\3\2\2\2\u03d4\u0102\3\2\2\2\u03d5\u03d7\7\60\2\2\u03d6")
        buf.write("\u03d8\5\u00f5{\2\u03d7\u03d6\3\2\2\2\u03d8\u03d9\3\2")
        buf.write("\2\2\u03d9\u03d7\3\2\2\2\u03d9\u03da\3\2\2\2\u03da\u0104")
        buf.write("\3\2\2\2\u03db\u03dd\t\f\2\2\u03dc\u03de\t\r\2\2\u03dd")
        buf.write("\u03dc\3\2\2\2\u03dd\u03de\3\2\2\2\u03de\u03e0\3\2\2\2")
        buf.write("\u03df\u03e1\5\u00f5{\2\u03e0\u03df\3\2\2\2\u03e1\u03e2")
        buf.write("\3\2\2\2\u03e2\u03e0\3\2\2\2\u03e2\u03e3\3\2\2\2\u03e3")
        buf.write("\u0106\3\2\2\2\u03e4\u03e7\5w<\2\u03e5\u03e7\5\u010b\u0086")
        buf.write("\2\u03e6\u03e4\3\2\2\2\u03e6\u03e5\3\2\2\2\u03e7\u0108")
        buf.write("\3\2\2\2\u03e8\u03eb\5\u0107\u0084\2\u03e9\u03eb\5\u00f5")
        buf.write("{\2\u03ea\u03e8\3\2\2\2\u03ea\u03e9\3\2\2\2\u03eb\u010a")
        buf.write("\3\2\2\2\u03ec\u03ed\t\16\2\2\u03ed\u010c\3\2\2\2\u03ee")
        buf.write("\u03f0\t\17\2\2\u03ef\u03ee\3\2\2\2\u03f0\u03f1\3\2\2")
        buf.write("\2\u03f1\u03ef\3\2\2\2\u03f1\u03f2\3\2\2\2\u03f2\u010e")
        buf.write("\3\2\2\2\u03f3\u03f7\7%\2\2\u03f4\u03f6\n\20\2\2\u03f5")
        buf.write("\u03f4\3\2\2\2\u03f6\u03f9\3\2\2\2\u03f7\u03f5\3\2\2\2")
        buf.write("\u03f7\u03f8\3\2\2\2\u03f8\u0110\3\2\2\2\u03f9\u03f7\3")
        buf.write("\2\2\2\u03fa\u03fc\7^\2\2\u03fb\u03fd\5\u010d\u0087\2")
        buf.write("\u03fc\u03fb\3\2\2\2\u03fc\u03fd\3\2\2\2\u03fd\u0403\3")
        buf.write("\2\2\2\u03fe\u0400\7\17\2\2\u03ff\u03fe\3\2\2\2\u03ff")
        buf.write("\u0400\3\2\2\2\u0400\u0401\3\2\2\2\u0401\u0404\7\f\2\2")
        buf.write("\u0402\u0404\4\16\17\2\u0403\u03ff\3\2\2\2\u0403\u0402")
        buf.write("\3\2\2\2\u0404\u0112\3\2\2\2\64\2\u0134\u015a\u01b3\u01bf")
        buf.write("\u0211\u022f\u023a\u023c\u0271\u0273\u033c\u0342\u034a")
        buf.write("\u034e\u0351\u0359\u035f\u0365\u0367\u036e\u0375\u037c")
        buf.write("\u0380\u0385\u0389\u038c\u038e\u0395\u039e\u03a0\u03a7")
        buf.write("\u03a9\u03ad\u03b3\u03bd\u03c2\u03c8\u03cc\u03d3\u03d9")
        buf.write("\u03dd\u03e2\u03e6\u03ea\u03f1\u03f7\u03fc\u03ff\u0403")
        buf.write("\13\3*\2\b\2\2\3R\3\3S\4\3T\5\3U\6\3V\7\3W\b\3u\t")
        return buf.getvalue()


class YarcLexer(YarcLexerBase):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = [
        "<INVALID>",
        "'scenario'",
        "'settings'",
        "'writer'",
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
        "'set'",
        "'translate'",
        "'rotate'",
        "'scale'",
        "'semantics'",
        "'visible'",
        "'size'",
        "'look_at'",
        "'up_axis'",
        "'scatter'",
        "'around'",
        "'texture'",
        "'every'",
        "'Uniform'",
        "'Normal'",
        "'Choice'",
        "'Sequence'",
        "'LogUniform'",
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

    ruleNames = [
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
        "NESTED_CODE",
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
            actions[40] = self.SNIPPET_action
            actions[80] = self.LPAREN_action
            actions[81] = self.RPAREN_action
            actions[82] = self.LBRACK_action
            actions[83] = self.RBRACK_action
            actions[84] = self.LBRACE_action
            actions[85] = self.RBRACE_action
            actions[115] = self.NEWLINE_action
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
            preds[115] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx: RuleContext, predIndex: int):
        if predIndex == 0:
            return self.atStartOfInput()
