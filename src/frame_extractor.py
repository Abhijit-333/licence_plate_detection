import cv2
import os
import shutil

def video_to_frames(video_path, output_folder):
    # Clear old frames
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    i = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(output_folder, f"frame{i}.png"), frame)
        i += 1
    cap.release()
    cv2.destroyAllWindows()
    print(f"✅ Extracted {i-1} frames into {output_folder}")
