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

## Filter tricks
* Mandelbrot (runs out of mem quickly, causes cool *shimmer* effect
* Add analysis edge / corner panels
* [docs / more examples](https://trac.ffmpeg.org/wiki/FancyFilteringExamples)
```
ffmpeg -t $((60*10)) -hide_banner \
    -filter_complex "mandelbrot=s=hd480,format=yuv444p,split=4[a][b][c][d],[a]waveform=d=overlay[aa],[b][aa]vstack[V],[c]waveform=m=0:display=parade[cc],[d]vectorscope=color3[dd],[cc][dd]vstack[V2],[V][V2]hstack[fin],[fin]scale=hd720" \
    -c:v libx264 -preset slow -crf 12 out.mp4
```