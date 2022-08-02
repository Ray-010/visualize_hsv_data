import cv2
import csv
import numpy as np


img = cv2.imread("./images/a_pedestrian_light_image4.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
save_hsv_path = "./data/hsv_data.csv"
csv_file = np.loadtxt(save_hsv_path)

def main():
    # img_width = img.shape[1]
    # # for i in range(img_width):
    data = img_hsv[0][0:5]

    print(data[0][0])
    data = np.vstack((csv_file, data))
    print(data[0][0])

    np.savetxt(save_hsv_path, data, fmt="%d")


if __name__ == "__main__":
    main()



