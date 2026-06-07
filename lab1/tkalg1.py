import tkinter as tk
from tkinter import filedialog
import alg1

def window(master):
    def calculate():
        Y1 = alg1.calculate(float(fields['a_entry'].get()), float(fields['b_entry'].get()))
        result.config(text=f"Result Y1: {Y1:.4f}")

    def save():
        filepath = filedialog.asksaveasfilename(
            title="Save file",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, 'w') as f:
                f.write(f"{fields['a_entry'].get()}\n")
                f.write(f"{fields['b_entry'].get()}\n")
        except Exception as e:
            result.config(text=f"Error: {e}")

    def load():
        filepath = filedialog.askopenfilename(
            title="Select save file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, 'r') as f:
                lines = f.read().splitlines()
                if len(lines) >= 2:
                    fields['a_entry'].delete(0, tk.END)
                    fields['a_entry'].insert(0, lines[0])
                    fields['b_entry'].delete(0, tk.END)
                    fields['b_entry'].insert(0, lines[1])
        except Exception as e:
            result.config(text=f"Error: {e}")

    fields = {}

    root = tk.Toplevel(master)
    root.configure(bg="white")
    root.title("Algorythm 1")
    root.geometry("300x330")

    fields['a_label'] = tk.Label(root, text="a")
    fields['a_entry'] = tk.Entry(root)
    fields['b_label'] = tk.Label(root, text="b")
    fields['b_entry'] = tk.Entry(root)

    image = tk.PhotoImage(file='lab1/alg1.png')
    formula = tk.Label(root, image=image, bg="white")
    formula.image = image
    formula.pack(anchor=tk.W, padx=10)

    for field in fields.values():
        field.pack(anchor=tk.W, padx=10, pady=5)
    
    result = tk.Label(root, text="Result Y1:", bg="white")
    
    frame = tk.Frame(root, bg="white")
    frame.pack(anchor=tk.W, padx=10, pady=5)

    tk.Button(frame, text='Calculate', command=calculate).pack(side=tk.LEFT, padx=10, pady=5)
    tk.Button(frame, text='Save',      command=save).pack(side=tk.LEFT, padx=10, pady=5)
    tk.Button(frame, text='Load',      command=load).pack(side=tk.LEFT, padx=10, pady=5)
    result.pack(anchor=tk.W, padx=10, pady=5)