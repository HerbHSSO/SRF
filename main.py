import cv2
from cv2 import dnn_superres
import pyautogui
import numpy as np
# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread('teste.jpg')

# Read the desired model
path = "ESPCN_x2.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("espcn", 2)

# Upscale the image
result = sr.upsample(image)

# Save the image
cv2.imwrite("./upscaled.jpg", result)
