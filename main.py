import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QLineEdit, QPushButton, QSizePolicy, QAbstractItemView, QHBoxLayout, QVBoxLayout, QLayout
from PyQt5.QtCore import Qt, QRectF, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
import tinify

def compress_image(image_source, output_file_path):
    try:
        image_name = os.path.basename(image_source)
        source = tinify.from_file(image_source)
    except tinify.errors.AccountError:
        return (False, 'Invalide API Key')
    except tinify.errors.ConnectionError as e:
        return (False, str(e))
    except tinify.errors.clientError:
        return (False, 'File type unsupported')
    else:
        source.to_file(output_file_path)
        return (True, 'OK')
    
class appli(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width(), self.window_height() = 1200, 900
        self.setMinimumSize(self.window_width, self.window_height)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''QWidget {font-size: 30px;
                    }
                        QPushButton {
                            windth: 245px;
                            height: 65px;
                            background-color: #152436;
                            color: #ffffff;
                            border-radius: 10px;
                        }
                        ''')
    
    appli = appli()
    appli.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Window Closing')
    