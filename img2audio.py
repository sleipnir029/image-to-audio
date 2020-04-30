import wave, struct, math, itertools
from PIL import Image


# Extracting pixel data from the picture
img = Image.open('shadesofb&g.jpg')
pixels = list(img.getdata())
print(len(pixels))
width, height = img.size
fpixels = list(itertools.chain(*pixels))
print(len(fpixels))


# Histogram of pixel values, used for custom note assignment
counts = {}
for i in fpixels:
    counts[i] = counts.get(i, 0) + 1
print(counts)