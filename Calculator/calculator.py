import tkinter as tk

# --- LOGIC FUNCTIONS ---

def button_click(value):
    """Called when any number/operator button is pressed."""
    current = display_var.get()
    if current == "Error":
        display_var.set("")
    display_var.set(current + value)

def clear():
    """Clears the display (C button)."""
    display_var.set("")

def calculate():
    """Evaluates the expression shown on the display."""
    try:
        expression = display_var.get()
        # Replace ^ with ** so Python understands power
        expression = expression.replace('^', '**')
        # Replace \ with // for integer division
        expression = expression.replace('\\', '//')
        result = eval(expression)
        display_var.set(str(result))
    except:
        display_var.set("Error")

# --- WINDOW SETUP ---

root = tk.Tk()
root.title("CSC426 Calculator")
root.resizable(False, False)
root.configure(bg="#1a1a2e")  # Dark background

# Variable linked to the display
display_var = tk.StringVar(value="")

# --- DISPLAY SCREEN ---

display = tk.Entry(
    root,
    textvariable=display_var,
    font=('Courier New', 24, 'bold'),
    bg="#16213e",
    fg="#e2e2e2",
    justify='right',
    bd=0,
    relief='flat',
    state='readonly'   # User can't type directly; only buttons work
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# --- BUTTON LAYOUT ---
# Each tuple: (label, row, col, command_or_value)

buttons = [
    ('C',  1, 0), ('%',  1, 1), ('^',  1, 2), ('/',  1, 3),
    ('7',  2, 0), ('8',  2, 1), ('9',  2, 2), ('*',  2, 3),
    ('4',  3, 0), ('5',  3, 1), ('6',  3, 2), ('-',  3, 3),
    ('1',  4, 0), ('2',  4, 1), ('3',  4, 2), ('+',  4, 3),
    ('\\', 5, 0), ('0',  5, 1), ('.',  5, 2), ('=',  5, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        cmd = clear
        color = "#e94560"
    elif text == '=':
        cmd = calculate
        color = "#0f3460"
    else:
        cmd = lambda v=text: button_click(v)
        color = "#16213e"

    btn = tk.Button(
        root,
        text=text,
        font=('Arial', 16, 'bold'),
        bg=color,
        fg="white",
        width=4, height=2,
        bd=0,
        relief="flat",
        command=cmd
    )
    btn.grid(row=row, column=col, padx=4, pady=4)

# --- START THE APP ---
root.mainloop()
