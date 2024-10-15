import os
import shutil

# 定义原始数据集路径和目标提取路径
source_dir = '/root/autodl-tmp/vimeo_septuplet/sequences/'  # 替换为 Vimeo-90k 数据集的路径
target_dir = '/root/autodl-tmp/train'  # 替换为提取后图像的目标文件夹路径

# 如果目标文件夹不存在，创建该文件夹
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 遍历所有子文件夹和图像文件
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.png'):  # 确保只处理 PNG 图像
            # 获取文件的完整路径
            file_path = os.path.join(root, file)
            
            # 提取文件夹路径信息，用于重命名
            relative_path = os.path.relpath(root, source_dir)
            folder_name = relative_path.replace(os.sep, '_')  # 替换路径分隔符为下划线
            
            # 生成新的文件名：文件夹路径_文件名
            new_file_name = f"{folder_name}_{file}"
            
            # 目标文件的完整路径
            target_path = os.path.join(target_dir, new_file_name)
            
            # 移动并重命名图像
            shutil.move(file_path, target_path)

print(f"所有图像已成功移动并重命名到文件夹 {target_dir} 中。")
