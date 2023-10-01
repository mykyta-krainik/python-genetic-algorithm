import tkinter as tk


class UI:
    def __init__(self):
        self._window = tk.Tk()

    @staticmethod
    def _create_btn(text: str, row: int, column: int, on_click: callable):
        btn = tk.Button(text=text, command=on_click)
        btn.grid(row=row, column=column)

        return btn

    @staticmethod
    def _create_entry_with_label(
        label_text: str, row: int, label_column: int, padx=0, pady=0
    ) -> dict:
        label = UI._create_label(label_text, row, label_column, padx, pady)
        entry = UI._create_entry(row, label_column + 1)

        return {"label": label, "entry": entry}

    @staticmethod
    def _create_label(label_text: str, row: int, column: int, padx=0, pady=0):
        label = tk.Label(text=label_text, padx=padx, pady=pady)
        label.grid(row=row, column=column)

        return label

    @staticmethod
    def _create_entry(row: int, column: int):
        entry = tk.Entry()
        entry.grid(row=row, column=column + 1)

        return entry
