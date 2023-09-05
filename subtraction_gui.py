from subtraction import subtraction
import tkinter as tk
from tkinter import ttk

# Create a window object
window = tk.Tk()
# Set the title of the window
window.title("Subtraction")
# Set the size of the window
window.geometry('350x200')
# create answer entry
answer = tk.StringVar()
answer_entry = ttk.Entry(window, width=7, textvariable=answer)
answer_entry.grid(column=1, row=1)
# create label for answer entry
answer_label = ttk.Label(window, text="Answer:")
answer_label.grid(column=0, row=1)
# create label for question
question_label = ttk.Label(window, text="What is 10 - 5?")
question_label.grid(column=0, row=0)
# create button
button = ttk.Button(window, text="Submit")
button.grid(column=2, row=1)
# create label for feedback
feedback_label = ttk.Label(window, text="You got it!")
feedback_label.grid(column=0, row=2)

# Run the window's main loop
window.mainloop()



