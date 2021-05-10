import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sqlite3


class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
        self.connect()
    def  connect(self):
        con = sqlite3.connect("database.db")

        self.cursor = con.cursor()

        self.cursor.execute("Create Table If not exists books (book_name TEXT,author TEXT,page TEXT)")
        con.commit()


    def init_ui(self):
        self.book_name = QtWidgets.QLineEdit()
        self.author = QtWidgets.QLineEdit()
        self.bsearch = QtWidgets.QPushButton("Search")
        self.text_area = QtWidgets.QLabel("")
        self.text_area2 = QtWidgets.QLabel("")
        self.sticker1 = QLabel("Book name")
        self.sticker2 = QLabel("Author")

        self.sticker1.setStyleSheet("color: white;")
        self.sticker2.setStyleSheet("color: white;")

        self.setWindowTitle("ACBlibrary")
        self.setGeometry(100,100,600,500)
        self.label = QLabel(self)
        self.pixmap = QPixmap('space.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.text_area.setStyleSheet("color: blue;")
        self.text_area2.setStyleSheet("color: red;")
        self.text_area2.setFont(QtGui.QFont('Arial',20))
        self.text_area.setFont(QtGui.QFont('Arial', 20))
        self.setWindowIcon(QtGui.QIcon('book1.png'))


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.sticker1)
        v_box.addWidget(self.book_name)
        v_box.addWidget(self.sticker2)
        v_box.addWidget(self.author)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.text_area2)
        v_box.addStretch()
        v_box.addWidget(self.bsearch)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.bsearch.clicked.connect(self.search)

        self.show()

    def search(self):
        book = self.book_name.text()
        aut = self.author.text()


        self.cursor.execute("Select * From books where book_name = ? and author = ? ", (book,aut))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.text_area2.setText("There is no such book")
        else:
            self.text_area.setText("-Book name ==>" + book)
            self.text_area2.setText("-Author ==>" + aut)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window1 = Window()



    sys.exit(app.exec_())