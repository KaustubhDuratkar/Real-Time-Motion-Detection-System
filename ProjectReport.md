# 📄 Project Report: Real-Time Motion Detection 

**Student Name:** Kaustubh Duratkar
**Registration Number:** 25BAI10592
**Program:** B.Tech CSE (AI & ML)
**University:** VIT Bhopal University

---

## 1. Abstract

Modern security systems require continuous monitoring, which is both time-consuming and inefficient when performed manually. This project addresses the problem by developing a Real-Time Motion Detection & Alert System using Python and computer vision techniques. The system utilizes a webcam feed to detect motion dynamically and triggers an alert mechanism, such as visual indicators and alarm sounds. Built using Python and OpenCV, the application processes live video frames using image differencing and contour detection algorithms to provide efficient and real-time monitoring.

---

## 2. Introduction & Problem Statement

With increasing concerns about safety and surveillance, there is a need for automated systems that can monitor environments without human intervention. Traditional CCTV systems require constant observation, leading to inefficiency and fatigue.

The objective of this project was to design a smart motion detection system that:

* Continuously analyzes video input
* Detects motion in real-time
* Alerts users instantly upon detecting activity

By using image processing techniques, the system filters out unnecessary information and focuses only on significant motion events, improving efficiency and usability.

---

## 3. Technologies Used

* Programming Language: Python 3
* Computer Vision Library: OpenCV (cv2)
* Numerical Computation: NumPy
* Audio Alert System: Playsound module
* Development Environment: Spyder / VS Code
* Version Control: Git & GitHub

---

## 4. System Architecture & Methodology

The application is structured into multiple components:

### 4.1 Video Capture & Frame Processing

The system uses the device’s webcam to capture continuous video frames. Two consecutive frames are stored and compared to detect motion.

* Frames are resized for performance optimization
* Converted to grayscale to reduce computational complexity
* Gaussian blur is applied to remove noise

---

### 4.2 Motion Detection Algorithm

The core logic is based on frame differencing:

* Absolute difference between consecutive frames is calculated
* Thresholding is applied to highlight motion regions
* Morphological operations (dilation and erosion) improve detection accuracy

Contours are then extracted from the processed frame:

* Small contours are ignored to eliminate noise
* Significant contours indicate motion

---

### 4.3 Alert & Visualization System

Once motion is detected:

* Bounding boxes are drawn around moving objects
* Status text ("Motion Detected") is displayed
* An alarm sound is triggered using multithreading to avoid freezing

Additional features:

* Real-time FPS display
* Timestamp overlay
* Sensitivity adjustment using trackbars

---

## 5. Challenges & Technical Learnings

During the development of this project, several challenges were encountered:

* Environment Setup Issues: Faced issues with installing Python libraries and configuring pip. Learned how to manage environment variables and dependencies.

* Real-Time Processing Optimization: Initial implementation was slow and noisy. Improved performance using resizing and Gaussian blur.

* False Motion Detection: Minor pixel variations triggered false alerts. Solved using contour area filtering and morphological operations.

* Multithreading for Alarm: Playing sound blocked the video feed. Implemented threading to ensure smooth execution.

* IDE Limitations: Spyder had issues displaying OpenCV windows. Learned to configure backend settings and manage execution environments.

---

## 6. Conclusion

This project successfully demonstrates the application of computer vision in real-time surveillance systems. By combining OpenCV with Python, an efficient motion detection system was developed that provides immediate visual and audio feedback.

The project strengthened understanding of:

* Image processing techniques
* Real-time system design
* Algorithm optimization
* Practical debugging and deployment

As a B.Tech CSE (AI & ML) student, this project enhances interdisciplinary skills that can be applied in artificial intelligence, robotics, automation, smart surveillance systems, and industrial monitoring.

---

## 7. Future Scope

* Integration with AI-based human detection
* Cloud-based alert system (email/SMS notifications)
* Mobile app integration
* Face recognition for smart security
* IoT-based smart home surveillance

---
