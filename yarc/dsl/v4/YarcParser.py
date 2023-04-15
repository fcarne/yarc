# Generated from c:\Users\feder\Desktop\University\Magistrale\Secondo_Anno\1_Linguaggi\Progetto\yarc\yarc\dsl\v4\YarcParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3k")
        buf.write("\u0311\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\7\2\u00a6\n\2\f\2")
        buf.write("\16\2\u00a9\13\2\3\2\3\2\3\3\3\3\5\3\u00af\n\3\3\4\3\4")
        buf.write("\3\4\7\4\u00b4\n\4\f\4\16\4\u00b7\13\4\3\4\5\4\u00ba\n")
        buf.write("\4\3\4\3\4\3\5\3\5\5\5\u00c0\n\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\7\6\u00c9\n\6\f\6\16\6\u00cc\13\6\5\6\u00ce\n\6")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u00d4\n\7\3\b\3\b\5\b\u00d8\n\b\3")
        buf.write("\b\3\b\3\b\5\b\u00dd\n\b\7\b\u00df\n\b\f\b\16\b\u00e2")
        buf.write("\13\b\3\b\5\b\u00e5\n\b\3\t\3\t\3\n\3\n\3\13\3\13\5\13")
        buf.write("\u00ed\n\13\3\f\3\f\3\f\5\f\u00f2\n\f\3\r\3\r\3\r\5\r")
        buf.write("\u00f7\n\r\3\16\3\16\3\16\7\16\u00fc\n\16\f\16\16\16\u00ff")
        buf.write("\13\16\3\16\5\16\u0102\n\16\3\17\3\17\3\17\7\17\u0107")
        buf.write("\n\17\f\17\16\17\u010a\13\17\3\20\3\20\3\20\7\20\u010f")
        buf.write("\n\20\f\20\16\20\u0112\13\20\3\21\3\21\3\21\5\21\u0117")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u0122\n\22\f\22\16\22\u0125\13\22\3\22\3\22\3\22\5\22")
        buf.write("\u012a\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u0135\n\23\3\24\3\24\3\24\3\24\7\24\u013b\n\24")
        buf.write("\f\24\16\24\u013e\13\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\5\25\u0146\n\25\3\26\3\26\3\26\3\26\6\26\u014c\n\26\r")
        buf.write("\26\16\26\u014d\3\26\3\26\5\26\u0152\n\26\3\27\3\27\3")
        buf.write("\27\5\27\u0157\n\27\3\27\5\27\u015a\n\27\3\30\3\30\6\30")
        buf.write("\u015e\n\30\r\30\16\30\u015f\3\30\5\30\u0163\n\30\3\31")
        buf.write("\3\31\3\31\5\31\u0168\n\31\3\32\3\32\3\32\3\33\3\33\5")
        buf.write("\33\u016f\n\33\3\34\3\34\5\34\u0173\n\34\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\7\36\u017c\n\36\f\36\16\36\u017f")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0189")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u0193\n \3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\5!\u019d\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\5\"\u01a7\n\"\3#\3#\3#\5#\u01ac\n#\3$\3$\3$\5$\u01b1")
        buf.write("\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+")
        buf.write("\3+\6+\u01c4\n+\r+\16+\u01c5\3,\3,\5,\u01ca\n,\3-\3-\3")
        buf.write("-\3-\3.\3.\5.\u01d2\n.\3.\3.\3.\5.\u01d7\n.\3.\5.\u01da")
        buf.write("\n.\3/\3/\3/\5/\u01df\n/\3\60\3\60\3\60\7\60\u01e4\n\60")
        buf.write("\f\60\16\60\u01e7\13\60\3\60\5\60\u01ea\n\60\3\61\3\61")
        buf.write("\5\61\u01ee\n\61\3\62\3\62\3\62\3\62\5\62\u01f4\n\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\5\63\u01fb\n\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u0204\n\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u020b\n\63\3\63\3\63\5\63\u020f\n\63\3\64")
        buf.write("\3\64\3\64\7\64\u0214\n\64\f\64\16\64\u0217\13\64\3\65")
        buf.write("\3\65\5\65\u021b\n\65\3\65\3\65\3\65\3\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u022b\n\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0233\n\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u023d\n\67\3\67")
        buf.write("\3\67\5\67\u0241\n\67\38\38\38\78\u0246\n8\f8\168\u0249")
        buf.write("\138\39\39\39\79\u024e\n9\f9\169\u0251\139\3:\3:\3:\3")
        buf.write(":\3;\3;\3;\3;\3;\3;\5;\u025d\n;\3<\3<\3=\3=\3=\7=\u0264")
        buf.write("\n=\f=\16=\u0267\13=\3>\3>\3>\7>\u026c\n>\f>\16>\u026f")
        buf.write("\13>\3?\3?\3?\5?\u0274\n?\3@\3@\3@\3@\7@\u027a\n@\f@\16")
        buf.write("@\u027d\13@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u028b")
        buf.write("\nA\3B\3B\3B\3C\3C\3C\7C\u0293\nC\fC\16C\u0296\13C\3D")
        buf.write("\3D\3D\7D\u029b\nD\fD\16D\u029e\13D\3E\3E\3E\7E\u02a3")
        buf.write("\nE\fE\16E\u02a6\13E\3F\3F\3F\7F\u02ab\nF\fF\16F\u02ae")
        buf.write("\13F\3G\3G\3G\7G\u02b3\nG\fG\16G\u02b6\13G\3H\3H\3H\7")
        buf.write("H\u02bb\nH\fH\16H\u02be\13H\3I\3I\3I\3J\3J\3J\6J\u02c6")
        buf.write("\nJ\rJ\16J\u02c7\3J\3J\3J\3J\5J\u02ce\nJ\3K\3K\3L\3L\3")
        buf.write("L\7L\u02d5\nL\fL\16L\u02d8\13L\3L\5L\u02db\nL\3M\3M\5")
        buf.write("M\u02df\nM\3M\3M\5M\u02e3\nM\3M\5M\u02e6\nM\5M\u02e8\n")
        buf.write("M\3N\3N\5N\u02ec\nN\3O\3O\5O\u02f0\nO\3O\3O\3O\5O\u02f5")
        buf.write("\nO\7O\u02f7\nO\fO\16O\u02fa\13O\3O\5O\u02fd\nO\3P\3P")
        buf.write("\3P\7P\u0302\nP\fP\16P\u0305\13P\3P\5P\u0308\nP\3Q\3Q")
        buf.write("\3R\6R\u030d\nR\rR\16R\u030e\3R\2\2S\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write("\u009c\u009e\u00a0\u00a2\2\b\3\2R^\3\2;<\3\2=>\4\2?BD")
        buf.write("D\4\2::=>\4\2..aa\2\u033b\2\u00a7\3\2\2\2\4\u00ae\3\2")
        buf.write("\2\2\6\u00b0\3\2\2\2\b\u00bf\3\2\2\2\n\u00c1\3\2\2\2\f")
        buf.write("\u00cf\3\2\2\2\16\u00d7\3\2\2\2\20\u00e6\3\2\2\2\22\u00e8")
        buf.write("\3\2\2\2\24\u00ea\3\2\2\2\26\u00ee\3\2\2\2\30\u00f3\3")
        buf.write("\2\2\2\32\u00f8\3\2\2\2\34\u0103\3\2\2\2\36\u010b\3\2")
        buf.write("\2\2 \u0116\3\2\2\2\"\u0118\3\2\2\2$\u012b\3\2\2\2&\u0136")
        buf.write("\3\2\2\2(\u0142\3\2\2\2*\u0151\3\2\2\2,\u0159\3\2\2\2")
        buf.write(".\u015b\3\2\2\2\60\u0167\3\2\2\2\62\u0169\3\2\2\2\64\u016e")
        buf.write("\3\2\2\2\66\u0172\3\2\2\28\u0174\3\2\2\2:\u0178\3\2\2")
        buf.write("\2<\u0188\3\2\2\2>\u0192\3\2\2\2@\u019c\3\2\2\2B\u01a6")
        buf.write("\3\2\2\2D\u01ab\3\2\2\2F\u01b0\3\2\2\2H\u01b2\3\2\2\2")
        buf.write("J\u01b4\3\2\2\2L\u01b6\3\2\2\2N\u01b8\3\2\2\2P\u01bb\3")
        buf.write("\2\2\2R\u01bd\3\2\2\2T\u01c0\3\2\2\2V\u01c9\3\2\2\2X\u01cb")
        buf.write("\3\2\2\2Z\u01d9\3\2\2\2\\\u01db\3\2\2\2^\u01e0\3\2\2\2")
        buf.write("`\u01ed\3\2\2\2b\u01f3\3\2\2\2d\u020e\3\2\2\2f\u0210\3")
        buf.write("\2\2\2h\u021a\3\2\2\2j\u021f\3\2\2\2l\u0240\3\2\2\2n\u0242")
        buf.write("\3\2\2\2p\u024a\3\2\2\2r\u0252\3\2\2\2t\u0256\3\2\2\2")
        buf.write("v\u025e\3\2\2\2x\u0260\3\2\2\2z\u0268\3\2\2\2|\u0273\3")
        buf.write("\2\2\2~\u0275\3\2\2\2\u0080\u028a\3\2\2\2\u0082\u028c")
        buf.write("\3\2\2\2\u0084\u028f\3\2\2\2\u0086\u0297\3\2\2\2\u0088")
        buf.write("\u029f\3\2\2\2\u008a\u02a7\3\2\2\2\u008c\u02af\3\2\2\2")
        buf.write("\u008e\u02b7\3\2\2\2\u0090\u02bf\3\2\2\2\u0092\u02cd\3")
        buf.write("\2\2\2\u0094\u02cf\3\2\2\2\u0096\u02d1\3\2\2\2\u0098\u02e7")
        buf.write("\3\2\2\2\u009a\u02e9\3\2\2\2\u009c\u02ef\3\2\2\2\u009e")
        buf.write("\u02fe\3\2\2\2\u00a0\u0309\3\2\2\2\u00a2\u030c\3\2\2\2")
        buf.write("\u00a4\u00a6\7i\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3")
        buf.write("\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7\2\2\3\u00ab")
        buf.write("\3\3\2\2\2\u00ac\u00af\5\6\4\2\u00ad\u00af\5 \21\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\5\3\2\2\2\u00b0")
        buf.write("\u00b5\5\b\5\2\u00b1\u00b2\7\65\2\2\u00b2\u00b4\5\b\5")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b8\u00ba\7\65\2\2\u00b9\u00b8\3\2\2")
        buf.write("\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc")
        buf.write("\7i\2\2\u00bc\7\3\2\2\2\u00bd\u00c0\5\n\6\2\u00be\u00c0")
        buf.write("\5\22\n\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write("\t\3\2\2\2\u00c1\u00cd\5\16\b\2\u00c2\u00ce\5\f\7\2\u00c3")
        buf.write("\u00c4\5\20\t\2\u00c4\u00c5\5\u009eP\2\u00c5\u00ce\3\2")
        buf.write("\2\2\u00c6\u00c7\7\66\2\2\u00c7\u00c9\5\16\b\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cd\u00c2\3\2\2\2\u00cd\u00c3\3\2\2\2\u00cd\u00ca\3")
        buf.write("\2\2\2\u00ce\13\3\2\2\2\u00cf\u00d0\7\64\2\2\u00d0\u00d3")
        buf.write("\5t;\2\u00d1\u00d2\7\66\2\2\u00d2\u00d4\5t;\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\r\3\2\2\2\u00d5\u00d8")
        buf.write("\5t;\2\u00d6\u00d8\5\u0082B\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\u00e0\3\2\2\2\u00d9\u00dc\7\63\2")
        buf.write("\2\u00da\u00dd\5t;\2\u00db\u00dd\5\u0082B\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00d9\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3")
        buf.write("\2\2\2\u00e3\u00e5\7\63\2\2\u00e4\u00e3\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\17\3\2\2\2\u00e6\u00e7\t\2\2\2\u00e7")
        buf.write("\21\3\2\2\2\u00e8\u00e9\7+\2\2\u00e9\23\3\2\2\2\u00ea")
        buf.write("\u00ec\7,\2\2\u00eb\u00ed\5\u009eP\2\u00ec\u00eb\3\2\2")
        buf.write("\2\u00ec\u00ed\3\2\2\2\u00ed\25\3\2\2\2\u00ee\u00f1\5")
        buf.write("\u0094K\2\u00ef\u00f0\7\37\2\2\u00f0\u00f2\5\u0094K\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\27\3\2")
        buf.write("\2\2\u00f3\u00f6\5\36\20\2\u00f4\u00f5\7\37\2\2\u00f5")
        buf.write("\u00f7\5\u0094K\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2")
        buf.write("\2\2\u00f7\31\3\2\2\2\u00f8\u00fd\5\26\f\2\u00f9\u00fa")
        buf.write("\7\63\2\2\u00fa\u00fc\5\26\f\2\u00fb\u00f9\3\2\2\2\u00fc")
        buf.write("\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0102\7")
        buf.write("\63\2\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\33\3\2\2\2\u0103\u0108\5\30\r\2\u0104\u0105\7\63\2\2")
        buf.write("\u0105\u0107\5\30\r\2\u0106\u0104\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\35\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u0110\5\u0094K\2")
        buf.write("\u010c\u010d\7\60\2\2\u010d\u010f\5\u0094K\2\u010e\u010c")
        buf.write("\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\37\3\2\2\2\u0112\u0110\3\2\2\2\u0113")
        buf.write("\u0117\5\"\22\2\u0114\u0117\5$\23\2\u0115\u0117\5&\24")
        buf.write("\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117!\3\2\2\2\u0118\u0119\7%\2\2\u0119\u011a")
        buf.write("\5t;\2\u011a\u011b\7\64\2\2\u011b\u0123\5*\26\2\u011c")
        buf.write("\u011d\7!\2\2\u011d\u011e\5t;\2\u011e\u011f\7\64\2\2\u011f")
        buf.write("\u0120\5*\26\2\u0120\u0122\3\2\2\2\u0121\u011c\3\2\2\2")
        buf.write("\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3")
        buf.write("\2\2\2\u0124\u0129\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127")
        buf.write("\7\"\2\2\u0127\u0128\7\64\2\2\u0128\u012a\5*\26\2\u0129")
        buf.write("\u0126\3\2\2\2\u0129\u012a\3\2\2\2\u012a#\3\2\2\2\u012b")
        buf.write("\u012c\7$\2\2\u012c\u012d\5\u009cO\2\u012d\u012e\7&\2")
        buf.write("\2\u012e\u012f\5\u009eP\2\u012f\u0130\7\64\2\2\u0130\u0134")
        buf.write("\5*\26\2\u0131\u0132\7\"\2\2\u0132\u0133\7\64\2\2\u0133")
        buf.write("\u0135\5*\26\2\u0134\u0131\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135%\3\2\2\2\u0136\u0137\7/\2\2\u0137\u013c\5(\25\2")
        buf.write("\u0138\u0139\7\63\2\2\u0139\u013b\5(\25\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u013c\3\2\2\2")
        buf.write("\u013f\u0140\7\64\2\2\u0140\u0141\5*\26\2\u0141\'\3\2")
        buf.write("\2\2\u0142\u0145\5t;\2\u0143\u0144\7\37\2\2\u0144\u0146")
        buf.write("\5\u0084C\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write(")\3\2\2\2\u0147\u0152\5\6\4\2\u0148\u0149\7i\2\2\u0149")
        buf.write("\u014b\7\3\2\2\u014a\u014c\5\4\3\2\u014b\u014a\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3")
        buf.write("\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\7\4\2\2\u0150\u0152")
        buf.write("\3\2\2\2\u0151\u0147\3\2\2\2\u0151\u0148\3\2\2\2\u0152")
        buf.write("+\3\2\2\2\u0153\u0154\5\60\31\2\u0154\u0156\7\63\2\2\u0155")
        buf.write("\u0157\5.\30\2\u0156\u0155\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\u015a\3\2\2\2\u0158\u015a\5t;\2\u0159\u0153\3\2")
        buf.write("\2\2\u0159\u0158\3\2\2\2\u015a-\3\2\2\2\u015b\u015d\7")
        buf.write("\63\2\2\u015c\u015e\5\60\31\2\u015d\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2")
        buf.write("\u0160\u0162\3\2\2\2\u0161\u0163\7\63\2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163/\3\2\2\2\u0164\u0165")
        buf.write("\7@\2\2\u0165\u0168\5\u0084C\2\u0166\u0168\5t;\2\u0167")
        buf.write("\u0164\3\2\2\2\u0167\u0166\3\2\2\2\u0168\61\3\2\2\2\u0169")
        buf.write("\u016a\7%\2\2\u016a\u016b\5t;\2\u016b\63\3\2\2\2\u016c")
        buf.write("\u016f\5\\/\2\u016d\u016f\5\66\34\2\u016e\u016c\3\2\2")
        buf.write("\2\u016e\u016d\3\2\2\2\u016f\65\3\2\2\2\u0170\u0173\5")
        buf.write("8\35\2\u0171\u0173\5:\36\2\u0172\u0170\3\2\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173\67\3\2\2\2\u0174\u0175\5:\36\2\u0175\u0176")
        buf.write("\7\37\2\2\u0176\u0177\5N(\2\u01779\3\2\2\2\u0178\u017d")
        buf.write("\5<\37\2\u0179\u017a\7\67\2\2\u017a\u017c\5<\37\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017e;\3\2\2\2\u017f\u017d\3\2\2")
        buf.write("\2\u0180\u0189\5> \2\u0181\u0189\5L\'\2\u0182\u0189\5")
        buf.write("P)\2\u0183\u0189\5R*\2\u0184\u0189\5X-\2\u0185\u0189\5")
        buf.write("Z.\2\u0186\u0189\5d\63\2\u0187\u0189\5l\67\2\u0188\u0180")
        buf.write("\3\2\2\2\u0188\u0181\3\2\2\2\u0188\u0182\3\2\2\2\u0188")
        buf.write("\u0183\3\2\2\2\u0188\u0184\3\2\2\2\u0188\u0185\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189=\3\2\2")
        buf.write("\2\u018a\u018b\5D#\2\u018b\u018c\6 \2\3\u018c\u0193\3")
        buf.write("\2\2\2\u018d\u0193\5B\"\2\u018e\u0193\5\u00a2R\2\u018f")
        buf.write("\u0193\7(\2\2\u0190\u0193\7-\2\2\u0191\u0193\7#\2\2\u0192")
        buf.write("\u018a\3\2\2\2\u0192\u018d\3\2\2\2\u0192\u018e\3\2\2\2")
        buf.write("\u0192\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3")
        buf.write("\2\2\2\u0193?\3\2\2\2\u0194\u0195\5D#\2\u0195\u0196\6")
        buf.write("!\3\3\u0196\u019d\3\2\2\2\u0197\u019d\5B\"\2\u0198\u019d")
        buf.write("\5\u00a2R\2\u0199\u019d\7(\2\2\u019a\u019d\7-\2\2\u019b")
        buf.write("\u019d\7#\2\2\u019c\u0194\3\2\2\2\u019c\u0197\3\2\2\2")
        buf.write("\u019c\u0198\3\2\2\2\u019c\u0199\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019c\u019b\3\2\2\2\u019dA\3\2\2\2\u019e\u019f")
        buf.write("\5F$\2\u019f\u01a0\7=\2\2\u01a0\u01a1\5J&\2\u01a1\u01a7")
        buf.write("\3\2\2\2\u01a2\u01a3\5F$\2\u01a3\u01a4\7>\2\2\u01a4\u01a5")
        buf.write("\5J&\2\u01a5\u01a7\3\2\2\2\u01a6\u019e\3\2\2\2\u01a6\u01a2")
        buf.write("\3\2\2\2\u01a7C\3\2\2\2\u01a8\u01ac\7`\2\2\u01a9\u01aa")
        buf.write("\7>\2\2\u01aa\u01ac\7`\2\2\u01ab\u01a8\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01acE\3\2\2\2\u01ad\u01b1\5H%\2\u01ae\u01af")
        buf.write("\7>\2\2\u01af\u01b1\5H%\2\u01b0\u01ad\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b1G\3\2\2\2\u01b2\u01b3\7`\2\2\u01b3I\3\2")
        buf.write("\2\2\u01b4\u01b5\7`\2\2\u01b5K\3\2\2\2\u01b6\u01b7\5N")
        buf.write("(\2\u01b7M\3\2\2\2\u01b8\u01b9\5\u0094K\2\u01b9\u01ba")
        buf.write("\6(\4\3\u01baO\3\2\2\2\u01bb\u01bc\7.\2\2\u01bcQ\3\2\2")
        buf.write("\2\u01bd\u01be\5T+\2\u01be\u01bf\6*\5\3\u01bfS\3\2\2\2")
        buf.write("\u01c0\u01c3\5\u0094K\2\u01c1\u01c2\7\60\2\2\u01c2\u01c4")
        buf.write("\5\u0094K\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6U\3\2\2\2\u01c7")
        buf.write("\u01ca\5T+\2\u01c8\u01ca\5\u0094K\2\u01c9\u01c7\3\2\2")
        buf.write("\2\u01c9\u01c8\3\2\2\2\u01caW\3\2\2\2\u01cb\u01cc\7F\2")
        buf.write("\2\u01cc\u01cd\5\66\34\2\u01cd\u01ce\7G\2\2\u01ceY\3\2")
        buf.write("\2\2\u01cf\u01d1\7H\2\2\u01d0\u01d2\5^\60\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01da\7I\2\2\u01d4\u01d6\7F\2\2\u01d5\u01d7\5\\/\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u01da\7G\2\2\u01d9\u01cf\3\2\2\2\u01d9\u01d4\3")
        buf.write("\2\2\2\u01da[\3\2\2\2\u01db\u01dc\5`\61\2\u01dc\u01de")
        buf.write("\7\63\2\2\u01dd\u01df\5^\60\2\u01de\u01dd\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df]\3\2\2\2\u01e0\u01e5\5`\61\2\u01e1")
        buf.write("\u01e2\7\63\2\2\u01e2\u01e4\5`\61\2\u01e3\u01e1\3\2\2")
        buf.write("\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8")
        buf.write("\u01ea\7\63\2\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea\3\2\2")
        buf.write("\2\u01ea_\3\2\2\2\u01eb\u01ee\5b\62\2\u01ec\u01ee\5\66")
        buf.write("\34\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01eea\3")
        buf.write("\2\2\2\u01ef\u01f0\7@\2\2\u01f0\u01f4\5N(\2\u01f1\u01f2")
        buf.write("\7@\2\2\u01f2\u01f4\5P)\2\u01f3\u01ef\3\2\2\2\u01f3\u01f1")
        buf.write("\3\2\2\2\u01f4c\3\2\2\2\u01f5\u01f6\7J\2\2\u01f6\u020f")
        buf.write("\7K\2\2\u01f7\u01f8\7J\2\2\u01f8\u01fa\5j\66\2\u01f9\u01fb")
        buf.write("\7\63\2\2\u01fa\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fc\u01fd\7K\2\2\u01fd\u020f\3\2\2\2")
        buf.write("\u01fe\u01ff\7J\2\2\u01ff\u0200\5f\64\2\u0200\u0201\7")
        buf.write("\63\2\2\u0201\u0203\5j\66\2\u0202\u0204\7\63\2\2\u0203")
        buf.write("\u0202\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0206\7K\2\2\u0206\u020f\3\2\2\2\u0207\u0208\7")
        buf.write("J\2\2\u0208\u020a\5f\64\2\u0209\u020b\7\63\2\2\u020a\u0209")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("\u020d\7K\2\2\u020d\u020f\3\2\2\2\u020e\u01f5\3\2\2\2")
        buf.write("\u020e\u01f7\3\2\2\2\u020e\u01fe\3\2\2\2\u020e\u0207\3")
        buf.write("\2\2\2\u020fe\3\2\2\2\u0210\u0215\5h\65\2\u0211\u0212")
        buf.write("\7\63\2\2\u0212\u0214\5h\65\2\u0213\u0211\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216g\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021b\5@!\2")
        buf.write("\u0219\u021b\5T+\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2")
        buf.write("\2\2\u021b\u021c\3\2\2\2\u021c\u021d\7\64\2\2\u021d\u021e")
        buf.write("\5\66\34\2\u021ei\3\2\2\2\u021f\u0220\7C\2\2\u0220\u0221")
        buf.write("\5N(\2\u0221k\3\2\2\2\u0222\u0223\5V,\2\u0223\u0224\7")
        buf.write("F\2\2\u0224\u0225\7G\2\2\u0225\u0241\3\2\2\2\u0226\u0227")
        buf.write("\5V,\2\u0227\u0228\7F\2\2\u0228\u022a\5n8\2\u0229\u022b")
        buf.write("\7\63\2\2\u022a\u0229\3\2\2\2\u022a\u022b\3\2\2\2\u022b")
        buf.write("\u022c\3\2\2\2\u022c\u022d\7G\2\2\u022d\u0241\3\2\2\2")
        buf.write("\u022e\u022f\5V,\2\u022f\u0230\7F\2\2\u0230\u0232\5p9")
        buf.write("\2\u0231\u0233\7\63\2\2\u0232\u0231\3\2\2\2\u0232\u0233")
        buf.write("\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\7G\2\2\u0235")
        buf.write("\u0241\3\2\2\2\u0236\u0237\5V,\2\u0237\u0238\7F\2\2\u0238")
        buf.write("\u0239\5n8\2\u0239\u023a\7\63\2\2\u023a\u023c\5p9\2\u023b")
        buf.write("\u023d\7\63\2\2\u023c\u023b\3\2\2\2\u023c\u023d\3\2\2")
        buf.write("\2\u023d\u023e\3\2\2\2\u023e\u023f\7G\2\2\u023f\u0241")
        buf.write("\3\2\2\2\u0240\u0222\3\2\2\2\u0240\u0226\3\2\2\2\u0240")
        buf.write("\u022e\3\2\2\2\u0240\u0236\3\2\2\2\u0241m\3\2\2\2\u0242")
        buf.write("\u0247\5\66\34\2\u0243\u0244\7\63\2\2\u0244\u0246\5\66")
        buf.write("\34\2\u0245\u0243\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245")
        buf.write("\3\2\2\2\u0247\u0248\3\2\2\2\u0248o\3\2\2\2\u0249\u0247")
        buf.write("\3\2\2\2\u024a\u024f\5r:\2\u024b\u024c\7\63\2\2\u024c")
        buf.write("\u024e\5r:\2\u024d\u024b\3\2\2\2\u024e\u0251\3\2\2\2\u024f")
        buf.write("\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250q\3\2\2\2\u0251")
        buf.write("\u024f\3\2\2\2\u0252\u0253\5\u0094K\2\u0253\u0254\7\66")
        buf.write("\2\2\u0254\u0255\5\66\34\2\u0255s\3\2\2\2\u0256\u025c")
        buf.write("\5x=\2\u0257\u0258\7%\2\2\u0258\u0259\5x=\2\u0259\u025a")
        buf.write("\7\"\2\2\u025a\u025b\5t;\2\u025b\u025d\3\2\2\2\u025c\u0257")
        buf.write("\3\2\2\2\u025c\u025d\3\2\2\2\u025du\3\2\2\2\u025e\u025f")
        buf.write("\5x=\2\u025fw\3\2\2\2\u0260\u0265\5z>\2\u0261\u0262\7")
        buf.write("*\2\2\u0262\u0264\5z>\2\u0263\u0261\3\2\2\2\u0264\u0267")
        buf.write("\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266")
        buf.write("y\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u026d\5|?\2\u0269")
        buf.write("\u026a\7\36\2\2\u026a\u026c\5|?\2\u026b\u0269\3\2\2\2")
        buf.write("\u026c\u026f\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3")
        buf.write("\2\2\2\u026e{\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271")
        buf.write("\7)\2\2\u0271\u0274\5|?\2\u0272\u0274\5~@\2\u0273\u0270")
        buf.write("\3\2\2\2\u0273\u0272\3\2\2\2\u0274}\3\2\2\2\u0275\u027b")
        buf.write("\5\u0084C\2\u0276\u0277\5\u0080A\2\u0277\u0278\5\u0084")
        buf.write("C\2\u0278\u027a\3\2\2\2\u0279\u0276\3\2\2\2\u027a\u027d")
        buf.write("\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c")
        buf.write("\177\3\2\2\2\u027d\u027b\3\2\2\2\u027e\u028b\7L\2\2\u027f")
        buf.write("\u028b\7M\2\2\u0280\u028b\7N\2\2\u0281\u028b\7O\2\2\u0282")
        buf.write("\u028b\7P\2\2\u0283\u028b\7Q\2\2\u0284\u028b\7&\2\2\u0285")
        buf.write("\u0286\7)\2\2\u0286\u028b\7&\2\2\u0287\u028b\7\'\2\2\u0288")
        buf.write("\u0289\7\'\2\2\u0289\u028b\7)\2\2\u028a\u027e\3\2\2\2")
        buf.write("\u028a\u027f\3\2\2\2\u028a\u0280\3\2\2\2\u028a\u0281\3")
        buf.write("\2\2\2\u028a\u0282\3\2\2\2\u028a\u0283\3\2\2\2\u028a\u0284")
        buf.write("\3\2\2\2\u028a\u0285\3\2\2\2\u028a\u0287\3\2\2\2\u028a")
        buf.write("\u0288\3\2\2\2\u028b\u0081\3\2\2\2\u028c\u028d\7@\2\2")
        buf.write("\u028d\u028e\5\u0084C\2\u028e\u0083\3\2\2\2\u028f\u0294")
        buf.write("\5\u0086D\2\u0290\u0291\7\67\2\2\u0291\u0293\5\u0086D")
        buf.write("\2\u0292\u0290\3\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292")
        buf.write("\3\2\2\2\u0294\u0295\3\2\2\2\u0295\u0085\3\2\2\2\u0296")
        buf.write("\u0294\3\2\2\2\u0297\u029c\5\u0088E\2\u0298\u0299\78\2")
        buf.write("\2\u0299\u029b\5\u0088E\2\u029a\u0298\3\2\2\2\u029b\u029e")
        buf.write("\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029d\3\2\2\2\u029d")
        buf.write("\u0087\3\2\2\2\u029e\u029c\3\2\2\2\u029f\u02a4\5\u008a")
        buf.write("F\2\u02a0\u02a1\79\2\2\u02a1\u02a3\5\u008aF\2\u02a2\u02a0")
        buf.write("\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4")
        buf.write("\u02a5\3\2\2\2\u02a5\u0089\3\2\2\2\u02a6\u02a4\3\2\2\2")
        buf.write("\u02a7\u02ac\5\u008cG\2\u02a8\u02a9\t\3\2\2\u02a9\u02ab")
        buf.write("\5\u008cG\2\u02aa\u02a8\3\2\2\2\u02ab\u02ae\3\2\2\2\u02ac")
        buf.write("\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u008b\3\2\2\2")
        buf.write("\u02ae\u02ac\3\2\2\2\u02af\u02b4\5\u008eH\2\u02b0\u02b1")
        buf.write("\t\4\2\2\u02b1\u02b3\5\u008eH\2\u02b2\u02b0\3\2\2\2\u02b3")
        buf.write("\u02b6\3\2\2\2\u02b4\u02b2\3\2\2\2\u02b4\u02b5\3\2\2\2")
        buf.write("\u02b5\u008d\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b7\u02bc\5")
        buf.write("\u0090I\2\u02b8\u02b9\t\5\2\2\u02b9\u02bb\5\u0090I\2\u02ba")
        buf.write("\u02b8\3\2\2\2\u02bb\u02be\3\2\2\2\u02bc\u02ba\3\2\2\2")
        buf.write("\u02bc\u02bd\3\2\2\2\u02bd\u008f\3\2\2\2\u02be\u02bc\3")
        buf.write("\2\2\2\u02bf\u02c0\t\6\2\2\u02c0\u02c1\5\u0090I\2\u02c1")
        buf.write("\u0091\3\2\2\2\u02c2\u02ce\5\u0094K\2\u02c3\u02ce\7`\2")
        buf.write("\2\u02c4\u02c6\7_\2\2\u02c5\u02c4\3\2\2\2\u02c6\u02c7")
        buf.write("\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8")
        buf.write("\u02ce\3\2\2\2\u02c9\u02ce\7\62\2\2\u02ca\u02ce\7(\2\2")
        buf.write("\u02cb\u02ce\7-\2\2\u02cc\u02ce\7#\2\2\u02cd\u02c2\3\2")
        buf.write("\2\2\u02cd\u02c3\3\2\2\2\u02cd\u02c5\3\2\2\2\u02cd\u02c9")
        buf.write("\3\2\2\2\u02cd\u02ca\3\2\2\2\u02cd\u02cb\3\2\2\2\u02cd")
        buf.write("\u02cc\3\2\2\2\u02ce\u0093\3\2\2\2\u02cf\u02d0\t\7\2\2")
        buf.write("\u02d0\u0095\3\2\2\2\u02d1\u02d6\5\u0098M\2\u02d2\u02d3")
        buf.write("\7\63\2\2\u02d3\u02d5\5\u0098M\2\u02d4\u02d2\3\2\2\2\u02d5")
        buf.write("\u02d8\3\2\2\2\u02d6\u02d4\3\2\2\2\u02d6\u02d7\3\2\2\2")
        buf.write("\u02d7\u02da\3\2\2\2\u02d8\u02d6\3\2\2\2\u02d9\u02db\7")
        buf.write("\63\2\2\u02da\u02d9\3\2\2\2\u02da\u02db\3\2\2\2\u02db")
        buf.write("\u0097\3\2\2\2\u02dc\u02e8\5t;\2\u02dd\u02df\5t;\2\u02de")
        buf.write("\u02dd\3\2\2\2\u02de\u02df\3\2\2\2\u02df\u02e0\3\2\2\2")
        buf.write("\u02e0\u02e2\7\64\2\2\u02e1\u02e3\5t;\2\u02e2\u02e1\3")
        buf.write("\2\2\2\u02e2\u02e3\3\2\2\2\u02e3\u02e5\3\2\2\2\u02e4\u02e6")
        buf.write("\5\u009aN\2\u02e5\u02e4\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6")
        buf.write("\u02e8\3\2\2\2\u02e7\u02dc\3\2\2\2\u02e7\u02de\3\2\2\2")
        buf.write("\u02e8\u0099\3\2\2\2\u02e9\u02eb\7\64\2\2\u02ea\u02ec")
        buf.write("\5t;\2\u02eb\u02ea\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec\u009b")
        buf.write("\3\2\2\2\u02ed\u02f0\5\u0084C\2\u02ee\u02f0\5\u0082B\2")
        buf.write("\u02ef\u02ed\3\2\2\2\u02ef\u02ee\3\2\2\2\u02f0\u02f8\3")
        buf.write("\2\2\2\u02f1\u02f4\7\63\2\2\u02f2\u02f5\5\u0084C\2\u02f3")
        buf.write("\u02f5\5\u0082B\2\u02f4\u02f2\3\2\2\2\u02f4\u02f3\3\2")
        buf.write("\2\2\u02f5\u02f7\3\2\2\2\u02f6\u02f1\3\2\2\2\u02f7\u02fa")
        buf.write("\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9")
        buf.write("\u02fc\3\2\2\2\u02fa\u02f8\3\2\2\2\u02fb\u02fd\7\63\2")
        buf.write("\2\u02fc\u02fb\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd\u009d")
        buf.write("\3\2\2\2\u02fe\u0303\5t;\2\u02ff\u0300\7\63\2\2\u0300")
        buf.write("\u0302\5t;\2\u0301\u02ff\3\2\2\2\u0302\u0305\3\2\2\2\u0303")
        buf.write("\u0301\3\2\2\2\u0303\u0304\3\2\2\2\u0304\u0307\3\2\2\2")
        buf.write("\u0305\u0303\3\2\2\2\u0306\u0308\7\63\2\2\u0307\u0306")
        buf.write("\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u009f\3\2\2\2\u0309")
        buf.write("\u030a\5\u0094K\2\u030a\u00a1\3\2\2\2\u030b\u030d\7_\2")
        buf.write("\2\u030c\u030b\3\2\2\2\u030d\u030e\3\2\2\2\u030e\u030c")
        buf.write("\3\2\2\2\u030e\u030f\3\2\2\2\u030f\u00a3\3\2\2\2]\u00a7")
        buf.write("\u00ae\u00b5\u00b9\u00bf\u00ca\u00cd\u00d3\u00d7\u00dc")
        buf.write("\u00e0\u00e4\u00ec\u00f1\u00f6\u00fd\u0101\u0108\u0110")
        buf.write("\u0116\u0123\u0129\u0134\u013c\u0145\u014d\u0151\u0156")
        buf.write("\u0159\u015f\u0162\u0167\u016e\u0172\u017d\u0188\u0192")
        buf.write("\u019c\u01a6\u01ab\u01b0\u01c5\u01c9\u01d1\u01d6\u01d9")
        buf.write("\u01de\u01e5\u01e9\u01ed\u01f3\u01fa\u0203\u020a\u020e")
        buf.write("\u0215\u021a\u022a\u0232\u023c\u0240\u0247\u024f\u025c")
        buf.write("\u0265\u026d\u0273\u027b\u028a\u0294\u029c\u02a4\u02ac")
        buf.write("\u02b4\u02bc\u02c7\u02cd\u02d6\u02da\u02de\u02e2\u02e5")
        buf.write("\u02e7\u02eb\u02ef\u02f4\u02f8\u02fc\u0303\u0307\u030e")
        return buf.getvalue()


class YarcParser ( YarcParserBase ):

    grammarFileName = "YarcParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'scenario'", 
                     "<INVALID>", "'writer'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'create'", "'instantiate'", "'get'", "'x'", "'y'", 
                     "'z'", "<INVALID>", "'set'", "'translate'", "'rotate'", 
                     "'scale'", "'semantics'", "<INVALID>", "'every'", "<INVALID>", 
                     "<INVALID>", "'and'", "'as'", "'def'", "'elif'", "'else'", 
                     "'False'", "'for'", "'if'", "'in'", "'is'", "'None'", 
                     "'not'", "'or'", "'pass'", "'return'", "'True'", "'_'", 
                     "'with'", "'.'", "'..'", "'...'", "','", "':'", "';'", 
                     "'='", "'|'", "'^'", "'&'", "'~'", "'<<'", "'>>'", 
                     "'+'", "'-'", "'/'", "'*'", "'%'", "'//'", "'**'", 
                     "'@'", "'->'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'<'", "'>'", "'=='", "'>='", "'<='", "'!='", "'+='", 
                     "'-='", "'*='", "'@='", "'/='", "'%='", "'&='", "'|='", 
                     "'^='", "'<<='", "'>>='", "'**='", "'//='" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "SCENARIO", "SETTINGS", 
                      "WRITER", "SNIPPET", "UNIFORM", "NORMAL", "CHOICE", 
                      "SEQUENCE", "LOG_UNIFORM", "CREATE", "INSTANTIATE", 
                      "GET", "X", "Y", "Z", "EDIT", "SET", "TRANSLATE", 
                      "ROTATE", "SCALE", "SEMANTICS", "SCATTER", "EVERY", 
                      "FRAMES", "TIME", "AND", "AS", "DEF", "ELIF", "ELSE", 
                      "FALSE", "FOR", "IF", "IN", "IS", "NONE", "NOT", "OR", 
                      "PASS", "RETURN", "TRUE", "UNDERSCORE", "WITH", "DOT", 
                      "RANGE", "ELLIPSIS", "COMMA", "COLON", "SEMI_COLON", 
                      "ASSIGN", "BIT_OR", "XOR", "BIT_AND", "BIT_NOT", "LEFT_SHIFT", 
                      "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "STAR", "MOD", 
                      "IDIV", "POWER", "AT", "ARROW", "LPAREN", "RPAREN", 
                      "LBRACK", "RBRACK", "LBRACE", "RBRACE", "LESS_THAN", 
                      "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
                      "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", 
                      "XOR_ASSIGN", "LSHIFT_ASSIGN", "RSHIFT_ASSIGN", "POWER_ASSIGN", 
                      "IDIV_ASSIGN", "STRING", "NUMBER", "NAME", "STRING_LITERAL", 
                      "INTEGER", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
                      "BIN_INTEGER", "FLOAT_NUMBER", "NEWLINE", "SKIP_", 
                      "UNKNOWN" ]

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
    RULE_with_stmt = 18
    RULE_with_item = 19
    RULE_block = 20
    RULE_subject_expr = 21
    RULE_star_named_expressions = 22
    RULE_star_named_expression = 23
    RULE_guard = 24
    RULE_patterns = 25
    RULE_pattern = 26
    RULE_as_pattern = 27
    RULE_or_pattern = 28
    RULE_closed_pattern = 29
    RULE_literal_pattern = 30
    RULE_literal_expr = 31
    RULE_complex_number = 32
    RULE_signed_number = 33
    RULE_signed_real_number = 34
    RULE_real_number = 35
    RULE_imaginary_number = 36
    RULE_capture_pattern = 37
    RULE_pattern_capture_target = 38
    RULE_wildcard_pattern = 39
    RULE_value_pattern = 40
    RULE_attr = 41
    RULE_name_or_attr = 42
    RULE_group_pattern = 43
    RULE_sequence_pattern = 44
    RULE_open_sequence_pattern = 45
    RULE_maybe_sequence_pattern = 46
    RULE_maybe_star_pattern = 47
    RULE_star_pattern = 48
    RULE_mapping_pattern = 49
    RULE_items_pattern = 50
    RULE_key_value_pattern = 51
    RULE_double_star_pattern = 52
    RULE_class_pattern = 53
    RULE_positional_patterns = 54
    RULE_keyword_patterns = 55
    RULE_keyword_pattern = 56
    RULE_test = 57
    RULE_test_nocond = 58
    RULE_or_test = 59
    RULE_and_test = 60
    RULE_not_test = 61
    RULE_comparison = 62
    RULE_comp_op = 63
    RULE_star_expr = 64
    RULE_expr = 65
    RULE_xor_expr = 66
    RULE_and_expr = 67
    RULE_shift_expr = 68
    RULE_arith_expr = 69
    RULE_term = 70
    RULE_factor = 71
    RULE_atom = 72
    RULE_name = 73
    RULE_subscriptlist = 74
    RULE_subscript_ = 75
    RULE_sliceop = 76
    RULE_exprlist = 77
    RULE_testlist = 78
    RULE_encoding_decl = 79
    RULE_strings = 80

    ruleNames =  [ "file_input", "stmt", "simple_stmts", "simple_stmt", 
                   "expr_stmt", "annassign", "testlist_star_expr", "augassign", 
                   "pass_stmt", "return_stmt", "import_as_name", "dotted_as_name", 
                   "import_as_names", "dotted_as_names", "dotted_name", 
                   "compound_stmt", "if_stmt", "for_stmt", "with_stmt", 
                   "with_item", "block", "subject_expr", "star_named_expressions", 
                   "star_named_expression", "guard", "patterns", "pattern", 
                   "as_pattern", "or_pattern", "closed_pattern", "literal_pattern", 
                   "literal_expr", "complex_number", "signed_number", "signed_real_number", 
                   "real_number", "imaginary_number", "capture_pattern", 
                   "pattern_capture_target", "wildcard_pattern", "value_pattern", 
                   "attr", "name_or_attr", "group_pattern", "sequence_pattern", 
                   "open_sequence_pattern", "maybe_sequence_pattern", "maybe_star_pattern", 
                   "star_pattern", "mapping_pattern", "items_pattern", "key_value_pattern", 
                   "double_star_pattern", "class_pattern", "positional_patterns", 
                   "keyword_patterns", "keyword_pattern", "test", "test_nocond", 
                   "or_test", "and_test", "not_test", "comparison", "comp_op", 
                   "star_expr", "expr", "xor_expr", "and_expr", "shift_expr", 
                   "arith_expr", "term", "factor", "atom", "name", "subscriptlist", 
                   "subscript_", "sliceop", "exprlist", "testlist", "encoding_decl", 
                   "strings" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    SCENARIO=3
    SETTINGS=4
    WRITER=5
    SNIPPET=6
    UNIFORM=7
    NORMAL=8
    CHOICE=9
    SEQUENCE=10
    LOG_UNIFORM=11
    CREATE=12
    INSTANTIATE=13
    GET=14
    X=15
    Y=16
    Z=17
    EDIT=18
    SET=19
    TRANSLATE=20
    ROTATE=21
    SCALE=22
    SEMANTICS=23
    SCATTER=24
    EVERY=25
    FRAMES=26
    TIME=27
    AND=28
    AS=29
    DEF=30
    ELIF=31
    ELSE=32
    FALSE=33
    FOR=34
    IF=35
    IN=36
    IS=37
    NONE=38
    NOT=39
    OR=40
    PASS=41
    RETURN=42
    TRUE=43
    UNDERSCORE=44
    WITH=45
    DOT=46
    RANGE=47
    ELLIPSIS=48
    COMMA=49
    COLON=50
    SEMI_COLON=51
    ASSIGN=52
    BIT_OR=53
    XOR=54
    BIT_AND=55
    BIT_NOT=56
    LEFT_SHIFT=57
    RIGHT_SHIFT=58
    ADD=59
    MINUS=60
    DIV=61
    STAR=62
    MOD=63
    IDIV=64
    POWER=65
    AT=66
    ARROW=67
    LPAREN=68
    RPAREN=69
    LBRACK=70
    RBRACK=71
    LBRACE=72
    RBRACE=73
    LESS_THAN=74
    GREATER_THAN=75
    EQUALS=76
    GT_EQ=77
    LT_EQ=78
    NOT_EQ=79
    ADD_ASSIGN=80
    SUB_ASSIGN=81
    MULT_ASSIGN=82
    AT_ASSIGN=83
    DIV_ASSIGN=84
    MOD_ASSIGN=85
    AND_ASSIGN=86
    OR_ASSIGN=87
    XOR_ASSIGN=88
    LSHIFT_ASSIGN=89
    RSHIFT_ASSIGN=90
    POWER_ASSIGN=91
    IDIV_ASSIGN=92
    STRING=93
    NUMBER=94
    NAME=95
    STRING_LITERAL=96
    INTEGER=97
    DECIMAL_INTEGER=98
    OCT_INTEGER=99
    HEX_INTEGER=100
    BIN_INTEGER=101
    FLOAT_NUMBER=102
    NEWLINE=103
    SKIP_=104
    UNKNOWN=105

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(YarcParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.NEWLINE)
            else:
                return self.getToken(YarcParser.NEWLINE, i)

        def getRuleIndex(self):
            return YarcParser.RULE_file_input




    def file_input(self):

        localctx = YarcParser.File_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.NEWLINE:
                self.state = 162
                self.match(YarcParser.NEWLINE)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
            self.match(YarcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmts(self):
            return self.getTypedRuleContext(YarcParser.Simple_stmtsContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(YarcParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_stmt




    def stmt(self):

        localctx = YarcParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT, YarcParser.PASS, YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS, YarcParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.simple_stmts()
                pass
            elif token in [YarcParser.FOR, YarcParser.IF, YarcParser.WITH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Simple_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Simple_stmtContext,i)


        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.SEMI_COLON)
            else:
                return self.getToken(YarcParser.SEMI_COLON, i)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_stmts




    def simple_stmts(self):

        localctx = YarcParser.Simple_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.simple_stmt()
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    self.match(YarcParser.SEMI_COLON)
                    self.state = 176
                    self.simple_stmt() 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.SEMI_COLON:
                self.state = 182
                self.match(YarcParser.SEMI_COLON)


            self.state = 185
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_stmt(self):
            return self.getTypedRuleContext(YarcParser.Expr_stmtContext,0)


        def pass_stmt(self):
            return self.getTypedRuleContext(YarcParser.Pass_stmtContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_simple_stmt




    def simple_stmt(self):

        localctx = YarcParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT, YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS, YarcParser.STAR]:
                self.state = 187
                self.expr_stmt()
                pass
            elif token in [YarcParser.PASS]:
                self.state = 188
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testlist_star_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Testlist_star_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Testlist_star_exprContext,i)


        def annassign(self):
            return self.getTypedRuleContext(YarcParser.AnnassignContext,0)


        def augassign(self):
            return self.getTypedRuleContext(YarcParser.AugassignContext,0)


        def testlist(self):
            return self.getTypedRuleContext(YarcParser.TestlistContext,0)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.ASSIGN)
            else:
                return self.getToken(YarcParser.ASSIGN, i)

        def getRuleIndex(self):
            return YarcParser.RULE_expr_stmt




    def expr_stmt(self):

        localctx = YarcParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.testlist_star_expr()
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 192
                self.annassign()
                pass
            elif token in [YarcParser.ADD_ASSIGN, YarcParser.SUB_ASSIGN, YarcParser.MULT_ASSIGN, YarcParser.AT_ASSIGN, YarcParser.DIV_ASSIGN, YarcParser.MOD_ASSIGN, YarcParser.AND_ASSIGN, YarcParser.OR_ASSIGN, YarcParser.XOR_ASSIGN, YarcParser.LSHIFT_ASSIGN, YarcParser.RSHIFT_ASSIGN, YarcParser.POWER_ASSIGN, YarcParser.IDIV_ASSIGN]:
                self.state = 193
                self.augassign()

                self.state = 194
                self.testlist()
                pass
            elif token in [YarcParser.SEMI_COLON, YarcParser.ASSIGN, YarcParser.NEWLINE]:
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==YarcParser.ASSIGN:
                    self.state = 196
                    self.match(YarcParser.ASSIGN)

                    self.state = 197
                    self.testlist_star_expr()
                    self.state = 202
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext,i)


        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_annassign




    def annassign(self):

        localctx = YarcParser.AnnassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_annassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(YarcParser.COLON)
            self.state = 206
            self.test()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.ASSIGN:
                self.state = 207
                self.match(YarcParser.ASSIGN)
                self.state = 208
                self.test()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Testlist_star_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext,i)


        def star_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Star_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Star_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_testlist_star_expr




    def testlist_star_expr(self):

        localctx = YarcParser.Testlist_star_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_testlist_star_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT, YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                self.state = 211
                self.test()
                pass
            elif token in [YarcParser.STAR]:
                self.state = 212
                self.star_expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 215
                    self.match(YarcParser.COMMA)
                    self.state = 218
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [YarcParser.NOT, YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                        self.state = 216
                        self.test()
                        pass
                    elif token in [YarcParser.STAR]:
                        self.state = 217
                        self.star_expr()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.COMMA:
                self.state = 225
                self.match(YarcParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AugassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not(((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (YarcParser.ADD_ASSIGN - 80)) | (1 << (YarcParser.SUB_ASSIGN - 80)) | (1 << (YarcParser.MULT_ASSIGN - 80)) | (1 << (YarcParser.AT_ASSIGN - 80)) | (1 << (YarcParser.DIV_ASSIGN - 80)) | (1 << (YarcParser.MOD_ASSIGN - 80)) | (1 << (YarcParser.AND_ASSIGN - 80)) | (1 << (YarcParser.OR_ASSIGN - 80)) | (1 << (YarcParser.XOR_ASSIGN - 80)) | (1 << (YarcParser.LSHIFT_ASSIGN - 80)) | (1 << (YarcParser.RSHIFT_ASSIGN - 80)) | (1 << (YarcParser.POWER_ASSIGN - 80)) | (1 << (YarcParser.IDIV_ASSIGN - 80)))) != 0)):
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASS(self):
            return self.getToken(YarcParser.PASS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_pass_stmt




    def pass_stmt(self):

        localctx = YarcParser.Pass_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pass_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(YarcParser.PASS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(YarcParser.RETURN, 0)

        def testlist(self):
            return self.getTypedRuleContext(YarcParser.TestlistContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_return_stmt




    def return_stmt(self):

        localctx = YarcParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(YarcParser.RETURN)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YarcParser.NOT) | (1 << YarcParser.BIT_NOT) | (1 << YarcParser.ADD) | (1 << YarcParser.MINUS))) != 0):
                self.state = 233
                self.testlist()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_as_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext,i)


        def AS(self):
            return self.getToken(YarcParser.AS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_import_as_name




    def import_as_name(self):

        localctx = YarcParser.Import_as_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_import_as_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.name()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.AS:
                self.state = 237
                self.match(YarcParser.AS)
                self.state = 238
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dotted_as_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dotted_name(self):
            return self.getTypedRuleContext(YarcParser.Dotted_nameContext,0)


        def AS(self):
            return self.getToken(YarcParser.AS, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_dotted_as_name




    def dotted_as_name(self):

        localctx = YarcParser.Dotted_as_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dotted_as_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.dotted_name()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.AS:
                self.state = 242
                self.match(YarcParser.AS)
                self.state = 243
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_as_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_as_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Import_as_nameContext)
            else:
                return self.getTypedRuleContext(YarcParser.Import_as_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_import_as_names




    def import_as_names(self):

        localctx = YarcParser.Import_as_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_import_as_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.import_as_name()
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 247
                    self.match(YarcParser.COMMA)
                    self.state = 248
                    self.import_as_name() 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.COMMA:
                self.state = 254
                self.match(YarcParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dotted_as_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dotted_as_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Dotted_as_nameContext)
            else:
                return self.getTypedRuleContext(YarcParser.Dotted_as_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_dotted_as_names




    def dotted_as_names(self):

        localctx = YarcParser.Dotted_as_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dotted_as_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.dotted_as_name()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.COMMA:
                self.state = 258
                self.match(YarcParser.COMMA)
                self.state = 259
                self.dotted_as_name()
                self.state = 264
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.DOT)
            else:
                return self.getToken(YarcParser.DOT, i)

        def getRuleIndex(self):
            return YarcParser.RULE_dotted_name




    def dotted_name(self):

        localctx = YarcParser.Dotted_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dotted_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.name()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.DOT:
                self.state = 266
                self.match(YarcParser.DOT)
                self.state = 267
                self.name()
                self.state = 272
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(YarcParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(YarcParser.For_stmtContext,0)


        def with_stmt(self):
            return self.getTypedRuleContext(YarcParser.With_stmtContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_compound_stmt




    def compound_stmt(self):

        localctx = YarcParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compound_stmt)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.if_stmt()
                pass
            elif token in [YarcParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.for_stmt()
                pass
            elif token in [YarcParser.WITH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.with_stmt()
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(YarcParser.IF, 0)

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COLON)
            else:
                return self.getToken(YarcParser.COLON, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.BlockContext)
            else:
                return self.getTypedRuleContext(YarcParser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.ELIF)
            else:
                return self.getToken(YarcParser.ELIF, i)

        def ELSE(self):
            return self.getToken(YarcParser.ELSE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_if_stmt




    def if_stmt(self):

        localctx = YarcParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(YarcParser.IF)
            self.state = 279
            self.test()
            self.state = 280
            self.match(YarcParser.COLON)
            self.state = 281
            self.block()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.ELIF:
                self.state = 282
                self.match(YarcParser.ELIF)
                self.state = 283
                self.test()
                self.state = 284
                self.match(YarcParser.COLON)
                self.state = 285
                self.block()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.ELSE:
                self.state = 292
                self.match(YarcParser.ELSE)
                self.state = 293
                self.match(YarcParser.COLON)
                self.state = 294
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(YarcParser.FOR, 0)

        def exprlist(self):
            return self.getTypedRuleContext(YarcParser.ExprlistContext,0)


        def IN(self):
            return self.getToken(YarcParser.IN, 0)

        def testlist(self):
            return self.getTypedRuleContext(YarcParser.TestlistContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COLON)
            else:
                return self.getToken(YarcParser.COLON, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.BlockContext)
            else:
                return self.getTypedRuleContext(YarcParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(YarcParser.ELSE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_for_stmt




    def for_stmt(self):

        localctx = YarcParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(YarcParser.FOR)
            self.state = 298
            self.exprlist()
            self.state = 299
            self.match(YarcParser.IN)
            self.state = 300
            self.testlist()
            self.state = 301
            self.match(YarcParser.COLON)
            self.state = 302
            self.block()
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.ELSE:
                self.state = 303
                self.match(YarcParser.ELSE)
                self.state = 304
                self.match(YarcParser.COLON)
                self.state = 305
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class With_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(YarcParser.WITH, 0)

        def with_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.With_itemContext)
            else:
                return self.getTypedRuleContext(YarcParser.With_itemContext,i)


        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(YarcParser.BlockContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_with_stmt




    def with_stmt(self):

        localctx = YarcParser.With_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_with_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(YarcParser.WITH)
            self.state = 309
            self.with_item()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.COMMA:
                self.state = 310
                self.match(YarcParser.COMMA)
                self.state = 311
                self.with_item()
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 317
            self.match(YarcParser.COLON)
            self.state = 318
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class With_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext,0)


        def AS(self):
            return self.getToken(YarcParser.AS, 0)

        def expr(self):
            return self.getTypedRuleContext(YarcParser.ExprContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_with_item




    def with_item(self):

        localctx = YarcParser.With_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_with_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.test()
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.AS:
                self.state = 321
                self.match(YarcParser.AS)
                self.state = 322
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmts(self):
            return self.getTypedRuleContext(YarcParser.Simple_stmtsContext,0)


        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.StmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.StmtContext,i)


        def getRuleIndex(self):
            return YarcParser.RULE_block




    def block(self):

        localctx = YarcParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT, YarcParser.PASS, YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS, YarcParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.simple_stmts()
                pass
            elif token in [YarcParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(YarcParser.NEWLINE)
                self.state = 327
                self.match(YarcParser.INDENT)
                self.state = 329 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 328
                    self.stmt()
                    self.state = 331 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YarcParser.FOR) | (1 << YarcParser.IF) | (1 << YarcParser.NOT) | (1 << YarcParser.PASS) | (1 << YarcParser.WITH) | (1 << YarcParser.BIT_NOT) | (1 << YarcParser.ADD) | (1 << YarcParser.MINUS) | (1 << YarcParser.STAR))) != 0)):
                        break

                self.state = 333
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_named_expression(self):
            return self.getTypedRuleContext(YarcParser.Star_named_expressionContext,0)


        def COMMA(self):
            return self.getToken(YarcParser.COMMA, 0)

        def star_named_expressions(self):
            return self.getTypedRuleContext(YarcParser.Star_named_expressionsContext,0)


        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_subject_expr




    def subject_expr(self):

        localctx = YarcParser.Subject_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_subject_expr)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.star_named_expression()
                self.state = 338
                self.match(YarcParser.COMMA)
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COMMA:
                    self.state = 339
                    self.star_named_expressions()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def star_named_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Star_named_expressionContext)
            else:
                return self.getTypedRuleContext(YarcParser.Star_named_expressionContext,i)


        def getRuleIndex(self):
            return YarcParser.RULE_star_named_expressions




    def star_named_expressions(self):

        localctx = YarcParser.Star_named_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_star_named_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(YarcParser.COMMA)
            self.state = 347 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 346
                self.star_named_expression()
                self.state = 349 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YarcParser.NOT) | (1 << YarcParser.BIT_NOT) | (1 << YarcParser.ADD) | (1 << YarcParser.MINUS) | (1 << YarcParser.STAR))) != 0)):
                    break

            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.COMMA:
                self.state = 351
                self.match(YarcParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Star_named_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(YarcParser.STAR, 0)

        def expr(self):
            return self.getTypedRuleContext(YarcParser.ExprContext,0)


        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_star_named_expression




    def star_named_expression(self):

        localctx = YarcParser.Star_named_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_star_named_expression)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(YarcParser.STAR)
                self.state = 355
                self.expr()
                pass
            elif token in [YarcParser.NOT, YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(YarcParser.IF, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_guard




    def guard(self):

        localctx = YarcParser.GuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_guard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(YarcParser.IF)
            self.state = 360
            self.test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Open_sequence_patternContext,0)


        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_patterns




    def patterns(self):

        localctx = YarcParser.PatternsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_patterns)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.open_sequence_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def as_pattern(self):
            return self.getTypedRuleContext(YarcParser.As_patternContext,0)


        def or_pattern(self):
            return self.getTypedRuleContext(YarcParser.Or_patternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_pattern




    def pattern(self):

        localctx = YarcParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_pattern)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.as_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.or_pattern()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_pattern(self):
            return self.getTypedRuleContext(YarcParser.Or_patternContext,0)


        def AS(self):
            return self.getToken(YarcParser.AS, 0)

        def pattern_capture_target(self):
            return self.getTypedRuleContext(YarcParser.Pattern_capture_targetContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_as_pattern




    def as_pattern(self):

        localctx = YarcParser.As_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_as_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.or_pattern()
            self.state = 371
            self.match(YarcParser.AS)
            self.state = 372
            self.pattern_capture_target()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closed_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Closed_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Closed_patternContext,i)


        def BIT_OR(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.BIT_OR)
            else:
                return self.getToken(YarcParser.BIT_OR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_or_pattern




    def or_pattern(self):

        localctx = YarcParser.Or_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_or_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.closed_pattern()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.BIT_OR:
                self.state = 375
                self.match(YarcParser.BIT_OR)
                self.state = 376
                self.closed_pattern()
                self.state = 381
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_pattern(self):
            return self.getTypedRuleContext(YarcParser.Literal_patternContext,0)


        def capture_pattern(self):
            return self.getTypedRuleContext(YarcParser.Capture_patternContext,0)


        def wildcard_pattern(self):
            return self.getTypedRuleContext(YarcParser.Wildcard_patternContext,0)


        def value_pattern(self):
            return self.getTypedRuleContext(YarcParser.Value_patternContext,0)


        def group_pattern(self):
            return self.getTypedRuleContext(YarcParser.Group_patternContext,0)


        def sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Sequence_patternContext,0)


        def mapping_pattern(self):
            return self.getTypedRuleContext(YarcParser.Mapping_patternContext,0)


        def class_pattern(self):
            return self.getTypedRuleContext(YarcParser.Class_patternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_closed_pattern




    def closed_pattern(self):

        localctx = YarcParser.Closed_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_closed_pattern)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.literal_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.capture_pattern()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.wildcard_pattern()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.value_pattern()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 386
                self.group_pattern()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 387
                self.sequence_pattern()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 388
                self.mapping_pattern()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 389
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_number(self):
            return self.getTypedRuleContext(YarcParser.Signed_numberContext,0)


        def complex_number(self):
            return self.getTypedRuleContext(YarcParser.Complex_numberContext,0)


        def strings(self):
            return self.getTypedRuleContext(YarcParser.StringsContext,0)


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
        self.enterRule(localctx, 60, self.RULE_literal_pattern)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.signed_number()
                self.state = 393
                if not  self.CannotBePlusMinus() :
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, " $parser.CannotBePlusMinus() ")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.complex_number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.strings()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.match(YarcParser.NONE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 398
                self.match(YarcParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 399
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_number(self):
            return self.getTypedRuleContext(YarcParser.Signed_numberContext,0)


        def complex_number(self):
            return self.getTypedRuleContext(YarcParser.Complex_numberContext,0)


        def strings(self):
            return self.getTypedRuleContext(YarcParser.StringsContext,0)


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
        self.enterRule(localctx, 62, self.RULE_literal_expr)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.signed_number()
                self.state = 403
                if not  self.CannotBePlusMinus() :
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, " $parser.CannotBePlusMinus() ")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.complex_number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.strings()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.match(YarcParser.NONE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 408
                self.match(YarcParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 409
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_real_number(self):
            return self.getTypedRuleContext(YarcParser.Signed_real_numberContext,0)


        def ADD(self):
            return self.getToken(YarcParser.ADD, 0)

        def imaginary_number(self):
            return self.getTypedRuleContext(YarcParser.Imaginary_numberContext,0)


        def MINUS(self):
            return self.getToken(YarcParser.MINUS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_complex_number




    def complex_number(self):

        localctx = YarcParser.Complex_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_complex_number)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.signed_real_number()
                self.state = 413
                self.match(YarcParser.ADD)
                self.state = 414
                self.imaginary_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.signed_real_number()
                self.state = 417
                self.match(YarcParser.MINUS)
                self.state = 418
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
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
        self.enterRule(localctx, 66, self.RULE_signed_number)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(YarcParser.NUMBER)
                pass
            elif token in [YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(YarcParser.MINUS)
                self.state = 424
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def real_number(self):
            return self.getTypedRuleContext(YarcParser.Real_numberContext,0)


        def MINUS(self):
            return self.getToken(YarcParser.MINUS, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_signed_real_number




    def signed_real_number(self):

        localctx = YarcParser.Signed_real_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_signed_real_number)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.real_number()
                pass
            elif token in [YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(YarcParser.MINUS)
                self.state = 429
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YarcParser.NUMBER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_real_number




    def real_number(self):

        localctx = YarcParser.Real_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_real_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(YarcParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Imaginary_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YarcParser.NUMBER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_imaginary_number




    def imaginary_number(self):

        localctx = YarcParser.Imaginary_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_imaginary_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(YarcParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Capture_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern_capture_target(self):
            return self.getTypedRuleContext(YarcParser.Pattern_capture_targetContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_capture_pattern




    def capture_pattern(self):

        localctx = YarcParser.Capture_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_capture_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.pattern_capture_target()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pattern_capture_targetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_pattern_capture_target




    def pattern_capture_target(self):

        localctx = YarcParser.Pattern_capture_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_pattern_capture_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.name()
            self.state = 439
            if not  self.CannotBeDotLpEq() :
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(YarcParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_wildcard_pattern




    def wildcard_pattern(self):

        localctx = YarcParser.Wildcard_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_wildcard_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(YarcParser.UNDERSCORE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(YarcParser.AttrContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_value_pattern




    def value_pattern(self):

        localctx = YarcParser.Value_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_value_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.attr()
            self.state = 444
            if not  self.CannotBeDotLpEq() :
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.DOT)
            else:
                return self.getToken(YarcParser.DOT, i)

        def getRuleIndex(self):
            return YarcParser.RULE_attr




    def attr(self):

        localctx = YarcParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.name()
            self.state = 449 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 447
                    self.match(YarcParser.DOT)
                    self.state = 448
                    self.name()

                else:
                    raise NoViableAltException(self)
                self.state = 451 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_or_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(YarcParser.AttrContext,0)


        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_name_or_attr




    def name_or_attr(self):

        localctx = YarcParser.Name_or_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_name_or_attr)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext,0)


        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_group_pattern




    def group_pattern(self):

        localctx = YarcParser.Group_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_group_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(YarcParser.LPAREN)
            self.state = 458
            self.pattern()
            self.state = 459
            self.match(YarcParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sequence_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def maybe_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Maybe_sequence_patternContext,0)


        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def open_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Open_sequence_patternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_sequence_pattern




    def sequence_pattern(self):

        localctx = YarcParser.Sequence_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_sequence_pattern)
        self._la = 0 # Token type
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.match(YarcParser.LBRACK)
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & ((1 << (YarcParser.FALSE - 33)) | (1 << (YarcParser.NONE - 33)) | (1 << (YarcParser.TRUE - 33)) | (1 << (YarcParser.UNDERSCORE - 33)) | (1 << (YarcParser.MINUS - 33)) | (1 << (YarcParser.STAR - 33)) | (1 << (YarcParser.LPAREN - 33)) | (1 << (YarcParser.LBRACK - 33)) | (1 << (YarcParser.LBRACE - 33)) | (1 << (YarcParser.STRING - 33)) | (1 << (YarcParser.NUMBER - 33)) | (1 << (YarcParser.NAME - 33)))) != 0):
                    self.state = 462
                    self.maybe_sequence_pattern()


                self.state = 465
                self.match(YarcParser.RBRACK)
                pass
            elif token in [YarcParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.match(YarcParser.LPAREN)
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & ((1 << (YarcParser.FALSE - 33)) | (1 << (YarcParser.NONE - 33)) | (1 << (YarcParser.TRUE - 33)) | (1 << (YarcParser.UNDERSCORE - 33)) | (1 << (YarcParser.MINUS - 33)) | (1 << (YarcParser.STAR - 33)) | (1 << (YarcParser.LPAREN - 33)) | (1 << (YarcParser.LBRACK - 33)) | (1 << (YarcParser.LBRACE - 33)) | (1 << (YarcParser.STRING - 33)) | (1 << (YarcParser.NUMBER - 33)) | (1 << (YarcParser.NAME - 33)))) != 0):
                    self.state = 467
                    self.open_sequence_pattern()


                self.state = 470
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def maybe_star_pattern(self):
            return self.getTypedRuleContext(YarcParser.Maybe_star_patternContext,0)


        def COMMA(self):
            return self.getToken(YarcParser.COMMA, 0)

        def maybe_sequence_pattern(self):
            return self.getTypedRuleContext(YarcParser.Maybe_sequence_patternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_open_sequence_pattern




    def open_sequence_pattern(self):

        localctx = YarcParser.Open_sequence_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_open_sequence_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.maybe_star_pattern()
            self.state = 474
            self.match(YarcParser.COMMA)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & ((1 << (YarcParser.FALSE - 33)) | (1 << (YarcParser.NONE - 33)) | (1 << (YarcParser.TRUE - 33)) | (1 << (YarcParser.UNDERSCORE - 33)) | (1 << (YarcParser.MINUS - 33)) | (1 << (YarcParser.STAR - 33)) | (1 << (YarcParser.LPAREN - 33)) | (1 << (YarcParser.LBRACK - 33)) | (1 << (YarcParser.LBRACE - 33)) | (1 << (YarcParser.STRING - 33)) | (1 << (YarcParser.NUMBER - 33)) | (1 << (YarcParser.NAME - 33)))) != 0):
                self.state = 475
                self.maybe_sequence_pattern()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Maybe_sequence_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def maybe_star_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Maybe_star_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Maybe_star_patternContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_maybe_sequence_pattern




    def maybe_sequence_pattern(self):

        localctx = YarcParser.Maybe_sequence_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_maybe_sequence_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.maybe_star_pattern()
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 479
                    self.match(YarcParser.COMMA)
                    self.state = 480
                    self.maybe_star_pattern() 
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.COMMA:
                self.state = 486
                self.match(YarcParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Maybe_star_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_pattern(self):
            return self.getTypedRuleContext(YarcParser.Star_patternContext,0)


        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_maybe_star_pattern




    def maybe_star_pattern(self):

        localctx = YarcParser.Maybe_star_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_maybe_star_pattern)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.star_pattern()
                pass
            elif token in [YarcParser.FALSE, YarcParser.NONE, YarcParser.TRUE, YarcParser.UNDERSCORE, YarcParser.MINUS, YarcParser.LPAREN, YarcParser.LBRACK, YarcParser.LBRACE, YarcParser.STRING, YarcParser.NUMBER, YarcParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(YarcParser.STAR, 0)

        def pattern_capture_target(self):
            return self.getTypedRuleContext(YarcParser.Pattern_capture_targetContext,0)


        def wildcard_pattern(self):
            return self.getTypedRuleContext(YarcParser.Wildcard_patternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_star_pattern




    def star_pattern(self):

        localctx = YarcParser.Star_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_star_pattern)
        try:
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(YarcParser.STAR)
                self.state = 494
                self.pattern_capture_target()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.match(YarcParser.STAR)
                self.state = 496
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(YarcParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YarcParser.RBRACE, 0)

        def double_star_pattern(self):
            return self.getTypedRuleContext(YarcParser.Double_star_patternContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def items_pattern(self):
            return self.getTypedRuleContext(YarcParser.Items_patternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_mapping_pattern




    def mapping_pattern(self):

        localctx = YarcParser.Mapping_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_mapping_pattern)
        self._la = 0 # Token type
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.match(YarcParser.LBRACE)
                self.state = 500
                self.match(YarcParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.match(YarcParser.LBRACE)
                self.state = 502
                self.double_star_pattern()
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COMMA:
                    self.state = 503
                    self.match(YarcParser.COMMA)


                self.state = 506
                self.match(YarcParser.RBRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.match(YarcParser.LBRACE)
                self.state = 509
                self.items_pattern()
                self.state = 510
                self.match(YarcParser.COMMA)
                self.state = 511
                self.double_star_pattern()
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COMMA:
                    self.state = 512
                    self.match(YarcParser.COMMA)


                self.state = 515
                self.match(YarcParser.RBRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 517
                self.match(YarcParser.LBRACE)
                self.state = 518
                self.items_pattern()
                self.state = 520
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COMMA:
                    self.state = 519
                    self.match(YarcParser.COMMA)


                self.state = 522
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key_value_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Key_value_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Key_value_patternContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_items_pattern




    def items_pattern(self):

        localctx = YarcParser.Items_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_items_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.key_value_pattern()
            self.state = 531
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 527
                    self.match(YarcParser.COMMA)
                    self.state = 528
                    self.key_value_pattern() 
                self.state = 533
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_value_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext,0)


        def literal_expr(self):
            return self.getTypedRuleContext(YarcParser.Literal_exprContext,0)


        def attr(self):
            return self.getTypedRuleContext(YarcParser.AttrContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_key_value_pattern




    def key_value_pattern(self):

        localctx = YarcParser.Key_value_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_key_value_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FALSE, YarcParser.NONE, YarcParser.TRUE, YarcParser.MINUS, YarcParser.STRING, YarcParser.NUMBER]:
                self.state = 534
                self.literal_expr()
                pass
            elif token in [YarcParser.UNDERSCORE, YarcParser.NAME]:
                self.state = 535
                self.attr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 538
            self.match(YarcParser.COLON)
            self.state = 539
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Double_star_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POWER(self):
            return self.getToken(YarcParser.POWER, 0)

        def pattern_capture_target(self):
            return self.getTypedRuleContext(YarcParser.Pattern_capture_targetContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_double_star_pattern




    def double_star_pattern(self):

        localctx = YarcParser.Double_star_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_double_star_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(YarcParser.POWER)
            self.state = 542
            self.pattern_capture_target()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self):
            return self.getTypedRuleContext(YarcParser.Name_or_attrContext,0)


        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def positional_patterns(self):
            return self.getTypedRuleContext(YarcParser.Positional_patternsContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def keyword_patterns(self):
            return self.getTypedRuleContext(YarcParser.Keyword_patternsContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_class_pattern




    def class_pattern(self):

        localctx = YarcParser.Class_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_class_pattern)
        self._la = 0 # Token type
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.name_or_attr()
                self.state = 545
                self.match(YarcParser.LPAREN)
                self.state = 546
                self.match(YarcParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.name_or_attr()
                self.state = 549
                self.match(YarcParser.LPAREN)
                self.state = 550
                self.positional_patterns()
                self.state = 552
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COMMA:
                    self.state = 551
                    self.match(YarcParser.COMMA)


                self.state = 554
                self.match(YarcParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.name_or_attr()
                self.state = 557
                self.match(YarcParser.LPAREN)
                self.state = 558
                self.keyword_patterns()
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COMMA:
                    self.state = 559
                    self.match(YarcParser.COMMA)


                self.state = 562
                self.match(YarcParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 564
                self.name_or_attr()
                self.state = 565
                self.match(YarcParser.LPAREN)
                self.state = 566
                self.positional_patterns()
                self.state = 567
                self.match(YarcParser.COMMA)
                self.state = 568
                self.keyword_patterns()
                self.state = 570
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COMMA:
                    self.state = 569
                    self.match(YarcParser.COMMA)


                self.state = 572
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.PatternContext)
            else:
                return self.getTypedRuleContext(YarcParser.PatternContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_positional_patterns




    def positional_patterns(self):

        localctx = YarcParser.Positional_patternsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_positional_patterns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.pattern()
            self.state = 581
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 577
                    self.match(YarcParser.COMMA)
                    self.state = 578
                    self.pattern() 
                self.state = 583
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_patternsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword_pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Keyword_patternContext)
            else:
                return self.getTypedRuleContext(YarcParser.Keyword_patternContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_keyword_patterns




    def keyword_patterns(self):

        localctx = YarcParser.Keyword_patternsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_keyword_patterns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.keyword_pattern()
            self.state = 589
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 585
                    self.match(YarcParser.COMMA)
                    self.state = 586
                    self.keyword_pattern() 
                self.state = 591
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext,0)


        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def pattern(self):
            return self.getTypedRuleContext(YarcParser.PatternContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_keyword_pattern




    def keyword_pattern(self):

        localctx = YarcParser.Keyword_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_keyword_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.name()
            self.state = 593
            self.match(YarcParser.ASSIGN)
            self.state = 594
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Or_testContext)
            else:
                return self.getTypedRuleContext(YarcParser.Or_testContext,i)


        def IF(self):
            return self.getToken(YarcParser.IF, 0)

        def ELSE(self):
            return self.getToken(YarcParser.ELSE, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_test




    def test(self):

        localctx = YarcParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.or_test()
            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.IF:
                self.state = 597
                self.match(YarcParser.IF)
                self.state = 598
                self.or_test()
                self.state = 599
                self.match(YarcParser.ELSE)
                self.state = 600
                self.test()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Test_nocondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self):
            return self.getTypedRuleContext(YarcParser.Or_testContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_test_nocond




    def test_nocond(self):

        localctx = YarcParser.Test_nocondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_test_nocond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.or_test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.And_testContext)
            else:
                return self.getTypedRuleContext(YarcParser.And_testContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.OR)
            else:
                return self.getToken(YarcParser.OR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_or_test




    def or_test(self):

        localctx = YarcParser.Or_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_or_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.and_test()
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.OR:
                self.state = 607
                self.match(YarcParser.OR)
                self.state = 608
                self.and_test()
                self.state = 613
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Not_testContext)
            else:
                return self.getTypedRuleContext(YarcParser.Not_testContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.AND)
            else:
                return self.getToken(YarcParser.AND, i)

        def getRuleIndex(self):
            return YarcParser.RULE_and_test




    def and_test(self):

        localctx = YarcParser.And_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_and_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.not_test()
            self.state = 619
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.AND:
                self.state = 615
                self.match(YarcParser.AND)
                self.state = 616
                self.not_test()
                self.state = 621
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(YarcParser.NOT, 0)

        def not_test(self):
            return self.getTypedRuleContext(YarcParser.Not_testContext,0)


        def comparison(self):
            return self.getTypedRuleContext(YarcParser.ComparisonContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_not_test




    def not_test(self):

        localctx = YarcParser.Not_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_not_test)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 622
                self.match(YarcParser.NOT)
                self.state = 623
                self.not_test()
                pass
            elif token in [YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.ExprContext)
            else:
                return self.getTypedRuleContext(YarcParser.ExprContext,i)


        def comp_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Comp_opContext)
            else:
                return self.getTypedRuleContext(YarcParser.Comp_opContext,i)


        def getRuleIndex(self):
            return YarcParser.RULE_comparison




    def comparison(self):

        localctx = YarcParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.expr()
            self.state = 633
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 628
                    self.comp_op()
                    self.state = 629
                    self.expr() 
                self.state = 635
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
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
        self.enterRule(localctx, 126, self.RULE_comp_op)
        try:
            self.state = 648
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.match(YarcParser.LESS_THAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 637
                self.match(YarcParser.GREATER_THAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 638
                self.match(YarcParser.EQUALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 639
                self.match(YarcParser.GT_EQ)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 640
                self.match(YarcParser.LT_EQ)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 641
                self.match(YarcParser.NOT_EQ)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 642
                self.match(YarcParser.IN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 643
                self.match(YarcParser.NOT)
                self.state = 644
                self.match(YarcParser.IN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 645
                self.match(YarcParser.IS)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 646
                self.match(YarcParser.IS)
                self.state = 647
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(YarcParser.STAR, 0)

        def expr(self):
            return self.getTypedRuleContext(YarcParser.ExprContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_star_expr




    def star_expr(self):

        localctx = YarcParser.Star_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_star_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            self.match(YarcParser.STAR)
            self.state = 651
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xor_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Xor_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Xor_exprContext,i)


        def BIT_OR(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.BIT_OR)
            else:
                return self.getToken(YarcParser.BIT_OR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_expr




    def expr(self):

        localctx = YarcParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.xor_expr()
            self.state = 658
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.BIT_OR:
                self.state = 654
                self.match(YarcParser.BIT_OR)
                self.state = 655
                self.xor_expr()
                self.state = 660
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.And_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.And_exprContext,i)


        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.XOR)
            else:
                return self.getToken(YarcParser.XOR, i)

        def getRuleIndex(self):
            return YarcParser.RULE_xor_expr




    def xor_expr(self):

        localctx = YarcParser.Xor_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_xor_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.and_expr()
            self.state = 666
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.XOR:
                self.state = 662
                self.match(YarcParser.XOR)
                self.state = 663
                self.and_expr()
                self.state = 668
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Shift_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Shift_exprContext,i)


        def BIT_AND(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.BIT_AND)
            else:
                return self.getToken(YarcParser.BIT_AND, i)

        def getRuleIndex(self):
            return YarcParser.RULE_and_expr




    def and_expr(self):

        localctx = YarcParser.And_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_and_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 669
            self.shift_expr()
            self.state = 674
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.BIT_AND:
                self.state = 670
                self.match(YarcParser.BIT_AND)
                self.state = 671
                self.shift_expr()
                self.state = 676
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Arith_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Arith_exprContext,i)


        def LEFT_SHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.LEFT_SHIFT)
            else:
                return self.getToken(YarcParser.LEFT_SHIFT, i)

        def RIGHT_SHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.RIGHT_SHIFT)
            else:
                return self.getToken(YarcParser.RIGHT_SHIFT, i)

        def getRuleIndex(self):
            return YarcParser.RULE_shift_expr




    def shift_expr(self):

        localctx = YarcParser.Shift_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_shift_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.arith_expr()
            self.state = 682
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YarcParser.LEFT_SHIFT or _la==YarcParser.RIGHT_SHIFT:
                self.state = 678
                _la = self._input.LA(1)
                if not(_la==YarcParser.LEFT_SHIFT or _la==YarcParser.RIGHT_SHIFT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 679
                self.arith_expr()
                self.state = 684
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TermContext)
            else:
                return self.getTypedRuleContext(YarcParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.ADD)
            else:
                return self.getToken(YarcParser.ADD, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.MINUS)
            else:
                return self.getToken(YarcParser.MINUS, i)

        def getRuleIndex(self):
            return YarcParser.RULE_arith_expr




    def arith_expr(self):

        localctx = YarcParser.Arith_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_arith_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.term()
            self.state = 690
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 686
                    _la = self._input.LA(1)
                    if not(_la==YarcParser.ADD or _la==YarcParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 687
                    self.term() 
                self.state = 692
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.FactorContext)
            else:
                return self.getTypedRuleContext(YarcParser.FactorContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.STAR)
            else:
                return self.getToken(YarcParser.STAR, i)

        def AT(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.AT)
            else:
                return self.getToken(YarcParser.AT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.DIV)
            else:
                return self.getToken(YarcParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.MOD)
            else:
                return self.getToken(YarcParser.MOD, i)

        def IDIV(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.IDIV)
            else:
                return self.getToken(YarcParser.IDIV, i)

        def getRuleIndex(self):
            return YarcParser.RULE_term




    def term(self):

        localctx = YarcParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 693
            self.factor()
            self.state = 698
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 694
                    _la = self._input.LA(1)
                    if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & ((1 << (YarcParser.DIV - 61)) | (1 << (YarcParser.STAR - 61)) | (1 << (YarcParser.MOD - 61)) | (1 << (YarcParser.IDIV - 61)) | (1 << (YarcParser.AT - 61)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 695
                    self.factor() 
                self.state = 700
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(YarcParser.FactorContext,0)


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
        self.enterRule(localctx, 142, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YarcParser.BIT_NOT) | (1 << YarcParser.ADD) | (1 << YarcParser.MINUS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 702
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext,0)


        def NUMBER(self):
            return self.getToken(YarcParser.NUMBER, 0)

        def STRING(self, i:int=None):
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
        self.enterRule(localctx, 144, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 715
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.UNDERSCORE, YarcParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 704
                self.name()
                pass
            elif token in [YarcParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 705
                self.match(YarcParser.NUMBER)
                pass
            elif token in [YarcParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 707 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 706
                    self.match(YarcParser.STRING)
                    self.state = 709 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==YarcParser.STRING):
                        break

                pass
            elif token in [YarcParser.ELLIPSIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 711
                self.match(YarcParser.ELLIPSIS)
                pass
            elif token in [YarcParser.NONE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 712
                self.match(YarcParser.NONE)
                pass
            elif token in [YarcParser.TRUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 713
                self.match(YarcParser.TRUE)
                pass
            elif token in [YarcParser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 714
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(YarcParser.NAME, 0)

        def UNDERSCORE(self):
            return self.getToken(YarcParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_name




    def name(self):

        localctx = YarcParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            _la = self._input.LA(1)
            if not(_la==YarcParser.UNDERSCORE or _la==YarcParser.NAME):
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subscript_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Subscript_Context)
            else:
                return self.getTypedRuleContext(YarcParser.Subscript_Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_subscriptlist




    def subscriptlist(self):

        localctx = YarcParser.SubscriptlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_subscriptlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
            self.subscript_()
            self.state = 724
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 720
                    self.match(YarcParser.COMMA)
                    self.state = 721
                    self.subscript_() 
                self.state = 726
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

            self.state = 728
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.COMMA:
                self.state = 727
                self.match(YarcParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subscript_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext,i)


        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def sliceop(self):
            return self.getTypedRuleContext(YarcParser.SliceopContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_subscript_




    def subscript_(self):

        localctx = YarcParser.Subscript_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_subscript_)
        self._la = 0 # Token type
        try:
            self.state = 741
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 730
                self.test()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 732
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YarcParser.NOT) | (1 << YarcParser.BIT_NOT) | (1 << YarcParser.ADD) | (1 << YarcParser.MINUS))) != 0):
                    self.state = 731
                    self.test()


                self.state = 734
                self.match(YarcParser.COLON)
                self.state = 736
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YarcParser.NOT) | (1 << YarcParser.BIT_NOT) | (1 << YarcParser.ADD) | (1 << YarcParser.MINUS))) != 0):
                    self.state = 735
                    self.test()


                self.state = 739
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YarcParser.COLON:
                    self.state = 738
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_sliceop




    def sliceop(self):

        localctx = YarcParser.SliceopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_sliceop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(YarcParser.COLON)
            self.state = 745
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YarcParser.NOT) | (1 << YarcParser.BIT_NOT) | (1 << YarcParser.ADD) | (1 << YarcParser.MINUS))) != 0):
                self.state = 744
                self.test()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.ExprContext)
            else:
                return self.getTypedRuleContext(YarcParser.ExprContext,i)


        def star_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Star_exprContext)
            else:
                return self.getTypedRuleContext(YarcParser.Star_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_exprlist




    def exprlist(self):

        localctx = YarcParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                self.state = 747
                self.expr()
                pass
            elif token in [YarcParser.STAR]:
                self.state = 748
                self.star_expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 758
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 751
                    self.match(YarcParser.COMMA)
                    self.state = 754
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [YarcParser.BIT_NOT, YarcParser.ADD, YarcParser.MINUS]:
                        self.state = 752
                        self.expr()
                        pass
                    elif token in [YarcParser.STAR]:
                        self.state = 753
                        self.star_expr()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 760
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

            self.state = 762
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.COMMA:
                self.state = 761
                self.match(YarcParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_testlist




    def testlist(self):

        localctx = YarcParser.TestlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_testlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self.test()
            self.state = 769
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 765
                    self.match(YarcParser.COMMA)
                    self.state = 766
                    self.test() 
                self.state = 771
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

            self.state = 773
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==YarcParser.COMMA:
                self.state = 772
                self.match(YarcParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Encoding_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext,0)


        def getRuleIndex(self):
            return YarcParser.RULE_encoding_decl




    def encoding_decl(self):

        localctx = YarcParser.Encoding_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_encoding_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(YarcParser.STRING)
            else:
                return self.getToken(YarcParser.STRING, i)

        def getRuleIndex(self):
            return YarcParser.RULE_strings




    def strings(self):

        localctx = YarcParser.StringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_strings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 778 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 777
                self.match(YarcParser.STRING)
                self.state = 780 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==YarcParser.STRING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.literal_pattern_sempred
        self._predicates[31] = self.literal_expr_sempred
        self._predicates[38] = self.pattern_capture_target_sempred
        self._predicates[40] = self.value_pattern_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def literal_pattern_sempred(self, localctx:Literal_patternContext, predIndex:int):
            if predIndex == 0:
                return  self.CannotBePlusMinus() 
         

    def literal_expr_sempred(self, localctx:Literal_exprContext, predIndex:int):
            if predIndex == 1:
                return  self.CannotBePlusMinus() 
         

    def pattern_capture_target_sempred(self, localctx:Pattern_capture_targetContext, predIndex:int):
            if predIndex == 2:
                return  self.CannotBeDotLpEq() 
         

    def value_pattern_sempred(self, localctx:Value_patternContext, predIndex:int):
            if predIndex == 3:
                return  self.CannotBeDotLpEq() 
         




