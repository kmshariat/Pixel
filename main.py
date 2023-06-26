#importing modules
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

#Taking two parameters row and col number of the image
def randomImg(row,col):
    image = np.random.randint(0, 256, (row, col))
    plt.matshow(image)

folder_path = r"inputpath"  # Enter the folder where images are stored
output_path = r"outputPath\output.mp4" # Enter the folder where video will be created

frame_duration = 0.2 #frame duration

# Get a list of image files in the folder
image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png'))]

# Sort the image files in ascending order
image_files.sort()

# Get the first image to determine the frame size
first_image = cv2.imread(os.path.join(folder_path, image_files[0]))
frame_size = (first_image.shape[1], first_image.shape[0])

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_path, fourcc, 1 / frame_duration, frame_size)

# Iterate through the image files and write each frame to the video
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    frame = cv2.imread(image_path)
    video_writer.write(frame)

# Release the video writer and close the video file
video_writer.release()

print("Video created successfully!")
