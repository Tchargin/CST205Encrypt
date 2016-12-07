import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PIL import Image
import smtplib
import getpass
import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Decoder/Encoder'
        self.left = 10
        self.top = 10
        self.width = 420
        self.height = 300
        self.initUI()
        QtLabelObj = QLabel(self)
        QtLabelObj.setText("Enter Message: ")
        QtLabelObj.move(20,10)

        QtLabelObj2 = QLabel(self)
        QtLabelObj2.setText("Recipient Email: ")
        QtLabelObj2.move(20,90)

        QtLabelObj3 = QLabel(self)
        QtLabelObj3.setText("Sender Email: ")
        QtLabelObj3.move(20,170)

        #QtLabelObj.AlignCenter()
        QtLabelObj.show()
        QtLabelObj2.show()
        QtLabelObj3.show()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create text

        #self.text = setText(text)
        #self.text.move(20, 150)
        #self.text.resize(300,40)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 40)
        self.textbox.resize(300,40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 120)
        self.textbox2.resize(300,40)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(20, 200)
        self.textbox3.resize(300,40)

        # Create a button in the window
        #self.button1 = QPushButton('Brandon', self)
        #self.button1.move(20,150)

        self.button2 = QPushButton('Send', self)
        self.button2.move(160,250)

        #self.button3 = QPushButton('Tyler', self)
        #self.button3.move(300,150)

        # connect button to function on_click
        #self.button1.clicked.connect(self.on_click)
        self.button2.clicked.connect(self.on_click)
        #self.button3.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        emailRecip = self.textbox2.text()
        emailSend = self.textbox3.text()

        new = list(textboxValue)
        i=0
        for letter in textboxValue:

            if new[i]=='a':
                new[i]= 'd'
            elif new[i]=='b':
                new[i]="e"
            elif new[i]=='c':
                new[i]='f'
            elif new[i]=='d':
                new[i]='g'
            elif new[i]=='e':
                new[i]='h'
            elif new[i]=='f':
                new[i]='i'
            elif new[i]=='g':
                new[i]='j'
            elif new[i]=='h':
                new[i]='k'
            elif new[i]=='i':
                new[i]='l'
            elif new[i]=='j':
                new[i]='m'
            elif new[i]=='k':
                new[i]='n'
            elif new[i]=='l':
                new[i]='o'
            elif new[i]=='m':
                new[i]='p'
            elif new[i]=='n':
                new[i]='q'
            elif new[i]=='o':
                new[i]='r'
            elif new[i]=='p':
                new[i]='s'
            elif new[i]=='q':
                new[i]='t'
            elif new[i]=='r':
                new[i]='u'
            elif new[i]=='s':
                new[i]='v'
            elif new[i]=='t':
                new[i]='w'
            elif new[i]=='u':
                new[i]='x'
            elif new[i]=='v':
                new[i]='y'
            elif new[i]=='w':
                new[i]='z'
            elif new[i]=='x':
                new[i]='a'
            elif new[i]=='y':
                new[i]='b'
            elif new[i]=='z':
                new[i]='c'
            elif new[i]==' ':
                new[i]=" "

            i=i+1
        msg=str(new)

        QMessageBox.question(self, 'Message - pythonspot.com', "Your message is now encrypted to: " + msg, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


        def encode_image(img, msg):
                length = len(msg)
                if length > 255:
                    print("Make the message shorter please < 255 characters.")
                    return False

                encoded = img.copy()
                width, height = img.size
                index = 0
                for row in range(height):
                    for col in range(width):
                        r, g, b = img.getpixel((col, row))
                        if row == 0 and col == 0 and index < length:
                            asc = length
                        elif index <= length:
                            c = msg[index -1]
                            asc = ord(c)
                        else:
                            asc = r
                        encoded.putpixel((col, row), (asc, g , b))
                        index += 1
                return encoded

        def decode_image(img):
                width, height = img.size
                msg = ""
                index = 0
                for row in range(height):
                    for col in range(width):
                        try:
                            r, g, b = img.getpixel((col, row))
                        except ValueError:
                            r, g, b, a = img.getpixel((col, row))
                        if row == 0 and col == 0:
                            length = r
                        elif index <= length:
                            msg += chr(r)
                        index += 1
                return msg

        original_image_file = "Nothingtoseehere.png"
        img = Image.open(original_image_file)
        print(img, img.mode)
        encoded_image_file = "enc_" + original_image_file
        secret_msg = msg
        print(len(secret_msg))
        img_encoded = encode_image(img, secret_msg)

        if img_encoded:
                img_encoded.save(encoded_image_file)

        import os, sys, subprocess

        def open_file(filename):
            if sys.platform == "win32":
                os.startfile(encoded_image_file)
            else:
                opener ="open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, encoded_image_file])

        img2 = Image.open(encoded_image_file)
        hidden_text = decode_image(img2)
        print("Secret message: {}".format(hidden_text))
        img_data= open('enc_Nothingtoseehere.png','rb').read()

        msg=MIMEMultipart()

        try:
          server = smtplib.SMTP('smtp.gmail.com', 587)
          server.ehlo()
        except:
          print("Something went wrong")

        # make connection secure
        server.starttls()
        mypwd=getpass.getpass('Enter your password: ')
        myemail=emailSend
        recip = emailRecip
        server.login(myemail,mypwd)
        image=MIMEImage(img_data,name=os.path.basename('enc_Nothingtoseehere.png'))
        msg.attach(image)
        msg['Subject']='Elction3'
        server.sendmail(myemail,recip,msg.as_string())
        server.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
