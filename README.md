# 🧚 Pixie-Trixie

### Image Encryption & Decryption Tool • Python GUI

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Pillow](https://img.shields.io/badge/Library-Pillow-orange?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Pixel%20Scrambling-cyan?style=for-the-badge)

---

## 📖 Overview
**Pixie-Trixie** is a specialized cybersecurity utility developed during my internship at **Prodigy Infotech**. It provides a robust yet user-friendly way to secure image data through advanced pixel manipulation. By combining **Seeded Shuffling** and **Bitwise XOR operations**, it transforms any standard image into unreadable digital static.

## ✨ Key Features
* **Secure Pixel Scrambling:** Physically rearranges pixel coordinates based on a private key.
* **Dual-Layer Encryption:** Applies bitwise XOR color shifting in addition to spatial shuffling.
* **Zero Loss Decryption:** Uses lossless processing to ensure images are restored with 100% original quality.
* **Animated Terminal UI:** Features a centered, responsive dashboard with a winking "Pixie" guardian.
* **Cross-Platform GUI:** Integrated file dialogs for easy image and folder selection.

## 🛠️ How It Works

| Step | Action | Logic / Formula |
| :--- | :--- | :--- |
| **01** | **Load Matrix** | Image is converted into a raw RGB pixel array. |
| **02** | **Seeded Shuffle** | `random.seed(key)` ensures the shuffle is unique but reproducible. |
| **03** | **XOR Shift** | Every pixel value $P$ is transformed: $P' = P \oplus (key \pmod{255})$. |
| **04** | **Coordinate Swap** | Pixels are moved to new indices based on the generated seed. |
| **05** | **Export** | The resulting "noise" image is saved as a lossless `.png`. |

## 🚀 Installation & Usage

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/noufal-ns/PRODIGY_CS_02.git](https://github.com/noufal-ns/PRODIGY_CS_02.git)
    cd PRODIGY_CS_02
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch Pixie-Trixie:**
    ```bash
    python pixie-trixie.py
    ```

## 📜 Developer Credits
* **Developer:** Noufal N S
* **Task:** Prodigy Infotech Cybersecurity Internship - Task 02

---
*Pixie-Trixie: Making your art invisible to the prying eyes.*
