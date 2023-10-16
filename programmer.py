#INSTALL PyQt5 WITH:
# 2. PIP:
# pip install PyQt5


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

#assign widget to global dictionary
widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Ujian Travia Pulamek")
window.setFixedWidth(1100)
#window.move(2700, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

#clear widget
def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

#show start menu
def show_frame1():
    clear_widgets()
    frame1()

#create function
def start_game():
    clear_widgets()
    frame2()
    

def create_button(answer, l_margin, r_margin):
    #create varius button
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "margin-left:" + str(l_margin) + "px;" +
        "margin-left:" + str(r_margin) + "px;" +
        "color: 'white';" +
        "font-family: 'shanti';" +
        "font-size: 16px;" +
        "border-radius: 25px;" +
        "padding: 15px 0;" +
        "margin-top: 20px;}" +
        "*:hover{background: '#BC006C';}"
    )
    button.clicked.connect(show_frame1)
    return button

def frame1():
    #display logo
    image = QPixmap("logo_pulamek.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter) #align widget to center
    logo.setStyleSheet("margin-top: 50px;")
    widgets["logo"].append(logo)


    #button widget
    button = QPushButton("MULA")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 20px;" +
        "font-size: 20px;" +
        "color: 'white';" +
        "margin: 100px 200px;" +
        "padding: 10px 0;}" +
        "*:hover{background: '#BC006C';}"
    )
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    #place widget in grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

def frame2():
    #create text widget
    score = QLabel("80")
    score.setAlignment(QtCore.Qt.AlignRight) #align widget to right
    score.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 20px 25px 20px;" +
        "margin: 20px 200px;" +
        "background: '#64A314';" +
        "border: 1px solid '#64A314';" +
        "border-radius: 45px;"
    )
    widgets["score"].append(score)

    #multiline text widget
    question = QLabel("Placeholder text will be here")
    question.setAlignment(QtCore.Qt.AlignCenter) #align widget to center
    question.setWordWrap(True) # to wrap the question
    question.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"
    )
    widgets["question"].append(question)

    button1 = create_button("answer1", 50, 5)
    button2 = create_button("answer2", 5, 50)
    button3 = create_button("answer3", 50, 5)
    button4 = create_button("answer4", 5, 50)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    #display logo bottom
    image = QPixmap("pulamek_small-removebg-preview.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter) #align widget to center
    logo.setStyleSheet(
        "margin-top: 50px;" +
        "height: 10px;" +
        "width: 50px;"
        )
    widgets["logo"].append(logo)

    #place widget in grid
    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2) #span 1 row 2 column
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1, 2)

#call function
frame1()

window.setLayout(grid)

window.show()
sys.exit(app.exec())