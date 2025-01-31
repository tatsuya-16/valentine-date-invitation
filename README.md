# PyQt5 バレンタインアプリ

## 📝 概要
**PyQt5** を使用してバレンタインデーデートに誘うシンプルなGUIアプリを作成した．ユーザに対して **"バレンタインのデートに行きませんか？"** という質問を表示する．
"Sí"（Yes）がクリックされた場合はメッセージを表示しする．
"No"（No）をクリックしようとするとランダムに移動する仕様になっている．

## 📌 使用技術
- **Python 3**
- **PyQt5**（GUIフレームワーク）

## 🏗️ 実装の流れ
1. **ウィンドウの作成**（`QWidget` を継承）
2. **メッセージラベルの設置**
3. **ボタンの配置（Yes / No）**
4. **Noボタンのランダム移動機能**
5. **Yesボタンのクリック時のメッセージ表示**
6. **PyQt5のメインループ実行**

## 📜 コード解説

### **1️⃣ 必要なライブラリをインポート**
```python
import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                            QLabel, QHBoxLayout)
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
```
- `PyQt5.QtWidgets` … GUI要素（ウィンドウ・ボタン・レイアウトなど）
- `PyQt5.QtCore` … ウィンドウの位置や動作を管理
- `PyQt5.QtGui` … フォントや色の設定
- `random` … Noボタンの移動に使用

### **2️⃣ クラス `ValentineApp` の定義**
```python
class ValentineApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
```
- `QWidget` を継承し，PyQt5のGUIアプリとして機能
- `initUI()` メソッドでGUIを初期化

### **3️⃣ ウィンドウの設定**
```python
self.setGeometry(300, 300, 500, 300)  # ウィンドウサイズと位置
self.setWindowTitle('❤ バレンタイン ❤')  # ウィンドウのタイトル
self.setStyleSheet('background-color: #FFE6E6;')  # 背景色を薄いピンクに設定
```

### **4️⃣ メッセージラベルの作成**
```python
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
```
- `QLabel` で質問を表示
- `setFont()` でフォント設定
- `setStyleSheet()` で背景や枠線のデザインを調整
- `setAlignment(Qt.AlignCenter)` で中央揃え

### **5️⃣ ボタンの作成（Yes / No）**
#### ✅ **Yesボタンの作成**
```python
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
```
- ピンク色の "Sí" ボタンを作成
- `clicked.connect(self.on_yes)` でクリック時の動作を定義

#### ❌ **Noボタンの作成**
```python
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
```
- `clicked.connect(self.move_no_button)` でクリック時にランダム移動

### **6️⃣ Noボタンのランダム移動**
```python
def move_no_button(self):
    x = random.randint(0, self.width() - self.no_btn.width())
    y = random.randint(0, self.height() - self.no_btn.height())
    self.no_btn.move(x, y)
```
- `random.randint()` を使ってランダムな座標を計算し，Noボタンを移動

### **7️⃣ Yesボタンのクリック時の動作**
```python
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
```
- "Sí" ボタンを押すと，成功メッセージを表示

### **8️⃣ メイン関数の定義**
```python
def main():
    app = QApplication(sys.argv)
    ex = ValentineApp()
    ex.show()
    sys.exit(app.exec_())
```
- `QApplication` を作成し，アプリを実行
- `sys.exit(app.exec_())` でアプリのメインループを開始

### **9️⃣ 実行スクリプト**
```python
if __name__ == '__main__':
    main()
```
- `main()` を呼び出してプログラムを開始

## 🎉 まとめ
- **PyQt5を使って簡単なGUIアプリを作成**
- **ボタンをクリックすると動作が変わる仕様**
- **Noボタンはランダムに移動して押しづらくなる**

実行するには，以下のコマンドで PyQt5 をインストールしてください．
```bash
pip install PyQt5
```
その後，スクリプトを実行すれば動作します．
```bash
python script.py
```
楽しいバレンタインアプリを作りましょう！💖
