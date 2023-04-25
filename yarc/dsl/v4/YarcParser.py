# Generated from c:\Users\feder\Desktop\University\Magistrale\Secondo_Anno\1_Linguaggi\Progetto\yarc\yarc\dsl\v4\YarcParser.g4 by ANTLR 4.9.2
import sys
from io import StringIO

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3x")
        buf.write("\u02fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write('\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%\4&\t')
        buf.write("&\4'\t'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\7\2\u0085")
        buf.write("\n\2\f\2\16\2\u0088\13\2\3\2\5\2\u008b\n\2\3\2\5\2\u008e")
        buf.write("\n\2\3\2\5\2\u0091\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0099")
        buf.write("\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\6\4\u00a2\n\4\r\4\16")
        buf.write("\4\u00a3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\6\6\u00b5\n\6\r\6\16\6\u00b6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\5\b\u00c1\n\b\3\b\3\b\3\b\6\b\u00c6")
        buf.write("\n\b\r\b\16\b\u00c7\3\t\3\t\3\t\3\t\3\t\6\t\u00cf\n\t")
        buf.write("\r\t\16\t\u00d0\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\5\13\u00dc\n\13\3\13\3\13\3\f\3\f\5\f\u00e2\n\f\3\f\5")
        buf.write("\f\u00e5\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ee\n\f")
        buf.write("\3\f\3\f\5\f\u00f2\n\f\3\f\3\f\5\f\u00f6\n\f\3\r\3\r\5")
        buf.write("\r\u00fa\n\r\3\r\3\r\3\r\3\r\5\r\u0100\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\7\16\u0107\n\16\f\16\16\16\u010a\13\16\3")
        buf.write("\16\3\16\3\16\5\16\u010f\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u0116\n\17\3\17\5\17\u0119\n\17\3\17\3\17\3\17\5")
        buf.write("\17\u011e\n\17\3\20\3\20\3\20\3\20\3\20\6\20\u0125\n\20")
        buf.write("\r\20\16\20\u0126\3\20\3\20\3\21\3\21\3\21\3\21\6\21\u012f")
        buf.write("\n\21\r\21\16\21\u0130\3\21\3\21\3\22\3\22\3\22\5\22\u0138")
        buf.write("\n\22\3\23\3\23\3\23\5\23\u013d\n\23\3\23\5\23\u0140\n")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\5\25\u0149\n\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0152\n\25\3")
        buf.write("\25\3\25\5\25\u0156\n\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0164\n\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\6\27\u016f\n\27")
        buf.write("\r\27\16\27\u0170\3\27\3\27\3\30\3\30\3\30\3\31\3\31\5")
        buf.write("\31\u017a\n\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\6\32")
        buf.write("\u0183\n\32\r\32\16\32\u0184\3\32\3\32\3\33\3\33\3\33")
        buf.write("\5\33\u018c\n\33\3\33\3\33\5\33\u0190\n\33\5\33\u0192")
        buf.write("\n\33\3\33\5\33\u0195\n\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u019e\n\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u01a5\n\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u01ad\n")
        buf.write("\34\5\34\u01af\n\34\3\34\3\34\3\34\5\34\u01b4\n\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u01ba\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u01c2\n\35\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u01cc\n\37\3 \3 \3!\3!\3!\7!\u01d3\n!")
        buf.write('\f!\16!\u01d6\13!\3"\3"\3"\7"\u01db\n"\f"\16"\u01de')
        buf.write('\13"\3#\3#\3#\5#\u01e3\n#\3$\3$\3$\3$\7$\u01e9\n$\f$')
        buf.write("\16$\u01ec\13$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%")
        buf.write("\u01fa\n%\3&\3&\3&\7&\u01ff\n&\f&\16&\u0202\13&\3'\3")
        buf.write("'\3'\7'\u0207\n'\f'\16'\u020a\13'\3(\3(\3(\7(\u020f")
        buf.write("\n(\f(\16(\u0212\13(\3)\3)\3)\7)\u0217\n)\f)\16)\u021a")
        buf.write("\13)\3*\3*\3*\7*\u021f\n*\f*\16*\u0222\13*\3+\3+\3+\7")
        buf.write("+\u0227\n+\f+\16+\u022a\13+\3,\3,\3,\5,\u022f\n,\3-\3")
        buf.write("-\3-\5-\u0234\n-\3.\3.\7.\u0238\n.\f.\16.\u023b\13.\3")
        buf.write("/\3/\3/\3/\3/\3/\5/\u0243\n/\3/\5/\u0246\n/\3/\3/\3/\3")
        buf.write("/\5/\u024c\n/\3/\5/\u024f\n/\3/\3/\3/\5/\u0254\n/\3/\3")
        buf.write("/\3/\5/\u0259\n/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0265")
        buf.write("\n/\3\60\3\60\3\61\3\61\5\61\u026b\n\61\3\61\3\61\3\61")
        buf.write("\5\61\u0270\n\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\64\3\64\7\64\u027d\n\64\f\64\16\64\u0280\13")
        buf.write("\64\5\64\u0282\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u0290\n\66\3\67\3\67\3")
        buf.write("\67\7\67\u0295\n\67\f\67\16\67\u0298\13\67\38\38\38\3")
        buf.write("8\58\u029e\n8\39\39\39\79\u02a3\n9\f9\169\u02a6\139\3")
        buf.write(":\3:\3:\5:\u02ab\n:\3:\5:\u02ae\n:\5:\u02b0\n:\3:\3:\5")
        buf.write(":\u02b4\n:\3:\5:\u02b7\n:\5:\u02b9\n:\3;\3;\5;\u02bd\n")
        buf.write(";\3<\3<\3<\7<\u02c2\n<\f<\16<\u02c5\13<\3=\3=\3=\7=\u02ca")
        buf.write("\n=\f=\16=\u02cd\13=\3>\3>\3>\3>\3>\3>\3>\3>\3>\7>\u02d8")
        buf.write("\n>\f>\16>\u02db\13>\5>\u02dd\n>\3>\3>\3>\7>\u02e2\n>")
        buf.write("\f>\16>\u02e5\13>\5>\u02e7\n>\5>\u02e9\n>\3?\3?\5?\u02ed")
        buf.write("\n?\3@\3@\3@\3@\3@\5@\u02f4\n@\3A\3A\3A\5A\u02f9\nA\3")
        buf.write('A\2\2B\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 "$&(*,')
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\2\n\3\2'(\3\2al\3\2LM\3\2NO\3\2PS\4\2KKNO\4\2@@mm\3")
        buf.write("\2)-\2\u0346\2\u0082\3\2\2\2\4\u0094\3\2\2\2\6\u009c\3")
        buf.write("\2\2\2\b\u00a7\3\2\2\2\n\u00ae\3\2\2\2\f\u00ba\3\2\2\2")
        buf.write("\16\u00c0\3\2\2\2\20\u00c9\3\2\2\2\22\u00d4\3\2\2\2\24")
        buf.write("\u00d8\3\2\2\2\26\u00df\3\2\2\2\30\u00f7\3\2\2\2\32\u0101")
        buf.write("\3\2\2\2\34\u0110\3\2\2\2\36\u011f\3\2\2\2 \u012a\3\2")
        buf.write('\2\2"\u0137\3\2\2\2$\u0139\3\2\2\2&\u0143\3\2\2\2(\u0163')
        buf.write("\3\2\2\2*\u0167\3\2\2\2,\u016a\3\2\2\2.\u0174\3\2\2\2")
        buf.write("\60\u0177\3\2\2\2\62\u017d\3\2\2\2\64\u0194\3\2\2\2\66")
        buf.write("\u01b9\3\2\2\28\u01bb\3\2\2\2:\u01c3\3\2\2\2<\u01c5\3")
        buf.write("\2\2\2>\u01cd\3\2\2\2@\u01cf\3\2\2\2B\u01d7\3\2\2\2D\u01e2")
        buf.write("\3\2\2\2F\u01e4\3\2\2\2H\u01f9\3\2\2\2J\u01fb\3\2\2\2")
        buf.write("L\u0203\3\2\2\2N\u020b\3\2\2\2P\u0213\3\2\2\2R\u021b\3")
        buf.write("\2\2\2T\u0223\3\2\2\2V\u022e\3\2\2\2X\u0230\3\2\2\2Z\u0235")
        buf.write("\3\2\2\2\\\u0264\3\2\2\2^\u0266\3\2\2\2`\u026f\3\2\2\2")
        buf.write("b\u0271\3\2\2\2d\u0276\3\2\2\2f\u0278\3\2\2\2h\u0283\3")
        buf.write("\2\2\2j\u028f\3\2\2\2l\u0291\3\2\2\2n\u0299\3\2\2\2p\u029f")
        buf.write("\3\2\2\2r\u02b8\3\2\2\2t\u02ba\3\2\2\2v\u02be\3\2\2\2")
        buf.write("x\u02c6\3\2\2\2z\u02ce\3\2\2\2|\u02ec\3\2\2\2~\u02ee\3")
        buf.write("\2\2\2\u0080\u02f5\3\2\2\2\u0082\u0086\5\4\3\2\u0083\u0085")
        buf.write("\7v\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u008a\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0089\u008b\5\6\4\2\u008a\u0089\3")
        buf.write("\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008e")
        buf.write("\5\b\5\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u0091\5\n\6\2\u0090\u008f\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\7")
        buf.write("\2\2\3\u0093\3\3\2\2\2\u0094\u0095\7\5\2\2\u0095\u0098")
        buf.write("\5^\60\2\u0096\u0097\7E\2\2\u0097\u0099\5^\60\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\7v\2\2\u009b\5\3\2\2\2\u009c\u009d\7\6\2")
        buf.write("\2\u009d\u009e\7E\2\2\u009e\u009f\7v\2\2\u009f\u00a1\7")
        buf.write("\3\2\2\u00a0\u00a2\5\f\7\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\7\4\2\2\u00a6\7\3\2\2\2\u00a7")
        buf.write("\u00a8\7\7\2\2\u00a8\u00a9\7E\2\2\u00a9\u00aa\7v\2\2\u00aa")
        buf.write("\u00ab\7\3\2\2\u00ab\u00ac\5\16\b\2\u00ac\u00ad\7\4\2")
        buf.write("\2\u00ad\t\3\2\2\2\u00ae\u00af\7\b\2\2\u00af\u00b0\7E")
        buf.write("\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b4\7\3\2\2\u00b2\u00b5")
        buf.write("\5\64\33\2\u00b3\u00b5\5\20\t\2\u00b4\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\7")
        buf.write("\4\2\2\u00b9\13\3\2\2\2\u00ba\u00bb\7m\2\2\u00bb\u00bc")
        buf.write("\7G\2\2\u00bc\u00bd\5<\37\2\u00bd\u00be\7v\2\2\u00be\r")
        buf.write("\3\2\2\2\u00bf\u00c1\5\22\n\2\u00c0\u00bf\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00c5\3\2\2\2\u00c2\u00c6\5\66\34")
        buf.write("\2\u00c3\u00c6\5\24\13\2\u00c4\u00c6\5.\30\2\u00c5\u00c2")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\17\3\2\2\2\u00c9\u00ca\7m\2\2\u00ca\u00cb\7E\2")
        buf.write("\2\u00cb\u00cc\7v\2\2\u00cc\u00ce\7\3\2\2\u00cd\u00cf")
        buf.write("\5\f\7\2\u00ce\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d3\7\4\2\2\u00d3\21\3\2\2\2\u00d4\u00d5\7\17")
        buf.write("\2\2\u00d5\u00d6\5<\37\2\u00d6\u00d7\7v\2\2\u00d7\23\3")
        buf.write("\2\2\2\u00d8\u00db\7\24\2\2\u00d9\u00dc\7\16\2\2\u00da")
        buf.write("\u00dc\5^\60\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd\u00de\5\36\20\2\u00de\25\3")
        buf.write("\2\2\2\u00df\u00e1\7\20\2\2\u00e0\u00e2\5<\37\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00f5\3\2\2\2")
        buf.write("\u00e3\u00e5\7\f\2\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3")
        buf.write("\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00ee\7\n\2\2\u00e7\u00ee")
        buf.write("\7\t\2\2\u00e8\u00e9\5^\60\2\u00e9\u00ea\7\13\2\2\u00ea")
        buf.write("\u00ee\3\2\2\2\u00eb\u00ec\7\67\2\2\u00ec\u00ee\5<\37")
        buf.write("\2\u00ed\u00e4\3\2\2\2\u00ed\u00e7\3\2\2\2\u00ed\u00e8")
        buf.write("\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00f2\5\36\20\2\u00f0\u00f2\7v\2\2\u00f1\u00ef\3\2\2")
        buf.write("\2\u00f1\u00f0\3\2\2\2\u00f2\u00f6\3\2\2\2\u00f3\u00f4")
        buf.write("\7\r\2\2\u00f4\u00f6\5 \21\2\u00f5\u00ed\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\27\3\2\2\2\u00f7\u00f9\7\22\2\2\u00f8")
        buf.write("\u00fa\5<\37\2\u00f9\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00fc\7\67\2\2\u00fc\u00ff")
        buf.write("\5<\37\2\u00fd\u0100\5\36\20\2\u00fe\u0100\7v\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\31\3\2\2\2\u0101")
        buf.write("\u0102\7\21\2\2\u0102\u0103\7W\2\2\u0103\u0108\5^\60\2")
        buf.write("\u0104\u0105\7D\2\2\u0105\u0107\5^\60\2\u0106\u0104\3")
        buf.write("\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010e\7X\2\2\u010c\u010f\5\36\20\2\u010d\u010f\7v\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010e\u010d\3\2\2\2\u010f\33\3\2")
        buf.write("\2\2\u0110\u0118\7\23\2\2\u0111\u0116\7\n\2\2\u0112\u0116")
        buf.write("\7\13\2\2\u0113\u0116\7\r\2\2\u0114\u0116\5^\60\2\u0115")
        buf.write("\u0111\3\2\2\2\u0115\u0112\3\2\2\2\u0115\u0113\3\2\2\2")
        buf.write("\u0115\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119\7")
        buf.write("\61\2\2\u0118\u0115\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011d\5<\37\2\u011b\u011e\5 \21\2")
        buf.write("\u011c\u011e\7v\2\2\u011d\u011b\3\2\2\2\u011d\u011c\3")
        buf.write("\2\2\2\u011e\35\3\2\2\2\u011f\u0120\7E\2\2\u0120\u0121")
        buf.write('\7v\2\2\u0121\u0124\7\3\2\2\u0122\u0125\5"\22\2\u0123')
        buf.write("\u0125\5*\26\2\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\7\4\2\2\u0129\37")
        buf.write("\3\2\2\2\u012a\u012b\7E\2\2\u012b\u012c\7v\2\2\u012c\u012e")
        buf.write("\7\3\2\2\u012d\u012f\5$\23\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0133\7\4\2\2\u0133!\3\2\2")
        buf.write("\2\u0134\u0138\5(\25\2\u0135\u0138\5$\23\2\u0136\u0138")
        buf.write("\5&\24\2\u0137\u0134\3\2\2\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138#\3\2\2\2\u0139\u013c\5^\60\2\u013a")
        buf.write("\u013b\7E\2\2\u013b\u013d\5^\60\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u0140\5")
        buf.write("<\37\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0142\7v\2\2\u0142%\3\2\2\2\u0143\u0144")
        buf.write("\7\"\2\2\u0144\u0145\7v\2\2\u0145'\3\2\2\2\u0146\u0148")
        buf.write("\7\27\2\2\u0147\u0149\7 \2\2\u0148\u0147\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\7/\2\2")
        buf.write("\u014b\u0164\5<\37\2\u014c\u014d\7\30\2\2\u014d\u014e")
        buf.write("\7/\2\2\u014e\u0164\5<\37\2\u014f\u0151\7\31\2\2\u0150")
        buf.write("\u0152\7 \2\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0155\5<\37\2\u0154\u0156\7")
        buf.write("!\2\2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0164")
        buf.write("\3\2\2\2\u0157\u0158\7\32\2\2\u0158\u0164\5<\37\2\u0159")
        buf.write("\u015a\7\36\2\2\u015a\u0164\5<\37\2\u015b\u015c\7\37\2")
        buf.write("\2\u015c\u0164\5<\37\2\u015d\u015e\7\35\2\2\u015e\u0164")
        buf.write("\5<\37\2\u015f\u0160\7\33\2\2\u0160\u0164\5<\37\2\u0161")
        buf.write("\u0162\7\34\2\2\u0162\u0164\5<\37\2\u0163\u0146\3\2\2")
        buf.write("\2\u0163\u014c\3\2\2\2\u0163\u014f\3\2\2\2\u0163\u0157")
        buf.write("\3\2\2\2\u0163\u0159\3\2\2\2\u0163\u015b\3\2\2\2\u0163")
        buf.write("\u015d\3\2\2\2\u0163\u015f\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0166\7v\2\2\u0166)\3\2\2\2")
        buf.write("\u0167\u0168\5\60\31\2\u0168\u0169\5,\27\2\u0169+\3\2")
        buf.write("\2\2\u016a\u016b\7E\2\2\u016b\u016c\7v\2\2\u016c\u016e")
        buf.write('\7\3\2\2\u016d\u016f\5"\22\2\u016e\u016d\3\2\2\2\u016f')
        buf.write("\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0172\3\2\2\2\u0172\u0173\7\4\2\2\u0173-\3\2\2")
        buf.write("\2\u0174\u0175\5\60\31\2\u0175\u0176\5\62\32\2\u0176/")
        buf.write("\3\2\2\2\u0177\u0179\7&\2\2\u0178\u017a\5<\37\2\u0179")
        buf.write("\u0178\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u017c\t\2\2\2\u017c\61\3\2\2\2\u017d\u017e\7E\2")
        buf.write("\2\u017e\u017f\7v\2\2\u017f\u0182\7\3\2\2\u0180\u0183")
        buf.write("\5\66\34\2\u0181\u0183\5\24\13\2\u0182\u0180\3\2\2\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\7")
        buf.write("\4\2\2\u0187\63\3\2\2\2\u0188\u0191\5x=\2\u0189\u018c")
        buf.write("\5:\36\2\u018a\u018c\7G\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u0190\5x=\2\u018e")
        buf.write("\u0190\58\35\2\u018f\u018d\3\2\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190\u0192\3\2\2\2\u0191\u018b\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192\u0195\3\2\2\2\u0193\u0195\58\35\2\u0194\u0188")
        buf.write("\3\2\2\2\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0197\7v\2\2\u0197\65\3\2\2\2\u0198\u01ae\5x=\2\u0199")
        buf.write("\u01af\7v\2\2\u019a\u019d\5:\36\2\u019b\u019e\5x=\2\u019c")
        buf.write("\u019e\58\35\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\7")
        buf.write("v\2\2\u01a0\u01af\3\2\2\2\u01a1\u01ac\7G\2\2\u01a2\u01a5")
        buf.write("\5x=\2\u01a3\u01a5\58\35\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\7v\2\2\u01a7")
        buf.write("\u01ad\3\2\2\2\u01a8\u01ad\5\26\f\2\u01a9\u01ad\5\30\r")
        buf.write("\2\u01aa\u01ad\5\34\17\2\u01ab\u01ad\5\32\16\2\u01ac\u01a4")
        buf.write("\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac\u01a9\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01af\3\2\2\2")
        buf.write("\u01ae\u0199\3\2\2\2\u01ae\u019a\3\2\2\2\u01ae\u01a1\3")
        buf.write("\2\2\2\u01af\u01b4\3\2\2\2\u01b0\u01b1\58\35\2\u01b1\u01b2")
        buf.write("\7v\2\2\u01b2\u01b4\3\2\2\2\u01b3\u0198\3\2\2\2\u01b3")
        buf.write("\u01b0\3\2\2\2\u01b4\u01ba\3\2\2\2\u01b5\u01ba\5\26\f")
        buf.write("\2\u01b6\u01ba\5\30\r\2\u01b7\u01ba\5\34\17\2\u01b8\u01ba")
        buf.write("\5\32\16\2\u01b9\u01b3\3\2\2\2\u01b9\u01b5\3\2\2\2\u01b9")
        buf.write("\u01b6\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2")
        buf.write("\u01ba\67\3\2\2\2\u01bb\u01bc\7\25\2\2\u01bc\u01bd\5<")
        buf.write("\37\2\u01bd\u01be\7\67\2\2\u01be\u01c1\5<\37\2\u01bf\u01c0")
        buf.write("\7\26\2\2\u01c0\u01c2\5<\37\2\u01c1\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c29\3\2\2\2\u01c3\u01c4\t\3\2\2\u01c4")
        buf.write(";\3\2\2\2\u01c5\u01cb\5@!\2\u01c6\u01c7\78\2\2\u01c7\u01c8")
        buf.write("\5@!\2\u01c8\u01c9\7\64\2\2\u01c9\u01ca\5<\37\2\u01ca")
        buf.write("\u01cc\3\2\2\2\u01cb\u01c6\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc=\3\2\2\2\u01cd\u01ce\5@!\2\u01ce?\3\2\2\2\u01cf")
        buf.write('\u01d4\5B"\2\u01d0\u01d1\7=\2\2\u01d1\u01d3\5B"\2\u01d2')
        buf.write("\u01d0\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5A\3\2\2\2\u01d6\u01d4\3\2\2")
        buf.write("\2\u01d7\u01dc\5D#\2\u01d8\u01d9\7\62\2\2\u01d9\u01db")
        buf.write("\5D#\2\u01da\u01d8\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01ddC\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01df\u01e0\7<\2\2\u01e0\u01e3\5D#\2\u01e1\u01e3")
        buf.write("\5F$\2\u01e2\u01df\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3E")
        buf.write("\3\2\2\2\u01e4\u01ea\5J&\2\u01e5\u01e6\5H%\2\u01e6\u01e7")
        buf.write("\5J&\2\u01e7\u01e9\3\2\2\2\u01e8\u01e5\3\2\2\2\u01e9\u01ec")
        buf.write("\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write("G\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01fa\7[\2\2\u01ee")
        buf.write("\u01fa\7\\\2\2\u01ef\u01fa\7]\2\2\u01f0\u01fa\7^\2\2\u01f1")
        buf.write("\u01fa\7_\2\2\u01f2\u01fa\7`\2\2\u01f3\u01fa\79\2\2\u01f4")
        buf.write("\u01f5\7<\2\2\u01f5\u01fa\79\2\2\u01f6\u01fa\7:\2\2\u01f7")
        buf.write("\u01f8\7:\2\2\u01f8\u01fa\7<\2\2\u01f9\u01ed\3\2\2\2\u01f9")
        buf.write("\u01ee\3\2\2\2\u01f9\u01ef\3\2\2\2\u01f9\u01f0\3\2\2\2")
        buf.write("\u01f9\u01f1\3\2\2\2\u01f9\u01f2\3\2\2\2\u01f9\u01f3\3")
        buf.write("\2\2\2\u01f9\u01f4\3\2\2\2\u01f9\u01f6\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01faI\3\2\2\2\u01fb\u0200\5L'\2\u01fc\u01fd")
        buf.write("\7H\2\2\u01fd\u01ff\5L'\2\u01fe\u01fc\3\2\2\2\u01ff\u0202")
        buf.write("\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201")
        buf.write("K\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0208\5N(\2\u0204")
        buf.write("\u0205\7I\2\2\u0205\u0207\5N(\2\u0206\u0204\3\2\2\2\u0207")
        buf.write("\u020a\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2")
        buf.write("\u0209M\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u0210\5P)\2")
        buf.write("\u020c\u020d\7J\2\2\u020d\u020f\5P)\2\u020e\u020c\3\2")
        buf.write("\2\2\u020f\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211O\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0218")
        buf.write("\5R*\2\u0214\u0215\t\4\2\2\u0215\u0217\5R*\2\u0216\u0214")
        buf.write("\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219Q\3\2\2\2\u021a\u0218\3\2\2\2\u021b")
        buf.write("\u0220\5T+\2\u021c\u021d\t\5\2\2\u021d\u021f\5T+\2\u021e")
        buf.write("\u021c\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u0221\3\2\2\2\u0221S\3\2\2\2\u0222\u0220\3\2\2")
        buf.write("\2\u0223\u0228\5V,\2\u0224\u0225\t\6\2\2\u0225\u0227\5")
        buf.write("V,\2\u0226\u0224\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226")
        buf.write("\3\2\2\2\u0228\u0229\3\2\2\2\u0229U\3\2\2\2\u022a\u0228")
        buf.write("\3\2\2\2\u022b\u022c\t\7\2\2\u022c\u022f\5V,\2\u022d\u022f")
        buf.write("\5X-\2\u022e\u022b\3\2\2\2\u022e\u022d\3\2\2\2\u022fW")
        buf.write("\3\2\2\2\u0230\u0233\5Z.\2\u0231\u0232\7T\2\2\u0232\u0234")
        buf.write("\5V,\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234Y")
        buf.write("\3\2\2\2\u0235\u0239\5\\/\2\u0236\u0238\5j\66\2\u0237")
        buf.write("\u0236\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u0239\u023a\3\2\2\2\u023a[\3\2\2\2\u023b\u0239\3\2\2")
        buf.write("\2\u023c\u023d\7U\2\2\u023d\u023e\5<\37\2\u023e\u023f")
        buf.write("\7V\2\2\u023f\u0265\3\2\2\2\u0240\u024e\7W\2\2\u0241\u0243")
        buf.write("\5f\64\2\u0242\u0241\3\2\2\2\u0242\u0243\3\2\2\2\u0243")
        buf.write("\u024f\3\2\2\2\u0244\u0246\7O\2\2\u0245\u0244\3\2\2\2")
        buf.write("\u0245\u0246\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0248\7")
        buf.write("p\2\2\u0248\u0249\3\2\2\2\u0249\u024b\7B\2\2\u024a\u024c")
        buf.write("\7O\2\2\u024b\u024a\3\2\2\2\u024b\u024c\3\2\2\2\u024c")
        buf.write("\u024d\3\2\2\2\u024d\u024f\7p\2\2\u024e\u0242\3\2\2\2")
        buf.write("\u024e\u0245\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0265\7")
        buf.write("X\2\2\u0251\u0253\7[\2\2\u0252\u0254\5h\65\2\u0253\u0252")
        buf.write("\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0255\3\2\2\2\u0255")
        buf.write("\u0265\7\\\2\2\u0256\u0258\7Y\2\2\u0257\u0259\5z>\2\u0258")
        buf.write("\u0257\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025a\3\2\2\2")
        buf.write("\u025a\u0265\7Z\2\2\u025b\u0265\5^\60\2\u025c\u0265\7")
        buf.write("n\2\2\u025d\u0265\5b\62\2\u025e\u0265\7p\2\2\u025f\u0265")
        buf.write("\7u\2\2\u0260\u0265\7o\2\2\u0261\u0265\7;\2\2\u0262\u0265")
        buf.write("\7?\2\2\u0263\u0265\7\65\2\2\u0264\u023c\3\2\2\2\u0264")
        buf.write("\u0240\3\2\2\2\u0264\u0251\3\2\2\2\u0264\u0256\3\2\2\2")
        buf.write("\u0264\u025b\3\2\2\2\u0264\u025c\3\2\2\2\u0264\u025d\3")
        buf.write("\2\2\2\u0264\u025e\3\2\2\2\u0264\u025f\3\2\2\2\u0264\u0260")
        buf.write("\3\2\2\2\u0264\u0261\3\2\2\2\u0264\u0262\3\2\2\2\u0264")
        buf.write("\u0263\3\2\2\2\u0265]\3\2\2\2\u0266\u0267\t\b\2\2\u0267")
        buf.write("_\3\2\2\2\u0268\u0270\7\t\2\2\u0269\u026b\7\f\2\2\u026a")
        buf.write("\u0269\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026c\3\2\2\2")
        buf.write("\u026c\u0270\7\n\2\2\u026d\u0270\7\13\2\2\u026e\u0270")
        buf.write("\7\r\2\2\u026f\u0268\3\2\2\2\u026f\u026a\3\2\2\2\u026f")
        buf.write("\u026d\3\2\2\2\u026f\u026e\3\2\2\2\u0270a\3\2\2\2\u0271")
        buf.write("\u0272\5d\63\2\u0272\u0273\7U\2\2\u0273\u0274\5l\67\2")
        buf.write("\u0274\u0275\7V\2\2\u0275c\3\2\2\2\u0276\u0277\t\t\2\2")
        buf.write("\u0277e\3\2\2\2\u0278\u0281\5<\37\2\u0279\u0282\5~@\2")
        buf.write("\u027a\u027b\7D\2\2\u027b\u027d\5<\37\2\u027c\u027a\3")
        buf.write("\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c\3\2\2\2\u027e\u027f")
        buf.write("\3\2\2\2\u027f\u0282\3\2\2\2\u0280\u027e\3\2\2\2\u0281")
        buf.write("\u0279\3\2\2\2\u0281\u027e\3\2\2\2\u0282g\3\2\2\2\u0283")
        buf.write("\u0284\5J&\2\u0284\u0285\7D\2\2\u0285\u0286\5J&\2\u0286")
        buf.write("\u0287\7D\2\2\u0287\u0288\5J&\2\u0288i\3\2\2\2\u0289\u028a")
        buf.write("\7W\2\2\u028a\u028b\5p9\2\u028b\u028c\7X\2\2\u028c\u0290")
        buf.write("\3\2\2\2\u028d\u028e\7A\2\2\u028e\u0290\5^\60\2\u028f")
        buf.write("\u0289\3\2\2\2\u028f\u028d\3\2\2\2\u0290k\3\2\2\2\u0291")
        buf.write("\u0296\5n8\2\u0292\u0293\7D\2\2\u0293\u0295\5n8\2\u0294")
        buf.write("\u0292\3\2\2\2\u0295\u0298\3\2\2\2\u0296\u0294\3\2\2\2")
        buf.write("\u0296\u0297\3\2\2\2\u0297m\3\2\2\2\u0298\u0296\3\2\2")
        buf.write("\2\u0299\u029d\5<\37\2\u029a\u029e\5~@\2\u029b\u029c\7")
        buf.write("G\2\2\u029c\u029e\5<\37\2\u029d\u029a\3\2\2\2\u029d\u029b")
        buf.write("\3\2\2\2\u029d\u029e\3\2\2\2\u029eo\3\2\2\2\u029f\u02a4")
        buf.write("\5r:\2\u02a0\u02a1\7D\2\2\u02a1\u02a3\5r:\2\u02a2\u02a0")
        buf.write("\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4")
        buf.write("\u02a5\3\2\2\2\u02a5q\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a7")
        buf.write("\u02af\5<\37\2\u02a8\u02aa\7E\2\2\u02a9\u02ab\5<\37\2")
        buf.write("\u02aa\u02a9\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab\u02ad\3")
        buf.write("\2\2\2\u02ac\u02ae\5t;\2\u02ad\u02ac\3\2\2\2\u02ad\u02ae")
        buf.write("\3\2\2\2\u02ae\u02b0\3\2\2\2\u02af\u02a8\3\2\2\2\u02af")
        buf.write("\u02b0\3\2\2\2\u02b0\u02b9\3\2\2\2\u02b1\u02b3\7E\2\2")
        buf.write("\u02b2\u02b4\5<\37\2\u02b3\u02b2\3\2\2\2\u02b3\u02b4\3")
        buf.write("\2\2\2\u02b4\u02b6\3\2\2\2\u02b5\u02b7\5t;\2\u02b6\u02b5")
        buf.write("\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u02b9\3\2\2\2\u02b8")
        buf.write("\u02a7\3\2\2\2\u02b8\u02b1\3\2\2\2\u02b9s\3\2\2\2\u02ba")
        buf.write("\u02bc\7E\2\2\u02bb\u02bd\5<\37\2\u02bc\u02bb\3\2\2\2")
        buf.write("\u02bc\u02bd\3\2\2\2\u02bdu\3\2\2\2\u02be\u02c3\5J&\2")
        buf.write("\u02bf\u02c0\7D\2\2\u02c0\u02c2\5J&\2\u02c1\u02bf\3\2")
        buf.write("\2\2\u02c2\u02c5\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3\u02c4")
        buf.write("\3\2\2\2\u02c4w\3\2\2\2\u02c5\u02c3\3\2\2\2\u02c6\u02cb")
        buf.write("\5<\37\2\u02c7\u02c8\7D\2\2\u02c8\u02ca\5<\37\2\u02c9")
        buf.write("\u02c7\3\2\2\2\u02ca\u02cd\3\2\2\2\u02cb\u02c9\3\2\2\2")
        buf.write("\u02cb\u02cc\3\2\2\2\u02ccy\3\2\2\2\u02cd\u02cb\3\2\2")
        buf.write("\2\u02ce\u02e8\5<\37\2\u02cf\u02d0\7E\2\2\u02d0\u02dc")
        buf.write("\5<\37\2\u02d1\u02dd\5~@\2\u02d2\u02d3\7D\2\2\u02d3\u02d4")
        buf.write("\5<\37\2\u02d4\u02d5\7E\2\2\u02d5\u02d6\5<\37\2\u02d6")
        buf.write("\u02d8\3\2\2\2\u02d7\u02d2\3\2\2\2\u02d8\u02db\3\2\2\2")
        buf.write("\u02d9\u02d7\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u02dd\3")
        buf.write("\2\2\2\u02db\u02d9\3\2\2\2\u02dc\u02d1\3\2\2\2\u02dc\u02d9")
        buf.write("\3\2\2\2\u02dd\u02e9\3\2\2\2\u02de\u02e7\5~@\2\u02df\u02e0")
        buf.write("\7D\2\2\u02e0\u02e2\5<\37\2\u02e1\u02df\3\2\2\2\u02e2")
        buf.write("\u02e5\3\2\2\2\u02e3\u02e1\3\2\2\2\u02e3\u02e4\3\2\2\2")
        buf.write("\u02e4\u02e7\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e6\u02de\3")
        buf.write("\2\2\2\u02e6\u02e3\3\2\2\2\u02e7\u02e9\3\2\2\2\u02e8\u02cf")
        buf.write("\3\2\2\2\u02e8\u02e6\3\2\2\2\u02e9{\3\2\2\2\u02ea\u02ed")
        buf.write("\5~@\2\u02eb\u02ed\5\u0080A\2\u02ec\u02ea\3\2\2\2\u02ec")
        buf.write("\u02eb\3\2\2\2\u02ed}\3\2\2\2\u02ee\u02ef\7\66\2\2\u02ef")
        buf.write("\u02f0\5v<\2\u02f0\u02f1\79\2\2\u02f1\u02f3\5@!\2\u02f2")
        buf.write("\u02f4\5|?\2\u02f3\u02f2\3\2\2\2\u02f3\u02f4\3\2\2\2\u02f4")
        buf.write("\177\3\2\2\2\u02f5\u02f6\78\2\2\u02f6\u02f8\5> \2\u02f7")
        buf.write("\u02f9\5|?\2\u02f8\u02f7\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9")
        buf.write("\u0081\3\2\2\2c\u0086\u008a\u008d\u0090\u0098\u00a3\u00b4")
        buf.write("\u00b6\u00c0\u00c5\u00c7\u00d0\u00db\u00e1\u00e4\u00ed")
        buf.write("\u00f1\u00f5\u00f9\u00ff\u0108\u010e\u0115\u0118\u011d")
        buf.write("\u0124\u0126\u0130\u0137\u013c\u013f\u0148\u0151\u0155")
        buf.write("\u0163\u0170\u0179\u0182\u0184\u018b\u018f\u0191\u0194")
        buf.write("\u019d\u01a4\u01ac\u01ae\u01b3\u01b9\u01c1\u01cb\u01d4")
        buf.write("\u01dc\u01e2\u01ea\u01f9\u0200\u0208\u0210\u0218\u0220")
        buf.write("\u0228\u022e\u0233\u0239\u0242\u0245\u024b\u024e\u0253")
        buf.write("\u0258\u0264\u026a\u026f\u027e\u0281\u028f\u0296\u029d")
        buf.write("\u02a4\u02aa\u02ad\u02af\u02b3\u02b6\u02b8\u02bc\u02c3")
        buf.write("\u02cb\u02d9\u02dc\u02e3\u02e6\u02e8\u02ec\u02f3\u02f8")
        return buf.getvalue()


class YarcParser(Parser):
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
        "'stage'",
        "'writers'",
        "<INVALID>",
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
        "<INVALID>",
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

    RULE_scenario = 0
    RULE_declaration = 1
    RULE_settings = 2
    RULE_stage = 3
    RULE_writers = 4
    RULE_option = 5
    RULE_stmts = 6
    RULE_writer = 7
    RULE_open_stmt = 8
    RULE_edit_stmt = 9
    RULE_create_expr = 10
    RULE_instantiate_expr = 11
    RULE_group_expr = 12
    RULE_get_expr = 13
    RULE_edit_block = 14
    RULE_simple_block = 15
    RULE_attr = 16
    RULE_simple_attr = 17
    RULE_compound_attr = 18
    RULE_core_attr = 19
    RULE_inner_behavior_stmt = 20
    RULE_inner_behavior_block = 21
    RULE_behavior_stmt = 22
    RULE_behavior_expr = 23
    RULE_behavior_block = 24
    RULE_expr_stmt = 25
    RULE_aug_expr_stmt = 26
    RULE_fetch_expr = 27
    RULE_aug_assign = 28
    RULE_test = 29
    RULE_test_nocond = 30
    RULE_or_test = 31
    RULE_and_test = 32
    RULE_not_test = 33
    RULE_comparison = 34
    RULE_comp_op = 35
    RULE_expr = 36
    RULE_xor_expr = 37
    RULE_and_expr = 38
    RULE_shift_expr = 39
    RULE_arith_expr = 40
    RULE_term = 41
    RULE_factor = 42
    RULE_power = 43
    RULE_atom_expr = 44
    RULE_atom = 45
    RULE_name = 46
    RULE_primitives = 47
    RULE_distribution_expr = 48
    RULE_distribution = 49
    RULE_testlist_comp = 50
    RULE_vector_comp = 51
    RULE_trailer = 52
    RULE_arglist = 53
    RULE_argument = 54
    RULE_subscriptlist = 55
    RULE_subscript_ = 56
    RULE_sliceop = 57
    RULE_exprlist = 58
    RULE_testlist = 59
    RULE_dict_or_set_maker = 60
    RULE_comp_iter = 61
    RULE_comp_for = 62
    RULE_comp_if = 63

    ruleNames = [
        "scenario",
        "declaration",
        "settings",
        "stage",
        "writers",
        "option",
        "stmts",
        "writer",
        "open_stmt",
        "edit_stmt",
        "create_expr",
        "instantiate_expr",
        "group_expr",
        "get_expr",
        "edit_block",
        "simple_block",
        "attr",
        "simple_attr",
        "compound_attr",
        "core_attr",
        "inner_behavior_stmt",
        "inner_behavior_block",
        "behavior_stmt",
        "behavior_expr",
        "behavior_block",
        "expr_stmt",
        "aug_expr_stmt",
        "fetch_expr",
        "aug_assign",
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
        "distribution_expr",
        "distribution",
        "testlist_comp",
        "vector_comp",
        "trailer",
        "arglist",
        "argument",
        "subscriptlist",
        "subscript_",
        "sliceop",
        "exprlist",
        "testlist",
        "dict_or_set_maker",
        "comp_iter",
        "comp_for",
        "comp_if",
    ]

    EOF = Token.EOF
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

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ScenarioContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(YarcParser.DeclarationContext, 0)

        def EOF(self):
            return self.getToken(YarcParser.EOF, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.NEWLINE)
            else:
                return self.getToken(YarcParser.NEWLINE, i)

        def settings(self):
            return self.getTypedRuleContext(YarcParser.SettingsContext, 0)

        def stage(self):
            return self.getTypedRuleContext(YarcParser.StageContext, 0)

        def writers(self):
            return self.getTypedRuleContext(YarcParser.WritersContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_scenario

    def scenario(self):
        localctx = YarcParser.ScenarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_scenario)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.declaration()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.NEWLINE:
                self.state = 129
                self.match(YarcParser.NEWLINE)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.SETTINGS:
                self.state = 135
                self.settings()

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.STAGE:
                self.state = 138
                self.stage()

            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.WRITERS:
                self.state = 141
                self.writers()

            self.state = 144
            self.match(YarcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCENARIO(self):
            return self.getToken(YarcParser.SCENARIO, 0)

        def name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext, i)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_declaration

    def declaration(self):
        localctx = YarcParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(YarcParser.SCENARIO)
            self.state = 147
            self.name()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 148
                self.match(YarcParser.COLON)
                self.state = 149
                self.name()

            self.state = 152
            self.match(YarcParser.NEWLINE)
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

        def option(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.OptionContext)
            else:
                return self.getTypedRuleContext(YarcParser.OptionContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_settings

    def settings(self):
        localctx = YarcParser.SettingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_settings)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(YarcParser.SETTINGS)
            self.state = 155
            self.match(YarcParser.COLON)
            self.state = 156
            self.match(YarcParser.NEWLINE)
            self.state = 157
            self.match(YarcParser.INDENT)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 158
                self.option()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.ID):
                    break

            self.state = 163
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StageContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAGE(self):
            return self.getToken(YarcParser.STAGE, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def stmts(self):
            return self.getTypedRuleContext(YarcParser.StmtsContext, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_stage

    def stage(self):
        localctx = YarcParser.StageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(YarcParser.STAGE)
            self.state = 166
            self.match(YarcParser.COLON)
            self.state = 167
            self.match(YarcParser.NEWLINE)
            self.state = 168
            self.match(YarcParser.INDENT)
            self.state = 169
            self.stmts()
            self.state = 170
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WritersContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITERS(self):
            return self.getToken(YarcParser.WRITERS, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Expr_stmtContext, i)

        def writer(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.WriterContext)
            else:
                return self.getTypedRuleContext(YarcParser.WriterContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_writers

    def writers(self):
        localctx = YarcParser.WritersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_writers)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(YarcParser.WRITERS)
            self.state = 173
            self.match(YarcParser.COLON)
            self.state = 174
            self.match(YarcParser.NEWLINE)
            self.state = 175
            self.match(YarcParser.INDENT)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 6, self._ctx)
                if la_ == 1:
                    self.state = 176
                    self.expr_stmt()
                    pass

                elif la_ == 2:
                    self.state = 177
                    self.writer()
                    pass

                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.FETCH)
                                | (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 73) & ~0x3F) == 0
                        and (
                            (1 << (_la - 73))
                            & (
                                (1 << (YarcParser.BIT_NOT - 73))
                                | (1 << (YarcParser.PLUS - 73))
                                | (1 << (YarcParser.MINUS - 73))
                                | (1 << (YarcParser.LPAREN - 73))
                                | (1 << (YarcParser.LBRACK - 73))
                                | (1 << (YarcParser.LBRACE - 73))
                                | (1 << (YarcParser.LT - 73))
                                | (1 << (YarcParser.ID - 73))
                                | (1 << (YarcParser.SETTING_ID - 73))
                                | (1 << (YarcParser.STRING - 73))
                                | (1 << (YarcParser.INTEGER - 73))
                                | (1 << (YarcParser.FLOAT_NUMBER - 73))
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 182
            self.match(YarcParser.DEDENT)
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
        self.enterRule(localctx, 10, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(YarcParser.ID)
            self.state = 185
            self.match(YarcParser.ASSIGN)
            self.state = 186
            self.test()
            self.state = 187
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

        def open_stmt(self):
            return self.getTypedRuleContext(YarcParser.Open_stmtContext, 0)

        def aug_expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Aug_expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Aug_expr_stmtContext, i)

        def edit_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Edit_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Edit_stmtContext, i)

        def behavior_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Behavior_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Behavior_stmtContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_stmts

    def stmts(self):
        localctx = YarcParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmts)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.OPEN:
                self.state = 189
                self.open_stmt()

            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 195
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.CREATE,
                    YarcParser.GROUP,
                    YarcParser.INSTANTIATE,
                    YarcParser.GET,
                    YarcParser.FETCH,
                    YarcParser.UNIFORM,
                    YarcParser.NORMAL,
                    YarcParser.CHOICE,
                    YarcParser.SEQUENCE,
                    YarcParser.LOG_UNIFORM,
                    YarcParser.FALSE,
                    YarcParser.NONE,
                    YarcParser.NOT,
                    YarcParser.TRUE,
                    YarcParser.UNDERSCORE,
                    YarcParser.BIT_NOT,
                    YarcParser.PLUS,
                    YarcParser.MINUS,
                    YarcParser.LPAREN,
                    YarcParser.LBRACK,
                    YarcParser.LBRACE,
                    YarcParser.LT,
                    YarcParser.ID,
                    YarcParser.SETTING_ID,
                    YarcParser.STRING,
                    YarcParser.INTEGER,
                    YarcParser.FLOAT_NUMBER,
                ]:
                    self.state = 192
                    self.aug_expr_stmt()
                    pass
                elif token in [YarcParser.EDIT]:
                    self.state = 193
                    self.edit_stmt()
                    pass
                elif token in [YarcParser.EVERY]:
                    self.state = 194
                    self.behavior_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.CREATE)
                                | (1 << YarcParser.GROUP)
                                | (1 << YarcParser.INSTANTIATE)
                                | (1 << YarcParser.GET)
                                | (1 << YarcParser.EDIT)
                                | (1 << YarcParser.FETCH)
                                | (1 << YarcParser.EVERY)
                                | (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 73) & ~0x3F) == 0
                        and (
                            (1 << (_la - 73))
                            & (
                                (1 << (YarcParser.BIT_NOT - 73))
                                | (1 << (YarcParser.PLUS - 73))
                                | (1 << (YarcParser.MINUS - 73))
                                | (1 << (YarcParser.LPAREN - 73))
                                | (1 << (YarcParser.LBRACK - 73))
                                | (1 << (YarcParser.LBRACE - 73))
                                | (1 << (YarcParser.LT - 73))
                                | (1 << (YarcParser.ID - 73))
                                | (1 << (YarcParser.SETTING_ID - 73))
                                | (1 << (YarcParser.STRING - 73))
                                | (1 << (YarcParser.INTEGER - 73))
                                | (1 << (YarcParser.FLOAT_NUMBER - 73))
                            )
                        )
                        != 0
                    )
                ):
                    break

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

        def option(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.OptionContext)
            else:
                return self.getTypedRuleContext(YarcParser.OptionContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_writer

    def writer(self):
        localctx = YarcParser.WriterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_writer)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(YarcParser.ID)
            self.state = 200
            self.match(YarcParser.COLON)
            self.state = 201
            self.match(YarcParser.NEWLINE)
            self.state = 202
            self.match(YarcParser.INDENT)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 203
                self.option()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.ID):
                    break

            self.state = 208
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Open_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(YarcParser.OPEN, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_open_stmt

    def open_stmt(self):
        localctx = YarcParser.Open_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_open_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(YarcParser.OPEN)
            self.state = 211
            self.test()
            self.state = 212
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Edit_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EDIT(self):
            return self.getToken(YarcParser.EDIT, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def TIMELINE(self):
            return self.getToken(YarcParser.TIMELINE, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_edit_stmt

    def edit_stmt(self):
        localctx = YarcParser.Edit_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_edit_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(YarcParser.EDIT)
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.TIMELINE]:
                self.state = 215
                self.match(YarcParser.TIMELINE)
                pass
            elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.state = 216
                self.name()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 219
            self.edit_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Create_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(YarcParser.CREATE, 0)

        def MATERIAL(self):
            return self.getToken(YarcParser.MATERIAL, 0)

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def CAMERA(self):
            return self.getToken(YarcParser.CAMERA, 0)

        def SHAPES(self):
            return self.getToken(YarcParser.SHAPES, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def LIGHT(self):
            return self.getToken(YarcParser.LIGHT, 0)

        def FROM(self):
            return self.getToken(YarcParser.FROM, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def simple_block(self):
            return self.getTypedRuleContext(YarcParser.Simple_blockContext, 0)

        def STEREO(self):
            return self.getToken(YarcParser.STEREO, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_create_expr

    def create_expr(self):
        localctx = YarcParser.Create_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_create_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(YarcParser.CREATE)
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 13, self._ctx)
            if la_ == 1:
                self.state = 222
                self.test()

            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.SHAPES,
                YarcParser.CAMERA,
                YarcParser.STEREO,
                YarcParser.FROM,
                YarcParser.UNDERSCORE,
                YarcParser.ID,
            ]:
                self.state = 235
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.CAMERA, YarcParser.STEREO]:
                    self.state = 226
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.STEREO:
                        self.state = 225
                        self.match(YarcParser.STEREO)

                    self.state = 228
                    self.match(YarcParser.CAMERA)
                    pass
                elif token in [YarcParser.SHAPES]:
                    self.state = 229
                    self.match(YarcParser.SHAPES)
                    pass
                elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                    self.state = 230
                    self.name()
                    self.state = 231
                    self.match(YarcParser.LIGHT)
                    pass
                elif token in [YarcParser.FROM]:
                    self.state = 233
                    self.match(YarcParser.FROM)
                    self.state = 234
                    self.test()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 239
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.COLON]:
                    self.state = 237
                    self.edit_block()
                    pass
                elif token in [YarcParser.NEWLINE]:
                    self.state = 238
                    self.match(YarcParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [YarcParser.MATERIAL]:
                self.state = 241
                self.match(YarcParser.MATERIAL)

                self.state = 242
                self.simple_block()
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

    class Instantiate_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANTIATE(self):
            return self.getToken(YarcParser.INSTANTIATE, 0)

        def FROM(self):
            return self.getToken(YarcParser.FROM, 0)

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_instantiate_expr

    def instantiate_expr(self):
        localctx = YarcParser.Instantiate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instantiate_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(YarcParser.INSTANTIATE)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or (
                ((_la - 73) & ~0x3F) == 0
                and (
                    (1 << (_la - 73))
                    & (
                        (1 << (YarcParser.BIT_NOT - 73))
                        | (1 << (YarcParser.PLUS - 73))
                        | (1 << (YarcParser.MINUS - 73))
                        | (1 << (YarcParser.LPAREN - 73))
                        | (1 << (YarcParser.LBRACK - 73))
                        | (1 << (YarcParser.LBRACE - 73))
                        | (1 << (YarcParser.LT - 73))
                        | (1 << (YarcParser.ID - 73))
                        | (1 << (YarcParser.SETTING_ID - 73))
                        | (1 << (YarcParser.STRING - 73))
                        | (1 << (YarcParser.INTEGER - 73))
                        | (1 << (YarcParser.FLOAT_NUMBER - 73))
                    )
                )
                != 0
            ):
                self.state = 246
                self.test()

            self.state = 249
            self.match(YarcParser.FROM)
            self.state = 250
            self.test()
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 251
                self.edit_block()
                pass
            elif token in [YarcParser.NEWLINE]:
                self.state = 252
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

    class Group_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(YarcParser.GROUP, 0)

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def name(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.NameContext)
            else:
                return self.getTypedRuleContext(YarcParser.NameContext, i)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def edit_block(self):
            return self.getTypedRuleContext(YarcParser.Edit_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.COMMA)
            else:
                return self.getToken(YarcParser.COMMA, i)

        def getRuleIndex(self):
            return YarcParser.RULE_group_expr

    def group_expr(self):
        localctx = YarcParser.Group_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_group_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(YarcParser.GROUP)
            self.state = 256
            self.match(YarcParser.LBRACK)
            self.state = 257
            self.name()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 258
                self.match(YarcParser.COMMA)
                self.state = 259
                self.name()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 265
            self.match(YarcParser.RBRACK)
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 266
                self.edit_block()
                pass
            elif token in [YarcParser.NEWLINE]:
                self.state = 267
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

    class Get_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(YarcParser.GET, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def simple_block(self):
            return self.getTypedRuleContext(YarcParser.Simple_blockContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def AT(self):
            return self.getToken(YarcParser.AT, 0)

        def CAMERA(self):
            return self.getToken(YarcParser.CAMERA, 0)

        def LIGHT(self):
            return self.getToken(YarcParser.LIGHT, 0)

        def MATERIAL(self):
            return self.getToken(YarcParser.MATERIAL, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_get_expr

    def get_expr(self):
        localctx = YarcParser.Get_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_get_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(YarcParser.GET)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 23, self._ctx)
            if la_ == 1:
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.CAMERA]:
                    self.state = 271
                    self.match(YarcParser.CAMERA)
                    pass
                elif token in [YarcParser.LIGHT]:
                    self.state = 272
                    self.match(YarcParser.LIGHT)
                    pass
                elif token in [YarcParser.MATERIAL]:
                    self.state = 273
                    self.match(YarcParser.MATERIAL)
                    pass
                elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                    self.state = 274
                    self.name()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 277
                self.match(YarcParser.AT)

            self.state = 280
            self.test()
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 281
                self.simple_block()
                pass
            elif token in [YarcParser.NEWLINE]:
                self.state = 282
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

    class Edit_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def attr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.AttrContext)
            else:
                return self.getTypedRuleContext(YarcParser.AttrContext, i)

        def inner_behavior_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Inner_behavior_stmtContext)
            else:
                return self.getTypedRuleContext(
                    YarcParser.Inner_behavior_stmtContext, i
                )

        def getRuleIndex(self):
            return YarcParser.RULE_edit_block

    def edit_block(self):
        localctx = YarcParser.Edit_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_edit_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(YarcParser.COLON)
            self.state = 286
            self.match(YarcParser.NEWLINE)
            self.state = 287
            self.match(YarcParser.INDENT)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 290
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.TRANSLATE,
                    YarcParser.CAM_TRANSLATE,
                    YarcParser.ROTATE,
                    YarcParser.SCALE,
                    YarcParser.SEMANTICS,
                    YarcParser.VISIBLE,
                    YarcParser.SIZE,
                    YarcParser.LOOK_AT,
                    YarcParser.UP_AXIS,
                    YarcParser.SCATTER,
                    YarcParser.UNDERSCORE,
                    YarcParser.ID,
                ]:
                    self.state = 288
                    self.attr()
                    pass
                elif token in [YarcParser.EVERY]:
                    self.state = 289
                    self.inner_behavior_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.TRANSLATE)
                                | (1 << YarcParser.CAM_TRANSLATE)
                                | (1 << YarcParser.ROTATE)
                                | (1 << YarcParser.SCALE)
                                | (1 << YarcParser.SEMANTICS)
                                | (1 << YarcParser.VISIBLE)
                                | (1 << YarcParser.SIZE)
                                | (1 << YarcParser.LOOK_AT)
                                | (1 << YarcParser.UP_AXIS)
                                | (1 << YarcParser.SCATTER)
                                | (1 << YarcParser.EVERY)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or _la == YarcParser.ID
                ):
                    break

            self.state = 294
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def simple_attr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Simple_attrContext)
            else:
                return self.getTypedRuleContext(YarcParser.Simple_attrContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_block

    def simple_block(self):
        localctx = YarcParser.Simple_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_simple_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(YarcParser.COLON)
            self.state = 297
            self.match(YarcParser.NEWLINE)
            self.state = 298
            self.match(YarcParser.INDENT)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 299
                self.simple_attr()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == YarcParser.UNDERSCORE or _la == YarcParser.ID):
                    break

            self.state = 304
            self.match(YarcParser.DEDENT)
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

        def core_attr(self):
            return self.getTypedRuleContext(YarcParser.Core_attrContext, 0)

        def simple_attr(self):
            return self.getTypedRuleContext(YarcParser.Simple_attrContext, 0)

        def compound_attr(self):
            return self.getTypedRuleContext(YarcParser.Compound_attrContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_attr

    def attr(self):
        localctx = YarcParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attr)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.TRANSLATE,
                YarcParser.CAM_TRANSLATE,
                YarcParser.ROTATE,
                YarcParser.SCALE,
                YarcParser.SEMANTICS,
                YarcParser.VISIBLE,
                YarcParser.SIZE,
                YarcParser.LOOK_AT,
                YarcParser.UP_AXIS,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.core_attr()
                pass
            elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.simple_attr()
                pass
            elif token in [YarcParser.SCATTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.compound_attr()
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

    class Simple_attrContext(ParserRuleContext):
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

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_simple_attr

    def simple_attr(self):
        localctx = YarcParser.Simple_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_simple_attr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.name()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.COLON:
                self.state = 312
                self.match(YarcParser.COLON)
                self.state = 313
                self.name()

            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or (
                ((_la - 73) & ~0x3F) == 0
                and (
                    (1 << (_la - 73))
                    & (
                        (1 << (YarcParser.BIT_NOT - 73))
                        | (1 << (YarcParser.PLUS - 73))
                        | (1 << (YarcParser.MINUS - 73))
                        | (1 << (YarcParser.LPAREN - 73))
                        | (1 << (YarcParser.LBRACK - 73))
                        | (1 << (YarcParser.LBRACE - 73))
                        | (1 << (YarcParser.LT - 73))
                        | (1 << (YarcParser.ID - 73))
                        | (1 << (YarcParser.SETTING_ID - 73))
                        | (1 << (YarcParser.STRING - 73))
                        | (1 << (YarcParser.INTEGER - 73))
                        | (1 << (YarcParser.FLOAT_NUMBER - 73))
                    )
                )
                != 0
            ):
                self.state = 316
                self.test()

            self.state = 319
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compound_attrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCATTER(self):
            return self.getToken(YarcParser.SCATTER, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_compound_attr

    def compound_attr(self):
        localctx = YarcParser.Compound_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_compound_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(YarcParser.SCATTER)
            self.state = 322
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Core_attrContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def TRANSLATE(self):
            return self.getToken(YarcParser.TRANSLATE, 0)

        def TO(self):
            return self.getToken(YarcParser.TO, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def CAM_TRANSLATE(self):
            return self.getToken(YarcParser.CAM_TRANSLATE, 0)

        def ROTATE(self):
            return self.getToken(YarcParser.ROTATE, 0)

        def SCALE(self):
            return self.getToken(YarcParser.SCALE, 0)

        def LOOK_AT(self):
            return self.getToken(YarcParser.LOOK_AT, 0)

        def UP_AXIS(self):
            return self.getToken(YarcParser.UP_AXIS, 0)

        def SIZE(self):
            return self.getToken(YarcParser.SIZE, 0)

        def SEMANTICS(self):
            return self.getToken(YarcParser.SEMANTICS, 0)

        def VISIBLE(self):
            return self.getToken(YarcParser.VISIBLE, 0)

        def AXIS(self):
            return self.getToken(YarcParser.AXIS, 0)

        def ORDER(self):
            return self.getToken(YarcParser.ORDER, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_core_attr

    def core_attr(self):
        localctx = YarcParser.Core_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_core_attr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.TRANSLATE]:
                self.state = 324
                self.match(YarcParser.TRANSLATE)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.AXIS:
                    self.state = 325
                    self.match(YarcParser.AXIS)

                self.state = 328
                self.match(YarcParser.TO)
                self.state = 329
                self.test()
                pass
            elif token in [YarcParser.CAM_TRANSLATE]:
                self.state = 330
                self.match(YarcParser.CAM_TRANSLATE)
                self.state = 331
                self.match(YarcParser.TO)
                self.state = 332
                self.test()
                pass
            elif token in [YarcParser.ROTATE]:
                self.state = 333
                self.match(YarcParser.ROTATE)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.AXIS:
                    self.state = 334
                    self.match(YarcParser.AXIS)

                self.state = 337
                self.test()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.ORDER:
                    self.state = 338
                    self.match(YarcParser.ORDER)

                pass
            elif token in [YarcParser.SCALE]:
                self.state = 341
                self.match(YarcParser.SCALE)
                self.state = 342
                self.test()
                pass
            elif token in [YarcParser.LOOK_AT]:
                self.state = 343
                self.match(YarcParser.LOOK_AT)
                self.state = 344
                self.test()
                pass
            elif token in [YarcParser.UP_AXIS]:
                self.state = 345
                self.match(YarcParser.UP_AXIS)
                self.state = 346
                self.test()
                pass
            elif token in [YarcParser.SIZE]:
                self.state = 347
                self.match(YarcParser.SIZE)
                self.state = 348
                self.test()
                pass
            elif token in [YarcParser.SEMANTICS]:
                self.state = 349
                self.match(YarcParser.SEMANTICS)
                self.state = 350
                self.test()
                pass
            elif token in [YarcParser.VISIBLE]:
                self.state = 351
                self.match(YarcParser.VISIBLE)
                self.state = 352
                self.test()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 355
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_behavior_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def behavior_expr(self):
            return self.getTypedRuleContext(YarcParser.Behavior_exprContext, 0)

        def inner_behavior_block(self):
            return self.getTypedRuleContext(YarcParser.Inner_behavior_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_inner_behavior_stmt

    def inner_behavior_stmt(self):
        localctx = YarcParser.Inner_behavior_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_inner_behavior_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.behavior_expr()
            self.state = 358
            self.inner_behavior_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_behavior_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def attr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.AttrContext)
            else:
                return self.getTypedRuleContext(YarcParser.AttrContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_inner_behavior_block

    def inner_behavior_block(self):
        localctx = YarcParser.Inner_behavior_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_inner_behavior_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(YarcParser.COLON)
            self.state = 361
            self.match(YarcParser.NEWLINE)
            self.state = 362
            self.match(YarcParser.INDENT)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 363
                self.attr()
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.TRANSLATE)
                                | (1 << YarcParser.CAM_TRANSLATE)
                                | (1 << YarcParser.ROTATE)
                                | (1 << YarcParser.SCALE)
                                | (1 << YarcParser.SEMANTICS)
                                | (1 << YarcParser.VISIBLE)
                                | (1 << YarcParser.SIZE)
                                | (1 << YarcParser.LOOK_AT)
                                | (1 << YarcParser.UP_AXIS)
                                | (1 << YarcParser.SCATTER)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or _la == YarcParser.ID
                ):
                    break

            self.state = 368
            self.match(YarcParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Behavior_stmtContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def behavior_expr(self):
            return self.getTypedRuleContext(YarcParser.Behavior_exprContext, 0)

        def behavior_block(self):
            return self.getTypedRuleContext(YarcParser.Behavior_blockContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_stmt

    def behavior_stmt(self):
        localctx = YarcParser.Behavior_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_behavior_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.behavior_expr()
            self.state = 371
            self.behavior_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Behavior_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVERY(self):
            return self.getToken(YarcParser.EVERY, 0)

        def FRAMES(self):
            return self.getToken(YarcParser.FRAMES, 0)

        def TIME(self):
            return self.getToken(YarcParser.TIME, 0)

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_expr

    def behavior_expr(self):
        localctx = YarcParser.Behavior_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_behavior_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(YarcParser.EVERY)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or (
                ((_la - 73) & ~0x3F) == 0
                and (
                    (1 << (_la - 73))
                    & (
                        (1 << (YarcParser.BIT_NOT - 73))
                        | (1 << (YarcParser.PLUS - 73))
                        | (1 << (YarcParser.MINUS - 73))
                        | (1 << (YarcParser.LPAREN - 73))
                        | (1 << (YarcParser.LBRACK - 73))
                        | (1 << (YarcParser.LBRACE - 73))
                        | (1 << (YarcParser.LT - 73))
                        | (1 << (YarcParser.ID - 73))
                        | (1 << (YarcParser.SETTING_ID - 73))
                        | (1 << (YarcParser.STRING - 73))
                        | (1 << (YarcParser.INTEGER - 73))
                        | (1 << (YarcParser.FLOAT_NUMBER - 73))
                    )
                )
                != 0
            ):
                self.state = 374
                self.test()

            self.state = 377
            _la = self._input.LA(1)
            if not (_la == YarcParser.FRAMES or _la == YarcParser.TIME):
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

    class Behavior_blockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YarcParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(YarcParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(YarcParser.DEDENT, 0)

        def aug_expr_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Aug_expr_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Aug_expr_stmtContext, i)

        def edit_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.Edit_stmtContext)
            else:
                return self.getTypedRuleContext(YarcParser.Edit_stmtContext, i)

        def getRuleIndex(self):
            return YarcParser.RULE_behavior_block

    def behavior_block(self):
        localctx = YarcParser.Behavior_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_behavior_block)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(YarcParser.COLON)
            self.state = 380
            self.match(YarcParser.NEWLINE)
            self.state = 381
            self.match(YarcParser.INDENT)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 384
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.CREATE,
                    YarcParser.GROUP,
                    YarcParser.INSTANTIATE,
                    YarcParser.GET,
                    YarcParser.FETCH,
                    YarcParser.UNIFORM,
                    YarcParser.NORMAL,
                    YarcParser.CHOICE,
                    YarcParser.SEQUENCE,
                    YarcParser.LOG_UNIFORM,
                    YarcParser.FALSE,
                    YarcParser.NONE,
                    YarcParser.NOT,
                    YarcParser.TRUE,
                    YarcParser.UNDERSCORE,
                    YarcParser.BIT_NOT,
                    YarcParser.PLUS,
                    YarcParser.MINUS,
                    YarcParser.LPAREN,
                    YarcParser.LBRACK,
                    YarcParser.LBRACE,
                    YarcParser.LT,
                    YarcParser.ID,
                    YarcParser.SETTING_ID,
                    YarcParser.STRING,
                    YarcParser.INTEGER,
                    YarcParser.FLOAT_NUMBER,
                ]:
                    self.state = 382
                    self.aug_expr_stmt()
                    pass
                elif token in [YarcParser.EDIT]:
                    self.state = 383
                    self.edit_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.CREATE)
                                | (1 << YarcParser.GROUP)
                                | (1 << YarcParser.INSTANTIATE)
                                | (1 << YarcParser.GET)
                                | (1 << YarcParser.EDIT)
                                | (1 << YarcParser.FETCH)
                                | (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    )
                    or (
                        ((_la - 73) & ~0x3F) == 0
                        and (
                            (1 << (_la - 73))
                            & (
                                (1 << (YarcParser.BIT_NOT - 73))
                                | (1 << (YarcParser.PLUS - 73))
                                | (1 << (YarcParser.MINUS - 73))
                                | (1 << (YarcParser.LPAREN - 73))
                                | (1 << (YarcParser.LBRACK - 73))
                                | (1 << (YarcParser.LBRACE - 73))
                                | (1 << (YarcParser.LT - 73))
                                | (1 << (YarcParser.ID - 73))
                                | (1 << (YarcParser.SETTING_ID - 73))
                                | (1 << (YarcParser.STRING - 73))
                                | (1 << (YarcParser.INTEGER - 73))
                                | (1 << (YarcParser.FLOAT_NUMBER - 73))
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 388
            self.match(YarcParser.DEDENT)
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

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def testlist(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestlistContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestlistContext, i)

        def fetch_expr(self):
            return self.getTypedRuleContext(YarcParser.Fetch_exprContext, 0)

        def aug_assign(self):
            return self.getTypedRuleContext(YarcParser.Aug_assignContext, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_expr_stmt

    def expr_stmt(self):
        localctx = YarcParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.state = 390
                self.testlist()
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la - 69) & ~0x3F) == 0 and (
                    (1 << (_la - 69))
                    & (
                        (1 << (YarcParser.ASSIGN - 69))
                        | (1 << (YarcParser.ADD_ASSIGN - 69))
                        | (1 << (YarcParser.SUB_ASSIGN - 69))
                        | (1 << (YarcParser.MULT_ASSIGN - 69))
                        | (1 << (YarcParser.DIV_ASSIGN - 69))
                        | (1 << (YarcParser.MOD_ASSIGN - 69))
                        | (1 << (YarcParser.AND_ASSIGN - 69))
                        | (1 << (YarcParser.OR_ASSIGN - 69))
                        | (1 << (YarcParser.XOR_ASSIGN - 69))
                        | (1 << (YarcParser.LSHIFT_ASSIGN - 69))
                        | (1 << (YarcParser.RSHIFT_ASSIGN - 69))
                        | (1 << (YarcParser.POWER_ASSIGN - 69))
                        | (1 << (YarcParser.IDIV_ASSIGN - 69))
                    )
                ) != 0:
                    self.state = 393
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
                        self.state = 391
                        self.aug_assign()
                        pass
                    elif token in [YarcParser.ASSIGN]:
                        self.state = 392
                        self.match(YarcParser.ASSIGN)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 397
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [
                        YarcParser.UNIFORM,
                        YarcParser.NORMAL,
                        YarcParser.CHOICE,
                        YarcParser.SEQUENCE,
                        YarcParser.LOG_UNIFORM,
                        YarcParser.FALSE,
                        YarcParser.NONE,
                        YarcParser.NOT,
                        YarcParser.TRUE,
                        YarcParser.UNDERSCORE,
                        YarcParser.BIT_NOT,
                        YarcParser.PLUS,
                        YarcParser.MINUS,
                        YarcParser.LPAREN,
                        YarcParser.LBRACK,
                        YarcParser.LBRACE,
                        YarcParser.LT,
                        YarcParser.ID,
                        YarcParser.SETTING_ID,
                        YarcParser.STRING,
                        YarcParser.INTEGER,
                        YarcParser.FLOAT_NUMBER,
                    ]:
                        self.state = 395
                        self.testlist()
                        pass
                    elif token in [YarcParser.FETCH]:
                        self.state = 396
                        self.fetch_expr()
                        pass
                    else:
                        raise NoViableAltException(self)

                pass
            elif token in [YarcParser.FETCH]:
                self.state = 401
                self.fetch_expr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 404
            self.match(YarcParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Aug_expr_stmtContext(ParserRuleContext):
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

        def fetch_expr(self):
            return self.getTypedRuleContext(YarcParser.Fetch_exprContext, 0)

        def NEWLINE(self):
            return self.getToken(YarcParser.NEWLINE, 0)

        def aug_assign(self):
            return self.getTypedRuleContext(YarcParser.Aug_assignContext, 0)

        def ASSIGN(self):
            return self.getToken(YarcParser.ASSIGN, 0)

        def create_expr(self):
            return self.getTypedRuleContext(YarcParser.Create_exprContext, 0)

        def instantiate_expr(self):
            return self.getTypedRuleContext(YarcParser.Instantiate_exprContext, 0)

        def get_expr(self):
            return self.getTypedRuleContext(YarcParser.Get_exprContext, 0)

        def group_expr(self):
            return self.getTypedRuleContext(YarcParser.Group_exprContext, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_aug_expr_stmt

    def aug_expr_stmt(self):
        localctx = YarcParser.Aug_expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_aug_expr_stmt)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.FETCH,
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [
                    YarcParser.UNIFORM,
                    YarcParser.NORMAL,
                    YarcParser.CHOICE,
                    YarcParser.SEQUENCE,
                    YarcParser.LOG_UNIFORM,
                    YarcParser.FALSE,
                    YarcParser.NONE,
                    YarcParser.NOT,
                    YarcParser.TRUE,
                    YarcParser.UNDERSCORE,
                    YarcParser.BIT_NOT,
                    YarcParser.PLUS,
                    YarcParser.MINUS,
                    YarcParser.LPAREN,
                    YarcParser.LBRACK,
                    YarcParser.LBRACE,
                    YarcParser.LT,
                    YarcParser.ID,
                    YarcParser.SETTING_ID,
                    YarcParser.STRING,
                    YarcParser.INTEGER,
                    YarcParser.FLOAT_NUMBER,
                ]:
                    self.state = 406
                    self.testlist()
                    self.state = 428
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [YarcParser.NEWLINE]:
                        self.state = 407
                        self.match(YarcParser.NEWLINE)
                        pass
                    elif token in [
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
                        self.state = 408
                        self.aug_assign()
                        self.state = 411
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [
                            YarcParser.UNIFORM,
                            YarcParser.NORMAL,
                            YarcParser.CHOICE,
                            YarcParser.SEQUENCE,
                            YarcParser.LOG_UNIFORM,
                            YarcParser.FALSE,
                            YarcParser.NONE,
                            YarcParser.NOT,
                            YarcParser.TRUE,
                            YarcParser.UNDERSCORE,
                            YarcParser.BIT_NOT,
                            YarcParser.PLUS,
                            YarcParser.MINUS,
                            YarcParser.LPAREN,
                            YarcParser.LBRACK,
                            YarcParser.LBRACE,
                            YarcParser.LT,
                            YarcParser.ID,
                            YarcParser.SETTING_ID,
                            YarcParser.STRING,
                            YarcParser.INTEGER,
                            YarcParser.FLOAT_NUMBER,
                        ]:
                            self.state = 409
                            self.testlist()
                            pass
                        elif token in [YarcParser.FETCH]:
                            self.state = 410
                            self.fetch_expr()
                            pass
                        elif token in [YarcParser.NEWLINE]:
                            pass
                        else:
                            pass
                        self.state = 413
                        self.match(YarcParser.NEWLINE)
                        pass
                    elif token in [YarcParser.ASSIGN]:
                        self.state = 415
                        self.match(YarcParser.ASSIGN)
                        self.state = 426
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [
                            YarcParser.FETCH,
                            YarcParser.UNIFORM,
                            YarcParser.NORMAL,
                            YarcParser.CHOICE,
                            YarcParser.SEQUENCE,
                            YarcParser.LOG_UNIFORM,
                            YarcParser.FALSE,
                            YarcParser.NONE,
                            YarcParser.NOT,
                            YarcParser.TRUE,
                            YarcParser.UNDERSCORE,
                            YarcParser.BIT_NOT,
                            YarcParser.PLUS,
                            YarcParser.MINUS,
                            YarcParser.LPAREN,
                            YarcParser.LBRACK,
                            YarcParser.LBRACE,
                            YarcParser.LT,
                            YarcParser.ID,
                            YarcParser.SETTING_ID,
                            YarcParser.STRING,
                            YarcParser.INTEGER,
                            YarcParser.FLOAT_NUMBER,
                        ]:
                            self.state = 418
                            self._errHandler.sync(self)
                            token = self._input.LA(1)
                            if token in [
                                YarcParser.UNIFORM,
                                YarcParser.NORMAL,
                                YarcParser.CHOICE,
                                YarcParser.SEQUENCE,
                                YarcParser.LOG_UNIFORM,
                                YarcParser.FALSE,
                                YarcParser.NONE,
                                YarcParser.NOT,
                                YarcParser.TRUE,
                                YarcParser.UNDERSCORE,
                                YarcParser.BIT_NOT,
                                YarcParser.PLUS,
                                YarcParser.MINUS,
                                YarcParser.LPAREN,
                                YarcParser.LBRACK,
                                YarcParser.LBRACE,
                                YarcParser.LT,
                                YarcParser.ID,
                                YarcParser.SETTING_ID,
                                YarcParser.STRING,
                                YarcParser.INTEGER,
                                YarcParser.FLOAT_NUMBER,
                            ]:
                                self.state = 416
                                self.testlist()
                                pass
                            elif token in [YarcParser.FETCH]:
                                self.state = 417
                                self.fetch_expr()
                                pass
                            else:
                                raise NoViableAltException(self)

                            self.state = 420
                            self.match(YarcParser.NEWLINE)
                            pass
                        elif token in [YarcParser.CREATE]:
                            self.state = 422
                            self.create_expr()
                            pass
                        elif token in [YarcParser.INSTANTIATE]:
                            self.state = 423
                            self.instantiate_expr()
                            pass
                        elif token in [YarcParser.GET]:
                            self.state = 424
                            self.get_expr()
                            pass
                        elif token in [YarcParser.GROUP]:
                            self.state = 425
                            self.group_expr()
                            pass
                        else:
                            raise NoViableAltException(self)

                        pass
                    else:
                        raise NoViableAltException(self)

                    pass
                elif token in [YarcParser.FETCH]:
                    self.state = 430
                    self.fetch_expr()
                    self.state = 431
                    self.match(YarcParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [YarcParser.CREATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.create_expr()
                pass
            elif token in [YarcParser.INSTANTIATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.instantiate_expr()
                pass
            elif token in [YarcParser.GET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 437
                self.get_expr()
                pass
            elif token in [YarcParser.GROUP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 438
                self.group_expr()
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

    class Fetch_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FETCH(self):
            return self.getToken(YarcParser.FETCH, 0)

        def test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(YarcParser.TestContext)
            else:
                return self.getTypedRuleContext(YarcParser.TestContext, i)

        def FROM(self):
            return self.getToken(YarcParser.FROM, 0)

        def MATCH(self):
            return self.getToken(YarcParser.MATCH, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_fetch_expr

    def fetch_expr(self):
        localctx = YarcParser.Fetch_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_fetch_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(YarcParser.FETCH)
            self.state = 442
            self.test()
            self.state = 443
            self.match(YarcParser.FROM)
            self.state = 444
            self.test()
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.MATCH:
                self.state = 445
                self.match(YarcParser.MATCH)
                self.state = 446
                self.test()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Aug_assignContext(ParserRuleContext):
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
            return YarcParser.RULE_aug_assign

    def aug_assign(self):
        localctx = YarcParser.Aug_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_aug_assign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            _la = self._input.LA(1)
            if not (
                ((_la - 95) & ~0x3F) == 0
                and (
                    (1 << (_la - 95))
                    & (
                        (1 << (YarcParser.ADD_ASSIGN - 95))
                        | (1 << (YarcParser.SUB_ASSIGN - 95))
                        | (1 << (YarcParser.MULT_ASSIGN - 95))
                        | (1 << (YarcParser.DIV_ASSIGN - 95))
                        | (1 << (YarcParser.MOD_ASSIGN - 95))
                        | (1 << (YarcParser.AND_ASSIGN - 95))
                        | (1 << (YarcParser.OR_ASSIGN - 95))
                        | (1 << (YarcParser.XOR_ASSIGN - 95))
                        | (1 << (YarcParser.LSHIFT_ASSIGN - 95))
                        | (1 << (YarcParser.RSHIFT_ASSIGN - 95))
                        | (1 << (YarcParser.POWER_ASSIGN - 95))
                        | (1 << (YarcParser.IDIV_ASSIGN - 95))
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
        self.enterRule(localctx, 58, self.RULE_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.or_test()
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.IF:
                self.state = 452
                self.match(YarcParser.IF)
                self.state = 453
                self.or_test()
                self.state = 454
                self.match(YarcParser.ELSE)
                self.state = 455
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
        self.enterRule(localctx, 60, self.RULE_test_nocond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
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
        self.enterRule(localctx, 62, self.RULE_or_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.and_test()
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.OR:
                self.state = 462
                self.match(YarcParser.OR)
                self.state = 463
                self.and_test()
                self.state = 468
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
        self.enterRule(localctx, 64, self.RULE_and_test)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.not_test()
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.AND:
                self.state = 470
                self.match(YarcParser.AND)
                self.state = 471
                self.not_test()
                self.state = 476
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
        self.enterRule(localctx, 66, self.RULE_not_test)
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(YarcParser.NOT)
                self.state = 478
                self.not_test()
                pass
            elif token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
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
        self.enterRule(localctx, 68, self.RULE_comparison)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.expr()
            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la - 55) & ~0x3F) == 0 and (
                (1 << (_la - 55))
                & (
                    (1 << (YarcParser.IN - 55))
                    | (1 << (YarcParser.IS - 55))
                    | (1 << (YarcParser.NOT - 55))
                    | (1 << (YarcParser.LT - 55))
                    | (1 << (YarcParser.GT - 55))
                    | (1 << (YarcParser.EQUALS - 55))
                    | (1 << (YarcParser.GT_EQ - 55))
                    | (1 << (YarcParser.LT_EQ - 55))
                    | (1 << (YarcParser.NOT_EQ - 55))
                )
            ) != 0:
                self.state = 483
                self.comp_op()
                self.state = 484
                self.expr()
                self.state = 490
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def LT(self):
            return self.getToken(YarcParser.LT, 0)

        def GT(self):
            return self.getToken(YarcParser.GT, 0)

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
        self.enterRule(localctx, 70, self.RULE_comp_op)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 55, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.match(YarcParser.LT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.match(YarcParser.GT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 493
                self.match(YarcParser.EQUALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 494
                self.match(YarcParser.GT_EQ)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 495
                self.match(YarcParser.LT_EQ)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 496
                self.match(YarcParser.NOT_EQ)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 497
                self.match(YarcParser.IN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 498
                self.match(YarcParser.NOT)
                self.state = 499
                self.match(YarcParser.IN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 500
                self.match(YarcParser.IS)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 501
                self.match(YarcParser.IS)
                self.state = 502
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
        self.enterRule(localctx, 72, self.RULE_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.xor_expr()
            self.state = 510
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_OR:
                self.state = 506
                self.match(YarcParser.BIT_OR)
                self.state = 507
                self.xor_expr()
                self.state = 512
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
        self.enterRule(localctx, 74, self.RULE_xor_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.and_expr()
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.XOR:
                self.state = 514
                self.match(YarcParser.XOR)
                self.state = 515
                self.and_expr()
                self.state = 520
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
        self.enterRule(localctx, 76, self.RULE_and_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.shift_expr()
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.BIT_AND:
                self.state = 522
                self.match(YarcParser.BIT_AND)
                self.state = 523
                self.shift_expr()
                self.state = 528
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
        self.enterRule(localctx, 78, self.RULE_shift_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.arith_expr()
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT:
                self.state = 530
                _la = self._input.LA(1)
                if not (_la == YarcParser.LSHIFT or _la == YarcParser.RSHIFT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 531
                self.arith_expr()
                self.state = 536
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

        def PLUS(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.PLUS)
            else:
                return self.getToken(YarcParser.PLUS, i)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.MINUS)
            else:
                return self.getToken(YarcParser.MINUS, i)

        def getRuleIndex(self):
            return YarcParser.RULE_arith_expr

    def arith_expr(self):
        localctx = YarcParser.Arith_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arith_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.term()
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.PLUS or _la == YarcParser.MINUS:
                self.state = 538
                _la = self._input.LA(1)
                if not (_la == YarcParser.PLUS or _la == YarcParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 539
                self.term()
                self.state = 544
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

        def MUL(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.MUL)
            else:
                return self.getToken(YarcParser.MUL, i)

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
        self.enterRule(localctx, 82, self.RULE_term)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.factor()
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la - 78) & ~0x3F) == 0 and (
                (1 << (_la - 78))
                & (
                    (1 << (YarcParser.DIV - 78))
                    | (1 << (YarcParser.MUL - 78))
                    | (1 << (YarcParser.MOD - 78))
                    | (1 << (YarcParser.IDIV - 78))
                )
            ) != 0:
                self.state = 546
                _la = self._input.LA(1)
                if not (
                    ((_la - 78) & ~0x3F) == 0
                    and (
                        (1 << (_la - 78))
                        & (
                            (1 << (YarcParser.DIV - 78))
                            | (1 << (YarcParser.MUL - 78))
                            | (1 << (YarcParser.MOD - 78))
                            | (1 << (YarcParser.IDIV - 78))
                        )
                    )
                    != 0
                ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 547
                self.factor()
                self.state = 552
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

        def PLUS(self):
            return self.getToken(YarcParser.PLUS, 0)

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
        self.enterRule(localctx, 84, self.RULE_factor)
        self._la = 0  # Token type
        try:
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.BIT_NOT, YarcParser.PLUS, YarcParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                _la = self._input.LA(1)
                if not (
                    ((_la - 73) & ~0x3F) == 0
                    and (
                        (1 << (_la - 73))
                        & (
                            (1 << (YarcParser.BIT_NOT - 73))
                            | (1 << (YarcParser.PLUS - 73))
                            | (1 << (YarcParser.MINUS - 73))
                        )
                    )
                    != 0
                ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 554
                self.factor()
                pass
            elif token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.power()
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
        self.enterRule(localctx, 86, self.RULE_power)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.atom_expr()
            self.state = 561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.POWER:
                self.state = 559
                self.match(YarcParser.POWER)
                self.state = 560
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
        self.enterRule(localctx, 88, self.RULE_atom_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.atom()
            self.state = 567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.DOT or _la == YarcParser.LBRACK:
                self.state = 564
                self.trailer()
                self.state = 569
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

        def test(self):
            return self.getTypedRuleContext(YarcParser.TestContext, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def LBRACK(self):
            return self.getToken(YarcParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(YarcParser.RBRACK, 0)

        def RANGE(self):
            return self.getToken(YarcParser.RANGE, 0)

        def INTEGER(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.INTEGER)
            else:
                return self.getToken(YarcParser.INTEGER, i)

        def testlist_comp(self):
            return self.getTypedRuleContext(YarcParser.Testlist_compContext, 0)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(YarcParser.MINUS)
            else:
                return self.getToken(YarcParser.MINUS, i)

        def LT(self):
            return self.getToken(YarcParser.LT, 0)

        def GT(self):
            return self.getToken(YarcParser.GT, 0)

        def vector_comp(self):
            return self.getTypedRuleContext(YarcParser.Vector_compContext, 0)

        def LBRACE(self):
            return self.getToken(YarcParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(YarcParser.RBRACE, 0)

        def dict_or_set_maker(self):
            return self.getTypedRuleContext(YarcParser.Dict_or_set_makerContext, 0)

        def name(self):
            return self.getTypedRuleContext(YarcParser.NameContext, 0)

        def SETTING_ID(self):
            return self.getToken(YarcParser.SETTING_ID, 0)

        def distribution_expr(self):
            return self.getTypedRuleContext(YarcParser.Distribution_exprContext, 0)

        def FLOAT_NUMBER(self):
            return self.getToken(YarcParser.FLOAT_NUMBER, 0)

        def STRING(self):
            return self.getToken(YarcParser.STRING, 0)

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
        self.enterRule(localctx, 90, self.RULE_atom)
        self._la = 0  # Token type
        try:
            self.state = 610
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.match(YarcParser.LPAREN)
                self.state = 571
                self.test()
                self.state = 572
                self.match(YarcParser.RPAREN)
                pass
            elif token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 574
                self.match(YarcParser.LBRACK)
                self.state = 588
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 68, self._ctx)
                if la_ == 1:
                    self.state = 576
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    ) or (
                        ((_la - 73) & ~0x3F) == 0
                        and (
                            (1 << (_la - 73))
                            & (
                                (1 << (YarcParser.BIT_NOT - 73))
                                | (1 << (YarcParser.PLUS - 73))
                                | (1 << (YarcParser.MINUS - 73))
                                | (1 << (YarcParser.LPAREN - 73))
                                | (1 << (YarcParser.LBRACK - 73))
                                | (1 << (YarcParser.LBRACE - 73))
                                | (1 << (YarcParser.LT - 73))
                                | (1 << (YarcParser.ID - 73))
                                | (1 << (YarcParser.SETTING_ID - 73))
                                | (1 << (YarcParser.STRING - 73))
                                | (1 << (YarcParser.INTEGER - 73))
                                | (1 << (YarcParser.FLOAT_NUMBER - 73))
                            )
                        )
                        != 0
                    ):
                        self.state = 575
                        self.testlist_comp()

                    pass

                elif la_ == 2:
                    self.state = 579
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.MINUS:
                        self.state = 578
                        self.match(YarcParser.MINUS)

                    self.state = 581
                    self.match(YarcParser.INTEGER)
                    self.state = 583
                    self.match(YarcParser.RANGE)

                    self.state = 585
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.MINUS:
                        self.state = 584
                        self.match(YarcParser.MINUS)

                    self.state = 587
                    self.match(YarcParser.INTEGER)
                    pass

                self.state = 590
                self.match(YarcParser.RBRACK)
                pass
            elif token in [YarcParser.LT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 591
                self.match(YarcParser.LT)
                self.state = 593
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.UNIFORM)
                            | (1 << YarcParser.NORMAL)
                            | (1 << YarcParser.CHOICE)
                            | (1 << YarcParser.SEQUENCE)
                            | (1 << YarcParser.LOG_UNIFORM)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 73) & ~0x3F) == 0
                    and (
                        (1 << (_la - 73))
                        & (
                            (1 << (YarcParser.BIT_NOT - 73))
                            | (1 << (YarcParser.PLUS - 73))
                            | (1 << (YarcParser.MINUS - 73))
                            | (1 << (YarcParser.LPAREN - 73))
                            | (1 << (YarcParser.LBRACK - 73))
                            | (1 << (YarcParser.LBRACE - 73))
                            | (1 << (YarcParser.LT - 73))
                            | (1 << (YarcParser.ID - 73))
                            | (1 << (YarcParser.SETTING_ID - 73))
                            | (1 << (YarcParser.STRING - 73))
                            | (1 << (YarcParser.INTEGER - 73))
                            | (1 << (YarcParser.FLOAT_NUMBER - 73))
                        )
                    )
                    != 0
                ):
                    self.state = 592
                    self.vector_comp()

                self.state = 595
                self.match(YarcParser.GT)
                pass
            elif token in [YarcParser.LBRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 596
                self.match(YarcParser.LBRACE)
                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.UNIFORM)
                            | (1 << YarcParser.NORMAL)
                            | (1 << YarcParser.CHOICE)
                            | (1 << YarcParser.SEQUENCE)
                            | (1 << YarcParser.LOG_UNIFORM)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 73) & ~0x3F) == 0
                    and (
                        (1 << (_la - 73))
                        & (
                            (1 << (YarcParser.BIT_NOT - 73))
                            | (1 << (YarcParser.PLUS - 73))
                            | (1 << (YarcParser.MINUS - 73))
                            | (1 << (YarcParser.LPAREN - 73))
                            | (1 << (YarcParser.LBRACK - 73))
                            | (1 << (YarcParser.LBRACE - 73))
                            | (1 << (YarcParser.LT - 73))
                            | (1 << (YarcParser.ID - 73))
                            | (1 << (YarcParser.SETTING_ID - 73))
                            | (1 << (YarcParser.STRING - 73))
                            | (1 << (YarcParser.INTEGER - 73))
                            | (1 << (YarcParser.FLOAT_NUMBER - 73))
                        )
                    )
                    != 0
                ):
                    self.state = 597
                    self.dict_or_set_maker()

                self.state = 600
                self.match(YarcParser.RBRACE)
                pass
            elif token in [YarcParser.UNDERSCORE, YarcParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 601
                self.name()
                pass
            elif token in [YarcParser.SETTING_ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 602
                self.match(YarcParser.SETTING_ID)
                pass
            elif token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
            ]:
                self.enterOuterAlt(localctx, 7)
                self.state = 603
                self.distribution_expr()
                pass
            elif token in [YarcParser.INTEGER]:
                self.enterOuterAlt(localctx, 8)
                self.state = 604
                self.match(YarcParser.INTEGER)
                pass
            elif token in [YarcParser.FLOAT_NUMBER]:
                self.enterOuterAlt(localctx, 9)
                self.state = 605
                self.match(YarcParser.FLOAT_NUMBER)
                pass
            elif token in [YarcParser.STRING]:
                self.enterOuterAlt(localctx, 10)
                self.state = 606
                self.match(YarcParser.STRING)
                pass
            elif token in [YarcParser.NONE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 607
                self.match(YarcParser.NONE)
                pass
            elif token in [YarcParser.TRUE]:
                self.enterOuterAlt(localctx, 12)
                self.state = 608
                self.match(YarcParser.TRUE)
                pass
            elif token in [YarcParser.FALSE]:
                self.enterOuterAlt(localctx, 13)
                self.state = 609
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
        self.enterRule(localctx, 92, self.RULE_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
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
        self.enterRule(localctx, 94, self.RULE_primitives)
        self._la = 0  # Token type
        try:
            self.state = 621
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.SHAPES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.match(YarcParser.SHAPES)
                pass
            elif token in [YarcParser.CAMERA, YarcParser.STEREO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.STEREO:
                    self.state = 615
                    self.match(YarcParser.STEREO)

                self.state = 618
                self.match(YarcParser.CAMERA)
                pass
            elif token in [YarcParser.LIGHT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 619
                self.match(YarcParser.LIGHT)
                pass
            elif token in [YarcParser.MATERIAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 620
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

    class Distribution_exprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distribution(self):
            return self.getTypedRuleContext(YarcParser.DistributionContext, 0)

        def LPAREN(self):
            return self.getToken(YarcParser.LPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(YarcParser.ArglistContext, 0)

        def RPAREN(self):
            return self.getToken(YarcParser.RPAREN, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_distribution_expr

    def distribution_expr(self):
        localctx = YarcParser.Distribution_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_distribution_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.distribution()
            self.state = 624
            self.match(YarcParser.LPAREN)
            self.state = 625
            self.arglist()
            self.state = 626
            self.match(YarcParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DistributionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIFORM(self):
            return self.getToken(YarcParser.UNIFORM, 0)

        def NORMAL(self):
            return self.getToken(YarcParser.NORMAL, 0)

        def CHOICE(self):
            return self.getToken(YarcParser.CHOICE, 0)

        def SEQUENCE(self):
            return self.getToken(YarcParser.SEQUENCE, 0)

        def LOG_UNIFORM(self):
            return self.getToken(YarcParser.LOG_UNIFORM, 0)

        def getRuleIndex(self):
            return YarcParser.RULE_distribution

    def distribution(self):
        localctx = YarcParser.DistributionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_distribution)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            _la = self._input.LA(1)
            if not (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
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
        self.enterRule(localctx, 100, self.RULE_testlist_comp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.test()
            self.state = 639
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.state = 631
                self.comp_for()
                pass
            elif token in [YarcParser.COMMA, YarcParser.RBRACK]:
                self.state = 636
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == YarcParser.COMMA:
                    self.state = 632
                    self.match(YarcParser.COMMA)
                    self.state = 633
                    self.test()
                    self.state = 638
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

    class Vector_compContext(ParserRuleContext):
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
            return YarcParser.RULE_vector_comp

    def vector_comp(self):
        localctx = YarcParser.Vector_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_vector_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.expr()
            self.state = 642
            self.match(YarcParser.COMMA)
            self.state = 643
            self.expr()
            self.state = 644
            self.match(YarcParser.COMMA)
            self.state = 645
            self.expr()
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
        self.enterRule(localctx, 104, self.RULE_trailer)
        try:
            self.state = 653
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                self.match(YarcParser.LBRACK)
                self.state = 648
                self.subscriptlist()
                self.state = 649
                self.match(YarcParser.RBRACK)
                pass
            elif token in [YarcParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 651
                self.match(YarcParser.DOT)
                self.state = 652
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
        self.enterRule(localctx, 106, self.RULE_arglist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655
            self.argument()
            self.state = 660
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 656
                self.match(YarcParser.COMMA)
                self.state = 657
                self.argument()
                self.state = 662
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 108, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 663
            self.test()
            self.state = 667
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.state = 664
                self.comp_for()
                pass
            elif token in [YarcParser.ASSIGN]:
                self.state = 665
                self.match(YarcParser.ASSIGN)
                self.state = 666
                self.test()
                pass
            elif token in [YarcParser.COMMA, YarcParser.RPAREN]:
                pass
            else:
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
        self.enterRule(localctx, 110, self.RULE_subscriptlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 669
            self.subscript_()
            self.state = 674
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 670
                self.match(YarcParser.COMMA)
                self.state = 671
                self.subscript_()
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
        self.enterRule(localctx, 112, self.RULE_subscript_)
        self._la = 0  # Token type
        try:
            self.state = 694
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                YarcParser.UNIFORM,
                YarcParser.NORMAL,
                YarcParser.CHOICE,
                YarcParser.SEQUENCE,
                YarcParser.LOG_UNIFORM,
                YarcParser.FALSE,
                YarcParser.NONE,
                YarcParser.NOT,
                YarcParser.TRUE,
                YarcParser.UNDERSCORE,
                YarcParser.BIT_NOT,
                YarcParser.PLUS,
                YarcParser.MINUS,
                YarcParser.LPAREN,
                YarcParser.LBRACK,
                YarcParser.LBRACE,
                YarcParser.LT,
                YarcParser.ID,
                YarcParser.SETTING_ID,
                YarcParser.STRING,
                YarcParser.INTEGER,
                YarcParser.FLOAT_NUMBER,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 677
                self.test()
                self.state = 685
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COLON:
                    self.state = 678
                    self.match(YarcParser.COLON)
                    self.state = 680
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << YarcParser.UNIFORM)
                                | (1 << YarcParser.NORMAL)
                                | (1 << YarcParser.CHOICE)
                                | (1 << YarcParser.SEQUENCE)
                                | (1 << YarcParser.LOG_UNIFORM)
                                | (1 << YarcParser.FALSE)
                                | (1 << YarcParser.NONE)
                                | (1 << YarcParser.NOT)
                                | (1 << YarcParser.TRUE)
                                | (1 << YarcParser.UNDERSCORE)
                            )
                        )
                        != 0
                    ) or (
                        ((_la - 73) & ~0x3F) == 0
                        and (
                            (1 << (_la - 73))
                            & (
                                (1 << (YarcParser.BIT_NOT - 73))
                                | (1 << (YarcParser.PLUS - 73))
                                | (1 << (YarcParser.MINUS - 73))
                                | (1 << (YarcParser.LPAREN - 73))
                                | (1 << (YarcParser.LBRACK - 73))
                                | (1 << (YarcParser.LBRACE - 73))
                                | (1 << (YarcParser.LT - 73))
                                | (1 << (YarcParser.ID - 73))
                                | (1 << (YarcParser.SETTING_ID - 73))
                                | (1 << (YarcParser.STRING - 73))
                                | (1 << (YarcParser.INTEGER - 73))
                                | (1 << (YarcParser.FLOAT_NUMBER - 73))
                            )
                        )
                        != 0
                    ):
                        self.state = 679
                        self.test()

                    self.state = 683
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == YarcParser.COLON:
                        self.state = 682
                        self.sliceop()

                pass
            elif token in [YarcParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 687
                self.match(YarcParser.COLON)
                self.state = 689
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (
                    ((_la) & ~0x3F) == 0
                    and (
                        (1 << _la)
                        & (
                            (1 << YarcParser.UNIFORM)
                            | (1 << YarcParser.NORMAL)
                            | (1 << YarcParser.CHOICE)
                            | (1 << YarcParser.SEQUENCE)
                            | (1 << YarcParser.LOG_UNIFORM)
                            | (1 << YarcParser.FALSE)
                            | (1 << YarcParser.NONE)
                            | (1 << YarcParser.NOT)
                            | (1 << YarcParser.TRUE)
                            | (1 << YarcParser.UNDERSCORE)
                        )
                    )
                    != 0
                ) or (
                    ((_la - 73) & ~0x3F) == 0
                    and (
                        (1 << (_la - 73))
                        & (
                            (1 << (YarcParser.BIT_NOT - 73))
                            | (1 << (YarcParser.PLUS - 73))
                            | (1 << (YarcParser.MINUS - 73))
                            | (1 << (YarcParser.LPAREN - 73))
                            | (1 << (YarcParser.LBRACK - 73))
                            | (1 << (YarcParser.LBRACE - 73))
                            | (1 << (YarcParser.LT - 73))
                            | (1 << (YarcParser.ID - 73))
                            | (1 << (YarcParser.SETTING_ID - 73))
                            | (1 << (YarcParser.STRING - 73))
                            | (1 << (YarcParser.INTEGER - 73))
                            | (1 << (YarcParser.FLOAT_NUMBER - 73))
                        )
                    )
                    != 0
                ):
                    self.state = 688
                    self.test()

                self.state = 692
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == YarcParser.COLON:
                    self.state = 691
                    self.sliceop()

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
        self.enterRule(localctx, 114, self.RULE_sliceop)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(YarcParser.COLON)
            self.state = 698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (
                ((_la) & ~0x3F) == 0
                and (
                    (1 << _la)
                    & (
                        (1 << YarcParser.UNIFORM)
                        | (1 << YarcParser.NORMAL)
                        | (1 << YarcParser.CHOICE)
                        | (1 << YarcParser.SEQUENCE)
                        | (1 << YarcParser.LOG_UNIFORM)
                        | (1 << YarcParser.FALSE)
                        | (1 << YarcParser.NONE)
                        | (1 << YarcParser.NOT)
                        | (1 << YarcParser.TRUE)
                        | (1 << YarcParser.UNDERSCORE)
                    )
                )
                != 0
            ) or (
                ((_la - 73) & ~0x3F) == 0
                and (
                    (1 << (_la - 73))
                    & (
                        (1 << (YarcParser.BIT_NOT - 73))
                        | (1 << (YarcParser.PLUS - 73))
                        | (1 << (YarcParser.MINUS - 73))
                        | (1 << (YarcParser.LPAREN - 73))
                        | (1 << (YarcParser.LBRACK - 73))
                        | (1 << (YarcParser.LBRACE - 73))
                        | (1 << (YarcParser.LT - 73))
                        | (1 << (YarcParser.ID - 73))
                        | (1 << (YarcParser.SETTING_ID - 73))
                        | (1 << (YarcParser.STRING - 73))
                        | (1 << (YarcParser.INTEGER - 73))
                        | (1 << (YarcParser.FLOAT_NUMBER - 73))
                    )
                )
                != 0
            ):
                self.state = 697
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
        self.enterRule(localctx, 116, self.RULE_exprlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self.expr()
            self.state = 705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 701
                self.match(YarcParser.COMMA)
                self.state = 702
                self.expr()
                self.state = 707
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 118, self.RULE_testlist)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708
            self.test()
            self.state = 713
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == YarcParser.COMMA:
                self.state = 709
                self.match(YarcParser.COMMA)
                self.state = 710
                self.test()
                self.state = 715
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_or_set_makerContext(ParserRuleContext):
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
            return YarcParser.RULE_dict_or_set_maker

    def dict_or_set_maker(self):
        localctx = YarcParser.Dict_or_set_makerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_dict_or_set_maker)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.test()
            self.state = 742
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.COLON]:
                self.state = 717
                self.match(YarcParser.COLON)
                self.state = 718
                self.test()
                self.state = 730
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 719
                    self.comp_for()
                    pass
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 727
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == YarcParser.COMMA:
                        self.state = 720
                        self.match(YarcParser.COMMA)
                        self.state = 721
                        self.test()
                        self.state = 722
                        self.match(YarcParser.COLON)
                        self.state = 723
                        self.test()
                        self.state = 729
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [YarcParser.FOR, YarcParser.COMMA, YarcParser.RBRACE]:
                self.state = 740
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [YarcParser.FOR]:
                    self.state = 732
                    self.comp_for()
                    pass
                elif token in [YarcParser.COMMA, YarcParser.RBRACE]:
                    self.state = 737
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == YarcParser.COMMA:
                        self.state = 733
                        self.match(YarcParser.COMMA)
                        self.state = 734
                        self.test()
                        self.state = 739
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

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
        self.enterRule(localctx, 122, self.RULE_comp_iter)
        try:
            self.state = 746
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YarcParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 744
                self.comp_for()
                pass
            elif token in [YarcParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 745
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
        self.enterRule(localctx, 124, self.RULE_comp_for)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
            self.match(YarcParser.FOR)
            self.state = 749
            self.exprlist()
            self.state = 750
            self.match(YarcParser.IN)
            self.state = 751
            self.or_test()
            self.state = 753
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 752
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
        self.enterRule(localctx, 126, self.RULE_comp_if)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.match(YarcParser.IF)
            self.state = 756
            self.test_nocond()
            self.state = 758
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == YarcParser.FOR or _la == YarcParser.IF:
                self.state = 757
                self.comp_iter()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
