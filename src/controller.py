import os
import tkinter as tk
from ocr import detect_text
from database import query_plate

def run_detection():
    frames_path = "data/frames"
    if not os.path.exists(frames_path):
        print("❌ No frames found. Please record first.")
        return

    files = sorted(os.listdir(frames_path))[:15]

    for f in files:
        plate = detect_text(os.path.join(frames_path, f))
        if not plate:
            continue

        plate = plate[:10]  # limit length
        result = query_plate(plate)

        if len(result) > 0:
            msg = f"{plate} → {result}"
            print("✅ Match:", msg)
            tk.Label(text=msg, width=50, height=2,
                     font=('Times New Roman', 18, 'italic'),
                     bg="gold", fg="black").place(x=350, y=510)

            # Example: Serial trigger (disabled by default)
            # import serial
            # ser = serial.Serial(port='COM6', baudrate=9600,
            #     parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
            #     bytesize=serial.EIGHTBITS, timeout=1)
            # ser.write("A".encode())
            break
        else:
            msg = "Number Plate Not Matched with Database"
            print("❌", msg)
            tk.Label(text=msg, width=50, height=2,
                     font=('Times New Roman', 18, 'italic'),
                     bg="gold", fg="black").place(x=350, y=510)
