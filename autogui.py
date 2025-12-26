"""Auto-generate GUI from function type hints."""

from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QSpinBox,
)
from PySide2.QtCore import Slot, Qt
from typing import Dict, List, get_origin, get_args


def example(a: int, b: str, c: List[int]):
    """Example function with typed parameters."""
    print(f"{a} {b}")


class GuiException(Exception):
    """Exception raised for GUI generation errors."""

    pass


class autogui:
    """Auto-generate a GUI from function type hints."""

    def __init__(self, func):
        """Initialize autogui with a function."""
        print("read type hints, and make a gui to call function.")
        self.func = func
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.submit = QPushButton("call function")
        self.submit.clicked.connect(self.callFunction)
        self.widgets = []
        self.anames = []

        for name, t in func.__annotations__.items():
            if name == "return":
                continue
            self.anames.append(name)
            label = QLabel(f"{name}:")
            self.layout.addWidget(label)

            origin = get_origin(t)
            if origin is not None:
                # Handle generic types like List[int]
                widget = QLineEdit()
                widget.setPlaceholderText(f"Enter {name} (comma-separated)")
            elif t == int or (isinstance(t, type) and issubclass(t, int)):
                widget = QSpinBox()
            elif t == str or (isinstance(t, type) and issubclass(t, str)):
                widget = QLineEdit()
                widget.setPlaceholderText(f"Enter {name}")
            else:
                raise GuiException(f"unknown argument type {t}")

            self.widgets.append(widget)
            self.layout.addWidget(widget)

        self.layout.addWidget(self.submit)
        self.window.setLayout(self.layout)

        print(dir(func.__annotations__))

    @Slot()
    def callFunction(self):
        """Call the wrapped function with widget values."""
        args = []
        for widget in self.widgets:
            if isinstance(widget, QSpinBox):
                args.append(widget.value())
            elif isinstance(widget, QLineEdit):
                args.append(widget.text())
        self.func(*args)

    def run(self):
        """Show the window and run the application."""
        self.window.show()
        return self.app.exec_()


if __name__ == "__main__":
    gui = autogui(example)
    gui.run()
