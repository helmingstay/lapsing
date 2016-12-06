## Helpful scripts for action camera, time-lapse

* Developed on debian testing

## Commandline tips / docs:

* [ffmpeg / time-lapse encoding](ffmpeg.md)
* [file management](files.md)
* [feeback](feedback.md)

## ImageMagick 
* Lighten:
    - `INDIR=somedir ; time for ii in `ls $INDIR`; do convert $INDIR/$ii -modulate 300 outdir/$ii`
