# EMO 项目概述

## 基本信息

- **名称**：EMO（Personal Emoticon Library）
- **位置**：`D:\Users\user\Pictures\EMO`
- **类型**：纯内容表情包图库，无应用代码。辅助脚本维护统计与画廊
- **技术栈**：Python 3（stdlib）+ pillow 12.0.0 + GitHub Actions（ubuntu-latest）

## 项目类型说明

- 仓库主体是 `emo/` 下的图片（41 个分类，README 统计 Total 1089 files）
- 无运行时、无服务端、无构建产物提交（`index.html` 由脚本生成）
- 所有表情来源互联网，仅限个人学习交流（README Acknowledge 声明）

## 技术栈

| 技术 | 版本 | 用途 |
|---|---|---|
| Python | 3.x（CI 用 "3.x"） | 统计/画廊/切图脚本 |
| pillow | 12.0.0（requirements.txt） | 仅 emoCut.py 需要 |
| GitHub Actions | actions/checkout@v4, setup-python@v5 | README 统计自动更新 |

## 目录结构

```
EMO/
├── emo/                    # 表情库，每子目录一分类（主内容）
├── emoCut.py               # 交互式切图工具（pillow）
├── scripts/
│   ├── update_stats.py     # 重算 README 统计块（stdlib only）
│   ├── generate_gallery.py # 生成 index.html 画廊（stdlib only）
│   └── template.html       # 画廊模板，占位符 {{ DATA }}
├── .github/
│   ├── deploy-gallery.yml     # 画廊部署（误放位置，不生效）
│   └── workflows/update_stats.yml  # 统计自动更新（生效）
├── docs/
│   ├── ai/emojiMaker.prompt.txt  # 表情制作 prompt（非协议文档）
│   └── .ai/                     # 本项目 AI 协议文档
├── README.md               # 项目说明 + stats 块（勿手改）
├── AGENTS.md               # agent 指引（与 docs/.ai 内容互补）
├── requirements.txt        # pillow==12.0.0
├── .gitignore              # .venv / info.txt / **/bilibili超かぐや姫！
└── .nomedia.example        # Android .nomedia 示例路径
```

## 关键功能

- **表情库**：`emo/<category>/` 直接丢图片即为新增内容；供 Android [EweSticker](https://github.com/FredHappyface/Android.EweSticker) 等应用指向该目录使用。
- **统计数据**：`python scripts/update_stats.py` 重算 README 的 stats 块（Total 行 + 5 列分类表格，折叠块）。
- **切图工具**：`python emoCut.py` 交互式把大图切成 rows×cols 小图，输出 `<名>_split_{rows}x{cols}/` 目录（内含小图 + info.txt）。
- **画廊生成**：`python scripts/generate_gallery.py` 扫描 `emo/*/` 的图片，以脚本同目录 `template.html` 为模板，替换 `{{ DATA }}`，写出根目录 `index.html`。

## 重要配置

- `requirements.txt`：仅 `pillow==12.0.0`（emoCut.py 依赖）
- `.gitignore`：`.venv`、`info.txt`、`**/bilibili超かぐや姫！`
- `.nomedia.example`：内容 `/storage/emulated/0/project/emo`——Android 上防相册扫描的 `.nomedia` 示例
- 无 env 变量

## 开发命令

| 命令 | 功能 |
|---|---|
| `pip install -r requirements.txt` | 安装切图工具依赖 |
| `python scripts/update_stats.py` | 重算 README 统计块 |
| `python scripts/generate_gallery.py` | 重新生成 index.html |
| `python emoCut.py` | 交互式切图 |

## 开发规范

- `scripts/*.py` 只用 stdlib；只有 `emoCut.py` 可依赖 pillow（不混用）
- 中文输出消息；CJK 文件名
- 文档维护遵循 docs/.ai 协议：任务完成 → 清冗余 → 回写文档 → changelog 顶部记账

## 已知问题

- `.github/deploy-gallery.yml` 不在 `.github/workflows/`，画廊部署流程从不运行
- 文件名非 ASCII + 标点重，shell 里必须引号包裹