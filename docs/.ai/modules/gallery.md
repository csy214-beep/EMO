# Gallery 画廊生成 模块

## 职责

扫描 `emo/` 图片，用模板生成静态画廊 `index.html`。stdlib only，纯前端静态产物。

## 关键文件

| 文件路径 | 作用 |
|---|---|
| `scripts/generate_gallery.py` | 脚本本体（58 行） |
| `scripts/template.html` | 模板（zh-CN，title "Emo Gallery"，含 SEO/OG meta），占位符 `{{ DATA }}` |
| `index.html`（根目录） | 生成产物，图片用相对路径 `emo/<cat>/<file>` |

## 页面结构（模板实测）

- `<header class="navbar">`：顶部经典导航栏——左标题 `Emo Stickers`，右 GitHub 图标链接（`fa-brands fa-github`，无文字，`title`/`aria-label`="GitHub 仓库"，新窗口打开，链接 `https://github.com/igugyj/EMO`）
- `.layout`（flex row）：下方左右两栏——左 `<nav>` 分类列表（260px 侧栏），右 `<main>` 画廊网格
- Font Awesome CDN：cdnjs 6.5.2 `all.min.css`
- 移动端（≤768px）：`.layout` 转 column，分类栏横置限高 30vh

## 数据流

```
emo/<cat>/*（jpg/jpeg/png/gif/webp/bmp）→ json.dumps(分类+图片相对路径, ensure_ascii=False)
  → template.html.replace('{{ DATA }}', data) → 写根目录 index.html
```

细节（源码实测）：
- 分类按名称排序；每个分类内文件排序
- 无分类或模板缺失时打印错误并跳过
- 生成的 JSON 内联进 HTML——非转义中文（ensure_ascii=False）

## 依赖关系

- 依赖：仅 stdlib（json/pathlib）
- 被依赖：期望由 `.github/deploy-gallery.yml` 驱动（**当前不生效**，见 deployment 最佳实践）

## 变更记录索引

- 2025-06-01：docs/.ai 初始化（本卡建立）

> TODO: 待验证——index.html 当前是否存在/是否过时；template.html 的 JS 渲染逻辑细节