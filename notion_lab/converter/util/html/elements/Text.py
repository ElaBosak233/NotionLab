from ..html import *


class Text:
    b_ctx: Dict
    b_type: str

    def __init__(self, b_type: str, b_ctx: Dict):
        self.b_type = b_type
        self.b_ctx = b_ctx

    def export(self):
        r = ""
        for child in self.b_ctx["rich_text"]:
            r += div(child)
        return textwrap.dedent(f"""
        <{text_mapping[self.b_type]}>
            {r}
        </{text_mapping[self.b_type]}>
        """)
