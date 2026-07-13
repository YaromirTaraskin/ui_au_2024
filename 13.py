import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def on_tab1_button_click():
    messagebox.showinfo("Tab 1", "The button on Tab 1 clicked!")


def on_tab2_button_click():
    messagebox.showinfo("Tab 2", "Pink")


def on_quit():
    if messagebox.askokcancel("Quit", "Confirm exitting?"):
        root_window.destroy()


if __name__ == "__main__":
    root_window = tk.Tk()
    root_window.title("(Draft of) Multi-Tab Interface")
    root_window.geometry("800x600")

    style = ttk.Style()
    style.configure('TNotebook.Tab', font=('default', 18, 'bold'))
    style.configure('TNotebook', background='burlywood')

    notebook = ttk.Notebook(root_window)
    tab1 = tk.Frame(notebook)
    tab1['bg'] = 'blueviolet'
    tab2 = tk.Frame(notebook)
    tab2['bg'] = 'lightpink'
    notebook.add(tab1, text="Tab 1")
    notebook.add(tab2, text="Tab 2")
    notebook.pack(expand=1, fill="both")

    tab1_button = tk.Button(tab1, text="Button from tab 1", command=on_tab1_button_click)
    tab1_button.pack(pady=100)

    tab2_button = tk.Button(tab2, text="Other button (from tab 2)", command=on_tab2_button_click)
    tab2_button.pack(pady=100)

    quit_button = tk.Button(root_window, text="Quit", command=on_quit)
    quit_button['font'] = ('default', 18)
    quit_button.pack(side="bottom", pady=5)

    menu = tk.Menu(root_window)
    root_window.config(menu=menu)
    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Quit", command=on_quit)
    root_window.protocol("WM_DELETE_WINDOW", on_quit)

    root_window.mainloop()
