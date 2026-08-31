# EMO 架构文档

## 架构概览

纯内容仓库 + 轻量脚本层：**数据（emo/ 图片）→ stdlib 脚本 → 生成物（README 统计块 / index.html）**。无后端、无框架、无运行时依赖，CI 只做统计重算。

架构原则（实测归纳）：
- 内容与工具分离：图片只进 `emo/`，脚本只放仓库根/`scripts/`，生成物不提交（index.html 由脚本再生成）
- 脚本零依赖优先：`scripts/*.py` 均为 Python stdlib
- 自动流程只有一条生效链路（stats），其余靠手动

## 分层与模块

### 内容层 `emo/`

- 职责：持图，每子目录一分类
- 关键文件：41 个分类目录
- 被依赖：update_stats.py、generate_gallery.py 扫描对象

### 工具层 `emoCut.py`（根目录）

- 职责：无 GUI 的交互式切图（pillow）
- 见 [modules/emoCut.md](../modules/emoCut.md)

### 脚本层 `scripts/`

- `update_stats.py`：扫 emo/ → 算每目录文件数 → 替换 README 的 stats 块
- `generate_gallery.py`：扫 emo/ 图片 → 填 template.html 的 `{{ DATA }}` → 写根目录 index.html

### CI 层 `.github/`

- `workflows/update_stats.yml`：唯一生效工作流
- `deploy-gallery.yml`：误放 `.github/` 根，**不生效**（见 [best-practices/deployment.md](../best-practices/deployment.md)）

## 数据流

```
emo/<cat>/图片
  ├─→ scripts/update_stats.py → README.md 的 stats_start/stats_end 块（CI 自动 + 本地手动）
  └─→ scripts/generate_gallery.py → scripts/template.html({{ DATA }}) → index.html（手动）
emoCut.py: 大图 + rows/cols[+overlap][+keep_aspect_ratio] → <名>_split_{rows}x{cols}/ 小图 + info.txt
```

stats 忽略规则（update_stats.py 实测）：跳过 `.preview*` 前缀文件，跳过 `.html/.psd/.txt/.md/.url` 扩展名。

## 路由架构

无路由。无 Web 应用（index.html 为静态画廊，非应用）。

## 状态管理

无。所有状态即文件本身；统计是派生数据，随时可由脚本重算。

## 性能优化

- gallery 只收集 6 种图片扩展名（jpg/jpeg/png/gif/webp/bmp），过滤非图文件
- stats 读取完整 README 内存替换（文件小，无优化必要）

## 安全考虑

- 无输入面、无网络请求（除 CI 拉取 actions）
- CI `permissions.contents: write` 最小化到单仓库；commit message 带 `[skip ci]` 防循环触发

## 扩展性

- 新增分类：`emo/` 下建目录丢图即可，零代码改
- 新增脚本：放 `scripts/`，保持 stdlib-only；需要第三方依赖的放根目录（参照 emoCut.py + requirements.txt 模式）
- 新增 workflow：必须放 `.github/workflows/`

## 架构演进

- 初始 → 当前：纯内容仓库 + 统计脚本；`deploy-gallery.yml`（画廊部署）已写但从未生效（误置路径）
- 规划：TODO——修复 deploy-gallery.yml 路径使其生效，或删除该意图