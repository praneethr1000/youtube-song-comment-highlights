# -*- coding: utf-8 -*-
"""
@author: praneeth
"""

import os

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'comments.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:

import matplotlib.pyplot as plt
wordcloud = WordCloud(max_font_size=30).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
wordcloud.to_file("sample2.png")
plt.show()

