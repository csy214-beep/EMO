# 表情库内容 模块

## 职责

`emo/` 下每个子目录一个分类，直接放图片即为全部内容。本仓库的主体数据，无代码逻辑（逻辑在本模块，脚本见同目录其他卡）。

## 关键文件

| 文件路径 | 作用 |
|---|---|
| `emo/<category>/` | 分类目录，41 个（README 统计 Total 1089 files） |
| `README.md` stats 块 | 每个分类的文件计数（由 update_stats.py 生成） |
| `.gitignore` | 忽略 `**/bilibili超かぐや姫！`（该分类部分文件被 git 忽略，计数仍计入） |

## 数据流

```
emo/<cat>/图片 → update_stats.py 扫描统计 → README stats 块
emo/<cat>/图片 → generate_gallery.py 扫描 → index.html 画廊
```

计数忽略规则（update_stats.py 实测）：`.preview` 前缀文件 + `.html/.psd/.txt/.md/.url` 扩展名不计入。

## 依赖关系

- 被 `scripts/update_stats.py`、`scripts/generate_gallery.py` 扫描
- 被 Android EweSticker 等应用直接引用为贴纸源

## 变更记录索引

- 2025-06-01：docs/.ai 初始化（本卡建立）