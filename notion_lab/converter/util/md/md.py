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
        r = f'<font color={child["annotations"]["color"]}>{r}</font>'
        pass
    return f"{r}"

