个人表情包库

项目结构：

- EMO/: 主文件夹，包含各类表情包。
- EMO/emoCut.py: 用于切割图片的表情包生成工具。
- EMO/README.md: 项目说明文档。
- EMO/requirements.txt: 项目所需依赖库信息。

使用说明：

1. 若要使用[EweSticker](https://github.com/FredHappyface/Android.EweSticker)，请在应用中将 emo 文件夹设为贴纸文件夹。
2. emoCut.py 是一个图片切割工具，位于 EMO/emoCut.py 文件中，可以将大图切割成小图，生成表情包。使用方法见文件内注释。
3. 表情包库中的所有文件均来源于网络。

依赖库：

- pillow==12.0.0: 用于图像处理的 Python 库。
