## use glob to set up files 
```
ffmpeg -framerate 12 \
    -pattern_type glob -i 'G*.JPG' \
    -c:v libx264 -preset slow -crf 14 \
    -hide_banner \
    -vf scale=1920:-1 \
    out.mp4
```

## mux audio, trim to shortest 

* [SO link](http://stackoverflow.com/questions/11779490/how-to-add-a-new-audio-not-mixing-into-a-video-using-ffmpeg)
```
ffmpeg -i in.mp4 -i in.mp3 \
    -codec copy -shortest out.mp4
```

## Filter chain example
*  kaleidoscope - split and flip
```
ffmpeg -i in.mp4 \
    -vf "split [main][tmp]; [tmp] crop=iw:ih/2:0:0, vflip [flip]; [main][flip] overlay=0:H/2" \
    -codec:a copy out.mp4 
```
