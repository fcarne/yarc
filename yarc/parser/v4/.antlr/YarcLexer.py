# Generated from /media/federico/Data_Hdd/University/Magistrale/Secondo_Anno/LFC/Progetto/yarc/yarc/parser/v4/YarcLexer.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2i")
        buf.write("\u034a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("y\ty\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u018a\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0199\n\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u01a4\n")
        buf.write("\30\5\30\u01a6\n\30\3\31\3\31\3\31\7\31\u01ab\n\31\f\31")
        buf.write("\16\31\u01ae\13\31\5\31\u01b0\n\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write('\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3"\3"\3"\3#\3')
        buf.write("#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3'\3'\3'\3")
        buf.write("'\3'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3<\3<\3")
        buf.write("=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3I\3I\3J\3")
        buf.write("J\3J\3K\3K\3K\3L\3L\3L\3M\3M\3M\3N\3N\3N\3O\3O\3O\3P\3")
        buf.write("P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3V\3")
        buf.write("V\3V\3W\3W\3W\3W\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3")
        buf.write("[\3[\3\\\3\\\5\\\u0285\n\\\3]\3]\7]\u0289\n]\f]\16]\u028c")
        buf.write("\13]\3^\3^\3^\5^\u0291\n^\3^\3^\5^\u0295\n^\3^\5^\u0298")
        buf.write("\n^\5^\u029a\n^\3^\3^\3_\3_\5_\u02a0\n_\3_\3_\5_\u02a4")
        buf.write("\n_\3_\5_\u02a7\n_\3_\3_\3`\3`\3`\3`\5`\u02af\n`\3a\3")
        buf.write("a\7a\u02b3\na\fa\16a\u02b6\13a\3a\6a\u02b9\na\ra\16a\u02ba")
        buf.write("\5a\u02bd\na\3b\3b\3b\6b\u02c2\nb\rb\16b\u02c3\3c\3c\3")
        buf.write("c\6c\u02c9\nc\rc\16c\u02ca\3d\3d\3d\6d\u02d0\nd\rd\16")
        buf.write("d\u02d1\3e\3e\5e\u02d6\ne\3f\3f\3f\5f\u02db\nf\3f\3f\3")
        buf.write("g\3g\3h\3h\3h\7h\u02e4\nh\fh\16h\u02e7\13h\3h\3h\3h\3")
        buf.write("h\7h\u02ed\nh\fh\16h\u02f0\13h\3h\5h\u02f3\nh\3i\3i\3")
        buf.write("i\3i\5i\u02f9\ni\3j\3j\3k\3k\3l\3l\3m\3m\5m\u0303\nm\3")
        buf.write("n\3n\3o\5o\u0308\no\3o\3o\3o\3o\5o\u030e\no\3p\3p\5p\u0312")
        buf.write("\np\3p\3p\3q\6q\u0317\nq\rq\16q\u0318\3r\3r\6r\u031d\n")
        buf.write("r\rr\16r\u031e\3s\3s\5s\u0323\ns\3s\6s\u0326\ns\rs\16")
        buf.write("s\u0327\3t\6t\u032b\nt\rt\16t\u032c\3u\3u\7u\u0331\nu")
        buf.write("\fu\16u\u0334\13u\3v\3v\5v\u0338\nv\3v\5v\u033b\nv\3v")
        buf.write("\3v\5v\u033f\nv\3w\3w\5w\u0343\nw\3x\3x\5x\u0347\nx\3")
        buf.write("y\3y\3\u01ac\2z\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23")
        buf.write("\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25%\26'\27")
        buf.write(')\30+\31-\32/\33\61\2\63\34\65\35\67\369\37; =!?"A#C')
        buf.write("$E%G&I'K(M)O*Q+S,U-W.Y/[\60]\61_\62a\63c\64e\65g\66i")
        buf.write("\67k8m9o:q;s<u=w>y?{@}A\177B\u0081C\u0083D\u0085E\u0087")
        buf.write("F\u0089G\u008bH\u008dI\u008fJ\u0091K\u0093L\u0095M\u0097")
        buf.write("N\u0099O\u009bP\u009dQ\u009fR\u00a1S\u00a3T\u00a5U\u00a7")
        buf.write("V\u00a9W\u00abX\u00adY\u00afZ\u00b1[\u00b3\\\u00b5]\u00b7")
        buf.write("^\u00b9_\u00bb`\u00bda\u00bfb\u00c1c\u00c3d\u00c5e\u00c7")
        buf.write("f\u00c9g\u00cbh\u00cdi\u00cf\2\u00d1\2\u00d3\2\u00d5\2")
        buf.write("\u00d7\2\u00d9\2\u00db\2\u00dd\2\u00df\2\u00e1\2\u00e3")
        buf.write("\2\u00e5\2\u00e7\2\u00e9\2\u00eb\2\u00ed\2\u00ef\2\u00f1")
        buf.write("\2\3\2\20\4\2WWww\4\2HHhh\4\2TTtt\4\2QQqq\4\2ZZzz\4\2")
        buf.write("DDdd\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\4\2CHch\4\2G")
        buf.write('Ggg\4\2--//\4\2\13\13""\4\2\f\f\16\17\4\2C\\c|\2\u0369')
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3")
        buf.write("\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2")
        buf.write("\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\3\u00f3\3\2\2\2\5\u00fc")
        buf.write("\3\2\2\2\7\u0106\3\2\2\2\t\u010f\3\2\2\2\13\u0111\3\2")
        buf.write("\2\2\r\u011b\3\2\2\2\17\u0124\3\2\2\2\21\u012d\3\2\2\2")
        buf.write("\23\u0138\3\2\2\2\25\u0145\3\2\2\2\27\u014c\3\2\2\2\31")
        buf.write("\u0158\3\2\2\2\33\u015c\3\2\2\2\35\u015e\3\2\2\2\37\u0160")
        buf.write("\3\2\2\2!\u0162\3\2\2\2#\u0166\3\2\2\2%\u0170\3\2\2\2")
        buf.write("'\u0177\3\2\2\2)\u017d\3\2\2\2+\u018b\3\2\2\2-\u0191")
        buf.write("\3\2\2\2/\u019a\3\2\2\2\61\u01a7\3\2\2\2\63\u01b3\3\2")
        buf.write("\2\2\65\u01b7\3\2\2\2\67\u01ba\3\2\2\29\u01be\3\2\2\2")
        buf.write(";\u01c3\3\2\2\2=\u01c8\3\2\2\2?\u01ce\3\2\2\2A\u01d2\3")
        buf.write("\2\2\2C\u01d5\3\2\2\2E\u01d8\3\2\2\2G\u01db\3\2\2\2I\u01e0")
        buf.write("\3\2\2\2K\u01e4\3\2\2\2M\u01e7\3\2\2\2O\u01ec\3\2\2\2")
        buf.write("Q\u01f3\3\2\2\2S\u01f8\3\2\2\2U\u01fa\3\2\2\2W\u01ff\3")
        buf.write("\2\2\2Y\u0201\3\2\2\2[\u0204\3\2\2\2]\u0208\3\2\2\2_\u020a")
        buf.write("\3\2\2\2a\u020c\3\2\2\2c\u020e\3\2\2\2e\u0210\3\2\2\2")
        buf.write("g\u0212\3\2\2\2i\u0214\3\2\2\2k\u0216\3\2\2\2m\u0218\3")
        buf.write("\2\2\2o\u021a\3\2\2\2q\u021d\3\2\2\2s\u0220\3\2\2\2u\u0222")
        buf.write("\3\2\2\2w\u0224\3\2\2\2y\u0226\3\2\2\2{\u0228\3\2\2\2")
        buf.write("}\u022b\3\2\2\2\177\u022e\3\2\2\2\u0081\u0230\3\2\2\2")
        buf.write("\u0083\u0233\3\2\2\2\u0085\u0236\3\2\2\2\u0087\u0239\3")
        buf.write("\2\2\2\u0089\u023c\3\2\2\2\u008b\u023f\3\2\2\2\u008d\u0242")
        buf.write("\3\2\2\2\u008f\u0245\3\2\2\2\u0091\u0247\3\2\2\2\u0093")
        buf.write("\u0249\3\2\2\2\u0095\u024c\3\2\2\2\u0097\u024f\3\2\2\2")
        buf.write("\u0099\u0252\3\2\2\2\u009b\u0255\3\2\2\2\u009d\u0258\3")
        buf.write("\2\2\2\u009f\u025b\3\2\2\2\u00a1\u025e\3\2\2\2\u00a3\u0261")
        buf.write("\3\2\2\2\u00a5\u0264\3\2\2\2\u00a7\u0267\3\2\2\2\u00a9")
        buf.write("\u026a\3\2\2\2\u00ab\u026d\3\2\2\2\u00ad\u0270\3\2\2\2")
        buf.write("\u00af\u0274\3\2\2\2\u00b1\u0278\3\2\2\2\u00b3\u027c\3")
        buf.write("\2\2\2\u00b5\u0280\3\2\2\2\u00b7\u0284\3\2\2\2\u00b9\u0286")
        buf.write("\3\2\2\2\u00bb\u0299\3\2\2\2\u00bd\u02a6\3\2\2\2\u00bf")
        buf.write("\u02ae\3\2\2\2\u00c1\u02bc\3\2\2\2\u00c3\u02be\3\2\2\2")
        buf.write("\u00c5\u02c5\3\2\2\2\u00c7\u02cc\3\2\2\2\u00c9\u02d5\3")
        buf.write("\2\2\2\u00cb\u02da\3\2\2\2\u00cd\u02de\3\2\2\2\u00cf\u02f2")
        buf.write("\3\2\2\2\u00d1\u02f8\3\2\2\2\u00d3\u02fa\3\2\2\2\u00d5")
        buf.write("\u02fc\3\2\2\2\u00d7\u02fe\3\2\2\2\u00d9\u0302\3\2\2\2")
        buf.write("\u00db\u0304\3\2\2\2\u00dd\u030d\3\2\2\2\u00df\u0311\3")
        buf.write("\2\2\2\u00e1\u0316\3\2\2\2\u00e3\u031a\3\2\2\2\u00e5\u0320")
        buf.write("\3\2\2\2\u00e7\u032a\3\2\2\2\u00e9\u032e\3\2\2\2\u00eb")
        buf.write("\u0335\3\2\2\2\u00ed\u0342\3\2\2\2\u00ef\u0346\3\2\2\2")
        buf.write("\u00f1\u0348\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7")
        buf.write("e\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7c\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\4\3\2\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7r\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7p\2\2\u0102\u0103\7u\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0105\5\u008bF\2\u0105\6\3\2\2\2\u0106")
        buf.write("\u0107\7y\2\2\u0107\u0108\7t\2\2\u0108\u0109\7k\2\2\u0109")
        buf.write("\u010a\7v\2\2\u010a\u010b\7g\2\2\u010b\u010c\7t\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d\u010e\5\u008bF\2\u010e\b\3\2\2\2")
        buf.write("\u010f\u0110\5\61\31\2\u0110\n\3\2\2\2\u0111\u0112\7W")
        buf.write("\2\2\u0112\u0113\7p\2\2\u0113\u0114\7k\2\2\u0114\u0115")
        buf.write("\7h\2\2\u0115\u0116\7q\2\2\u0116\u0117\7t\2\2\u0117\u0118")
        buf.write("\7o\2\2\u0118\u0119\3\2\2\2\u0119\u011a\5\u0083B\2\u011a")
        buf.write("\f\3\2\2\2\u011b\u011c\7P\2\2\u011c\u011d\7q\2\2\u011d")
        buf.write("\u011e\7t\2\2\u011e\u011f\7o\2\2\u011f\u0120\7c\2\2\u0120")
        buf.write("\u0121\7n\2\2\u0121\u0122\3\2\2\2\u0122\u0123\5\u0083")
        buf.write("B\2\u0123\16\3\2\2\2\u0124\u0125\7E\2\2\u0125\u0126\7")
        buf.write("j\2\2\u0126\u0127\7q\2\2\u0127\u0128\7k\2\2\u0128\u0129")
        buf.write("\7e\2\2\u0129\u012a\7g\2\2\u012a\u012b\3\2\2\2\u012b\u012c")
        buf.write("\5\u0083B\2\u012c\20\3\2\2\2\u012d\u012e\7U\2\2\u012e")
        buf.write("\u012f\7g\2\2\u012f\u0130\7s\2\2\u0130\u0131\7w\2\2\u0131")
        buf.write("\u0132\7g\2\2\u0132\u0133\7p\2\2\u0133\u0134\7e\2\2\u0134")
        buf.write("\u0135\7g\2\2\u0135\u0136\3\2\2\2\u0136\u0137\5\u0083")
        buf.write("B\2\u0137\22\3\2\2\2\u0138\u0139\7N\2\2\u0139\u013a\7")
        buf.write("q\2\2\u013a\u013b\7i\2\2\u013b\u013c\7W\2\2\u013c\u013d")
        buf.write("\7p\2\2\u013d\u013e\7k\2\2\u013e\u013f\7h\2\2\u013f\u0140")
        buf.write("\7q\2\2\u0140\u0141\7t\2\2\u0141\u0142\7o\2\2\u0142\u0143")
        buf.write("\3\2\2\2\u0143\u0144\5\u0083B\2\u0144\24\3\2\2\2\u0145")
        buf.write("\u0146\7e\2\2\u0146\u0147\7t\2\2\u0147\u0148\7g\2\2\u0148")
        buf.write("\u0149\7c\2\2\u0149\u014a\7v\2\2\u014a\u014b\7g\2\2\u014b")
        buf.write("\26\3\2\2\2\u014c\u014d\7k\2\2\u014d\u014e\7p\2\2\u014e")
        buf.write("\u014f\7u\2\2\u014f\u0150\7v\2\2\u0150\u0151\7c\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152\u0153\7v\2\2\u0153\u0154\7k\2\2\u0154")
        buf.write("\u0155\7c\2\2\u0155\u0156\7v\2\2\u0156\u0157\7g\2\2\u0157")
        buf.write("\30\3\2\2\2\u0158\u0159\7i\2\2\u0159\u015a\7g\2\2\u015a")
        buf.write("\u015b\7v\2\2\u015b\32\3\2\2\2\u015c\u015d\7z\2\2\u015d")
        buf.write("\34\3\2\2\2\u015e\u015f\7{\2\2\u015f\36\3\2\2\2\u0160")
        buf.write("\u0161\7|\2\2\u0161 \3\2\2\2\u0162\u0163\7u\2\2\u0163")
        buf.write('\u0164\7g\2\2\u0164\u0165\7v\2\2\u0165"\3\2\2\2\u0166')
        buf.write("\u0167\7v\2\2\u0167\u0168\7t\2\2\u0168\u0169\7c\2\2\u0169")
        buf.write("\u016a\7p\2\2\u016a\u016b\7u\2\2\u016b\u016c\7n\2\2\u016c")
        buf.write("\u016d\7c\2\2\u016d\u016e\7v\2\2\u016e\u016f\7g\2\2\u016f")
        buf.write("$\3\2\2\2\u0170\u0171\7t\2\2\u0171\u0172\7q\2\2\u0172")
        buf.write("\u0173\7v\2\2\u0173\u0174\7c\2\2\u0174\u0175\7v\2\2\u0175")
        buf.write("\u0176\7g\2\2\u0176&\3\2\2\2\u0177\u0178\7u\2\2\u0178")
        buf.write("\u0179\7e\2\2\u0179\u017a\7c\2\2\u017a\u017b\7n\2\2\u017b")
        buf.write("\u017c\7g\2\2\u017c(\3\2\2\2\u017d\u017e\7u\2\2\u017e")
        buf.write("\u017f\7e\2\2\u017f\u0180\7c\2\2\u0180\u0181\7v\2\2\u0181")
        buf.write("\u0182\7v\2\2\u0182\u0183\7g\2\2\u0183\u0184\7t\2\2\u0184")
        buf.write("\u0189\3\2\2\2\u0185\u0186\7\64\2\2\u0186\u018a\7f\2\2")
        buf.write("\u0187\u0188\7\65\2\2\u0188\u018a\7f\2\2\u0189\u0185\3")
        buf.write("\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a*")
        buf.write("\3\2\2\2\u018b\u018c\7g\2\2\u018c\u018d\7x\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018e\u018f\7t\2\2\u018f\u0190\7{\2\2\u0190,\3")
        buf.write("\2\2\2\u0191\u0192\7h\2\2\u0192\u0193\7t\2\2\u0193\u0194")
        buf.write("\7c\2\2\u0194\u0195\7o\2\2\u0195\u0196\7g\2\2\u0196\u0198")
        buf.write("\3\2\2\2\u0197\u0199\7u\2\2\u0198\u0197\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199.\3\2\2\2\u019a\u019b\7u\2\2\u019b")
        buf.write("\u019c\7g\2\2\u019c\u019d\7e\2\2\u019d\u01a5\3\2\2\2\u019e")
        buf.write("\u019f\7q\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1\7f\2\2\u01a1")
        buf.write("\u01a3\3\2\2\2\u01a2\u01a4\7u\2\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u019e\3")
        buf.write("\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\60\3\2\2\2\u01a7\u01af")
        buf.write("\5\u008bF\2\u01a8\u01b0\5\61\31\2\u01a9\u01ab\13\2\2\2")
        buf.write("\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01af\u01a8\3\2\2\2\u01af\u01ac\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b2\5\u008dG\2\u01b2\62\3\2\2\2")
        buf.write("\u01b3\u01b4\7c\2\2\u01b4\u01b5\7p\2\2\u01b5\u01b6\7f")
        buf.write("\2\2\u01b6\64\3\2\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9\7")
        buf.write("u\2\2\u01b9\66\3\2\2\2\u01ba\u01bb\7f\2\2\u01bb\u01bc")
        buf.write("\7g\2\2\u01bc\u01bd\7h\2\2\u01bd8\3\2\2\2\u01be\u01bf")
        buf.write("\7g\2\2\u01bf\u01c0\7n\2\2\u01c0\u01c1\7k\2\2\u01c1\u01c2")
        buf.write("\7h\2\2\u01c2:\3\2\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5")
        buf.write("\7n\2\2\u01c5\u01c6\7u\2\2\u01c6\u01c7\7g\2\2\u01c7<\3")
        buf.write("\2\2\2\u01c8\u01c9\7H\2\2\u01c9\u01ca\7c\2\2\u01ca\u01cb")
        buf.write("\7n\2\2\u01cb\u01cc\7u\2\2\u01cc\u01cd\7g\2\2\u01cd>\3")
        buf.write("\2\2\2\u01ce\u01cf\7h\2\2\u01cf\u01d0\7q\2\2\u01d0\u01d1")
        buf.write("\7t\2\2\u01d1@\3\2\2\2\u01d2\u01d3\7k\2\2\u01d3\u01d4")
        buf.write("\7h\2\2\u01d4B\3\2\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7")
        buf.write("\7p\2\2\u01d7D\3\2\2\2\u01d8\u01d9\7k\2\2\u01d9\u01da")
        buf.write("\7u\2\2\u01daF\3\2\2\2\u01db\u01dc\7P\2\2\u01dc\u01dd")
        buf.write("\7q\2\2\u01dd\u01de\7p\2\2\u01de\u01df\7g\2\2\u01dfH\3")
        buf.write("\2\2\2\u01e0\u01e1\7p\2\2\u01e1\u01e2\7q\2\2\u01e2\u01e3")
        buf.write("\7v\2\2\u01e3J\3\2\2\2\u01e4\u01e5\7q\2\2\u01e5\u01e6")
        buf.write("\7t\2\2\u01e6L\3\2\2\2\u01e7\u01e8\7r\2\2\u01e8\u01e9")
        buf.write("\7c\2\2\u01e9\u01ea\7u\2\2\u01ea\u01eb\7u\2\2\u01ebN\3")
        buf.write("\2\2\2\u01ec\u01ed\7t\2\2\u01ed\u01ee\7g\2\2\u01ee\u01ef")
        buf.write("\7v\2\2\u01ef\u01f0\7w\2\2\u01f0\u01f1\7t\2\2\u01f1\u01f2")
        buf.write("\7p\2\2\u01f2P\3\2\2\2\u01f3\u01f4\7V\2\2\u01f4\u01f5")
        buf.write("\7t\2\2\u01f5\u01f6\7w\2\2\u01f6\u01f7\7g\2\2\u01f7R\3")
        buf.write("\2\2\2\u01f8\u01f9\7a\2\2\u01f9T\3\2\2\2\u01fa\u01fb\7")
        buf.write("y\2\2\u01fb\u01fc\7k\2\2\u01fc\u01fd\7v\2\2\u01fd\u01fe")
        buf.write("\7j\2\2\u01feV\3\2\2\2\u01ff\u0200\7\60\2\2\u0200X\3\2")
        buf.write("\2\2\u0201\u0202\7\60\2\2\u0202\u0203\7\60\2\2\u0203Z")
        buf.write("\3\2\2\2\u0204\u0205\7\60\2\2\u0205\u0206\7\60\2\2\u0206")
        buf.write("\u0207\7\60\2\2\u0207\\\3\2\2\2\u0208\u0209\7,\2\2\u0209")
        buf.write("^\3\2\2\2\u020a\u020b\7.\2\2\u020b`\3\2\2\2\u020c\u020d")
        buf.write("\7<\2\2\u020db\3\2\2\2\u020e\u020f\7=\2\2\u020fd\3\2\2")
        buf.write("\2\u0210\u0211\7?\2\2\u0211f\3\2\2\2\u0212\u0213\7~\2")
        buf.write("\2\u0213h\3\2\2\2\u0214\u0215\7`\2\2\u0215j\3\2\2\2\u0216")
        buf.write("\u0217\7(\2\2\u0217l\3\2\2\2\u0218\u0219\7\u0080\2\2\u0219")
        buf.write("n\3\2\2\2\u021a\u021b\7>\2\2\u021b\u021c\7>\2\2\u021c")
        buf.write("p\3\2\2\2\u021d\u021e\7@\2\2\u021e\u021f\7@\2\2\u021f")
        buf.write("r\3\2\2\2\u0220\u0221\7-\2\2\u0221t\3\2\2\2\u0222\u0223")
        buf.write("\7/\2\2\u0223v\3\2\2\2\u0224\u0225\7\61\2\2\u0225x\3\2")
        buf.write("\2\2\u0226\u0227\7'\2\2\u0227z\3\2\2\2\u0228\u0229\7")
        buf.write("\61\2\2\u0229\u022a\7\61\2\2\u022a|\3\2\2\2\u022b\u022c")
        buf.write("\7,\2\2\u022c\u022d\7,\2\2\u022d~\3\2\2\2\u022e\u022f")
        buf.write("\7B\2\2\u022f\u0080\3\2\2\2\u0230\u0231\7/\2\2\u0231\u0232")
        buf.write("\7@\2\2\u0232\u0082\3\2\2\2\u0233\u0234\7*\2\2\u0234\u0235")
        buf.write("\bB\2\2\u0235\u0084\3\2\2\2\u0236\u0237\7+\2\2\u0237\u0238")
        buf.write("\bC\3\2\u0238\u0086\3\2\2\2\u0239\u023a\7]\2\2\u023a\u023b")
        buf.write("\bD\4\2\u023b\u0088\3\2\2\2\u023c\u023d\7_\2\2\u023d\u023e")
        buf.write("\bE\5\2\u023e\u008a\3\2\2\2\u023f\u0240\7}\2\2\u0240\u0241")
        buf.write("\bF\6\2\u0241\u008c\3\2\2\2\u0242\u0243\7\177\2\2\u0243")
        buf.write("\u0244\bG\7\2\u0244\u008e\3\2\2\2\u0245\u0246\7>\2\2\u0246")
        buf.write("\u0090\3\2\2\2\u0247\u0248\7@\2\2\u0248\u0092\3\2\2\2")
        buf.write("\u0249\u024a\7?\2\2\u024a\u024b\7?\2\2\u024b\u0094\3\2")
        buf.write("\2\2\u024c\u024d\7@\2\2\u024d\u024e\7?\2\2\u024e\u0096")
        buf.write("\3\2\2\2\u024f\u0250\7>\2\2\u0250\u0251\7?\2\2\u0251\u0098")
        buf.write("\3\2\2\2\u0252\u0253\7#\2\2\u0253\u0254\7?\2\2\u0254\u009a")
        buf.write("\3\2\2\2\u0255\u0256\7-\2\2\u0256\u0257\7?\2\2\u0257\u009c")
        buf.write("\3\2\2\2\u0258\u0259\7/\2\2\u0259\u025a\7?\2\2\u025a\u009e")
        buf.write("\3\2\2\2\u025b\u025c\7,\2\2\u025c\u025d\7?\2\2\u025d\u00a0")
        buf.write("\3\2\2\2\u025e\u025f\7B\2\2\u025f\u0260\7?\2\2\u0260\u00a2")
        buf.write("\3\2\2\2\u0261\u0262\7\61\2\2\u0262\u0263\7?\2\2\u0263")
        buf.write("\u00a4\3\2\2\2\u0264\u0265\7'\2\2\u0265\u0266\7?\2\2")
        buf.write("\u0266\u00a6\3\2\2\2\u0267\u0268\7(\2\2\u0268\u0269\7")
        buf.write("?\2\2\u0269\u00a8\3\2\2\2\u026a\u026b\7~\2\2\u026b\u026c")
        buf.write("\7?\2\2\u026c\u00aa\3\2\2\2\u026d\u026e\7`\2\2\u026e\u026f")
        buf.write("\7?\2\2\u026f\u00ac\3\2\2\2\u0270\u0271\7>\2\2\u0271\u0272")
        buf.write("\7>\2\2\u0272\u0273\7?\2\2\u0273\u00ae\3\2\2\2\u0274\u0275")
        buf.write("\7@\2\2\u0275\u0276\7@\2\2\u0276\u0277\7?\2\2\u0277\u00b0")
        buf.write("\3\2\2\2\u0278\u0279\7,\2\2\u0279\u027a\7,\2\2\u027a\u027b")
        buf.write("\7?\2\2\u027b\u00b2\3\2\2\2\u027c\u027d\7\61\2\2\u027d")
        buf.write("\u027e\7\61\2\2\u027e\u027f\7?\2\2\u027f\u00b4\3\2\2\2")
        buf.write("\u0280\u0281\5\u00bd_\2\u0281\u00b6\3\2\2\2\u0282\u0285")
        buf.write("\5\u00bf`\2\u0283\u0285\5\u00c9e\2\u0284\u0282\3\2\2\2")
        buf.write("\u0284\u0283\3\2\2\2\u0285\u00b8\3\2\2\2\u0286\u028a\5")
        buf.write("\u00edw\2\u0287\u0289\5\u00efx\2\u0288\u0287\3\2\2\2\u0289")
        buf.write("\u028c\3\2\2\2\u028a\u0288\3\2\2\2\u028a\u028b\3\2\2\2")
        buf.write("\u028b\u00ba\3\2\2\2\u028c\u028a\3\2\2\2\u028d\u028e\6")
        buf.write("^\2\2\u028e\u029a\5\u00e7t\2\u028f\u0291\7\17\2\2\u0290")
        buf.write("\u028f\3\2\2\2\u0290\u0291\3\2\2\2\u0291\u0292\3\2\2\2")
        buf.write("\u0292\u0295\7\f\2\2\u0293\u0295\4\16\17\2\u0294\u0290")
        buf.write("\3\2\2\2\u0294\u0293\3\2\2\2\u0295\u0297\3\2\2\2\u0296")
        buf.write("\u0298\5\u00e7t\2\u0297\u0296\3\2\2\2\u0297\u0298\3\2")
        buf.write("\2\2\u0298\u029a\3\2\2\2\u0299\u028d\3\2\2\2\u0299\u0294")
        buf.write("\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u029c\b^\b\2\u029c")
        buf.write("\u00bc\3\2\2\2\u029d\u02a7\t\2\2\2\u029e\u02a0\t\3\2\2")
        buf.write("\u029f\u029e\3\2\2\2\u029f\u02a0\3\2\2\2\u02a0\u02a1\3")
        buf.write("\2\2\2\u02a1\u02a7\t\4\2\2\u02a2\u02a4\t\4\2\2\u02a3\u02a2")
        buf.write("\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5")
        buf.write("\u02a7\t\3\2\2\u02a6\u029d\3\2\2\2\u02a6\u029f\3\2\2\2")
        buf.write("\u02a6\u02a3\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7\u02a8\3")
        buf.write("\2\2\2\u02a8\u02a9\5\u00cfh\2\u02a9\u00be\3\2\2\2\u02aa")
        buf.write("\u02af\5\u00c1a\2\u02ab\u02af\5\u00c3b\2\u02ac\u02af\5")
        buf.write("\u00c5c\2\u02ad\u02af\5\u00c7d\2\u02ae\u02aa\3\2\2\2\u02ae")
        buf.write("\u02ab\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae\u02ad\3\2\2\2")
        buf.write("\u02af\u00c0\3\2\2\2\u02b0\u02b4\5\u00d3j\2\u02b1\u02b3")
        buf.write("\5\u00d5k\2\u02b2\u02b1\3\2\2\2\u02b3\u02b6\3\2\2\2\u02b4")
        buf.write("\u02b2\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b5\u02bd\3\2\2\2")
        buf.write("\u02b6\u02b4\3\2\2\2\u02b7\u02b9\7\62\2\2\u02b8\u02b7")
        buf.write("\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba\u02b8\3\2\2\2\u02ba")
        buf.write("\u02bb\3\2\2\2\u02bb\u02bd\3\2\2\2\u02bc\u02b0\3\2\2\2")
        buf.write("\u02bc\u02b8\3\2\2\2\u02bd\u00c2\3\2\2\2\u02be\u02bf\7")
        buf.write("\62\2\2\u02bf\u02c1\t\5\2\2\u02c0\u02c2\5\u00d7l\2\u02c1")
        buf.write("\u02c0\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c1\3\2\2\2")
        buf.write("\u02c3\u02c4\3\2\2\2\u02c4\u00c4\3\2\2\2\u02c5\u02c6\7")
        buf.write("\62\2\2\u02c6\u02c8\t\6\2\2\u02c7\u02c9\5\u00d9m\2\u02c8")
        buf.write("\u02c7\3\2\2\2\u02c9\u02ca\3\2\2\2\u02ca\u02c8\3\2\2\2")
        buf.write("\u02ca\u02cb\3\2\2\2\u02cb\u00c6\3\2\2\2\u02cc\u02cd\7")
        buf.write("\62\2\2\u02cd\u02cf\t\7\2\2\u02ce\u02d0\5\u00dbn\2\u02cf")
        buf.write("\u02ce\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02cf\3\2\2\2")
        buf.write("\u02d1\u02d2\3\2\2\2\u02d2\u00c8\3\2\2\2\u02d3\u02d6\5")
        buf.write("\u00ddo\2\u02d4\u02d6\5\u00dfp\2\u02d5\u02d3\3\2\2\2\u02d5")
        buf.write("\u02d4\3\2\2\2\u02d6\u00ca\3\2\2\2\u02d7\u02db\5\u00e7")
        buf.write("t\2\u02d8\u02db\5\u00e9u\2\u02d9\u02db\5\u00ebv\2\u02da")
        buf.write("\u02d7\3\2\2\2\u02da\u02d8\3\2\2\2\u02da\u02d9\3\2\2\2")
        buf.write("\u02db\u02dc\3\2\2\2\u02dc\u02dd\bf\t\2\u02dd\u00cc\3")
        buf.write("\2\2\2\u02de\u02df\13\2\2\2\u02df\u00ce\3\2\2\2\u02e0")
        buf.write("\u02e5\7)\2\2\u02e1\u02e4\5\u00d1i\2\u02e2\u02e4\n\b\2")
        buf.write("\2\u02e3\u02e1\3\2\2\2\u02e3\u02e2\3\2\2\2\u02e4\u02e7")
        buf.write("\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6")
        buf.write("\u02e8\3\2\2\2\u02e7\u02e5\3\2\2\2\u02e8\u02f3\7)\2\2")
        buf.write("\u02e9\u02ee\7$\2\2\u02ea\u02ed\5\u00d1i\2\u02eb\u02ed")
        buf.write("\n\t\2\2\u02ec\u02ea\3\2\2\2\u02ec\u02eb\3\2\2\2\u02ed")
        buf.write("\u02f0\3\2\2\2\u02ee\u02ec\3\2\2\2\u02ee\u02ef\3\2\2\2")
        buf.write("\u02ef\u02f1\3\2\2\2\u02f0\u02ee\3\2\2\2\u02f1\u02f3\7")
        buf.write("$\2\2\u02f2\u02e0\3\2\2\2\u02f2\u02e9\3\2\2\2\u02f3\u00d0")
        buf.write("\3\2\2\2\u02f4\u02f5\7^\2\2\u02f5\u02f9\13\2\2\2\u02f6")
        buf.write("\u02f7\7^\2\2\u02f7\u02f9\5\u00bb^\2\u02f8\u02f4\3\2\2")
        buf.write("\2\u02f8\u02f6\3\2\2\2\u02f9\u00d2\3\2\2\2\u02fa\u02fb")
        buf.write("\4\63;\2\u02fb\u00d4\3\2\2\2\u02fc\u02fd\4\62;\2\u02fd")
        buf.write("\u00d6\3\2\2\2\u02fe\u02ff\4\629\2\u02ff\u00d8\3\2\2\2")
        buf.write("\u0300\u0303\5\u00d5k\2\u0301\u0303\t\n\2\2\u0302\u0300")
        buf.write("\3\2\2\2\u0302\u0301\3\2\2\2\u0303\u00da\3\2\2\2\u0304")
        buf.write("\u0305\4\62\63\2\u0305\u00dc\3\2\2\2\u0306\u0308\5\u00e1")
        buf.write("q\2\u0307\u0306\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u0309")
        buf.write("\3\2\2\2\u0309\u030e\5\u00e3r\2\u030a\u030b\5\u00e1q\2")
        buf.write("\u030b\u030c\7\60\2\2\u030c\u030e\3\2\2\2\u030d\u0307")
        buf.write("\3\2\2\2\u030d\u030a\3\2\2\2\u030e\u00de\3\2\2\2\u030f")
        buf.write("\u0312\5\u00e1q\2\u0310\u0312\5\u00ddo\2\u0311\u030f\3")
        buf.write("\2\2\2\u0311\u0310\3\2\2\2\u0312\u0313\3\2\2\2\u0313\u0314")
        buf.write("\5\u00e5s\2\u0314\u00e0\3\2\2\2\u0315\u0317\5\u00d5k\2")
        buf.write("\u0316\u0315\3\2\2\2\u0317\u0318\3\2\2\2\u0318\u0316\3")
        buf.write("\2\2\2\u0318\u0319\3\2\2\2\u0319\u00e2\3\2\2\2\u031a\u031c")
        buf.write("\7\60\2\2\u031b\u031d\5\u00d5k\2\u031c\u031b\3\2\2\2\u031d")
        buf.write("\u031e\3\2\2\2\u031e\u031c\3\2\2\2\u031e\u031f\3\2\2\2")
        buf.write("\u031f\u00e4\3\2\2\2\u0320\u0322\t\13\2\2\u0321\u0323")
        buf.write("\t\f\2\2\u0322\u0321\3\2\2\2\u0322\u0323\3\2\2\2\u0323")
        buf.write("\u0325\3\2\2\2\u0324\u0326\5\u00d5k\2\u0325\u0324\3\2")
        buf.write("\2\2\u0326\u0327\3\2\2\2\u0327\u0325\3\2\2\2\u0327\u0328")
        buf.write("\3\2\2\2\u0328\u00e6\3\2\2\2\u0329\u032b\t\r\2\2\u032a")
        buf.write("\u0329\3\2\2\2\u032b\u032c\3\2\2\2\u032c\u032a\3\2\2\2")
        buf.write("\u032c\u032d\3\2\2\2\u032d\u00e8\3\2\2\2\u032e\u0332\7")
        buf.write("%\2\2\u032f\u0331\n\16\2\2\u0330\u032f\3\2\2\2\u0331\u0334")
        buf.write("\3\2\2\2\u0332\u0330\3\2\2\2\u0332\u0333\3\2\2\2\u0333")
        buf.write("\u00ea\3\2\2\2\u0334\u0332\3\2\2\2\u0335\u0337\7^\2\2")
        buf.write("\u0336\u0338\5\u00e7t\2\u0337\u0336\3\2\2\2\u0337\u0338")
        buf.write("\3\2\2\2\u0338\u033e\3\2\2\2\u0339\u033b\7\17\2\2\u033a")
        buf.write("\u0339\3\2\2\2\u033a\u033b\3\2\2\2\u033b\u033c\3\2\2\2")
        buf.write("\u033c\u033f\7\f\2\2\u033d\u033f\4\16\17\2\u033e\u033a")
        buf.write("\3\2\2\2\u033e\u033d\3\2\2\2\u033f\u00ec\3\2\2\2\u0340")
        buf.write("\u0343\5S*\2\u0341\u0343\5\u00f1y\2\u0342\u0340\3\2\2")
        buf.write("\2\u0342\u0341\3\2\2\2\u0343\u00ee\3\2\2\2\u0344\u0347")
        buf.write("\5\u00edw\2\u0345\u0347\5\u00d5k\2\u0346\u0344\3\2\2\2")
        buf.write("\u0346\u0345\3\2\2\2\u0347\u00f0\3\2\2\2\u0348\u0349\t")
        buf.write("\17\2\2\u0349\u00f2\3\2\2\2\60\2\u0189\u0198\u01a3\u01a5")
        buf.write("\u01ac\u01af\u0284\u028a\u0290\u0294\u0297\u0299\u029f")
        buf.write("\u02a3\u02a6\u02ae\u02b4\u02ba\u02bc\u02c3\u02ca\u02d1")
        buf.write("\u02d5\u02da\u02e3\u02e5\u02ec\u02ee\u02f2\u02f8\u0302")
        buf.write("\u0307\u030d\u0311\u0318\u031e\u0322\u0327\u032c\u0332")
        buf.write("\u0337\u033a\u033e\u0342\u0346\n\3B\2\3C\3\3D\4\3E\5\3")
        buf.write("F\6\3G\7\3^\b\b\2\2")
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
    SET = 18
    TRANSLATE = 19
    ROTATE = 20
    SCALE = 21
    SCATTER = 22
    EVERY = 23
    FRAMES = 24
    TIME = 25
    AND = 26
    AS = 27
    DEF = 28
    ELIF = 29
    ELSE = 30
    FALSE = 31
    FOR = 32
    IF = 33
    IN = 34
    IS = 35
    NONE = 36
    NOT = 37
    OR = 38
    PASS = 39
    RETURN = 40
    TRUE = 41
    UNDERSCORE = 42
    WITH = 43
    DOT = 44
    RANGE = 45
    ELLIPSIS = 46
    STAR = 47
    COMMA = 48
    COLON = 49
    SEMI_COLON = 50
    ASSIGN = 51
    BIT_OR = 52
    XOR = 53
    BIT_AND = 54
    BIT_NOT = 55
    LEFT_SHIFT = 56
    RIGHT_SHIFT = 57
    ADD = 58
    MINUS = 59
    DIV = 60
    MOD = 61
    IDIV = 62
    POWER = 63
    AT = 64
    ARROW = 65
    LPAREN = 66
    RPAREN = 67
    LBRACK = 68
    RBRACK = 69
    LBRACE = 70
    RBRACE = 71
    LESS_THAN = 72
    GREATER_THAN = 73
    EQUALS = 74
    GT_EQ = 75
    LT_EQ = 76
    NOT_EQ = 77
    ADD_ASSIGN = 78
    SUB_ASSIGN = 79
    MULT_ASSIGN = 80
    AT_ASSIGN = 81
    DIV_ASSIGN = 82
    MOD_ASSIGN = 83
    AND_ASSIGN = 84
    OR_ASSIGN = 85
    XOR_ASSIGN = 86
    LEFT_SHIFT_ASSIGN = 87
    RIGHT_SHIFT_ASSIGN = 88
    POWER_ASSIGN = 89
    IDIV_ASSIGN = 90
    STRING = 91
    NUMBER = 92
    NAME = 93
    NEWLINE = 94
    STRING_LITERAL = 95
    INTEGER = 96
    DECIMAL_INTEGER = 97
    OCT_INTEGER = 98
    HEX_INTEGER = 99
    BIN_INTEGER = 100
    FLOAT_NUMBER = 101
    SKIP_ = 102
    UNKNOWN_CHAR = 103

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = [
        "<INVALID>",
        "'scenario'",
        "'create'",
        "'instantiate'",
        "'get'",
        "'x'",
        "'y'",
        "'z'",
        "'set'",
        "'translate'",
        "'rotate'",
        "'scale'",
        "'every'",
        "'and'",
        "'as'",
        "'def'",
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
        "UNIFORM",
        "NORMAL",
        "CHOICE",
        "SEQUENCE",
        "LOG_UNIFORM",
        "CREATE",
        "INSTANTIATE",
        "GET",
        "X",
        "Y",
        "Z",
        "SET",
        "TRANSLATE",
        "ROTATE",
        "SCALE",
        "SCATTER",
        "EVERY",
        "FRAMES",
        "TIME",
        "AND",
        "AS",
        "DEF",
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
        "BIT_OR",
        "XOR",
        "BIT_AND",
        "BIT_NOT",
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
        "UNIFORM",
        "NORMAL",
        "CHOICE",
        "SEQUENCE",
        "LOG_UNIFORM",
        "CREATE",
        "INSTANTIATE",
        "GET",
        "X",
        "Y",
        "Z",
        "SET",
        "TRANSLATE",
        "ROTATE",
        "SCALE",
        "SCATTER",
        "EVERY",
        "FRAMES",
        "TIME",
        "NESTED_CODE",
        "AND",
        "AS",
        "DEF",
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
        "BIT_OR",
        "XOR",
        "BIT_AND",
        "BIT_NOT",
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
        "ID_START",
        "ID_CONTINUE",
        "LETTER",
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
            actions[64] = self.LPAREN_action
            actions[65] = self.RPAREN_action
            actions[66] = self.LBRACK_action
            actions[67] = self.RBRACK_action
            actions[68] = self.LBRACE_action
            actions[69] = self.RBRACE_action
            actions[92] = self.NEWLINE_action
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def LPAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 0:
            self.openBrace()

    def RPAREN_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 1:
            self.closeBrace()

    def LBRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 2:
            self.openBrace()

    def RBRACK_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 3:
            self.closeBrace()

    def LBRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 4:
            self.openBrace()

    def RBRACE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 5:
            self.closeBrace()

    def NEWLINE_action(self, localctx: RuleContext, actionIndex: int):
        if actionIndex == 6:
            self.onNewLine()

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates is None:
            preds = dict()
            preds[92] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx: RuleContext, predIndex: int):
        if predIndex == 0:
            return self.atStartOfInput()
