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
    self.filemenu.add_command(label="Close without Question", command=exit) #
    self.filemenu.add_separator()
    self.filemenu.add_command(label="show Messagebox", command=self.ShowMessagebox)
    
    self.switch_screen = tk.Menu(self.menubar, tearoff=0)
    self.switch_screen.add_command(label="Program", command=self.SwitchScreens)
    self.switch_screen.add_separator()
    self.switch_screen.add_command(label="main", command=self.SwitchScreens)
    self.switch_screen.add_separator()
    self.switch_screen.add_command(label="Note", command=self.SwitchScreens)
    
    self.menubar.add_cascade(menu=self.filemenu, label="File")
    self.menubar.add_cascade(menu=self.switch_screen, label="Switch Screens")
    
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
    self.btn7 = tk.Button(self.buttonFrame, text="7", font=('Arial', 18), command=self.Num7)
    self.btn7.grid(row=0, column=0, sticky=tk.W+tk.E)
    self.btn8 = tk.Button(self.buttonFrame, text="8", font=('Arial', 18), command=self.Num8)
    self.btn8.grid(row=0, column=1, sticky=tk.W+tk.E)
    self.btn9 = tk.Button(self.buttonFrame, text="9", font=('Arial', 18), command=self.Num9)
    self.btn9.grid(row=0, column=2, sticky=tk.W+tk.E)
    self.btn_Del = tk.Button(self.buttonFrame, text="Del", font=('Arial', 18), command=self.SymDel)
    self.btn_Del.grid(row=0, column=3, sticky=tk.W+tk.E)
    self.btn_Ac = tk.Button(self.buttonFrame, text="AC", font=('Arial', 18), command=self.SymAC)
    self.btn_Ac.grid(row=0, column=4, sticky=tk.W+tk.E)
    #row2
    self.btn4 = tk.Button(self.buttonFrame, text="4", font=('Arial', 18), command=self.Num4)
    self.btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
    self.btn5 = tk.Button(self.buttonFrame, text="5", font=('Arial', 18), command=self.Num5)
    self.btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
    self.btn6 = tk.Button(self.buttonFrame, text="6", font=('Arial', 18), command=self.Num6)
    self.btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
    self.btn_Times = tk.Button(self.buttonFrame, text="X", font=('Arial', 18), command=self.SymTime)
    self.btn_Times.grid(row=1, column=3, sticky=tk.W+tk.E)
    self.btn_Divide = tk.Button(self.buttonFrame, text="/", font=('Arial', 18), command=self.SymDivide)
    self.btn_Divide.grid(row=1, column=4, sticky=tk.W+tk.E) 
    #row3 
    self.btn1 = tk.Button(self.buttonFrame, text="1", font=('Arial', 18), command=self.Num1)
    self.btn1.grid(row=2, column=0, sticky=tk.W+tk.E)
    self.btn2 = tk.Button(self.buttonFrame, text="2", font=('Arial', 18), command=self.Num2)
    self.btn2.grid(row=2, column=1, sticky=tk.W+tk.E)
    self.btn3 = tk.Button(self.buttonFrame, text="3", font=('Arial', 18), command=self.Num3)
    self.btn3.grid(row=2, column=2, sticky=tk.W+tk.E)
    self.btn_Add  = tk.Button(self.buttonFrame, text="+", font=('Arial', 18), command=self.SymAdd)
    self.btn_Add.grid(row=2, column=3, sticky=tk.W+tk.E)
    self.btn_Subtract = tk.Button(self.buttonFrame, text="-", font=('Arial', 18), command=self.SymSubtract)
    self.btn_Subtract.grid(row=2, column=4, sticky=tk.W+tk.E) 
    #row4 dot power X10 answer equal
    self.btn0 = tk.Button(self.buttonFrame, text="0", font=('Arial', 18), command=self.Num0)
    self.btn0.grid(row=3, column=0, sticky=tk.W+tk.E)
    self.btn_Dot = tk.Button(self.buttonFrame, text=".", font=('Arial', 18), command=self.SymDot)
    self.btn_Dot.grid(row=3, column=1, sticky=tk.W+tk.E)
    self.btn_X10 = tk.Button(self.buttonFrame, text="X10", font=('Arial', 18), command=self.SymX10)
    self.btn_X10.grid(row=3, column=2, sticky=tk.W+tk.E)
    self.btn_Ans  = tk.Button(self.buttonFrame, text="Ans", font=('Arial', 18), command=self.SymAns)
    self.btn_Ans.grid(row=3, column=3, sticky=tk.W+tk.E)
    self.btn_Equal = tk.Button(self.buttonFrame, text="=", font=('Arial', 18), command=self.SymEqual)
    self.btn_Equal.grid(row=3, column=4, sticky=tk.W+tk.E) 
    #row5 (empty row)
    self.buttonFrame.pack(fill='x')
    
    self.root.mainloop()
  #TabBars Frame Def's
  def ShowMessagebox(self):
    pass
    
  def SwitchScreens(self):
    pass
  # Show Frame Def's
  def show_CAL(self):
    pass
  #main Cal
  def CAL(self, input):
    print(input)
  #button Frame Def's-number
  def Num1(self):
    self.CAL(1)
    
  def Num2(self):
    pass
  def Num3(self):
    pass
  def Num4(self):
    pass
  def Num5(self):
    pass
  def Num6(self):
    pass
  def Num7(self):
    pass
  def Num8(self):
    pass
  def Num9(self):
    pass
  def Num0(self):
    pass
  
  #button Frame Def's-symble
  def SymDel(self):
    pass
  def SymAC(self):
    self.textbox.delete('1.0', tk.END)
  def SymTime(self):
    pass
  def SymDivide(self):
    pass
  def SymAdd(self):
    pass
  def SymSubtract(self):
    pass
  def SymDot(self):
    pass
  def SymX10(self):
    pass
  def SymAns(self):
    pass
  def SymEqual(self):
    pass
  
  

  def myclick(self):
    print('hi hi hi')
  

MyGUICalculator()