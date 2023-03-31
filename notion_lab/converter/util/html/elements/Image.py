import textwrap
from typing import Dict


class Image:
    b_ctx: Dict

    def __init__(self, b_ctx: Dict):
        self.b_ctx = b_ctx

    def export(self):
        if self.b_ctx["type"] == "file":
            return textwrap.dedent(f"""
                <img src="{self.b_ctx["file"]["url"]}" />
            """)
        elif self.b_ctx["type"] == "external":
            return textwrap.dedent(f"""
                <img src="{self.b_ctx["external"]["url"]}" />
            """)
