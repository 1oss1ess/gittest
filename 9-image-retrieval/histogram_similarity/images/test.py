from PIL import Image
import math
import numpy as np

def normalize(hist):
    hist_np = np.array(hist, dtype=np.float)
    hist_sum = sum(hist)
    hist_norm = hist_np / hist_sum
    return hist_norm.tolist()

image1 = Image.open('1.jpeg').resize((500, 325))
image2 = Image.open('2.jpeg')
image3 = Image.open('4.jpeg')

image1_hist = normalize(image1.histogram())
image2_hist = normalize(image2.histogram())
image3_hist = normalize(image3.histogram())

def distance(hist1, hist2):
    dist = 0.0
    for a, b in zip(hist1, hist2):
        dist += (a - b) * (a - b)

        return math.sqrt(dist)

    image12_dist = distance(image1_hist, image2_hist)
    image23_dist = distance(image2_hist, image3_hist)
    image13_dist = distance(image1_hist, image3_hist)

    print(image12_dist)
    print(image23_dist)
    print(image13_dist)
