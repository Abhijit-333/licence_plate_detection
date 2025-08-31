import tkinter as tk
from recorder import record_video
from controller import run_detection

def run_app():
    root = tk.Tk()
    root.configure(background="gold")

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("License Plate Detection")

    lbl = tk.Label(root, text="License Plate Recognition System",
                   font=('times', 25, 'bold'), bg="gold", fg="black")
    lbl.place(x=430, y=5)

    frame_alpr = tk.LabelFrame(root, text=" Detection Process ",
                               width=280, height=500, bd=3,
                               font=('times', 15, 'bold'), bg="gold")
    frame_alpr.place(x=5, y=50)

    def on_exit():
        root.destroy()

    button1 = tk.Button(frame_alpr, text="Record",
                        command=record_video,
                        width=20, height=1,
                        font=('Times New Roman', 15, 'italic'),
                        bg="black", fg="white")
    button1.place(x=10, y=40)

    button2 = tk.Button(frame_alpr, text="Detection",
                        command=run_detection,
                        width=20, height=1,
                        font=('Times New Roman', 15, 'italic'),
                        bg="black", fg="white")
    button2.place(x=10, y=120)

    exit_btn = tk.Button(frame_alpr, text="Exit",
                         command=on_exit,
                         width=20, height=1,
                         font=('Times New Roman', 15, 'italic'),
                         bg="red", fg="white")
    exit_btn.place(x=10, y=200)

    root.mainloop()
