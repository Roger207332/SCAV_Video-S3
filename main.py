from resize import *
from cdcs import *
from visual import *

if __name__ == '__main__':

    input = 'BBB.mp4'
    size = '1280x720'
    resize(input, size, size)
    size = '640x480'
    resize(input, size, size)
    size = '360x240'
    resize(input, size, size)
    size = '160x120'
    resize(input, size, size)

    """
    input = 'BigBuckBunny.mp4'
    size = '1280x720'
    size2 = '1280x720Big'
    resize(input, size, size2)
    size = '640x480'
    size2 = '640x480Big'
    resize(input, size, size2)
    size = '360x240'
    size2 = '360x240Big'
    resize(input, size, size2)
    size = '160x120'
    size2 = '160x120Big'
    resize(input, size, size2)
    """

    input = 'BBB.mp4' 
    output = 'vp8.webm'
    vp8(input, output)
    
    input = 'BBB.mp4'
    output = 'vp9.webm'
    vp9(input, output)

    input = 'BBB.mp4'
    output = 'h265.mp4'
    h265(input, output)
    
    input = 'BBB.mp4'
    output = 'av1.mp4'
    av1(input, output)

    """
    i1 = 'vp8.webm'
    i2 = 'vp9.webm'
    i3 = 'h265.mp4'
    i4 = 'av1.mp4'
    output = 'display.mkv'
    display(i1, i2, i3, i4, output)
    """

    v = Visualise()
    v.visual()
