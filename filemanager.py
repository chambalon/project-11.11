import tkinter as tk
import os
import shutil
from tkinter import filedialog, messagebox


class FileManagerApp:
  def __init__(self,root):
    self.root = root
    self.root.title("File Manager")
    # Initial size of the window
    self.root.geometry("600x400")
    self.create_widgets()
    #self.update_files()

  def create_widgets(self):
    self.label1 = tk.Label(self.root, text="path")
    self.label1.pack()
    


if __name__ == '__main__':
  # Main window
  root = tk.Tk()
  app = FileManagerApp(root)
  # Keep the window open by running the Tkinter event loop
  root.mainloop()
