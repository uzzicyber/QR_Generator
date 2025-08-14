import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import os

# Function to generate QR Code


def generate_qr(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    filename = "qr_code.png"
    img.save(filename)
    return filename


# Function to save QR Code


def save_qr(filename):

    filepath = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG Images", "*.png")]
    )

    if filepath:
        os.rename(filename, filepath)
        messagebox.showinfo("QR Code Saved!")


# Function to create window and elements


def create_window():

    window = tk.Tk()
    window.title("QR Code Generator")

    label = tk.Label(window, text="Enter the text/URL:")
    label.pack()

    ent = tk.Entry(window)
    ent.pack()

    canvas = tk.Canvas(window, width=200, height=200)
    canvas.pack()

    def generate_and_display():
        text = ent.get()
        filename = generate_qr(text)
        photo = ImageTk.PhotoImage(Image.open(filename))
        canvas.create_image(100, 100, image=photo)
        button2 = tk.Button(
            window, text="Save QR Code", command=lambda: save_qr(filename)
        )
        button2.pack()
        window.mainloop()

    button = tk.Button(window, text="Generate QR Code", command=generate_and_display)
    button.pack()

    window.mainloop()


if __name__ == "__main__":

    create_window()

    generate_qr("Hello World!")
