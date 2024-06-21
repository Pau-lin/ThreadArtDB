from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget, QTabWidget, QApplication, QLineEdit, QTableWidget
import sys

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ThreadArtDB")
        self.showMaximized()

        tabs = self.init_tabs()
        dbsection = self.init_dbsection() 
        
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        layout.addWidget(dbsection)
         
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        print(self.table)

    def init_tabs(self):
        tabs = QTabWidget()
        for i in range(3):
                    tab = QWidget()
                    tabs.addTab(tab, f"Onglet {i + 1}")
                    self.setup_tab(tab, i + 1)
        return tabs

    def setup_tab(self, tab, tab_number):
        layout = QVBoxLayout()
        label = QLabel(f"Contenu de l'onglet {tab_number}")
        layout.addWidget(label)
        tab.setLayout(layout)

    def init_dbsection(self):
        text = QLineEdit()
        self.table = QTableWidget()

        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        return container
        
    def structure_table(self, table):
        return
