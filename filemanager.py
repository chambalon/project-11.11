import tkinter as tk
import os
import shutil
from tkinter import filedialog, messagebox, simpledialog
import dropbox
import dropbox.exceptions


class FileManagerApp:
  def __init__(self,root):
    self.root = root
    self.root.title("File Manager")
    # Initial size of the window
    self.root.geometry("600x400")
    self.current_dir_path = os.getcwd()
    self.create_widgets()
    self.update_listbox()
    self.ACCESS_TOKEN = 'sl.u.AGEmUEli2RkQbxWXQSLYfOChNYTynCyDRRrWe2IGfNjLo6ikuc_LzZ24QKNwr5j0btTC-vbD5ihfMM0JkxBanA1kCMP6OqudS16FPOG7KVhownwvEoh7JEsmkt8ZQTZafDS8hVqnbwGw-ye8pcydECjTkweOWlOsjhjMP6T72g6zB-xc6iZ70cJpbXcUbvZ_ktKnNqTMlAamLsttsUvJDXqjqy7ly3U1FrohL2FTD5gTca5pMyb0MA9QGbU4_e-yl_Y8t0gfGgzfsa0O5wVAfuMF-vI0zpFNevTLIcsOaT2i9SqnAsn18LFOCvelo5aiZ96Wu0_Ei_HcuhUdxTeURvYb060VZKOc3nPZvPUzgdoVVetoPytnLzgmFe6Lg67nM1ZFqvyCRgCrX82FU9i6klbKwFeCOl01pvyf4dhCuwmnxGWl6DMREscNTDeHFXkvfaBvrDxiQIw9Z9rgg6pGmukFRvviiY8lPPQEo4QFoLSMB7e8tV9j3eeE0Si1Nwlr123xFdPYI4033koiEJ3sEWOGpX6JZ6P4OH59ulXJ473PXrjBb1vhHYbyca1mMcqrx8RDWMvzYGaBM2LVNUeHjPBWe2hHyi-9WGOPsLgtcyvi0QUBrrjq8ssw3zdPL15KiuyHSddpRqneZDlmyAwvNcd31n2T1pMUFuFDrQlcVtNvhTTQSk2l1EOk5iktheWxJ29O2lR2sMpxnIv8F-g8wJy94msWyoM5QQz7SRTffdvlGNFkxJFrOaMwIaVCBIBvmtUwI1vcNZ3__GJyslWO23Eln6j_hJw78fUuu7Wm1UknIrxUsrC6uaD99Gc8ZBWiSc97q0ZjP1x0a_tQ03l3_Nai8y-FmRwNwbnT_hO-X6RQ9DVCLiKWsDnXW6bFhLxQpSKJXtNf-tiarfj-YhSDs9SBz2hLqUFBp066bcahjAidUdxfw6FsfXriOkjZ2oanIhtzNMjdAkK7SLpJK-t7noxZyDaA7OYUU0s5htdI5kRZV1wjKK-Y5L4QFKZ7fvEE7QZ3uaXhTmLvJUY4B6n2vaOWxlEWAZ87RAw5FsVsUqG22OTAqkJtjjnmWXXZ_8uFN8ror2dHa2gQRErsFe6mZxv1_xmP0cLtQ3E079afiPQnSDVbe9DwdiRHLz1QkQ1f-SevrDIxpoTiyRNtP0M9Eh6afv47vTMS1Yb2gLlCWC13BnYfarKzwyakUKWPkCSPwLU2TFquVuQzVunfOvZ2kBTdVr_OZc27hgoLf-kRsZucgfe0NQ2jocB9PeInWs0CMqD6UkVjLnGFk802vtBDVDUAOg5K0_9eSHix_QGBtWkVbjI46y0nOK0E46qPH-BOxBbfOmsRHR_cVjH2fAy359xOrKnGlM0rUqQzmgddWKJpbfPyzU1syfhHdhW-mYxDbM1sJajEn-jd43IgpfMqXsWj'
  
  
  
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
    self.dropbox_btn = tk.Button(self.buttons_frame, text="List dropbox files", command=self.list_dropbox_files)
    self.dropbox_btn.pack(side=tk.RIGHT)


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


  def list_dropbox_files(self):
    try:
      dbx = dropbox.Dropbox(self.ACCESS_TOKEN)
      result = dbx.files_list_folder('')
      self.listbox.delete(0, tk.END)
      for entry in result.entries:
        self.listbox.insert(tk.END, entry.name)
    except dropbox.exceptions.AuthError as e:
      print(f"Error connecting to dropbox with access tokem: {e}")
    except Exception as e:
      print(f"An error occured {e}")
  



if __name__ == '__main__':
  # Main window
  root = tk.Tk()
  app = FileManagerApp(root)
  # Keep the window open by running the Tkinter event loop
  root.mainloop()
