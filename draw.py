import tkinter as tk
import os
import sys


prev_x, prev_y = None, None


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def draw(event):
    global prev_x, prev_y
    x, y = event.x, event.y

    if prev_x and prev_y:
        canvas.create_line(prev_x, prev_y, x, y, fill="white", width=3)

    prev_x, prev_y = x, y


def release(event):
    global prev_x, prev_y
    prev_x, prev_y = None, None


def clear_canvas():
    canvas.delete("all")


def on_key_press(event):
    if event.keysym == "grave":  # Check for the ` key
        clear_canvas()


root = tk.Tk()
root.title(
    "~~~Draw on Black Sketch~~~ By Konafa "
)  # CC @Konafa DON"T TAKE IT AND RE POST !!!!@
root.geometry("1920x1080")  # Set window size to 1920x1080


root.iconbitmap(resource_path("./resources/icon/app.ico"))

canvas = tk.Canvas(root, bg="black", width=1920, height=1080)
canvas.pack()

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", release)
root.bind("<KeyPress>", on_key_press)

root.mainloop()
