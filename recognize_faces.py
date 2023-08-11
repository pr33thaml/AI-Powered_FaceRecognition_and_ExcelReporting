import os
import face_recognition
import pickle
from openpyxl import Workbook
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import re

def process_image():
    # Step 1: Load Encodings and Roll Numbers
    with open("encodings.pickle", "rb") as f:
        data = pickle.load(f)
    known_face_encodings = data["encodings"]
    roll_numbers = data["roll_numbers"]

    # Step 2: Get Image File Name
    image_filename = image_entry.get()

    # Step 3: Specify the Fixed Directory Path
    directory_path = r"your directory path here"

    # Step 4: Get Image File Path
    image_path = os.path.join(directory_path, image_filename)

    # Step 5: Load and Identify Group Photo
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Step 6: Initialize Excel Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Face Recognition"
    ws.append(["Roll Number"])

    # Step 7: Process Detected Faces
    for face_encoding in face_encodings:
        roll_number_match = "Unknown"
        for i, known_encoding_list in enumerate(known_face_encodings):
            matches = face_recognition.compare_faces(known_encoding_list, face_encoding)
            if any(matches):
                roll_number_match = roll_numbers[i]
                break

        # Step 8: Add Data to Excel
        ws.append([roll_number_match])

    # Step 9: Save Excel File
    excel_file_path = "recognized_faces.xlsx"
    wb.save(excel_file_path)

    result_label.config(text=f"Recognition complete. Results saved to {excel_file_path}")

def validate_filename(filename):
    allowed_extensions = ['.jpg', '.jpeg', '.png']
    _, extension = os.path.splitext(filename)
    return extension.lower() in allowed_extensions

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if filename:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, os.path.basename(filename))

# Create UI
root = tk.Tk()
root.title("Face Recognition UI")

# Image Entry
image_label = ttk.Label(root, text="Select Image File:")
image_label.pack()
image_entry = ttk.Entry(root)
image_entry.pack()

# Browse Button
browse_button = ttk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Process Button
process_button = ttk.Button(root, text="Process Image", command=process_image)
process_button.pack()

# Result Label
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
