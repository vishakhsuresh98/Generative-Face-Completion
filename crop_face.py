import dlib
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt


def detect_face(image):
    """
    Detects faces in the input image - uses dlib library
    :param image: original image
    :return: detected face in the image
    """
    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the face in the image.
    return face_detector(image, 1)[0]


def get_relaxed_boundaries(image, face, factor):
    """
    Relaxes (expands) the boundaries by a factor
    :param image: original image
    :param face: oetected face
    :param factor: relaxation factor
    :return: a 4-tuple with the relaxed boundaries
    """
    height, width, depth = image.shape # dimensions of the image

    relaxed_left = round((1 - factor) * face.left())
    relaxed_top = round((1 - factor) * face.top())
    relaxed_right = face.right() + round(factor * (width - face.right()))
    relaxed_bottom = face.bottom() + round(factor * (height - face.bottom()))
    return (relaxed_left, relaxed_top, relaxed_right, relaxed_bottom)


def crop_face(image):
    """
    Steps:
    1. Detect the face in the original image
    2. Relax the bounding regions
    3. Crop the image to get exclusively, the face
    4. Return the cropped image, used in subsequent stages
    :param image: original image
    :return: cropped face
    """
    detected_face = detect_face(image)

    # Relax the bounding boxes of the image
    relaxation_factor = .33
    relaxed_boundaries = get_relaxed_boundaries(image, detected_face, relaxation_factor)

    # Crop the image
    cropped_face = Image.fromarray(image).crop(relaxed_boundaries)
    return cropped_face


# Load image
img_path = 'image.jpeg'
# img_path = 'test_pic_01.jpg'
# img_path = 'test_pic_02.jpg'
image = io.imread(img_path)

cropped_face = crop_face(image)
plt.imshow(cropped_face)
plt.show()