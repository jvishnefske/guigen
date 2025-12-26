from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Slot, Qt
from typing import Dict, List


def example(a:int, b:str, c:List[int]):
	print(f'{a} {b}')
	
class GuiException(Exception):
    pass



class autogui:
    def __init__(self, func):
        print("read type hints, and make a gui to call function.")
        ## iterate throuth arguments, and make a list of 
        app = QApplication()
        self.layout = QVBoxLayout()
        self.submit = QPushButton("call function")
        self.submit.clicked.connect(self.callFunction)
        self.widgets=[]
        self.anames =[]
        for name, t in func.__annotations__.items():
            self.anames.append(name)
            if issubclass(t,int):
                print(f'{name} int')
                self.widgets.append(
            elif t == string
                self.widgets.append(Q
            else:
                raise GuiException(f"unknown argument type {t}")
        for w in self.widgets:
            self.layout.addWidget(w)
        app.setLayout(self.layout)
        
        print (dir(func.__annotations__), func.__anno)
    def callFunction(self):
        for w in widgets
autogui(example)