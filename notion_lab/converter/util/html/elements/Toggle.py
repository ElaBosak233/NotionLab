import textwrap
from typing import Dict

from ..html import *

toggle_parser = """
<details>
<summary>{}</summary>

{}

</details>
"""


class Toggle:
    b_ctx: Dict
    details: str

    def __init__(self, b_ctx: Dict, details: str):
        self.b_ctx = b_ctx
        self.details = details

    def export(self):
        r = ""
        for child in self.b_ctx["rich_text"]:
            r += div(child)
        return toggle_parser.format(r, self.details)
