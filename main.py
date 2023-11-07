import cv2
import numpy as np
import serial
import time

# Load YOLOv4 model and configuration
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Initialize other variables
img2 = cv2.imread("red.jpg")
img3 = cv2.imread("green.jpg")
img4 = cv2.imread("yellow.jpg")
img3 = cv2.resize(img3, (200, 200))
img2 = cv2.resize(img2, (200, 200))
img4 = cv2.resize(img4, (200, 200))
ard_srl = serial.Serial('com6', 9600)
carCnt = 0

def CheckEntranceLineCrossing(y, x):
    if abs(x) < abs(y):
        return 1
    else:
        return 0

def detectCount(vid):
    img = cv.VideoCapture(vid)

    while img.isOpened():
        ret, frame = img.read()
        if ret == False:
            print('No Video Found!!')
            break
        else:
            frame1 = cv2.resize(frame, (900, 400))
            try:
                width = np.size(frame1, 1)
            except IndexError:
                pass

            # Use YOLOv4 to detect vehicles
            blob = cv2.dnn.blobFromImage(frame1, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            class_ids = []
            confidences = []
            boxes = []

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * 400)
                        w = int(detection[2] * width)
                        h = int(detection[3] * 400)

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 255), 2)

            # Your existing code here

            # Update carCnt based on YOLO detections
            carCnt = len(boxes)

            if (carCnt >= 0 and carCnt <= 5):
                ard_srl.write('0')
                cv2.destroyWindow('REDsignal')
                cv2.imshow('GREENsignal', img3)
            elif (carCnt >= 6 and carCnt <= 9):
                ard_srl.write('1')
                cv2.destroyWindow('GREENsignal')
                cv2.imshow('YELLOWsignal', img4)
            elif (carCnt == 10):
                ard_srl.write('2')
                cv2.destroyWindow('YELLOWsignal')
                cv2.imshow('REDsignal', img2)
            elif (carCnt > 10):
                time.sleep(10)
                carCnt = 0

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    sbb = "Total counted car: "
    print(sbb, carCnt)
    img.release()  # destroys capture object
    cv2.destroyAllWindows()  # destroys all windows