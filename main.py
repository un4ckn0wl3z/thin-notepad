import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
# import qdarktheme


app = QApplication(sys.argv)
# qdarktheme.setup_theme()
app.setStyle("Fusion")

w = MainWindow(app)
w.show()
app.exec()