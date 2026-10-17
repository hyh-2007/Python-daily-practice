"""在仓库中创建下一天的笔记和代码，不自动上传。"""

from datetime import date
from pathlib import Path
import re


def create_next_day(root):
    """读取模板并新建下一编号的目录，已有目录不会被覆盖。"""
    root = Path(root)
    day_numbers = []
    for item in root.iterdir():
        match = re.fullmatch(r"day(\d+)", item.name)
        if match and item.is_dir():
            day_numbers.append(int(match.group(1)))
    next_number = max(day_numbers, default=0) + 1
    target = root / f"day{next_number:02d}"

    # 先读完模板，再创建目录，避免缺少模板时留下空目录。
    contents = {}
    for name in ("day.md", "day.py"):
        text = (root / "templates" / name).read_text(encoding="utf-8")
        contents[name] = text.replace("{{DAY}}", str(next_number)).replace(
            "{{DATE}}", date.today().isoformat()
        )

    target.mkdir()
    for name, text in contents.items():
        with (target / name).open("x", encoding="utf-8") as output:
            output.write(text)
    return target


if __name__ == "__main__":
    directory = create_next_day(Path(__file__).resolve().parent)
    print(f"已创建：{directory}")
    print("请填写 day.md 和 day.py，运行检查后按 README 的步骤上传。")
