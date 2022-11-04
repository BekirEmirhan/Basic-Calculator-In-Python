from graphics import *
win = GraphWin(title="Calculator", width=600,height=600)
rectMain = Rectangle(Point(0,0),Point(600,100)).draw(win)
entMain = Entry(Point(300,50),width=20).draw(win)
controller = False #controls number buttons
processController =False #checks process active
first = True #controls number and process
DFA1Controller = False #checks pressed equal button.
start = True #checks if position at start.
twicer = False #checks process pressed twice.
processList = []
mode =""
a = 0
def converter(c):
    if "." in c:
        c= float(c)
    else:
        c =int(c)
    return c
entMain.setText("0")

def AC():
    global processList, controller,processController,first,mode,start,twicer,DFA1Controller
    entMain.setText("0")
    processList = []
    controller = False
    processController =False
    first = True
    mode = ""
    start=True
    twicer=False
    DFA1Controller =False
def sign():
    c = entMain.getText()
    if c[0] == "0" and len(c)==1:
        return
    if c[0] == "-":
        c = c[1:]
    else:
        c = "-" + c
    entMain.setText(int(c))
    c =""
def modder():
    if "." in str(processList[0]):
        newc = float(processList[0])%int(entMain.getText())
    else:
        newc = int(processList[0])%int(entMain.getText())
    if "." in str(newc) and str(newc)[-1] !="0":
        return float(newc)
    elif "." in str(newc) and str(newc)[-1] =="0":
        return int(newc)
    else:
        return int(newc)
def multiplier():
    if "." in str(processList[0]):
        newc = float(processList[0])*int(entMain.getText())
    else:
        newc = int(processList[0])*int(entMain.getText())
    if "." in str(newc) and str(newc)[-1] !="0":
        return float(newc)
    elif "." in str(newc) and str(newc)[-1] =="0":
        return int(newc)
    else:
        return int(newc)
def addtion():
    if "." in str(processList[0]):
        newc = float(processList[0])+int(entMain.getText())
    else:
        newc = int(processList[0])+int(entMain.getText())
    if "." in str(newc) and str(newc)[-1] !="0":
        return float(newc)
    elif "." in str(newc) and str(newc)[-1] =="0":
        return int(newc)
    else:
        return int(newc)
def substraction():
    if "." in str(processList[0]):
        newc = float(processList[0])-int(entMain.getText())
    else:
        newc = int(processList[0])-int(entMain.getText())
    if "." in str(newc) and str(newc)[-1] !="0":
        return float(newc)
    elif "." in str(newc) and str(newc)[-1] =="0":
        return int(newc)
    else:
        return int(newc)
def division():
    if "." in str(processList[0]):
        newc = float(processList[0])/float(entMain.getText())
    else:
        newc = int(processList[0])/int(entMain.getText())
    if "." in str(newc) and str(newc)[-1] !="0":
        return float(newc)
    elif "." in str(newc) and str(newc)[-1] =="0":
        return int(newc)
    else:
        return int(newc)
def power():
    if "." in str(processList[0]):
        newc = float(processList[0])**int(entMain.getText())
    else:
        newc = int(processList[0])**int(entMain.getText())
    if "." in str(newc) and str(newc)[-1] !="0":
        return float(newc)
    elif "." in str(newc) and str(newc)[-1] =="0":
        return int(newc)
    else:
        return int(newc)
def equal(a):
    entMain.setText(str(a))
    return a



def b0():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "0"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="0"
        entMain.setText(c)
        return
    c = entMain.getText() + "0"
    entMain.setText(c)
    c=""
def b1():
    global first
    if controller:
        if first:
            entMain.setText("")
            first = False
        c = entMain.getText() + "1"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="1"
        entMain.setText(c)
        return
    c = entMain.getText() + "1"
    entMain.setText(c)
    c=""
def b2():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "2"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="2"
        entMain.setText(c)
        return
    c = entMain.getText() + "2"
    entMain.setText(c)
    c=""
def b3():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "3"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="3"
        entMain.setText(c)
        return
    c = entMain.getText() + "3"
    entMain.setText(c)
    c=""
def b4():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "4"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="4"
        entMain.setText(c)
        return
    c = entMain.getText() + "4"
    entMain.setText(c)
    c=""
def b5():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "5"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="5"
        entMain.setText(c)
        return
    c = entMain.getText() + "5"
    entMain.setText(c)
    c=""
def b6():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "6"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="6"
        entMain.setText(c)
        return
    c = entMain.getText() + "6"
    entMain.setText(c)
    c=""
def b7():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "7"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="7"
        entMain.setText(c)
        return
    c = entMain.getText() + "7"
    entMain.setText(c)
    c=""
def b8():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "8"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="8"
        entMain.setText(c)
        return
    c = entMain.getText() + "8"
    entMain.setText(c)
    c=""
def b9():
    global first
    if controller:
        if first:
            entMain.setText("")
            first=False
        c = entMain.getText() + "9"
        entMain.setText(c)
        return
    if entMain.getText() == "0" and len(entMain.getText()) ==1:
        c ="9"
        entMain.setText(c)
        return
    c = entMain.getText() + "9"
    entMain.setText(c)
    c=""






btnAC = Rectangle(Point(0,100),Point(150,200)).draw(win)
textAC = Text(Point(75,150),text="AC").draw(win)
ACList = []
for x in range(0,150):
    for y in range(100,200):
        ACList.append((x,y))

btnSign = btnAC.clone()
btnSign.move(150,0)
btnSign.draw(win)
textSign = Text(Point(225,150),text="+/-").draw(win)
signList = []
for x in range(150,300):
    for y in range(100,200):
       signList.append((x,y))

btnModder = btnAC.clone()
btnModder.move(300,0)
btnModder.draw(win)
textModder = Text(Point(375,150),text="%").draw(win)
modderList = []
for x in range(300,450):
    for y in range(100,200):
       modderList.append((x,y)) 

btnDivider = btnAC.clone()
btnDivider.move(450,0)
btnDivider.draw(win)
textDivider = Text(Point(525,150),text="/").draw(win)
dividerList = []
for x in range(450,600):
    for y in range(100,200):
       dividerList.append((x,y))


btn7 = btnAC.clone()
btn7.move(0,100)
btn7.draw(win)
text7 = Text(Point(75,250),text="7").draw(win)
sevenList = []
for x in range(0,150):
    for y in range(200,300):
       sevenList.append((x,y))

btn8 = btnAC.clone()
btn8.move(150,100)
btn8.draw(win)
text8 = Text(Point(225,250),text="8").draw(win)
eigthList = []
for x in range(150,300):
    for y in range(200,300):
       eigthList.append((x,y))

btn9 = btnAC.clone()
btn9.move(300,100)
btn9.draw(win)
text9 = Text(Point(375,250),text="9").draw(win)
nineList = []
for x in range(300,450):
    for y in range(200,300):
       nineList.append((x,y)) 

btnMultiply = btnAC.clone()
btnMultiply.move(450,100)
btnMultiply.draw(win)
textMultiply = Text(Point(525,250),text="X").draw(win)
MultiplyList = []
for x in range(450,600):
    for y in range(200,300):
       MultiplyList.append((x,y))


btn4 = btnAC.clone()
btn4.move(0,200)
btn4.draw(win)
text4 = Text(Point(75,350),text="4").draw(win)
fourList = []
for x in range(0,150):
    for y in range(300,400):
       fourList.append((x,y))

btn5 = btnAC.clone()
btn5.move(150,200)
btn5.draw(win)
text5 = Text(Point(225,350),text="5").draw(win)
fiveList = []
for x in range(150,300):
    for y in range(300,400):
       fiveList.append((x,y))

btn6 = btnAC.clone()
btn6.move(300,200)
btn6.draw(win)
text6 = Text(Point(375,350),text="6").draw(win)
sixList = []
for x in range(300,450):
    for y in range(300,400):
       sixList.append((x,y)) 

btnSubstract = btnAC.clone()
btnSubstract.move(450,200)
btnSubstract.draw(win)
textSubstract = Text(Point(525,350),text="-").draw(win)
SubstractList = []
for x in range(450,600):
    for y in range(300,400):
       SubstractList.append((x,y))


btn1 = btnAC.clone()
btn1.move(0,300)
btn1.draw(win)
text1 = Text(Point(75,450),text="1").draw(win)
oneList = []
for x in range(0,150):
    for y in range(400,500):
       oneList.append((x,y))

btn2 = btnAC.clone()
btn2.move(150,300)
btn2.draw(win)
text2 = Text(Point(225,450),text="2").draw(win)
twoList = []
for x in range(150,300):
    for y in range(400,500):
       twoList.append((x,y))

btn3 = btnAC.clone()
btn3.move(300,300)
btn3.draw(win)
text3 = Text(Point(375,450),text="3").draw(win)
threeList = []
for x in range(300,450):
    for y in range(400,500):
       threeList.append((x,y))


btnAdd = btnAC.clone()
btnAdd.move(450,300)
btnAdd.draw(win)
textAdd = Text(Point(525,450),text="+").draw(win)
AddList = []
for x in range(450,600):
    for y in range(400,500):
       AddList.append((x,y))


btn0 = Rectangle(Point(0,500),Point(300,600)).draw(win)
text0 = Text(Point(150,550),text="0").draw(win)
zeroList = []
for x in range(0,300):
    for y in range(500,600):
       zeroList.append((x,y))

btnExponent = btnAC.clone()
btnExponent.move(300,400)
btnExponent.draw(win)
textExponent = Text(Point(375,550),text="**").draw(win)
ExponentList = []
for x in range(300,450):
    for y in range(500,600):
       ExponentList.append((x,y))

btnEqual = btnAC.clone()
btnEqual.move(450,400)
btnEqual.draw(win)
textEqual = Text(Point(525,550),text="=").draw(win)
EqualList = []
for x in range(450,600):
    for y in range(500,600):
       EqualList.append((x,y))

def numberEntry(command):
    if command in zeroList:
        b0()
    if command in oneList:
        b1()
    if command in twoList:
        b2()
    if command in threeList:
        b3()
    if command in fourList:
        b4()
    if command in fiveList:
        b5()
    if command in sixList:
        b6()
    if command in sevenList:
        b7()
    if command in eigthList:
        b8()
    if command in nineList:
        b9()
def extends(L,*args):
    for arg in args:
        for x in arg:
            L.append(x)
    return L
numbersList = []
extends(numbersList, zeroList,oneList,twoList,threeList,fourList,fiveList,sixList,sevenList,eigthList,nineList)



while True:
    try:
        c = ""
        com = win.getMouse()
        command = (com.getX(),com.getY())
        numberEntry(command)
        if command in numbersList:
            start = False
            twicer=False
        if DFA1Controller and command in numbersList:
            AC()
        else:
            DFA1Controller=False
        if mode!="":
            if mode=="add":
                try:
                    a = addtion()
                except:
                    AC()
                    continue
            if mode =="sub":
                try:
                    a = substraction()
                except:
                    AC()
                    continue
            if mode=="mul":
                try:
                    a = multiplier()
                except:
                    AC()
                    continue
            if mode=="mod":
                try:
                    a = modder()
                except:
                    AC()
                    continue
            if mode=="div":
                try:
                    a = division()
                except:
                    AC()
                    continue
            if mode=="pow":
                try:
                    a = power()
                except:
                    AC()
                    continue
        if command in ACList:
            AC()
        if command in signList:
            sign()
            a =-a
        if command in modderList and start==False:
            if processController and twicer==False:
                try:
                    b = equal(a)
                except:
                    AC()
                    continue
                processList[0] = b
                controller = True
                first = True
                mode = "mod"
                twicer = True
                continue
            elif processController == True and twicer==True:
                AC()
                continue
            processList.append(entMain.getText())
            controller = True
            processController = True
            controller = True
            mode = "mod"
            processController = True
            if twicer:
                AC()
                continue
            twicer=True
        if command in MultiplyList and start==False:
            if processController and twicer==False:
                try:
                    b = equal(a)
                except:
                    AC()
                    continue
                processList[0] = b
                controller = True
                first = True
                mode = "mul"
                twicer = True
                continue
            elif processController == True and twicer==True and mode=="mul":
                AC()
                continue
            processList.append(entMain.getText())
            controller = True
            processController = True
            controller = True
            mode = "mul"
            processController = True
            if twicer:
                AC()
                continue
            twicer=True
        if command in AddList and start==False:
            if processController and twicer==False:
                try:
                    b = equal(a)
                except:
                    AC()
                    continue
                processList[0] = b
                controller = True
                first = True
                mode = "add"
                twicer = True
                continue
            elif processController == True and twicer==True:
                AC()
                continue
            processList.append(entMain.getText())
            controller = True
            processController = True
            controller = True
            if twicer:
                AC()
                continue
            mode = "add"
            twicer=True
        if command in SubstractList and start==False:
            if processController and twicer==False:
                try:
                    b = equal(a)
                except:
                    AC()
                    continue
                processList[0] = b
                controller = True
                first = True
                mode = "sub"
                twicer = True
                continue
            elif processController == True and twicer==True:
                AC()
                continue
            processList.append(entMain.getText())
            controller = True
            processController = True
            controller = True
            mode = "sub"
            if twicer:
                AC()
                continue
            twicer=True
        if command in dividerList and start==False:
            if processController and twicer==False:
                try:
                    b = equal(a)
                except:
                    AC()
                    continue
                processList[0] = b
                controller = True
                first = True
                mode = "div"
                twicer = True
                continue
            elif processController == True and twicer==True:
                AC()
                continue
            processList.append(entMain.getText())
            controller = True
            processController = True
            controller = True
            mode = "div"
            processController = True
            if twicer:
                AC()
                continue
            twicer=True
        if command in ExponentList and start==False:
            if processController and twicer==False:
                try:
                    b = equal(a)
                except:
                    AC()
                processList[0] = b
                controller = True
                first = True
                mode = "pow"
                twicer = True
                continue
            elif processController == True and twicer==True:
                AC()
                continue
            processList.append(entMain.getText())
            controller = True
            processController = True
            controller = True
            mode = "pow"
            if twicer:
                AC()
                continue
            twicer=True
        if command in EqualList and start==False:
            equal(a)
            DFA1Controller = True
            controller = False
            first =True
            processController =False
            processList[0] = entMain.getText()
    except GraphicsError:
        win.close()
        break
