# AI-Powered_FaceRecognition_and_ExcelReporting
My python project is based on identifying familiar faces in group photos, generating roll number-packed Excel sheets for seamless organization.

## Overview

- Train a set of face images with their corresponding roll numbers.
- Recognize faces in a group photo based on the trained data.
- Generate an Excel sheet containing the roll numbers of the recognized faces.

## Features

- User-friendly UI for easy interaction.
- Efficient face recognition using advanced algorithms.
- Excel reporting for organized results.
- Extensive compatibility with various image formats.
- Simple setup and usage instructions.

## Getting Started

### Prerequisites and instructions

- Python 3.7 or 3.8 required | check this using this command in cmd: "python --version"

## libraries and software components needed

**open-cv python library**
    - Helps with image and video processing, including tasks like loading images, editing, and detecting objects.
    - install this library using cmd, with this code: 
    **pip install opencv-python**
    - Verify using IDLE (can be found in startmenu) with this code: (output must be the version of the library):
    import cv2
    print(cv2.__version__)
   
    
- ******openpyxl library******
    - It helps read, write, and modify Excel spreadsheets.
    - In this program, it's used to save recognized roll numbers in an Excel file.
    - open cmd as admin>`py -m pip install openpyxl` use the code> type py and import openpyxl> if you do not get any errors, the library has installed perfectly.
    
- **CMake**
    - It helps developers build and organize their code on different types of computers without too much hassle.
- **Dlib**
    - It can find faces, figure out who they belong to, and even tell you where the eyes, nose, and mouth are on a face.
- **Visual Studio C++**
    - Go to [Visual Studio C++](https://visualstudio.microsoft.com/vs/features/cplusplus/) and download the installer, when installing check the development with C++ box and let it install.
    - It is required for creating a Dlib build without any errors
- **face_recognition library**
    - Specifically designed for face detection and recognition in images. It finds faces and can even identify who they belong to.
    - Create a new folder>name it> open cmd> iterate into this folder path using cd
    - Install face_recognition lib using this command in cmd: pip install face_recognition

## Usage

Change this`"your directory path here"`to your group pics folder path
Change this `r"folder path here"`  to your training images folder path
Run train_faces.py and wait for the training to finish, now you will get a encodings.pickle file in the same dir.
Run recognize_faces.py to browse and select a group photo and generate the Excel report.
Excel report will be stored in the same dir as encodings.pickle

## Directory Structure
recognize_faces.py: Main script for recognizing faces in a group photo.
train_faces.py: Script for training face images and creating encodings.
requirements.txt: List of required Python packages.
roll numbers/: Folder name containing roll number data with face photos for training.
group pics/: Folder containing group photos for recognition.

## Contributing
Contributions are welcome! If you'd like to contribute to the project, feel free to fork the repository and submit pull requests.
