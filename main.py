from tkinter import *
from tkinter import ttk
from googletrans import Translator


def translate():
    for language, suffix in lanngues.items():
        if comboTwo.get() ==  language:
            text = t_input.get('1.0', END)
            translation = translator.translate(text, dest=suffix)
            t_output.delete('1.0', END)
            t_output.insert('1.0', translation.text)


root =Tk()
root.title("OREL Translator 1.0")
root.resizable(0, 0)
root.geometry('500x390')
root['bg'] = 'black'

translator = Translator()
lanngues = {'ألعربية': 'ar', 'Русский': 'ru', 'Türkçe': 'tr', 'English': 'en', 'Azərbaycan': 'az'}

header = Frame(root, bg='black')
header.pack(fill=X)

header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=1)
header.grid_columnconfigure(2, weight=1)


comboOne = ttk.Combobox(header, values=[lang for lang in lanngues], state='readonly')
comboOne.current(0)
comboOne.grid(row=0, column=0)

lb = Label(header, fg='white', bg='black', font='Alegreya 17 bold', text="→")
lb.grid(row=0, column=1)

comboTwo = ttk.Combobox(header, values=[lang for lang in lanngues], state='readonly')
comboTwo.current(1)
comboTwo.grid(row=0, column=2)

t_input = Text(root, width=35, height=5, font='Alegreya 12 bold')
t_input.pack(pady=20)

translator2 = Button(root, width=45, text="Перевести", command=translate)
translator2.pack()

t_output = Text(root, width=35, height=5, font='Alegreya 12 bold')
t_output.pack(pady=20)

root.mainloop()