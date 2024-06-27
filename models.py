import tkinter as tk
from tkinter import messagebox


class Player(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Player Stats")
        self.geometry("500x500")

        self.DEBUG = tk.Button(self, text="DEBUG", command=self.store_input)
        self.DEBUG.grid(row=8, column=4)

        self.player_id = tk.Label(self, text="Player ID:")
        self.player_entry = tk.Entry(self)
        self.player_id.grid(row=0, column=0)
        self.player_entry.grid(row=0, column=1)

        self.first_name = tk.Label(self, text="First Name:")
        self.first_name_entry = tk.Entry(self)
        self.first_name.grid(row=1, column=0, pady=10, padx=10)
        self.first_name_entry.grid(row=1, column=1, pady=10, padx=10)

        self.last_name = tk.Label(self, text="Last Name: ")
        self.last_name_entry = tk.Entry(self)
        self.last_name.grid(row=2, column=0, pady=10, padx=10)
        self.last_name_entry.grid(row=2, column=1, pady=10, padx=10)

        self.position = tk.Label(self, text="Position: ")
        self.position_entry = tk.Entry(self)
        self.position.grid(row=3, column=0, pady=10, padx=10)
        self.position_entry.grid(row=3, column=1, pady=10, padx=10)

        self.total_bats = tk.Label(self, text="Total Bats: ")
        self.total_bats_entry = tk.Entry(self)
        self.total_bats.grid(row=4, column=0, pady=10, padx=10)
        self.total_bats_entry.grid(row=4, column=1, pady=10, padx=10)

        self.bats_hit = tk.Label(self, text="Bats hit: ")
        self.bats_hit_entry = tk.Entry(self)
        self.bats_hit.grid(row=5, column=0, pady=10, padx=10)
        self.bats_hit_entry.grid(row=5, column=1, pady=10, padx=10)

        self.percentage_hit = tk.Label(self, text="Percentage Hit: ")
        self.percentage_hit_entry = tk.Entry(self)
        self.percentage_hit.grid(row=6, column=0, pady=10, padx=10)
        self.percentage_hit_entry.grid(row=6, column=1, pady=10, padx=10)

        self.add_player = tk.Button(self, text="Add Player", command=self.add_player_handler())
        self.add_player.grid(row=0, column=4, pady=10, padx=10)

        self.get_player = tk.Button(self, text="Get Player", command=self.get_player_handler())
        self.get_player.grid(row=0, column=5, pady=10, padx=10)

        self.save_changes = tk.Button(self, text="Save Changes", command=self.save_changes_handler())
        self.save_changes.grid(row=7, column=0, pady=10, padx=10)

        self.cancel = tk.Button(self, text="Cancel", command=self.cancel_handler())
        self.cancel.grid(row=7, column=1, pady=10, padx=10)

        self.display_text = tk.Text(self)

    def is_int(self, entry: tk.Entry) -> bool:
        try:
            int(entry.get())
            return True
        except ValueError:
            return False

    def validate_range(self, entry: tk.Entry, min_value: float = float('0'), max_value: float = float('inf')) -> bool:
        if not self.is_int(entry):
            return False
        else:
            return min_value <= int(entry.get()) < max_value

    def validate_str(self, entry: tk.Entry) -> bool:
        string = entry.get().strip()
        return bool(string) and string.isalpha()

    def validate_position(self, entry: tk.Entry) -> bool:
        position_string = entry.get().strip()
        return len(position_string) == 2 and position_string.isalnum()

    def messagebox(self) -> bool:
        if not self.validate_range(self.player_entry, min_value=0):
            self.player_entry.delete(0, tk.END)
            self.player_entry.focus_set()
            messagebox.showerror("Player Entry Error", "Ensure player entry is a positive whole numeric value.")
            return False

        if not self.validate_range(self.total_bats_entry, min_value=0):
            self.total_bats_entry.delete(0, tk.END)
            self.total_bats_entry.focus_set()
            messagebox.showerror("Total Bats Entry Error", "Ensure total bats entry is a positive whole numeric value.")
            return False

        if not self.validate_range(self.bats_hit_entry, min_value=0):
            self.bats_hit_entry.delete(0, tk.END)
            self.bats_hit_entry.focus_set()
            messagebox.showerror("Bats Hit Entry Error",
                                 "Ensure total bats hit entry is a positive whole numeric value.")
            return False

        if not self.validate_str(self.first_name_entry):
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.focus_set()
            messagebox.showerror("First Name Entry Error", "Ensure first name entry is alphabetical and not empty.")
            return False

        if not self.validate_str(self.last_name_entry):
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.focus_set()
            messagebox.showerror("Last Name Entry Error", "Ensure last name entry is alphabetical and not empty.")
            return False

        if not self.validate_position(self.position_entry):
            self.position_entry.delete(0, tk.END)
            self.position_entry.focus_set()
            messagebox.showerror("Position Entry Error",
                                 "Ensure position entry is a two symbol alphanumeric entry and not empty.")
            return False

        return True

    def store_input(self):
        if self.messagebox():
            playerID = self.player_entry.get()
            at_bats = self.total_bats_entry.get()
            total_hits = self.bats_hit_entry.get()
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            position = self.position_entry.get()

            print(
                f" Player ID: {playerID} || At Bats: {at_bats} || Total hit: {total_hits} || First Name: {first_name} || First Name: {last_name} || Position: {position}")

    def get_player_handler(self):
        pass

    def add_player_handler(self):
        pass

    def save_changes_handler(self):
        pass

    def cancel_handler(self):
        pass


class PlayerList:
    def __init__(self):
        pass 