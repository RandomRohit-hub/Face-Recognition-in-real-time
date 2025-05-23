
# Face Recognition in Real-Time

A Python-based application that performs real-time face recognition using OpenCV. This project captures live video from a webcam, detects faces, and recognizes them by comparing with known images.

## Features

* **Real-Time Face Detection**: Utilizes OpenCV's Haar Cascade classifiers to detect faces in live video streams.
* **Face Recognition**: Compares detected faces with known images using feature matching techniques.
* **Image Comparison**: Provides functionality to compare two images and determine if they contain the same person.

## Getting Started

### Prerequisites

* Python 3.x
* OpenCV
* NumPy

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/RandomRohit-hub/Face-Recognition-in-real-time.git
   cd Face-Recognition-in-real-time
   ```

2. **Install the required packages**:

   It's recommended to use a virtual environment.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install opencv-python numpy
   ```

## Usage

### 1. Real-Time Face Recognition

Run the `main.py` script to start the webcam and perform face recognition.

```bash
python main.py
```

* The script will access your webcam.
* Detected faces will be highlighted.
* If a face matches a known image, it will display the name.

### 2. Real-Time Face Recognition with Video

Run the `main_video.py` script to perform face recognition on a video file.

```bash
python main_video.py
```

* Modify the script to specify the path to your video file.
* The script will process the video and perform face recognition frame by frame.

### 3. Image Comparison

Use the `image_comparison.py` script to compare two images.

```bash
python image_comparison.py
```

* Modify the script to specify the paths to the two images you want to compare.
* The script will output whether the two images contain the same person.

## Project Structure

```
├── image_comparison.py      # Script to compare two images
├── main.py                  # Real-time face recognition using webcam
├── main_video.py            # Face recognition on a video file
├── messi.jpg                # Sample image of a known person
├── simple_facerec.py        # Module containing face recognition logic
└── README.md                # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

