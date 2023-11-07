# Automatic-Vehicle-Detection-For-Traffic-Analysis-Using-Image-Processing-Machine-Learning
This project was done during my final year thesis. This project employs OpenCV, YOLOv4, and Arduino Uno in order to construct a system for traffic analysis that detects vehicles from prerecorded videos or real time. OpenCV is utilized by the system to perform image processing and machine learning operations, whereas YOLOv4 is employed to ensure precise vehicle detection. The system operates on Arduino Uno, an inexpensive and multifunctional microcontroller board, which grants it accessibility to a broad spectrum of users. It is used tc control three LEDs (Green, Yellow & Red) to indicate the presence of vehicles just like traffic light in real life.

This project includes some features related to image processing and machine learning

### Image processing:

Image resizing: Images are resized to 640x640 pixels prior to being input into the YOLO Version 4 model. This is implemented in order to enhance the model's efficacy.
Color conversion: Prior to feeding the YOLO Version 4 model the converted images from the BGR to RGB color space, OpenCV is utilized to resize and convert the images. In order to train YOLO Version 4, which utilizes RGB images, it is critical to transform the images into RGB color space prior to inputting them into the model.
Here, it is important to mention that OpenCV is used to display the video stream from the webcam or video file.

### Machine learning:

Object detection: Vehicles are detected in the images utilizing the YOLO Version 4 model. The YOLO Version 4 is a deep learning model that was trained using an extensive dataset comprising vehicle images. The model is capable of accurately and in real time detecting vehicles.
In addition to these features, the project also uses other machine learning techniques, such as:

Data augmentation: The training dataset is augmented using various techniques, such as random cropping, flipping, and rotating the images. This contributes to the enhancement of the YOLO Version 4 model's generalizability.
Transfer learning: The YOLO Version 4 model is pre-trained on a dataset of images of various objects, such as cars, trucks, buses, and motorcycles. This contributes to the enhancement of the model's efficacy in the task of vehicle detection.

The following are several prospective uses of the system:

Traffic monitoring: The system is capable of monitoring highways and routes for traffic conditions. By utilizing this data, obstruction can be decreased and traffic flow can be enhanced.

Counting vehicles: The system is capable of measuring the quantity of vehicles that traverse a specific location. Planning transportation infrastructure and estimating traffic volume are both possible applications of this data.

Identification of vehicles: The system is capable of real-time vehicle identification. This data may be utilized for surveillance and security purposes.










