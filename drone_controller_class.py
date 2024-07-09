import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

# http://coding-sim.droneblocks.io/

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700, 300) # Sets the size of the app window to 700 x 300

        ############## Assigns an initial value to all the variables ######################
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
        ######################

        self.initUI()


    def get_control_button(self, label):
        '''
        A function that defines a button and sets the size
        '''
        button = QPushButton(label)
        button.setFixedSize(60, 30)
        return button
    
    def get_edit_box(self, text="0"):
        '''
        A function that defines an edit input box to accept inputs and sets the size. It also sets the size of the text font
        '''
        edit = QLineEdit(text)
        edit.setFixedSize(40, 20)

        font = QFont()
        font.setPointSize(12)
        edit.setFont(font)
        return edit
    
    def is_connected(self):
        '''
        This function only checks of the edit input box is is not enabled. If it is not enabled, it means the controller is connected to the drone
        '''
        return not self.edit_api_key.isEnabled()
    
    def on_connect_button_clicked(self):
        '''
        This function is called when the "connect" button is called and then establishes connection to the drone
        '''
        if not self.is_connected(): # Checks if the controller is not connected to the simulated drone

            self.label_message.setText("Connecting...")     # Prints a message that shows the controller is connecting
            self.api_key = self.edit_api_key.text()         # Retrieves the entered drone API
            self.edit_api_key.setEnabled(False)             # Disables the edit input box to prevent the API from being edited
            self.btn_connect.setText("Land")                # Changes the text on the button from "Connect" to "Land"

            ########## Everything here establishes the connection to the simulated drone using the entered API #######################
            self.simulator_context_manager = DroneBlocksSimulatorContextManager(simulator_key=self.api_key)
            self.drone = self.simulator_context_manager.__enter__()
            try:
                self.label_message.setText("Connected")
                self.drone.takeoff()
            except Exception as e:
                print("Error occurred", e)
                self.label_message.setText(e)
            ################################################################################################

        else:   # If the controller is not connected to the drone, it goes ahead and executes the lines of code below

            self.label_message.setText("Disconnecting...")  # Prints a message that shows the controller is disconnecting
            self.edit_api_key.setEnabled(True)              # Enables the edit input box to allow the API to be editable
            self.btn_connect.setText("Connect")             # Changes the text on the button from "Land" to "Connect"

            ############# Everything here lands the drone and cancels connection #######################
            self.drone.land()
            self.simulator_context_manager.__exit__(None, None, None)
            self.label_message.setText("Disconnected")
            ################################################################################################

    def on_flip_forward_button_clicked(self):
        '''
        Flips the drone forward
        '''
        self.drone.flip_forward()

    def on_flip_left_button_clicked(self):
        '''
        Flips the drone to the left
        '''
        self.drone.flip_left()

    def on_flip_right_button_clicked(self):
        '''
        Flips the drone to the right
        '''
        self.drone.flip_right()

    def on_flip_backward_button_clicked(self):
        '''
        Flips the drone backward
        '''
        self.drone.flip_backward()

    def on_go_xyz_button_clicked(self):
        '''
        This function is called when the "Go" button is clicked. It flys the drone to the x, y, and z coordinates entered
        '''
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
        '''
        This function is called when the "Go Circle" button is clicked, and it takes the drone in circles based on the coordinates entered
        '''
        if self.is_connected(): # Checks if the controller is connected to the drone. If it is, it proceeds to retrieve all the entered coordinates
            self.c1 = self.edit_coord1.text()
            self.c2 = self.edit_coord2.text()
            self.c3 = self.edit_coord3.text()
            self.c4 = self.edit_coord4.text()
            self.c5 = self.edit_coord5.text()
            self.c6 = self.edit_coord6.text()
            self.drone.fly_curve(self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, 'in')
        else:
            self.label_message.setText("Drone not connected") # Prints "Drone not connected"


    def initUI(self):
        # Create main layout
        main_layout = QVBoxLayout()

        ################################# TOP SECTION ######################################
        top_layout = QHBoxLayout()

        self.label_api = None # TODO: Create a label and make the displayed text "Enter API key:"
        top_layout.addWidget(self.label_api)

        self.edit_api_key = None # TODO: Create an edit box for extering the API
        top_layout.addWidget(self.edit_api_key)

        self.btn_connect = None # TODO: Create a push button and make the displayed text "Connect"
        # TODO: Set the size to 100 x 30
        # ------ Type it here ----------

        # TODO: Add a button click listener to call the "on_connect_button_clicked" function when the button is clicked
        # ------ Type it here ----------

        top_layout.addWidget(self.btn_connect)

        main_layout.addLayout(top_layout)
        ########################################################################################

        self.label_message = None # TODO: Create a label for displaying the "connection" message
        layout = QHBoxLayout()
        layout.addStretch()  # Add stretchable space before the button
        layout.addWidget(self.label_message)
        layout.addStretch() 
        main_layout.addLayout(layout)

        #######################################################################################################

        # #################################### MIDDLE SECTION #################################################
        # button_layout = QHBoxLayout()
        # ############################## Left button groups ######################################
        # left_group_layout = QVBoxLayout()

        # left_vert_group1 = QHBoxLayout()
        # self.btn_flip_forward = self.get_control_button("▲")
        # # TODO: Add a button click listener to call the "on_flip_forward_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # left_vert_group1.addWidget(self.btn_flip_forward)
        # left_group_layout.addLayout(left_vert_group1)

        # left_hor_group = QHBoxLayout()
        # self.btn_flip_left = self.get_control_button("◀")
        # # TODO: Add a button click listener to call the "on_flip_left_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # # TODO: Add the button widget to the "left_hor_group" layout
        # # ------ Type it here ----------

        # self.btn_flip_right = self.get_control_button("▶")
        # self.btn_flip_right.clicked.connect(self.on_flip_right_button_clicked)
        # left_hor_group.addWidget(self.btn_flip_right)
        # left_group_layout.addLayout(left_hor_group)

        # left_vert_group2 = QHBoxLayout()
        # self.btn_flip_backward = self.get_control_button("▼")
        # # TODO: Add a button click listener to call the "on_flip_backward_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # # TODO: Add the button widget to the "left_vert_group2" layout
        # # ------ Type it here ----------

        # left_group_layout.addLayout(left_vert_group2)

        # button_layout.addLayout(left_group_layout)
        # ################################################################################

        # ####################### Middle section with input boxes and button ######################
        # middle_layout = QHBoxLayout()
        
        # self.edit_x = self.get_edit_box()
        # middle_layout.addWidget(self.edit_x)

        # self.edit_y = self.get_edit_box()
        # middle_layout.addWidget(self.edit_y)

        # self.edit_z = self.get_edit_box()
        # middle_layout.addWidget(self.edit_z)

        # self.btn_go = None # TODO: Create a push button and make the displayed text "Go"
        # # TODO: Set the size to 80 x 30
        # # ------ Type it here ----------

        # # TODO: Add a button click listener to call the "on_go_xyz_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # # TODO: Add the button widget to the "middle_layout" layout
        # # ------ Type it here ----------

        # button_layout.addLayout(middle_layout)
        # #########################################################################################

        # ############################ Right button groups ###############################
        # right_group_layout = QVBoxLayout()

        # right_vert_group1 = QHBoxLayout()
        # self.btn_fly_forward = self.get_control_button("▲")
        # # TODO: Add a button click listener to call the "on_fly_forward_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # # TODO: Add the button widget to the "right_vert_group1" layout
        # # ------ Type it here ----------

        # right_group_layout.addLayout(right_vert_group1)

        # right_hor_group = QHBoxLayout()
        # self.btn_fly_left = self.get_control_button("◀")
        # # TODO: Add a button click listener to call the "on_fly_left_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # # TODO: Add the button widget to the "right_hor_group" layout
        # # ------ Type it here ----------

        # self.btn_fly_right = self.get_control_button("▶")
        # # TODO: Add a button click listener to call the "on_fly_right_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # # TODO: Add the button widget to the "right_hor_group" layout
        # # ------ Type it here ----------

        # right_group_layout.addLayout(right_hor_group)

        # right_vert_group2 = QHBoxLayout()
        # self.btn_fly_backward = self.get_control_button("▼")
        # # TODO: Add a button click listener to call the "on_fly_backward_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # # TODO: Add the button widget to the "right_vert_group2" layout
        # # ------ Type it here ----------

        # right_group_layout.addLayout(right_vert_group2)

        # button_layout.addLayout(right_group_layout)
        # ########################################################################################
        # main_layout.addLayout(button_layout)
        # ##########################################################################################


        # ################################ BOTTOM SECTION ########################################
        # bottom_layout = QVBoxLayout()

        # edit_layout = QHBoxLayout()
        
        # self.edit_coord1 = self.get_edit_box()
        # edit_layout.addWidget(self.edit_coord1)

        # self.edit_coord2 = self.get_edit_box()
        # edit_layout.addWidget(self.edit_coord2)

        # self.edit_coord3 = self.get_edit_box()
        # edit_layout.addWidget(self.edit_coord3)

        # self.edit_coord4 = self.get_edit_box()
        # edit_layout.addWidget(self.edit_coord4)

        # self.edit_coord5  = self.get_edit_box()
        # edit_layout.addWidget(self.edit_coord5)

        # self.edit_coord6 = self.get_edit_box()
        # edit_layout.addWidget(self.edit_coord6)

        # bottom_layout.addLayout(edit_layout)

        # self.btn_curve = None # TODO: Create a push button and make the displayed text "Curve"
        # # TODO: Set the size to 120 x 30
        # # ------ Type it here ----------

        # # TODO: Add a button click listener to call the "on_go_circle_button_clicked" function when the button is clicked
        # # ------ Type it here ----------

        # h_layout2 = QHBoxLayout()
        # h_layout2.addStretch()  # Add stretchable space before the button
        # h_layout2.addWidget(self.btn_curve)
        # h_layout2.addStretch() 
        # bottom_layout.addLayout(h_layout2)

        # main_layout.addLayout(bottom_layout)
        # #########################################################################################

        self.setLayout(main_layout)
        self.setWindowTitle("Sim Drone")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())