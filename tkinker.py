from tkinter import * 
window = Tk()
label = Label(window, text="Hello World!")
button = Button(window, text="Click Me!")
label.pack()
button.pack()
window.geometry('350x200')
window.title("Welcome to LikeGeeks app")

window.mainloop()
