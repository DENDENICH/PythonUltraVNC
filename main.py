import tkinter as tk

from uploading import UploadIPsManager
from interface import IPListApp

import json

if __name__ == "__main__":

    root = tk.Tk()
    objects = UploadIPsManager().object_ips
    app = IPListApp(root, objects)
    root.mainloop()
