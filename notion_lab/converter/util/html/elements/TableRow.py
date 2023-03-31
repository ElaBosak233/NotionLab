from pprint import pprint

from ..html import *


class TableRow:
    b_ctx: Dict
    has_column_header: bool

    def __init__(self, b_ctx: Dict, has_column_header: bool = False):
        self.b_ctx = b_ctx
        self.has_column_header = has_column_header

    def export(self):
        r: str = ""
        for col in self.b_ctx["cells"]:
            rr = ""
            for child in col:
                rr += div(child)
            if self.has_column_header:
                r += f"<th>{rr}</th>"
            else:
                r += f"<td>{rr}</td>"
        return f"<tr>{r}</tr>"
