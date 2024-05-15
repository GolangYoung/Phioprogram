import csv
from collections import defaultdict
import os

os.makedirs("labels", exist_ok=True)
# 假设你的CSV文件名为 'data.csv'
input_csv_file = 'annotation.csv'
output_folder = './pis/labels/train'

# 读取图像尺寸，这里假设所有图像都是同样的尺寸，需要根据实际情况修改
image_width = 1070
image_height = 600

# 使用defaultdict来存储每张图片对应的标注数据
annotations = defaultdict(list)

with open(input_csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        filename, x_min, y_min, x_max, y_max, class_id = row
        x_min, y_min, x_max, y_max = map(int, [x_min, y_min, x_max, y_max])

        # 计算中心点坐标和宽高，并归一化
        x_center = (x_min + x_max) / 2 / image_width
        y_center = (y_min + y_max) / 2 / image_height
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height

        # 添加到annotations字典
        annotations[filename].append(f"{class_id} {x_center} {y_center} {width} {height}")

# 将annotations写入对应的.txt文件
import os

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename, boxes in annotations.items():
    base_filename = os.path.splitext(filename)[0]  # 移除文件扩展名
    output_filename = os.path.join(output_folder, f"{base_filename}.txt")
    with open(output_filename, 'w') as file:
        for box in boxes:
            file.write(box + '\n')