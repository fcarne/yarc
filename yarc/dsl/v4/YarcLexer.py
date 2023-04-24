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
        buf.write("\u03f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0133")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0159\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37\u0204\n")
        buf.write('\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3"\3')
        buf.write('"\3"\3"\3"\3"\3#\3#\3#\3#\3#\3#\3#\5#\u0222\n#\3')
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u022d\n$\5$\u022f\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3'\3'\3'\3")
        buf.write("'\3'\3'\3'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\7+\u0264")
        buf.write("\n+\f+\16+\u0267\13+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.")
        buf.write("\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\38\39\39\39\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3")
        buf.write("H\3I\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3P\3")
        buf.write("P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3V\3")
        buf.write("V\3V\3W\3W\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\3")
        buf.write("\\\3]\3]\3]\3^\3^\3^\3_\3_\3_\3`\3`\3`\3a\3a\3a\3b\3b")
        buf.write("\3b\3c\3c\3c\3d\3d\3d\3e\3e\3e\3e\3f\3f\3f\3f\3g\3g\3")
        buf.write("g\3g\3h\3h\3h\3h\3i\3i\7i\u032a\ni\fi\16i\u032d\13i\3")
        buf.write("j\3j\3j\3k\3k\3l\3l\5l\u0336\nl\3m\3m\5m\u033a\nm\3m\3")
        buf.write("m\5m\u033e\nm\3m\5m\u0341\nm\3m\3m\3n\3n\3n\3n\5n\u0349")
        buf.write("\nn\3o\3o\7o\u034d\no\fo\16o\u0350\13o\3o\6o\u0353\no")
        buf.write("\ro\16o\u0354\5o\u0357\no\3p\3p\3p\6p\u035c\np\rp\16p")
        buf.write("\u035d\3q\3q\3q\6q\u0363\nq\rq\16q\u0364\3r\3r\3r\6r\u036a")
        buf.write("\nr\rr\16r\u036b\3s\3s\5s\u0370\ns\3t\3t\3t\5t\u0375\n")
        buf.write("t\3t\3t\5t\u0379\nt\3t\5t\u037c\nt\5t\u037e\nt\3t\3t\3")
        buf.write("u\3u\3u\5u\u0385\nu\3u\3u\3v\3v\3w\3w\3w\7w\u038e\nw\f")
        buf.write("w\16w\u0391\13w\3w\3w\3w\3w\7w\u0397\nw\fw\16w\u039a\13")
        buf.write("w\3w\5w\u039d\nw\3x\3x\3x\3x\5x\u03a3\nx\3y\3y\3z\3z\3")
        buf.write("{\3{\3|\3|\5|\u03ad\n|\3}\3}\3~\5~\u03b2\n~\3~\3~\3~\3")
        buf.write("~\5~\u03b8\n~\3\177\3\177\5\177\u03bc\n\177\3\177\3\177")
        buf.write("\3\u0080\6\u0080\u03c1\n\u0080\r\u0080\16\u0080\u03c2")
        buf.write("\3\u0081\3\u0081\6\u0081\u03c7\n\u0081\r\u0081\16\u0081")
        buf.write("\u03c8\3\u0082\3\u0082\5\u0082\u03cd\n\u0082\3\u0082\6")
        buf.write("\u0082\u03d0\n\u0082\r\u0082\16\u0082\u03d1\3\u0083\3")
        buf.write("\u0083\5\u0083\u03d6\n\u0083\3\u0084\3\u0084\5\u0084\u03da")
        buf.write("\n\u0084\3\u0085\3\u0085\3\u0086\6\u0086\u03df\n\u0086")
        buf.write("\r\u0086\16\u0086\u03e0\3\u0087\3\u0087\7\u0087\u03e5")
        buf.write("\n\u0087\f\u0087\16\u0087\u03e8\13\u0087\3\u0088\3\u0088")
        buf.write("\5\u0088\u03ec\n\u0088\3\u0088\5\u0088\u03ef\n\u0088\3")
        buf.write("\u0088\3\u0088\5\u0088\u03f3\n\u0088\3\u0265\2\u0089\3")
        buf.write("\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31")
        buf.write("\20\33\21\35\22\37\23!\24#\25%\26'\27)\30+\31-\32/\33")
        buf.write("\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G'I(K)M*O+Q,S")
        buf.write("-U\2W.Y/[\60]\61_\62a\63c\64e\65g\66i\67k8m9o:q;s<u=w")
        buf.write(">y?{@}A\177B\u0081C\u0083D\u0085E\u0087F\u0089G\u008b")
        buf.write("H\u008dI\u008fJ\u0091K\u0093L\u0095M\u0097N\u0099O\u009b")
        buf.write("P\u009dQ\u009fR\u00a1S\u00a3T\u00a5U\u00a7V\u00a9W\u00ab")
        buf.write("X\u00adY\u00afZ\u00b1[\u00b3\\\u00b5]\u00b7^\u00b9_\u00bb")
        buf.write("`\u00bda\u00bfb\u00c1c\u00c3d\u00c5e\u00c7f\u00c9g\u00cb")
        buf.write("h\u00cdi\u00cfj\u00d1k\u00d3l\u00d5m\u00d7n\u00d9o\u00db")
        buf.write("p\u00ddq\u00dfr\u00e1s\u00e3t\u00e5u\u00e7v\u00e9w\u00eb")
        buf.write("x\u00ed\2\u00ef\2\u00f1\2\u00f3\2\u00f5\2\u00f7\2\u00f9")
        buf.write("\2\u00fb\2\u00fd\2\u00ff\2\u0101\2\u0103\2\u0105\2\u0107")
        buf.write("\2\u0109\2\u010b\2\u010d\2\u010f\2\3\2\21\4\2Z\\z|\4\2")
        buf.write("WWww\4\2HHhh\4\2TTtt\4\2QQqq\4\2ZZzz\4\2DDdd\6\2\f\f\16")
        buf.write("\17))^^\6\2\f\f\16\17$$^^\4\2CHch\4\2GGgg\4\2--//\4\2")
        buf.write('C\\c|\4\2\13\13""\4\2\f\f\16\17\2\u0419\2\3\3\2\2\2')
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write("\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2")
        buf.write("\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3")
        buf.write("\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2")
        buf.write("\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd")
        buf.write("\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2")
        buf.write("\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb")
        buf.write("\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2")
        buf.write("\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9")
        buf.write("\3\2\2\2\2\u00db\3\2\2\2\2\u00dd\3\2\2\2\2\u00df\3\2\2")
        buf.write("\2\2\u00e1\3\2\2\2\2\u00e3\3\2\2\2\2\u00e5\3\2\2\2\2\u00e7")
        buf.write("\3\2\2\2\2\u00e9\3\2\2\2\2\u00eb\3\2\2\2\3\u0111\3\2\2")
        buf.write("\2\5\u011a\3\2\2\2\7\u0123\3\2\2\2\t\u012a\3\2\2\2\13")
        buf.write("\u0158\3\2\2\2\r\u015a\3\2\2\2\17\u0161\3\2\2\2\21\u0167")
        buf.write("\3\2\2\2\23\u016e\3\2\2\2\25\u0177\3\2\2\2\27\u0180\3")
        buf.write("\2\2\2\31\u0185\3\2\2\2\33\u018c\3\2\2\2\35\u0192\3\2")
        buf.write("\2\2\37\u019e\3\2\2\2!\u01a2\3\2\2\2#\u01a7\3\2\2\2%\u01ad")
        buf.write("\3\2\2\2'\u01b3\3\2\2\2)\u01bd\3\2\2\2+\u01c4\3\2\2\2")
        buf.write("-\u01ca\3\2\2\2/\u01d4\3\2\2\2\61\u01dc\3\2\2\2\63\u01e1")
        buf.write("\3\2\2\2\65\u01e9\3\2\2\2\67\u01f1\3\2\2\29\u01f3\3\2")
        buf.write("\2\2;\u01f7\3\2\2\2=\u0203\3\2\2\2?\u0205\3\2\2\2A\u020c")
        buf.write("\3\2\2\2C\u0214\3\2\2\2E\u021a\3\2\2\2G\u0223\3\2\2\2")
        buf.write("I\u0230\3\2\2\2K\u0238\3\2\2\2M\u023f\3\2\2\2O\u0246\3")
        buf.write("\2\2\2Q\u024f\3\2\2\2S\u025a\3\2\2\2U\u025f\3\2\2\2W\u026b")
        buf.write("\3\2\2\2Y\u026e\3\2\2\2[\u0271\3\2\2\2]\u0274\3\2\2\2")
        buf.write("_\u0278\3\2\2\2a\u027c\3\2\2\2c\u0281\3\2\2\2e\u0287\3")
        buf.write("\2\2\2g\u028b\3\2\2\2i\u028e\3\2\2\2k\u0291\3\2\2\2m\u0294")
        buf.write("\3\2\2\2o\u0299\3\2\2\2q\u029d\3\2\2\2s\u02a0\3\2\2\2")
        buf.write("u\u02a7\3\2\2\2w\u02ac\3\2\2\2y\u02ae\3\2\2\2{\u02b0\3")
        buf.write("\2\2\2}\u02b3\3\2\2\2\177\u02b7\3\2\2\2\u0081\u02b9\3")
        buf.write("\2\2\2\u0083\u02bb\3\2\2\2\u0085\u02bd\3\2\2\2\u0087\u02bf")
        buf.write("\3\2\2\2\u0089\u02c1\3\2\2\2\u008b\u02c3\3\2\2\2\u008d")
        buf.write("\u02c5\3\2\2\2\u008f\u02c7\3\2\2\2\u0091\u02ca\3\2\2\2")
        buf.write("\u0093\u02cd\3\2\2\2\u0095\u02cf\3\2\2\2\u0097\u02d1\3")
        buf.write("\2\2\2\u0099\u02d3\3\2\2\2\u009b\u02d5\3\2\2\2\u009d\u02d7")
        buf.write("\3\2\2\2\u009f\u02da\3\2\2\2\u00a1\u02dd\3\2\2\2\u00a3")
        buf.write("\u02e0\3\2\2\2\u00a5\u02e3\3\2\2\2\u00a7\u02e6\3\2\2\2")
        buf.write("\u00a9\u02e9\3\2\2\2\u00ab\u02ec\3\2\2\2\u00ad\u02ef\3")
        buf.write("\2\2\2\u00af\u02f1\3\2\2\2\u00b1\u02f3\3\2\2\2\u00b3\u02f6")
        buf.write("\3\2\2\2\u00b5\u02f9\3\2\2\2\u00b7\u02fc\3\2\2\2\u00b9")
        buf.write("\u02ff\3\2\2\2\u00bb\u0302\3\2\2\2\u00bd\u0305\3\2\2\2")
        buf.write("\u00bf\u0308\3\2\2\2\u00c1\u030b\3\2\2\2\u00c3\u030e\3")
        buf.write("\2\2\2\u00c5\u0311\3\2\2\2\u00c7\u0314\3\2\2\2\u00c9\u0317")
        buf.write("\3\2\2\2\u00cb\u031b\3\2\2\2\u00cd\u031f\3\2\2\2\u00cf")
        buf.write("\u0323\3\2\2\2\u00d1\u0327\3\2\2\2\u00d3\u032e\3\2\2\2")
        buf.write("\u00d5\u0331\3\2\2\2\u00d7\u0335\3\2\2\2\u00d9\u0340\3")
        buf.write("\2\2\2\u00db\u0348\3\2\2\2\u00dd\u0356\3\2\2\2\u00df\u0358")
        buf.write("\3\2\2\2\u00e1\u035f\3\2\2\2\u00e3\u0366\3\2\2\2\u00e5")
        buf.write("\u036f\3\2\2\2\u00e7\u037d\3\2\2\2\u00e9\u0384\3\2\2\2")
        buf.write("\u00eb\u0388\3\2\2\2\u00ed\u039c\3\2\2\2\u00ef\u03a2\3")
        buf.write("\2\2\2\u00f1\u03a4\3\2\2\2\u00f3\u03a6\3\2\2\2\u00f5\u03a8")
        buf.write("\3\2\2\2\u00f7\u03ac\3\2\2\2\u00f9\u03ae\3\2\2\2\u00fb")
        buf.write("\u03b7\3\2\2\2\u00fd\u03bb\3\2\2\2\u00ff\u03c0\3\2\2\2")
        buf.write("\u0101\u03c4\3\2\2\2\u0103\u03ca\3\2\2\2\u0105\u03d5\3")
        buf.write("\2\2\2\u0107\u03d9\3\2\2\2\u0109\u03db\3\2\2\2\u010b\u03de")
        buf.write("\3\2\2\2\u010d\u03e2\3\2\2\2\u010f\u03e9\3\2\2\2\u0111")
        buf.write("\u0112\7u\2\2\u0112\u0113\7e\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("\u0115\7p\2\2\u0115\u0116\7c\2\2\u0116\u0117\7t\2\2\u0117")
        buf.write("\u0118\7k\2\2\u0118\u0119\7q\2\2\u0119\4\3\2\2\2\u011a")
        buf.write("\u011b\7u\2\2\u011b\u011c\7g\2\2\u011c\u011d\7v\2\2\u011d")
        buf.write("\u011e\7v\2\2\u011e\u011f\7k\2\2\u011f\u0120\7p\2\2\u0120")
        buf.write("\u0121\7i\2\2\u0121\u0122\7u\2\2\u0122\6\3\2\2\2\u0123")
        buf.write("\u0124\7y\2\2\u0124\u0125\7t\2\2\u0125\u0126\7k\2\2\u0126")
        buf.write("\u0127\7v\2\2\u0127\u0128\7g\2\2\u0128\u0129\7t\2\2\u0129")
        buf.write("\b\3\2\2\2\u012a\u012b\7n\2\2\u012b\u012c\7k\2\2\u012c")
        buf.write("\u012d\7d\2\2\u012d\u0132\3\2\2\2\u012e\u012f\7t\2\2\u012f")
        buf.write("\u0130\7c\2\2\u0130\u0131\7t\2\2\u0131\u0133\7{\2\2\u0132")
        buf.write("\u012e\3\2\2\2\u0132\u0133\3\2\2\2\u0133\n\3\2\2\2\u0134")
        buf.write("\u0135\7r\2\2\u0135\u0136\7n\2\2\u0136\u0137\7c\2\2\u0137")
        buf.write("\u0138\7p\2\2\u0138\u0159\7g\2\2\u0139\u013a\7e\2\2\u013a")
        buf.write("\u013b\7w\2\2\u013b\u013c\7d\2\2\u013c\u0159\7g\2\2\u013d")
        buf.write("\u013e\7u\2\2\u013e\u013f\7r\2\2\u013f\u0140\7j\2\2\u0140")
        buf.write("\u0141\7g\2\2\u0141\u0142\7t\2\2\u0142\u0159\7g\2\2\u0143")
        buf.write("\u0144\7e\2\2\u0144\u0145\7{\2\2\u0145\u0146\7n\2\2\u0146")
        buf.write("\u0147\7k\2\2\u0147\u0148\7p\2\2\u0148\u0149\7f\2\2\u0149")
        buf.write("\u014a\7g\2\2\u014a\u0159\7t\2\2\u014b\u014c\7e\2\2\u014c")
        buf.write("\u014d\7q\2\2\u014d\u014e\7p\2\2\u014e\u0159\7g\2\2\u014f")
        buf.write("\u0150\7v\2\2\u0150\u0151\7q\2\2\u0151\u0152\7t\2\2\u0152")
        buf.write("\u0153\7w\2\2\u0153\u0159\7u\2\2\u0154\u0155\7f\2\2\u0155")
        buf.write("\u0156\7k\2\2\u0156\u0157\7u\2\2\u0157\u0159\7m\2\2\u0158")
        buf.write("\u0134\3\2\2\2\u0158\u0139\3\2\2\2\u0158\u013d\3\2\2\2")
        buf.write("\u0158\u0143\3\2\2\2\u0158\u014b\3\2\2\2\u0158\u014f\3")
        buf.write("\2\2\2\u0158\u0154\3\2\2\2\u0159\f\3\2\2\2\u015a\u015b")
        buf.write("\7e\2\2\u015b\u015c\7c\2\2\u015c\u015d\7o\2\2\u015d\u015e")
        buf.write("\7g\2\2\u015e\u015f\7t\2\2\u015f\u0160\7c\2\2\u0160\16")
        buf.write("\3\2\2\2\u0161\u0162\7n\2\2\u0162\u0163\7k\2\2\u0163\u0164")
        buf.write("\7i\2\2\u0164\u0165\7j\2\2\u0165\u0166\7v\2\2\u0166\20")
        buf.write("\3\2\2\2\u0167\u0168\7u\2\2\u0168\u0169\7v\2\2\u0169\u016a")
        buf.write("\7g\2\2\u016a\u016b\7t\2\2\u016b\u016c\7g\2\2\u016c\u016d")
        buf.write("\7q\2\2\u016d\22\3\2\2\2\u016e\u016f\7o\2\2\u016f\u0170")
        buf.write("\7c\2\2\u0170\u0171\7v\2\2\u0171\u0172\7g\2\2\u0172\u0173")
        buf.write("\7t\2\2\u0173\u0174\7k\2\2\u0174\u0175\7c\2\2\u0175\u0176")
        buf.write("\7n\2\2\u0176\24\3\2\2\2\u0177\u0178\7v\2\2\u0178\u0179")
        buf.write("\7k\2\2\u0179\u017a\7o\2\2\u017a\u017b\7g\2\2\u017b\u017c")
        buf.write("\7n\2\2\u017c\u017d\7k\2\2\u017d\u017e\7p\2\2\u017e\u017f")
        buf.write("\7g\2\2\u017f\26\3\2\2\2\u0180\u0181\7q\2\2\u0181\u0182")
        buf.write("\7r\2\2\u0182\u0183\7g\2\2\u0183\u0184\7p\2\2\u0184\30")
        buf.write("\3\2\2\2\u0185\u0186\7e\2\2\u0186\u0187\7t\2\2\u0187\u0188")
        buf.write("\7g\2\2\u0188\u0189\7c\2\2\u0189\u018a\7v\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\32\3\2\2\2\u018c\u018d\7i\2\2\u018d\u018e")
        buf.write("\7t\2\2\u018e\u018f\7q\2\2\u018f\u0190\7w\2\2\u0190\u0191")
        buf.write("\7r\2\2\u0191\34\3\2\2\2\u0192\u0193\7k\2\2\u0193\u0194")
        buf.write("\7p\2\2\u0194\u0195\7u\2\2\u0195\u0196\7v\2\2\u0196\u0197")
        buf.write("\7c\2\2\u0197\u0198\7p\2\2\u0198\u0199\7v\2\2\u0199\u019a")
        buf.write("\7k\2\2\u019a\u019b\7c\2\2\u019b\u019c\7v\2\2\u019c\u019d")
        buf.write("\7g\2\2\u019d\36\3\2\2\2\u019e\u019f\7i\2\2\u019f\u01a0")
        buf.write("\7g\2\2\u01a0\u01a1\7v\2\2\u01a1 \3\2\2\2\u01a2\u01a3")
        buf.write("\7g\2\2\u01a3\u01a4\7f\2\2\u01a4\u01a5\7k\2\2\u01a5\u01a6")
        buf.write('\7v\2\2\u01a6"\3\2\2\2\u01a7\u01a8\7h\2\2\u01a8\u01a9')
        buf.write("\7g\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab\7e\2\2\u01ab\u01ac")
        buf.write("\7j\2\2\u01ac$\3\2\2\2\u01ad\u01ae\7o\2\2\u01ae\u01af")
        buf.write("\7c\2\2\u01af\u01b0\7v\2\2\u01b0\u01b1\7e\2\2\u01b1\u01b2")
        buf.write("\7j\2\2\u01b2&\3\2\2\2\u01b3\u01b4\7v\2\2\u01b4\u01b5")
        buf.write("\7t\2\2\u01b5\u01b6\7c\2\2\u01b6\u01b7\7p\2\2\u01b7\u01b8")
        buf.write("\7u\2\2\u01b8\u01b9\7n\2\2\u01b9\u01ba\7c\2\2\u01ba\u01bb")
        buf.write("\7v\2\2\u01bb\u01bc\7g\2\2\u01bc(\3\2\2\2\u01bd\u01be")
        buf.write("\7t\2\2\u01be\u01bf\7q\2\2\u01bf\u01c0\7v\2\2\u01c0\u01c1")
        buf.write("\7c\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3\7g\2\2\u01c3*\3")
        buf.write("\2\2\2\u01c4\u01c5\7u\2\2\u01c5\u01c6\7e\2\2\u01c6\u01c7")
        buf.write("\7c\2\2\u01c7\u01c8\7n\2\2\u01c8\u01c9\7g\2\2\u01c9,\3")
        buf.write("\2\2\2\u01ca\u01cb\7u\2\2\u01cb\u01cc\7g\2\2\u01cc\u01cd")
        buf.write("\7o\2\2\u01cd\u01ce\7c\2\2\u01ce\u01cf\7p\2\2\u01cf\u01d0")
        buf.write("\7v\2\2\u01d0\u01d1\7k\2\2\u01d1\u01d2\7e\2\2\u01d2\u01d3")
        buf.write("\7u\2\2\u01d3.\3\2\2\2\u01d4\u01d5\7x\2\2\u01d5\u01d6")
        buf.write("\7k\2\2\u01d6\u01d7\7u\2\2\u01d7\u01d8\7k\2\2\u01d8\u01d9")
        buf.write("\7d\2\2\u01d9\u01da\7n\2\2\u01da\u01db\7g\2\2\u01db\60")
        buf.write("\3\2\2\2\u01dc\u01dd\7u\2\2\u01dd\u01de\7k\2\2\u01de\u01df")
        buf.write("\7|\2\2\u01df\u01e0\7g\2\2\u01e0\62\3\2\2\2\u01e1\u01e2")
        buf.write("\7n\2\2\u01e2\u01e3\7q\2\2\u01e3\u01e4\7q\2\2\u01e4\u01e5")
        buf.write("\7m\2\2\u01e5\u01e6\7a\2\2\u01e6\u01e7\7c\2\2\u01e7\u01e8")
        buf.write("\7v\2\2\u01e8\64\3\2\2\2\u01e9\u01ea\7w\2\2\u01ea\u01eb")
        buf.write("\7r\2\2\u01eb\u01ec\7a\2\2\u01ec\u01ed\7c\2\2\u01ed\u01ee")
        buf.write("\7z\2\2\u01ee\u01ef\7k\2\2\u01ef\u01f0\7u\2\2\u01f0\66")
        buf.write("\3\2\2\2\u01f1\u01f2\t\2\2\2\u01f28\3\2\2\2\u01f3\u01f4")
        buf.write("\5\67\34\2\u01f4\u01f5\5\67\34\2\u01f5\u01f6\5\67\34\2")
        buf.write("\u01f6:\3\2\2\2\u01f7\u01f8\7u\2\2\u01f8\u01f9\7e\2\2")
        buf.write("\u01f9\u01fa\7c\2\2\u01fa\u01fb\7v\2\2\u01fb\u01fc\7v")
        buf.write("\2\2\u01fc\u01fd\7g\2\2\u01fd\u01fe\7t\2\2\u01fe<\3\2")
        buf.write("\2\2\u01ff\u0200\7\64\2\2\u0200\u0204\7f\2\2\u0201\u0202")
        buf.write("\7\65\2\2\u0202\u0204\7f\2\2\u0203\u01ff\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0204>\3\2\2\2\u0205\u0206\7c\2\2\u0206")
        buf.write("\u0207\7t\2\2\u0207\u0208\7q\2\2\u0208\u0209\7w\2\2\u0209")
        buf.write("\u020a\7p\2\2\u020a\u020b\7f\2\2\u020b@\3\2\2\2\u020c")
        buf.write("\u020d\7v\2\2\u020d\u020e\7g\2\2\u020e\u020f\7z\2\2\u020f")
        buf.write("\u0210\7v\2\2\u0210\u0211\7w\2\2\u0211\u0212\7t\2\2\u0212")
        buf.write("\u0213\7g\2\2\u0213B\3\2\2\2\u0214\u0215\7g\2\2\u0215")
        buf.write("\u0216\7x\2\2\u0216\u0217\7g\2\2\u0217\u0218\7t\2\2\u0218")
        buf.write("\u0219\7{\2\2\u0219D\3\2\2\2\u021a\u021b\7h\2\2\u021b")
        buf.write("\u021c\7t\2\2\u021c\u021d\7c\2\2\u021d\u021e\7o\2\2\u021e")
        buf.write("\u021f\7g\2\2\u021f\u0221\3\2\2\2\u0220\u0222\7u\2\2\u0221")
        buf.write("\u0220\3\2\2\2\u0221\u0222\3\2\2\2\u0222F\3\2\2\2\u0223")
        buf.write("\u0224\7u\2\2\u0224\u0225\7g\2\2\u0225\u0226\7e\2\2\u0226")
        buf.write("\u022e\3\2\2\2\u0227\u0228\7q\2\2\u0228\u0229\7p\2\2\u0229")
        buf.write("\u022a\7f\2\2\u022a\u022c\3\2\2\2\u022b\u022d\7u\2\2\u022c")
        buf.write("\u022b\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2\2")
        buf.write("\u022e\u0227\3\2\2\2\u022e\u022f\3\2\2\2\u022fH\3\2\2")
        buf.write("\2\u0230\u0231\7W\2\2\u0231\u0232\7p\2\2\u0232\u0233\7")
        buf.write("k\2\2\u0233\u0234\7h\2\2\u0234\u0235\7q\2\2\u0235\u0236")
        buf.write("\7t\2\2\u0236\u0237\7o\2\2\u0237J\3\2\2\2\u0238\u0239")
        buf.write("\7P\2\2\u0239\u023a\7q\2\2\u023a\u023b\7t\2\2\u023b\u023c")
        buf.write("\7o\2\2\u023c\u023d\7c\2\2\u023d\u023e\7n\2\2\u023eL\3")
        buf.write("\2\2\2\u023f\u0240\7E\2\2\u0240\u0241\7j\2\2\u0241\u0242")
        buf.write("\7q\2\2\u0242\u0243\7k\2\2\u0243\u0244\7e\2\2\u0244\u0245")
        buf.write("\7g\2\2\u0245N\3\2\2\2\u0246\u0247\7U\2\2\u0247\u0248")
        buf.write("\7g\2\2\u0248\u0249\7s\2\2\u0249\u024a\7w\2\2\u024a\u024b")
        buf.write("\7g\2\2\u024b\u024c\7p\2\2\u024c\u024d\7e\2\2\u024d\u024e")
        buf.write("\7g\2\2\u024eP\3\2\2\2\u024f\u0250\7N\2\2\u0250\u0251")
        buf.write("\7q\2\2\u0251\u0252\7i\2\2\u0252\u0253\7W\2\2\u0253\u0254")
        buf.write("\7p\2\2\u0254\u0255\7k\2\2\u0255\u0256\7h\2\2\u0256\u0257")
        buf.write("\7q\2\2\u0257\u0258\7t\2\2\u0258\u0259\7o\2\2\u0259R\3")
        buf.write("\2\2\2\u025a\u025b\5U+\2\u025b\u025c\b*\2\2\u025c\u025d")
        buf.write("\3\2\2\2\u025d\u025e\b*\3\2\u025eT\3\2\2\2\u025f\u0260")
        buf.write("\5\u00a9U\2\u0260\u0265\5\u00a9U\2\u0261\u0264\5U+\2\u0262")
        buf.write("\u0264\13\2\2\2\u0263\u0261\3\2\2\2\u0263\u0262\3\2\2")
        buf.write("\2\u0264\u0267\3\2\2\2\u0265\u0266\3\2\2\2\u0265\u0263")
        buf.write("\3\2\2\2\u0266\u0268\3\2\2\2\u0267\u0265\3\2\2\2\u0268")
        buf.write("\u0269\5\u00abV\2\u0269\u026a\5\u00abV\2\u026aV\3\2\2")
        buf.write("\2\u026b\u026c\7v\2\2\u026c\u026d\7q\2\2\u026dX\3\2\2")
        buf.write("\2\u026e\u026f\7q\2\2\u026f\u0270\7p\2\2\u0270Z\3\2\2")
        buf.write("\2\u0271\u0272\7c\2\2\u0272\u0273\7v\2\2\u0273\\\3\2\2")
        buf.write("\2\u0274\u0275\7c\2\2\u0275\u0276\7p\2\2\u0276\u0277\7")
        buf.write("f\2\2\u0277^\3\2\2\2\u0278\u0279\7f\2\2\u0279\u027a\7")
        buf.write("g\2\2\u027a\u027b\7h\2\2\u027b`\3\2\2\2\u027c\u027d\7")
        buf.write("g\2\2\u027d\u027e\7n\2\2\u027e\u027f\7u\2\2\u027f\u0280")
        buf.write("\7g\2\2\u0280b\3\2\2\2\u0281\u0282\7h\2\2\u0282\u0283")
        buf.write("\7c\2\2\u0283\u0284\7n\2\2\u0284\u0285\7u\2\2\u0285\u0286")
        buf.write("\7g\2\2\u0286d\3\2\2\2\u0287\u0288\7h\2\2\u0288\u0289")
        buf.write("\7q\2\2\u0289\u028a\7t\2\2\u028af\3\2\2\2\u028b\u028c")
        buf.write("\7k\2\2\u028c\u028d\7h\2\2\u028dh\3\2\2\2\u028e\u028f")
        buf.write("\7k\2\2\u028f\u0290\7p\2\2\u0290j\3\2\2\2\u0291\u0292")
        buf.write("\7k\2\2\u0292\u0293\7u\2\2\u0293l\3\2\2\2\u0294\u0295")
        buf.write("\7p\2\2\u0295\u0296\7q\2\2\u0296\u0297\7p\2\2\u0297\u0298")
        buf.write("\7g\2\2\u0298n\3\2\2\2\u0299\u029a\7p\2\2\u029a\u029b")
        buf.write("\7q\2\2\u029b\u029c\7v\2\2\u029cp\3\2\2\2\u029d\u029e")
        buf.write("\7q\2\2\u029e\u029f\7t\2\2\u029fr\3\2\2\2\u02a0\u02a1")
        buf.write("\7t\2\2\u02a1\u02a2\7g\2\2\u02a2\u02a3\7v\2\2\u02a3\u02a4")
        buf.write("\7w\2\2\u02a4\u02a5\7t\2\2\u02a5\u02a6\7p\2\2\u02a6t\3")
        buf.write("\2\2\2\u02a7\u02a8\7v\2\2\u02a8\u02a9\7t\2\2\u02a9\u02aa")
        buf.write("\7w\2\2\u02aa\u02ab\7g\2\2\u02abv\3\2\2\2\u02ac\u02ad")
        buf.write("\7a\2\2\u02adx\3\2\2\2\u02ae\u02af\7\60\2\2\u02afz\3\2")
        buf.write("\2\2\u02b0\u02b1\7\60\2\2\u02b1\u02b2\7\60\2\2\u02b2|")
        buf.write("\3\2\2\2\u02b3\u02b4\7\60\2\2\u02b4\u02b5\7\60\2\2\u02b5")
        buf.write("\u02b6\7\60\2\2\u02b6~\3\2\2\2\u02b7\u02b8\7.\2\2\u02b8")
        buf.write("\u0080\3\2\2\2\u02b9\u02ba\7<\2\2\u02ba\u0082\3\2\2\2")
        buf.write("\u02bb\u02bc\7=\2\2\u02bc\u0084\3\2\2\2\u02bd\u02be\7")
        buf.write("?\2\2\u02be\u0086\3\2\2\2\u02bf\u02c0\7~\2\2\u02c0\u0088")
        buf.write("\3\2\2\2\u02c1\u02c2\7`\2\2\u02c2\u008a\3\2\2\2\u02c3")
        buf.write("\u02c4\7(\2\2\u02c4\u008c\3\2\2\2\u02c5\u02c6\7\u0080")
        buf.write("\2\2\u02c6\u008e\3\2\2\2\u02c7\u02c8\7>\2\2\u02c8\u02c9")
        buf.write("\7>\2\2\u02c9\u0090\3\2\2\2\u02ca\u02cb\7@\2\2\u02cb\u02cc")
        buf.write("\7@\2\2\u02cc\u0092\3\2\2\2\u02cd\u02ce\7-\2\2\u02ce\u0094")
        buf.write("\3\2\2\2\u02cf\u02d0\7/\2\2\u02d0\u0096\3\2\2\2\u02d1")
        buf.write("\u02d2\7\61\2\2\u02d2\u0098\3\2\2\2\u02d3\u02d4\7,\2\2")
        buf.write("\u02d4\u009a\3\2\2\2\u02d5\u02d6\7'\2\2\u02d6\u009c\3")
        buf.write("\2\2\2\u02d7\u02d8\7\61\2\2\u02d8\u02d9\7\61\2\2\u02d9")
        buf.write("\u009e\3\2\2\2\u02da\u02db\7,\2\2\u02db\u02dc\7,\2\2\u02dc")
        buf.write("\u00a0\3\2\2\2\u02dd\u02de\7*\2\2\u02de\u02df\bQ\4\2\u02df")
        buf.write("\u00a2\3\2\2\2\u02e0\u02e1\7+\2\2\u02e1\u02e2\bR\5\2\u02e2")
        buf.write("\u00a4\3\2\2\2\u02e3\u02e4\7]\2\2\u02e4\u02e5\bS\6\2\u02e5")
        buf.write("\u00a6\3\2\2\2\u02e6\u02e7\7_\2\2\u02e7\u02e8\bT\7\2\u02e8")
        buf.write("\u00a8\3\2\2\2\u02e9\u02ea\7}\2\2\u02ea\u02eb\bU\b\2\u02eb")
        buf.write("\u00aa\3\2\2\2\u02ec\u02ed\7\177\2\2\u02ed\u02ee\bV\t")
        buf.write("\2\u02ee\u00ac\3\2\2\2\u02ef\u02f0\7>\2\2\u02f0\u00ae")
        buf.write("\3\2\2\2\u02f1\u02f2\7@\2\2\u02f2\u00b0\3\2\2\2\u02f3")
        buf.write("\u02f4\7?\2\2\u02f4\u02f5\7?\2\2\u02f5\u00b2\3\2\2\2\u02f6")
        buf.write("\u02f7\7@\2\2\u02f7\u02f8\7?\2\2\u02f8\u00b4\3\2\2\2\u02f9")
        buf.write("\u02fa\7>\2\2\u02fa\u02fb\7?\2\2\u02fb\u00b6\3\2\2\2\u02fc")
        buf.write("\u02fd\7#\2\2\u02fd\u02fe\7?\2\2\u02fe\u00b8\3\2\2\2\u02ff")
        buf.write("\u0300\7-\2\2\u0300\u0301\7?\2\2\u0301\u00ba\3\2\2\2\u0302")
        buf.write("\u0303\7/\2\2\u0303\u0304\7?\2\2\u0304\u00bc\3\2\2\2\u0305")
        buf.write("\u0306\7,\2\2\u0306\u0307\7?\2\2\u0307\u00be\3\2\2\2\u0308")
        buf.write("\u0309\7\61\2\2\u0309\u030a\7?\2\2\u030a\u00c0\3\2\2\2")
        buf.write("\u030b\u030c\7'\2\2\u030c\u030d\7?\2\2\u030d\u00c2\3")
        buf.write("\2\2\2\u030e\u030f\7(\2\2\u030f\u0310\7?\2\2\u0310\u00c4")
        buf.write("\3\2\2\2\u0311\u0312\7~\2\2\u0312\u0313\7?\2\2\u0313\u00c6")
        buf.write("\3\2\2\2\u0314\u0315\7`\2\2\u0315\u0316\7?\2\2\u0316\u00c8")
        buf.write("\3\2\2\2\u0317\u0318\7>\2\2\u0318\u0319\7>\2\2\u0319\u031a")
        buf.write("\7?\2\2\u031a\u00ca\3\2\2\2\u031b\u031c\7@\2\2\u031c\u031d")
        buf.write("\7@\2\2\u031d\u031e\7?\2\2\u031e\u00cc\3\2\2\2\u031f\u0320")
        buf.write("\7,\2\2\u0320\u0321\7,\2\2\u0321\u0322\7?\2\2\u0322\u00ce")
        buf.write("\3\2\2\2\u0323\u0324\7\61\2\2\u0324\u0325\7\61\2\2\u0325")
        buf.write("\u0326\7?\2\2\u0326\u00d0\3\2\2\2\u0327\u032b\5\u0105")
        buf.write("\u0083\2\u0328\u032a\5\u0107\u0084\2\u0329\u0328\3\2\2")
        buf.write("\2\u032a\u032d\3\2\2\2\u032b\u0329\3\2\2\2\u032b\u032c")
        buf.write("\3\2\2\2\u032c\u00d2\3\2\2\2\u032d\u032b\3\2\2\2\u032e")
        buf.write("\u032f\7&\2\2\u032f\u0330\5\u00d1i\2\u0330\u00d4\3\2\2")
        buf.write("\2\u0331\u0332\5\u00d9m\2\u0332\u00d6\3\2\2\2\u0333\u0336")
        buf.write("\5\u00dbn\2\u0334\u0336\5\u00e5s\2\u0335\u0333\3\2\2\2")
        buf.write("\u0335\u0334\3\2\2\2\u0336\u00d8\3\2\2\2\u0337\u0341\t")
        buf.write("\3\2\2\u0338\u033a\t\4\2\2\u0339\u0338\3\2\2\2\u0339\u033a")
        buf.write("\3\2\2\2\u033a\u033b\3\2\2\2\u033b\u0341\t\5\2\2\u033c")
        buf.write("\u033e\t\5\2\2\u033d\u033c\3\2\2\2\u033d\u033e\3\2\2\2")
        buf.write("\u033e\u033f\3\2\2\2\u033f\u0341\t\4\2\2\u0340\u0337\3")
        buf.write("\2\2\2\u0340\u0339\3\2\2\2\u0340\u033d\3\2\2\2\u0340\u0341")
        buf.write("\3\2\2\2\u0341\u0342\3\2\2\2\u0342\u0343\5\u00edw\2\u0343")
        buf.write("\u00da\3\2\2\2\u0344\u0349\5\u00ddo\2\u0345\u0349\5\u00df")
        buf.write("p\2\u0346\u0349\5\u00e1q\2\u0347\u0349\5\u00e3r\2\u0348")
        buf.write("\u0344\3\2\2\2\u0348\u0345\3\2\2\2\u0348\u0346\3\2\2\2")
        buf.write("\u0348\u0347\3\2\2\2\u0349\u00dc\3\2\2\2\u034a\u034e\5")
        buf.write("\u00f1y\2\u034b\u034d\5\u00f3z\2\u034c\u034b\3\2\2\2\u034d")
        buf.write("\u0350\3\2\2\2\u034e\u034c\3\2\2\2\u034e\u034f\3\2\2\2")
        buf.write("\u034f\u0357\3\2\2\2\u0350\u034e\3\2\2\2\u0351\u0353\7")
        buf.write("\62\2\2\u0352\u0351\3\2\2\2\u0353\u0354\3\2\2\2\u0354")
        buf.write("\u0352\3\2\2\2\u0354\u0355\3\2\2\2\u0355\u0357\3\2\2\2")
        buf.write("\u0356\u034a\3\2\2\2\u0356\u0352\3\2\2\2\u0357\u00de\3")
        buf.write("\2\2\2\u0358\u0359\7\62\2\2\u0359\u035b\t\6\2\2\u035a")
        buf.write("\u035c\5\u00f5{\2\u035b\u035a\3\2\2\2\u035c\u035d\3\2")
        buf.write("\2\2\u035d\u035b\3\2\2\2\u035d\u035e\3\2\2\2\u035e\u00e0")
        buf.write("\3\2\2\2\u035f\u0360\7\62\2\2\u0360\u0362\t\7\2\2\u0361")
        buf.write("\u0363\5\u00f7|\2\u0362\u0361\3\2\2\2\u0363\u0364\3\2")
        buf.write("\2\2\u0364\u0362\3\2\2\2\u0364\u0365\3\2\2\2\u0365\u00e2")
        buf.write("\3\2\2\2\u0366\u0367\7\62\2\2\u0367\u0369\t\b\2\2\u0368")
        buf.write("\u036a\5\u00f9}\2\u0369\u0368\3\2\2\2\u036a\u036b\3\2")
        buf.write("\2\2\u036b\u0369\3\2\2\2\u036b\u036c\3\2\2\2\u036c\u00e4")
        buf.write("\3\2\2\2\u036d\u0370\5\u00fb~\2\u036e\u0370\5\u00fd\177")
        buf.write("\2\u036f\u036d\3\2\2\2\u036f\u036e\3\2\2\2\u0370\u00e6")
        buf.write("\3\2\2\2\u0371\u0372\6t\2\2\u0372\u037e\5\u010b\u0086")
        buf.write("\2\u0373\u0375\7\17\2\2\u0374\u0373\3\2\2\2\u0374\u0375")
        buf.write("\3\2\2\2\u0375\u0376\3\2\2\2\u0376\u0379\7\f\2\2\u0377")
        buf.write("\u0379\4\16\17\2\u0378\u0374\3\2\2\2\u0378\u0377\3\2\2")
        buf.write("\2\u0379\u037b\3\2\2\2\u037a\u037c\5\u010b\u0086\2\u037b")
        buf.write("\u037a\3\2\2\2\u037b\u037c\3\2\2\2\u037c\u037e\3\2\2\2")
        buf.write("\u037d\u0371\3\2\2\2\u037d\u0378\3\2\2\2\u037e\u037f\3")
        buf.write("\2\2\2\u037f\u0380\bt\n\2\u0380\u00e8\3\2\2\2\u0381\u0385")
        buf.write("\5\u010b\u0086\2\u0382\u0385\5\u010d\u0087\2\u0383\u0385")
        buf.write("\5\u010f\u0088\2\u0384\u0381\3\2\2\2\u0384\u0382\3\2\2")
        buf.write("\2\u0384\u0383\3\2\2\2\u0385\u0386\3\2\2\2\u0386\u0387")
        buf.write("\bu\3\2\u0387\u00ea\3\2\2\2\u0388\u0389\13\2\2\2\u0389")
        buf.write("\u00ec\3\2\2\2\u038a\u038f\7)\2\2\u038b\u038e\5\u00ef")
        buf.write("x\2\u038c\u038e\n\t\2\2\u038d\u038b\3\2\2\2\u038d\u038c")
        buf.write("\3\2\2\2\u038e\u0391\3\2\2\2\u038f\u038d\3\2\2\2\u038f")
        buf.write("\u0390\3\2\2\2\u0390\u0392\3\2\2\2\u0391\u038f\3\2\2\2")
        buf.write("\u0392\u039d\7)\2\2\u0393\u0398\7$\2\2\u0394\u0397\5\u00ef")
        buf.write("x\2\u0395\u0397\n\n\2\2\u0396\u0394\3\2\2\2\u0396\u0395")
        buf.write("\3\2\2\2\u0397\u039a\3\2\2\2\u0398\u0396\3\2\2\2\u0398")
        buf.write("\u0399\3\2\2\2\u0399\u039b\3\2\2\2\u039a\u0398\3\2\2\2")
        buf.write("\u039b\u039d\7$\2\2\u039c\u038a\3\2\2\2\u039c\u0393\3")
        buf.write("\2\2\2\u039d\u00ee\3\2\2\2\u039e\u039f\7^\2\2\u039f\u03a3")
        buf.write("\13\2\2\2\u03a0\u03a1\7^\2\2\u03a1\u03a3\5\u00e7t\2\u03a2")
        buf.write("\u039e\3\2\2\2\u03a2\u03a0\3\2\2\2\u03a3\u00f0\3\2\2\2")
        buf.write("\u03a4\u03a5\4\63;\2\u03a5\u00f2\3\2\2\2\u03a6\u03a7\4")
        buf.write("\62;\2\u03a7\u00f4\3\2\2\2\u03a8\u03a9\4\629\2\u03a9\u00f6")
        buf.write("\3\2\2\2\u03aa\u03ad\5\u00f3z\2\u03ab\u03ad\t\13\2\2\u03ac")
        buf.write("\u03aa\3\2\2\2\u03ac\u03ab\3\2\2\2\u03ad\u00f8\3\2\2\2")
        buf.write("\u03ae\u03af\4\62\63\2\u03af\u00fa\3\2\2\2\u03b0\u03b2")
        buf.write("\5\u00ff\u0080\2\u03b1\u03b0\3\2\2\2\u03b1\u03b2\3\2\2")
        buf.write("\2\u03b2\u03b3\3\2\2\2\u03b3\u03b8\5\u0101\u0081\2\u03b4")
        buf.write("\u03b5\5\u00ff\u0080\2\u03b5\u03b6\7\60\2\2\u03b6\u03b8")
        buf.write("\3\2\2\2\u03b7\u03b1\3\2\2\2\u03b7\u03b4\3\2\2\2\u03b8")
        buf.write("\u00fc\3\2\2\2\u03b9\u03bc\5\u00ff\u0080\2\u03ba\u03bc")
        buf.write("\5\u00fb~\2\u03bb\u03b9\3\2\2\2\u03bb\u03ba\3\2\2\2\u03bc")
        buf.write("\u03bd\3\2\2\2\u03bd\u03be\5\u0103\u0082\2\u03be\u00fe")
        buf.write("\3\2\2\2\u03bf\u03c1\5\u00f3z\2\u03c0\u03bf\3\2\2\2\u03c1")
        buf.write("\u03c2\3\2\2\2\u03c2\u03c0\3\2\2\2\u03c2\u03c3\3\2\2\2")
        buf.write("\u03c3\u0100\3\2\2\2\u03c4\u03c6\7\60\2\2\u03c5\u03c7")
        buf.write("\5\u00f3z\2\u03c6\u03c5\3\2\2\2\u03c7\u03c8\3\2\2\2\u03c8")
        buf.write("\u03c6\3\2\2\2\u03c8\u03c9\3\2\2\2\u03c9\u0102\3\2\2\2")
        buf.write("\u03ca\u03cc\t\f\2\2\u03cb\u03cd\t\r\2\2\u03cc\u03cb\3")
        buf.write("\2\2\2\u03cc\u03cd\3\2\2\2\u03cd\u03cf\3\2\2\2\u03ce\u03d0")
        buf.write("\5\u00f3z\2\u03cf\u03ce\3\2\2\2\u03d0\u03d1\3\2\2\2\u03d1")
        buf.write("\u03cf\3\2\2\2\u03d1\u03d2\3\2\2\2\u03d2\u0104\3\2\2\2")
        buf.write("\u03d3\u03d6\5w<\2\u03d4\u03d6\5\u0109\u0085\2\u03d5\u03d3")
        buf.write("\3\2\2\2\u03d5\u03d4\3\2\2\2\u03d6\u0106\3\2\2\2\u03d7")
        buf.write("\u03da\5\u0105\u0083\2\u03d8\u03da\5\u00f3z\2\u03d9\u03d7")
        buf.write("\3\2\2\2\u03d9\u03d8\3\2\2\2\u03da\u0108\3\2\2\2\u03db")
        buf.write("\u03dc\t\16\2\2\u03dc\u010a\3\2\2\2\u03dd\u03df\t\17\2")
        buf.write("\2\u03de\u03dd\3\2\2\2\u03df\u03e0\3\2\2\2\u03e0\u03de")
        buf.write("\3\2\2\2\u03e0\u03e1\3\2\2\2\u03e1\u010c\3\2\2\2\u03e2")
        buf.write("\u03e6\7%\2\2\u03e3\u03e5\n\20\2\2\u03e4\u03e3\3\2\2\2")
        buf.write("\u03e5\u03e8\3\2\2\2\u03e6\u03e4\3\2\2\2\u03e6\u03e7\3")
        buf.write("\2\2\2\u03e7\u010e\3\2\2\2\u03e8\u03e6\3\2\2\2\u03e9\u03eb")
        buf.write("\7^\2\2\u03ea\u03ec\5\u010b\u0086\2\u03eb\u03ea\3\2\2")
        buf.write("\2\u03eb\u03ec\3\2\2\2\u03ec\u03f2\3\2\2\2\u03ed\u03ef")
        buf.write("\7\17\2\2\u03ee\u03ed\3\2\2\2\u03ee\u03ef\3\2\2\2\u03ef")
        buf.write("\u03f0\3\2\2\2\u03f0\u03f3\7\f\2\2\u03f1\u03f3\4\16\17")
        buf.write("\2\u03f2\u03ee\3\2\2\2\u03f2\u03f1\3\2\2\2\u03f3\u0110")
        buf.write("\3\2\2\2\62\2\u0132\u0158\u0203\u0221\u022c\u022e\u0263")
        buf.write("\u0265\u032b\u0335\u0339\u033d\u0340\u0348\u034e\u0354")
        buf.write("\u0356\u035d\u0364\u036b\u036f\u0374\u0378\u037b\u037d")
        buf.write("\u0384\u038d\u038f\u0396\u0398\u039c\u03a2\u03ac\u03b1")
        buf.write("\u03b7\u03bb\u03c2\u03c8\u03cc\u03d1\u03d5\u03d9\u03e0")
        buf.write("\u03e6\u03eb\u03ee\u03f2\13\3*\2\b\2\2\3Q\3\3R\4\3S\5")
        buf.write("\3T\6\3U\7\3V\b\3t\t")
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
            actions[79] = self.LPAREN_action
            actions[80] = self.RPAREN_action
            actions[81] = self.LBRACK_action
            actions[82] = self.RBRACK_action
            actions[83] = self.LBRACE_action
            actions[84] = self.RBRACE_action
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

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates is None:
            preds = dict()
            preds[114] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx: RuleContext, predIndex: int):
        if predIndex == 0:
            return self.atStartOfInput()
