import codecs
import os

from notion_lab.converter import MDCvt, HtmlCvt
from notion_lab.database import DB

# 52a812df2b5e444285af7ebbd5a135bc
# c9fa055d79a84224b266bf5ebd9b2ca7

block_id = "49b140d0-bed4-4343-b439-80c88d1bef83"
database_id = "290cd6f4443e455d8873b9afad33b039"


def markdown_cvt_test():
    cvt = MDCvt(api_token=os.environ["NOTION_API_TOKEN"], block_id=block_id)
    f = codecs.open('out/test.md', 'w', 'utf-8')
    f.write(cvt.convert())
    f.close()


def html_cvt_test():
    cvt = HtmlCvt(api_token=os.environ["NOTION_API_TOKEN"], block_id=block_id)
    f = codecs.open('out/test.md', 'w', 'utf-8')
    f.write(cvt.convert())
    f.close()


def database_traversal_test():
    db = DB(api_token=os.environ["NOTION_API_TOKEN"], database_id=database_id)
    for i in db.traversal():
        cvt = MDCvt(api_token=os.environ["NOTION_API_TOKEN"], block_id=i["id"])
        f = codecs.open(f'out/db/{i["title"]}.md', 'w', 'utf-8')
        f.write(cvt.convert())
        f.close()


if __name__ == "__main__":
    database_traversal_test()
    # markdown_cvt_test()
