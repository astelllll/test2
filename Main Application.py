from PyQt5 import QtWidgets, uic

def printt():
    vLabel = call.label.text()
    vTextEdit = call.lineEdit.text()
    print("hello world")
    print("old label :", vLabel)
    print("text edit :", vTextEdit)
    call.label.setText(vTextEdit)
    vLabelNew = call.label.text()
    print("new label :", vLabelNew)
    call.label.adjustSize()
    
app = QtWidgets.QApplication([])
call = uic.loadUi("untitled.ui")

call.pushButton.clicked.connect(printt)

call.show()
app.exec()