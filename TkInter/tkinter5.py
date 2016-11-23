import tkinter as tk

def main():
    window = tk.Tk()

    def callback():
        print("We got:", var1.get())

    var1 = tk.StringVar()
    entry = tk.Entry(window)
    entry['textvariable'] = var1
    entry.pack()

    btn = tk.Button(window, text="Click me", command=callback)
    btn.pack()

    window.mainloop()
    
if __name__ == '__main__':
    main()