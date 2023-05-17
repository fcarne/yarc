import collections

from antlr3 import ANTLRFileStream, ANTLRStringStream, Token, TokenStream

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
    def __init__(self, stream: TokenStream):
        self.input: ANTLRStringStream = stream.tokenSource.input
        self.strdata: list[str] = self.input.strdata.split("\n")

    def format_error(self, tk: Token, error_msg: str) -> str:
        row = []
        header = f"Error occured at line {tk.line}"
        if isinstance(self.input, ANTLRFileStream):
            header += f" in file {self.input.fileName}"
        row.append(header)
        row.append("\n")

        line = self.strdata[tk.line - 1]

        stripped_line = line.strip()
        row.append(f"    {stripped_line}\n")

        orig_line_len = len(line)
        frame_line_len = len(line.lstrip())
        stripped_characters = orig_line_len - frame_line_len

        start_offset = tk.charPositionInLine
        end_offset = start_offset + len(tk.text)

        # TODO: Add anchor computations, if ever needed ¯\_(ツ)_/¯
        anchors = None

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
        row.append("\n")
        row.append(error_msg)
        return "".join(row)
