# ECLRT-DETR
Code in “Lightweight and Real-Time Detection Transformer with Enhanced Cross-Scale Fusion for SAR Object Detection”
Synthetic aperture radar (SAR) images pose significant challenges for object detection due to their complex backgrounds, mul-ti-scale targets, and numerous small targets. Addressing these issues, this paper proposes ECLRT-DETR, a lightweight real-time detection transformer based on enhanced cross-scale fusion specifically designed for multi-class SAR object detection.

## Contents

* [dependencies and requirements](#dependencies-and-requirements)
* [descriptions and implementations of key algorithms](#descriptions-and-implementations-of-key-algorithms)
* [Data Preparing](#Data-Preparing)
* [How to train](#How-to-train)
* [Visualization](#Visualization)
* [How to view results](#How-to-view-results)
* [How to get datasets (which are mentioned in our paper)](#How-to-get-datasets (which are mentioned in our paper))


## dependencies and requirements

Create a new python virtual environment by [Anaconda](https://www.anaconda.com/) or just use pip in your python environment and then clone this repository as following.

Our experimental environment:
python: 3.8.16
torch: 1.13.1+cu117
torchvision: 0.14.1+cu117
timm: 0.9.8
mmcv: 2.1.0
mmengine: 0.9.0
The GPU is NVIDIA GeForce GTX 3090, with the Linux server operating system. The training batch size is set to 8 for 100 training epochs.

 Additional required package installation commands.
   ```
    pip install timm==0.9.8 thop efficientnet_pytorch==0.7.1 einops grad-cam==1.4.8 dill==0.3.6 albumentations==1.3.1 pytorch_wavelets==1.3.0 tidecv PyWavelets -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install -U openmim
    mim install mmengine
    mim install "mmcv>=2.0.0
   ```
## descriptions and implementations of key algorithms

### 1. Wavelet Transform Convolution (WT-Conv)

Description:
Wavelet Transform Convolution (WT-Conv) is an innovative convolution technique that combines wavelet transforms with convolution operations to enhance their effectiveness. Traditional convolution operations have a limited receptive field, which restricts their ability to capture long-range dependencies. WT-Conv effectively extends the receptive field by integrating wavelet transforms, enabling the model to capture more low-frequency information. Low-frequency components are particularly useful for tasks that involve detecting small or low-resolution targets, as they provide important contextual details that may be missed by conventional convolutions.

Implementation:
WT-Conv replaces conventional convolution layers in backbone networks with wavelet transform-based convolutions, enhancing the capture of low-frequency information.
The method applies convolution filters at different scales, transforming the image in a way that extends the receptive field and allows the network to handle more complex and variable environments.
Key implementation details include selecting appropriate wavelet bases and defining the scales for the transformations to maximize the lightweight and performance characteristics of the model.

### 2. Enhanced Cross-Scale Encoder (ECSE) and SPD-Conv

Description:
The Enhanced Cross-Scale Encoder (ECSE) integrates SPD-Conv (Spatially Adaptive Convolution) to process features from the P2 layer and fuse them with features from the P3 layer. Unlike traditional methods where P2 features are directly added to the detection layer, ECSE effectively retains small target information through enhanced feature fusion. This results in better recognition of small targets by the network.

Implementation:
SPD-Conv: SPD-Conv is a convolution method that adapts to spatial position features, dynamically weighting different regions of the input feature map based on local context. This improves feature processing at various scales.
Feature Fusion: ECSE processes the P2 features using SPD-Conv and applies similar processing to P3 features, followed by a cross-scale fusion that maximizes the utilization of small target features.
DFFM and CSPOK: These two modules further enhance cross-scale feature fusion. DFFM (Deep Feature Fusion Module) combines features from multiple scales, while CSPOK (Small-Target Fusion Module) specializes in refining the detection of small targets, improving both feature extraction and fusion.

### 3. PN-Loss Loss Function

Description:
PN-Loss is a novel loss function that combines the advantages of Powerful-IoU loss (PIoU) and Normalized Wasserstein Distance (NWD) loss. PIoU is used to adjust anchor box quality gradients, while NWD loss focuses on measuring the similarity between small targets. The combination of these two loss functions allows PN-Loss to accelerate model convergence and improve accuracy, particularly for small target detection tasks.

Implementation:
PIoU: PIoU loss optimizes the anchor boxes by considering the Intersection over Union (IoU) between predicted and ground-truth boxes. It adds an extra gradient adjustment mechanism for improving box localization accuracy.
NWD: NWD loss is focused on measuring the similarity between small targets using Wasserstein distance, which is particularly beneficial when targets are small and have subtle differences.
PN-Loss: The PN-Loss function combines PIoU and NWD losses with a weighted strategy, providing a more efficient and robust loss function that accelerates convergence while improving small target detection accuracy.

The main improvement code path is `./ultralytics/nn/extra_modules/block.py`

## Data Preparing

This implementation uses joint dataset and MSAR datasets for trainin.

### Training Dataset

**Step 1**: Download the [datasets](https://pan.baidu.com/s/1QaZSznz89Yj90UcBBgomjA?pwd=6rwx ).

**Step 2**: Extract them into `./dataset/ship_plane__ssdd_hrsid_saraircraft` and `./dataset/MSAR` respectively.

## How to train

Directly run the train.py file in the project, before running, you need to change the yaml file path of the model`./dataset/data.yaml`  and the dataset configuration yaml file path`./ultralytics/cfg/models/rt-detr/ECLRT-DETR1.yaml`

## Visualization

The first column shows the ground truth annotations, the second column shows the prediction results of YOLOv8, and the third column shows the prediction results of ECLRT-DETR.ECLRT-DETR performs well across the four target types. We analyzed two near-shore scenes in ship detection, charac-terized by noise and detection challenges. The ECLRT-DETR model demonstrated higher confidence, while YOLOv8 ex-hibited comparatively lower confidence in target detection. In the complex aircraft detection scenario, both methods demonstrated strong performance; however, the ECLRT-DETR model exhibited greater confidence. Bridge detection is straightforward, and both methods can accurately determine bridge locations with high confidence. ECLRT-DETR outperforms YOLOv8 in tank detection, ex-hibiting higher confidence even in scenarios with compact target arrangements and detection challenges.

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

## If our work is helpful to you, please help cite our work
```
@article{ECLRT-DETR,
  title={Lightweight and Real-Time Detection Transformer with Enhanced Cross-Scale Fusion for SAR Object Detection},
  author={Tanqing Sun, Xianjun Zhang, Ziyu Li, Mingjia Wang, Na You and Yuping Feng},
  journal={The Visual Computer},
  pages={1--13},
  year={2024},
  publisher={Springer}
}
```

## Others

**If you have any concerns or questions, please contact us at 19861109610@163.com**

If the paper is fortunate enough to be accepted, we will optimize the code into a more mature and stable version.

