# DormGuardNet: A Lightweight Deep Learning Model for Detecting Prohibited Items in Student Dormitory Environments

This repository contains the dataset and source code associated with the paper:

> **Jahid, Imrul, A. A. M. Muzahid, Reda Lamtoueh, Sayed Jobaer, Nazratun Naim Neha, Hua Han, Yujin Zhang, and Ferdous Sohel, "DormGuardNet: A Lightweight Deep Learning Model for Detecting Prohibited Items in Student Dormitory Environments," 2025 17th International Conference on Computer and Automation Engineering (ICCAE), Perth, Australia, 2025, pp. 104-109, doi: [10.1109/ICCAE64891.2025.10980592](https://doi.org/10.1109/ICCAE64891.2025.10980592).**

## Overview

DormGuardNet is a lightweight deep learning model designed to detect prohibited items in student dormitories. It is implemented within the YOLO framework and achieves state-of-the-art performance in this domain. The dataset used in the paper is specially curated for this task and is provided here for research purposes.

## Getting Started

### Prerequisites

1. Clone the YOLOv5 repository:
   ```bash
   git clone https://github.com/ultralytics/yolov5
   cd yolov5
 ```bash
2. Copy the following files and folders from this repository into the YOLOv5 directory:

Dataset/
run.py
Dormguard.yaml
dormguard-pretrained200.pt


3. Install the required libraries using the YOLOv5 requirements.txt file:
 ```bash
pip install -r requirements.txt
 ```bash

4. Usage
Training the Model with Pretrained Weights. Run the following command to fine-tune the model with pretrained weights:

 ```bash
python train.py --img 640 --batch 24 --epochs 100 --data ../Dataset/data.yaml --cfg Dormguard.yaml --weights dormguard-pretrained200 --name dormguard_results
 ```bash

>>Training the Model from Scratch. To train the model without pretrained weights, use the following command:

 ```bash
python train.py --img 640 --batch 24 --epochs 100 --data ../Dataset/data.yaml --cfg Dormguard.yaml --name dormguard_results

 ```bash

>>Using a Bash Script for Batch Training
Create a file named run_scripts.sh and add multiple training commands as follows:
#!/bin/bash
python train.py --img 640 --batch 300 --epochs 200 --data /media/user/yolov5-master/Dataset/data.yaml --cfg Dormguard.yaml --weights dormguard-pretrained200 --name > output.txt > /Run_report/pretrained_200.txt
python train.py --img 640 --batch 300 --epochs 400 --data /media/user/yolov5-master/Dataset/data.yaml --cfg Dormguard.yaml --weights dormguard-pretrained200 --name > output.txt > /Run_report/pretrained_400.txt
python train.py --img 640 --batch 300 --epochs 200 --data /media/user/yolov5-master/Dataset/data.yaml --cfg Dormguard.yaml --name > output.txt > /Run_report/pretrained_400.txt

>>Run the script on command line to execute all commands:
 ```bash
./run_scripts.sh
 ```bash

Citation
If you use our dataset or source code in your research, please cite our paper as follows:
Jahid, Imrul, A. A. M. Muzahid, Reda Lamtoueh, Sayed Jobaer, Nazratun Naim Neha, Hua Han, Yujin Zhang, and Ferdous Sohel, 
"DormGuardNet: A Lightweight Deep Learning Model for Detecting Prohibited Items in Student Dormitory Environments," 
2025 17th International Conference on Computer and Automation Engineering (ICCAE), Perth, Australia, 2025, pp. 104-109, 
doi: 10.1109/ICCAE64891.2025.10980592.
