# NotionLab

![](https://i.postimg.cc/4yLS0xBN/Notion-Lab.png)

<div align="center">

![](https://img.shields.io/pypi/v/NotionLab?style=flat-square)
![](https://img.shields.io/github/v/tag/ElaBosak233/NotionLab?include_prereleases&style=flat-square)

</div>
 
***NotionLab is an easy-to-use Notion toolkit based on the [Notion Python SDK](https://github.com/ramnes/notion-sdk-py).
Designed to tap the maximum potential of the [Notion API](https://developers.notion.com/).***

## Installation

```bash
pip install NotionLab
```

## Usage

```python
import os
from notion_lab.converter import HtmlConverter

cvt = HtmlConverter(api_token=os.environ["NOTION_API_TOKEN"],
                    block_id="52a812df2b5e444285af7ebbd5a135bc",
                    is_page=True
                    )

print(cvt.convert())
```