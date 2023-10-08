
import cv2
import numpy as np
import pygame

# Initialize Pygame for audio
pygame.init()
pygame.mixer.init()

# Parameters for audio mapping
min_intensity = 0
max_intensity = 255
min_frequency = 220  # Minimum frequency (in Hz)
max_frequency = 880  # Maximum frequency (in Hz)

def intensity_to_pitch(intensity):
    return min_frequency + (max_frequency - min_frequency) * (intensity - min_intensity) / (max_intensity - min_intensity)

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Play sound based on intensity
    for row in gray_frame:
        for intensity in row:
            frequency = intensity_to_pitch(intensity)
            pygame.mixer.Sound(frequency).play()

    cv2.imshow('Sonified Image', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
