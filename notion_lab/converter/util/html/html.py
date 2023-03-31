import textwrap
from typing import Dict

text_mapping: Dict = {
    "heading_1": "h1",
    "heading_2": "h2",
    "heading_3": "h3",
    "paragraph": "p",
    "quote": "blockquote"
}


def div(child: Dict):
    """
    <div> 元素生成器
    """
    style = f'style="display: inline; {style_parser(child["annotations"])}"'
    r = f'<div {style}>{child["text"]["content"]}</div>'
    if child["href"]:
        r = textwrap.dedent(f"""
        <a href="{child["href"]}">
            {r}
        </a>
        """)
    if child["annotations"]["code"]:
        r = f"<code>{r}</code>"
    return r


def style_parser(annotations):
    """
    样式组合器
    """
    style = ""
    if annotations["bold"]:
        # 加粗
        style += 'font-weight: bold;'
    if annotations["italic"]:
        # 斜体
        style += 'font-style: italic;'
    if annotations["underline"] or annotations["strikethrough"]:
        # 下划线和删除线
        u = annotations["underline"]
        s = annotations["strikethrough"]
        style += f'text-decoration: {"underline" if u else ""} {"line-through" if s else ""};'
    if annotations["color"] and annotations["color"] != "default":
        # 字体颜色和背景颜色（二选一）
        if "_background" in annotations["color"]:
            style += f'background: {annotations["color"][:-11:1]};'
        else:
            style += f'color: {annotations["color"]};'
    return style
