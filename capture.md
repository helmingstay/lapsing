## capture from webcam

* List capabilities: `ffmpeg -f v4l2 -list_formats all -i /dev/videoX`
* Capture & compress (fast)
```
ffmpeg -f v4l2 -framerate 24 -video_size 1280x720  \
    -input_format mjpeg -i /dev/video1 \
    -c:v libx264 -preset fast -crf 23 \
    output720.mp4
```
* recompress
```
ffmpeg -i output720.mp4 \
    -c:v libx264 -preset slow -crf 23 \
    output720.fin.mp4
```
