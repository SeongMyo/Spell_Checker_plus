import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from main_ui import Ui_MainWindow
from utils.spell_checker import check, cleaned_result


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.open_file)
        self.pushButton_reset.clicked.connect(self.input_text.clear)
        self.pushButton_reset.clicked.connect(self.output_text.clear)
        self.pushButton_check.clicked.connect(self.output_text.clear)
        self.pushButton_check.clicked.connect(self.click_check)
        
        
    def open_file(self):  # 열기(O)
        file_name = QFileDialog.getOpenFileName(self)
        if file_name[0]:
            with open(file_name[0], encoding='UTF-8') as f:
                text = f.read()
            self.input_text.setPlainText(text)
            
    def click_check(self):
        text = self.input_text.toPlainText()
        result = cleaned_result(check(text))
        for sent in result:
            self.output_text.append(sent)
        
    
if __name__ == '__main__':        
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())