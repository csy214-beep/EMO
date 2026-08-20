# EMO 快速开始

## 环境要求

- **系统**：Windows（本机实测，`python` 命令可用即可）；CI 用 ubuntu-latest
- **运行时**：Python 3.x（无版本下限声明；requirements 仅 pillow）
- **硬件**：无要求

## 安装步骤

```bash
cd D:/Users/user/Pictures/EMO

# 切图工具需要 pillow
pip install -r requirements.txt
```

其余脚本（统计/画廊）纯 stdlib，无需安装。

## 基本命令（全部实测）

| 命令 | 功能 |
|---|---|
| `python scripts/update_stats.py` | 重算 README 统计块（无变化时输出 "No changes in statistics, skipping update."） |
| `python scripts/generate_gallery.py` | 生成根目录 index.html（无图片时输出"没有找到任何表情分类。"） |
| `python emoCut.py` | 交互式切图（提示输入图片路径、行列、重叠、宽高比、输出目录，逐一确认后切割） |

## 开发流程

**加表情**：
1. `emo/` 下建分类目录（或复用已有）
2. 丢图片进去（命名随意，但见 best-practices/development.md 的引号规范）
3. 可选：本地跑 `update_stats.py` 刷新 README；push master 后 CI 会自动重算

**改脚本**：
1. 脚本保持纯 stdlib；需第三方依赖的脚本放根目录并更新 requirements.txt
2. 改完本地实测（如 `update_stats.py` 改后跑一次验证输出）
3. 任务完成后按 docs/.ai 协议回写文档 + changelog

## 调试技巧

- stats 脚本：改完直接跑，观察 "README updated." / "No changes in statistics" 输出判断是否生效
- gallery：生成后浏览器打开根目录 `index.html` 检查图片路径对不对（相对路径 `emo/<cat>/<file>`）
- 忘引号报错时：路径含中文/日文/空格/全角标点，shell 加引号 `"path"`

## 常见问题

| 症状 | 原因 | 解法 |
|---|---|---|
| CI 改了 README 但本地没变 | push 后 Actions 才跑 | 本地先手动跑 update_stats.py 或等 CI 提交 |
| deploy 画廊不生效 | .github/deploy-gallery.yml 位置错 | 移到 .github/workflows/（当前不生效） |
| README 统计数不符 | 手改了 stats 块或加了忽略扩展名文件 | 重跑 update_stats.py |

## 下一步

- [模块文档](../modules/)
- [配置文档](../config/)
- [最佳实践](../best-practices/)