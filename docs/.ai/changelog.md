# 更新日志

本文件记录 EMO 的所有重要变更。**新条目加在顶部**。

---

## [2025-06-01]

### 画廊导航改版

- `scripts/template.html` 布局重构：左右两栏 → 上下两块
  - 顶部新增经典导航栏（`header.navbar`）——左标题、右 GitHub 图标链接（fa-brands fa-github）
  - 下方 `.layout` 保持左右两栏：左 `nav` 分类列表、右 `main` 画廊
  - 链接 `https://github.com/igugyj/EMO`，纯图标无文字，`title`/`aria-label` 提示，新窗口打开
  - 移动端媒体查询同步调整（`.layout` 转 column，nav 横置）
  - 重新运行 `python scripts/generate_gallery.py` 生成新 `index.html`
  - JS 的 `nav a` 选择器不受影响（分类列表仍在 `nav` 内）

### 初始记录

- 建立 docs/.ai 结构（Init 协议）
  - 扫描来源：README.md、AGENTS.md、requirements.txt、.gitignore、.nomedia.example、emoCut.py（grep 实测）、scripts/update_stats.py、scripts/generate_gallery.py、scripts/template.html（头部）、.github/workflows/update_stats.yml、.github/deploy-gallery.yml、emo/ 目录树
  - 待验证项：
    - emoCut.py 完整切割行为（重叠/宽高比细节未逐行读全，见 modules/emoCut.md）
    - `docs/ai/emojiMaker.prompt.txt` 内容未读（与文档协议无关，独立文件）
    - index.html 当前是否已生成、内容是否过时（generate_gallery.py 可重跑）