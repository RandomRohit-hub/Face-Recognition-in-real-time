import cv2
import face_recognition

# Load the image
img = cv2.imread("Messi1.webp")

# Check if image loaded correctly
if img is None:
    raise ValueError("Failed to load image. Check the file path and format.")

# If it has an alpha channel (4 channels), remove it
if img.shape[2] == 4:
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

# Convert BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get face encodings
encodings = face_recognition.face_encodings(rgb)

if encodings:
    img_encoding = encodings[0]
    print("Face encoding extracted successfully.")
else:
    print("No face found in the image.")

# Show the image
cv2.imshow("IMG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
