# pip install tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('𝗘𝗔𝗦𝗬-𝗣𝗘𝗔𝗦𝗬')
frame = tk.Frame(master=window, bg="black", padx=15)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, font="ArialBaltic 11", width=29, bg="white")
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=10)


def myclick(number):
    entry.insert(tk.END, number)


def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)

    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")


def change_sign():
    current_number = entry.get()
    if current_number.startswith('-'):
        entry.delete(0)
        entry.insert(tk.END, current_number[1:])
    else:
        entry.insert(0, '-')


def clear():
    entry.delete(len(entry.get()) - 1)


def add_parenthesis(parenthesis):
    entry.insert(tk.END, parenthesis)


def all_clear():
    entry.delete(0, tk.END)


def close_calculator():
    window.destroy()


button_1 = tk.Button(master=frame, text='𝟭', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='𝟮', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='𝟯', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='𝟰', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(4))
button_4.grid(row=1, column=3, pady=2)
button_5 = tk.Button(master=frame, text='𝟱', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(5))
button_5.grid(row=2, column=0, pady=2)
button_6 = tk.Button(master=frame, text='𝟲', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(6))
button_6.grid(row=2, column=1, pady=2)
button_7 = tk.Button(master=frame, text='𝟳', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(7))
button_7.grid(row=2, column=2, pady=2)
button_8 = tk.Button(master=frame, text='𝟴', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(8))
button_8.grid(row=2, column=3, pady=2)
button_9 = tk.Button(master=frame, text='𝟵', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(9))
button_9.grid(row=3, column=0, pady=2)
button_0 = tk.Button(master=frame, text='𝟬', padx=15,
                     pady=5, width=3, bg="#CCCCCC", command=lambda: myclick(0))
button_0.grid(row=3, column=1, pady=2)
button_00 = tk.Button(master=frame, text='𝟬𝟬', padx=15,
                      pady=5, width=3, bg="#CCCCCC", command=lambda: myclick("00"))
button_00.grid(row=3, column=2, pady=2)
button_decimal = tk.Button(master=frame, text='.', padx=15,
                           pady=5, width=3, bg="#CCCCCC", command=lambda: myclick('.'))
button_decimal.grid(row=3, column=3, pady=2)
# button_clear = tk.Button(master=frame, text="𝐂𝐋𝐄𝐀𝐑",
#                          padx=15, pady=5, width=3, bg="#E5D3B3", command=clear)
# button_clear.grid(row=3, column=3,pady=2)
button_add = tk.Button(master=frame, text="+", padx=15,
                       pady=5, width=3, bg="#999999", command=lambda: myclick('+'))
button_add.grid(row=4, column=0, pady=2)

button_subtract = tk.Button(
    master=frame, text="-", padx=15, pady=5, width=3, bg="#999999", command=lambda: myclick('-'))
button_subtract.grid(row=4, column=1, pady=2)

button_multiply = tk.Button(
    master=frame, text="*", padx=15, pady=5, width=3, bg="#999999", command=lambda: myclick('*'))
button_multiply.grid(row=4, column=2, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15,
                       pady=5, width=3, bg="#999999", command=lambda: myclick('/'))
button_div.grid(row=4, column=3, pady=2)
button_plus_minus = tk.Button(master=frame, text="±", padx=15,
                              pady=5, width=3, bg="#999999", command=change_sign)
button_plus_minus.grid(row=5, column=0, pady=2)
button_parenthesis_open = tk.Button(master=frame, text="(", padx=15,
                                    pady=5, width=3, bg="#999999", command=lambda: myclick('('))
button_parenthesis_open.grid(row=5, column=1, pady=2)
button_parenthesis_close = tk.Button(master=frame, text=")", padx=15,
                                     pady=5, width=3, bg="#999999", command=lambda: myclick(')'))
button_parenthesis_close.grid(row=5, column=2, pady=2)
button_percent = tk.Button(master=frame, text="%", padx=15,
                           pady=5, width=3, bg="#999999", command=lambda: myclick('%'))
button_percent.grid(row=5, column=3, pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15,
                         pady=5, width=3, bg="#E5D3B3", command=equal)
button_equal.grid(row=6, column=0, pady=10)
button_clear = tk.Button(master=frame, text="𝐂",
                         padx=15, pady=5, width=3, bg="#E5D3B3", command=clear)
button_clear.grid(row=6, column=1, pady=2)
button_all_clear = tk.Button(master=frame, text="𝗔𝐂𝐂",
                             padx=15, pady=5, width=3, bg="#E5D3B3", command=all_clear)
button_all_clear.grid(row=6, column=2, pady=2)
button_close = tk.Button(master=frame, text="𝗖𝗟𝗢𝗦𝗘",
                         padx=15, pady=5, width=3, bg="#E5D3B3", command=close_calculator)
button_close.grid(row=6, column=3, pady=2)

window.mainloop()
