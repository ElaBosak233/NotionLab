from typing import Dict, Optional

from notion_client import Client


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
            print(data["properties"])
            for d_property in data["properties"]:
                if data["properties"][d_property]["type"] == "title":
                    dc[d_property] = data["properties"][d_property]["title"][0]["plain_text"]
                elif data["properties"][d_property]["type"] == "url":
                    dc[d_property] = data["properties"][d_property]["url"]
                elif data["properties"][d_property]["type"] == "multi_select":
                    ms = []
                    for i in data["properties"][d_property]["multi_select"]:
                        ms.append(i["name"])
                    dc[d_property] = ms
            m.append(dc)
        return m
