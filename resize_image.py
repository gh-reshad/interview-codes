from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = np.array(Image.open(r'C:\Users\100689998\Dropbox\GhazalReshad&Mehran\result_GC\4-1-2020_Images\Image_ID_8\8.tif'))

res = cv2.resize(image, dsize=(256,256), interpolation=cv2.INTER_CUBIC)

cv2.imwrite(r'C:\Users\100689998\Dropbox\GhazalReshad&Mehran\result_GC\4-1-2020_Images\Image_ID_8\mask.tif', res)

plt.imshow(res)
plt.axis('off')

plt.show()