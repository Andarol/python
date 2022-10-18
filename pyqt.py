import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100, 360, 350)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Times New Roman', 15))
        push1 = QPushButton("1", self)
        push1.setGeometry(5, 150, 80, 40)
        push2 = QPushButton("2", self)
        push2.setGeometry(95, 150, 80, 40)
        push3 = QPushButton("3", self)
        push3.setGeometry(185, 150, 80, 40)
        push4 = QPushButton("4", self)
        push4.setGeometry(5, 200, 80, 40)
        push5 = QPushButton("5", self)
        push5.setGeometry(95, 200, 80, 40)
        push6 = QPushButton("5", self)
        push6.setGeometry(185, 200, 80, 40)
        push7 = QPushButton("7", self)
        push7.setGeometry(5, 250, 80, 40)
        push8 = QPushButton("8", self)
        push8.setGeometry(95, 250, 80, 40)
        push9 = QPushButton("9", self)
        push9.setGeometry(185, 250, 80, 40)
        push0 = QPushButton("0", self)
        push0.setGeometry(5, 300, 80, 40)
        push_equal = QPushButton("=", self)
        push_equal.setGeometry(275, 300, 80, 40)
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)
        push_plus = QPushButton("+", self)
        push_plus.setGeometry(275, 250, 80, 40)
        push_minus = QPushButton("-", self)
        push_minus.setGeometry(275, 200, 80, 40)
        push_mul = QPushButton("*", self)
        push_mul.setGeometry(275, 150, 80, 40)
        push_div = QPushButton("/", self)
        push_div.setGeometry(185, 300, 80, 40)
        push_point = QPushButton(".", self)
        push_point.setGeometry(95, 300, 80, 40)
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(15, 100, 200, 40)
        push_del = QPushButton("Del", self)
        push_del.setGeometry(210, 100, 145, 40)
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.button0)
        push1.clicked.connect(self.button1)
        push2.clicked.connect(self.button2)
        push3.clicked.connect(self.button3)
        push4.clicked.connect(self.button4)
        push5.clicked.connect(self.button5)
        push6.clicked.connect(self.button6)
        push7.clicked.connect(self.button7)
        push8.clicked.connect(self.button8)
        push9.clicked.connect(self.button9)
        push_div.clicked.connect(self.div)
        push_mul.clicked.connect(self.mul)
        push_plus.clicked.connect(self.plus)
        push_point.clicked.connect(self.point)
        push_clear.clicked.connect(self.clear)
        push_del.clicked.connect(self.delete)

    def action_equal(self):
        equation = self.label.text()
        try:
            ans = eval(equation)
            self.label.setText(str(ans))

        except:
            self.label.setText("Wrong Input")

    def button0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def button1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def button2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def button3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def button4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def button5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def button6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def button7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def button8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def button9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def div(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def clear(self):
        self.label.setText("")

    def delete(self):
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
