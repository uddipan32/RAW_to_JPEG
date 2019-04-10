import numpy
import rawpy
import imageio
import cv2
raw_image = rawpy.imread('IMG.CR2')
img = raw_image.postprocess()
rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
print(rgb.shape)
cv2.imwrite('1.jpg',rgb, [cv2.IMWRITE_PNG_COMPRESSION, 0])
