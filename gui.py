from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from filters import *
from tensorflow.keras.preprocessing.image import img_to_array


def openFile():
    filepath = filedialog.askopenfilename()
    file = Image.open(filepath)
    file = file.resize((500, 330))
    global image
    image = img_to_array(file)
    img = ImageTk.PhotoImage(file)
    # lbl.create_image(img)
    lbl.configure(width=500, height=330, image=img)
    lbl.image = img


window = Tk()
# window.geometry("1920x1080")
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.title("Filter Your Image")

canvas = Canvas(width=1920, height=1080)
canvas.pack(fill=BOTH, expand=True)

# logo
logo = PhotoImage(file="images/information.png")
window.iconphoto(True, logo)


bg = PhotoImage(file="images/bg10.png")
canvas.create_image(0, 0, image=bg, anchor=NW)
label = Label(
    window,
    image=bg
)
label.place(x=0, y=0)


lbl = Label(window, width=75, height=20)
lbl.place(x=530, y=250)


button2 = Button(window, text='U P L O A D', command=openFile,
                 width=50, height=3, border=2, bg="#ffffff")

button4 = Button(window, text="Grey Scale", command=lambda: grayscale(image, lbl),
                 width=50, height=2, border=2, bg="#ffffff")

button5 = Button(window, text="Black and White",
                 command=lambda: bnw(image, lbl), width=50, height=2, border=2, bg="#ffffff")

button6 = Button(window, text="Gaussian Blur", command=lambda: gaussian_blur(image, lbl),
                 width=50, height=2, border=2, bg="#ffffff")

button7 = Button(window, text="Dilation", command=lambda: Dilation_Opencv(image, lbl),
                 width=50, height=2, border=2, bg="#ffffff")

button8 = Button(window, text="Erosion", command=lambda: Erosion_Opencv(image, lbl),
                 width=50, height=2, border=2, bg="#ffffff")


button2.place(x=582, y=640, anchor='w')
button4.place(x=1082, y=280, anchor='w')
button5.place(x=1082, y=380, anchor='w')
button6.place(x=1082, y=480, anchor='w')
button7.place(x=1082, y=580, anchor='w')
button8.place(x=1082, y=680, anchor='w')


window.mainloop()