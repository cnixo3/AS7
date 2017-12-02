from tkinter import *
from tkinter.filedialog import askopenfilename



top = Tk()

top.minsize(width=400,height=300)
top.maxsize(width=400,height=300)
menubar = Menu(top)
def updateData(data, name,address,bday):
    tmp = name+', '+address+', '+bday
    data+=tmp
def addPatient(patientData):
    name =''
    address = ''
    bday=''
    root=Tk()
    mainFrame=Frame(root)
    frame1 = Frame(mainFrame)
    frame2 = Frame(mainFrame)
    buttonFrame = Frame(root)
    def grabData():
        name = str(E1.get())
        address =str(E2.get())
        bday=str(E3.get())
        root.destroy()
        updateData(patientData,name,address,bday)
        writeToScreen(patientData)
    E1 = Entry(frame2)
    title = Label(root,text='Enter New Patient Data: ')
    title.pack(side=TOP)
    label = Label(frame1,text='First and Last Name')
    label.pack(side=TOP)
    E1.pack(side=TOP)
    E2 = Entry(frame2)
    label2 = Label(frame1,text='Address')
    label2.pack(side=TOP)
    E2.pack(side=TOP)
    E3 = Entry(frame2)
    label3 = Label(frame1,text='Birthday (mm/dd/yyyy)')
    label3.pack(side=TOP)
    E3.pack(side=TOP)
    frame1.pack(side=LEFT)
    frame2.pack(side=RIGHT)
    B1 = Button(buttonFrame,text='Enter',width=5,command=grabData)
    B1.pack(side=TOP)
    mainFrame.pack(side=TOP)
    buttonFrame.pack(side=BOTTOM)
def writeToScreen(patientData):
    T1 = Text(top)
    T1.pack(side=TOP)
    T1.insert(END,patientData)
def readFromFile(data,patientData):
    handle = open(data)
    patientData+=handle.read()
    writeToScreen(patientData)
def fileSelect(patientData):
    root = Tk()
    root.filename=askopenfilename(initialdir = ".",title ='Select Patient File',
                                  filetypes = (('text files','*.txt'),('all files','*.*')))
    data = root.filename
    readFromFile(data,patientData)
    root.destroy()
patientData=''
filemenu= Menu(menubar,tearoff=0)
filemenu.add_command(label="Open",command = fileSelect(patientData))
filemenu.add_command(label="New", command = addPatient(patientData))
filemenu.add_command(label="Modify")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command = top.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
L1 = Label(top,text='Please load patient file.')
L1.pack(side=TOP)
top.config(menu=menubar)
top.mainloop()
