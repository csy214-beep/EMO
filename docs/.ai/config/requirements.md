# 依赖与仓库配置 配置文档

> 本仓库无传统"主配置"。三个小配置合并记录（requirements / gitignore / nomedia），按需参考。

## requirements.txt

**位置**：`requirements.txt`

| 配置项 | 值 | 作用 |
|---|---|---|
| pillow | ==12.0.0 | 唯一第三方依赖，仅 emoCut.py 使用（PIL.Image） |

修改注意：scripts/ 下脚本必须保持 stdlib-only，新第三方依赖一律进主清单并在根部放脚本。

## .gitignore

**位置**：`.gitignore`

| 项 | 作用 |
|---|---|
| `.venv` | 忽略虚拟环境 |
| `info.txt` | 忽略切图产物记录文件（emoCut.py 输出） |
| `**/bilibili超かぐや姫！` | 忽略该分类目录（注意：含全角感叹号，路径引用需引号） |

修改注意：`.gitignore` 不影响 update_stats.py 的文件计数（计数只看磁盘文件）。

## .nomedia.example

**位置**：`.nomedia.example`，内容一行：`/storage/emulated/0/project/emo`

用途：Android 上把该行内容存为 `.nomedia` 文件（复制到目标目录），防止手机相册扫描 `emo/` 目录。带 `.example` 后缀的是模板，非生效文件。

## 环境变量

无。