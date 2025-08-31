

# 🚗🔍 Licence Plate Detection with OCR

This project demonstrates a **computer vision pipeline** for detecting and recognizing license plates from video input.  
It combines **OpenCV** for image processing, **OCR** (Google Vision or Tesseract) for text extraction, and an **SQLite database** for storing results.  

The project is extensible, ideal for learning, research, or as a base for production-grade traffic monitoring systems.  

---

# 📂 Project Structure
- `src/` → Source code (main app, OCR, frame extraction, etc.)
- `data/` → Stores frames + SQLite demo DB
- `keys/` → API keys (not uploaded to GitHub)
- `requirements.txt` → Python dependencies

---

## ⚙️ Setup Instructions
```bash
# Create environment
conda create -n lpd python=3.10 -y
conda activate lpd

# Install dependencies
pip install -r requirements.txt

🚀 Running the App
python src/main.py

📊 Database Structure
The SQLite DB (INFO.db) contains a demo schema like detected license plates and related details.
Use src/setup_db.py to reset or customize the schema.

🔒 Note on Keys

API keys (keys/vision_keys.json) are excluded for security.
Add your own OCR API credentials there in JSON format.

---

🤝 Contributing &  📜 License 

MIT License. You are free to use, modify, and distribute with attribution. PRs and suggestions are welcome! Feel free to fork this repo and build on it :)

---
