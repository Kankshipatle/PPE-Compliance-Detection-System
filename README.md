# 🛡️ PPE Compliance Detection System
### AI-Based Smart Access Control for Food Processing Environments

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-ff6b35?style=flat-square)](https://ultralytics.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b?style=flat-square&logo=streamlit)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 📌 Problem Statement

In large kitchens and food-processing facilities, workers are required to wear mandatory hygiene PPE — gloves, face masks, and hairnets — before entering restricted work areas. Manual PPE checking is slow, inconsistent, and prone to human error.

This system automates PPE compliance verification using live camera footage and enforces smart access control decisions in real time.

---

## 🎯 Solution

An end-to-end AI pipeline that:
- Detects PPE items (gloves, mask, hairnet) using a custom-trained YOLOv8s model
- Evaluates compliance and grants or denies access based on detection results
- Displays real-time results through a professional Streamlit web interface
- Maintains a timestamped access log for audit purposes

---

## 🖥️ Demo

| ACCESS ALLOWED | ACCESS DENIED |
|---|---|
| 2 or more PPE items detected ✅ | Fewer than 2 PPE items detected ❌ |

---

## 🔧 Tech Stack

| Component | Technology |
|---|---|
| Object Detection | YOLOv8s (Ultralytics) |
| Deep Learning | PyTorch |
| Computer Vision | OpenCV |
| Web Interface | Streamlit |
| Language | Python 3.10+ |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
ppe-compliance-detection/
│
├── app.py                  # Streamlit web application
├── detect.py               # Webcam detection script (standalone)
├── test_image.py           # Image testing script
├── ppe_best_v2.pt          # Trained YOLOv8s model weights
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| Precision | 85.2% |
| Recall | 83.3% |
| **mAP50** | **87.6%** |
| mAP50-95 | 64.0% |

**Training Details:**
- Model: YOLOv8s
- Dataset: ~7,000 images (custom merged dataset)
- Classes: Gloves, Mask, Hairnet
- Epochs: 50
- Training Platform: Google Colab (T4 GPU)

---

## 📦 Dataset

Custom dataset compiled and cleaned from multiple sources:

| Class | Samples |
|---|---|
| Gloves | 3,308 |
| Mask | 3,487 |
| Hairnet | 1,071 |
| **Total** | **~7,000** |

Dataset pipeline included multi-source merging, label format conversion (segmentation → detection), class ID remapping, and train/val splitting.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/kankshipatle/ppe-compliance-detection.git
cd ppe-compliance-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python -m streamlit run app.py
```

---

## 📋 Requirements

```
ultralytics
streamlit
opencv-python
torch
Pillow
numpy
```

---

## ⚙️ How It Works

```
Worker enters camera area
        ↓
Live camera / uploaded image captured
        ↓
YOLOv8s model detects PPE items
        ↓
Decision logic evaluates compliance
  ├── 2 or 3 items detected → ✅ ACCESS ALLOWED
  └── 0 or 1 item detected  → ❌ ACCESS DENIED
        ↓
Result displayed + logged with timestamp
```

---

## 🔮 Future Improvements (v2 Roadmap)

- [ ] Expand hairnet dataset for improved detection accuracy
- [ ] Real-time video stream support
- [ ] Hardware integration (servo-based door lock / buzzer alert)
- [ ] Multi-person detection in single frame
- [ ] Alert notification system (email / SMS)
- [ ] Admin dashboard with access history analytics

---

## 👩‍💻 Author

**Kankshi Patle**  
[GitHub](https://github.com/kankshipatle) · [LinkedIn](https://linkedin.com/in/kankshipatle)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
