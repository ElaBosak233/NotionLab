from typing import Dict


class Code:
    b_ctx: Dict

    def __init__(self, b_ctx: Dict):
        self.b_ctx = b_ctx

    def export(self):
        r: str = ""
        for child in self.b_ctx["rich_text"]:
            r += child["text"]["content"]
        return f"<pre>{r}</pre>"
