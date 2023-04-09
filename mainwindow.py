from PySide6.QtCore import Qt, QTextStream, QFile, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox, QFileDialog
from PySide6.QtGui import QIcon
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowTitle("Thin Notepad v0.0.2")

        appIcon = QIcon(":/images/book-open-list.png")
        self.setWindowIcon(appIcon)

        self.actionQuit.triggered.connect(self.quit)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.aboutQt)
        self.actionSave.triggered.connect(self.write_triggered)
        self.actionOpen.triggered.connect(self.open_triggered)

    def quit(self):
        self.app.quit()
    def copy(self):
        self.textEdit.copy()
    def cut(self):
        self.textEdit.cut()
    def paste(self):
        self.textEdit.paste()
    def undo(self):
        self.textEdit.undo()
    def redo(self):
        self.textEdit.redo()
    def about(self):
        QMessageBox.information(self,"Going pro!","QMainWindow, Qt Designer and Resources : Going pro!")
    def aboutQt(self):
        QApplication.aboutQt()



    def write_triggered(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File",
                                 ".",
                                 "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
        if((file_name == "")):
            return
        print("file :",file_name)
        file = QFile(file_name)
        if (not file.open(QIODevice.WriteOnly | QIODevice.Text)):
            return
        out = QTextStream(file)
        out << self.textEdit.toPlainText() << "\n"
        file.close()

        self.statusBar().showMessage("File saved!", 5000)


    def open_triggered(self):
        file_content = ""
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                 ".",
                                 "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
        if((file_name == "")):
            return
        print("Opened file :",file_name)
        file = QFile(file_name)
        if (not file.open(QIODevice.ReadOnly | QIODevice.Text)):
            return
        in_stream = QTextStream(file)
        while (not in_stream.atEnd()) :
            line = in_stream.readLine() + '\n'
            file_content += line
        file.close()
        self.textEdit.clear()
        self.textEdit.setText(file_content)

        self.statusBar().showMessage("File openned!", 5000)
        
