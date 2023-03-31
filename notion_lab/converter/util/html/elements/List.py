import textwrap

from ..html import *


class List:
    b_ctx: Dict

    def __init__(self, b_ctx: Dict):
        self.b_ctx = b_ctx

    def export(self):
        r = ""
        for child in self.b_ctx["rich_text"]:
            r += div(child)
        return textwrap.dedent(f"""
            <li>
                {r}
            </li>
        """)
