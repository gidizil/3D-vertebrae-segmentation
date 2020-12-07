import SimpleITK as sitk
import os
import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np

imgs_dir_path = '/Users/gzilbar/msc/courses/medical_dl/project/vertebrae/xVertSeg/xVertSeg.v1/Data2/images'
img_name = 'image022.mhd'
img = io.imread(os.path.join(imgs_dir_path, img_name), plugin='simpleitk')

# See some data - one image:
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img[:, :, 512], cmap='gray')
ax.set_aspect(2000/280)
ax.set_title('Sagittal - Slice 512')
plt.show()

# See multiple Images
fig, ax = plt.subplots(nrows=1, ncols=5)
for i in range(5):
    ax[i].imshow(img[:, :, 450 + 50*i], cmap='gray')
    ax[i].set_aspect(3000/280)
    ax[i].set_title('Slice {}'.format(450 + 50*i))
fig.suptitle('Saggital View')
plt.tight_layout()
plt.show()

