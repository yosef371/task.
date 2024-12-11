import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os


myframe = tk.Tk()
myframe.title("Text to Speech")
myframe.geometry("700x300")


tk.Label(myframe, text="Text to Speech", font=("Arial", 20)).pack(pady=10)
tk.Label(myframe, text="Enter Your Text", font=("Arial,15"),bg="orange").pack(pady=30)


entry = tk.Entry(myframe, width=40, font=("Arial", 16))
entry.pack(pady=10)


def play_text():
    text = entry.get()
    if text.strip():
        
        tts = gTTS(text=text, lang='ar')
        tts.save("speech.mp3")
        os.system("start speech.mp3") 
    else:
        messagebox.showwarning("خطأ", "ادخل النص .")


def clear_text():
    entry.delete(0, tk.END)

def exit_app():
    myframe.destroy()


btn_play = tk.Button(myframe, text="Play", font=("Arial", 28), bg="green", command=play_text)
btn_play.pack(side=tk.LEFT, padx=10, pady=20)


btn_clear = tk.Button(myframe, text="Set", font=("Arial", 25), bg="red", fg="black", command=clear_text)
btn_clear.pack(side=tk.LEFT, padx=160)


btn_exit = tk.Button(myframe, text="Exit", font=("Arial", 28), bg="blue", fg="black", command=exit_app)
btn_exit.pack(side=tk.LEFT, padx=50)

myframe.mainloop()