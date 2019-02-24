import dlib
import cv2
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt

def detect_faces(image):
    im = cv2.read(image)
    (width, height) = im.shape
    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    # face_frames = [(x.left(), round(0.4*x.top()),
    #                x.right(), x.bottom()) for x in detected_faces]
    face_frames = []
    relaxation_factor = 0.25
    for face in detected_faces:
        relaxed_left = round((1-relaxation_factor)*face.left())
        relaxed_top = round((1-relaxation_factor)*face.top())
        relaxed_right = x.right() + round(relaxation_factor*(width-face.right()))
        relaxed_bottom = x.bottom() + round(relaxation_factor*(height-face.bottom()))
        face_frames.append((relaxed_left, relaxed_top, relaxed_right, relaxed_bottom))
    return face_frames

# Load image
img_path = 'test_pic_01.jpg'
image = io.imread(img_path)

# Detect faces
detected_faces = detect_faces(image)

face = Image.fromarray(image).crop(detected_faces[0])

plt.imshow(face)
plt.show()
'''
# Crop faces and plot
for n, face_rect in enumerate(detected_faces):
    face = Image.fromarray(image).crop(face_rect)
    plt.subplot(1, len(detected_faces), n+1)
    plt.axis('off')
    plt.imshow(face)
'''