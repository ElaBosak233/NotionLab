from . import Converter
from .util.html import *
from .util.html.elements import *


class HtmlConverter(Converter):
    _html: str = ""
    _bulleted_list_counter: int = 0
    _numbered_list_counter: int = 0
    _table_row_parsed: bool = False

    def __init__(
            self,
            api_token: str,
            block_id: str,
            is_page: bool = False,
            has_column_header: bool = False
    ):
        super().__init__(api_token, block_id, is_page, has_column_header)

    def convert(
            self
    ) -> str:
        self._html += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
        if self._title:
            self._html += f"<title>{self._title}</title>"
        for block in self._ctx:
            b_type = block["type"]
            b_ctx = block[f"{b_type.lower()}"]
            b_id = block["id"]
            if b_type != "bulleted_list_item" and self._bulleted_list_counter != 0:
                """
                无序列表封底&计数器复位
                """
                self._html += "</ul>"
                self._bulleted_list_counter = 0
            if b_type != "numbered_list_item" and self._numbered_list_counter != 0:
                """
                有序列表封底&计数器复位
                """
                self._html += "</ol>"
                self._numbered_list_counter = 0
            # 遍历开始
            if b_type in text_mapping:
                """
                H1,H2,H3,P 转换
                """
                if len(b_ctx["rich_text"]) != 0:
                    self._html += Text(b_type, b_ctx).export()
                else:
                    self._html += "<br />"
            elif b_type == "image":
                """
                图片转换
                """
                self._html += Image(b_ctx).export()
            elif b_type == "toggle":
                """
                折叠框转换
                """
                r: str = HtmlConverter(
                    api_token=self._api_token,
                    block_id=b_id,
                    is_page=False
                ).convert()
                self._html += Toggle(b_ctx, details=r).export()
            elif b_type == "code":
                """
                代码框转换
                """
                self._html += Code(b_ctx).export()
            elif b_type == "divider":
                """
                分割线转换
                """
                self._html += f"<hr />"
            elif b_type == "bulleted_list_item":
                """
                无序列表转换
                """
                if self._bulleted_list_counter == 0:
                    self._html += "<ul>"
                self._bulleted_list_counter += 1
                self._html += List(b_ctx).export()
            elif b_type == "numbered_list_item":
                """
                有序列表转换
                """
                if self._numbered_list_counter == 0:
                    self._html += "<ol>"
                self._numbered_list_counter += 1
                self._html += List(b_ctx).export()
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
                self._html += f'<table border="1">{r}</table>'
            elif b_type == "table_row":
                """
                表格行转换
                """
                if not self._table_row_parsed:
                    self._html += TableRow(b_ctx, self._has_column_header).export()
                    self._table_row_parsed = True
                else:
                    self._html += TableRow(b_ctx).export()
        return self._html
