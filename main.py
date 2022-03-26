import sys
from unicodedata import category
from PyQt5.QtWidgets import *
from PyQt5 import uic
from cate01 import *

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_main = uic.loadUiType("main.ui")[0]
form_learning = uic.loadUiType("learning_text.ui")[0]
form_quiz = uic.loadUiType("quiz.ui")[0]
form_word = uic.loadUiType("learning_word.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_learn.clicked.connect(self.btn_learn_function)
        self.btn_quiz.clicked.connect(self.btn_quiz_function)

    def btn_learn_function(self):
        # self.hide()                     # 메인윈도우 숨김
        self.close()
        self.second = LearningWindow()    #
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        # self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

    def btn_quiz_function(self):
        self.close()
        self.third = QuizWindow()
        self.third.exec()


class LearningWindow(QDialog, QWidget, form_learning):
    def __init__(self):
        super(LearningWindow, self).__init__()
        self.initUi()
        self.show()

        self.category = 1
        self.page = 1
        self.btn_quiz.clicked.connect(self.btn_quiz_function)
        # self.btn_cate01.clicked.connect(self.cate01)

        self.btn_pre.clicked.connect(self.page_pre)
        self.btn_next.clicked.connect(self.page_next)

        self.btn_word01.clicked.connect(self.word)
        self.btn_word02.clicked.connect(self.word)
        self.btn_word03.clicked.connect(self.word)
        self.btn_word04.clicked.connect(self.word)
        self.btn_word05.clicked.connect(self.word)
        self.btn_word06.clicked.connect(self.word)
        self.btn_word07.clicked.connect(self.word)
        self.btn_word08.clicked.connect(self.word)
        self.btn_word09.clicked.connect(self.word)
        self.btn_word10.clicked.connect(self.word)

    def initUi(self):
        self.setupUi(self)

    def btn_quiz_function(self):
        self.close()
        self.third = QuizWindow()
        self.third.exec()

    def word(self):
        self.close()
        self.fourth = WordWindow()
        self.fourth.exec()

    def page_pre(self):
        if self.page != 1:
            self.page -= 1
            self.label_page.setText(str(self.page))
            self.btn_word01.setText("단어"+str(10*(self.page-1)+1))
            self.btn_word02.setText("단어"+str(10*(self.page-1)+2))
            self.btn_word03.setText("단어"+str(10*(self.page-1)+3))
            self.btn_word04.setText("단어"+str(10*(self.page-1)+4))
            self.btn_word05.setText("단어"+str(10*(self.page-1)+5))
            self.btn_word06.setText("단어"+str(10*(self.page-1)+6))
            self.btn_word07.setText("단어"+str(10*(self.page-1)+7))
            self.btn_word08.setText("단어"+str(10*(self.page-1)+8))
            self.btn_word09.setText("단어"+str(10*(self.page-1)+9))
            self.btn_word10.setText("단어"+str(10*self.page))

    def page_next(self):
        self.page += 1
        self.label_page.setText(str(self.page))
        self.btn_word01.setText("단어"+str(10*(self.page-1)+1))
        self.btn_word02.setText("단어"+str(10*(self.page-1)+2))
        self.btn_word03.setText("단어"+str(10*(self.page-1)+3))
        self.btn_word04.setText("단어"+str(10*(self.page-1)+4))
        self.btn_word05.setText("단어"+str(10*(self.page-1)+5))
        self.btn_word06.setText("단어"+str(10*(self.page-1)+6))
        self.btn_word07.setText("단어"+str(10*(self.page-1)+7))
        self.btn_word08.setText("단어"+str(10*(self.page-1)+8))
        self.btn_word09.setText("단어"+str(10*(self.page-1)+9))
        self.btn_word10.setText("단어"+str(10*self.page))

    # def cate01(self):
    #     self.close()
    #     self.c01_01 = LearningWindow01_01()
    #     self.c01_01.exec()


class QuizWindow(QDialog, QWidget, form_quiz):
    def __init__(self):
        super(QuizWindow, self).__init__()
        self.initUi()
        self.show()

        self.btn_learn.clicked.connect(self.btn_learing_function)

    def initUi(self):
        self.setupUi(self)

    def btn_learing_function(self):
        self.close()
        self.second = LearningWindow()
        self.second.exec()


class WordWindow(QDialog, QWidget, form_word):
    def __init__(self):
        super(WordWindow, self).__init__()
        self.initUi()
        self.show()

        self.btn_learn.clicked.connect(self.btn_learing_function)
        self.btn_quiz.clicked.connect(self.btn_quiz_function)

    def initUi(self):
        self.setupUi(self)

    def btn_learing_function(self):
        self.close()
        self.second = LearningWindow()
        self.second.exec()

    def btn_quiz_function(self):
        self.close()
        self.third = QuizWindow()
        self.third.exec()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
