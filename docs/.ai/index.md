# EMO AI 上下文文档索引

## ⚠️ 必须遵守的原则（红线）

1. **不要手改 README.md 的 stats 块**（`<!-- stats_start -->` / `<!-- stats_end -->` 之间）。`update_stats.yml`（push master 时）自动重算并带 `[skip ci]` 提交。
2. **新 workflow 必须放 `.github/workflows/`**。`deploy-gallery.yml` 目前误放在 `.github/` 根，不生效。
3. **默认分支是 `master`**，不是 main。
4. **文件名非 ASCII 且带标点**（中文/日文、空格、`！？（）`）。shell 命令一律加引号。
5. `scripts/*.py` 只允许 stdlib（无第三方依赖）；只有 `emoCut.py` 需要 `pillow`。
6. 任务完成后：清冗余 + 更新对应文档 + 写 changelog。

## 项目类型

个人表情包/贴纸图库：纯内容仓库，无应用代码。表情图片在 `emo/`，辅助 Python 脚本 + GitHub Actions 维护 README 统计与静态画廊。技术栈：Python 3（stdlib + pillow）→ GitHub Actions → 静态 HTML。

## 文档结构（按优先级从高到低）

### 核心文档（必读）

| 文档路径 | 优先级 | 内容描述 |
|---|---|---|
| [core/project-overview.md](./core/project-overview.md) | 1 | 项目概述、目录结构、关键脚本 |
| [core/architecture.md](./core/architecture.md) | 2 | 数据流、CI 流水线、git 工作流 |
| [core/quick-start.md](./core/quick-start.md) | 3 | 本地验证命令、开发流程 |

### 变更台账（每次会话开头读）

| 文档路径 | 优先级 | 内容描述 |
|---|---|---|
| [changelog.md](./changelog.md) | 0 | 最新变更记录，了解项目现状 |

### 模块文档（按任务点读）

| 文档路径 | 优先级 | 内容描述 |
|---|---|---|
| [modules/emo-library.md](./modules/emo-library.md) | 4 | `emo/` 内容结构、命名、忽略规则 |
| [modules/emoCut.md](./modules/emoCut.md) | 4 | 切图工具交互流程与产物 |
| [modules/update-stats.md](./modules/update-stats.md) | 4 | README 统计块重算逻辑 |
| [modules/gallery.md](./modules/gallery.md) | 4 | 静态画廊生成 |

### 配置文档（按需参考）

| 文档路径 | 优先级 | 内容描述 |
|---|---|---|
| [config/requirements.md](./config/requirements.md) | 按需 | requirements.txt / .gitignore / .nomedia.example |

### 最佳实践（参考级）

| 文档路径 | 优先级 | 内容描述 |
|---|---|---|
| [best-practices/development.md](./best-practices/development.md) | 参考 | 文件名/路径处理、脚本维护规范 |
| [best-practices/deployment.md](./best-practices/deployment.md) | 参考 | CI 现状、已知失效流程 |

## 读取建议

1. changelog 尾部最新条目 → 项目现状
2. core/ 三篇 → 理解底座
3. 按任务点读 modules/、config/
4. 规范类 best-practices/ 按需查

## 文档更新规则

- 结构变化 → project-overview.md
- 架构变化 → architecture.md
- 模块增改 → 对应 modules/*.md
- 配置变化 → 对应 config/*.md
- **每次任务完成后必须更新 changelog.md，记录本次变更**

## 关键路径

| 路径 | 用途 |
|---|---|
| `emo/<category>/` | 表情库，每子目录一分类，主内容 |
| `emoCut.py` | 交互式图片切割工具（pillow） |
| `scripts/update_stats.py` | 重算 README 统计块 |
| `scripts/generate_gallery.py` + `scripts/template.html` | 生成根目录 `index.html` 画廊 |
| `.github/workflows/update_stats.yml` | push master 自动更新统计 |
| `.github/deploy-gallery.yml` | 画廊部署（**误放位置，不生效**） |
| `docs/ai/emojiMaker.prompt.txt` | 表情制作 prompt（与协议文档无关，勿混） |