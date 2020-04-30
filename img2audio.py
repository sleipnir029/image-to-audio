import wave, struct, math, itertools
from PIL import Image


# Extracting pixel data from the picture
img = Image.open('shadesofb&g.jpg')
pixels = list(img.getdata())
print(len(pixels))
width, height = img.size
fpixels = list(itertools.chain(*pixels))
print(len(fpixels))
print("*****Preparing*****")

"""
# Histogram of pixel values, used for custom note assignment
counts = {}
for i in fpixels:
    counts[i] = counts.get(i, 0) + 1
print(counts)
"""

# Distributing notes across pixel values
def notesDistribution(value):
    notes = [440.00, 493.88, 523.25, 587.33,
            659.25, 698.46, 783.99, 880.00,
            987.77, 1046.50, 1174.66, 1318.51,
            1396.91, 1567.98, 1760.00]
    
    if value <= 17:
        l = notes[0]
        r = notes[7]
    elif value > 17 and value <= 34:
        l = notes[1]
        r = notes[8]
    elif value > 34 and value <= 51:
        l = notes[3]
        r = notes[10]
    elif value > 51 and value <= 68:
        l = notes[4]
        r = notes[11]
    elif value > 68 and value <= 85:
        l = notes[5]
        r = notes[12]
    elif value > 85 and value <= 102:
        l = notes[6]
        r = notes[13]
    elif value > 102 and value <= 119:
        l = notes[7]
        r = notes[14]
    elif value > 119 and value <= 136:
        l = notes[8]
        r = notes[1]
    elif value > 136 and value <= 153:
        l = notes[9]
        r = notes[2]
    elif value > 153 and value <= 170:
        l = notes[10]
        r = notes[3]
    elif value > 170 and value <= 187:
        l = notes[11]
        r = notes[4]
    elif value > 187 and value <= 204:
        l = notes[12]
        r = notes[5]
    elif value > 204 and value <= 221:
        l = notes[13]
        r = notes[6]
    elif value > 221 and value <= 238:
        l = notes[14]
        r = notes[7]
    elif value > 238:
        l = notes[0]
        r = notes[7]
    return l, r


# Generating left and right channel frequencies
lFreq = []
rFreq = []
for i in fpixels:
    l, r = notesDistribution(i)
    lFreq.append(l)
    rFreq.append(r)


# Audio settings
sampleRate = 44100.00
duration = int(len(fpixels) / sampleRate)

fwave = wave.open('test_sound.wav', 'w')
fwave.setnchannels(2)           # 1-mono, 2-stereo
fwave.setsampwidth(2)           # 1-8bitInt, 2-16biInt, 4-32bitInt
fwave.setframerate(sampleRate)


# Creating the audio file
for i in range(len(fpixels)):
    lc = int(32767.0 * math.cos(lFreq[i]*math.pi*float(i) / float(sampleRate)))
    rc = int(32767.0 * math.cos(rFreq[i]*math.pi*float(i) / float(sampleRate)))
    fwave.writeframesraw(struct.pack('<hh', lc, rc))
fwave.close()
print("=====Done======")