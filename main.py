import tkinter as tk

from uploading import DataFavoriteManager, DataIPsManager
from interface import IPListApp



if __name__ == "__main__":

    # root = tk.Tk()
    # objects = UploadIPsManager().object_ips
    # app = IPListApp(root, objects)
    # root.mainloop()
    d = DataFavoriteManager()
    d.upload_new({
        "Test_old": [
            "255.100.0.0/32",
        ]
    })
