# Real-Time-Motion-Detection-System
This project is a Real-Time Motion Detection System using Python and OpenCV. It detects movement by comparing consecutive video frames from a webcam. The system highlights motion and displays results in real-time for surveillance use.
## 📌 Project Overview

This project is a Real-Time Motion Detection System developed using Python and OpenCV. It uses a webcam to capture live video and detects motion by comparing consecutive frames. The system applies image processing techniques such as grayscale conversion, Gaussian blur, thresholding, and contour detection to accurately identify movement.

Once motion is detected, the system highlights the moving region using bounding boxes and displays the motion status on the screen in real-time. This project demonstrates a practical implementation of computer vision for surveillance and monitoring applications, and serves as a foundation for building more advanced security systems.

---

## 🚀 Key Features

* Real-time motion detection using live webcam feed
* Frame differencing technique for accurate detection
* Image preprocessing using grayscale and Gaussian blur
* Noise reduction using thresholding and morphological operations
* Contour detection for identifying moving objects
* Highlights motion using bounding boxes
* Displays motion status dynamically
* Lightweight and efficient real-time performance
* Simple and user-friendly implementation

---

## ⚙️ Installation

1. Install Python (3.10 or above recommended)
2. Clone the repository or download the project files
3. Install required libraries:

```bash
pip install opencv-python numpy
```

---

## ▶️ How to Run

1. Open terminal/command prompt in the project folder
2. Run the Python file:

```bash
python motion_detector.py
```

3. Webcam will open and start detecting motion
4. Press **ESC** to exit the application

---
