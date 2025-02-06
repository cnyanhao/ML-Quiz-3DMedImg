
# Deep Learning for Automatic Cancer Segmentation and Classification in 3D CT Scans

This repository is my implementation of ML-Quiz-3DMedImg. 

## Environments and Requirements

- Ubuntu 24.04
- Intel i5-11600K, 32GB RAM, RTX 3090
- CUDA 12.4
- python 3.12

1. (Optional) Create a conda environment:
    ```bash
    conda create -n nnunet python=3.12
    conda activate nnunet
    ```

2. Install modified nnUNet:
    ```bash
    cd nnUNet
    pip install -e .
    cd ..
    ```

3. Install modified dynamic-network-architectures:
    ```bash
    cd dynamic-network-architectures
    pip install -e .
    cd ..
    ```

4. Install nibabel for label cleaning:
    ```bash
    pip install nibabel
    ```

5. Set environment variables. Add the following to `.bashrc` file:
    ```bash
    export nnUNet_raw="~/Projects/ML-Quiz-3DMedImg/nnUNetData/nnUNet_raw"
    export nnUNet_preprocessed="~/Projects/ML-Quiz-3DMedImg/nnUNetData/nnUNet_preprocessed"
    export nnUNet_results="~/Projects/ML-Quiz-3DMedImg/nnUNetData/nnUNet_results"
    ```

## Dataset

1. Organize data as follows

    ```
    data/
    ├── test
    ├── train
    └── validation
    ```

2. Run the following script to prepare data for nnUNet training and generate train/validation split file named `splits_final.json`
    ```bash
    python prepare_nnunet.py
    ```

3. Create a new file named `dataset.json` under the folder `nnUNetData/nnUNet_raw/Dataset101_Pancreas` with the following content:
    ```json
    {
        "channel_names": {
            "0": "CT"
        }, 
        "labels": {
            "background": 0,
            "pancreas": [1, 2],
            "lesion": 2
        },
        "regions_class_order": [1, 2],
        "numTraining": 288,
        "file_ending": ".nii.gz"
    }
    ```

4. As the provided label file contains labels with float numbers (e.g. 1.000005), run the following script to clean the labels
    ```bash
    python clean_labels.py
    ```

## Preprocessing

1. Preprocess the data using the nnUNet provided command
    ```bash
    nnUNetv2_plan_and_preprocess -d 101 --verify_dataset_integrity -pl nnUNetPlannerResEncM
    ```

2. Copy the previously generated `splits_final.json` file to the folder `nnUNetData/nnUNet_preprocessed/Dataset101_Pancreas`

## Training and Evaluation

1. To train the model, run this command:

    ```bash
    nnUNetv2_train 101 3d_fullres 0 -p nnUNetResEncUNetMPlans
    ```

2. To evaluate the trained model on the evaluation set, run this command:
    ```bash
    nnUNetv2_train 101 3d_fullres 0 -p nnUNetResEncUNetMPlans --val
    ```

## Results

We achieve the following performance on the provided ML-Quiz-3DMedImg data

1. Segmentation
    ```json
    "mean": {
        "(1, 2)": {
            "Dice": 0.9190607778603967,
            ...
        },
        "2": {
            "Dice": 0.6168275198643545,
            ...
        }
    }
    ```

2. Classification

    ```json
    Yayy! New best F1 macro: 0.4909
    ```

## Inference

1. Run the following command to conduct inference on the test set
    ```bash
    nnUNetv2_predict \
        -i ./nnUNetData/nnUNet_raw/Dataset101_Pancreas/imagesTs \
        -o ./nnUNetData/nnUNet_results/Dataset101_Pancreas/nnUNetTrainer__nnUNetResEncUNetMPlans__3d_fullres/fold_0/test \
        -d 101 \
        -p nnUNetResEncUNetMPlans \
        -chk checkpoint_best.pth \
        -c 3d_fullres \
        -f 0
    ```
