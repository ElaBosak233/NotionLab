from typing import Dict


def div(child: Dict):
    r: str = child["text"]["content"]
    r = r.rstrip()
    if child["annotations"]["code"]:
        r = f"`{r}`"
    if child["annotations"]["bold"]:
        r = f"**{r}**"
    if child["annotations"]["italic"]:
        r = f"*{r}*"
    if child["annotations"]["strikethrough"]:
        r = f"~~{r}~~"
    if child["href"]:
        r = f'[{r}]({child["href"]})'
    if child["annotations"]["underline"]:
        r = f"<u>{r}</u>"
    if child["annotations"]["color"] and child["annotations"]["color"] != "default":
        # 字体颜色和背景颜色（二选一）
        if "_background" in child["annotations"]["color"]:
            r = f'<span style="background: {child["annotations"]["color"][:-11:1]};">{r}</span>'
        else:
            r = f'<span style="color: {child["annotations"]["color"]};">{r}</span>'
    return f"{r}"
