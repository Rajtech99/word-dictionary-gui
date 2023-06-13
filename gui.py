from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from main import *
import vlc


# Play the input text
def playSound():
    url = sound
    # Check this url is exists or not
    if url != '':
        p = vlc.MediaPlayer(url)
        p.play()
    else:
        messagebox.showwarning(title="Warning", message="Audio not available!")


def Exit():
    win.destroy()

# Get text entry value
def info():
    global sound
    # Get the value of input text entry
    input_text = word_entry.get()

    # If the input word is a single letter
    if 0 < len(input_text) < 2:
        messagebox.showerror(title="Error", message=f"{input_text.capitalize()} is not a meaningful word")

    # Check the entry box empty or not
    elif input_text != '':
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{input_text}"
        get_value = requests.get(url)
        data = get_value.json()
        code = get_value.status_code
        # If the input word is a meaningful word
        if code == 200:
            win.geometry("400x690")
            close_button.destroy()
            saveData("data.json", data)
            value = loadFile("data.json")
            # Get the all required items
            sound = value[1]
            meaning = value[2]
            synonyms = value[3]

            # Display the meaning of the inputted word
            Label(win, text="Meaning", font=("Terminal", 15, "bold"), bg="gray81").place(x=40, y=300, height=27,
                                                                                         width=100)
            Label(win, text=meaning, font=('calibre', 10, 'normal'), bg="gray90", wraplength=330).place(x=40, y=335, height=100, width=330)
            # Sound play button and label
            Label(win, text="Audio", font=("Terminal", 15, "bold"), bg="gray81").place(x=40, y=445, height=27)
            Label(win, text=f"Say:", font=('calibre', 12, 'normal'), bg="gray81", fg="green").place(x=40, y=477, height=25, width=40)
            Button(win, text="Play", font=('calibre', 12, 'normal'), bg="gray67", fg="black", command=playSound).place(x=90, y=477, height=25, width=100)

            # Check the no. of items in synonyms
            if len(synonyms) != 0:
                synonyms = ', '.join(map(str, synonyms))
                Label(win, text="Synonyms", font=("Terminal", 15, "bold"), bg="gray81").place(x=40, y=512, height=27)
                Label(win, text=synonyms, font=('calibre', 12, 'normal'), bg="gray90", wraplength=330).place(x=40, y=550, height=80, width=330)
                Button(win, text="Close", bg="gray67", fg="black", command=Exit).place(x=100, y=640, width=200, height=30)
            else:
                Label(win, text="Synonyms", font=("Terminal", 15, "bold"), bg="gray81").place(x=40, y=512, height=27)
                Label(win, text="Synonyms not available", font=('calibre', 12, 'normal'), bg="gray90", wraplength=330).place(x=40, y=550, height=60, width=330)
                Button(win, text="Close", bg="gray67", fg="black", command=Exit).place(x=100, y=640, width=200, height=30)

        else:
            messagebox.showerror(title="Error occurred", message="This word is not define in US English")
    else:
        messagebox.showwarning(title="Warning", message="Please enter a valid word")


# Creating main window
def mainWindow():
    global word_entry, win, close_button

    # Create the main window
    win = Tk()
    win.config(bg="gray81")
    win.geometry("400x360")
    win.title("WordBook")
    win.resizable(False, False)

    # Main heading label
    Label(win, text="Welcome to WordBook", font=("Terminal", 18, "bold"), fg="black", bg="gray81").pack(pady=8)

    # Placing logo
    image_frame = Frame(win, width=120, height=120, bg="gray81")
    image_frame.place(x=140, y=50)
    img = ImageTk.PhotoImage(Image.open("logo.png"))
    label = Label(image_frame, image=img, bg="gray81")
    label.pack()

    Label(win, text="Powered by RT Production", font=("Terminal", 10, "bold"), bg="gray81").place(x=100, y=170, width=200)

    # Place the text entry box
    word_entry = Entry(win, font=('calibre', 15, 'normal'))
    word_entry.place(x=40, y=200, width=320, height=35)

    # Submit button
    Button(win, text="Get Meaning", bg="gray67", fg="black", command=info).place(x=100, y=250, width=200,
                                                                                 height=30)
    # Exit button
    close_button = Button(win, text="Close", bg="gray67", fg="black", command=Exit)
    close_button.place(x=100, y=300, width=200, height=30)

    win.mainloop()


mainWindow()
