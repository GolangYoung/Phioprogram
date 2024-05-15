# from ultralytics import YOLO


# if '__name__' == "main":
#     # Load a model
#     model = YOLO('yolov8n.yaml')  # build a new model from YAML
#     model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
#     model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

#     # Train the model
#     results = model.train(data='coco8.yaml', epochs=100, imgsz=640)
import sys
import argparse
import os

sys.path.append(r'C:\Users\llj\Desktop\Pistachio\ultralytics')

from ultralytics import YOLO
import os

if __name__ == '__main__':

    os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
    # Load a model
    model = YOLO('CBAM.yaml')  # build a new model from YAML
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
    model = YOLO('CBAM.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

    # Train the model
    results = model.train(data='set.yaml', epochs=100, imgsz=640,device=0)