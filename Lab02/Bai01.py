#Trần Gia Thuận
#2100002435
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget 
class YesNoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #00FFFF;")
        self.setWindowTitle("Pushbutton widgets (Yes or No)?")
        self.setGeometry(100, 100, 400, 200) # (x, y, width, height)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        yes_button.clicked.connect(self.show_yes_message) 
        no_button.clicked.connect(self.show_no_message)
         
        layout = QVBoxLayout()
        yes_button.setFixedSize(400, 200)#chỉnh size button
        layout.addWidget(yes_button)
        yes_font = yes_button.font()
        yes_font.setPointSize(20)   #chỉnh size chữ
        yes_button.setFont(yes_font)
        no_button.setFixedSize(400, 200) #chỉnh size button
        layout.addWidget(no_button)
        no_font = no_button.font()     
        no_font.setPointSize(20)  #chỉnh size chữ
        no_button.setFont(no_font)

        central_widget.setLayout(layout)
    def show_yes_message(self):
        QMessageBox.information(self, "Choice", "You chose 'Yes'.")

    def show_no_message(self):
        QMessageBox.information(self, "Choice", "You chose 'No'.")
def main():
        app = QApplication(sys.argv)
        window = YesNoApp()
        window.show()
        sys.exit(app.exec_())
if __name__=="__main__":
        main()
