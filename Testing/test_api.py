import requests
import cv2

image_path = "images/UltraEleven050.jpg"


def draw_result(img, list_bbox):
    img = cv2.imread(img)
    for bbox in list_bbox:
        img = cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 0, 255), thickness=2)

    cv2.namedWindow("my image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("my image", width=700, height=500)
    cv2.imshow("my image", img)
    cv2.waitKey()


resp = requests.post("http://localhost:5000/inference",
                     files={"file": open(image_path, 'rb')})

new_bbox = resp.json()["bbox"]
draw_result(img=image_path, list_bbox=new_bbox)
