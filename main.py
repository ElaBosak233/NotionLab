import os
import codecs

from notion_lab.converter import MDConverter

# 52a812df2b5e444285af7ebbd5a135bc
# c9fa055d79a84224b266bf5ebd9b2ca7

block_id = "c9fa055d79a84224b266bf5ebd9b2ca7"

cvt = MDConverter(api_token=os.environ["NOTION_API_TOKEN"],block_id=block_id)

f = codecs.open('out/test.md', 'w', 'utf-8')
f.write(cvt.convert())
f.close()