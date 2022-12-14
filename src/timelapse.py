#!/Users/tylerhaun/projects/timelapse/bin/python

import cv2
import sys
import os
import numpy as np
import datetime
from pytimeparse.timeparse import timeparse
import time


output_fps = 30

# python 1h30m 10s
input_time = timeparse(sys.argv[1])
output_time = timeparse(sys.argv[2])

print(input_time, output_time)



print("imagedir")
image_dir_name = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
print(image_dir_name)
image_dir_path = os.path.abspath(os.path.join(__file__, "../../output", image_dir_name))
print(image_dir_path)

os.makedirs(image_dir_path, exist_ok=True)


#nframes = 1024
nframes = output_time * output_fps
interval = input_time / nframes
print("interval")
print(interval)


cap = cv2.VideoCapture(1)
time.sleep(3)
ret, img = cap.read()
cv2.imshow('current_image',img)
cv2.waitKey(int(interval * 1000))

frames = []

for i in range(nframes):
    # capture
    print("taking image " + str(i) + " / " + str(nframes))
    ret, img = cap.read()
    # save file
    file = './img_'+str(i).zfill(4)+'.png'
    full_file_path = os.path.join(image_dir_path, file)
    print('writing to ' + full_file_path)
    cv2.imwrite(full_file_path, img)
    cv2.imshow('current_image',img)

    frames.append(img)

    cv2.waitKey(int(interval * 1000))


cv2.destroyAllWindows()

video_path = os.path.join(image_dir_path, "timelapse.mp4")

writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"MP4V"), 29.98, (1280, 720))

for frame in frames:
    writer.write(frame)
writer.release()

print("wrote to file")
print(video_path)
