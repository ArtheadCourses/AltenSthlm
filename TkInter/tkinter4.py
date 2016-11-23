import tkinter as tk

def main():
    window = tk.Tk()

    def callback():
        print("Button click")

    btn = tk.Button(window, text="Click me", command=callback)
    btn.pack()

    window.mainloop()
    
if __name__ == '__main__':
    main()