'''
This program is free software: 
you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or (at your option) 
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. 
If not, see www.gnu.org/licenses
'''

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import * 


class Ui_EmailSplitter(object):
    def setupUi(self, EmailSplitter):
        EmailSplitter.setObjectName("EmailSplitter")
        EmailSplitter.setFixedSize(670, 594)
        EmailSplitter.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/malin/PycharmProjects/Splitter/venv/src/main/icons/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EmailSplitter.setWindowIcon(icon)
        EmailSplitter.setIconSize(QtCore.QSize(16, 16))
        EmailSplitter.setWindowOpacity(1.0)
        EmailSplitter.setStyleSheet("background-color: rgb(20, 8, 8);")
        
        self.centralwidget = QtWidgets.QWidget(EmailSplitter)
        self.centralwidget.setObjectName("centralwidget")
        self._top_left = QtWidgets.QFrame(self.centralwidget)
        self._top_left.setGeometry(QtCore.QRect(10, 20, 311, 241))
        self._top_left.setStyleSheet("")
        self._top_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._top_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self._top_left.setObjectName("_top_left")
        
        self.emailBrowser = QtWidgets.QLabel(self._top_left)
        self.emailBrowser.setGeometry(QtCore.QRect(10, 10, 291, 221))
        ####self.emailBrowser.setPlaceholderText(f"SELECT SOURCE FILE OR PASTE YOUR LIST HERE")
        self.emailBrowser.setObjectName("emailBrowser")
        self.emailBrowser.setStyleSheet("color: rgb(85, 170, 255);background-color: rgb(36, 24, 34)")
        
        self.splitButton = QtWidgets.QPushButton(self.centralwidget)
        self.splitButton.setGeometry(QtCore.QRect(330, 270, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.splitButton.setFont(font)
        self.splitButton.setStyleSheet("color: rgb(239, 127, 0);\n"
"background-color: rgb(57, 57, 57);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/malin/PycharmProjects/Splitter/venv/src/main/icons/app-icons/splitter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.splitButton.setIcon(icon1)
        self.splitButton.setIconSize(QtCore.QSize(26, 26))
        self.splitButton.setObjectName("splitButton")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(635, 270, 30, 109))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("color: rgb(239, 239, 239);\n"
"background-color: rgb(57, 57, 57);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/malin/PycharmProjects/Splitter/venv/src/main/icons/app-icons/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetButton.setIcon(icon1)
        self.resetButton.setIconSize(QtCore.QSize(25, 25))
        self.resetButton.setObjectName("resetButton")

        self.creditsLabel = QtWidgets.QPushButton(self.centralwidget)
        self.creditsLabel.setGeometry(QtCore.QRect(560, 553, 91, 20))
        self.creditsLabel.setStyleSheet("color: rgb(66,66,66);background-color: rgb(20, 8, 8);")
        self.creditsLabel.setObjectName("creditsLabel")
        
        self.sourceButton = QtWidgets.QPushButton(self.centralwidget)
        self.sourceButton.setGeometry(QtCore.QRect(10, 270, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.sourceButton.setFont(font)
        self.sourceButton.setMouseTracking(False)
        self.sourceButton.setStyleSheet("color: rgb(239, 127, 0); background-color: rgb(57, 57, 57);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/malin/PycharmProjects/Splitter/venv/src/main/icons/app-icons/source.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sourceButton.setIcon(icon2)
        self.sourceButton.setIconSize(QtCore.QSize(25, 25))
        self.sourceButton.setObjectName("sourceButton")
        
        self.destButton = QtWidgets.QPushButton(self.centralwidget)
        self.destButton.setGeometry(QtCore.QRect(170, 270, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.destButton.setFont(font)
        self.destButton.setStyleSheet("color: rgb(239, 127, 0); background-color: rgb(57, 57, 57);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/malin/PycharmProjects/Splitter/venv/src/main/icons/app-icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.destButton.setIcon(icon3)
        self.destButton.setIconSize(QtCore.QSize(25, 25))
        self.destButton.setObjectName("destButton")
        
        self.filePath = QtWidgets.QLabel(self.centralwidget)
        self.filePath.setGeometry(QtCore.QRect(10, 350, 151, 29))
        self.filePath.setStyleSheet("color: rgb(85, 170, 255);background-color: rgb(36, 24, 34);")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.filePath.setFont(font)
        self.filePath.setObjectName("filePath")
        
        self.directoryPath = QtWidgets.QLabel(self.centralwidget)
        self.directoryPath.setGeometry(QtCore.QRect(170, 350, 151, 29))
        self.directoryPath.setStyleSheet("color: rgb(85, 170, 255);background-color: rgb(36, 24, 34);")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.directoryPath.setFont(font)
        self.directoryPath.setObjectName("directoryPath")
        
        self.statusUpdate = QtWidgets.QLabel(self.centralwidget)
        self.statusUpdate.setGeometry(QtCore.QRect(330, 350, 299, 29))
        self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(117,0,28);qproperty-alignment: 'AlignCenter';")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusUpdate.setFont(font)
        self.statusUpdate.setObjectName("statusUpdate")

        self.emailNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.emailNumber.setGeometry(QtCore.QRect(10, 400, 151, 29))
        self.emailNumber.setPlaceholderText("2000")
        self.emailNumber.setValidator(QIntValidator())
        self.emailNumber.setMaxLength(10)
        self.emailNumber.setFrame(True)
        self.emailNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.emailNumber.setObjectName("emailNumber")
        self.emailNumber.setStyleSheet("color: rgb(85, 170, 255);background-color: rgb(36, 24, 34);")
      
        self.emailperList_label = QtWidgets.QLabel(self.centralwidget)
        self.emailperList_label.setGeometry(QtCore.QRect(180, 400, 151, 31))
        self.emailperList_label.setStyleSheet("color: rgb(255, 229, 229);")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.emailperList_label.setFont(font)
        self.emailperList_label.setObjectName("emailperList_label")

        self.outputFileType_label = QtWidgets.QLabel(self.centralwidget)
        self.outputFileType_label.setGeometry(QtCore.QRect(180, 445, 141, 21))
        self.outputFileType_label.setStyleSheet("color: #fff;")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.outputFileType_label.setFont(font)
        self.outputFileType_label.setObjectName("outputFileType_label")

        self.selectType = QtWidgets.QComboBox(self.centralwidget)
        self.selectType.setGeometry(QtCore.QRect(10, 440, 151, 31))
        self.selectType.setObjectName("selectType")
        self.selectType.addItem("")
        self.selectType.addItem("")
        self.selectType.addItem("")
        self.selectType.setStyleSheet("color: rgb(85, 170, 255);background-color: rgb(36, 24, 34); padding-left: 62px; padding-right: auto;")
        font = QtGui.QFont()
        font.setBold(True)
        self.selectType.setFont(font)
        
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(370, 10, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Bengali UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: rgb(85, 170, 255);")
        self.titleLabel.setObjectName("titleLabel")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(330, 30, 331, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setObjectName("tabWidget")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.usage = QtWidgets.QLabel(self.About)
        self.usage.setStyleSheet("color: rgb(225, 225, 225);")
        self.usage.setGeometry(QtCore.QRect(10, 0, 281, 211))
        self.usage.setObjectName("usage")
        self.tabWidget.addTab(self.About, "")
        self.License = QtWidgets.QWidget()
        self.License.setObjectName("License")
        self.usage_3 = QtWidgets.QLabel(self.License)
        self.usage_3.setGeometry(QtCore.QRect(10, -10, 291, 241))
        self.usage_3.setMinimumSize(QtCore.QSize(271, 0))
        self.usage_3.setObjectName("usage_3")
        self.usage_3.setStyleSheet("color: rgb(225, 225, 225);")
        self.tabWidget.addTab(self.License, "")
        self.tabWidget.setStyleSheet("color: rgb(125, 125, 125);")
        self._top_left.raise_()
        self.splitButton.raise_()
        self.resetButton.raise_()
        self.creditsLabel.raise_()
        self.sourceButton.raise_()
        self.destButton.raise_()
        self.filePath.raise_()
        self.directoryPath.raise_()
        self.statusUpdate.raise_()
        self.emailNumber.raise_()
        self.emailperList_label.raise_()
        self.outputFileType_label.raise_()
        self.selectType.raise_()
        self.titleLabel.raise_()
        self.tabWidget.raise_()
        EmailSplitter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EmailSplitter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 23))
        self.menubar.setObjectName("menubar")
        EmailSplitter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EmailSplitter)
        self.statusbar.setObjectName("statusbar")
        EmailSplitter.setStatusBar(self.statusbar)
 

        self.retranslateUi(EmailSplitter)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(EmailSplitter)

        # Connect
        self.sourceButton.clicked.connect(self.openFileNameDialog)
        self.destButton.clicked.connect(self.saveFileDialog)
        self.splitButton.clicked.connect(self.splitEmails)
        self.resetButton.clicked.connect(self.resetApp)
        self.creditsLabel.clicked.connect(self.Open_url1)
        self.selectType.setItemText(0, "txt")
        self.selectType.activated.connect(self.selectedType)
        #########self.emailBrowser.textChanged.connect(self.text_change)
        self.emailNumber.textChanged['QString'].connect(self.selectedNR)


    def retranslateUi(self, EmailSplitter):
        _translate = QtCore.QCoreApplication.translate
        EmailSplitter.setWindowTitle(_translate("EmailSplitter", "Email List Splitter Tool"))
        self.splitButton.setText(_translate("EmailSplitter", "   SPLIT NOW"))
        self.resetButton.setText(_translate("EmailSplitter", "", "Ctrl+R"))
        self.splitButton.setShortcut(_translate("EmailSplitter", "Ctrl+S"))
        self.creditsLabel.setText(_translate("EmailSplitter", "by mmark0v"))
        self.sourceButton.setText(_translate("EmailSplitter", "   SOURCE\n"
"   FILE"))
        self.sourceButton.setShortcut(_translate("EmailSplitter", "Ctrl+O"))
        self.destButton.setText(_translate("EmailSplitter", "   DESTINATION\n"
"   DIRECTORY"))
        self.destButton.setShortcut(_translate("EmailSplitter", "Ctrl+D"))
        self.filePath.setText(_translate("EmailSplitter", "/File/path/"))
        self.directoryPath.setText(_translate("EmailSplitter", "/Output Directory/path/"))
        self.statusUpdate.setText(_translate("EmailSplitter", "Not Ready"))
        self.emailNumber.setText(_translate("EmailSplitter", "2000"))
        self.emailperList_label.setText(_translate("EmailSplitter", "EMAILS PER LIST"))
        self.outputFileType_label.setText(_translate("EmailSplitter", "OUTPUT FILE TYPE"))
        self.selectType.setItemText(0, _translate("EmailSplitter", "txt"))
        self.selectType.setItemText(1, _translate("EmailSplitter", "csv"))
        self.selectType.setItemText(2, _translate("EmailSplitter", "xlsx"))
        self.titleLabel.setText(_translate("EmailSplitter", ""
""))
        self.usage.setText(_translate("EmailSplitter", "Use this tool to split big email lists in to custom\n"
"smaller lists, i.e. to import contacts in popular\nemail relays like SendGrid and MailChimp,\nwhere limits for free accounts is up to 2000 emails.\n"
"\n"
"Instructions:\n"
"1. Open the file containing the list.\n"
"2. Select the directory to save the lists.\n"
"3. Choice emails per list number, i.e. 2000 emails.\n"
"4. Select output file type.\n"
"5. Click Split Now button"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("EmailSplitter", "About"))
        self.usage_3.setText(_translate("EmailSplitter", "<html><head/><body><p><span style=\" font-size:7pt;\">This program is free software: you can redistribute it and/or<br/>modify it under the terms of the GNU General Public License<br/>as published by the Free Software Foundation, either version 3<br/>of the License, or (at your option) any later version.<br/><br/>This program is distributed in the hope that it will be useful,<br/>but WITHOUT ANY WARRANTY; without even the implied<br/>warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR<br/>PURPOSE. See the GNU General Public License for more details.<br/><br/>You should have received a copy of the GNU General Public License<br/>along with this program. If not, see <b>www.gnu.org/licenses</b>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.License), _translate("EmailSplitter", "License"))


####  Finctions ####
    
    '''### Checking for input into email browser
    def text_change(self):
        global pasteList
        pasteList = list([self.emailBrowser.toPlainText()])
        self.statusUpdate.setText("Select Directory")
        self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(14,42,0);qproperty-alignment: 'AlignCenter';")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusUpdate.setFont(font)
        self.filePath.setText("List pasted in")
        self.filePath.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(34,102,0);qproperty-alignment: 'AlignCenter';")

        print(pasteList)
    '''  

    ### Open dialog and reading file
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filter= "All Files (*);;Text Files (*.txt);;Text CSV (*.csv);;Excel 2017-2013 (*.xlsx);;Excel 2007-2016 (.xlsm)"
        global openFile
        global saveFile
        openFile, _ = QFileDialog.getOpenFileName(None, "Open File", "", filter, options=options)
        
        
        if openFile:
            filenames = openFile
            f = open(filenames, 'r')
            
            with f:
                data = f.read()
                self.emailBrowser.setText(data)

            self.filePath.setText(openFile)
            self.filePath.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(34,102,0);")
        
        try: saveFile
        except NameError: saveFile = False

        if saveFile is False:
            self.statusUpdate.setText("Select Directory")
            self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(14,42,0);qproperty-alignment: 'AlignCenter';")
            font = QtGui.QFont()
            font.setPointSize(10)
            self.statusUpdate.setFont(font)
        else:
            self.statusUpdate.setText("Ready")
            self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(34,102,0);qproperty-alignment: 'AlignCenter';")
            font = QtGui.QFont()
            font.setPointSize(11)
            self.statusUpdate.setFont(font)

        print(f"Update: File selected\n({openFile})")

    ### Open destination derectory dialog
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        global saveFile
        global openFile
        saveFile = str(QFileDialog.getExistingDirectory(None, "Select Directory", options=options))

        self.directoryPath.setText(saveFile)
        if saveFile:
            self.directoryPath.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(34,102,0);")

        try: openFile
        except NameError: openFile = None

        if openFile == None:
            self.statusUpdate.setText("Select source file")
            self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(14,42,0);qproperty-alignment: 'AlignCenter';")
            font = QtGui.QFont()
            font.setPointSize(10)
            self.statusUpdate.setFont(font)
        else:
            self.statusUpdate.setText("Ready")
            self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(34,102,0);qproperty-alignment: 'AlignCenter';")
            font = QtGui.QFont()
            font.setPointSize(11)
            self.statusUpdate.setFont(font)


        print(f"Update: Directory selected\n({saveFile})")


        # Filetype select event 
    
    ### Store the output file type value
    def selectedType(self):
        global fileType
        fileType = str(self.selectType.currentText()) # filetype extention variable 
        print(f"Update: File type selected: {fileType}")

    ### Store email per list value
    def selectedNR(self):
        global number    
        try: number = int(self.emailNumber.text())
        except ValueError: number = 2000

    ### Execution function
    def splitEmails(self):
        global saveFile
        global openFile

        try: openFile
        except NameError: openFile = None
        try: saveFile
        except NameError: openFile = None

        ### Executing the program
        if openFile and saveFile:
            global number
            global fileType

            try: number
            except NameError: number = "2000" 
            
            ### Select file type
            fileType = str(self.selectType.currentText()) # get filetype value variable
            if number is None:
                number = 2000
            if number == "2000":
                number = 2000            

            ### Working with files
            source = open(openFile, "r")
            dest = saveFile
            email_file = source
            email_list = email_file.readlines()
            count = len(email_list)
            if number <= count:  # check if the count of emails per list is bigger than the source list
                loop = count // number
                start = int(0)
                fin = number
                blk = int(1)
                mode = "w" 

                ## writing email list blocks
                for i in range(0, loop):
                    new_list = open(f'{dest}/E-list-{blk}.{fileType}', f"{mode}")
                    new_file = new_list.writelines(email_list[start:fin])
                    blk += 1
                    start += number
                    fin += number

                if new_list:   # Check and updating if job has been completed
                    self.statusUpdate.setText(f"Job Completed, {loop} lists were created.")
                    self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(53,53,133);qproperty-alignment: 'AlignCenter';")
                    print(f"Update: Job Completed, {loop} lists were created.")
                    print(f"Update: {number} emails per list.")
                else:
                    self.statusUpdate.setText(f"Not really ready")
                    self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(117,0,28);qproperty-alignment: 'AlignCenter';")
                    print(f"Error: Not really ready")
            else:
                self.statusUpdate.setText(f"Too many emails per list")
                self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(184,138,0);qproperty-alignment: 'AlignCenter';")
                print(f"Error: Too many emails per list")
        else:
            self.statusUpdate.setText(f"Not really ready")
            self.statusUpdate.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(117,0,28);qproperty-alignment: 'AlignCenter';")
            print(f"Error: Not really ready")

    ### Restart application 
    def resetApp(self):
        import sys
        import os
        python = sys.executable
        os.execl(python, python, * sys.argv)
        print(restarting)

    ### Open credits link
    def Open_url1(self): 
        import webbrowser 
        webbrowser.open('https://github.com/mmark0v')


#### End Finctions ####


#### Runing main function ####
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmailSplitter = QtWidgets.QMainWindow()
    ui = Ui_EmailSplitter()
    ui.setupUi(EmailSplitter)
    EmailSplitter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main()
