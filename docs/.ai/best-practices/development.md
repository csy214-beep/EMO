# 开发最佳实践

## 文件命名与路径处理（红线级）

来源：AGENTS.md + 目录实测。

- 文件名大量非 ASCII（中文/日文）且带全角标点：`！？（）`、空格。shell 命令必须引号包裹，例：`python emoCut.py "emo/超かぐや姫！/图.png"`
- Windows 与 Android 路径混用：仓库内一律相对路径 + `/`；`.nomedia.example` 里是绝对 Android 路径（仅示例）
- 分类名唯一即可，改名会破坏 README 统计与 index.html 相对路径一致性（改后必须重跑两脚本）

## 脚本维护规范

来源：scripts/*.py 源码实测。

- `scripts/` 下只允许 stdlib（os/re/pathlib/json）；需要第三方依赖的工具放仓库根（emoCut.py 模式），依赖进 requirements.txt
- 脚本输出用中文；面向终端交互（emoCut.py）带确认步骤
- 生成物不重复提交逻辑：index.html、README stats 块都是派生数据，可随时重跑恢复

## 踩坑记录

| 症状 | 根因 | 解法 |
|---|---|---|
| 忘记了 `.preview` 文件进统计 | update_stats 按前缀/后缀过滤，`.preview*` 跳过 | 预览图命名加 `.preview` 前缀即可不进统计 |
| README 统计被 CI 提交覆盖手改 | 红线：勿手改 stats 块 | 改 README 其他部分没问题，stats 块交给脚本 |
| 分类目录名带 `|` | 表格单元格转义处理过了（`\\|`），无需担心 | —— |
| 切图产物 info.txt 被 git 跟踪 | .gitignore 已忽略 | 无需处理 |

## 违例与后果

- 手改 stats 块 → CI push 后自动重算覆盖，手改丢失——已列入红线
- 脚本引入第三方依赖 → 破坏 stdlib-only 约定，CI 无 requirements 安装步骤会挂——严格禁止