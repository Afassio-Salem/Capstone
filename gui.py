from tkinter import *
import tkinter as tk
import random as rand
import threading
import time
from tkinter.filedialog import askopenfilename
import pyAudio
import wave


root = Tk()
root.title("Music Recognition")
# width x height + x_offset + y_offset:
root.geometry("440x300+30+30")
root.configure(background='white')
frame = tk.Canvas(root, width=440, height=300, borderwidth=0, bg='black')
frame.pack()
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file="C:\\Users\\shaun\\Pictures\\cap.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

def import_csv_data():
    df = pd.read_csv(csv_file_path)
    with open('Top100.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Artist_Name = row['Artist Name']
            Album_Name = row['Album Name']
            Song_Name = row['Song Name']
            tree.insert("", 0, values=(Artist_Name,Album_Name,Song_Name))

def drawcircle(self, x, y, r, **kwargs):
    # changed this to return the ID
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def clickedContinue():
    # info.remove(info[1])
    B.config(state=DISABLED)
    # info.update()
    info1 = ["Listening to song playing...", "", ""]

    for i in range(3):
        # ct =
        brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
        ct_hex = "%02x%02x%02x" % tuple(ct)
        bg_colour = '#' + "".join(ct_hex)
        l = tk.Label(root,
                     text=info1[i],
                     fg='white',
                     bg='black')
        l.place(x=20, y=30 + i * 30, width=400, height=25)

    cr1 = drawcircle(frame, 10, 150, 10, fill='pink', width=3);

    x = 5
    y = 0
    while True:

        frame.move(cr1, x, y)
        p = frame.coords(cr1)
        if p[3] >= 440 or p[1] <= 0:
            y = -y
        if p[2] >= 440 or p[0] <= 0:
            x = -x
        root.update()
        time.sleep(.011)


B = Button(root, text="Continue", command=clickedContinue)
B.place(x=190, y=250)
info = ['Music Recognition', 'Created by: Angela Fassio & Shauna Hunt', "Play a song to find out its info!"]
labels = range(3)
for i in range(3):
    ct = [rand.randrange(256) for x in range(3)]
    brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    l = tk.Label(root,
                 text=info[i],
                 fg='White' if brightness < 120 else 'Black',
                 bg=bg_colour)
    l.place(x=20, y=30 + i * 30, width=400, height=25)

def display():
    info = ['Artist Name:', 'Album Name: ', 'Song Name: ']
    labels = range(3)
    for i in range(3):
        ct = [rand.randrange(256) for x in range(3)]
        brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
        ct_hex = "%02x%02x%02x" % tuple(ct)
        bg_colour = '#' + "".join(ct_hex)
        l = tk.Label(root,
                     text=info[i],
                     fg='White' if brightness < 120 else 'Black',
                     bg=bg_colour)
        l.place(x=20, y=30 + i * 30, width=400, height=25)


class App():
    def __init__(self, master):
        self.isrecording = False
        self.button = tk.Button(root, text='rec')
        self.button.bind("<Button-1>", self.startrecording)
        self.button.bind("<ButtonRelease-1>", self.stoprecording)
        self.button.pack()

    def startrecording(self, event):
        self.isrecording = True
        t = threading.Thread(target=self._record)
        t.start()

    def stoprecording(self, event):
        self.isrecording = False

    def _record(self):
        while self.isrecording:
            print("Recording")


app = App(root)
root.mainloop()
