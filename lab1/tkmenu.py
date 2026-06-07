import tkinter as tk
import tkalg1, tkalg2, tkalg3

root = tk.Tk()
root.configure(bg="white")
root.title("Algorythm menu")
root.geometry("470x200")

tk.Label(text="Оберіть потрібний алгоритм: ").pack(anchor=tk.N, side="top")

buttons = {}
buttons['Alg1'] = tk.Button(text="Лінійний алгоритм", command=lambda: tkalg1.window(root))
buttons['Alg2'] = tk.Button(text="Алгоритм з розгалуженням", command=lambda: tkalg2.window(root))
buttons['Alg3'] = tk.Button(text="Циклічний алгоритм", command=lambda: tkalg3.window(root))

for button in buttons.values():
    button.pack(anchor=tk.W, side='left', padx=10, pady=5)

root.mainloop()