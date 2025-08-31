import cv2
import time
from frame_extractor import video_to_frames

def record_video(output_path="data/sample_video.avi", duration=4):
    cap = cv2.VideoCapture(0)

    out = cv2.VideoWriter(output_path,
        cv2.VideoWriter_fourcc(*'MJPG'), 30., (640, 480))

    start = time.time()
    end = time.time()

    while end - start < duration:
        end = time.time()
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        out.write(frame.astype('uint8'))

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    video_to_frames(output_path, "data/frames")
