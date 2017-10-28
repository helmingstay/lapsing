## Links

* [h.264 Encoder Guide](https://trac.ffmpeg.org/wiki/Encode/H.264)
    - CRF + VBV settinge
* [Filter docs](http://ffmpeg.org/ffmpeg-filters.html)
* [Rate control mode primer](http://slhck.info/video/2017/03/01/rate-control.html)
    - With figures!
* [Metadata fields](https://multimedia.cx/eggs/supplying-ffmpeg-with-metadata/)
    - E.g. `-metadata title="my title"`

## use glob to set up files 
```
ffmpeg -framerate 12 \
    -pattern_type glob -i 'G*.JPG' \
    -c:v libx264 -preset slow -crf 14 \
    -hide_banner \
    -vf scale=1920:-1 \
    out.mp4
```

* Rotate:
  - `-vf rotate=PI`

* Crop (ex. from bottom / left)
  - Compute dimensions: `NN=20; WW=$(($NN * 16)); HH=$(($NN * 9));` 
  - `-vf "crop=in_w-$WW:in_h-$HH:$WW:0,scale=1920:-1" 

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

## Filter tricks
* Mandelbrot (runs out of mem quickly, causes cool *shimmer* effect
* Add analysis edge / corner panels
* [docs / more examples](https://trac.ffmpeg.org/wiki/FancyFilteringExamples)
```
ffmpeg -t $((60*10)) -hide_banner \
    -filter_complex "mandelbrot=s=hd480,format=yuv444p,split=4[a][b][c][d],[a]waveform=d=overlay[aa],[b][aa]vstack[V],[c]waveform=m=0:display=parade[cc],[d]vectorscope=color3[dd],[cc][dd]vstack[V2],[V][V2]hstack[fin],[fin]scale=hd720" \
    -c:v libx264 -preset slow -crf 12 out.mp4
```

## Down-sample time (assumes 60 fps inpu)
* Note: this re-encodes
* Start time (```-ss```), duration (`-t`)
* Strip audio (`-an`)
```
ffmpeg -r 30 -ss 1 -i input.mp4 -t 15 -an out.mp4
```

