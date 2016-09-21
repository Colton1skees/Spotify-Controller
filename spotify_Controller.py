import gi
gi.require_version('Gtk', '3.0')
import sys
import dbus
import pygtk
import gi
import signal
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Hello world")

player = dbus.SessionBus().get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
properties_manager = dbus.Interface(player, 'org.freedesktop.DBus.Properties')

curr_volume = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'Metadata')


info = [curr_volume["xesam:title"], curr_volume["xesam:albumArtist"]]

def nextNotify():
    nextNotify=Notify.Notification.new("Skipped Song:", "Click Previous To Go Back: BROKEN", "dialog-information")
    nextNotify.show()

def previousNotify():
    previousNotify=Notify.Notification.new(" Song:", "Click Next To Play Next Song: ", "dialog-information")
    previousNotify.show()

def pauseNotify():
    pauseNotify=Notify.Notification.new(" Paused Song:", "Click Play To Continue Listening ", "dialog-information")
    pauseNotify.show()

def playNotify():
    playNotify=Notify.Notification.new(" Playing Song", "Click Pause To Pause Song: ", "dialog-information")
    playNotify.show()

def infoNotify():
    infoNotify=Notify.Notification.new(" Song info:", "Title: " + info[0] + " - " + info[1][0], "dialog-information")
    infoNotify.show()






try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def test():
    player.Next(dbus_interface='org.mpris.MediaPlayer2.Player')
    nextNotify()

def commander (self, arg):
    test()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):





        #Button clicked functions

        def on_button1_clicked():
            test()



        def on_button2_clicked():
            player.Previous(dbus_interface='org.mpris.MediaPlayer2.Player')
            previousNotify()

        def on_button3_clicked():
            player.Play(dbus_interface='org.mpris.MediaPlayer2.Player')
            playNotify()

        def on_button4_clicked():
            player.Pause(dbus_interface='org.mpris.MediaPlayer2.Player')
            pauseNotify()

        def on_button5_clicked():
            infoNotify()

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(229, 364)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 242, 85, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 276, 85, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 208, 85, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 174, 85, 28))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 310, 85, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(40, 10, 161, 161))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        link = curr_volume['mpris:artUrl']
        self.webView.load(QUrl(link))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #Button clicked actions



        self.pushButton.clicked.connect(lambda: commander(on_button1_clicked()))
        self.pushButton_2.clicked.connect(lambda: commander(on_button2_clicked()))
        self.pushButton_3.clicked.connect(lambda: commander(on_button3_clicked()))
        self.pushButton_4.clicked.connect(lambda: commander(on_button4_clicked()))
        self.pushButton_5.clicked.connect(lambda: commander(on_button5_clicked()))

        import threading





        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Next", None))
        self.pushButton_2.setText(_translate("MainWindow", "Previous", None))
        self.pushButton_4.setText(_translate("MainWindow", "Pause", None))
        self.pushButton_5.setText(_translate("MainWindow", "Info", None))
        self.pushButton_3.setText(_translate("MainWindow", "Play", None))




from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


