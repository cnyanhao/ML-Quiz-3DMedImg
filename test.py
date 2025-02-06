import nibabel as nib

# Path to the .nii.gz file
file_path = "nnUNetData/nnUNet_raw/Dataset101_Pancreas/imagesTs/quiz_037_0000.nii.gz"

# Load the NIfTI file
nii_img = nib.load(file_path)

# Get image shape (dimensions in voxels)
image_shape = nii_img.shape

# Get voxel size (spatial resolution in mm)
voxel_size = nii_img.header.get_zooms()

print(f"Image Shape (voxels): {image_shape}")
print(f"Voxel Size (mm): {voxel_size}")
