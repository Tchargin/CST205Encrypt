from PIL import Image
import smtplib
import getpass
import os, sys, subprocess
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Input message string
encryption=input("Enter the sentence you would like to encrypt: ")

# Start creating the list to shift the message letters
new = list(encryption)
i=0
for letter in encryption:

    if new[i]=='a':
        new[i]= 'd'
    elif new[i]=='b':
        new[i]='e'
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
        new[i]=' '

    i=i+1
msg=str(new)

# Start encode cannot exceed 255 characters.
def encode_image(img, msg):
        length = len(msg)
        if length > 255:
            print("Make the message shorter please < 255 characters.")
            return False

# Create a copy of the new image in the meantime while it puts the information
# inside of the pixel then returns the information to the copy it made.
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

# Start decoding the text that is stored inside of the pixel in the image.
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

# Taking the image copy and making a brand new image with the enc_ extention.
original_image_file = "Image.png"
img = Image.open(original_image_file)

# Giving you the image information: Size, RGB / RGBA.
print(img, img.mode)
encoded_image_file = "enc_" + original_image_file
secret_msg = msg

# Giving you the length of the secret message.
print(len(secret_msg))

# Saving the new image on the desktop with the secret message stored inside.
img_encoded = encode_image(img, secret_msg)
if img_encoded:
        img_encoded.save(encoded_image_file)


# Opening the picture for windows or iOS depending on your system.
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(encoded_image_file)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, encoded_image_file])

# Printing the encoded message on your screen.
img2 = Image.open(encoded_image_file)
hidden_text = decode_image(img2)
print("Secret message: {}".format(hidden_text))
img_data= open('enc_Image.png','rb').read()

# Sending the image through email with a catch.
msg=MIMEMultipart()
try:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
except:
  print("Something went wrong")

# make connection secure
server.starttls()
mypwd=getpass.getpass('Enter your password: ')
myemail="tchargin@csumb.edu"
recip="dgrady@csumb.edu"
server.login(myemail,mypwd)
image=MIMEImage(img_data,name=os.path.basename('enc_Image.png'))
msg.attach(image)
msg['Subject']='Election of 3s'
server.sendmail(myemail,recip,msg.as_string())
server.quit()
