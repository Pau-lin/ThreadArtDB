from src.core.db import Database
from src.utils.config import get_config
from src.utils.args import parse_arguments
from src.gui.main_window import MainWin

from PyQt6.QtWidgets import QApplication, QWidget
import sys

def main():
    config = get_config()['database']
    db = Database(config['host'],config['database'],config['user'],config['password'])

    app = QApplication(sys.argv)

    window = MainWin()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    parse_arguments()
    main()
