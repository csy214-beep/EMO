#!/usr/bin/env python3
# scripts/update_stats.py

import os
import re
from pathlib import Path

EMO_DIR = Path("EMO")
README_PATH = Path("README.md")
START_MARK = "<!-- stats_start -->"
END_MARK = "<!-- stats_end -->"

# 配置
COLS = 5  # 表格每行的列数
USE_DETAILS = True  # 是否使用折叠块包裹表格
SUMMARY_TEXT = "Click to expand folder statistics"  # 折叠摘要文字
ignore_extensions = ['.html', '.psd',".txt",".md",".url"]

def main():
    if not EMO_DIR.exists():
        print("EMO directory not found, skipping.")
        return

    # 统计子文件夹及其文件数量
    folders = []
    total_files = 0
    for item in sorted(EMO_DIR.iterdir()):
        if item.is_dir():
            file_count = sum(
                1
                for f in item.iterdir()
                if f.is_file()
                and not (
                    f.name.startswith('.preview')  # 忽略 .preview 开头的文件
                    or f.suffix.lower() in ignore_extensions  # 忽略指定扩展名的文件
                )
            )
            folders.append((item.name, file_count))
            total_files += file_count

    # 生成总文件数字符串
    total_line = f"**Total: {total_files} files**"

    # 生成表格内容
    table_lines = []
    if folders:
        # 将文件夹列表按 COLS 切分成行
        rows = [folders[i : i + COLS] for i in range(0, len(folders), COLS)]
        # 添加表头（空表头，仅用于对齐）
        table_lines.append("| " + " | ".join([""] * COLS) + " |")
        table_lines.append("|" + "---|" * COLS)  # 分隔线
        for row in rows:
            cells = []
            for name, count in row:
                # 转义单元格内的竖线（罕见情况）
                cell_name = name.replace("|", "\\|")
                cells.append(f"{cell_name} ({count})")
            # 补足空单元格
            while len(cells) < COLS:
                cells.append("")
            table_lines.append("| " + " | ".join(cells) + " |")
    else:
        table_lines.append("| |")
        table_lines.append("|---|")
        table_lines.append("| (no folders) |")

    table_content = "\n".join(table_lines)

    # 组装完整统计块（包含总行和可能的折叠）
    if USE_DETAILS:
        stats_block = f"""{total_line}

<details>
<summary>{SUMMARY_TEXT}</summary>

{table_content}

</details>"""
    else:
        stats_block = f"{total_line}\n\n{table_content}"

    # 读取 README
    if not README_PATH.exists():
        # 文件不存在，创建完整内容
        full_content = f"""## Infor
{START_MARK}
{stats_block}
{END_MARK}"""
        README_PATH.write_text(full_content, encoding="utf-8")
        print("README created.")
        return

    content = README_PATH.read_text(encoding="utf-8")

    # 找到所有开始和结束标记的位置
    start_positions = [m.start() for m in re.finditer(re.escape(START_MARK), content)]
    end_positions = [m.start() for m in re.finditer(re.escape(END_MARK), content)]

    if not start_positions or not end_positions:
        # 缺少标记，追加到文件末尾
        with open(README_PATH, "a", encoding="utf-8") as f:
            f.write(f"\n\n## Infor\n{START_MARK}\n{stats_block}\n{END_MARK}\n")
        print("README appended.")
        return

    # 使用第一个开始标记和最后一个结束标记，中间的全部替换
    first_start = start_positions[0]
    last_end = end_positions[-1] + len(END_MARK)

    before = content[:first_start]
    after = content[last_end:]

    # 新统计块要包含开始和结束标记
    new_block = f"{START_MARK}\n{stats_block}\n{END_MARK}"

    new_content = before + new_block + after

    if new_content == content:
        print("No changes in statistics, skipping update.")
        return

    README_PATH.write_text(new_content, encoding="utf-8")
    print("README updated.")


if __name__ == "__main__":
    main()
