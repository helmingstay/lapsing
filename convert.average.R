## average sequential images with convert 
## see http://www.imagemagick.org/Usage/color_mods/#modulate
.dir.in = './stars30'
.dir.out = './stars_high'
## grab all files
.fns = Sys.glob(paste(.dir.in, pattern='*.JPG', sep='/'))
.by=2
## wait every njob
.njob = 3
## convert filters to apply
.lighten <- 300
.command = paste('-modulate', .lighten, '-average', sep=' ')
## lighten and desaturate
#.command = '-modulate 180,20 -average'

## total jobs
.nf = length(.fns)
## manually specify (testing)
#.nf = 50
## job submission counter
.ijob=0

## job loop - combine images .by at a time
## quasi-parallelism: submit to shell, 
## blocking every .njob submissions
for (ii in seq(from=1, to =(.nf-.by), by=.by)) {
    ## report
    cat(sprintf('##\t%2.0f%%\r', 100*(ii/.nf)))
    ## increment job count
    .ijob = (.ijob+1)%%.njob
    ## wait every .njob
    .wait = !(.ijob)
    ## files to average
    .fn <- .fns[ii:(ii+.by)]
    ## multiple in
    .in.fn = paste(.fn, collapse=' ')
    ## name out from first in
    .out.fn = basename(.fn[1])
    ## shell command
    .job <- paste(sep=' ',
        'convert  ', .in.fn, .command,
        paste(.dir.out, .out.fn, sep='/')
    )
    ret = system(.job, wait=.wait)
    ## break if problems
    if (ret != 0 ) {
        warning('## Command failed')
        break
    }
}
