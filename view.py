import customtkinter as ctk


class View(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gym Tracker v1.0")
        self.minsize(400, 300)
        self.frame = SessionInput(self)
        self.frame.grid(row=0, column=0, padx=20, pady=20)


class SessionInput(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame_elements = []

        self.title = ctk.CTkLabel(self, text="Add the exercises of the day!")
        self.title.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.button_plus = ctk.CTkButton(self, text="+", width=15, height=15, command=self.create_input)
        self.button_plus.grid(row=1, column=0, padx=0, pady=5)

        self.button_minus = ctk.CTkButton(self, text="-", width=15, height=15, command=self.delete_input)
        self.button_minus.grid(row=1, column=1, padx=0, pady=5)

        # Create 4 exercise options by default
        for _index in range(4):
            self.create_input()

    def create_input(self):
        _index = len(self.frame_elements)
        label = ctk.CTkLabel(self, text="Exercise %s:" % str(_index+1))
        label.grid(row=_index+2, column=0, padx=10, pady=10)

        entry = ctk.CTkEntry(self, width=60, height=15, border_width=1.5, corner_radius=10)
        entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        entry.grid(row=_index+2, column=1, padx=10, pady=10)
        # Save label and entry references to frame_elements
        self.frame_elements.append((label, entry))

    def delete_input(self):
        if len(self.frame_elements) > 1:
            self.frame_elements[-1][0].destroy()
            self.frame_elements[-1][1].destroy()
            del self.frame_elements[-1]


if __name__ == "__main__":
    view = View()
    view.mainloop()
