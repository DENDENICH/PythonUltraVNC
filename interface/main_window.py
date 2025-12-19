import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip  # для работы с буфером обмена
from typing import List, Dict, Optional

from uploading import (
    DataIPsManager,
    DataFavoriteManager
)
from errors import FileNotFound, OtherException
from utils.connect_to_vnc import connect_vnc


class IPListApp:
    """
    Главное UI окно приложения
    """
    def __init__(
            self,
            root: tk.Tk,
            data_ips_manager: DataIPsManager,
            data_favorite_manager: DataFavoriteManager
    ):
        self.root = root
        self.data_ips_manager = data_ips_manager
        self.data_favorite_manager = data_favorite_manager

        self.section_widgets: Optional[str, Dict[List]] = dict()

        self.root.title("Список IP с копированием")
        self.root.geometry("800x600")

        # Создаем фрейм для секций
        # self.frame = ttk.Frame(root)
        # self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Создаем Canvas с прокруткой
        self.canvas = tk.Canvas(root)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Настраиваем Canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Размещаем элементы в главном окне
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Обработчик изменения размера содержимого
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self._build_ui()

    def _build_ui(self):
        """Строит UI на основе переданных данных"""
        row = 0
        try:
            for section_name, ip_objects in self.data_ips_manager.get_data().items():
                # Заголовок секции с обработчиком клик
                header_label = ttk.Label(
                    self.scrollable_frame,
                    text=section_name,
                    font=("Arial", 12, "bold"),
                    cursor="hand2"  # визуальная подсказка, что элемент кликабелен
                )
                header_label.grid(row=row, column=0, columnspan=3, pady=(0, 10), sticky="w")
                header_label.bind("<Button-1>", lambda event, name=section_name: self._toggle_section(name))

                # Хранилище виджетов секции (для управления видимостью)
                self.section_widgets[section_name] = []
                row += 1

                # Список IP с кнопками (изначально скрытый)
                for ip in ip_objects:
                    # Контейнер для строки IP + комментарий
                    container = ttk.Frame(self.scrollable_frame)
                    container.grid(row=row, column=0, columnspan=3, sticky="ew", pady=5)
                    container.grid_remove()  # изначально скрываем

                    # Надпись IP адреса
                    ip_label = ttk.Label(container, text=ip.ip)
                    ip_label.pack(side="left", padx=(0, 10))

                    # Кнопка копирования IP
                    copy_btn = ttk.Button(
                        container,
                        text="подключиться",
                        command=lambda ip_adr=ip.ip: self._connect_to_server(ip_adr)
                    )
                    copy_btn.pack(side="right")

                    # Комментарий (справа от IP)
                    comment_label = ttk.Label(container, text=ip.comment, foreground="gray")
                    comment_label.pack(side="left", padx=(10, 0))

                    # Сохраняем виджеты секции для управления видимостью
                    self.section_widgets[section_name].append(container)
                    row += 1

                # Отступ между секциями
                separator = ttk.Separator(self.scrollable_frame, orient="horizontal")
                separator.grid(row=row, column=0, columnspan=3, sticky="ew", pady=20)
                separator.grid_remove()  # скрываем изначально
                self.section_widgets[section_name].append(separator)

                row += 1
        except FileNotFound as e:
            self._show_critical_error("Файл не найден", e.message)
        except OtherException as e:
            self._show_critical_error("Не предвиденная ошибка", e.message)

    def _toggle_section(self, section_name):
        """Переключает видимость секции при клике на заголовок"""
        widgets = self.section_widgets.get(section_name, [])
        if not widgets:
            return

        # Проверяем состояние первого виджета (если виден — скрываем, иначе показываем)
        is_visible = widgets[0].winfo_ismapped()

        for widget in widgets:
            if is_visible:
                widget.grid_remove()
            else:
                widget.grid()

        # Обновляем область прокрутки после изменения видимости
        self.scrollable_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _connect_to_server(self, ip: str) -> None:
        """Запускает UltraVNC с заданым ip"""
        try:
            connect_vnc(ip)
        except FileNotFound as e:
            self._show_critical_error("Файл не найден", e.message)
        except OtherException as e:
            self._show_critical_error("Ошибка", e.message)

    @staticmethod
    def _copy_to_clipboard(ip: str) -> None:
        """Копирует IP (с префиксом) в буфер обмена"""
        # Формируем строку для копирования (добавляем префикс)
        pyperclip.copy(ip)

    @staticmethod
    def _show_critical_error(title: str, message: str):
        """
        Отображает окошко с критической ошибкой

        :param title: заголовок окна ошибки
        :param message: текст ошибки
        """
        messagebox.showerror(
            title=title,
            message=f"{message}\n\n"
        )
