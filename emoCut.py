import os
from PIL import Image


def split_image(
    image_path, rows, cols, output_dir=None, overlap=0, keep_aspect_ratio=False
):
    """
    将图片切割成rows×cols个小图片

    Args:
        image_path (str): 输入图片路径
        rows (int): 行数（垂直方向切割数）
        cols (int): 列数（水平方向切割数）
        output_dir (str, optional): 输出目录
        overlap (int, optional): 重叠像素数，默认0
        keep_aspect_ratio (bool, optional): 是否保持小图宽高比，默认False
    """

    # 验证输入参数
    if not os.path.exists(image_path):
        print(f"错误：图片文件 '{image_path}' 不存在")
        return False

    if rows <= 0 or cols <= 0:
        print("错误：行数和列数必须大于0")
        return False

    if overlap < 0:
        print("错误：重叠像素数不能为负数")
        return False

    # 打开图片
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"无法打开图片：{e}")
        return False

    # 获取图片基本信息
    width, height = img.size
    img_format = img.format or "Unknown"
    print(f"原图信息：{width}×{height}像素，格式：{img_format}")
    print(f"切割方式：{rows}行×{cols}列")
    if overlap > 0:
        print(f"重叠像素：{overlap}像素")

    # 设置输出目录
    if output_dir is None:
        # 默认输出到输入图片同目录的split文件夹
        base_dir = os.path.dirname(image_path)
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_dir = os.path.join(base_dir, f"{base_name}_split_{rows}x{cols}")

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 计算每个小图片的尺寸
    if keep_aspect_ratio:
        # 保持原图宽高比
        tile_width = width // cols
        tile_height = height // rows
        aspect_ratio = width / height
        tile_height = int(tile_width / aspect_ratio)
        print(f"每个小图尺寸：{tile_width}×{tile_height}像素（保持宽高比）")
    else:
        # 平均切割
        tile_width = width // cols
        tile_height = height // rows
        print(f"每个小图尺寸：{tile_width}×{tile_height}像素")

    if tile_width <= 0 or tile_height <= 0:
        print(f"错误：图片太小，无法切割成{rows}×{cols}份")
        return False

    # 计算实际切割位置，考虑重叠
    actual_tile_width = tile_width + (2 * overlap if cols > 1 else 0)
    actual_tile_height = tile_height + (2 * overlap if rows > 1 else 0)

    # 开始切割
    count = 0
    for i in range(rows):
        for j in range(cols):
            # 计算当前小图片的位置（考虑重叠）
            if cols == 1:
                left = 0
                right = width
            else:
                left = max(0, j * tile_width - overlap)
                right = min(width, (j + 1) * tile_width + overlap)

            if rows == 1:
                upper = 0
                lower = height
            else:
                upper = max(0, i * tile_height - overlap)
                lower = min(height, (i + 1) * tile_height + overlap)

            # 切割图片
            tile = img.crop((left, upper, right, lower))

            # 生成文件名（使用行列索引）
            tile_name = f"tile_{i+1:03d}_{j+1:03d}_{right-left}x{lower-upper}.png"
            tile_path = os.path.join(output_dir, tile_name)

            # 保存小图片
            tile.save(tile_path, "PNG")
            count += 1

    print(f"切割完成！共生成{count}个小图片")
    print(f"输出目录：{output_dir}")

    # 生成预览信息文件
    info_file = os.path.join(output_dir, "info.txt")
    with open(info_file, 'w', encoding='utf-8') as f:
        f.write(f"原图信息:\n")
        f.write(f"  文件路径: {image_path}\n")
        f.write(f"  尺寸: {width}×{height}像素\n")
        f.write(f"  格式: {img_format}\n")
        f.write(f"\n切割参数:\n")
        f.write(f"  行数: {rows}\n")
        f.write(f"  列数: {cols}\n")
        f.write(f"  重叠像素: {overlap}\n")
        f.write(f"  保持宽高比: {keep_aspect_ratio}\n")
        f.write(f"  小图尺寸: {tile_width}×{tile_height}像素\n")
        f.write(f"  生成数量: {count}\n")

    return True


def get_image_preview(image_path):
    """获取图片预览信息"""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            format_info = img.format or "Unknown"
            mode_info = img.mode

            # 计算文件大小
            file_size = os.path.getsize(image_path)
            size_str = format_file_size(file_size)

            return {
                "尺寸": f"{width}×{height}像素",
                "格式": format_info,
                "色彩模式": mode_info,
                "文件大小": size_str,
            }
    except:
        return None


def format_file_size(size_in_bytes):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.1f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} TB"


def get_valid_input(prompt, input_type=int, min_val=None, max_val=None, default=None):
    """获取有效的用户输入"""
    while True:
        user_input = input(prompt).strip()

        # 如果允许默认值且用户输入为空
        if default is not None and user_input == "":
            return default

        try:
            # 转换输入类型
            if input_type == int:
                value = int(user_input)
            elif input_type == float:
                value = float(user_input)
            elif input_type == bool:
                value = user_input.lower() in ['y', 'yes', 'true', 't', '1']
            else:
                value = user_input

            # 检查最小值
            if min_val is not None and value < min_val:
                print(f"输入值不能小于{min_val}，请重新输入")
                continue

            # 检查最大值
            if max_val is not None and value > max_val:
                print(f"输入值不能大于{max_val}，请重新输入")
                continue

            return value
        except ValueError:
            print("输入无效，请重新输入")


def main():
    """主函数：处理用户交互"""

    print("=" * 60)
    print("图片切割工具 v2.0")
    print("功能：将图片平均切割成n×m个小图片")
    print("=" * 60)

    # 显示示例
    print("\n示例：")
    print("  输入图片: emoji.png (1000×1000像素)")
    print("  切割参数: 4行×3列")
    print("  结果: 生成12个小图片，每个约250×333像素")
    print()

    # 步骤1：选择图片
    while True:
        print("\n步骤1：选择图片文件")
        print("-" * 40)
        image_path = input("请输入图片文件路径：").strip('"').strip("'")

        if image_path.lower() in ['exit', 'quit', 'q']:
            print("退出程序")
            return

        # 检查文件是否存在
        if not os.path.exists(image_path):
            print(f"错误：文件 '{image_path}' 不存在")

            # 询问是否查看当前目录文件
            current_dir = os.getcwd()
            list_files = input(
                f"是否查看当前目录下的图片文件？({current_dir}) (y/n): "
            ).lower()
            if list_files == 'y':
                image_extensions = (
                    '.png',
                    '.jpg',
                    '.jpeg',
                    '.bmp',
                    '.gif',
                    '.tiff',
                    '.webp',
                )
                image_files = [
                    f
                    for f in os.listdir(current_dir)
                    if f.lower().endswith(image_extensions)
                ]

                if image_files:
                    print("当前目录下的图片文件：")
                    for i, file in enumerate(image_files[:10], 1):  # 只显示前10个
                        print(f"  {i}. {file}")
                    if len(image_files) > 10:
                        print(f"  ... 还有{len(image_files)-10}个文件")
                else:
                    print("当前目录没有图片文件")
            continue

        # 检查是否为图片文件
        if not image_path.lower().endswith(
            ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
        ):
            print("警告：文件可能不是图片格式")
            proceed = input("是否继续？(y/n): ").lower()
            if proceed != 'y':
                continue

        # 显示图片信息
        preview = get_image_preview(image_path)
        if preview:
            print("\n图片信息：")
            for key, value in preview.items():
                print(f"  {key}: {value}")

            confirm = input("\n使用这张图片？(y/n): ").lower()
            if confirm == 'y':
                break
        else:
            print("无法读取图片信息")

    # 步骤2：设置切割参数
    print("\n步骤2：设置切割参数")
    print("-" * 40)

    # 获取切割行数
    rows = get_valid_input(
        "请输入切割行数（垂直方向份数）: ",
        input_type=int,
        min_val=1,
        max_val=100,
        default=3,
    )

    # 获取切割列数
    cols = get_valid_input(
        "请输入切割列数（水平方向份数）: ",
        input_type=int,
        min_val=1,
        max_val=100,
        default=3,
    )

    # 可选功能：重叠像素
    use_overlap = input("\n是否设置重叠像素？(y/n) [默认: n]: ").lower()
    if use_overlap == 'y':
        overlap = get_valid_input(
            "请输入重叠像素数: ", input_type=int, min_val=0, max_val=100, default=10
        )
    else:
        overlap = 0

    # 可选功能：保持宽高比
    keep_aspect = input("\n是否保持小图的宽高比？(y/n) [默认: n]: ").lower()
    keep_aspect_ratio = keep_aspect == 'y'

    # 步骤3：设置输出目录
    print("\n步骤3：设置输出目录")
    print("-" * 40)
    default_output = None  # 使用默认目录
    custom_output = (
        input("请输入自定义输出目录（直接回车使用默认目录）: ").strip('"').strip("'")
    )

    if custom_output:
        # 检查目录是否存在，不存在则询问是否创建
        if not os.path.exists(custom_output):
            create_dir = input(
                f"目录 '{custom_output}' 不存在，是否创建？(y/n): "
            ).lower()
            if create_dir == 'y':
                try:
                    os.makedirs(custom_output, exist_ok=True)
                    output_dir = custom_output
                except Exception as e:
                    print(f"创建目录失败：{e}")
                    print("将使用默认目录")
                    output_dir = None
            else:
                print("将使用默认目录")
                output_dir = None
        else:
            output_dir = custom_output
    else:
        output_dir = None

    # 步骤4：确认设置
    print("\n步骤4：确认设置")
    print("-" * 40)
    print(f"图片路径: {image_path}")
    print(f"切割参数: {rows}行 × {cols}列")
    print(f"重叠像素: {overlap}")
    print(f"保持宽高比: {'是' if keep_aspect_ratio else '否'}")

    if output_dir:
        print(f"输出目录: {output_dir}")
    else:
        base_dir = os.path.dirname(image_path)
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        default_output_dir = os.path.join(base_dir, f"{base_name}_split_{rows}x{cols}")
        print(f"输出目录: {default_output_dir} (默认)")

    # 开始切割
    print("\n" + "=" * 60)
    confirm = input("确认开始切割？(y/n): ").lower()

    if confirm == 'y':
        print("\n开始切割图片...")
        success = split_image(
            image_path, rows, cols, output_dir, overlap, keep_aspect_ratio
        )

        if success:
            print("\nOK 切割完成！")
            print("=" * 60)

            # 询问是否打开输出目录
            open_dir = input("是否打开输出目录？(y/n): ").lower()
            if open_dir == 'y':
                try:
                    import subprocess
                    import platform

                    output_path = output_dir or os.path.join(
                        os.path.dirname(image_path),
                        f"{os.path.splitext(os.path.basename(image_path))[0]}_split_{rows}x{cols}",
                    )

                    # 根据操作系统打开目录
                    system = platform.system()
                    if system == "Windows":
                        os.startfile(output_path)
                    elif system == "Darwin":  # macOS
                        subprocess.Popen(["open", output_path])
                    else:  # Linux
                        subprocess.Popen(["xdg-open", output_path])

                except Exception as e:
                    print(f"无法打开目录：{e}")
        else:
            print("\n❌ 切割失败！")
    else:
        print("\n操作已取消")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n程序运行出错：{e}")
    finally:
        input("\n按回车键退出...")
