import re
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip  # для работы с буфером обмена

class IPListApp:
    def __init__(self, root, data: dict[str, list[str]]):
        self.root = root
        self.data = data
        self.root.title("Список IP с копированием")
        self.root.geometry("600x400")

        # Создаем фрейм для секций
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self._build_ui()

    def _build_ui(self):
        """Строит UI на основе переданных данных"""
        row = 0
        for section_name, ip_list in self.data.items():
            # Заголовок секции
            ttk.Label(self.frame, text=section_name, font=("Arial", 12, "bold")).grid(
                row=row, column=0, columnspan=2, pady=(0, 5), sticky="w"
            )
            row += 1

            # Список IP с кнопками
            for ip in ip_list:
                ttk.Label(self.frame, text=ip).grid(row=row, column=0, sticky="w", padx=(0, 10))
                copy_btn = ttk.Button(self.frame, text="скопировать ip", command=lambda ip: self._copy_to_clipboard(ip))
                copy_btn.grid(row=row, column=1, sticky="e")
                row += 1

            # Отступ между секциями
            ttk.Separator(self.frame, orient="horizontal").grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
            row += 1

    def _copy_to_clipboard(self, ip: str):
        """Копирует IP (с префиксом) в буфер обмена"""
        # Формируем строку для копирования (добавляем префикс)
        copy_text = f"{ip}/dat"
        pyperclip.copy(copy_text)
        messagebox.showinfo("Копирование", f"Скопировано в буфер: {copy_text}")

