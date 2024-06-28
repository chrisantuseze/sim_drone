import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 300)
        self.number = 0
        self.initUI()

    def add_number(self):
        number = self.edit_number.text()
        self.number += int(number)
        self.label_result.setText(str(self.number))

    def clear_number(self):
        self.number = 0
        self.label_result.setText("0")
        self.edit_number.setText("")

    def sub_number(self):
        number = self.edit_number.text()
        self.number -= int(number)
        self.label_result.setText(str(self.number))

    def initUI(self):
        # Create main layout
        main_layout = QVBoxLayout()

        ############### TOP LAYOUT ###############################
        top_layout = QHBoxLayout()

        self.label_result = QLabel("0")
        top_layout.addWidget(self.label_result)

        self.edit_number = QLineEdit()
        top_layout.addWidget(self.edit_number)

        main_layout.addLayout(top_layout)

        ##########################################################

        ############### MIDDLE LAYOUT ############################
        mid_layout = QHBoxLayout()

        ############### Left ###################
        left_group_layout = QVBoxLayout()

        left_vert_group1 = QHBoxLayout()
        left_button = QPushButton("+")
        left_button.setFixedSize(80, 35)
        left_button.clicked.connect(self.add_number)
        left_vert_group1.addWidget(left_button)
        left_group_layout.addLayout(left_vert_group1)

        mid_layout.addLayout(left_group_layout)
        ########################################

        ############### Mid ###################
        mid_group_layout = QVBoxLayout()

        mid_vert_group1 = QHBoxLayout()
        mid_button = QPushButton("Clear")
        mid_button.setFixedSize(80, 35)
        mid_button.clicked.connect(self.clear_number)
        mid_vert_group1.addWidget(mid_button)
        mid_group_layout.addLayout(mid_vert_group1)

        mid_layout.addLayout(mid_group_layout)
        ########################################

        ############### Right ##################
        right_group_layout = QVBoxLayout()

        right_vert_group1 = QHBoxLayout()
        right_button = QPushButton("-")
        right_button.setFixedSize(80, 35)
        right_button.clicked.connect(self.sub_number)
        right_vert_group1.addWidget(right_button)
        right_group_layout.addLayout(right_vert_group1)

        mid_layout.addLayout(right_group_layout)
        ########################################

        main_layout.addLayout(mid_layout)
        ##########################################################

        self.setLayout(main_layout)
        self.setWindowTitle("Upward Bound CS")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
