## Query device

* ```v4l2-ctl --list-formats-ext``` 
* ```ffmpeg -f v4l2 -list_formats all -i /dev/video1```


## 

* Copy h.264 
```
ffmpeg -f v4l2 -vcodec h264 -framerate 30 -s 640x480 \
    -i /dev/video1  -copyinkf -c:v copy output.mkv
ffmpeg -framerate 12 \
```

* Copy mjpeg
```
ffmpeg -f v4l2 -vcodec mjpeg -framerate 30 -s 640x480 \
    -i /dev/video1  -c:v copy output.mkv
ffmpeg -framerate 12 \
```
