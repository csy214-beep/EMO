# update_stats 统计脚本 模块

## 职责

扫描 `emo/` 各分类目录，统计文件数，重算并替换 README.md 中 `<!-- stats_start -->` / `<!-- stats_end -->` 之间的统计块。stdlib only。

## 关键文件

| 文件路径 | 作用 |
|---|---|
| `scripts/update_stats.py` | 脚本本体（127 行） |
| `README.md` | 被修改目标（stats 块） |
| `.github/workflows/update_stats.yml` | CI 自动执行（push master） |

## 输出格式（实测）

- `**Total: N files**` 总行
- `<details>` 折叠块内 5 列表格（`COLS = 5`），每格 `分类名 (数量)`
- 空分类时输出 `(no folders)`

## 数据流

```
emo/<cat>/ 遍历 → 过滤（.preview* 前缀 + .html/.psd/.txt/.md/.url 后缀）→ 计数
  → 组装 stats 块 → 替换 README 首个 start 到末个 end 标记之间内容
  → 无变化则跳过（"No changes in statistics, skipping update."）
```

边界行为（源码实测）：
- 无 `emo/` 目录：打印跳过，不动 README
- README 无标记：追加 `## Infor` 段落
- README 不存在：创建含完整 stats 块的 README
- 多对标记：用首个开始 + 末个结束，中间全替换

## 依赖关系

- 依赖：仅 stdlib（os/re/pathlib）
- 被依赖：CI workflow（python scripts/update_stats.py）

## 变更记录索引

- 2025-06-01：docs/.ai 初始化（本卡建立）