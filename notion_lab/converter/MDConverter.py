from .util.html.elements import Toggle, TableRow

from . import Converter, HtmlConverter
from .util.md import div

code_parser = """
```
{}
```
"""


class MDConverter(Converter):
    _md: str = ""
    _numbered_list_counter: int = 1

    def __init__(
            self,
            api_token: str,
            block_id: str,
            is_page: bool = False,
            has_column_header: bool = False
    ):
        super().__init__(api_token, block_id, is_page, has_column_header)

    def convert(self) -> str:
        for block in self._ctx:
            b_type = block["type"]
            b_ctx = block[f"{b_type.lower()}"]
            b_id = block["id"]
            if b_type != "numbered_list_item":
                self._numbered_list_counter = 1
            if b_type == "heading_1":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += div(child)
                self._md += f"# {r}\n\n"
            elif b_type == "heading_2":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += div(child)
                self._md += f"## {r}\n\n"
            elif b_type == "heading_3":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += div(child)
                self._md += f"### {r}\n\n"
            elif b_type == "paragraph":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += div(child)
                self._md += f"{r}\n\n"
            elif b_type == "code":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += child["text"]["content"]
                self._md += code_parser.format(r) + "\n"
            elif b_type == "image":
                if b_ctx["type"] == "file":
                    self._md += f'![]({b_ctx["file"]["url"]})\n'
                elif b_ctx["type"] == "external":
                    self._md += f'![]({b_ctx["external"]["url"]})\n'
            elif b_type == "divider":
                self._md += "---\n\n"
            elif b_type == "quote":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += child["text"]["content"]
                self._md += f"> {r}\n"
            elif b_type == "bulleted_list_item":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += div(child)
                self._md += f"- {r}\n"
            elif b_type == "numbered_list_item":
                r = ""
                for child in b_ctx["rich_text"]:
                    r += div(child)
                self._md += f"{self._numbered_list_counter}. {r}\n"
                self._numbered_list_counter += 1
            elif b_type == "table":
                """
                表格转换
                """
                r: str = HtmlConverter(
                    api_token=self._api_token,
                    block_id=b_id,
                    is_page=False,
                    has_column_header=b_ctx["has_column_header"]
                ).convert()
                self._md += f'<table>{r}</table>'
            elif b_type == "table_row":
                """
                表格行转换
                """
                self._md += TableRow(b_ctx).export()
            elif b_type == "toggle":
                r: str = MDConverter(
                    api_token=self._api_token,
                    block_id=b_id,
                    is_page=False
                ).convert()
                self._md += Toggle(b_ctx, details=r).export()

        return self._md
