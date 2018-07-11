## Cat all exif data
import exifread
import glob
from pprint import pformat

sep = '----'
fnPic = glob.glob("./*.JPG")

for fn in fnPic:
    print(sep)
    fh = open(fn, 'rb')
    dat = exifread.process_file(fh)
    for kk, vv in dat.items():
        if kk in ('JPEGThumbnail', 'TIFFThumbnail'):
            continue
        print("%s: %s" % (kk, vv))
