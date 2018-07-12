## Use jpg exif info to create .srt subtitles
## HH:MM:SS
import argparse
import exifread
import glob
import re

parser = argparse.ArgumentParser(description='Create timebase captions from image exif data')
parser.add_argument('fps', help='Frames per second', type=int)
args = parser.parse_args()

## hh:mm:ss
hh_mm = re.compile(r" (\d+:\d+):\d+$")
## files in current dir
fnPic = glob.glob("./*.JPG")

## fps
rate = args.fps

## turn frame into timecode
def mkLoc(loc):
    return "00:%02d:%02d:%02d" % ( loc//60, loc%60, (loc%1)*100) 

## frame number
ii = 0.0
for fn in fnPic:
    ii += 1
    ## this frame: hh:mm:ss:..
    locFrom = mkLoc(ii/rate)
    locTo = mkLoc((ii+1)/rate)
    # Return Exif tags
    fh = open(fn, 'rb')
    dat = exifread.process_file(fh, stop_tag='DateTime')['Image DateTime']
    #aa = hh_mm.search(time).group(1)
    #print hh_mm.search("aa bb 12:34:56").group(1)
    clock = hh_mm.search(str(dat)).group(1)
    print "%d\n%s-->%s\n%s\n" % (ii, locFrom, locTo, clock)
