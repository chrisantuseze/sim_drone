import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

# http://coding-sim.droneblocks.io/

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 300)
        self.initUI()

        self.api_key = ""
        
        self.x = ""
        self.y = ""
        self.z = ""

        self.c1 = ""
        self.c2 = ""
        self.c3 = ""
        self.c4 = ""
        self.c5 = ""
        self.c6 = ""


    def get_control_button(self, label):
        button = QPushButton(label)
        button.setFixedSize(60, 30)
        return button
    
    def get_edit_box(self, text="0"):
        edit = QLineEdit(text)
        edit.setFixedSize(40, 20)

        font = QFont()
        font.setPointSize(12)
        edit.setFont(font)
        return edit
    
    def is_connected(self):
        return not self.edit_api_key.isEnabled()
    
    def on_connect_button_clicked(self):
        if not self.is_connected():
            self.label_message.setText("Connecting...")
            self.api_key = self.edit_api_key.text()
            self.edit_api_key.setEnabled(False)
            self.btn_connect.setText("Land")

            self.simulator_context_manager = DroneBlocksSimulatorContextManager(simulator_key=self.api_key)
            self.drone = self.simulator_context_manager.__enter__()
            try:
                self.label_message.setText("Connected")
                self.drone.takeoff()
            except Exception as e:
                print("Error occurred", e)
                self.label_message.setText(e)
        else:
            self.label_message.setText("Disconnecting...")
            self.edit_api_key.setEnabled(True)
            self.btn_connect.setText("Connect")

            self.drone.land()
            self.simulator_context_manager.__exit__(None, None, None)
            self.label_message.setText("Disconnected")

    def on_flip_forward_button_clicked(self):
        self.drone.flip_forward()

    def on_flip_left_button_clicked(self):
        self.drone.flip_left()

    def on_flip_right_button_clicked(self):
        self.drone.flip_right()

    def on_flip_backward_button_clicked(self):
        self.drone.flip_backward()

    def on_go_xyz_button_clicked(self):
        if self.is_connected():
            self.x = self.edit_x.text()
            self.y = self.edit_y.text()
            self.z = self.edit_z.text()
            self.drone.fly_to_xyz(self.x, self.y, self.z, 'in')
        else:
            self.label_message.setText("Drone not connected")

    def on_fly_forward_button_clicked(self):
        # flip forward by 20 inches
        self.drone.fly_forward(20, 'in')

    def on_fly_left_button_clicked(self):
        # flip left by 20 inches
        self.drone.fly_left(20, 'in')

    def on_fly_right_button_clicked(self):
        # flip right by 20 inches
        self.drone.fly_right(20, 'in')

    def on_fly_backward_button_clicked(self):
        # flip backward by 20 inches
        self.drone.fly_backward(20, 'in')

    def on_go_circle_button_clicked(self):
        if self.is_connected():
            self.c1 = self.edit_coord1.text()
            self.c2 = self.edit_coord2.text()
            self.c3 = self.edit_coord3.text()
            self.c4 = self.edit_coord4.text()
            self.c5 = self.edit_coord5.text()
            self.c6 = self.edit_coord6.text()
            self.drone.fly_curve(self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, 'in')
        else:
            self.label_message.setText("Drone not connected")


    def initUI(self):
        # Create main layout
        main_layout = QVBoxLayout()

        ####################### Top section with input box and button ######################
        top_layout = QHBoxLayout()

        self.label_api = QLabel("Enter API key:")
        top_layout.addWidget(self.label_api)

        self.edit_api_key = QLineEdit()
        top_layout.addWidget(self.edit_api_key)

        self.btn_connect = QPushButton("Connect")
        self.btn_connect.setFixedSize(100, 30)
        self.btn_connect.clicked.connect(self.on_connect_button_clicked)
        top_layout.addWidget(self.btn_connect)

        main_layout.addLayout(top_layout)
        ########################################################################################

        self.label_message = QLabel()
        layout = QHBoxLayout()
        layout.addStretch()  # Add stretchable space before the button
        layout.addWidget(self.label_message)
        layout.addStretch() 
        main_layout.addLayout(layout)

        ########################################################################################
        button_layout = QHBoxLayout()
        ############################## Left button groups ######################################
        left_group_layout = QVBoxLayout()

        left_vert_group1 = QHBoxLayout()
        self.btn_flip_forward = self.get_control_button("▲")
        self.btn_flip_forward.clicked.connect(self.on_flip_forward_button_clicked)
        left_vert_group1.addWidget(self.btn_flip_forward)
        left_group_layout.addLayout(left_vert_group1)

        left_hor_group = QHBoxLayout()
        self.btn_flip_left = self.get_control_button("◀")
        self.btn_flip_left.clicked.connect(self.on_flip_left_button_clicked)
        left_hor_group.addWidget(self.btn_flip_left)

        self.btn_flip_right = self.get_control_button("▶")
        self.btn_flip_right.clicked.connect(self.on_flip_right_button_clicked)
        left_hor_group.addWidget(self.btn_flip_right)
        left_group_layout.addLayout(left_hor_group)

        left_vert_group2 = QHBoxLayout()
        self.btn_flip_backward = self.get_control_button("▼")
        self.btn_flip_backward.clicked.connect(self.on_flip_backward_button_clicked)
        left_vert_group2.addWidget(self.btn_flip_backward)
        left_group_layout.addLayout(left_vert_group2)

        button_layout.addLayout(left_group_layout)
        ################################################################################

        ####################### Middle section with input boxes and button ######################
        middle_layout = QHBoxLayout()
        
        self.edit_x = self.get_edit_box()
        middle_layout.addWidget(self.edit_x)

        self.edit_y = self.get_edit_box()
        middle_layout.addWidget(self.edit_y)

        self.edit_z = self.get_edit_box()
        middle_layout.addWidget(self.edit_z)

        self.btn_go = QPushButton("Go")
        self.btn_go.setFixedSize(80, 30)
        self.btn_go.clicked.connect(self.on_go_xyz_button_clicked)
        middle_layout.addWidget(self.btn_go)

        button_layout.addLayout(middle_layout)
        #########################################################################################

        ############################ Right button groups ###############################
        right_group_layout = QVBoxLayout()

        right_vert_group1 = QHBoxLayout()
        self.btn_fly_forward = self.get_control_button("▲")
        self.btn_fly_forward.clicked.connect(self.on_fly_forward_button_clicked)
        right_vert_group1.addWidget(self.btn_fly_forward)
        right_group_layout.addLayout(right_vert_group1)

        right_hor_group = QHBoxLayout()
        self.btn_fly_left = self.get_control_button("◀")
        self.btn_fly_left.clicked.connect(self.on_fly_left_button_clicked)
        right_hor_group.addWidget(self.btn_fly_left)

        self.btn_fly_right = self.get_control_button("▶")
        self.btn_fly_right.clicked.connect(self.on_fly_right_button_clicked)
        right_hor_group.addWidget(self.btn_fly_right)
        right_group_layout.addLayout(right_hor_group)

        right_vert_group2 = QHBoxLayout()
        self.btn_fly_backward = self.get_control_button("▼")
        self.btn_fly_backward.clicked.connect(self.on_fly_backward_button_clicked)
        right_vert_group2.addWidget(self.btn_fly_backward)
        right_group_layout.addLayout(right_vert_group2)

        button_layout.addLayout(right_group_layout)
        ########################################################################################
        main_layout.addLayout(button_layout)
        ########################################################################################


        ####################### Bottom section with input boxes and button ######################
        bottom_layout = QVBoxLayout()

        edit_layout = QHBoxLayout()
        
        self.edit_coord1 = self.get_edit_box()
        edit_layout.addWidget(self.edit_coord1)

        self.edit_coord2 = self.get_edit_box()
        edit_layout.addWidget(self.edit_coord2)

        self.edit_coord3 = self.get_edit_box()
        edit_layout.addWidget(self.edit_coord3)

        self.edit_coord4 = self.get_edit_box()
        edit_layout.addWidget(self.edit_coord4)

        self.edit_coord5  = self.get_edit_box()
        edit_layout.addWidget(self.edit_coord5)

        self.edit_coord6 = self.get_edit_box()
        edit_layout.addWidget(self.edit_coord6)

        bottom_layout.addLayout(edit_layout)

        self.btn_curve = QPushButton("Curve")
        self.btn_curve.setFixedSize(120, 30)
        self.btn_curve.clicked.connect(self.on_go_circle_button_clicked)

        h_layout2 = QHBoxLayout()
        h_layout2.addStretch()  # Add stretchable space before the button
        h_layout2.addWidget(self.btn_curve)
        h_layout2.addStretch() 
        bottom_layout.addLayout(h_layout2)

        main_layout.addLayout(bottom_layout)
        #########################################################################################

        self.setLayout(main_layout)
        self.setWindowTitle("My Window")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())