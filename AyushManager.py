from PyQt5.QtWidgets import QMainWindow,QApplication,QFrame,QLabel,QPushButton,QTextBrowser,QPlainTextEdit,QLineEdit,QStackedWidget,QDialog,QTableView,QTableWidget

from PyQt5 import uic
import sys

name = "fkj"

class UI(QDialog):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("UIPages/TEST.ui",self)
        self.pushButton.clicked.connect(self.goToHome)
        
    def goToHome(self):
        if(self.usernameText.text() == "ayush"):
            global name
            name = "ayush"
            if(self.passwordText.text() == "kam"):
                self.usernameText.setText("")
                self.passwordText.setText("")
                homepage = home()
                widget.addWidget(homepage)
                widget.setCurrentIndex(widget.currentIndex() + 1)
        
                



class home(QDialog):
    def __init__(self):
        super(home,self).__init__()
        uic.loadUi("UIPages/homepage.ui",self)

        self.pushButton.clicked.connect(self.goToLogin)
        #self.addEntry.clicked.connect(self.goToAddPage)
        self.profileButton.clicked.connect(self.goToProfile)
        self.myBooksButton.clicked.connect(self.goToMyBooks)
        self.libBooksbutton.clicked.connect(self.goToLibBooks)
        self.notifButton.clicked.connect(self.goToNotif)
    
    def goToLogin(self):
        widget.removeWidget(widget.currentWidget())

    def goToProfile(self):
        profile = pPage()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        profile.setText()
    
    def goToMyBooks(self):
        my_books_page = myBP()
        widget.addWidget(my_books_page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToLibBooks(self):
        LB = libBooks()
        widget.addWidget(LB)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToNotif(self):
        N = notif_page()
        widget.addWidget(N)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        



class pPage(QDialog):
    def __init__(self):
        super(pPage,self).__init__()
        uic.loadUi("UIPages/profilepage.ui",self)

        self.editprofile.clicked.connect(self.goToEditPage)
        self.backButton.clicked.connect(self.goBack)
        

    def goBack(self):
        widget.removeWidget(widget.currentWidget())
    
    def setText(self):
        self.name.setText(name)

    def goToEditPage(self):
        eP = editProfileP()
        widget.addWidget(eP)
        widget.setCurrentIndex(widget.currentIndex() + 1)




class editProfileP(QDialog):
    def __init__(self):
        super(editProfileP,self).__init__()
        uic.loadUi("UIPages/profileEditPage.ui",self)
        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())




class bookHist(QDialog):
    def __init__(self):
        super(bookHist,self).__init__()
        uic.loadUi("UIPages/bookHistory.ui",self)

        self.tableWidget.setColumnWidth(0,160)


        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())





class myBP(QDialog):
    def __init__(self):
        super(myBP,self).__init__()
        uic.loadUi("UIPages/myBooksP.ui",self)

        self.backButton.clicked.connect(self.goBack)
        self.bookHistory.clicked.connect(self.goToBookHist)
        self.currBooks.clicked.connect(self.goToCurrBooks)
        self.remainders.clicked.connect(self.goToRemPage)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())

    def goToBookHist(self):
        bH = bookHist()
        widget.addWidget(bH)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToCurrBooks(self):
        currBS = currB()
        widget.addWidget(currBS)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goToRemPage(self):
        RP = remPage()
        widget.addWidget(RP)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    


class currB(QDialog):
    def __init__(self):
        super(currB,self).__init__()
        uic.loadUi("UIPages/currBooks.ui",self)
        self.backButton.clicked.connect(self.goback)
    
    def goback(self):
        widget.removeWidget(widget.currentWidget())

class remPage(QDialog):
    def __init__(self):
        super(remPage,self).__init__()
        uic.loadUi("UIPages/remPage.ui",self)

        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())

class libBooks(QDialog):
    def __init__(self):
        super(libBooks,self).__init__()
        uic.loadUi("UIPages/libBooksPage.ui",self)

        self.backButton.clicked.connect(self.goBack)
        
    def goBack(self):
        widget.removeWidget(widget.currentWidget())


class notif_page(QDialog):
    def __init__(self):
        super(notif_page,self).__init__()
        uic.loadUi("UIPages/notifSet.ui",self)

        self.backButton.clicked.connect(self.goBack)
    
    def goBack(self):
        widget.removeWidget(widget.currentWidget())



app = QApplication(sys.argv)
widget = QStackedWidget()
UI1 = UI()
widget.addWidget(UI1)
widget.setFixedHeight(900)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exit")


