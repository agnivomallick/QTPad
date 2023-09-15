from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import sys
import time

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()
        loadUi("splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap = QPixmap("splash_grad.jpg")
        self.setPixmap(pixmap)

    
    def progress(self):
        for i in range(101):
            time.sleep(0.1)
            self.prog.setValue(i)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("window.ui", self)

        self.currentFileName = None
        self.defaulttheme.triggered.connect(self.lightmode)
        self.blacktheme.triggered.connect(self.darktheme)
        self.exit.triggered.connect(self.closeapp)
        self.undo.triggered.connect(self.undoText)
        self.redo.triggered.connect(self.redoText)
        self.copy.triggered.connect(self.copyText)
        self.cut.triggered.connect(self.cutText)
        self.paste.triggered.connect(self.pasteText)

        self.newact.triggered.connect(self.newFile)
        self.open.triggered.connect(self.openFile)
        self.save.triggered.connect(self.saveFile)
        self.saveas.triggered.connect(self.saveFileAs)

    def undoText(self):
        self.textEdit.undo()

    def redoText(self):
        self.textEdit.redo()

    def cutText(self):
        self.textEdit.cut()

    def copyText(self):
        self.textEdit.copy()

    def pasteText(self):
        self.textEdit.paste()

    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")

    def openFile(self):
        path = QFileDialog.getOpenFileName(self, "Open file", "C:\\", "All Files (*),Text file (*.txt)")
        self.setWindowTitle(path[0])

        with open(path[0], "r") as file:
            text = file.read()
            self.textEdit.setText(text)

        self.currentFileName = path[0]

    def saveFile(self):
        if self.currentFileName is not None:
            with open(self.currentFileName, 'w') as file:
                fileText = self.textEdit.toPlainText()
                file.write(fileText)
                file.close()
        else:
            self.saveFileAs()


    def saveFileAs(self):
        path = QFileDialog.getSaveFileName(self, "Save as", "C:\\", "All Files (*),Text file (*.txt)")
        if path[0] == '':
            msg = QMessageBox(self)
            msg.setWindowTitle("Cancelled Action")
            msg.setIcon(QMessageBox.Information)
            msg.setText("You cancelled the action.")
            msg.setDetailedText("You cancelled the Save as action. No worries, edit your text.")
            show = msg.exec_()

        else: 
            fileText = self.textEdit.toPlainText()
    
            with open(path[0], 'w') as file:
                file.write(fileText)
                file.close()
                self.currentFileName = path[0]
                self.setWindowTitle(path[0])



    def lightmode(self):
        self.setStyleSheet("")

    def darktheme(self):
       self.setStyleSheet("""
           QWidget {
           background-color: black;
           color: white;
           }
           
           QTextEdit {
           background-color: #2e2e2e;
           }
           QMenuBar::item:selected {
           color: black;
           }
        """)
       
    def closeapp():
        exit()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    splash=SplashScreen()
    splash.show()
    splash.progress()
    
    win = MainWindow()
    win.show()
    
    splash.finish(win)
    app.exec_()