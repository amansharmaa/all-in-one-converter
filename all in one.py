from tkinter import *
import smtplib
root = Tk()
global userr
def lengconvert():
  userr = ename.get()
  a=int(l.get())
  b=int(l1.get())
  c=float(valuenter.get())
  if (a==1):
    c=c/1000
  elif (a==2):
    c=c/100
  elif (a==4):
    c=c*1000
  elif (a==5):
    c=c*0.0254
  elif (a==6):
    c=c*0.3048
  elif (a==7):
    c=c/1000000
  if (b==1):
    c=c*1000
  elif (b==2):
    c=c*100
  elif (b==4):
    c=c/1000
  elif (b==5):
    c=c/0.0254
  elif (b==6):
    c=c/0.3048
  elif (b==7):
    c=c*1000000
  valuenter.delete(0, END)
  valuenter.insert(0 , c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting length where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def areaconvert():
  userr = ename.get()
  a = int(a1.get())
  b = int(a2.get())
  c = float(valuenter1.get())
  if (a==1):
    c=c/(1000*1000)
  elif (a==2):
    c=c/(100*100)
  elif (a==4):
    c=c*(1000*1000)
  elif (a==5):
    c=c*(0.0254*0.0254)
  elif (a==6):
    c=c*(0.3048*0.3048)
  elif (a==7):
    c=c/(1000000*1000000)
  if (b==1):
    c=c*(1000*1000)
  elif (b==2):
    c=c*(100*100)
  elif (b==4):
    c=c/(1000*1000)
  elif (b==5):
    c=c/(0.0254*0.0254)
  elif (b==6):
    c=c/(0.3048*0.3048)
  elif (b==7):
    c=c*(1000000*1000000)

  valuenter1.delete(0, END)
  valuenter1.insert(0 , c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting area where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def volumeconvert():
  userr = ename.get()
  a = int(v1.get())
  b = int(v2.get())
  c = float(valuenter2.get())
  if (a==1):
    c=c/(1000*1000*1000)
  elif (a==2):
    c=c/(100*100*100)
  elif (a==4):
    c=c*(1000*1000*1000)
  elif (a==5):
    c=c*(0.0254*0.0254*0.0254)
  elif (a==6):
    c=c*(0.3048*0.3048*0.3048)
  elif (a==7):
    c=c/(1000000*1000000*1000000)
  if (b==1):
    c=c*(1000*1000*1000)
  elif (b==2):
    c=c*(100*100*100)
  elif (b==4):
    c=c/(1000*1000*1000)
  elif (b==5):
    c=c/(0.0254*0.0254*0.0254)
  elif (b==6):
    c=c/(0.3048*0.3048*0.3048)
  elif (b==7):
    c=c*(1000000*1000000*1000000)
  valuenter2.delete(0, END)
  valuenter2.insert(0, c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting volume where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def weightconvert():
  userr = ename.get()
  a = int(w1.get())
  b = int(w2.get())
  c = float(valuenter4.get())
  if (a==1):
    c=c/0.000000001
  elif (a==2):
    c=c/0.000001
  elif (a==4):
    c=c/0.001
  elif (a==5):
    c=c/0.000002204623
  elif (a==6):
    c=c/0.000000157473
  elif (a==7):
    c=c/0.00003527396
  if (b==1):
    c=c*0.000000001
  elif (b==2):
    c=c*0.000001
  elif (b==4):
    c=c*0.001
  elif (b==5):
    c=c*0.000002204623
  elif (b==6):
    c=c*0.000000157473
  elif (b==7):
    c=c*0.00003527396
  valuenter4.delete(0, END)
  valuenter4.insert(0, c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting weight where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def pressureconvert():
  userr = ename.get()
  a = int(p1.get())
  b = int(p2.get())
  c = float(valuenter3.get())
  if (a==1):
    c=c*101325
  elif (a==2):
    c=c*100000
  elif (a==4):
    c=c*100
  elif (a==5):
    c=c*1000
  elif (a==6):
    c=c*133.3224
  elif (a==7):
    c=c*6894.7573
  if (b==1):
    c=c/101325
  elif (b==2):
    c=c/100000
  elif (b==4):
    c=c/100
  elif (b==5):
    c=c/1000
  elif (b==6):
    c=c/133.3224
  elif (b==7):
    c=c/6894.7573
  valuenter3.delete(0, END)
  valuenter3.insert(0, c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting pressure where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def temperatureconvert():
  userr = ename.get()
  a = int(t1.get())
  b = int(t2.get())
  c = float(valuenter7.get())
  if (a==1):
    c=c-273.15
  elif (a==3):
    c=(c - 32) * 5/9
  if (b==1):
    c=c + 273.15
  elif (b==3):
    c=(c * 9/5) + 32
  valuenter7.delete(0, END)
  valuenter7.insert(0, c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting temperature where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def currencyconvert():
  userr = ename.get()
  a = int(c1.get())
  b = int(c2.get())
  c = float(valuenter6.get())
  if (a==1):
    c=c*74.1873
  elif (a==2):
    c=c*87.9658
  elif (a==4):
    c=c*97.3874
  elif (a==5):
    c=c*56.7596
  elif (a==6):
    c=c*55.0535
  elif (a==7):
    c=c*53.9254
  if (b==1):
    c=c/74.1873
  elif (b==2):
    c=c/87.9658
  elif (b==4):
    c=c/97.3874
  elif (b==5):
    c=c/56.7596
  elif (b==6):
    c=c/55.0535
  elif (b==7):
    c=c/53.9254
  valuenter6.delete(0, END)
  valuenter6.insert(0, c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting currency where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def speedconvert():
  userr = ename.get()
  a = int(s1.get())
  b = int(s2.get())
  c = float(valuenter8.get())
  if (a==1):
    c=c*3.6
  elif (a==3):
    c=c*1.60934
  if (b==1):
    c=c/3.6
  elif (b==3):
    c=c/1.60934
  valuenter8.delete(0, END)
  valuenter8.insert(0, c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting speed where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
def powerconvert():
  userr = ename.get()
  a = int(po1.get())
  b = int(po2.get())
  c = float(valuenter5.get())
  if (a==1):
    c=c/0.000001
  elif (a==2):
    c=c/0.001
  elif (a==4):
    c=c/0.000000001
  elif (a==5):
    c=c/0.000001341
  elif (a==6):
    c=c/10000
  elif (a==7):
    c=c/0.000238845
  if (b==1):
    c=c*0.000001
  elif (b==2):
    c=c*0.001
  elif (b==4):
    c=c*0.000000001
  elif (b==5):
    c=c*0.000001341
  elif (b==6):
    c=c*10000
  elif (b==7):
    c=c*0.000238845
  valuenter5.delete(0, END)
  valuenter5.insert(0, c)
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)
  s.starttls()
  Sender_mail = 'project6043@gmail.com'
  Sender_mail_password = 'klkliipp'
  try:
      s.login(Sender_mail, Sender_mail_password)
  except:
      print("Wrong Mail_id or Password...!Try Again...")
      exit()
  To_mail = 'aman.sharma23432@gmail.com'
  Message =  str(c) + ' is the value recived by ' + userr + ' after converting power where a = ' + str(a) + ' and b = ' +str(b)
  s.sendmail(Sender_mail, To_mail, Message)
  s.quit()
root.geometry("200x400")
root.title('all in one')
quitbut = Button(root , text="exit the converter",command=root.quit)
r=IntVar()
l1=IntVar()
l=IntVar()
a1=IntVar()
a2=IntVar()
v1=IntVar()
v2=IntVar()
p1=IntVar()
p2=IntVar()
w1=IntVar()
w2=IntVar()
po1=IntVar()
po2=IntVar()
c1=IntVar()
c2=IntVar()
t1=IntVar()
t2=IntVar()
s1=IntVar()
s2=IntVar()
def dimensions(r):
  if (r==1):
    global lengthh
    lengthh = Toplevel()
    lengthh.title("length conversion")
    ask1=Label(lengthh , text = 'select the unit in which you want\n to convert and from which you want to')
    ask1.grid(row='0',column='1')
    Radiobutton(lengthh, text='milimeter ', variable=l, value=1).grid(row='1',column='0')
    Radiobutton(lengthh, text='centimeter', variable=l, value=2).grid(row='2',column='0')
    Radiobutton(lengthh, text='meter     ', variable=l, value=3).grid(row='3',column='0')
    Radiobutton(lengthh, text='kilometer ', variable=l, value=4).grid(row='4',column='0')
    Radiobutton(lengthh, text='inch      ', variable=l, value=5).grid(row='5',column='0')
    Radiobutton(lengthh, text='foot      ', variable=l, value=6).grid(row='6',column='0')
    Radiobutton(lengthh, text='micrometer', variable=l, value=7).grid(row='7',column='0')
    global valuenter
    valuenter = Entry(lengthh , width = '30')
    valuenter.grid(row='4',column='1')
    Radiobutton(lengthh, text='milimeter ', variable=l1, value=1).grid(row='1', column='2')
    Radiobutton(lengthh, text='centimeter', variable=l1, value=2).grid(row='2', column='2')
    Radiobutton(lengthh, text='meter     ', variable=l1, value=3).grid(row='3', column='2')
    Radiobutton(lengthh, text='kilometer ', variable=l1, value=4).grid(row='4', column='2')
    Radiobutton(lengthh, text='inch      ', variable=l1, value=5).grid(row='5', column='2')
    Radiobutton(lengthh, text='foot      ', variable=l1, value=6).grid(row='6', column='2')
    Radiobutton(lengthh, text='micrometer', variable=l1, value=7).grid(row='7', column='2')
    lconvertbutt= Button(lengthh , text='perform conversion', command=lengconvert)
    lconvertbutt.grid(row='5',column='1')
    quitbutl = Button(lengthh, text="close and go back", command=lengthh.destroy)
    quitbutl.grid(row = '7' , column='1')
  elif (r==2):
    global areaa
    areaa = Toplevel()
    areaa.title("area conversion")
    ask1 = Label(areaa, text='select the unit in which you want\n to convert and from which you want to')
    ask1.grid(row='0', column='1')
    Radiobutton(areaa, text='milimeter sq ', variable=a1, value=1).grid(row='1', column='0')
    Radiobutton(areaa, text='centimeter sq', variable=a1, value=2).grid(row='2', column='0')
    Radiobutton(areaa, text='meter sq     ', variable=a1, value=3).grid(row='3', column='0')
    Radiobutton(areaa, text='kilometer sq ', variable=a1, value=4).grid(row='4', column='0')
    Radiobutton(areaa, text='inch sq      ', variable=a1, value=5).grid(row='5', column='0')
    Radiobutton(areaa, text='foot sq      ', variable=a1, value=6).grid(row='6', column='0')
    Radiobutton(areaa, text='micrometer sq', variable=a1, value=7).grid(row='7', column='0')
    global valuenter1
    valuenter1 = Entry(areaa, width='30')
    valuenter1.grid(row='4', column='1')
    Radiobutton(areaa, text='milimeter sq ', variable=a2, value=1).grid(row='1', column='2')
    Radiobutton(areaa, text='centimeter sq', variable=a2, value=2).grid(row='2', column='2')
    Radiobutton(areaa, text='meter sq     ', variable=a2, value=3).grid(row='3', column='2')
    Radiobutton(areaa, text='kilometer sq ', variable=a2, value=4).grid(row='4', column='2')
    Radiobutton(areaa, text='inch sq      ', variable=a2, value=5).grid(row='5', column='2')
    Radiobutton(areaa, text='foot sq      ', variable=a2, value=6).grid(row='6', column='2')
    Radiobutton(areaa, text='micrometer sq', variable=a2, value=7).grid(row='7', column='2')
    lconvertbutt = Button(areaa, text='perform conversion', command=areaconvert)
    lconvertbutt.grid(row='5', column='1')
    quitbutl = Button(areaa, text="close and go back", command=areaa.destroy)
    quitbutl.grid(row='7', column='1')
  elif (r==3):
    global volumee
    volumee = Toplevel()
    volumee.title("volume conversion")
    ask1 = Label(volumee, text='select the unit in which you want\n to convert and from which you want to')
    ask1.grid(row='0', column='1')
    Radiobutton(volumee, text='milimeter cube ', variable=v1, value=1).grid(row='1', column='0')
    Radiobutton(volumee, text='centimeter cube', variable=v1, value=2).grid(row='2', column='0')
    Radiobutton(volumee, text='meter cube     ', variable=v1, value=3).grid(row='3', column='0')
    Radiobutton(volumee, text='kilometer cube ', variable=v1, value=4).grid(row='4', column='0')
    Radiobutton(volumee, text='inch cube      ', variable=v1, value=5).grid(row='5', column='0')
    Radiobutton(volumee, text='foot cube      ', variable=v1, value=6).grid(row='6', column='0')
    Radiobutton(volumee, text='micrometer cube', variable=v1, value=7).grid(row='7', column='0')
    global valuenter2
    valuenter2 = Entry(volumee, width='30')
    valuenter2.grid(row='4', column='1')
    Radiobutton(volumee, text='milimeter cube ', variable=v2, value=1).grid(row='1', column='2')
    Radiobutton(volumee, text='centimeter cube', variable=v2, value=2).grid(row='2', column='2')
    Radiobutton(volumee, text='meter cube     ', variable=v2, value=3).grid(row='3', column='2')
    Radiobutton(volumee, text='kilometer cube ', variable=v2, value=4).grid(row='4', column='2')
    Radiobutton(volumee, text='inch cube      ', variable=v2, value=5).grid(row='5', column='2')
    Radiobutton(volumee, text='foot cube      ', variable=v2, value=6).grid(row='6', column='2')
    Radiobutton(volumee, text='micrometer cube', variable=v2, value=7).grid(row='7', column='2')
    lconvertbutt = Button(volumee, text='perform conversion', command=volumeconvert)
    lconvertbutt.grid(row='5', column='1')
    quitbutl = Button(volumee, text="close and go back", command=volumee.destroy)
    quitbutl.grid(row='7', column='1')
  elif (r==4):
    global pressuree
    pressuree = Toplevel()
    pressuree.title("pressure conversion")
    ask1 = Label(pressuree, text='select the unit in which you want\n to convert and from which you want to')
    ask1.grid(row='0', column='1')
    Radiobutton(pressuree, text='atmosphere ', variable=p1, value=1).grid(row='1', column='0')
    Radiobutton(pressuree, text='bar        ', variable=p1, value=2).grid(row='2', column='0')
    Radiobutton(pressuree, text='pascal     ', variable=p1, value=3).grid(row='3', column='0')
    Radiobutton(pressuree, text='milibar    ', variable=p1, value=4).grid(row='4', column='0')
    Radiobutton(pressuree, text='kilopascal ', variable=p1, value=5).grid(row='5', column='0')
    Radiobutton(pressuree, text='torr       ', variable=p1, value=6).grid(row='6', column='0')
    Radiobutton(pressuree, text='psi        ', variable=p1, value=7).grid(row='7', column='0')
    global valuenter3
    valuenter3 = Entry(pressuree, width='30')
    valuenter3.grid(row='4', column='1')
    Radiobutton(pressuree, text='atmosphere ', variable=p2, value=1).grid(row='1', column='2')
    Radiobutton(pressuree, text='bar        ', variable=p2, value=2).grid(row='2', column='2')
    Radiobutton(pressuree, text='pascal     ', variable=p2, value=3).grid(row='3', column='2')
    Radiobutton(pressuree, text='milibar    ', variable=p2, value=4).grid(row='4', column='2')
    Radiobutton(pressuree, text='kilopascal ', variable=p2, value=5).grid(row='5', column='2')
    Radiobutton(pressuree, text='torr       ', variable=p2, value=6).grid(row='6', column='2')
    Radiobutton(pressuree, text='psi        ', variable=p2, value=7).grid(row='7', column='2')
    lconvertbutt = Button(pressuree, text='perform conversion', command=pressureconvert)
    lconvertbutt.grid(row='5', column='1')
    quitbutl = Button(pressuree, text="close and go back", command=pressuree.destroy)
    quitbutl.grid(row='7', column='1')
  elif (r==5):
    global weightt
    weightt = Toplevel()
    weightt.title("weight conversion")
    ask1 = Label(weightt, text='select the unit in which you want\n to convert and from which you want to')
    ask1.grid(row='0', column='1')
    Radiobutton(weightt, text='metric ton ', variable=w1, value=1).grid(row='1', column='0')
    Radiobutton(weightt, text='kilogram   ', variable=w1, value=2).grid(row='2', column='0')
    Radiobutton(weightt, text='miligram   ', variable=w1, value=3).grid(row='3', column='0')
    Radiobutton(weightt, text='gram       ', variable=w1, value=4).grid(row='4', column='0')
    Radiobutton(weightt, text='pounds     ', variable=w1, value=5).grid(row='5', column='0')
    Radiobutton(weightt, text='stones     ', variable=w1, value=6).grid(row='6', column='0')
    Radiobutton(weightt, text='ounces     ', variable=w1, value=7).grid(row='7', column='0')
    global valuenter4
    valuenter4 = Entry(weightt, width='30')
    valuenter4.grid(row='4', column='1')
    Radiobutton(weightt, text='metric ton ', variable=w2, value=1).grid(row='1', column='2')
    Radiobutton(weightt, text='kilogram   ', variable=w2, value=2).grid(row='2', column='2')
    Radiobutton(weightt, text='miligram   ', variable=w2, value=3).grid(row='3', column='2')
    Radiobutton(weightt, text='gram       ', variable=w2, value=4).grid(row='4', column='2')
    Radiobutton(weightt, text='pounds     ', variable=w2, value=5).grid(row='5', column='2')
    Radiobutton(weightt, text='stones     ', variable=w2, value=6).grid(row='6', column='2')
    Radiobutton(weightt, text='ounces     ', variable=w2, value=7).grid(row='7', column='2')
    lconvertbutt = Button(weightt, text='perform conversion', command=weightconvert)
    lconvertbutt.grid(row='5', column='1')
    quitbutl = Button(weightt, text="close and go back", command=weightt.destroy)
    quitbutl.grid(row='7', column='1')
  elif (r==6):
    global powerr
    powerr = Toplevel()
    powerr.title("power conversion")
    ask1 = Label(powerr, text='select the unit in which you want\n to convert and from which you want to')
    ask1.grid(row='0', column='1')
    Radiobutton(powerr, text='kiloWatt           ', variable=po1, value=1).grid(row='1', column='0')
    Radiobutton(powerr, text='Watt               ', variable=po1, value=2).grid(row='2', column='0')
    Radiobutton(powerr, text='miliWatt           ', variable=po1, value=3).grid(row='3', column='0')
    Radiobutton(powerr, text='megaWatt           ', variable=po1, value=4).grid(row='4', column='0')
    Radiobutton(powerr, text='horsepower         ', variable=po1, value=5).grid(row='5', column='0')
    Radiobutton(powerr, text='erg per second     ', variable=po1, value=6).grid(row='6', column='0')
    Radiobutton(powerr, text='calories per second', variable=po1, value=7).grid(row='7', column='0')
    global valuenter5
    valuenter5 = Entry(powerr, width='30')
    valuenter5.grid(row='4', column='1')
    Radiobutton(powerr, text='kiloWatt           ', variable=po2, value=1).grid(row='1', column='2')
    Radiobutton(powerr, text='Watt               ', variable=po2, value=2).grid(row='2', column='2')
    Radiobutton(powerr, text='miliWatt           ', variable=po2, value=3).grid(row='3', column='2')
    Radiobutton(powerr, text='megaWatt           ', variable=po2, value=4).grid(row='4', column='2')
    Radiobutton(powerr, text='horsepower         ', variable=po2, value=5).grid(row='5', column='2')
    Radiobutton(powerr, text='erg per second     ', variable=po2, value=6).grid(row='6', column='2')
    Radiobutton(powerr, text='calories per second', variable=po2, value=7).grid(row='7', column='2')
    lconvertbutt = Button(powerr, text='perform conversion', command=powerconvert)
    lconvertbutt.grid(row='5', column='1')
    quitbutl = Button(powerr, text="close and go back", command=powerr.destroy)
    quitbutl.grid(row='7', column='1')
  elif (r==7):
    global currencyy
    currencyy = Toplevel()
    currencyy.title("currency conversion")
    ask1 = Label(currencyy, text='select the unit in which you want\n to convert and from which you want to \n(Last updated: 2020-11-06 10:17 UTC)')
    ask1.grid(row='0', column='1')
    Radiobutton(currencyy, text='US dollar        ', variable=c1, value=1).grid(row='1', column='0')
    Radiobutton(currencyy, text='Euro             ', variable=c1, value=2).grid(row='2', column='0')
    Radiobutton(currencyy, text='Indian rupee     ', variable=c1, value=3).grid(row='3', column='0')
    Radiobutton(currencyy, text='British pound    ', variable=c1, value=4).grid(row='4', column='0')
    Radiobutton(currencyy, text='Canadian dollar  ', variable=c1, value=5).grid(row='5', column='0')
    Radiobutton(currencyy, text='singapore dollar ', variable=c1, value=6).grid(row='6', column='0')
    Radiobutton(currencyy, text='aurtralian dollar', variable=c1, value=7).grid(row='7', column='0')
    global valuenter6
    valuenter6 = Entry(currencyy, width='30')
    valuenter6.grid(row='4', column='1')
    Radiobutton(currencyy, text='US dollar        ', variable=c2, value=1).grid(row='1', column='2')
    Radiobutton(currencyy, text='Euro             ', variable=c2, value=2).grid(row='2', column='2')
    Radiobutton(currencyy, text='Indian rupee     ', variable=c2, value=3).grid(row='3', column='2')
    Radiobutton(currencyy, text='British pound    ', variable=c2, value=4).grid(row='4', column='2')
    Radiobutton(currencyy, text='Canadian dollar  ', variable=c2, value=5).grid(row='5', column='2')
    Radiobutton(currencyy, text='singapore dollar ', variable=c2, value=6).grid(row='6', column='2')
    Radiobutton(currencyy, text='australian dollar', variable=c2, value=7).grid(row='7', column='2')
    lconvertbutt = Button(currencyy, text='perform conversion', command=currencyconvert)
    lconvertbutt.grid(row='5', column='1')
    quitbutl = Button(currencyy, text="close and go back", command=currencyy.destroy)
    quitbutl.grid(row='7', column='1')
  elif (r==8):
    global temperatt
    temperatt = Toplevel()
    temperatt.title("temperature conversion")
    ask1 = Label(temperatt, text='select the unit in which you want\n to convert and from which you want to ')
    ask1.grid(row='0', column='1')
    Radiobutton(temperatt, text='kelvin    ', variable=t1, value=1).grid(row='1', column='0')
    Radiobutton(temperatt, text='celsius   ', variable=t1, value=2).grid(row='2', column='0')
    Radiobutton(temperatt, text='fahrenheit', variable=t1, value=3).grid(row='3', column='0')
    global valuenter7
    valuenter7 = Entry(temperatt, width='30')
    valuenter7.grid(row='2', column='1')
    Radiobutton(temperatt, text='kelvin    ', variable=t2, value=1).grid(row='1', column='2')
    Radiobutton(temperatt, text='celsius   ', variable=t2, value=2).grid(row='2', column='2')
    Radiobutton(temperatt, text='fahrenheit', variable=t2, value=3).grid(row='3', column='2')
    lconvertbutt = Button(temperatt, text='perform conversion', command=temperatureconvert)
    lconvertbutt.grid(row='3', column='1',pady='7')
    quitbutl = Button(temperatt, text="close and go back", command=temperatt.destroy)
    quitbutl.grid(row='7', column='1')
  elif (r==9):
    global speedd
    speedd = Toplevel()
    speedd.title("speed conversion")
    ask1 = Label(speedd, text='select the unit in which you want\n to convert and from which you want to ')
    ask1.grid(row='0', column='1')
    Radiobutton(speedd, text='meter per second  ', variable=s1, value=1).grid(row='1', column='0')
    Radiobutton(speedd, text='kilometer per hour', variable=s1, value=2).grid(row='2', column='0')
    Radiobutton(speedd, text='miles per hour    ', variable=s1, value=3).grid(row='3', column='0')
    global valuenter8
    valuenter8 = Entry(speedd, width='30')
    valuenter8.grid(row='2', column='1')
    Radiobutton(speedd, text='meter per second  ', variable=s2, value=1).grid(row='1', column='2')
    Radiobutton(speedd, text='kilometer per hour', variable=s2, value=2).grid(row='2', column='2')
    Radiobutton(speedd, text='miles per hour    ', variable=s2, value=3).grid(row='3', column='2')
    lconvertbutt = Button(speedd, text='perform conversion', command=speedconvert)
    lconvertbutt.grid(row='3', column='1',pady='7')
    quitbutl = Button(speedd, text="close and go back", command=speedd.destroy)
    quitbutl.grid(row='7', column='1')
namelan = Label(text ='enter your name' ).pack(pady=7)
ename = Entry(root,)
ename.get()
ename.pack(pady="7")
unitlab = Label(text ='select the unit' ).pack(pady=7)
Radiobutton(root , text='length     ' , variable=r , value=1).pack()
Radiobutton(root , text='area       ' , variable=r , value=2).pack()
Radiobutton(root , text='volume     ' , variable=r , value=3).pack()
Radiobutton(root , text='pressure   ' , variable=r , value=4).pack()
Radiobutton(root , text='weight     ' , variable=r , value=5).pack()
Radiobutton(root , text='power      ' , variable=r , value=6).pack()
Radiobutton(root , text='currency   ' , variable=r , value=7).pack()
Radiobutton(root , text='temperature' , variable=r , value=8).pack()
Radiobutton(root , text='speed      ' , variable=r , value=9).pack()
getdimensionbutt=Button(root , text='start conversion',command=lambda: dimensions(r.get()))
getdimensionbutt.pack(pady='7')
quitbut.pack()

root.mainloop()

