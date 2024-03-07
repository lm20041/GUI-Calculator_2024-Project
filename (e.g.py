import tkinter as tk
#messagebox
from tkinter import messagebox

class MyGUI:
  def __init__(self):
    self.root = tk.Tk() #windom
    self.root.geometry("400x400") #sides of windom
    self.root.title("My First GUI")
    #--- menu Line ----
    self.menubar = tk.Menu(self.root)
    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Close", command=self.on_closing)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Close without Question", command=exit)

    self.actionmenu = tk.Menu(self.menubar, tearoff=0)
    self.actionmenu.add_command(label="Show Messagebox", command=self.on_click)

    self.menubar.add_cascade(menu=self.filemenu, label="File")
    self.menubar.add_cascade(menu=self.actionmenu, label="Action")

    self.root.config(menu=self.menubar)
    #--                --


    self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
    self.label.pack(padx=10, pady=10)

    self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
    # bind <<KeyPress>>
    self.textbox.bind("<<KeyPress>>", self.shortcut)
    self.textbox.pack(padx=10, pady=10)

    self.check_state = tk.IntVar()
    self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
    self.check.pack(padx=10, pady=10)

    self.button = tk.Button(self.root, text="Click Me!", font=('Arial', 18), command=self.on_click)
    self.button.pack(padx=10, pady=10)

    #--------- clearbtn ---------
    self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
    self.clearbtn.pack(padx=10, pady=10)
    #---------          ---------

    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.root.mainloop()
  def on_click(self):
    print(self.check_state.get())
    if self.check_state.get() == 0:
      print(self.textbox.get('1.0', tk.END))
    else:
      messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

  def shortcut(self, event):
    print(event.keysym)
    print(event.state)
    if event.state == 12 and event.keysym == "Return":
      self.on_click()
  def on_closing(self):
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
      self.root.destroy()

  def clear(self):
    self.textbox.delete('1.0', tk.END)
MyGUI()