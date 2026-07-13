import tkinter as tk

if __name__ == "__main__":
    root_window = tk.Tk()
    root_window.title("Polynomial plot")

    COL_INFO, COL_ENTRIES, COL_INCREASE, COL_DECREASE = range(4)

    ROW_COEFFS = 0
    tk.Label(
        root_window,
        text="Enter the coefficients of the desired polynomial separated with whitespaces starting from the constant: "
    ).grid(row=ROW_COEFFS, column=COL_INFO)
    coeffs_field = tk.Entry(root_window)
    coeffs_field.grid(row=ROW_COEFFS, column=COL_ENTRIES, columnspan=3)

    rows_bounds = range(1, 5)
    default_min_var = tk.StringVar(root_window, "0")
    default_max_var = tk.StringVar(root_window, "1")

    tk_labels_bound = map(lambda bound: f"{bound} of the plot: ",
                          [
                              "Leftmost point",
                              "Rightmost point",
                              "Lowest value",
                              "Topmost value",
                          ]
                          )

    fields_x_y_min_max = []
    print_not_implemented_button = lambda: print("Button not implemented!")
    for label_bound, row_bound in zip(tk_labels_bound, rows_bounds):
        tk.Label(
            root_window,
            text=label_bound
        ).grid(row=row_bound, column=COL_INFO)
        fields_x_y_min_max.append(tk.Entry(root_window))
        fields_x_y_min_max[-1].grid(row=row_bound, column=COL_ENTRIES)
        tk.Button(root_window, text="x2", command=print_not_implemented_button).grid(row=row_bound, column=COL_INCREASE)
        tk.Button(root_window, text="/2", command=print_not_implemented_button).grid(row=row_bound, column=COL_DECREASE)

    root_window.mainloop()
