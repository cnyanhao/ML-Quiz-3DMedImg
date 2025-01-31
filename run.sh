# python prepare_nnunet.py
# pip install nibabel
# python clean_labels.py
# nnUNetv2_plan_and_preprocess -d 101 --verify_dataset_integrity -pl nnUNetPlannerResEncM
# nnUNetv2_train 101 3d_fullres 0 -p nnUNetResEncUNetMPlans
nnUNetv2_predict \
    -i ./nnUNetData/nnUNet_raw/Dataset101_Pancreas/imagesTs \
    -o ./nnUNetData/nnUNet_results/Dataset101_Pancreas/nnUNetTrainer__nnUNetResEncUNetMPlans__3d_fullres/fold_0/test \
    -d 101 \
    -p nnUNetResEncUNetMPlans \
    -chk checkpoint_best.pth \
    -c 3d_fullres \
    -f 0
