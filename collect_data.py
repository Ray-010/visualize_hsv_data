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
red_hue = [0]*180
red_saturation = [0]*256
red_value = [0]*256
green_hue = [0]*180
green_saturation = [0]*256
green_value = [0]*256

csv_red_data_path = "./data/hsv_red_data.csv"
csv_red_file = open(csv_red_data_path)
csv_green_data_path = "./data/hsv_green_data.csv"
csv_green_file = open(csv_green_data_path)

# Red
for row in csv.reader(csv_red_file):
    red_hue[int(row[0])] += 1
    red_saturation[int(row[1])] += 1
    red_value[int(row[2])] += 1
# Green
for row in csv.reader(csv_green_file):
    green_hue[int(row[0])] += 1
    green_saturation[int(row[1])] += 1
    green_value[int(row[2])] += 1

hue_x = np.arange(180)
sat_x = np.arange(256)
val_x = np.arange(256)

# Hue
fig1 = plt.figure()
plt.xlabel("Hue")
plt.ylabel("Number")
plt.bar(hue_x, red_hue, label="red", width=1.0, alpha=0.5, color="r")
plt.bar(hue_x, green_hue, label="green", width=1.0, alpha=0.5, color="g")
plt.legend()
fig1.savefig("results/both_results/hue_result.jpg")
plt.show()

# Saturation
fig2 = plt.figure()
plt.xlabel("Saturation")
plt.ylabel("Number")
plt.bar(sat_x, red_saturation, label="red", width=1.0, alpha=0.5, color="r")
plt.bar(sat_x, green_saturation, label="green", width=1.0, alpha=0.5, color="g")
plt.legend()
fig2.savefig("results/both_results/saturation_result.jpg")
plt.show()

# Value
fig3 = plt.figure()
plt.xlabel("Value")
plt.ylabel("Number")
plt.bar(val_x, red_value, label="red", width=1.0, alpha=0.5, color="r")
plt.bar(val_x, green_value, label="green", width=1.0, alpha=0.5, color="g")
plt.legend()
fig3.savefig("results/both_results/value_result.jpg")
plt.show()
