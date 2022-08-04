import cv2
import glob
from csv import writer


images_file = glob.glob("./images/red_only/*.jpg")
save_hsv_path = "./data/hsv_red_data.csv"

def main():
    for file in images_file:
        img = cv2.imread(file)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_height = img_hsv.shape[0]
        for i in range(img_height):
            data = img_hsv[i]
            with open(save_hsv_path, "a", newline="") as file:
                writer_obj = writer(file)
                writer_obj.writerows(data)

if __name__ == "__main__":
    main()
