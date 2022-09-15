import os
import sys
import cv2

input_path = sys.argv[1]

print(input_path)

image_extensions = [".png"]

all_files = os.listdir(input_path)
image_files = [a for a in all_files if a[-4:] in image_extensions]
image_files.sort()
print("using files")
print(image_files)


frames = [cv2.imread(os.path.join(input_path, image_file)) for image_file in image_files]


video_path = os.path.join(input_path, "timelapse.mp4")


shape = frames[0].shape
# (576, 1024, 3)
size = (shape[1], shape[0])
print("size")
print(size)

# writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"MP4V"), 29.98, (1280, 720))
writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"MP4V"), 30, size)


for frame in frames:
    writer.write(frame)
writer.release()

print("wrote to file")
print(video_path)
