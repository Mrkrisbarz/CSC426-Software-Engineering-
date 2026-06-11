import tkinter as tk

def button_click(value):
    current = display_var.get()
    if current == "Error":
        display_var.set("")
    display_var.set(current + value)

def clear():
    display_var.set("")

def calculate():
    try:
        expression = display_var.get()
        expression = expression.replace('^', '**')
        expression = expression.replace('\\', '//')
        result = eval(expression)
        display_var.set(str(result))
    except:
        display_var.set("Error")

root = tk.Tk()
root.title("CSC426 Calculator")
root.resizable(False, False)
root.configure(bg="#000000")

display_var = tk.StringVar(value="")

display = tk.Entry(
    root, textvariable=display_var,
    font=('Helvetica', 36, 'normal'),
    bg="#000000", fg="#ffffff",
    justify='right', bd=0,
    relief='flat', state='readonly'
)
display.grid(row=0, column=0, columnspan=4, padx=16, pady=20, sticky='ew', ipady=22)

buttons = [
    ('C',  1,0), ('^', 1,1), ('%', 1,2), ('/',  1,3),
    ('7',  2,0), ('8', 2,1), ('9', 2,2), ('*',  2,3),
    ('4',  3,0), ('5', 3,1), ('6', 3,2), ('-',  3,3),
    ('1',  4,0), ('2', 4,1), ('3', 4,2), ('+',  4,3),
    ('\\', 5,0), ('0', 5,1), ('.', 5,2), ('=',  5,3),
]

colors = {
    'C': '#a5a5a5', '^': '#a5a5a5', '%': '#a5a5a5',
    '/': '#ff9f0a', '*': '#ff9f0a', '-': '#ff9f0a',
    '+': '#ff9f0a', '=': '#ff9f0a',
}
text_colors = {
    'C': '#000000', '^': '#000000', '%': '#000000',
}

for (text, row, col) in buttons:
    if text == 'C':
        cmd = clear
    elif text == '=':
        cmd = calculate
    else:
        cmd = lambda v=text: button_click(v)

    bg = colors.get(text, '#333333')
    fg = text_colors.get(text, '#ffffff')

    btn = tk.Button(
        root, text=text,
        font=('Helvetica', 18),
        bg=bg, fg=fg,
        width=4, height=2,
        bd=0, relief='flat',
        activebackground=bg,
        activeforeground=fg,
        command=cmd
    )
    btn.grid(row=row, column=col, padx=6, pady=6)

root.mainloop()