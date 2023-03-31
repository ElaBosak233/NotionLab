from typing import Dict

from notion_client import Client
from notion_client.api_endpoints import PagesEndpoint


class Converter(object):
    _notion: Client
    _api_token: str = ""
    _title: str = ""
    _ctx: Dict
    _has_column_header: bool = False

    def __init__(
            self,
            api_token: str,
            block_id: str,
            is_page: bool = False,
            has_column_header: bool = False
    ):
        self._api_token = api_token
        self._notion: Client = Client(auth=api_token)
        if is_page:
            page: PagesEndpoint = self._notion.pages.retrieve(page_id=block_id)
            self._title = page["properties"]["title"]["title"][0]["plain_text"]
        self._ctx = self._notion.blocks.children.list(block_id=block_id)["results"]
        self._has_column_header = has_column_header

    def convert(self):
        pass
