# python prepare_nnunet.py
# pip install nibabel
# python clean_labels.py
# nnUNetv2_plan_and_preprocess -d 101 --verify_dataset_integrity -pl nnUNetPlannerResEncM
nnUNetv2_train 101 3d_fullres 0 -p nnUNetResEncUNetMPlans