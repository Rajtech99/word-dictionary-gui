from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from main import *


# Get text entry value
def info():
    input_text = word_entry.get()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{input_text}"
    get_value = requests.get(url)
    data = get_value.json()
    code = get_value.status_code
    if code == 200:
        saveData("data.json", data)
        value = loadFile("data.json")
        sound = value[1]
        meaning = value[2]
        synonyms = value[3]
        Label(win, text=meaning, font=('calibre', 10, 'normal')).place(x=40, y=330, height=50, width=330)
        return sound, meaning, synonyms
    else:
        messagebox.showerror(title="Error occurred", message="This word is not define in US English")


# Creating main window
def mainWindow():
    global word_entry, win
    win = Tk()
    win.config(bg="gray81")
    win.geometry("400x600")
    win.title("WordBook")

    # Main heading label
    Label(win, text="Welcome to WordBook", font=("Terminal", 18, "bold"), fg="black", bg="gray81").pack(pady=8)

    # Placing logo
    image_frame = Frame(win, width=120, height=120, bg="gray81")
    image_frame.place(x=140, y=50)
    img = ImageTk.PhotoImage(Image.open("logo.png"))
    label = Label(image_frame, image=img, bg="gray81")
    label.pack()

    word_entry = Entry(win, font=('calibre', 15, 'normal'))
    word_entry.place(x=40, y=200, width=320, height=35)

    Button(win, text="Get Meaning", bg="gray67", fg="black", command=info).place(x=100, y=250, width=200,
                                                                                 height=30)
    Label(win, text="Meaning", font=("Terminal", 15, "bold"), bg="yellow").place(x=40, y=300, height=27, width=100)

    win.mainloop()


mainWindow()
