import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                            QLabel, QHBoxLayout)
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class ValentineApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # ウィンドウの設定
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('❤ バレンタイン ❤')
        self.setStyleSheet('background-color: #FFE6E6;')  # 薄いピンク色の背景
        
        # メインレイアウト
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)  # ウィジェット間の間隔を設定
        
        # スペイン語でメッセージを表示
        label = QLabel('¿Quieres ir a una cita de San Valentín conmigo?', self)
        label.setFont(QFont('Arial', 16))
        label.setStyleSheet('''
            QLabel {
                color: #0066CC;  # 濃い青
                padding: 20px;
                background-color: white;
                border: 2px solid #0066CC;
                border-radius: 10px;
                font-weight: bold;
            }
        ''')
        label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label)
        
        # ボタンを横並びにするための水平レイアウト
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)  # ボタン間の間隔
        
        # Yesボタン
        self.yes_btn = QPushButton('Sí', self)
        self.yes_btn.setMinimumSize(100, 50)
        self.yes_btn.setStyleSheet('''
            QPushButton {
                background-color: #FF69B4;
                color: white;
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF1493;
            }
        ''')
        self.yes_btn.clicked.connect(self.on_yes)
        button_layout.addWidget(self.yes_btn)
        
        # Noボタン
        self.no_btn = QPushButton('No', self)
        self.no_btn.setMinimumSize(100, 50)
        self.no_btn.setStyleSheet('''
            QPushButton {
                background-color: #B0B0B0;
                color: white;
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #808080;
            }
        ''')
        self.no_btn.clicked.connect(self.move_no_button)
        button_layout.addWidget(self.no_btn)
        
        # ボタンレイアウトをメインレイアウトに追加
        main_layout.addLayout(button_layout)
        
        # 余白を追加
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        
    def move_no_button(self):
        x = random.randint(0, self.width() - self.no_btn.width())
        y = random.randint(0, self.height() - self.no_btn.height())
        self.no_btn.move(x, y)
        
    def on_yes(self):
        self.label_result = QLabel('¡Genial! ¡Nos vemos pronto! ❤', self)
        self.label_result.setGeometry(QRect(50, 200, 400, 30))
        self.label_result.setAlignment(Qt.AlignCenter)
        self.label_result.setStyleSheet('''
            QLabel {
                color: #FF1493;
                font-size: 16px;
                font-weight: bold;
                background-color: white;
                padding: 5px;
                border-radius: 5px;
            }
        ''')
        self.label_result.show()

def main():
    app = QApplication(sys.argv)
    ex = ValentineApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()