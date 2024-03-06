# Create a window
import tkinter as tk 
Screen = tk.Tk() 
#sides of the window
root.geometry("400x400")
#title of the window
root.title("My First GUI")
#create a label
label = tk.Label(root, text="Hello World!", font=('Arial', 18))
#place the label in the window
label.pack(padx=20, pady=20)
#place the textbox in the window
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()
#button
button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()