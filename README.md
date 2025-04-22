# 🧥 Invisibility Cloak using Python & OpenCV

Inspired by the magical world of Harry Potter, this fun computer vision project simulates an **invisibility cloak** using Python and OpenCV. By detecting a specific colored cloth (like red or green), the program captures the background and replaces the cloth with that background in real-time — creating the illusion of invisibility!

---

## 📌 Project Overview

This project leverages computer vision techniques to:
- Detect a specific color in a video frame (cloth).
- Replace the detected color area with a previously captured background.
- Create the illusion of a person disappearing under the cloak.

It uses **HSV color space**, **image masking**, and **real-time video processing** to achieve the effect.

---

## 🎯 Features

- ✅ Real-time video processing using OpenCV.
- 🎨 Custom color detection for the cloak (e.g., red, green).
- 🎛️ Live HSV tuning tool for accurate color detection.
- 📹 Option to record video with the invisibility effect.
- 🧪 Distance-based detection experimentation for improved accuracy.

---

## 🛠️ Getting Started

### 🔧 Prerequisites

- Python 3.x
- OpenCV
- NumPy

### 📦 Installation

```bash
git clone https://github.com/yourusername/invisibility-cloak-opencv.git
cd invisibility-cloak-opencv
pip install -r requirements.txt
