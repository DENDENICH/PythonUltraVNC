import tkinter as tk

from uploading import DataFavoriteManager, DataIPsManager
from interface import IPListApp


if __name__ == "__main__":
    d = DataIPsManager()

    root = tk.Tk()
    app = IPListApp(
        root=root,
        data_ips_manager=DataIPsManager(),
        data_favorite_manager=DataFavoriteManager()
    )
    root.mainloop()
