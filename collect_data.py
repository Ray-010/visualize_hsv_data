# データ集計
import csv
import matplotlib.pyplot as plt
import numpy as np


"""
HSV範囲
H: 0-179
S: 0-255
V: 0-255
"""
hue = [0]*180
saturation = [0]*255
value = [0]*255
csv_data_path = "./data/hsv_data.csv"

csv_file = open(csv_data_path)

for row in csv.reader(csv_file):
    hue[int(row[0])] += 1

x_pos = np.arange(180)

print(hue)

plt.bar(x_pos, hue)
plt.show()
