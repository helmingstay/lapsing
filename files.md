## relocate files older than
```
find . -wholename *GOPRO/G*.JPG \
    ! -newermt 2000-00-00
    -exec ls {} \;
```
