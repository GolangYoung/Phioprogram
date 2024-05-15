import csv
import os

# Define the CSV file path and the output directory path
csv_file = 'annotation.csv'
output_dir = 'yolo_annotations'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the CSV file
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    annotations = [row for row in reader]

# Create a dictionary to store the annotations for each image
image_annotations = {}

# Iterate over each annotation
for annotation in annotations:
    # Extract the image path, class, and bounding box coordinates
    image_path, x_min, y_min, x_max, y_max, class_index = annotation

    # Get the image name without the extension
    image_name = image_path.split('.')[0]

    # Calculate the bounding box coordinates in YOLO format
    x_center = (float(x_min) + float(x_max)) / 2 / 1024  # assuming 1024 is the image width
    y_center = (float(y_min) + float(y_max)) / 2 / 768  # assuming 768 is the image height
    w = (float(x_max) - float(x_min)) / 1024
    h = (float(y_max) - float(y_min)) / 768

    # Add the annotation to the dictionary
    if image_name not in image_annotations:
        image_annotations[image_name] = []
    image_annotations[image_name].append(f'{class_index} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n')

# Write the annotations to the corresponding.txt file for each image
for image_name, annotations in image_annotations.items():
    with open(os.path.join(output_dir, f'{image_name}.txt'), 'w') as f:
        f.writelines(annotations)