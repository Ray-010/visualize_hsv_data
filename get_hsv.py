import cv2
import csv
import numpy as np
from csv import writer


img = cv2.imread("./images/a_pedestrian_light_image4.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
save_hsv_path = "./data/hsv_data.csv"
def main():
    img_height = img_hsv.shape[0]
    for i in range(img_height):
        data = img_hsv[i]
        with open(save_hsv_path, "a", newline="") as file:
            writer_obj = writer(file)
            writer_obj.writerows(data)

if __name__ == "__main__":
    main()
