import tkinter as tk
import random
from tkinter import ttk
import os
random.seed()

# set working directory to current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# generate window
window = tk.Tk()
window.title("Poetry")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.attributes('-fullscreen', True)
window.minsize(500, 500)
style = ttk.Style(window)
style.configure(".", font=("Century Gothic", 24, "bold"))

# get 3 random words from words.txt
def get_words():
    words = set()
    try:
        f = open("words.txt", "r")
        lines = f.readlines()
        f.close()
        while (len(words) < 3):
            words.add(lines[random.randint(0, len(lines))])
    except Exception as e:
        print("There is no file. " + str(e))
    return list(words)

words_list = get_words()

#print(words)


# tkinter stuff here
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=3)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)

lbl_task = ttk.Label(window, text="Schreibe ein Gedicht, dass die folgenden drei Wörter enthält!")
lbl_task.grid(column=0, row=0, columnspan=3, padx=10, pady=10)
lbl_w0 = ttk.Label(window, text=words_list[0])
lbl_w1 = ttk.Label(window, text=words_list[1])
lbl_w2 = ttk.Label(window, text=words_list[2])
lbl_w0.grid(column=0, row=1, padx=30, pady=10)
lbl_w1.grid(column=0, row=2, padx=30, pady=10)
lbl_w2.grid(column=0, row=3, padx=30, pady=10)
entry = tk.Text(window, background="snow", font=("Century Gothic", 24, "bold"), height=1, width=40, padx=10, pady=10, insertwidth=5, insertbackground="red")
entry.focus()
entry.grid(column=1, row=1, rowspan=3, padx=20, pady=20, sticky=tk.NS)


# when button is clicked
def button_click():
    entry_text = entry.get("1.0", "end").rstrip()
    #check if entry_text contains any letters
    if any(c.isalpha() for c in entry_text):
        #count files in directory "poems"
        number = 0
        numbers_set = set()
        for path in os.listdir("poems"):
            numbers_set.add(path[:4])
        while "{:04d}".format(number) in numbers_set:
            number += 1
        #write poem to file
        with open("poems/{:04d}.txt".format(number), "w+") as poem:
            poem.write(entry_text)
            poem.close()
            entry.delete("1.0", "end")
        from fpdf import FPDF
        entry_lines = entry_text.splitlines()
        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()
        pdf.set_font("Courier", "B", 24)
        pdf.set_y(297/2-len(entry_lines)*10/2)
        for line in entry_lines:
            pdf.cell(190, 10 , line, 0, 1, "C")
        pdf.output("poems/{:04d}.pdf".format(number))
        words_list = get_words()
        lbl_w0.config(text=words_list[0])
        lbl_w1.config(text=words_list[1])
        lbl_w2.config(text=words_list[2])





btn_submit = ttk.Button(window, text="Abschicken", command=button_click)
btn_submit.grid(column=1, row=4)

window.mainloop()