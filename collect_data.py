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
saturation = [0]*256
value = [0]*256
csv_data_path = "./data/hsv_data.csv"
csv_file = open(csv_data_path)

for row in csv.reader(csv_file):
    hue[int(row[0])] += 1
    saturation[int(row[1])] += 1
    value[int(row[2])] += 1

row = 1 # グラフの行数
col = 3 # グラフの列数

hue_x = np.arange(180)
sat_x = np.arange(256)
val_x = np.arange(256)

print(hue)
print(saturation)
print(value)
fig = plt.figure()

ax1 = fig.add_subplot(1, 3 ,1)
ax2 = fig.add_subplot(1, 3 ,2)
ax3 = fig.add_subplot(1, 3 ,3)

ax1.bar(hue_x, hue)
ax2.bar(sat_x, saturation)
ax3.bar(val_x, value)

fig.tight_layout()
fig.savefig("results/result.jpg")
plt.show()
