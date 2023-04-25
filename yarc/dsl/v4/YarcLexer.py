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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2x")
        buf.write("\u03fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\t\u0087\4\u0088\t\u0088\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0156\n\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0212")
        buf.write('\n \3!\3!\3!\3!\3!\3!\3!\3"\3"\3"\3"\3"\3"\3"\3')
        buf.write('"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u0230\n$')
        buf.write("\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u023b\n%\5%\u023d\n%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3'\3'\3'\3'\3'\3'\3'\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\7")
        buf.write(",\u0272\n,\f,\16,\u0275\13,\3,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\39\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3M\3M\3N\3N\3")
        buf.write("O\3O\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3")
        buf.write("U\3V\3V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3[\3\\")
        buf.write("\3\\\3\\\3]\3]\3]\3^\3^\3^\3_\3_\3_\3`\3`\3`\3a\3a\3a")
        buf.write("\3b\3b\3b\3c\3c\3c\3d\3d\3d\3e\3e\3e\3f\3f\3f\3g\3g\3")
        buf.write("g\3g\3h\3h\3h\3h\3i\3i\3i\3i\3j\3j\3j\3j\3k\3k\7k\u033d")
        buf.write("\nk\fk\16k\u0340\13k\3l\3l\3l\3m\3m\5m\u0347\nm\3m\3m")
        buf.write("\5m\u034b\nm\3m\5m\u034e\nm\3m\3m\3n\3n\3n\3n\5n\u0356")
        buf.write("\nn\3o\3o\7o\u035a\no\fo\16o\u035d\13o\3o\6o\u0360\no")
        buf.write("\ro\16o\u0361\5o\u0364\no\3p\3p\3p\6p\u0369\np\rp\16p")
        buf.write("\u036a\3q\3q\3q\6q\u0370\nq\rq\16q\u0371\3r\3r\3r\6r\u0377")
        buf.write("\nr\rr\16r\u0378\3s\3s\5s\u037d\ns\3t\5t\u0380\nt\3t\3")
        buf.write("t\5t\u0384\nt\3t\5t\u0387\nt\3t\3t\3u\3u\3u\5u\u038e\n")
        buf.write("u\3u\3u\3v\3v\3w\3w\3w\7w\u0397\nw\fw\16w\u039a\13w\3")
        buf.write("w\3w\3w\3w\7w\u03a0\nw\fw\16w\u03a3\13w\3w\5w\u03a6\n")
        buf.write("w\3x\3x\3x\3x\5x\u03ac\nx\3y\3y\3z\3z\3{\3{\3|\3|\5|\u03b6")
        buf.write("\n|\3}\3}\3~\5~\u03bb\n~\3~\3~\3~\3~\5~\u03c1\n~\3\177")
        buf.write("\3\177\5\177\u03c5\n\177\3\177\3\177\3\u0080\6\u0080\u03ca")
        buf.write("\n\u0080\r\u0080\16\u0080\u03cb\3\u0081\3\u0081\6\u0081")
        buf.write("\u03d0\n\u0081\r\u0081\16\u0081\u03d1\3\u0082\3\u0082")
        buf.write("\5\u0082\u03d6\n\u0082\3\u0082\6\u0082\u03d9\n\u0082\r")
        buf.write("\u0082\16\u0082\u03da\3\u0083\3\u0083\5\u0083\u03df\n")
        buf.write("\u0083\3\u0084\3\u0084\5\u0084\u03e3\n\u0084\3\u0085\3")
        buf.write("\u0085\3\u0086\6\u0086\u03e8\n\u0086\r\u0086\16\u0086")
        buf.write("\u03e9\3\u0087\3\u0087\7\u0087\u03ee\n\u0087\f\u0087\16")
        buf.write("\u0087\u03f1\13\u0087\3\u0088\3\u0088\5\u0088\u03f5\n")
        buf.write("\u0088\3\u0088\5\u0088\u03f8\n\u0088\3\u0088\3\u0088\5")
        buf.write("\u0088\u03fc\n\u0088\3\u0273\2\u0089\3\5\5\6\7\7\t\b\13")
        buf.write("\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35\22\37")
        buf.write("\23!\24#\25%\26'\27)\30+\31-\32/\33\61\34\63\35\65\36")
        buf.write("\67\379 ;!=\"?#A$C%E&G'I(K)M*O+Q,S-U.W\2Y/[\60]\61_\62")
        buf.write("a\63c\64e\65g\66i\67k8m9o:q;s<u=w>y?{@}A\177B\u0081C\u0083")
        buf.write("D\u0085E\u0087F\u0089G\u008bH\u008dI\u008fJ\u0091K\u0093")
        buf.write("L\u0095M\u0097N\u0099O\u009bP\u009dQ\u009fR\u00a1S\u00a3")
        buf.write("T\u00a5U\u00a7V\u00a9W\u00abX\u00adY\u00afZ\u00b1[\u00b3")
        buf.write("\\\u00b5]\u00b7^\u00b9_\u00bb`\u00bda\u00bfb\u00c1c\u00c3")
        buf.write("d\u00c5e\u00c7f\u00c9g\u00cbh\u00cdi\u00cfj\u00d1k\u00d3")
        buf.write("l\u00d5m\u00d7n\u00d9o\u00dbp\u00ddq\u00dfr\u00e1s\u00e3")
        buf.write("t\u00e5u\u00e7v\u00e9w\u00ebx\u00ed\2\u00ef\2\u00f1\2")
        buf.write("\u00f3\2\u00f5\2\u00f7\2\u00f9\2\u00fb\2\u00fd\2\u00ff")
        buf.write("\2\u0101\2\u0103\2\u0105\2\u0107\2\u0109\2\u010b\2\u010d")
        buf.write("\2\u010f\2\3\2\21\4\2Z\\z|\4\2WWww\4\2HHhh\4\2TTtt\4\2")
        buf.write("QQqq\4\2ZZzz\4\2DDdd\6\2\f\f\16\17))^^\6\2\f\f\16\17$")
        buf.write('$^^\4\2CHch\4\2GGgg\4\2--//\4\2C\\c|\4\2\13\13""\4\2')
        buf.write("\f\f\16\17\2\u041f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
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
        buf.write("\3\2\2\2\3\u0111\3\2\2\2\5\u011a\3\2\2\2\7\u0123\3\2\2")
        buf.write("\2\t\u0129\3\2\2\2\13\u0155\3\2\2\2\r\u0157\3\2\2\2\17")
        buf.write("\u015e\3\2\2\2\21\u0164\3\2\2\2\23\u016b\3\2\2\2\25\u0174")
        buf.write("\3\2\2\2\27\u017d\3\2\2\2\31\u0182\3\2\2\2\33\u0189\3")
        buf.write("\2\2\2\35\u018f\3\2\2\2\37\u019b\3\2\2\2!\u019f\3\2\2")
        buf.write("\2#\u01a4\3\2\2\2%\u01aa\3\2\2\2'\u01b0\3\2\2\2)\u01ba")
        buf.write("\3\2\2\2+\u01cb\3\2\2\2-\u01d2\3\2\2\2/\u01d8\3\2\2\2")
        buf.write("\61\u01e2\3\2\2\2\63\u01ea\3\2\2\2\65\u01ef\3\2\2\2\67")
        buf.write("\u01f7\3\2\2\29\u01ff\3\2\2\2;\u0201\3\2\2\2=\u0205\3")
        buf.write("\2\2\2?\u0211\3\2\2\2A\u0213\3\2\2\2C\u021a\3\2\2\2E\u0222")
        buf.write("\3\2\2\2G\u0228\3\2\2\2I\u0231\3\2\2\2K\u023e\3\2\2\2")
        buf.write("M\u0246\3\2\2\2O\u024d\3\2\2\2Q\u0254\3\2\2\2S\u025d\3")
        buf.write("\2\2\2U\u0268\3\2\2\2W\u026d\3\2\2\2Y\u0279\3\2\2\2[\u027c")
        buf.write("\3\2\2\2]\u027f\3\2\2\2_\u0282\3\2\2\2a\u0286\3\2\2\2")
        buf.write("c\u028a\3\2\2\2e\u028f\3\2\2\2g\u0295\3\2\2\2i\u0299\3")
        buf.write("\2\2\2k\u029e\3\2\2\2m\u02a1\3\2\2\2o\u02a4\3\2\2\2q\u02a7")
        buf.write("\3\2\2\2s\u02ac\3\2\2\2u\u02b0\3\2\2\2w\u02b3\3\2\2\2")
        buf.write("y\u02ba\3\2\2\2{\u02bf\3\2\2\2}\u02c1\3\2\2\2\177\u02c3")
        buf.write("\3\2\2\2\u0081\u02c6\3\2\2\2\u0083\u02ca\3\2\2\2\u0085")
        buf.write("\u02cc\3\2\2\2\u0087\u02ce\3\2\2\2\u0089\u02d0\3\2\2\2")
        buf.write("\u008b\u02d2\3\2\2\2\u008d\u02d4\3\2\2\2\u008f\u02d6\3")
        buf.write("\2\2\2\u0091\u02d8\3\2\2\2\u0093\u02da\3\2\2\2\u0095\u02dd")
        buf.write("\3\2\2\2\u0097\u02e0\3\2\2\2\u0099\u02e2\3\2\2\2\u009b")
        buf.write("\u02e4\3\2\2\2\u009d\u02e6\3\2\2\2\u009f\u02e8\3\2\2\2")
        buf.write("\u00a1\u02ea\3\2\2\2\u00a3\u02ed\3\2\2\2\u00a5\u02f0\3")
        buf.write("\2\2\2\u00a7\u02f3\3\2\2\2\u00a9\u02f6\3\2\2\2\u00ab\u02f9")
        buf.write("\3\2\2\2\u00ad\u02fc\3\2\2\2\u00af\u02ff\3\2\2\2\u00b1")
        buf.write("\u0302\3\2\2\2\u00b3\u0304\3\2\2\2\u00b5\u0306\3\2\2\2")
        buf.write("\u00b7\u0309\3\2\2\2\u00b9\u030c\3\2\2\2\u00bb\u030f\3")
        buf.write("\2\2\2\u00bd\u0312\3\2\2\2\u00bf\u0315\3\2\2\2\u00c1\u0318")
        buf.write("\3\2\2\2\u00c3\u031b\3\2\2\2\u00c5\u031e\3\2\2\2\u00c7")
        buf.write("\u0321\3\2\2\2\u00c9\u0324\3\2\2\2\u00cb\u0327\3\2\2\2")
        buf.write("\u00cd\u032a\3\2\2\2\u00cf\u032e\3\2\2\2\u00d1\u0332\3")
        buf.write("\2\2\2\u00d3\u0336\3\2\2\2\u00d5\u033a\3\2\2\2\u00d7\u0341")
        buf.write("\3\2\2\2\u00d9\u034d\3\2\2\2\u00db\u0355\3\2\2\2\u00dd")
        buf.write("\u0363\3\2\2\2\u00df\u0365\3\2\2\2\u00e1\u036c\3\2\2\2")
        buf.write("\u00e3\u0373\3\2\2\2\u00e5\u037c\3\2\2\2\u00e7\u0383\3")
        buf.write("\2\2\2\u00e9\u038d\3\2\2\2\u00eb\u0391\3\2\2\2\u00ed\u03a5")
        buf.write("\3\2\2\2\u00ef\u03ab\3\2\2\2\u00f1\u03ad\3\2\2\2\u00f3")
        buf.write("\u03af\3\2\2\2\u00f5\u03b1\3\2\2\2\u00f7\u03b5\3\2\2\2")
        buf.write("\u00f9\u03b7\3\2\2\2\u00fb\u03c0\3\2\2\2\u00fd\u03c4\3")
        buf.write("\2\2\2\u00ff\u03c9\3\2\2\2\u0101\u03cd\3\2\2\2\u0103\u03d3")
        buf.write("\3\2\2\2\u0105\u03de\3\2\2\2\u0107\u03e2\3\2\2\2\u0109")
        buf.write("\u03e4\3\2\2\2\u010b\u03e7\3\2\2\2\u010d\u03eb\3\2\2\2")
        buf.write("\u010f\u03f2\3\2\2\2\u0111\u0112\7u\2\2\u0112\u0113\7")
        buf.write("e\2\2\u0113\u0114\7g\2\2\u0114\u0115\7p\2\2\u0115\u0116")
        buf.write("\7c\2\2\u0116\u0117\7t\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\4\3\2\2\2\u011a\u011b\7u\2\2\u011b\u011c")
        buf.write("\7g\2\2\u011c\u011d\7v\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7k\2\2\u011f\u0120\7p\2\2\u0120\u0121\7i\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122\6\3\2\2\2\u0123\u0124\7u\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7c\2\2\u0126\u0127\7i\2\2\u0127\u0128")
        buf.write("\7g\2\2\u0128\b\3\2\2\2\u0129\u012a\7y\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\u012c\7k\2\2\u012c\u012d\7v\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e\u012f\7t\2\2\u012f\u0130\7u\2\2\u0130\n")
        buf.write("\3\2\2\2\u0131\u0132\7R\2\2\u0132\u0133\7n\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7p\2\2\u0135\u0156\7g\2\2\u0136\u0137")
        buf.write("\7E\2\2\u0137\u0138\7w\2\2\u0138\u0139\7d\2\2\u0139\u0156")
        buf.write("\7g\2\2\u013a\u013b\7U\2\2\u013b\u013c\7r\2\2\u013c\u013d")
        buf.write("\7j\2\2\u013d\u013e\7g\2\2\u013e\u013f\7t\2\2\u013f\u0156")
        buf.write("\7g\2\2\u0140\u0141\7E\2\2\u0141\u0142\7{\2\2\u0142\u0143")
        buf.write("\7n\2\2\u0143\u0144\7k\2\2\u0144\u0145\7p\2\2\u0145\u0146")
        buf.write("\7f\2\2\u0146\u0147\7g\2\2\u0147\u0156\7t\2\2\u0148\u0149")
        buf.write("\7E\2\2\u0149\u014a\7q\2\2\u014a\u014b\7p\2\2\u014b\u0156")
        buf.write("\7g\2\2\u014c\u014d\7V\2\2\u014d\u014e\7q\2\2\u014e\u014f")
        buf.write("\7t\2\2\u014f\u0150\7w\2\2\u0150\u0156\7u\2\2\u0151\u0152")
        buf.write("\7F\2\2\u0152\u0153\7k\2\2\u0153\u0154\7u\2\2\u0154\u0156")
        buf.write("\7m\2\2\u0155\u0131\3\2\2\2\u0155\u0136\3\2\2\2\u0155")
        buf.write("\u013a\3\2\2\2\u0155\u0140\3\2\2\2\u0155\u0148\3\2\2\2")
        buf.write("\u0155\u014c\3\2\2\2\u0155\u0151\3\2\2\2\u0156\f\3\2\2")
        buf.write("\2\u0157\u0158\7E\2\2\u0158\u0159\7c\2\2\u0159\u015a\7")
        buf.write("o\2\2\u015a\u015b\7g\2\2\u015b\u015c\7t\2\2\u015c\u015d")
        buf.write("\7c\2\2\u015d\16\3\2\2\2\u015e\u015f\7N\2\2\u015f\u0160")
        buf.write("\7k\2\2\u0160\u0161\7i\2\2\u0161\u0162\7j\2\2\u0162\u0163")
        buf.write("\7v\2\2\u0163\20\3\2\2\2\u0164\u0165\7U\2\2\u0165\u0166")
        buf.write("\7v\2\2\u0166\u0167\7g\2\2\u0167\u0168\7t\2\2\u0168\u0169")
        buf.write("\7g\2\2\u0169\u016a\7q\2\2\u016a\22\3\2\2\2\u016b\u016c")
        buf.write("\7O\2\2\u016c\u016d\7c\2\2\u016d\u016e\7v\2\2\u016e\u016f")
        buf.write("\7g\2\2\u016f\u0170\7t\2\2\u0170\u0171\7k\2\2\u0171\u0172")
        buf.write("\7c\2\2\u0172\u0173\7n\2\2\u0173\24\3\2\2\2\u0174\u0175")
        buf.write("\7V\2\2\u0175\u0176\7k\2\2\u0176\u0177\7o\2\2\u0177\u0178")
        buf.write("\7g\2\2\u0178\u0179\7n\2\2\u0179\u017a\7k\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017b\u017c\7g\2\2\u017c\26\3\2\2\2\u017d\u017e")
        buf.write("\7q\2\2\u017e\u017f\7r\2\2\u017f\u0180\7g\2\2\u0180\u0181")
        buf.write("\7p\2\2\u0181\30\3\2\2\2\u0182\u0183\7e\2\2\u0183\u0184")
        buf.write("\7t\2\2\u0184\u0185\7g\2\2\u0185\u0186\7c\2\2\u0186\u0187")
        buf.write("\7v\2\2\u0187\u0188\7g\2\2\u0188\32\3\2\2\2\u0189\u018a")
        buf.write("\7i\2\2\u018a\u018b\7t\2\2\u018b\u018c\7q\2\2\u018c\u018d")
        buf.write("\7w\2\2\u018d\u018e\7r\2\2\u018e\34\3\2\2\2\u018f\u0190")
        buf.write("\7k\2\2\u0190\u0191\7p\2\2\u0191\u0192\7u\2\2\u0192\u0193")
        buf.write("\7v\2\2\u0193\u0194\7c\2\2\u0194\u0195\7p\2\2\u0195\u0196")
        buf.write("\7v\2\2\u0196\u0197\7k\2\2\u0197\u0198\7c\2\2\u0198\u0199")
        buf.write("\7v\2\2\u0199\u019a\7g\2\2\u019a\36\3\2\2\2\u019b\u019c")
        buf.write("\7i\2\2\u019c\u019d\7g\2\2\u019d\u019e\7v\2\2\u019e \3")
        buf.write("\2\2\2\u019f\u01a0\7g\2\2\u01a0\u01a1\7f\2\2\u01a1\u01a2")
        buf.write('\7k\2\2\u01a2\u01a3\7v\2\2\u01a3"\3\2\2\2\u01a4\u01a5')
        buf.write("\7h\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8")
        buf.write("\7e\2\2\u01a8\u01a9\7j\2\2\u01a9$\3\2\2\2\u01aa\u01ab")
        buf.write("\7o\2\2\u01ab\u01ac\7c\2\2\u01ac\u01ad\7v\2\2\u01ad\u01ae")
        buf.write("\7e\2\2\u01ae\u01af\7j\2\2\u01af&\3\2\2\2\u01b0\u01b1")
        buf.write("\7v\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3\7c\2\2\u01b3\u01b4")
        buf.write("\7p\2\2\u01b4\u01b5\7u\2\2\u01b5\u01b6\7n\2\2\u01b6\u01b7")
        buf.write("\7c\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9\7g\2\2\u01b9(\3")
        buf.write("\2\2\2\u01ba\u01bb\7e\2\2\u01bb\u01bc\7c\2\2\u01bc\u01bd")
        buf.write("\7o\2\2\u01bd\u01be\7g\2\2\u01be\u01bf\7t\2\2\u01bf\u01c0")
        buf.write("\7c\2\2\u01c0\u01c1\7a\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3")
        buf.write("\7t\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5\7p\2\2\u01c5\u01c6")
        buf.write("\7u\2\2\u01c6\u01c7\7n\2\2\u01c7\u01c8\7c\2\2\u01c8\u01c9")
        buf.write("\7v\2\2\u01c9\u01ca\7g\2\2\u01ca*\3\2\2\2\u01cb\u01cc")
        buf.write("\7t\2\2\u01cc\u01cd\7q\2\2\u01cd\u01ce\7v\2\2\u01ce\u01cf")
        buf.write("\7c\2\2\u01cf\u01d0\7v\2\2\u01d0\u01d1\7g\2\2\u01d1,\3")
        buf.write("\2\2\2\u01d2\u01d3\7u\2\2\u01d3\u01d4\7e\2\2\u01d4\u01d5")
        buf.write("\7c\2\2\u01d5\u01d6\7n\2\2\u01d6\u01d7\7g\2\2\u01d7.\3")
        buf.write("\2\2\2\u01d8\u01d9\7u\2\2\u01d9\u01da\7g\2\2\u01da\u01db")
        buf.write("\7o\2\2\u01db\u01dc\7c\2\2\u01dc\u01dd\7p\2\2\u01dd\u01de")
        buf.write("\7v\2\2\u01de\u01df\7k\2\2\u01df\u01e0\7e\2\2\u01e0\u01e1")
        buf.write("\7u\2\2\u01e1\60\3\2\2\2\u01e2\u01e3\7x\2\2\u01e3\u01e4")
        buf.write("\7k\2\2\u01e4\u01e5\7u\2\2\u01e5\u01e6\7k\2\2\u01e6\u01e7")
        buf.write("\7d\2\2\u01e7\u01e8\7n\2\2\u01e8\u01e9\7g\2\2\u01e9\62")
        buf.write("\3\2\2\2\u01ea\u01eb\7u\2\2\u01eb\u01ec\7k\2\2\u01ec\u01ed")
        buf.write("\7|\2\2\u01ed\u01ee\7g\2\2\u01ee\64\3\2\2\2\u01ef\u01f0")
        buf.write("\7n\2\2\u01f0\u01f1\7q\2\2\u01f1\u01f2\7q\2\2\u01f2\u01f3")
        buf.write("\7m\2\2\u01f3\u01f4\7a\2\2\u01f4\u01f5\7c\2\2\u01f5\u01f6")
        buf.write("\7v\2\2\u01f6\66\3\2\2\2\u01f7\u01f8\7w\2\2\u01f8\u01f9")
        buf.write("\7r\2\2\u01f9\u01fa\7a\2\2\u01fa\u01fb\7c\2\2\u01fb\u01fc")
        buf.write("\7z\2\2\u01fc\u01fd\7k\2\2\u01fd\u01fe\7u\2\2\u01fe8\3")
        buf.write("\2\2\2\u01ff\u0200\t\2\2\2\u0200:\3\2\2\2\u0201\u0202")
        buf.write("\59\35\2\u0202\u0203\59\35\2\u0203\u0204\59\35\2\u0204")
        buf.write("<\3\2\2\2\u0205\u0206\7u\2\2\u0206\u0207\7e\2\2\u0207")
        buf.write("\u0208\7c\2\2\u0208\u0209\7v\2\2\u0209\u020a\7v\2\2\u020a")
        buf.write("\u020b\7g\2\2\u020b\u020c\7t\2\2\u020c>\3\2\2\2\u020d")
        buf.write("\u020e\7\64\2\2\u020e\u0212\7f\2\2\u020f\u0210\7\65\2")
        buf.write("\2\u0210\u0212\7f\2\2\u0211\u020d\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0212@\3\2\2\2\u0213\u0214\7c\2\2\u0214\u0215")
        buf.write("\7t\2\2\u0215\u0216\7q\2\2\u0216\u0217\7w\2\2\u0217\u0218")
        buf.write("\7p\2\2\u0218\u0219\7f\2\2\u0219B\3\2\2\2\u021a\u021b")
        buf.write("\7v\2\2\u021b\u021c\7g\2\2\u021c\u021d\7z\2\2\u021d\u021e")
        buf.write("\7v\2\2\u021e\u021f\7w\2\2\u021f\u0220\7t\2\2\u0220\u0221")
        buf.write("\7g\2\2\u0221D\3\2\2\2\u0222\u0223\7g\2\2\u0223\u0224")
        buf.write("\7x\2\2\u0224\u0225\7g\2\2\u0225\u0226\7t\2\2\u0226\u0227")
        buf.write("\7{\2\2\u0227F\3\2\2\2\u0228\u0229\7h\2\2\u0229\u022a")
        buf.write("\7t\2\2\u022a\u022b\7c\2\2\u022b\u022c\7o\2\2\u022c\u022d")
        buf.write("\7g\2\2\u022d\u022f\3\2\2\2\u022e\u0230\7u\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u022f\u0230\3\2\2\2\u0230H\3\2\2\2\u0231\u0232")
        buf.write("\7u\2\2\u0232\u0233\7g\2\2\u0233\u0234\7e\2\2\u0234\u023c")
        buf.write("\3\2\2\2\u0235\u0236\7q\2\2\u0236\u0237\7p\2\2\u0237\u0238")
        buf.write("\7f\2\2\u0238\u023a\3\2\2\2\u0239\u023b\7u\2\2\u023a\u0239")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023d\3\2\2\2\u023c")
        buf.write("\u0235\3\2\2\2\u023c\u023d\3\2\2\2\u023dJ\3\2\2\2\u023e")
        buf.write("\u023f\7W\2\2\u023f\u0240\7p\2\2\u0240\u0241\7k\2\2\u0241")
        buf.write("\u0242\7h\2\2\u0242\u0243\7q\2\2\u0243\u0244\7t\2\2\u0244")
        buf.write("\u0245\7o\2\2\u0245L\3\2\2\2\u0246\u0247\7P\2\2\u0247")
        buf.write("\u0248\7q\2\2\u0248\u0249\7t\2\2\u0249\u024a\7o\2\2\u024a")
        buf.write("\u024b\7c\2\2\u024b\u024c\7n\2\2\u024cN\3\2\2\2\u024d")
        buf.write("\u024e\7E\2\2\u024e\u024f\7j\2\2\u024f\u0250\7q\2\2\u0250")
        buf.write("\u0251\7k\2\2\u0251\u0252\7e\2\2\u0252\u0253\7g\2\2\u0253")
        buf.write("P\3\2\2\2\u0254\u0255\7U\2\2\u0255\u0256\7g\2\2\u0256")
        buf.write("\u0257\7s\2\2\u0257\u0258\7w\2\2\u0258\u0259\7g\2\2\u0259")
        buf.write("\u025a\7p\2\2\u025a\u025b\7e\2\2\u025b\u025c\7g\2\2\u025c")
        buf.write("R\3\2\2\2\u025d\u025e\7N\2\2\u025e\u025f\7q\2\2\u025f")
        buf.write("\u0260\7i\2\2\u0260\u0261\7W\2\2\u0261\u0262\7p\2\2\u0262")
        buf.write("\u0263\7k\2\2\u0263\u0264\7h\2\2\u0264\u0265\7q\2\2\u0265")
        buf.write("\u0266\7t\2\2\u0266\u0267\7o\2\2\u0267T\3\2\2\2\u0268")
        buf.write("\u0269\5W,\2\u0269\u026a\b+\2\2\u026a\u026b\3\2\2\2\u026b")
        buf.write("\u026c\b+\3\2\u026cV\3\2\2\2\u026d\u026e\5\u00adW\2\u026e")
        buf.write("\u0273\5\u00adW\2\u026f\u0272\5W,\2\u0270\u0272\13\2\2")
        buf.write("\2\u0271\u026f\3\2\2\2\u0271\u0270\3\2\2\2\u0272\u0275")
        buf.write("\3\2\2\2\u0273\u0274\3\2\2\2\u0273\u0271\3\2\2\2\u0274")
        buf.write("\u0276\3\2\2\2\u0275\u0273\3\2\2\2\u0276\u0277\5\u00af")
        buf.write("X\2\u0277\u0278\5\u00afX\2\u0278X\3\2\2\2\u0279\u027a")
        buf.write("\7v\2\2\u027a\u027b\7q\2\2\u027bZ\3\2\2\2\u027c\u027d")
        buf.write("\7q\2\2\u027d\u027e\7p\2\2\u027e\\\3\2\2\2\u027f\u0280")
        buf.write("\7c\2\2\u0280\u0281\7v\2\2\u0281^\3\2\2\2\u0282\u0283")
        buf.write("\7c\2\2\u0283\u0284\7p\2\2\u0284\u0285\7f\2\2\u0285`\3")
        buf.write("\2\2\2\u0286\u0287\7f\2\2\u0287\u0288\7g\2\2\u0288\u0289")
        buf.write("\7h\2\2\u0289b\3\2\2\2\u028a\u028b\7g\2\2\u028b\u028c")
        buf.write("\7n\2\2\u028c\u028d\7u\2\2\u028d\u028e\7g\2\2\u028ed\3")
        buf.write("\2\2\2\u028f\u0290\7h\2\2\u0290\u0291\7c\2\2\u0291\u0292")
        buf.write("\7n\2\2\u0292\u0293\7u\2\2\u0293\u0294\7g\2\2\u0294f\3")
        buf.write("\2\2\2\u0295\u0296\7h\2\2\u0296\u0297\7q\2\2\u0297\u0298")
        buf.write("\7t\2\2\u0298h\3\2\2\2\u0299\u029a\7h\2\2\u029a\u029b")
        buf.write("\7t\2\2\u029b\u029c\7q\2\2\u029c\u029d\7o\2\2\u029dj\3")
        buf.write("\2\2\2\u029e\u029f\7k\2\2\u029f\u02a0\7h\2\2\u02a0l\3")
        buf.write("\2\2\2\u02a1\u02a2\7k\2\2\u02a2\u02a3\7p\2\2\u02a3n\3")
        buf.write("\2\2\2\u02a4\u02a5\7k\2\2\u02a5\u02a6\7u\2\2\u02a6p\3")
        buf.write("\2\2\2\u02a7\u02a8\7p\2\2\u02a8\u02a9\7q\2\2\u02a9\u02aa")
        buf.write("\7p\2\2\u02aa\u02ab\7g\2\2\u02abr\3\2\2\2\u02ac\u02ad")
        buf.write("\7p\2\2\u02ad\u02ae\7q\2\2\u02ae\u02af\7v\2\2\u02aft\3")
        buf.write("\2\2\2\u02b0\u02b1\7q\2\2\u02b1\u02b2\7t\2\2\u02b2v\3")
        buf.write("\2\2\2\u02b3\u02b4\7t\2\2\u02b4\u02b5\7g\2\2\u02b5\u02b6")
        buf.write("\7v\2\2\u02b6\u02b7\7w\2\2\u02b7\u02b8\7t\2\2\u02b8\u02b9")
        buf.write("\7p\2\2\u02b9x\3\2\2\2\u02ba\u02bb\7v\2\2\u02bb\u02bc")
        buf.write("\7t\2\2\u02bc\u02bd\7w\2\2\u02bd\u02be\7g\2\2\u02bez\3")
        buf.write("\2\2\2\u02bf\u02c0\7a\2\2\u02c0|\3\2\2\2\u02c1\u02c2\7")
        buf.write("\60\2\2\u02c2~\3\2\2\2\u02c3\u02c4\7\60\2\2\u02c4\u02c5")
        buf.write("\7\60\2\2\u02c5\u0080\3\2\2\2\u02c6\u02c7\7\60\2\2\u02c7")
        buf.write("\u02c8\7\60\2\2\u02c8\u02c9\7\60\2\2\u02c9\u0082\3\2\2")
        buf.write("\2\u02ca\u02cb\7.\2\2\u02cb\u0084\3\2\2\2\u02cc\u02cd")
        buf.write("\7<\2\2\u02cd\u0086\3\2\2\2\u02ce\u02cf\7=\2\2\u02cf\u0088")
        buf.write("\3\2\2\2\u02d0\u02d1\7?\2\2\u02d1\u008a\3\2\2\2\u02d2")
        buf.write("\u02d3\7~\2\2\u02d3\u008c\3\2\2\2\u02d4\u02d5\7`\2\2\u02d5")
        buf.write("\u008e\3\2\2\2\u02d6\u02d7\7(\2\2\u02d7\u0090\3\2\2\2")
        buf.write("\u02d8\u02d9\7\u0080\2\2\u02d9\u0092\3\2\2\2\u02da\u02db")
        buf.write("\7>\2\2\u02db\u02dc\7>\2\2\u02dc\u0094\3\2\2\2\u02dd\u02de")
        buf.write("\7@\2\2\u02de\u02df\7@\2\2\u02df\u0096\3\2\2\2\u02e0\u02e1")
        buf.write("\7-\2\2\u02e1\u0098\3\2\2\2\u02e2\u02e3\7/\2\2\u02e3\u009a")
        buf.write("\3\2\2\2\u02e4\u02e5\7\61\2\2\u02e5\u009c\3\2\2\2\u02e6")
        buf.write("\u02e7\7,\2\2\u02e7\u009e\3\2\2\2\u02e8\u02e9\7'\2\2")
        buf.write("\u02e9\u00a0\3\2\2\2\u02ea\u02eb\7\61\2\2\u02eb\u02ec")
        buf.write("\7\61\2\2\u02ec\u00a2\3\2\2\2\u02ed\u02ee\7,\2\2\u02ee")
        buf.write("\u02ef\7,\2\2\u02ef\u00a4\3\2\2\2\u02f0\u02f1\7*\2\2\u02f1")
        buf.write("\u02f2\bS\4\2\u02f2\u00a6\3\2\2\2\u02f3\u02f4\7+\2\2\u02f4")
        buf.write("\u02f5\bT\5\2\u02f5\u00a8\3\2\2\2\u02f6\u02f7\7]\2\2\u02f7")
        buf.write("\u02f8\bU\6\2\u02f8\u00aa\3\2\2\2\u02f9\u02fa\7_\2\2\u02fa")
        buf.write("\u02fb\bV\7\2\u02fb\u00ac\3\2\2\2\u02fc\u02fd\7}\2\2\u02fd")
        buf.write("\u02fe\bW\b\2\u02fe\u00ae\3\2\2\2\u02ff\u0300\7\177\2")
        buf.write("\2\u0300\u0301\bX\t\2\u0301\u00b0\3\2\2\2\u0302\u0303")
        buf.write("\7>\2\2\u0303\u00b2\3\2\2\2\u0304\u0305\7@\2\2\u0305\u00b4")
        buf.write("\3\2\2\2\u0306\u0307\7?\2\2\u0307\u0308\7?\2\2\u0308\u00b6")
        buf.write("\3\2\2\2\u0309\u030a\7@\2\2\u030a\u030b\7?\2\2\u030b\u00b8")
        buf.write("\3\2\2\2\u030c\u030d\7>\2\2\u030d\u030e\7?\2\2\u030e\u00ba")
        buf.write("\3\2\2\2\u030f\u0310\7#\2\2\u0310\u0311\7?\2\2\u0311\u00bc")
        buf.write("\3\2\2\2\u0312\u0313\7-\2\2\u0313\u0314\7?\2\2\u0314\u00be")
        buf.write("\3\2\2\2\u0315\u0316\7/\2\2\u0316\u0317\7?\2\2\u0317\u00c0")
        buf.write("\3\2\2\2\u0318\u0319\7,\2\2\u0319\u031a\7?\2\2\u031a\u00c2")
        buf.write("\3\2\2\2\u031b\u031c\7\61\2\2\u031c\u031d\7?\2\2\u031d")
        buf.write("\u00c4\3\2\2\2\u031e\u031f\7'\2\2\u031f\u0320\7?\2\2")
        buf.write("\u0320\u00c6\3\2\2\2\u0321\u0322\7(\2\2\u0322\u0323\7")
        buf.write("?\2\2\u0323\u00c8\3\2\2\2\u0324\u0325\7~\2\2\u0325\u0326")
        buf.write("\7?\2\2\u0326\u00ca\3\2\2\2\u0327\u0328\7`\2\2\u0328\u0329")
        buf.write("\7?\2\2\u0329\u00cc\3\2\2\2\u032a\u032b\7>\2\2\u032b\u032c")
        buf.write("\7>\2\2\u032c\u032d\7?\2\2\u032d\u00ce\3\2\2\2\u032e\u032f")
        buf.write("\7@\2\2\u032f\u0330\7@\2\2\u0330\u0331\7?\2\2\u0331\u00d0")
        buf.write("\3\2\2\2\u0332\u0333\7,\2\2\u0333\u0334\7,\2\2\u0334\u0335")
        buf.write("\7?\2\2\u0335\u00d2\3\2\2\2\u0336\u0337\7\61\2\2\u0337")
        buf.write("\u0338\7\61\2\2\u0338\u0339\7?\2\2\u0339\u00d4\3\2\2\2")
        buf.write("\u033a\u033e\5\u0105\u0083\2\u033b\u033d\5\u0107\u0084")
        buf.write("\2\u033c\u033b\3\2\2\2\u033d\u0340\3\2\2\2\u033e\u033c")
        buf.write("\3\2\2\2\u033e\u033f\3\2\2\2\u033f\u00d6\3\2\2\2\u0340")
        buf.write("\u033e\3\2\2\2\u0341\u0342\7&\2\2\u0342\u0343\5\u00d5")
        buf.write("k\2\u0343\u00d8\3\2\2\2\u0344\u034e\t\3\2\2\u0345\u0347")
        buf.write("\t\4\2\2\u0346\u0345\3\2\2\2\u0346\u0347\3\2\2\2\u0347")
        buf.write("\u0348\3\2\2\2\u0348\u034e\t\5\2\2\u0349\u034b\t\5\2\2")
        buf.write("\u034a\u0349\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u034c\3")
        buf.write("\2\2\2\u034c\u034e\t\4\2\2\u034d\u0344\3\2\2\2\u034d\u0346")
        buf.write("\3\2\2\2\u034d\u034a\3\2\2\2\u034d\u034e\3\2\2\2\u034e")
        buf.write("\u034f\3\2\2\2\u034f\u0350\5\u00edw\2\u0350\u00da\3\2")
        buf.write("\2\2\u0351\u0356\5\u00ddo\2\u0352\u0356\5\u00dfp\2\u0353")
        buf.write("\u0356\5\u00e1q\2\u0354\u0356\5\u00e3r\2\u0355\u0351\3")
        buf.write("\2\2\2\u0355\u0352\3\2\2\2\u0355\u0353\3\2\2\2\u0355\u0354")
        buf.write("\3\2\2\2\u0356\u00dc\3\2\2\2\u0357\u035b\5\u00f1y\2\u0358")
        buf.write("\u035a\5\u00f3z\2\u0359\u0358\3\2\2\2\u035a\u035d\3\2")
        buf.write("\2\2\u035b\u0359\3\2\2\2\u035b\u035c\3\2\2\2\u035c\u0364")
        buf.write("\3\2\2\2\u035d\u035b\3\2\2\2\u035e\u0360\7\62\2\2\u035f")
        buf.write("\u035e\3\2\2\2\u0360\u0361\3\2\2\2\u0361\u035f\3\2\2\2")
        buf.write("\u0361\u0362\3\2\2\2\u0362\u0364\3\2\2\2\u0363\u0357\3")
        buf.write("\2\2\2\u0363\u035f\3\2\2\2\u0364\u00de\3\2\2\2\u0365\u0366")
        buf.write("\7\62\2\2\u0366\u0368\t\6\2\2\u0367\u0369\5\u00f5{\2\u0368")
        buf.write("\u0367\3\2\2\2\u0369\u036a\3\2\2\2\u036a\u0368\3\2\2\2")
        buf.write("\u036a\u036b\3\2\2\2\u036b\u00e0\3\2\2\2\u036c\u036d\7")
        buf.write("\62\2\2\u036d\u036f\t\7\2\2\u036e\u0370\5\u00f7|\2\u036f")
        buf.write("\u036e\3\2\2\2\u0370\u0371\3\2\2\2\u0371\u036f\3\2\2\2")
        buf.write("\u0371\u0372\3\2\2\2\u0372\u00e2\3\2\2\2\u0373\u0374\7")
        buf.write("\62\2\2\u0374\u0376\t\b\2\2\u0375\u0377\5\u00f9}\2\u0376")
        buf.write("\u0375\3\2\2\2\u0377\u0378\3\2\2\2\u0378\u0376\3\2\2\2")
        buf.write("\u0378\u0379\3\2\2\2\u0379\u00e4\3\2\2\2\u037a\u037d\5")
        buf.write("\u00fb~\2\u037b\u037d\5\u00fd\177\2\u037c\u037a\3\2\2")
        buf.write("\2\u037c\u037b\3\2\2\2\u037d\u00e6\3\2\2\2\u037e\u0380")
        buf.write("\7\17\2\2\u037f\u037e\3\2\2\2\u037f\u0380\3\2\2\2\u0380")
        buf.write("\u0381\3\2\2\2\u0381\u0384\7\f\2\2\u0382\u0384\4\16\17")
        buf.write("\2\u0383\u037f\3\2\2\2\u0383\u0382\3\2\2\2\u0384\u0386")
        buf.write("\3\2\2\2\u0385\u0387\5\u010b\u0086\2\u0386\u0385\3\2\2")
        buf.write("\2\u0386\u0387\3\2\2\2\u0387\u0388\3\2\2\2\u0388\u0389")
        buf.write("\bt\n\2\u0389\u00e8\3\2\2\2\u038a\u038e\5\u010b\u0086")
        buf.write("\2\u038b\u038e\5\u010d\u0087\2\u038c\u038e\5\u010f\u0088")
        buf.write("\2\u038d\u038a\3\2\2\2\u038d\u038b\3\2\2\2\u038d\u038c")
        buf.write("\3\2\2\2\u038e\u038f\3\2\2\2\u038f\u0390\bu\3\2\u0390")
        buf.write("\u00ea\3\2\2\2\u0391\u0392\13\2\2\2\u0392\u00ec\3\2\2")
        buf.write("\2\u0393\u0398\7)\2\2\u0394\u0397\5\u00efx\2\u0395\u0397")
        buf.write("\n\t\2\2\u0396\u0394\3\2\2\2\u0396\u0395\3\2\2\2\u0397")
        buf.write("\u039a\3\2\2\2\u0398\u0396\3\2\2\2\u0398\u0399\3\2\2\2")
        buf.write("\u0399\u039b\3\2\2\2\u039a\u0398\3\2\2\2\u039b\u03a6\7")
        buf.write(")\2\2\u039c\u03a1\7$\2\2\u039d\u03a0\5\u00efx\2\u039e")
        buf.write("\u03a0\n\n\2\2\u039f\u039d\3\2\2\2\u039f\u039e\3\2\2\2")
        buf.write("\u03a0\u03a3\3\2\2\2\u03a1\u039f\3\2\2\2\u03a1\u03a2\3")
        buf.write("\2\2\2\u03a2\u03a4\3\2\2\2\u03a3\u03a1\3\2\2\2\u03a4\u03a6")
        buf.write("\7$\2\2\u03a5\u0393\3\2\2\2\u03a5\u039c\3\2\2\2\u03a6")
        buf.write("\u00ee\3\2\2\2\u03a7\u03a8\7^\2\2\u03a8\u03ac\13\2\2\2")
        buf.write("\u03a9\u03aa\7^\2\2\u03aa\u03ac\5\u00e7t\2\u03ab\u03a7")
        buf.write("\3\2\2\2\u03ab\u03a9\3\2\2\2\u03ac\u00f0\3\2\2\2\u03ad")
        buf.write("\u03ae\4\63;\2\u03ae\u00f2\3\2\2\2\u03af\u03b0\4\62;\2")
        buf.write("\u03b0\u00f4\3\2\2\2\u03b1\u03b2\4\629\2\u03b2\u00f6\3")
        buf.write("\2\2\2\u03b3\u03b6\5\u00f3z\2\u03b4\u03b6\t\13\2\2\u03b5")
        buf.write("\u03b3\3\2\2\2\u03b5\u03b4\3\2\2\2\u03b6\u00f8\3\2\2\2")
        buf.write("\u03b7\u03b8\4\62\63\2\u03b8\u00fa\3\2\2\2\u03b9\u03bb")
        buf.write("\5\u00ff\u0080\2\u03ba\u03b9\3\2\2\2\u03ba\u03bb\3\2\2")
        buf.write("\2\u03bb\u03bc\3\2\2\2\u03bc\u03c1\5\u0101\u0081\2\u03bd")
        buf.write("\u03be\5\u00ff\u0080\2\u03be\u03bf\7\60\2\2\u03bf\u03c1")
        buf.write("\3\2\2\2\u03c0\u03ba\3\2\2\2\u03c0\u03bd\3\2\2\2\u03c1")
        buf.write("\u00fc\3\2\2\2\u03c2\u03c5\5\u00ff\u0080\2\u03c3\u03c5")
        buf.write("\5\u00fb~\2\u03c4\u03c2\3\2\2\2\u03c4\u03c3\3\2\2\2\u03c5")
        buf.write("\u03c6\3\2\2\2\u03c6\u03c7\5\u0103\u0082\2\u03c7\u00fe")
        buf.write("\3\2\2\2\u03c8\u03ca\5\u00f3z\2\u03c9\u03c8\3\2\2\2\u03ca")
        buf.write("\u03cb\3\2\2\2\u03cb\u03c9\3\2\2\2\u03cb\u03cc\3\2\2\2")
        buf.write("\u03cc\u0100\3\2\2\2\u03cd\u03cf\7\60\2\2\u03ce\u03d0")
        buf.write("\5\u00f3z\2\u03cf\u03ce\3\2\2\2\u03d0\u03d1\3\2\2\2\u03d1")
        buf.write("\u03cf\3\2\2\2\u03d1\u03d2\3\2\2\2\u03d2\u0102\3\2\2\2")
        buf.write("\u03d3\u03d5\t\f\2\2\u03d4\u03d6\t\r\2\2\u03d5\u03d4\3")
        buf.write("\2\2\2\u03d5\u03d6\3\2\2\2\u03d6\u03d8\3\2\2\2\u03d7\u03d9")
        buf.write("\5\u00f3z\2\u03d8\u03d7\3\2\2\2\u03d9\u03da\3\2\2\2\u03da")
        buf.write("\u03d8\3\2\2\2\u03da\u03db\3\2\2\2\u03db\u0104\3\2\2\2")
        buf.write("\u03dc\u03df\5{>\2\u03dd\u03df\5\u0109\u0085\2\u03de\u03dc")
        buf.write("\3\2\2\2\u03de\u03dd\3\2\2\2\u03df\u0106\3\2\2\2\u03e0")
        buf.write("\u03e3\5\u0105\u0083\2\u03e1\u03e3\5\u00f3z\2\u03e2\u03e0")
        buf.write("\3\2\2\2\u03e2\u03e1\3\2\2\2\u03e3\u0108\3\2\2\2\u03e4")
        buf.write("\u03e5\t\16\2\2\u03e5\u010a\3\2\2\2\u03e6\u03e8\t\17\2")
        buf.write("\2\u03e7\u03e6\3\2\2\2\u03e8\u03e9\3\2\2\2\u03e9\u03e7")
        buf.write("\3\2\2\2\u03e9\u03ea\3\2\2\2\u03ea\u010c\3\2\2\2\u03eb")
        buf.write("\u03ef\7%\2\2\u03ec\u03ee\n\20\2\2\u03ed\u03ec\3\2\2\2")
        buf.write("\u03ee\u03f1\3\2\2\2\u03ef\u03ed\3\2\2\2\u03ef\u03f0\3")
        buf.write("\2\2\2\u03f0\u010e\3\2\2\2\u03f1\u03ef\3\2\2\2\u03f2\u03f4")
        buf.write("\7^\2\2\u03f3\u03f5\5\u010b\u0086\2\u03f4\u03f3\3\2\2")
        buf.write("\2\u03f4\u03f5\3\2\2\2\u03f5\u03fb\3\2\2\2\u03f6\u03f8")
        buf.write("\7\17\2\2\u03f7\u03f6\3\2\2\2\u03f7\u03f8\3\2\2\2\u03f8")
        buf.write("\u03f9\3\2\2\2\u03f9\u03fc\7\f\2\2\u03fa\u03fc\4\16\17")
        buf.write("\2\u03fb\u03f7\3\2\2\2\u03fb\u03fa\3\2\2\2\u03fc\u0110")
        buf.write("\3\2\2\2/\2\u0155\u0211\u022f\u023a\u023c\u0271\u0273")
        buf.write("\u033e\u0346\u034a\u034d\u0355\u035b\u0361\u0363\u036a")
        buf.write("\u0371\u0378\u037c\u037f\u0383\u0386\u038d\u0396\u0398")
        buf.write("\u039f\u03a1\u03a5\u03ab\u03b5\u03ba\u03c0\u03c4\u03cb")
        buf.write("\u03d1\u03d5\u03da\u03de\u03e2\u03e9\u03ef\u03f4\u03f7")
        buf.write("\u03fb\13\3+\2\b\2\2\3S\3\3T\4\3U\5\3V\6\3W\7\3X\b\3t")
        buf.write("\t")
        return buf.getvalue()


class YarcLexer(YarcLexerBase):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    INDENT = 1
    DEDENT = 2
    SCENARIO = 3
    SETTINGS = 4
    STAGE = 5
    WRITERS = 6
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
    CAM_TRANSLATE = 22
    ROTATE = 23
    SCALE = 24
    SEMANTICS = 25
    VISIBLE = 26
    SIZE = 27
    LOOK_AT = 28
    UP_AXIS = 29
    AXIS = 30
    ORDER = 31
    SCATTER = 32
    SCATTER_TYPE = 33
    AROUND = 34
    TEXTURE = 35
    EVERY = 36
    FRAMES = 37
    TIME = 38
    UNIFORM = 39
    NORMAL = 40
    CHOICE = 41
    SEQUENCE = 42
    LOG_UNIFORM = 43
    SNIPPET = 44
    TO = 45
    ON = 46
    AT = 47
    AND = 48
    DEF = 49
    ELSE = 50
    FALSE = 51
    FOR = 52
    FROM = 53
    IF = 54
    IN = 55
    IS = 56
    NONE = 57
    NOT = 58
    OR = 59
    RETURN = 60
    TRUE = 61
    UNDERSCORE = 62
    DOT = 63
    RANGE = 64
    ELLIPSIS = 65
    COMMA = 66
    COLON = 67
    SEMI = 68
    ASSIGN = 69
    BIT_OR = 70
    XOR = 71
    BIT_AND = 72
    BIT_NOT = 73
    LSHIFT = 74
    RSHIFT = 75
    PLUS = 76
    MINUS = 77
    DIV = 78
    MUL = 79
    MOD = 80
    IDIV = 81
    POWER = 82
    LPAREN = 83
    RPAREN = 84
    LBRACK = 85
    RBRACK = 86
    LBRACE = 87
    RBRACE = 88
    LT = 89
    GT = 90
    EQUALS = 91
    GT_EQ = 92
    LT_EQ = 93
    NOT_EQ = 94
    ADD_ASSIGN = 95
    SUB_ASSIGN = 96
    MULT_ASSIGN = 97
    DIV_ASSIGN = 98
    MOD_ASSIGN = 99
    AND_ASSIGN = 100
    OR_ASSIGN = 101
    XOR_ASSIGN = 102
    LSHIFT_ASSIGN = 103
    RSHIFT_ASSIGN = 104
    POWER_ASSIGN = 105
    IDIV_ASSIGN = 106
    ID = 107
    SETTING_ID = 108
    STRING = 109
    INTEGER = 110
    DEC_INTEGER = 111
    OCT_INTEGER = 112
    HEX_INTEGER = 113
    BIN_INTEGER = 114
    FLOAT_NUMBER = 115
    NEWLINE = 116
    SKIP_ = 117
    UNKNOWN = 118

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = [
        "<INVALID>",
        "'scenario'",
        "'settings'",
        "'stage'",
        "'writers'",
        "'Camera'",
        "'Light'",
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
        "'translate'",
        "'camera_translate'",
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

    ruleNames = [
        "SCENARIO",
        "SETTINGS",
        "STAGE",
        "WRITERS",
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
            actions[41] = self.SNIPPET_action
            actions[81] = self.LPAREN_action
            actions[82] = self.RPAREN_action
            actions[83] = self.LBRACK_action
            actions[84] = self.RBRACK_action
            actions[85] = self.LBRACE_action
            actions[86] = self.RBRACE_action
            actions[114] = self.NEWLINE_action
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
