"""Application entrypoint for Helper Fisica."""

import tkinter as tk

from app.ui.main_window import create_app


def main(root: tk.Tk | None = None) -> None:
    root = root or tk.Tk()
    create_app(root)
    root.mainloop()


if __name__ == "__main__":
    main()
