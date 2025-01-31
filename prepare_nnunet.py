import glob
import shutil
import os
import json

# images end with _0000.nii.gz
train_images = glob.glob('data/train/*/*_0000.nii.gz')
train_labels = [img.replace('_0000.nii.gz', '.nii.gz') for img in train_images]

val_images = glob.glob('data/validation/*/*_0000.nii.gz')
val_labels = [img.replace('_0000.nii.gz', '.nii.gz') for img in val_images]

test_images = glob.glob('data/test/*_0000.nii.gz')

imagesTr = 'nnUNetData/nnUNet_raw/Dataset101_Pancreas/imagesTr'
labelsTr = 'nnUNetData/nnUNet_raw/Dataset101_Pancreas/labelsTr'
imagesTs = 'nnUNetData/nnUNet_raw/Dataset101_Pancreas/imagesTs'

for folder in [imagesTr, labelsTr, imagesTs]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# move images and labels
for img in train_images:
    shutil.copy2(img, imagesTr)

for img in val_images:
    shutil.copy2(img, imagesTr)

for label in train_labels:
    shutil.copy2(label, labelsTr)

for label in val_labels:
    shutil.copy2(label, labelsTr)

for img in test_images:
    shutil.copy2(img, imagesTs)

print(len(glob.glob(imagesTr + '/*')))
print(len(glob.glob(labelsTr + '/*')))
print(len(glob.glob(imagesTs + '/*')))

# create splits_final.json
train_images.sort()
val_images.sort()
train_image_id = [os.path.basename(img).replace('_0000.nii.gz', '') for img in train_images]
val_image_id = [os.path.basename(img).replace('_0000.nii.gz', '') for img in val_images]

splits = []
splits.append({'train': train_image_id, 'val': val_image_id})

with open('splits_final.json', 'w') as f:
    json.dump(splits, f, indent=4)
