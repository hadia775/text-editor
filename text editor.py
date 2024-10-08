import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# Create a Text widget
text_area = tk.Text(root, undo=True)
text_area.pack(expand=True, fill='both')

# Functions for File Menu
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)  # Clear the text area
            text_area.insert(tk.END, file.read())  # Insert the file's content

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))  # Write the content of text area to the file

def quit_editor():
    root.quit()

# Functions for Edit Menu
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

# Function for Help Menu
def show_help():
    messagebox.showinfo("Help", "This is a simple text editor using Tkinter.\n\n"
                                "File -> Open: Open a text file\n"
                                "File -> Save: Save the current text\n"
                                "Edit -> Cut, Copy, Paste: Standard editing functions.")

# Create a Menu bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_help)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

# Start the application
root.mainloop()
