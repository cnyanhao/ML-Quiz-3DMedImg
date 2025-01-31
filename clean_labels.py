import glob
import nibabel as nib
import numpy as np
from tqdm import tqdm


labelsTr = 'nnUNetData/nnUNet_raw/Dataset101_Pancreas/labelsTr'
train_labels = glob.glob(labelsTr + '/*')

for label in tqdm(train_labels):
    # convert data into int64
    img = nib.load(label)
    data = img.get_fdata().astype(np.int64)
    # save the data
    img = nib.Nifti1Image(data, img.affine, img.header)
    nib.save(img, label)
