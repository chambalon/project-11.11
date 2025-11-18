import tkinter as tk
import os
import shutil
from tkinter import filedialog, messagebox, simpledialog


class FileManagerApp:
  def __init__(self,root):
    self.root = root
    self.root.title("File Manager")
    # Initial size of the window
    self.root.geometry("600x400")
    self.current_dir_path = os.getcwd()
    self.create_widgets()
    self.update_listbox()

  def create_widgets(self):
    self.path_label = tk.Label(self.root, text=self.current_dir_path)
    self.path_label.pack()
    self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
    self.listbox.pack(expand=True, fill=tk.BOTH)
    self.listbox.bind('<Double-l>', self.on_item_double_click)
    self.buttons_frame = tk.Frame(self.root)
    self.buttons_frame.pack(fill=tk.X)
    self.create_file_btn = tk.Button(self.buttons_frame, text="Create File", command=self.create_file)
    self.create_file_btn.pack(side=tk.LEFT)
    self.create_folder_btn = tk.Button(self.buttons_frame, text="Create Folder", command=self.create_folder)
    self.create_folder_btn.pack(side=tk.LEFT)
    self.delete_btn = tk.Button(self.buttons_frame, text="Delete", command=self.delete_item)
    self.delete_btn.pack(side=tk.LEFT)
    self.copy_btn = tk.Button(self.buttons_frame, text="Copy", command=self.copy_item)
    self.copy_btn.pack(side=tk.LEFT)
    self.move_btn = tk.Button(self.buttons_frame, text="Move", command=self.move_item)
    self.move_btn.pack(side=tk.LEFT)


  def update_listbox(self):
    self.listbox.delete(0, tk.END)
    self.path_label.config(text=self.current_dir_path)
    for item in os.listdir(self.current_dir_path):
      self.listbox.insert(tk.END, item)
    

  def on_item_double_click(self, event):
    selected_item = self.listbox.get(self.listbox.curselection())
    selected_path = os.path.join(self.current_dir_path, selected_item)
    if os.path.isdir(self.selected_path):
      self.current_dir_path = selected_path
      self.update_listbox()


  def create_file(self):
    filename = simpledialog.askstring("Create File", "Enter the filename: ")
    if filename:
      open(os.path.join(self.current_dir_path, filename), 'w').close()
      self.update_listbox()


  def create_folder(self):
    foldername = simpledialog.askstring("Create Folder", "Enter the foldername: ")
    if foldername:
      os.makedirs(os.path.join(self.current_dir_path, foldername), exist_ok=True)
      self.update_listbox()


  def delete_item(self):
    selected_item = self.listbox.get(self.listbox.curselection())
    selected_path = os.path.join(self.current_dir_path, selected_item)
    if os.path.isfile(selected_path):
      os.remove(selected_item)
    elif os.path.isdir(selected_item):
      shutil.rmtree(selected_item)
    self.update_listbox()



  def copy_item(self):
    selected_item = self.listbox.get(self.listbox.curselection())
    src_path = os.path.join(self.current_dir_path, selected_item)
    dst_path = filedialog.askdirectory(title="Select destination directory")
    if dst_path:
      if os.path.isdir(src_path):
        shutil.copytree(src_path, (os.path.join(dst_path, os.path.basename(src_path))))
      else:
        shutil.copy2(src_path, dst_path)
      self.update_listbox()


  def move_item(self):
    selected_item = self.listbox.get(self.listbox.curselection())
    src_path = os.path.join(self.current_dir_path, selected_item)
    dst_path = filedialog.askdirectory(title="Select destination directory")
    if dst_path:
      shutil.move(src_path, dst_path)
      self.update_listbox()



if __name__ == '__main__':
  # Main window
  root = tk.Tk()
  app = FileManagerApp(root)
  # Keep the window open by running the Tkinter event loop
  root.mainloop()
