import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from cdcs import *
from cdcs import *


class Visualise:
    def __int__(self, cod):
        self.cod = cod

    def visual(self):
        ventana = tkinter.Tk()
        ventana.title("SCAV: Seminar 3 Video")
        ventana.geometry("640x540")

        def saludo1():
            print("You have selected VP8 codec.")
            self.cod = 1

        def saludo2():
            print("You have selected VP9 codec.")
            self.cod = 2

        def saludo3():
            print("You have selected h265 codec.")
            self.cod = 3

        def saludo4():
            print("You have selected AV1 codec.")
            self.cod = 4

        # Resolution
        etiqueta = tkinter.Label(ventana, text="Choose the desired resolution:", fg="light green",
                             bg="black", font="Helvetica 16 bold italic")
        etiqueta.pack(fill=tkinter.X)

        list = ("160x120", "360x240", "640x480", "1280x720")
        codec = Combobox(ventana, values=list)
        codec.pack()

        # Codecs
        boton1 = tkinter.Button(ventana, text="VP8", width=20, height=10, bg='#ffb3fe', fg='black',
                            font="Helvetica 11 bold italic", command=saludo1)
        boton2 = tkinter.Button(ventana, text="VP9", width=20, height=10, bg='#ffb3fe', fg='black',
                            font="Helvetica 11 bold italic", command=saludo2)
        boton3 = tkinter.Button(ventana, text="h256", width=20, height=10, bg='#ffb3fe', fg='black',
                            font="Helvetica 11 bold italic", command=saludo3)
        boton4 = tkinter.Button(ventana, text="AV1", width=20, height=10, bg='#ffb3fe', fg='black',
                            font="Helvetica 11 bold italic", command=saludo4)

        etiqueta2 = tkinter.Label(ventana, text="Now choose the desired codec and click Create:", fg="light green",
                              bg="black", font="Helvetica 16 bold italic")
        etiqueta2.pack(fill=tkinter.X)
        etiqueta3 = tkinter.Label(ventana, text="*If you want to create 4 window _ video, click on 4w*",
                                  fg="light green", bg="black", font="Helvetica 16 bold italic")
        etiqueta3.pack()

        boton1.pack(side=tkinter.LEFT)
        boton2.pack(side=tkinter.RIGHT)
        boton3.pack(side=tkinter.TOP)
        boton4.pack(side=tkinter.BOTTOM)

        def makevideo():
            if codec.get() == "1280x720":
                if self.cod == 1:
                    print("You have selected codec vp8 with 1280x720 resolution.")
                    input = 'resize1280x720.mp4'
                    vp8(input, codec.get())
                elif self.cod == 2:
                    print("You have selected codec vp9 with 1280x720 resolution.")
                    input = 'resize1280x720.mp4'
                    vp9(input, codec.get())
                elif self.cod == 3:
                    print("You have selected codec h265 with 1280x720 resolution.")
                    input = 'resize1280x720.mp4'
                    h265(input, codec.get())
                elif self.cod == 4:
                    print("You have selected codec av1 with 1280x720 resolution.")
                    input = 'resize1280x720.mp4'
                    av1(input, codec.get())
            elif codec.get() == "640x480":
                if self.cod == 1:
                    print("You have selected codec vp8 with 640x480 resolution.")
                    input = 'resize640x480.mp4'
                    vp8(input, codec.get())
                elif self.cod == 2:
                    print("You have selected codec vp9 with 640x480 resolution.")
                    input = 'resize640x480.mp4'
                    vp9(input, codec.get())
                elif self.cod == 3:
                    print("You have selected codec h265 with 640x480 resolution.")
                    input = 'resize640x480.mp4'
                    h265(input, codec.get())
                elif self.cod == 4:
                    print("You have selected codec av1 with 640x480 resolution.")
                    input = 'resize640x480.mp4'
                    av1(input, codec.get())
            elif codec.get() == "360x240":
                if self.cod == 1:
                    print("You have selected codec vp8 with 360x240 resolution.")
                    input = 'resize360x240.mp4'
                    vp8(input, codec.get())
                elif self.cod == 2:
                    print("You have selected codec vp9 with 360x240 resolution.")
                    input = 'resize360x240.mp4'
                    vp9(input, codec.get())
                elif self.cod == 3:
                    print("You have selected codec h265 with 360x240 resolution.")
                    input = 'resize360x240.mp4'
                    h265(input, codec.get())
                elif self.cod == 4:
                    print("You have selected codec av1 with 360x240 resolution.")
                    input = 'resize360x240.mp4'
                    av1(input, codec.get())
            elif codec.get() == "160x120":
                if self.cod == 1:
                    print("You have selected codec vp8 with 160x120 resolution.")
                    input = 'resize160x120.mp4'
                    vp8(input, codec.get())
                elif self.cod == 2:
                    print("You have selected codec vp9 with 160x120 resolution.")
                    input = 'resize160x120.mp4'
                    vp9(input, codec.get())
                elif self.cod == 3:
                    print("You have selected codec h265 with 160x120 resolution.")
                    input = 'resize160x120.mp4'
                    h265(input, codec.get())
                elif self.cod == 4:
                    print("You have selected codec av1 with 160x120 resolution.")
                    input = 'resize160x120.mp4'
                    av1(input, codec.get())

        def make4video():
            i1 = 'vp8.webm'
            i2 = 'vp9.webm'
            i3 = 'h265.mp4'
            i4 = 'av1.mp4'
            output = 'display.mkv'
            display(i1, i2, i3, i4, output)

        create = tkinter.Button(ventana, text="Create", fg='Black', bg="white", font="Helvetica 12 bold italic",
                            command=makevideo)
        create.pack()

        w4 = tkinter.Button(ventana, text="4Window", fg='Black', bg="white", font="Helvetica 12 bold italic",
                          command=make4video)

        w4.pack()
        ventana.mainloop()
