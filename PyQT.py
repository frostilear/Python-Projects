from PyQt5.QtWidgets import QApplication,QWidget
import sys
my_app=QApplication(sys.argv)
widget=QWidget()
widget.setWindowTitle("This is a title!")
widget.show()
sys.exit(my_app.exec_())