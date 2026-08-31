# emoCut 切图工具 模块

## 职责

交互式把一张大图切成 rows×cols 小图，支持重叠像素与保持小图宽高比。命令行工具，无 GUI。

## 关键文件

| 文件路径 | 作用 |
|---|---|
| `emoCut.py` | 工具本体（约 347 行，依赖 pillow） |
| `requirements.txt` | `pillow==12.0.0`（唯一依赖来源） |

## 使用流程（实测 grep 归纳）

1. `python emoCut.py`
2. 提示输入图片路径（自动去两端引号；可选列目录文件供选择）
3. 确认图片 → 输入 rows、cols（校验 >0）
4. 可选重叠像素 `overlap`（默认 0，非负校验）、是否保持宽高比 `keep_aspect_ratio`（默认否）
5. 可选自定义输出目录（直接回车用默认）
6. 确认切割 → 输出 + 可选打开输出目录

核心函数：`split_image(image_path, rows, cols, output_dir=None, overlap=0, keep_aspect_ratio=False)`

## 数据流

```
大图 + rows×cols [+overlap] [+keep_aspect_ratio]
  → 默认目录 <图片名>_split_{rows}x{cols}/（与图片同目录）
  → 小图（tile 命名）+ info.txt（记录 rows/cols/overlap/keep_aspect_ratio 等参数）
```

重叠实现：`left = max(0, j*tile_width - overlap)`、`upper = max(0, i*tile_height - overlap)`（源码 89-97 行），即每块向上下左右各扩展 overlap 像素。

## 依赖关系

- 依赖：pillow（PIL.Image）
- 被依赖：无（独立工具）

## 变更记录索引

- 2025-06-01：docs/.ai 初始化（本卡建立）

> TODO: 待验证——tile 命名规则、keep_aspect_ratio 具体实现细节（未逐行读全，需时看源码）+ 完整交互文案