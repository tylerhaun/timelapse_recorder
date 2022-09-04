### Usage:
#### timelapse.py
`python src/timelapse.py 10s 1s`


first argument is input_time
second argument is output_time

uses timeparse on both


Defaults to 30fps.  Number of frames is output_time * 30fps
Time between photos is input time / number of frames 

Ex. 

python src/timelapse.py 10m 10s

number of frames = 10s * 30fps = 300
time between photos = 600s / 300 frames = 2s


VideoCapture index might need to be changed in the code to get correct camera


#### images_to_video.py
Format images into mp4 video

`python src/images_to_video.py output/2022-09-03T21:42:22`

finds all .png images in directory then creates timelapse.mp4

It is already run inside timelapse.py so no need to run it most of the time

