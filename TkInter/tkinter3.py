import tkinter as tk
def main():
    window = tk.Tk()

    colors = ['red', 'yellow', 'pink', 'green', 'purple', 'orange', 'blue']

    for color in colors:
        btn = tk.Button(window, text=color, bg=color)
        btn.pack(fill=tk.X)


    window.mainloop()
    
if __name__ == '__main__':
    main()