# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:31:50 2018

@author: praneeth
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import os
import random

from wordcloud import WordCloud, STOPWORDS

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# read the mask image
mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))

text = open(path.join(d, 'comments.txt')).read()

# stopwords declaration
stopwords = set(STOPWORDS)

wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)

# default colored image
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")

#save image to a file
wc.to_file("sample3.png")
plt.axis("off")
plt.figure()