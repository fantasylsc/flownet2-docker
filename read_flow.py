import numpy as np
import os
from PIL import Image

f = open('0000000-flow.flo','rb')

header = f.read(4)
if header.decode("utf-8") != 'PIEH':
    raise Exception('Flow file header does not contain PIEH')

width = np.fromfile(f, np.int32, 1).squeeze()
# print(width)
height = np.fromfile(f, np.int32, 1).squeeze()
# print(height.shape)
flow = np.fromfile(f, np.float32, width * height * 2).reshape((height,width, 2))
f.close()
img = Image.fromarray(flow[:,:,0])
img2 = Image.fromarray(flow[:,:,1])
# img.save('my.png')
img.show()
img2.show()





