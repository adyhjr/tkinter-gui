import form as f


def main():
    pass
    form = f.RectangleForm()
    form.mainloop()


import tkinter as tk
from tkinter import messagebox

class RectangleForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Rectangle Calculator')
        self.geometry('250x250')
        # I am the root because I am a TK.

        self.length_label = tk.Label(self, text='Length: ')
        self.width_label = tk.Label(self, text='Width: ')

        self.length_entry = tk.Entry(self)
        self.width_entry = tk.Entry(self)

        self.calculate_button = tk.Button(self, text='Calculate', command=self.calculate_click_handler)
        self.clear_button = tk.Button(self, text='Clear', command=self.clear_click_handler)

        self.display_text = tk.Text(self, height=5, width=20)
        self.display_text.config(state=tk.DISABLED) # Read only now.

        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.width_label.grid(row=1, column=0, padx=10, pady=10)
        self.width_entry.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button.grid(row=2, column=1, padx=10, pady=10)
        self.clear_button.grid(row=3, column=1, padx=10, pady=10)

        self.display_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def is_float(self, entry: tk.Entry) -> bool:
        try:
            # the other option would be to split on the optional (.) and check
            # that both sides are is_digit. This assumes we are using radix (base) 10
            # numbers.
            float(entry.get())
            return True
        except ValueError:
            return False

    def is_float_within_range(self, entry: tk.Entry,
                              min_value: float = float('-inf'),
                              max_value: float = float('inf')) -> bool:
        if not self.is_float(entry):
            return False
        else:
            return min_value <= float(entry.get()) < max_value

    def is_valid_sides(self) -> bool:
        if not self.is_float_within_range(self.length_entry, min_value=1.0):
            # The length is not valid.
            self.length_entry.delete(0, tk.END)
            self.length_entry.focus_set()
            messagebox.showerror('Invalid Length', 'The length is not valid, try again')
            return False

        if not self.is_float_within_range(self.width_entry, min_value=1.0):
            self.width_entry.delete(0, tk.END)
            self.width_entry.focus_set()
            messagebox.showerror('Invalid Width', 'The width is not valid, try again')
            return False

        return True

    def calculate_click_handler(self):
        if self.is_valid_sides():
            self.display_text.config(state=tk.NORMAL)
            self.display_text.delete('1.0', tk.END)
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            area = length * width
            perimeter = length + length + width + width
            # Why is \n here ok, but say not in a file?
            self.display_text.insert(tk.END, f"Area is {area:.2f}\n")
            self.display_text.insert(tk.END, f"Perimeter is {perimeter:.2f}\n")
            self.display_text.config(state=tk.DISABLED)

    def clear_click_handler(self):
        self.display_text.config(state=tk.NORMAL)
        self.display_text.delete('1.0', tk.END)
        self.display_text.config(state=tk.DISABLED)
        self.length_entry.delete(0, tk.END)
        self.width_entry.delete(0, tk.END)
        self.length_entry.focus_set()



