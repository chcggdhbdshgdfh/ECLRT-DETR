import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/rt-detr/ECLRT-DETR1.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=4,
                workers=4,
                device='0',
                # resume='/home/baby/STQ/RTDETR-20240926/RTDETR-main/runs/train/exp4/weights/last.pt', # last.pt path
                project='runs/train',
                name='exp',
                )