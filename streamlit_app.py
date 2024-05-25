import tkinter as tk

def update_label():
    label.config(text="Button clicked!")

# Create the main application window
app = tk.Tk()
app.title("Simple Python App")

# Create a label widget
label = tk.Label(app, text="Welcome to My App!", font=("Arial", 18))
label.pack(pady=20)

# Create a button widget
button = tk.Button(app, text="Click Me", command=update_label)
button.pack()

# Start the main event loop
app.mainloop()

