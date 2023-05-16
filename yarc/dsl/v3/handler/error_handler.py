import collections

from antlr3 import Token

_Anchors = collections.namedtuple(
    "_Anchors",
    [
        "left_end_offset",
        "right_start_offset",
        "primary_char",
        "secondary_char",
    ],
    defaults=["~", "^"],
)


class ErrorHandler:
    def __init__(self, input):
        self.input = input

    def format_error(self, tk: Token, error_msg: str) -> str:
        row = []
        row.append(
            '  File "{}", line {}, in {}\n'.format(
                frame_summary.filename, frame_summary.lineno, frame_summary.name
            )
        )
        if frame_summary.line:
            stripped_line = frame_summary.line.strip()
            row.append(f"    {stripped_line}\n")

            orig_line_len = len(frame_summary._original_line)
            frame_line_len = len(frame_summary.line.lstrip())
            stripped_characters = orig_line_len - frame_line_len
            if frame_summary.colno is not None and frame_summary.end_colno is not None:
                start_offset = (
                    _byte_offset_to_character_offset(
                        frame_summary._original_line, frame_summary.colno
                    )
                    + 1
                )
                end_offset = (
                    _byte_offset_to_character_offset(
                        frame_summary._original_line, frame_summary.end_colno
                    )
                    + 1
                )

                anchors = None
                if frame_summary.lineno == frame_summary.end_lineno:
                    with suppress(Exception):
                        anchors = _extract_caret_anchors_from_line_segment(
                            frame_summary._original_line[
                                start_offset - 1 : end_offset - 1
                            ]
                        )
                else:
                    end_offset = stripped_characters + len(stripped_line)

                # show indicators if primary char doesn't span the frame line
                if end_offset - start_offset < len(stripped_line) or (
                    anchors and anchors.right_start_offset - anchors.left_end_offset > 0
                ):
                    row.append("    ")
                    row.append(" " * (start_offset - stripped_characters))

                    if anchors:
                        row.append(anchors.primary_char * (anchors.left_end_offset))
                        row.append(
                            anchors.secondary_char
                            * (anchors.right_start_offset - anchors.left_end_offset)
                        )
                        row.append(
                            anchors.primary_char
                            * (end_offset - start_offset - anchors.right_start_offset)
                        )
                    else:
                        row.append("^" * (end_offset - start_offset))

                    row.append("\n")

        if frame_summary.locals:
            for name, value in sorted(frame_summary.locals.items()):
                row.append(f"    {name} = {value}\n")

        return "".join(row)

    def _extract_caret_anchors_from_line_segment(segment):
        import ast

        try:
            tree = ast.parse(segment)
        except SyntaxError:
            return None

        if len(tree.body) != 1:
            return None

        normalize = lambda offset: _byte_offset_to_character_offset(segment, offset)
        statement = tree.body[0]
        match statement:
            case ast.Expr(expr):
                match expr:
                    case ast.BinOp():
                        operator_start = normalize(expr.left.end_col_offset)
                        operator_end = normalize(expr.right.col_offset)
                        operator_str = segment[operator_start:operator_end]
                        operator_offset = len(operator_str) - len(operator_str.lstrip())

                        left_anchor = expr.left.end_col_offset + operator_offset
                        right_anchor = left_anchor + 1
                        if (
                            operator_offset + 1 < len(operator_str)
                            and not operator_str[operator_offset + 1].isspace()
                        ):
                            right_anchor += 1
                        return _Anchors(normalize(left_anchor), normalize(right_anchor))
                    case ast.Subscript():
                        subscript_start = normalize(expr.value.end_col_offset)
                        subscript_end = normalize(expr.slice.end_col_offset + 1)
                        return _Anchors(subscript_start, subscript_end)

        return None
