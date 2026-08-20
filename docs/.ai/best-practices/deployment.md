# 部署与 CI 最佳实践

## 现状（实测）

**生效链路（唯一）**：`.github/workflows/update_stats.yml`

- 触发：push 到 `master` + `workflow_dispatch` 手动
- 流程：checkout@v4 → setup-python@v5（"3.x"）→ `python scripts/update_stats.py` → 有变更则 git 提交 `"Update folder statistics [skip ci]"` 并 push
- 关键点：`permissions.contents: write`；`concurrency.cancel-in-progress: true` 取消同分支旧运行；`[skip ci]` 防 CI 提交再触发 CI

**失效链路（已知问题）**：`.github/deploy-gallery.yml`

- 误放在 `.github/` 根而非 `.github/workflows/`，GitHub Actions 不识别该路径 → 从不运行
- 设计意图（按文件内容）：push master / 每周一 0 点 / 手动 → 生成画廊 → peaceiris/actions-gh-pages 发布到 `gh-pages` 分支（force_orphan）

## 规范

- 新 workflow 一律放 `.github/workflows/`
- 默认分支 `master`，写 workflow 的 branches 时注意
- 画廊部署如需生效：把 `deploy-gallery.yml` 移到 `.github/workflows/`，再确认 GitHub Pages 源分支配置为 `gh-pages`

## 违例与后果

- workflow 放错目录 → 静默不执行，无报错。当前 deploy-gallery.yml 即此状态
- 改动 README 由 CI 提交时漏 `[skip ci]` → 提交触发 CI 再跑再提交，死循环（现工作流已带，勿删）