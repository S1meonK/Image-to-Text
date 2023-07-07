import cv2
import pytesseract
from tkinter import Tk, Text, messagebox, Button
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image

# Set the tesseract path in the script
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def drop(event):
    filepath = event.data
    if filepath.endswith('.png') or filepath.endswith('.jpg') or filepath.endswith('.jpeg'):
        image_to_text(filepath)
    else:
        messagebox.showerror("Error", "Please drop only image files!")

def image_to_text(filepath):
    # Load the image from path
    img = cv2.imread(filepath)
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OCR
    text = pytesseract.image_to_string(gray)

    # Insert the text to textbox
    textbox.insert("end", text)

def clear_text():
    textbox.delete('1.0', 'end')

root = TkinterDnD.Tk()
root.title("Image to Text")
root.geometry('600x400')

# Define textbox
textbox = Text(root, wrap='word', width=50, height=15)
textbox.pack(padx=10, pady=10)

# Define Clear button
clear_button = Button(root, text='Clear', command=clear_text, width=14, height=3)
clear_button.pack(pady=10)

# Define Exit button
exit_button = Button(root, text='Exit', command=root.destroy, width=14, height=3)
exit_button.pack(pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
