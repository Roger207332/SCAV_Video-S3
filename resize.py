import os


def resize(input, size, n):
    cmd = 'ffmpeg -i {} -vf scale={} resize{}.mp4'.format(input, size, n)
    os.system(cmd)
    return True
