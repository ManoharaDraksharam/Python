import tkinter as tk

class  myGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('My first GUI')

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=("Arial", 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state =tk.IntVar()

        self.check = tk.Checkbutton(self.root,text="Show Messsage", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)


        self.root.mainloop()

    def show_message(self):
        print("Hello World")

myGUI()