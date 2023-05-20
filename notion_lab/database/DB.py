from typing import Dict, Optional

from notion_client import Client
from ..converter.util.html.elements import Text


class DB(object):
    _notion: Client
    _api_token: str = ""
    _ctx: Dict

    def __init__(
            self,
            api_token: str,
            database_id: str,
            db_filter: Optional[Dict] = None
    ):
        self._api_token = api_token
        self._notion: Client = Client(auth=api_token)
        self._ctx = self._notion.databases.query(
            **{
                "database_id": database_id,
                "filter": db_filter
            }
        )

    def out(self):
        return self._ctx

    def traversal(self):
        m = []
        for data in self._ctx["results"]:
            dc = {"id": data["id"]}
            for d_property in data["properties"]:
                d_type = data["properties"][d_property]["type"]
                if d_type == "title":
                    # 标题
                    dc[d_property] = data["properties"][d_property]["title"][0]["plain_text"]
                elif d_type == ("url" or "email" or "tel" or "number"):
                    # 链接
                    if data["properties"][d_property][d_type] is not None:
                        dc[d_property] = data["properties"][d_property][d_type]
                elif d_type == "multi_select":
                    # 复选框
                    ms = []
                    for i in data["properties"][d_property]["multi_select"]:
                        ms.append(i["name"])
                    dc[d_property] = ms
                elif d_type == "rich_text":
                    # 富文本
                    if len(data["properties"][d_property]["rich_text"]) != 0:
                        dc[d_property] = Text("text", data["properties"][d_property]).export()

            m.append(dc)
        return m
