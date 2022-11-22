import os


def vp8(input, output):
    cmd = 'ffmpeg -i {} -c:v libvpx -b:v 1M -c:a libvorbis {}'.format(input, output)
    os.system(cmd)


def vp9(input, output):
    cmd = 'ffmpeg -i {} -c:v libvpx-vp9 -b:v 2M {}'.format(input, output)
    os.system(cmd)


def h265(input, output):
    cmd = 'ffmpeg -i {} -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k {}'.format(input, output)
    os.system(cmd)


def av1(input, output):
    # cmd = 'ffmpeg -i {} -c:v libaom-av1 -crf 30 {}'.format(input, output)
    # cmd = 'ffmpeg -i {} -c:v libaom-av1 -minrate 500k -b:v 2000k -maxrate 2500k {}'.format(input, output)
    cmd = 'ffmpeg -i {} -c:v libaom-av1 -b:v 2M {}'.format(input, output)

    os.system(cmd)


def display(i1, i2, i3, i4, output):
    cmd = 'ffmpeg -i {} -i {} -i {} -i {} -filter_complex "nullsrc=size=640x480 [base]; [0:v] ' \
          'setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright];' \
          ' [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 ' \
          '[lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 ' \
          '[tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] ' \
          'overlay=shortest=1:x=320:y=240" -c:v libx264 {}'.format(i1, i2, i3, i4, output)

    os.system(cmd)
