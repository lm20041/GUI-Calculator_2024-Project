import tkinter as tk 
from tkinter import messagebox

class MyGUICalculator:
  def __init__(self):
    self.root = tk.Tk() 
    self.root.geometry("400x400")
    self.root.title("My First GUI_Calculator-2024")
    self.label = tk.Label(self.root, text="Cal!", font=('Arial', 18))
    self.label.pack(padx=20, pady=10)
    #def
    
    ##--- menu Line ----
    self.menubar = tk.Menu(self.root)
    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Close", command=self.myclick)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Close without Question", command=exit)
    
    self.Switch_screens = tk.Menu(self.menubar, tearoff=0)
    self.Switch_screens.add_command(label="Program", command=self.myclick)
    self.Switch_screens.add_separator()
    self.Switch_screens.add_command(label="main", command=self.myclick)
    self.Switch_screens.add_separator()
    self.Switch_screens.add_command(label="Note", command=self.myclick)
    
    self.menubar.add_cascade(menu=self.filemenu, label="File")
    self.menubar.add_cascade(menu=self.Switch_screens, label="Switch Screens")
    
    self.root.config(menu=self.menubar)
    ##textbox
    self.textbox = tk.Text(self.root, height=3, font=('Arial', 16))
    self.textbox.pack()
    ##buttonFrame
    self.buttonFrame = tk.Frame(self.root)
    self.buttonFrame.columnconfigure(0, weight=1)
    self.buttonFrame.columnconfigure(1, weight=1)
    self.buttonFrame.columnconfigure(2, weight=1)
    #row1
    self.btn7 = tk.Button(self.buttonFrame, text="7", font=('Arial', 18))
    self.btn7.grid(row=0, column=0, sticky=tk.W+tk.E)
    self.btn8 = tk.Button(self.buttonFrame, text="8", font=('Arial', 18))
    self.btn8.grid(row=0, column=1, sticky=tk.W+tk.E)
    self.btn9 = tk.Button(self.buttonFrame, text="9", font=('Arial', 18))
    self.btn9.grid(row=0, column=2, sticky=tk.W+tk.E)
    self.btn_Del = tk.Button(self.buttonFrame, text="Del", font=('Arial', 18))
    self.btn_Del.grid(row=0, column=3, sticky=tk.W+tk.E)
    self.btn_Ac = tk.Button(self.buttonFrame, text="Ac", font=('Arial', 18))
    self.btn_Ac.grid(row=0, column=4, sticky=tk.W+tk.E)
    #row2
    self.btn4 = tk.Button(self.buttonFrame, text="4", font=('Arial', 18))
    self.btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
    self.btn5 = tk.Button(self.buttonFrame, text="5", font=('Arial', 18))
    self.btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
    self.btn6 = tk.Button(self.buttonFrame, text="6", font=('Arial', 18))
    self.btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
    self.btn_Times = tk.Button(self.buttonFrame, text="X", font=('Arial', 18))
    self.btn_Times.grid(row=1, column=3, sticky=tk.W+tk.E)
    self.btn_Divide = tk.Button(self.buttonFrame, text="/", font=('Arial', 18))
    self.btn_Divide.grid(row=1, column=4, sticky=tk.W+tk.E) 
    #row3 
    self.btn1 = tk.Button(self.buttonFrame, text="1", font=('Arial', 18))
    self.btn1.grid(row=2, column=0, sticky=tk.W+tk.E)
    self.btn2 = tk.Button(self.buttonFrame, text="2", font=('Arial', 18))
    self.btn2.grid(row=2, column=1, sticky=tk.W+tk.E)
    self.btn3 = tk.Button(self.buttonFrame, text="3", font=('Arial', 18))
    self.btn3.grid(row=2, column=2, sticky=tk.W+tk.E)
    self.btn_Add  = tk.Button(self.buttonFrame, text="+", font=('Arial', 18))
    self.btn_Add.grid(row=2, column=3, sticky=tk.W+tk.E)
    self.btn_Subtract = tk.Button(self.buttonFrame, text="-", font=('Arial', 18))
    self.btn_Subtract.grid(row=2, column=4, sticky=tk.W+tk.E) 
    #row4 dot power X10 answer equal
    self.btn0 = tk.Button(self.buttonFrame, text="0", font=('Arial', 18))
    self.btn0.grid(row=3, column=0, sticky=tk.W+tk.E)
    self.btn_Dot = tk.Button(self.buttonFrame, text=".", font=('Arial', 18))
    self.btn_Dot.grid(row=3, column=1, sticky=tk.W+tk.E)
    self.btn_X10 = tk.Button(self.buttonFrame, text="X10", font=('Arial', 18))
    self.btn_X10.grid(row=3, column=2, sticky=tk.W+tk.E)
    self.btn_Ans  = tk.Button(self.buttonFrame, text="Ans", font=('Arial', 18))
    self.btn_Ans.grid(row=3, column=3, sticky=tk.W+tk.E)
    self.btn_Equal = tk.Button(self.buttonFrame, text="=", font=('Arial', 18))
    self.btn_Equal.grid(row=3, column=4, sticky=tk.W+tk.E) 
    #row5 (empty row)
    self.buttonFrame.pack(fill='x')
    
    self.root.mainloop()
  def myclick(self):
    print("Hello World!")

MyGUICalculator()