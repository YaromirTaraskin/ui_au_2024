import tkinter as tk
import random

win_width = 400
d = 10
mb = win_width - 9 * d


def on_win_manager_closing():
    print("Using window manager is not allowed...")


class FlyingButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flying button")
        self.geometry(f"{win_width}x{win_width}")
        self.configure(bg='chartreuse3')
        self.resizable(False, False)

        self.button = tk.Button(self, text="QUIT BUTTON", command=self.on_winning)
        self.button.place(x=random.randint(d, mb), y=random.randint(d, mb))
        self.button.bind("<Enter>", self.move_button)

        self.protocol("WM_DELETE_WINDOW", on_win_manager_closing)

    def move_button(self, event):
        self.button.place(x=random.randint(d, mb), y=random.randint(d, mb))

    def on_winning(self):
        print("\nCongratulations!\nYou won!")
        self.destroy()


if __name__ == "__main__":
    main_app = FlyingButtonApp()
    main_app.mainloop()
