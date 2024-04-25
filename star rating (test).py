import tkinter as tk
from tkinter import messagebox

class StarRating(tk.Frame):
    def __init__(self, master=None, numStars=5, callback=None):
        super().__init__(master)
        self.master = master
        self.numStars = numStars
        self.callback = callback
        self.createWidgets()

    def createWidgets(self):
        self.stars = []
        for i in range(self.numStars):
            star = tk.Label(self, text="⭐", font=("Arial", 20))
            star.bind("<Enter>", lambda event, idx=i: self.on_enter(idx))
            star.bind("<Leave>", lambda event, idx=i: self.on_leave(idx))
            star.bind("<Button-1>", lambda event, idx=i: self.on_click(idx))
            star.grid(row=0, column=i)
            self.stars.append(star)

    def on_enter(self, idx):
        for i in range(idx + 1):
            self.stars[i].config(fg="orange")

    def on_leave(self, idx):
        for i in range(idx + 1):
            self.stars[i].config(fg="black")

    def on_click(self, idx):
        if self.callback:
            self.callback(idx + 1)  # Rating is 1-based
            messagebox.showinfo("Rating", "You rated: {}".format(idx + 1))

def updateRating(rating):
    print("You rated:", rating)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Star Rating")

    rating_frame = StarRating(root, numStars=5, callback=updateRating)
    rating_frame.pack(pady=20)

    root.mainloop()
