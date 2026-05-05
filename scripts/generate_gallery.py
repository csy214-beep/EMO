import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # 项目根目录
EMO_DIR = BASE_DIR / 'emo'
TEMPLATE_FILE = Path(__file__).resolve().parent / 'template.html'
OUTPUT_INDEX = BASE_DIR / 'index.html'  # 直接在根目录生成


def get_categories():
    categories = []
    if not EMO_DIR.is_dir():
        print(f"错误：找不到 {EMO_DIR}")
        return categories

    for cat_dir in sorted(EMO_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        images = []
        for file in sorted(cat_dir.iterdir()):
            if file.is_file() and file.suffix.lower() in (
                '.jpg',
                '.jpeg',
                '.png',
                '.gif',
                '.webp',
                '.bmp',
            ):
                # 图片路径：相对于 index.html 所在目录（根目录）
                rel = f'emo/{cat_dir.name}/{file.name}'
                images.append(rel)
        if images:
            categories.append({'name': cat_dir.name, 'images': images})
    return categories


def main():
    categories = get_categories()
    if not categories:
        print("没有找到任何表情分类。")
        return

    data_json = json.dumps(categories, ensure_ascii=False)

    if not TEMPLATE_FILE.is_file():
        print(f"模板文件 {TEMPLATE_FILE} 不存在。")
        return

    template = TEMPLATE_FILE.read_text(encoding='utf-8')
    # 注意占位符与模板内一致（假设为 {{DATA}}）
    html = template.replace('{{ DATA }}', data_json)

    OUTPUT_INDEX.write_text(html, encoding='utf-8')
    print(f"画廊已生成 → {OUTPUT_INDEX}")


if __name__ == '__main__':
    main()
