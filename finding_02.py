import cv2
import numpy as np
from matplotlib import pyplot as pltd
from PIL import Image
import time


def find_menu(photo):
    start_time = time.time()
    imaging = cv2.imdecode(np.frombuffer(photo.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    img_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)
    imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)
    xml_data = cv2.CascadeClassifier('cascade.xml')
    detecting = xml_data.detectMultiScale(img_gray, minSize=(30, 30))
    amountDetecting = len(detecting)

    if amountDetecting != 0:
        for (a, b, width, height) in detecting:
            cv2.rectangle(imaging_rgb, (a, b), (a + height, b + width), (0, 275, 0), 9)

    pltd.subplot(1, 1, 1)
    im = Image.fromarray(imaging_rgb)
    im.save('new_image.jpg')
    return time.time() - start_time
