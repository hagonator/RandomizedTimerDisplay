import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

H = 256
W = 256
BACK_COLOR = 'black'
PROG_COLOR = 'white'
N = 1000

bias = np.arange(H*W).reshape(H, W) % W / W
noise = 0.25 * np.random.randn(H*W).reshape(H, W)
random_weights = bias + noise

flat_weights = random_weights.flatten()
flat_order = flat_weights.argsort()
for i in range(1, N):
    j = flat_order[(i*H*W) // 1000]
    weight = flat_weights[j]
    im = random_weights > weight
    
    Image.fromarray(im).save(f"p_bar/{i:03d}_prog.jpg")
