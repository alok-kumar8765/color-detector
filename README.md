# 🎨 Webcam Color Detector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub Creator](https://img.shields.io/badge/GitHub-alok--kumar8765-lightgrey.svg)

A lightweight, real-time desktop application built with **Python**, **OpenCV**, and **Tkinter** that lets users detect, sample, and copy exact color codes (HEX and RGB) from physical objects using their webcam feed with a simple click.

---

## 📑 Table of Contents
1. [About the Project](#-about-the-project)
2. [Purpose & Use Cases](#-purpose--use-cases)
3. [Features](#-features)
4. [Project File Structure](#-project-file-structure)
5. [System Requirements](#-system-requirements)
6. [Installation & Setup](#-installation--setup)
7. [Data Flow Diagram (DFD)](#-data-flow-diagram-dfd)
8. [Data Architecture / Component Schema](#-data-architecture--component-schema)
9. [Pros & Cons](#-pros--cons)
10. [Limitations](#-limitations)
11. [Known Bugs & Vulnerabilities](#-known-bugs--vulnerabilities)
12. [Future Updates](#-future-updates)
13. [Contributing](#-contributing)
14. [Author & Acknowledgments](#-author--acknowledgments)

---

## 🎯 About the Project
The **Webcam Color Detector** bridges the physical and digital worlds by turning any standard webcam into a physical color picker. Whether you are matching paint, building a web UI palette, or studying computer vision, this tool provides instant color feedback without needing complex design software.

---

## 💡 Purpose & Use Cases
* **UI/UX Designers:** Instantly pick colors from physical objects or your environment for web and app mockups.
* **Developers & Hobbyists:** Learn how to integrate OpenCV video feeds with Tkinter graphical user interfaces.
* **Education:** Understand pixel matrix manipulation, RGB/HEX conversion, and mouse event handling in Python.

---

## ✨ Features
* **Real-Time Video Preview:** Live camera feed rendered smoothly inside a custom Tkinter window using `PIL` and `OpenCV`.
* **Click-to-Sample:** Click anywhere on the video feed to instantly isolate and inspect that specific pixel's color.
* **Live Color Breakdown:** Displays real-time **HEX code**, **RGB values**, and an **approximated Color Name**.
* **Visual Color Preview Box:** Dynamically updates a preview pane matching the selected color with intelligent text contrast.
* **One-Click Copy:** Easily copy the detected HEX code straight to your system clipboard.

---

## 📂 Project File Structure

```text
color-detector/
│
├── color_detector.py       # Main application script
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

```

---

## ⚙️ System Requirements

* **OS:** Windows 10/11, macOS, or Linux
* **Python:** Version 3.8 or higher
* **Hardware:** A working built-in or USB webcam

---

## 📦 Installation & Setup

1. **Clone the Repository:**
```bash
git clone [https://github.com/alok--kumar8765/color-detector.py.git](https://github.com/alok--kumar8765/color-detector.git)
cd color-detector

```


2. **Create a Virtual Environment (Optional but Recommended):**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```


3. **Install Dependencies:**
```bash
pip install opencv-python pillow numpy

```


4. **Run the Application:**
```bash
python color_detector

```



---

## 📊 Data Flow Diagram (DFD)

```text
 [ Webcam Feed ] 
        │
        ▼ (Captured via cv2.VideoCapture)
 [ Frame Matrix (BGR) ]
        │
        ├─────────────────────────────┐
        ▼                             ▼
 [ Horizontal Flip & Resize ]   [ Mouse Click Event ]
        │                             │
        ▼                             ▼
 [ Tkinter GUI Display ]        [ Pixel Coordinate Mapping ]
        │                             │
        └───────────────────► [ Extract RGB Values ]
                                      │
                                      ▼
                              [ Convert to HEX & Name ]
                                      │
                                      ▼
                              [ Update UI Elements ]

```

---

## 🗂️ Data Architecture / Component Schema

```text
+---------------------------------------------------------------+
|                      ColorDetectorApp                         |
+---------------------------------------------------------------+
| - cap: cv2.VideoCapture                                       |
| - current_rgb: tuple (R, G, B)                                |
| - current_hex: string (#RRGGBB)                               |
| - current_color_name: string                                  |
| - latest_frame: numpy array                                   |
+---------------------------------------------------------------+
| + update_frame() ---> Refreshes video stream every 15ms       |
| + pick_color_on_click() -> Maps widget click to pixel matrix  |
| + get_color_name() -> Evaluates RGB thresholds for naming     |
| + copy_hex() -------> Copies HEX string to system clipboard   |
+---------------------------------------------------------------+

```

---

## ⚖️ Pros & Cons

### **Pros:**

* Lightweight and responsive with zero heavy external UI frameworks.
* Standalone script that runs locally without internet connectivity or API keys.
* Interactive point-and-click color sampling mechanism.

### **Cons:**

* Highly susceptible to ambient room lighting and shadows.
* Webcam auto-white-balance can occasionally skew true color representation.

---

## ⚠️ Limitations

* Sampling is done on a single pixel click rather than an averaged spatial bounding box, making it sensitive to pixel noise or tiny surface reflections.
* Color naming relies on hardcoded threshold logic rather than comprehensive machine learning color spaces (e.g., CIELAB delta-E).

---

## 🐛 Known Bugs & Vulnerabilities

* **Uint8 Underflow Warnings:** In older versions, subtracting unsigned 8-bit integers during color distance checks could trigger scalar subtraction overflow warnings (resolved by explicit integer casting).
* **Webcam Indexing:** If multiple webcams or virtual cameras (like OBS Virtual Camera) are connected, `cv2.VideoCapture(0)` might occasionally bind to the wrong device.

---

## 🚀 Future Updates

* [ ] Add a **Color History Log** to save previously picked colors in a session table.
* [ ] Implement **Palette Export** (export saved colors directly to a JSON or CSV file).
* [ ] Integrate **CIELAB Color Delta-E matching** for highly accurate color naming based on standard color dictionaries.
* [ ] Add a slider to adjust sample area size (e.g., 3x3 or 5x5 pixel averaging).

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## ⭐ Support & Star the Repo

If you found this project helpful or interesting, please consider giving it a ⭐ on GitHub! It helps motivate future development.

---

## 👤 Author & Connect

**Alok Kumar**

* GitHub: [@alok--kumar8765](https://www.google.com/search?q=https://github.com/alok--kumar8765)

---

*Built with ❤️ using Python, OpenCV, and Tkinter.*
