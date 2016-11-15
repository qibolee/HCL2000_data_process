from PIL import Image
from pylab import *

im = array(Image.open("a.JPG"))

print im.shape,im.dtype
print im

im1 = im[:,:,0]
print im1.shape

imshow(im1)
show()
