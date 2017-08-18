from Tkinter import*
from PIL import ImageTk
import Tkinter as tk
import sys


phone_no = [ 9974125569,9712761520,9408750905,8487063435,9408009090,9987968345,9497845326,9712345678,9408750999,9498790905]
a = 0


win = Tk()

def exit1():
    win.destroy()
    
def backEnd(name,age,area,income,ndoc,dcod,lvisit,lail,pres,pres1,pres2,medf):
    mainText = Text(win,height =36,width = 60,bg= 'black',fg = 'white')
    print(mainText.insert(INSERT,'\n\n\n' ))
    print(mainText.insert(INSERT,'Name of patient' +'\t\t\t' ))
    print(mainText.insert(INSERT,name +'\n' ))
    print(mainText.insert(INSERT,'Age            ' +'\t\t\t' ))
    print(mainText.insert(INSERT,age +'\n' ))
    print(mainText.insert(INSERT,'Area           ' +'\t\t\t' ))
    print(mainText.insert(INSERT,area +'\n' ))
    print(mainText.insert(INSERT,'Income         ' +'\t\t\t' ))
    print(mainText.insert(INSERT,income +'\n' ))
    print(mainText.insert(INSERT,'Name of Doctor ' +'\t\t\t' ))
    print(mainText.insert(INSERT,ndoc +'\n' ))
    print(mainText.insert(INSERT,'Doctor Code    ' +'\t\t\t' ))
    print(mainText.insert(INSERT,dcod +'\n' ))
    print(mainText.insert(INSERT,'Last Visit     ' +'\t\t\t' ))
    print(mainText.insert(INSERT,lvisit +'\n' ))
    print(mainText.insert(INSERT,'Ailment        ' +'\t\t\t' ))
    print(mainText.insert(INSERT,lail +'\t\t\n' ))
    print(mainText.insert(INSERT,'Prescription   ' +'\t\t\t' ))
    print(mainText.insert(INSERT,pres ))
    print(mainText.insert(INSERT,pres1 ))
    print(mainText.insert(INSERT,pres2+'\n'))
    print(mainText.insert(INSERT,'Mediclaim  Fund' +'\t\t\t' ))
    print(mainText.insert(INSERT,medf +'\n' ))
    mainText.pack()
    mainText.place(bordermode=OUTSIDE, relx=0.56, rely=0.1)
    label_2 =Label(win,text="  BACKEND DATABASE  ",width = 40,height = 2,  bg='yellow', fg='red')
    label_2.pack()
    label_2.place(bordermode=OUTSIDE,relx=0.64, rely=0.1)
    e.delete(1.0,END)
    e.insert(INSERT,'1. APPOINTMENT\n2. MEDICINE\n3. MEDICLAIM\n4. EXIT\n\n_____________________________\n')

def pAppoBackend(doc, aval1,time1,aval2,time2,aval3,time3):
    text2 = Text(win,width = 60,height = 36,bg = 'black',fg = 'white' )
    print(text2.insert(INSERT,'\n\n\n' ))
    print(text2.insert(INSERT,'Doctor' +'\t\t' ))
    print(text2.insert(INSERT,'Availability ' +'\t' ))
    print(text2.insert(INSERT,'Time ' +'\n' ))
    print(text2.insert(INSERT,'____________' +'\t\t' ))
    print(text2.insert(INSERT,'____________' +'\t' ))
    print(text2.insert(INSERT,'____________' +'\n' ))
    print(text2.insert(INSERT,doc +'\t\t' ))
    print(text2.insert(INSERT,aval1+'\t\t' ))
    print(text2.insert(INSERT,time1 +'\n\t\t' ))
    print(text2.insert(INSERT,aval2+'\t\t' ))
    print(text2.insert(INSERT,time2 +'\n\t\t' ))
    print(text2.insert(INSERT,aval3+'\t\t' ))
    print(text2.insert(INSERT,time3 +'\n' ))
    text2.pack()
    text2.place(bordermode=OUTSIDE, relx=0.56, rely=0.1)
    label_2 =Label(win,text="  BACKEND DATABASE  ",width = 40,height = 2,  bg='yellow', fg='red')
    label_2.pack()
    label_2.place(bordermode=OUTSIDE,relx=0.64, rely=0.1)

def reschedule(area1,hos1,hos2,num1,num2):    
    text4 = Text(win,width = 60,height = 36,bg = 'black',fg='white')
    print(text4.insert(INSERT,'\n\n\n' ))
    print(text4.insert(INSERT,'Area     :   ' +'\t\t\t\t' ))
    print(text4.insert(INSERT,area1 +'\n' ))
    print(text4.insert(INSERT,'Hoispital avalable' +'\t\t\t\t' ))
    print(text4.insert(INSERT,'Phone             ' +'\n' ))
    print(text4.insert(INSERT,hos1 +'\t\t\t\t' ))
    print(text4.insert(INSERT,num1 +'\n' ))
    print(text4.insert(INSERT,hos2 +'\t\t\t\t' ))
    print(text4.insert(INSERT,num2 +'\n' ))
    text4.pack()
    text4.place(bordermode=OUTSIDE, relx=0.56, rely=0.1)
    label_2 =Label(win,text="  BACKEND DATABASE  ",width = 40,height = 2,  bg='yellow', fg='red')
    label_2.pack()
    label_2.place(bordermode=OUTSIDE,relx=0.64, rely=0.1)        

def mediBackend(income,insti1,insti2,cld1,approv1,ded1,cld2,approv2,ded2):
    new1Text = Text(win , width = 60, height = 36,bg = 'black',fg='white')
    print(new1Text.insert(INSERT,'\n\n\n' ))
    print(new1Text.insert(INSERT,'Income        ' +'\t' ))
    print(new1Text.insert(INSERT,income +'\n\n' ))
    print(new1Text.insert(INSERT,'INSTITUTION:' +'\t\t'))
    print(new1Text.insert(INSERT,insti1 +'\n' ))
    print(new1Text.insert(INSERT,'Claimed:' +'\t\t' ))
    print(new1Text.insert(INSERT,cld1+'\n' ))
    print(new1Text.insert(INSERT,'Approved:' +'\t\t' ))
    print(new1Text.insert(INSERT,approv1 +'\n' ))
    print(new1Text.insert(INSERT,'Deduction' +'\t\t' ))
    print(new1Text.insert(INSERT,ded1 +'\n' ))
    print(new1Text.insert(INSERT,'INSTITUTION:' +'\t\t'))
    print(new1Text.insert(INSERT,insti2 +'\n' ))
    print(new1Text.insert(INSERT,'Claimed:' +'\t\t' ))
    print(new1Text.insert(INSERT,cld2+'\n' ))
    print(new1Text.insert(INSERT,'Approved:' +'\t\t' ))
    print(new1Text.insert(INSERT,approv2 +'\n' ))
    print(new1Text.insert(INSERT,'Deduction' +'\t\t' ))
    print(new1Text.insert(INSERT,ded2 +'\t\t' ))  
    new1Text.pack()
    new1Text.place(bordermode=OUTSIDE, relx=0.56, rely=0.1)
    label_2 =Label(win,text="  BACKEND DATABASE  ",width = 40,height = 2,  bg='yellow', fg='red')
    label_2.pack()
    label_2.place(bordermode=OUTSIDE,relx=0.64, rely=0.1)

def newMed(area,clin1,num1,clin2,num2,clin3,num3):
    newText = Text(win , width = 60, height = 36,bg = 'black',fg='white')
    print(newText.insert(INSERT,'\n\n\n' ))
    print(newText.insert(INSERT,'Area         ' +'\t\t' ))
    print(newText.insert(INSERT,'CLINICS      ' +'\t\t'))
    print(newText.insert(INSERT,'PHONE Numbers' +'\n' ))
    print(newText.insert(INSERT,'___________________________________________\n\n' ))
    print(newText.insert(INSERT,area +'\t\t' ))
    print(newText.insert(INSERT,clin1 +'\t\t' ))
    print(newText.insert(INSERT,num1 +'\n' ))
    print(newText.insert(INSERT,area +'\t\t' ))
    print(newText.insert(INSERT,clin2 +'\t\t' ))
    print(newText.insert(INSERT,num2 +'\n' ))
    print(newText.insert(INSERT,area +'\t\t' ))
    print(newText.insert(INSERT,clin3 +'\t\t' ))
    print(newText.insert(INSERT,num3 +'\n' ))  
    newText.pack()
    newText.place(bordermode=OUTSIDE, relx=0.56, rely=0.1)
    label_2 =Label(win,text="  BACKEND DATABASE  ",width = 40,height = 2,  bg='yellow', fg='red')
    label_2.pack()
    label_2.place(bordermode=OUTSIDE,relx=0.64, rely=0.1)
           
def presbBackend(med1,avalb1,med2,avalb2,avalb3,med3):
    medicineText = Text(win,bg= 'black',height = 36,width = 60,fg = 'white')
    print( medicineText.insert(INSERT,'\n\n\n' ))
    print( medicineText.insert(INSERT,'medicine Priscribed' +'\t\t' ))
    print( medicineText.insert(INSERT,'Availability  ' +'\n' ))
    print( medicineText.insert(INSERT,med1 +'\t\t\t' ))
    print( medicineText.insert(INSERT,avalb1+'\n' ))
    print( medicineText.insert(INSERT,med2 +'\t\t\t' ))
    print( medicineText.insert(INSERT,avalb2 +'\n' ))
    medicineText.pack()
    medicineText.place(bordermode=OUTSIDE, relx=0.56, rely=0.1)
    label_2 =Label(win,text="  BACKEND DATABASE  ",width = 40,height = 2,  bg='yellow', fg='red')
    label_2.pack()
    label_2.place(bordermode=OUTSIDE,relx=0.64, rely=0.1)        

        
def set_text(text):
    global text1
    e.insert(END,text)
    text1= e.get(1.0 ,END)   
    
def delete():
    e.delete("%s-1c" % INSERT, INSERT)

def lab():
    label_3 =Label(win,text="                                                              ",  fg='black')
    label_3.pack()
    label_3.place(bordermode=OUTSIDE,relx=0.2, rely=0.18) 
    label_3.pack_forget()

def submit():
    text2 = e.get(1.0,END)
    lab()
    
    global a
    a = int(text2)
    if a == phone_no[0]:
            database1()
    if a == phone_no[1]:
            database2()
    if a == phone_no[2]:
            database3()
    if a == phone_no[3]:
            database4()
    if a == phone_no[4]:
            database5()
    if a == phone_no[5]:
            database6()
    if a == phone_no[6]:
            database7()
    if a == phone_no[7]:
            database8()
    if a == phone_no[8]:
            database9()
    if a == phone_no[9]:
            database10()
    else:
        print "no database found "
    
def select():
    init = int(e.get(7.0,END))
    if init ==1:
        appointment()
    if init ==2:
        medicine()
    if init ==3:
        mediclaim()
    if init == 4:
        exit1()

def database1():
    backEnd('Gopi Patel','21','Time Square','40000','Sejal Bhatt','DOC1','17/3/2017','cold','M01,\t','M02,\t','M03\t','10000')
def database2():
    backEnd('Rahul Gunkar','25','Kamroli','35000','Sagar Vejani','DOC5','28/2/2017','Fever','M02\t','M03\t','M04\t','10000')
def database3():
    backEnd('Ami Mehta','19','Sardarnagar','5000','Aditya Pandya','DOC10','10/3/2017','Cough','M01\t','M02\t','M05\t','2000')
def database4():
    backEnd('Amoli Shah','55','NavrangPura','30000','Kinjal Solanki','DOC6','11/3/2017','Kolera','M03\t','M04\t','M06\t','5000')
def database5():
    backEnd('Nikith Sai','45','M G road','100000','Kavya Bhatt','DOC9','15/3/2017','Stroke','M07\t','M08\t','M09\t','20000')
def database6():
    backEnd('Sagar Malik','32','S G highway','450000','Sanjay Sharma','DOC2','10/2/2017','cold','M01\t','M02\t','M03\t','30000')
def database7():
    backEnd('Pinak Shah','20','Athwa gate','50500','Dinesh Joshi','DOC4','15/1/2017','Fever','M02\t','M03\t','M04\t','5000')
def database8():
    backEnd('Kiran Patel','15','Chinkpokhli','30000','Nirali Mehta','DOC3','22/1/2017','Pneumonia','M08\t','M09\t','M010\t','7000')
def database9():
    backEnd('Aneri Shah','32','Railway station','20000','Divya Singhal','DOC7','1/1/2017','Dengue','M010\t','M011\t','M012\t','3000')
def database10():
    backEnd('Paras Sharma','60','Khavdhari Gali','200000','Ashutosh Vishwa','DOC8','17/2/2017','Cold','M02\t','M01\t','M02\t','10000')    
def mainMenu():
    e.delete(1.0,END)
    if a == phone_no[0]:
            database1()
    if a == phone_no[1]:
            database2()
    if a == phone_no[2]:
            database3()
    if a == phone_no[3]:
            database4()
    if a == phone_no[4]:
            database5()
    if a == phone_no[5]:
            database6()
    if a == phone_no[6]:
            database7()
    if a == phone_no[7]:
            database8()
    if a == phone_no[8]:
            database9()
    if a == phone_no[9]:
            database10()
    
    
def appointment():
    def select1():    
        n2=int(e.get(7.0 ,END))
        if n2 == 1:
            newAppo()
        if n2 == 2 :
            prevAppo()
        if n2 == 3:
            mainMenu()
            
    def select2():
        a0=e.index(INSERT)
        a1=int(e.get(7.0 ,END))
        if a1 == 1:
            confirm()
        if a1 == 2 :
            resd()
        if a1 == 3:
            mainMenu()
            
    def selectx():
        c0=e.index(INSERT)
        c1=int(e.get(7.0 ,END))
        if c1 == 1:
            confirm1()
        if c1 == 2 :
            resd1()
        if c1 == 3:
            mainMenu()
            
    def newAppo():
        if a == phone_no[0]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   34345\nHos2:   33445\n'))
            mainText.pack_forget()
            reschedule('Time Square','Hos1','Hos2','34345','33445')   
        if a == phone_no[1]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   12123\nHos2:   112233\n'))
            mainText.pack_forget()
            reschedule('Kamroli','hos1','hos2','12123','112233')
        if a == phone_no[2]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   99887\nHos2:   998887\n'))
            mainText.pack_forget()
            reschedule('Sardarnagar','hos1','hos2','99887','998887')
        if a == phone_no[3]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   55665\nHos2:   556644\n'))
            mainText.pack_forget()
            reschedule('Navrangpura','hos1','hos2','55665','556644')
        if a == phone_no[4]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   665566\nHos2:   66566\n'))
            mainText.pack_forget()
            reschedule('M G road','hos1','hos2','665566','66566')
        if a == phone_no[5]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   36363\nHos2:   336633\n'))
            mainText.pack_forget()
            reschedule('S G highway','hos1','hos2','36363','336633')
        if a == phone_no[6]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   20201\nHos2:   202200\n'))
            mainText.pack_forget()
            reschedule('chinkpokhli','hos1','hos2','20201','202200')
        if a == phone_no[7]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   39393\nHos2:   339399\n'))
            mainText.pack_forget()
            reschedule('Railway station','hos1','hos2','393930','339399')
        if a == phone_no[8]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   990099\nHos2:   90909\n'))
            mainText.pack_forget()
            reschedule('Khavdhari Gali','hos1','hos2','990099','90909')
        if a == phone_no[9]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'\nContact Numbers of Hospitals in    Your Area:\n\nHos1:   34346\nHos2:   334456\n'))
            mainText.pack_forget()
            reschedule('SVNIT','Gajjar','MTV','34346','334456')
            
    def prevAppo():
        s2 = Button(win,text='send',command=lambda:select2())
        s2.pack()
        s2.place(bordermode=OUTSIDE, height=68, width=110,relx=0.27, rely=0.91)
        image = ImageTk.PhotoImage(file="s3.jpg")
        s2.config(image=image)
        s2.image = image
        mainText.pack_forget()
        if a == phone_no[0]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:Sejal Bhatt(DOC1)10-11am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Sejal Bhatt','Available','10-11 am','Booked','11-12 am','Available','4-5 pm')
        if a == phone_no[1]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:Sagar Vejali(DOC10)9-10am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Sagar Vejani','Available','9-10am','Booked','10-11 am','Available','5-6 pm')         
        if a == phone_no[2]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:9-10am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Booked','Nikith sai','Booked','Sejal Bhatt','Available')
        if a == phone_no[3]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:10-11am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Available','Nikith sai','Booked','Sejal Bhatt','Booked')         
        if a == phone_no[4]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:9-10am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Booked','Nikith sai','Booked','Sejal Bhatt','Available')
        if a == phone_no[5]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:10-11am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Available','Nikith sai','Booked','Sejal Bhatt','Booked')         
        if a == phone_no[6]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:9-10am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Booked','Nikith sai','Booked','Sejal Bhatt','Available')
        if a == phone_no[7]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:10-11am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Available','Nikith sai','Booked','Sejal Bhatt','Booked')         
        if a == phone_no[8]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:9-10am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Booked','Nikith sai','Booked','Sejal Bhatt','Available')
        if a == phone_no[9]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:10-11am\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
            pAppoBackend('Ami Mehta','Available','Nikith sai','Booked','Sejal Bhatt','Booked')

    def confirm():
        if a == phone_no[0]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirmed with Dr. Sejal Bhatt at 10am.' ))
        if a == phone_no[1]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[2]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal Bhatt between 9 - 10 am ' ))
        if a == phone_no[3]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[4]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal BHatt between 9 - 10 am ' ))
        if a == phone_no[5]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[6]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal BHatt between 9 - 10 am ' ))
        if a == phone_no[7]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[8]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal BHatt between 9 - 10 am ' ))
        if a == phone_no[9]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))             


    def resd():
        s3 = Button(win,text='send',command=lambda:selectx())
        s3.pack()
        s3.place(bordermode=OUTSIDE, height=68, width=110,relx=0.27, rely=0.91)
        image = ImageTk.PhotoImage(file="s3.jpg")
        s3.config(image=image)
        s3.image = image
        mainText.pack_forget()    
        if a == phone_no[0]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:Sejal Bhatt(DOC1)4 -5 pm\n1. Confirm\n2. Reschuedule\n3. Main Menu\n\n_____________________\n'))
        if a == phone_no[1]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Ami Mehta'))
        if a == phone_no[2]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Amoli Shah'))
        if a == phone_no[3]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Aniket Sharma'))
        if a == phone_no[4]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Payal Mittal'))
        if a == phone_no[5]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Nirali Mehta'))
        if a == phone_no[6]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Yash Patil'))
        if a == phone_no[7]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Sarthak Desai'))
        if a == phone_no[8]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Divya Singhal'))
        if a == phone_no[9]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Upasana Vyas'))
    def confirm1():
        if a == phone_no[0]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirmed with Dr. Sejal Bhatt at 4 pm.' ))
        if a == phone_no[1]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[2]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal Bhatt between 9 - 10 am ' ))
        if a == phone_no[3]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[4]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal BHatt between 9 - 10 am ' ))
        if a == phone_no[5]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[6]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal BHatt between 9 - 10 am ' ))
        if a == phone_no[7]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
        if a == phone_no[8]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Sejal BHatt between 9 - 10 am ' ))
        if a == phone_no[9]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Your appointment has been confirm to doctor Ami Mehta between 10 - 11 am ' ))
    def resd1():
        if a == phone_no[0]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Available:Sejal Bhatt(DOC1)4 - 5 pm'))
        if a == phone_no[1]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Ami Mehta'))
        if a == phone_no[2]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Amoli Shah'))
        if a == phone_no[3]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Aniket Sharma'))
        if a == phone_no[4]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Payal Mittal'))
        if a == phone_no[5]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Nirali Mehta'))
        if a == phone_no[6]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Yash Patil'))
        if a == phone_no[7]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Sarthak Desai'))
        if a == phone_no[8]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Divya Singhal'))
        if a == phone_no[9]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Previous Doctor : Upasana Vyas'))


    e.delete(1.0,END)
    print(e.insert(INSERT,'1. New Appointment\n2. Previous Appointment\n3. Main Menu\n\n\n_________________________\n'))
    s.pack_forget()
    s1 = Button(win,text='send',command=lambda:select1())
    s1.pack()
    s1.place(bordermode=OUTSIDE, height=68, width=110,relx=0.27, rely=0.91)
    image = ImageTk.PhotoImage(file="s3.jpg")
    s1.config(image=image)
    s1.image = image

    
def medicine():
    def presFnt():
        e.delete(1.0,END)
        if a == phone_no[0]:
            print(e.insert(INSERT,'\nCurrently Available Medicines: \nM02\n'))
            presbBackend('M01','N','M02','Y','M03','Y')
        if a == phone_no[1]:
            print(e.insert(INSERT,'\nAvail: MO3\n'))
            presbBackend('MO1','N','MO3','Y')
        if a == phone_no[2]:
            print(e.insert(INSERT,'\nAvail: MO2\n'))
            presbBackend('MO1','N','MO2','Y')
        if a == phone_no[3]:
            print(e.insert(INSERT,'\nAvail: MO3\n'))
            presbBackend('MO1','N','MO3','Y')
        if a == phone_no[4]:
            print(e.insert(INSERT,'\nAvail: MO2\n'))
            presbBackend('MO1','N','MO2','Y')
        if a == phone_no[5]:
            print(e.insert(INSERT,'\nAvail: MO3\n'))
            presbBackend('MO1','N','MO3','Y')
        if a == phone_no[6]:
            print(e.insert(INSERT,'\nAvail: MO2\n'))
            presbBackend('MO1','N','MO2','Y')
        if a == phone_no[7]:
            print(e.insert(INSERT,'\nAvail: MO3\n'))
            presbBackend('MO1','N','MO3','Y')
        if a == phone_no[8]:
            print(e.insert(INSERT,'\nAvail: MO2\n'))
            presbBackend('MO1','N','MO2','Y')
        if a == phone_no[9]:
            print(e.insert(INSERT,'\nAvail: MO3\n'))
            presbBackend('MO1','N','MO3','Y')

    def newMed1():
        if a == phone_no[0]:
            e.delete(1.0,END)
            print(e.insert(INSERT,'Contact Numbers of Pharmacies in   Your Area:\nclinic x: 956524\n','1','clinic y: 956525\n','2','clinic z: 856589\t\n'))
            mainText.pack_forget()
            newMed('surat','clinic x','956524','clinic y','956525','clinic z','856589')
        if a == phone_no[1]:
            print(e.insert(INSERT,'\n956525\n','1','956526\n','2','856598\t\n'))
            newMed('Pune','clinic x1','956525','clinic y1','956526','clinic z1','856598')
        if a == phone_no[2]:
            print(e.insert(INSERT,'\n956524\n','1','956525\n','2','856589\t\n'))
            newMed('surat','clinic x','956525','clinic y','956525','clinic z','856589')
        if a == phone_no[3]:
            print(e.insert(INSERT,'\n956525\n','1','956526\n','2','856598\t\n'))
            newMed('Pune','clinic x1','956525','clinic y1','956526','clinic z1','856598')
        if a == phone_no[4]:
            print(e.insert(INSERT,'\n956524\n','1','956525\n','2','856589\t\n'))
            newMed('surat','clinic x','956525','clinic y','956525','clinic z','856589')
        if a == phone_no[5]:
            print(e.insert(INSERT,"\n'956525','956526',856598'\n"))
            newMed('Pune','clinic x1','956525','clinic y1','956526','clinic z1','856598')
        if a == phone_no[6]:
            print(e.insert(INSERT,"\n'956524','956525',856589'\n"))
            newMed('surat','clinic x','956525','clinic y','956525','clinic z','856589')
        if a == phone_no[7]:
            print(e.insert(INSERT,"\n'956525','956526',856598'\n"))
            newMed('Pune','clinic x1','956525','clinic y1','956526','clinic z1','856598')
        if a == phone_no[8]:
            print(e.insert(INSERT,"\n'956524','956525',856589'\n"))
            newMed('surat','clinic x','956525','clinic y','956525','clinic z','856589')
        if a == phone_no[9]:
            print(e.insert(INSERT,"\n'956525','956526',856598'\n"))
            newMed('Pune','clinic x1','956525','clinic y1','956526','clinic z1','856598')
            
    def select3():
        m1=e.index(INSERT)        
        m2=int(e.get(7.0 ,END))

        if m2 == 1:
            presFnt()
        
        if m2 == 2 :
            newMed1()
                
        if m2 == 3 :
            mainMenu()
            
    e.delete(1.0,END)
    print(e.insert(INSERT,'1.  Prescribed\n2.  New\n3.  Main Menu\n\n\n___________________________\n'))
    s.pack_forget()
    s3 = Button(win,text='send',command=lambda:select3())
    s3.pack()
    s3.place(bordermode=OUTSIDE, height=68, width=110,relx=0.27, rely=0.91)
    image = ImageTk.PhotoImage(file="s3.jpg")
    s3.config(image=image)
    s3.image = image


def mediclaim():
    e.delete(1.0,END)
    if a == phone_no[0]:
        print(e.insert(INSERT,'    LIC\nClaimed : 10000\nApproved : 9000\nDeduction :Excess Medicinal Expense\n    Aviva\nClaimed : 10000\nApproved : Not Apporved\nDeduction : Excess medicinal charge') )
        mediBackend('50000','LIC','Aviva','10000','9000','Excess Medical Expenses','10000','Not Apporved','Excess medicinal charge')
    if a == phone_no[1]:
        print(e.insert(INSERT,'Claimed   : 20000\nApproved  : 2000\nDeduction : Medicinal Expense  ') ) 
    if a == phone_no[2]:
        print(e.insert(INSERT,'Claimed   : 10000\nApproved  : 9000\nDeduction : Medicinal Expense  ') ) 
    if a == phone_no[3]:
        print(e.insert(INSERT,'Claimed   : 20000\nApproved  : 2000\nDeduction : Medicinal Expense  ') )
    if a == phone_no[4]:
        print(e.insert(INSERT,'Claimed   : 10000\nApproved  : 9000\nDeduction : Medicinal Expense  ') ) 
    if a == phone_no[5]:
        print(e.insert(INSERT,'Claimed   : 20000\nApproved  : 2000\nDeduction : Medicinal Expense  ') )
    if a == phone_no[6]:
        print(e.insert(INSERT,'Claimed   : 10000\nApproved  : 9000\nDeduction : Medicinal Expense  ') ) 
    if a == phone_no[7]:
        print(e.insert(INSERT,'Claimed   : 20000\nApproved  : 2000\nDeduction : Medicinal Expense  ') )
    if a == phone_no[8]:
        print(e.insert(INSERT,'Claimed   : 10000\nApproved  : 9000\nDeduction : Medicinal Expense  ') ) 
    if a == phone_no[9]:
        print(e.insert(INSERT,'Claimed   : 20000\nApproved  : 2000\nDeduction : Medicinal Expense  ') )


mainText = Text(win,width = 60, height = 36,bg='black',fg='white')    
print(mainText.insert(INSERT, '\n\n\n' ))
print(mainText.insert(INSERT, 'Patient No.'+'  Name         '+'Phone No  ' +'       Hospital\n' ))
print(mainText.insert(INSERT, '__________________________________________________________\n\n' ))
print(mainText.insert(INSERT, '1       '+'\t'+'Gopi Patel       '+' 9974125569' +'      A Hospital\n' ))
print(mainText.insert(INSERT, '2       '+'\t'+'Rahul Gunkar     '+' 9712761520' +'      B Hospital\n' ))
print(mainText.insert(INSERT, '3       '+'\t'+'Ami Mehta        '+' 9408750905' +'      C Hospital\n' ))
print(mainText.insert(INSERT, '4       '+'\t'+'Amoli Shah       '+' 8487063435' +'      D Hospital\n' ))
print(mainText.insert(INSERT, '5       '+'\t'+'Nikith Sai       '+' 9408009090' +'      E Hospital\n' ))
print(mainText.insert(INSERT, '6       '+'\t'+'Sagar Malik      '+' 9987968345' +'      F Hospital\n' ))
print(mainText.insert(INSERT, '7       '+'\t'+'Pinak Shah       '+' 9497845326' +'      G Hospital\n' ))
print(mainText.insert(INSERT, '8       '+'\t'+'Kiran Patel      '+' 9712345678' +'      H Hospital\n' ))
print(mainText.insert(INSERT, '9       '+'\t'+'Aneri Shah       '+' 9408750999' +'      I Hospital\n' ))
print(mainText.insert(INSERT, '10      '+'\t'+'Paras Sharma     '+' 9498790905' +'      J Hospital\n' ))
mainText.pack()
mainText.place(bordermode=OUTSIDE, relx=0.56, rely=0.1)

e = Text(win,width = 35, height = 7,bg='white',fg='black',font=("Helvetica",11))
e.pack()
e.place(bordermode=INSIDE, relx=0.203, rely=0.22)

l = Text(win,width = 1, height = 50,bg='light blue',fg='white')
l.pack()
l.place(bordermode=OUTSIDE, relx=0.48, rely=0.0)

label_1 =Label(win,text="  FEATURE PHONE  ",width = 40,height = 2,  bg='yellow', fg='red')
label_1.pack()
label_1.place(bordermode=OUTSIDE,relx=0.20, rely=0.1)

label_3 =Label(win,text="  ENTER YOUR PATIENT ID:  ",  fg='black')
label_3.pack()
label_3.place(bordermode=OUTSIDE,relx=0.2, rely=0.18)
label_3.pack_forget()

label_2 =Label(win,text="  BACKEND DATABASE  ",width = 40,height = 2,  bg='yellow', fg='red')
label_2.pack()
label_2.place(bordermode=OUTSIDE,relx=0.64, rely=0.1)

p1 = Button(win,text='1',command=lambda:set_text('1'))
p1.pack()
p1.place(bordermode=OUTSIDE, height=81, width=100,relx=0.20, rely=0.4)
image = ImageTk.PhotoImage(file="p1.png")
p1.config(image=image)
p1.image = image

p2 = Button(win,text='2',command=lambda:set_text('2'))
p2.pack()
p2.place(bordermode=OUTSIDE, height=81, width=100,relx=0.27, rely=0.4)
image = ImageTk.PhotoImage(file="p2.png")
p2.config(image=image)
p2.image = image

p3 = Button(win,text='3',command=lambda:set_text('3'))
p3.pack()
p3.place(bordermode=OUTSIDE, height=81, width=100,relx=0.34, rely=0.4)
image = ImageTk.PhotoImage(file="p3.png")
p3.config(image=image)
p3.image = image

p4 = Button(win,text='4',command=lambda:set_text('4'))
p4.pack()
p4.place(bordermode=OUTSIDE, height=81, width=100,relx=0.20, rely=0.5)
image = ImageTk.PhotoImage(file="p4.png")
p4.config(image=image)
p4.image = image

p5 = Button(win,text='5',command=lambda:set_text('5'))
p5.pack()
p5.place(bordermode=OUTSIDE, height=81, width=100,relx=0.27, rely=0.5)
image = ImageTk.PhotoImage(file="p5.png")
p5.config(image=image)
p5.image = image

p6 = Button(win,text='6',command=lambda:set_text('6'))
p6.pack()
p6.place(bordermode=OUTSIDE, height=81, width=100,relx=0.34, rely=0.5)
image = ImageTk.PhotoImage(file="p6.png")
p6.config(image=image)
p6.image = image

p7 = Button(win,text='7',command=lambda:set_text('7'))
p7.pack()
p7.place(bordermode=OUTSIDE, height=81, width=100,relx=0.20, rely=0.6)
image = ImageTk.PhotoImage(file="p7.png")
p7.config(image=image)
p7.image = image

p8 = Button(win,text='8',command=lambda:set_text('8'))
p8.pack()
p8.place(bordermode=OUTSIDE, height=81, width=100,relx=0.27, rely=0.6)
image = ImageTk.PhotoImage(file="p8.png")
p8.config(image=image)
p8.image = image

p9 = Button(win,text='9',command=lambda:set_text('9'))
p9.pack()
p9.place(bordermode=OUTSIDE, height=81, width=100,relx=0.34, rely=0.6)
image = ImageTk.PhotoImage(file="p9.png")
p9.config(image=image)
p9.image = image

p0 = Button(win,text='0',command=lambda:set_text('0'))
p0.pack()
p0.place(bordermode=OUTSIDE, height=81, width=100,relx=0.27, rely=0.71)
image = ImageTk.PhotoImage(file="p0.png")
p0.config(image=image)
p0.image = image

p11 = Button(win,text='*',command=lambda:set_text('*'))
p11.pack()
p11.place(bordermode=OUTSIDE, height=81, width=100,relx=0.20, rely=0.71)
image = ImageTk.PhotoImage(file="p11.png")
p11.config(image=image)
p11.image = image

p12 = Button(win,text='#',command=lambda:set_text('#'))
p12.pack()
p12.place(bordermode=OUTSIDE, height=81, width=100,relx=0.34, rely=0.71)
image = ImageTk.PhotoImage(file="p12.png")
p12.config(image=image)
p12.image = image

pb = Button(win,text='x',command=lambda:delete())
pb.pack()
pb.place(bordermode=OUTSIDE, height=81, width=100,relx=0.27, rely=0.8)
image = ImageTk.PhotoImage(file="pb.png")
pb.config(image=image)
pb.image = image

call = Button(win,command =submit)
call.pack()
call.place(bordermode=OUTSIDE, height=81, width=100,relx=0.20, rely=0.8)
image = ImageTk.PhotoImage(file="c1.png")
call.config(image=image)
call.image = image

cut = Button(win,command = exit1)
cut.pack()
cut.place(bordermode=OUTSIDE, height=81, width=100,relx=0.34, rely=0.80)
image = ImageTk.PhotoImage(file="cut2.png")
cut.config(image=image)
cut.image = image

s = Button(win,text='send',command=lambda:select())
s.pack()
s.place(bordermode=OUTSIDE, height=68, width=110,relx=0.27, rely=0.91)
image = ImageTk.PhotoImage(file="s3.jpg")
s.config(image=image)
s.image = image

win.mainloop()
