# 💸 Advanced Tip Calculator

A modern web application that helps you **accurately calculate tips**, split bills, and **generate shareable outputs** like **PDF receipts** and **images**. Built with **Flask**, **HTML/CSS**, and **Python libraries** for export capabilities.

---

## 📸 Live Demo

🌐 [Visit Live App](https://your-deployment-link.com)  
🧑‍💻 [GitHub Repository](https://github.com/DarshanSKReddy/AdvancedTipCalculator)

---

## 📌 Features

- ✅ **User-friendly interface** with modern UI
- 📊 **Custom tip percentage** input
- 👥 **Bill splitting** for multiple people
- 🧾 **Export as PDF** (optional image export with `wkhtmltoimage`)
- 💾 **Downloadable output**
- ⚙️ Built using **Flask backend** + **Bootstrap frontend**

---

## 🖼️ Screenshots

| 💻 Calculator UI | 📤 PDF Output |
|------------------|---------------|
| ![screenshot1](screenshots/ui.png) | ![screenshot2](screenshots/pdf_output.png) |

---

## 🚀 Getting Started (Local Setup)

### 🔧 Prerequisites

- Python 3.8+
- Flask
- reportlab
- (Optional) imgkit + wkhtmltoimage

### 🛠️ Installation

```bash
git clone https://github.com/DarshanSKReddy/AdvancedTipCalculator.git
cd AdvancedTipCalculator
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt

