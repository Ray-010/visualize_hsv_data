import glob
import torch
import cv2

yolov5_path = "../yolov5/yolov5"
weight_path = "./traffic_light_1.pt"
model = torch.hub.load(yolov5_path, "custom", path=weight_path, source="local")

images_file = glob.glob("./images/red/*.jpg")
for i, file in enumerate(images_file):
    img = cv2.imread(file)
    img_copy = img.copy()
    results = model(img)
    df = results.pandas().xyxy[0]

    if "traffic_light" in df.values:
        df_traffic_light = df.query(('name=="traffic_light"'))
        df_traffic_light_list = df_traffic_light.reset_index().values.tolist()
        for coordinates in df_traffic_light_list:
            xmin, ymin, xmax, ymax = int(coordinates[1]), int(coordinates[2]), int(coordinates[3]), int(coordinates[4])
            # [top:bottom, left:right]
            print(xmin, ymin, xmax, ymax)
            detected_img = img_copy[ymin:ymax, xmin:xmax]
            
            # 保存
            cv2.imwrite(f"./images/traffic_lights_red/traffic_light_red_{i}.jpg", detected_img)



