from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import FeatureExecution as fe
from threading import Thread
import pygame
from pystray import MenuItem as item
import pystray
import PIL.Image

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("800x500")
window.configure(bg = "#403E3E")
# window.overrideredirect(True) # Remove the window border
window.resizable(False, False)
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

def inputs():
    def thread1():        
        print("Mic button disabled")
        button_2.config(state="disabled")
        fe.showmagic(fe.takeCommand())
        button_2.config(state="active")
        print("Mic button enabled")
    thread = Thread(target=thread1)
    thread.start()

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

def EnterKeyPress(self):
    vars=entry_1.get()
    if(vars!=""):
        fe.showmagic(vars)
    entry_1.delete(0, 'end')

def EnterButtonPress():
    vars=entry_1.get()
    if(vars!=""):
        fe.showmagic(vars)
    entry_1.delete(0, 'end')

def show_window(icon, item):
   icon.stop()
   window.after(0,window.deiconify())

def quit_window(icon, item):
   icon.stop()
   window.destroy()

def hide_window():
   window.withdraw()
   fp=open(relative_to_assets("favicon.ico"),'rb')
   image = PIL.Image.open(fp)
   menu=(item('Quit', quit_window), item('Show Blink', show_window))
   icon=pystray.Icon("name", image, "Blink", menu)
   icon.run()

canvas = Canvas(
    window,
    bg = "#403E3E",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# canvasBox = Canvas(
#     window,
#     bg = "#FFFFFF",
#     height = 500,
#     width = 800,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge"
# )
# canvasBox.place(x = 0, y = 0)
entry_1 = Entry(
    bd=0,
    bg="#1E1F20",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Inter", 25 * -1),
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))

button_image_1 = PhotoImage(
    file=relative_to_assets("close.png"))

button_image_2 = PhotoImage(
    file=relative_to_assets("microphone.png"))

button_image_4 = PhotoImage(
    file=relative_to_assets("return-key.png"))

canvas.create_text(
    23.0,
    17.0,
    anchor="nw",
    text="Blink.",
    fill="#11B195",
    font=("Covered By Your Grace", 52 * -1,)
)

# canvas.create_text(
#     36.0,
#     461.0,
#     anchor="nw",
#     text="Ask me anything...",
#     fill="#494343",
#     font=("Inter", 20 * -1)
# )

canvas.create_text(
    229.0,
    196.0,
    anchor="nw",
    text="Hi! How can I help?",
    fill="#FFFFFF",
    font=("OpenSansRoman Regular", 40 * -1)
)

entry_bg_1 = canvas.create_image(
    400.0,
    474.0,
    image=entry_image_1
)

button_1 = Button(
    text="X",
    font=("Inter", 25 * -1,"bold"),
    command=window.destroy,
    relief="sunken",
    background="#403E3E",
    activebackground="#403E3E",
    borderwidth=0
)

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    background="#FFFFFF",
    command=inputs,
    relief="flat"
)

button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    background="#1e1e1e",
    command=EnterButtonPress,
    relief="flat"
)

canvas.place(x = 0, y = 0)

entry_1.place(
    x=15.0,
    y=452.0,
    width=800.0,
    height=40.0
)

# button_1.place(
#     x=762.0,
#     y=14.0,
#     width=25.0,
#     height=25.0
# )

button_2.place(
    x=749.0,
    y=448.0,
    width=50,
    height=50,
)

button_4.place(
    x=700.0,
    y=448.0,
    width=45.0,
    height=45.0
)

window.protocol('WM_DELETE_WINDOW', hide_window)
#enable dragging while holding the left mouse button
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)
window.bind('<Return>', EnterKeyPress)
window.mainloop()