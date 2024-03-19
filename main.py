import tkinter as tk

class Calculator:
  def __init__(self, root):
    self.root = root
    self.root.title("Calculator")

    self.expression = ""
    self.input_text = tk.StringVar()

    self.entry = tk.Entry(root, textvariable=self.input_text, font=('Arial', 20), bd=5, insertwidth=4, width=14, justify='right')
    self.entry.grid(row=0, column=0, columnspan=4)

    self.create_buttons()

  def create_buttons(self):
    buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

    for (text, row, col) in buttons:
      button = tk.Button(self.root, text=text, font=('Arial', 20), command=lambda t=text: self.on_button_click(t))
      button.grid(row=row, column=col)

  def on_button_click(self, value):
    if value == '=':
      try:
        self.expression = str(eval(self.expression))
      except:
        self.expression = "Error"
    elif value == 'C':
      self.expression = ""
    else:
      self.expression += value

    self.input_text.set(self.expression)

if __name__ == "__main__":
  root = tk.Tk()
  calculator = Calculator(root)
  root.mainloop()