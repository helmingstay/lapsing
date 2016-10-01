## Broadcast camera, inverse video
```
mpv --vf=eq=1:-1 --hue=-100  /dev/video1
```

## capture lower screen (ie config w/xrandr),
## write to mpeg4 file (h264 too slow for real-time)
```
ffmpeg -video_size 1920x1080 
    -framerate 10 -f x11grab 
    -i :0.0+0,1440 -c:v mpeg4 
    -bufsize 1000000k -maxrate 80000k 
    -qscale:v 3 output1.mp4
```
