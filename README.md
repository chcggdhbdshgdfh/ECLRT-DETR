# ECLRT-DETR
Code in “Lightweight and Real-Time Detection Transformer with Enhanced Cross-Scale Fusion for SAR Object Detection”

## Contents

* [How to setup](#How-to-setup)
* [Data Preparing](#Data-Preparing)
* [How to train](#How-to-train)
* [Visualization](#Visualization)
* [How to view results](#How-to-view-results)
* [How to get datasets (which are mentioned in our paper)](#How-to-get-datasets (which are mentioned in our paper))


## How to setup

Our experimental environment relies on the PyCharm 2021 build, and the deep learning framework consists of PyTorch 1.13.1 and CUDA 11.7. The GPU is NVIDIA GeForce GTX 3090, with the Linux server operating system. The training batch size is set to 8 for 100 training epochs.

 Additional required package installation commands.
   ```
    pip install timm==0.9.8 thop efficientnet_pytorch==0.7.1 einops grad-cam==1.4.8 dill==0.3.6 albumentations==1.3.1 pytorch_wavelets==1.3.0 tidecv PyWavelets -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install -U openmim
    mim install mmengine
    mim install "mmcv>=2.0.0
   ```
## Data Preparing

This implementation uses joint dataset and MSAR datasets for trainin.

### Training Dataset

**Step 1**: Download the [datasets](https://pan.baidu.com/s/1QaZSznz89Yj90UcBBgomjA?pwd=6rwx ).

**Step 2**: Extract them into `./dataset/ship_plane__ssdd_hrsid_saraircraft` and `./dataset/MSAR` respectively.

## How to train

Directly run the train.py file in the project, before running, you need to change the yaml file path of the model and the dataset configuration yaml file path

## Visualization

The first column shows the ground truth annotations, the second column shows the prediction results of YOLOv8, and the third column shows the prediction results of ECLRT-DETR.

### Comparison of ship scene target detection
![Comparison of ship scene target detection](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/ship1.jpg)
![Comparison of ship scene target detection](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/ship2.jpg)
### Comparison of aircraft scene target detection
![Comparison of aircraft scene target detection](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/plane1.jpg)
![Comparison of aircraft scene target detection](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/plane2.jpg)
### Comparison of bridge scene target detection
![Comparison of bridge scene target detection](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/bridge1.jpg)
![Comparison of bridge scene target detection](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/bridge2.jpg)
### Comparison of target detection in tank scene
![Comparison of target detection in tank scene](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/oil%20tank1.jpg)
![Comparison of target detection in tank scene](https://github.com/chcggdhbdshgdfh/ECLRT-DETR/blob/master/Visualization/oil%20tank2.jpg)
## How to view results

After running the runs file will appear, view the visualisation as well as the training data in the runs file

## How to get datasets (which are mentioned in our paper)

datasets:The datasets can be obtained at https://pan.baidu.com/s/1QaZSznz89Yj90UcBBgomjA?pwd=6rwx

## Others

**If you have any concerns or questions, please contact us at 19861109610@163.com**

If the paper is fortunate enough to be accepted, we will optimize the code into a more mature and stable version.

