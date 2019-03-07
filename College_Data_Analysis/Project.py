from tkinter import *
from tkinter import messagebox
import os
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas
import statistics




class MyInterface:

    LABEL_TEXT = ['This is the Interface package.',
                  'This is the main class for GUI,']

    def __init__(self, master):
        self.master = master
        master.title('Student Validator')
        master.attributes('-fullscreen', True)

        # master.geometry()

        # Declaration of Variables used in  Entry Widget

        self.Roll_No = StringVar()
        self.First_Name = StringVar()
        self.Last_Name = StringVar()
        self.Phone_Number = StringVar()
        self.Department = StringVar()
        self.Email_Id = StringVar()
        self.Python_Marks = StringVar()
        self.DS_Marks = StringVar()
        self.ADBMS_Marks = StringVar()
        self.Total_Marks = StringVar()
        self.Search_Roll_No = StringVar()
        #self.Search_Roll_No.set('1610991105')
        self.Drop_Down = StringVar()
        self.body()

    def body(self):

        # Label
        top_bar = Frame(bg = "#465454", width="1366", height="56").place(x=0, y=0)
        top_lab = Label(self.master, text='Student Information Statistics', anchor=W, font=100,
                     width=24).place(x=600, y=15)

        #f1 = Frame(bg = "#ffffff", width=50, height=100).place(x=100, y=100)

        bor1 = Frame(bg = "#465454", width="3", height="700").place(x=580, y=56)

        bottom_bar = Frame(bg = "#465454", width="1366", height="20").place(x=0, y=747)

        lab1 = Label(self.master, text='Roll No', anchor=W, font=55,
                     width=15).place(x=60, y=100)
        lab2 = Label(self.master, text='First Name', anchor=W, font=55,
                     width=15).place(x=60, y=140)
        lab3 = Label(self.master, text='Last Name', anchor=W, font=55,
                     width=15).place(x=60, y=180)
        lab4 = Label(self.master, text='Phone Number', anchor=W,
                     font=55, width=12).place(x=60, y=220)
        lab5 = Label(self.master, text='Department', anchor=W, font=55,
                     width=15).place(x=60, y=260)
        lab6 = Label(self.master, text='Email Id', anchor=W, font=55,
                     width=15).place(x=60, y=300)
        lab7 = Label(self.master, text='Python Marks', anchor=W,
                     font=55, width=15).place(x=60, y=340)
        lab8 = Label(self.master, text='DS Marks', anchor=W, font=55,
                     width=15).place(x=60, y=380)
        lab9 = Label(self.master, text='ADBMS Marks', anchor=W,
                     font=55, width=15).place(x=60, y=420)

        search_lab = Label(self.master, text='Search :', anchor=W,
                     font=55, width=15).place(x=60, y=580)
        
        python_lab = Label(self.master, text='Python', anchor=W,
                     font=70, width=15).place(x=850, y=100)
        python_lab = Label(self.master, text='DS', anchor=W,
                     font=70, width=15).place(x=950, y=100)
        python_lab = Label(self.master, text='ADBMS', anchor=W,
                     font=70, width=15).place(x=1050, y=100)

        # Entry

        ent1 = Entry(self.master, textvariable=self.Roll_No,
                     width=30).place(x=250, y=100)
        ent2 = Entry(self.master, textvariable=self.First_Name,
                     width=30).place(x=250, y=140)
        ent3 = Entry(self.master, textvariable=self.Last_Name,
                     width=30).place(x=250, y=180)
        ent4 = Entry(self.master, textvariable=self.Phone_Number,
                     width=30).place(x=250, y=220)
        ent5 = Entry(self.master, textvariable=self.Department,
                     width=30).place(x=250, y=260)
        ent6 = Entry(self.master, textvariable=self.Email_Id,
                     width=30).place(x=250, y=300)
        ent7 = Entry(self.master, textvariable=self.Python_Marks,
                     width=30).place(x=250, y=340)
        ent8 = Entry(self.master, textvariable=self.DS_Marks,
                     width=30).place(x=250, y=380)
        ent9 = Entry(self.master, textvariable=self.ADBMS_Marks,
                     width=30).place(x=250, y=420)

        search_ent = Entry(self.master, textvariable=self.Search_Roll_No,
                     width=62).place(x = 60, y=625)

        choices = { 'Python_Marks','DS_Marks','ADBMS_Marks'}
        self.Drop_Down.set('Python_Marks') # set the default option
        popupMenu = OptionMenu(self.master, self.Drop_Down, *choices).place(x = 700 ,y = 630)


        # Button

        exit_button = Button(self.master, text='Exit', width=15, height=3)
        exit_button.place(x =1250 ,y = 0)
        exit_button.bind('<Button-1>', self.closeGUI)



        reset_button = Button(self.master, text='Reset', width=15, height=3)
        reset_button.place(x = 80 ,y = 480)
        reset_button.bind('<Button-1>', self.resetEntry)

        save_button = Button(self.master, text='Save', width=15, height=3)
        save_button.place(x = 280 ,y = 480)
        save_button.bind('<ButtonRelease-1>', self.saveEntry)

        search_button = Button(self.master, text='Search', width=15, height=3)
        search_button.place(x = 180 ,y = 670)
        search_button.bind('<ButtonRelease-1>', self.search)



        total_button = Button(self.master, text='Total', width=15, height=3)
        total_button.place(x = 650, y = 150)
        total_button.bind('<Button-1>', self.total)

        average_button = Button(self.master, text='Average', width=15, height=3)
        average_button.place(x = 650, y = 220)
        average_button.bind('<Button-1>', self.average)

        max_button = Button(self.master, text='Max', width=15, height=3)
        max_button.place(x = 650, y = 290)
        max_button.bind('<Button-1>', self.maximum)

        min_button = Button(self.master, text='Min', width=15, height=3)
        min_button.place(x = 650, y = 360)
        min_button.bind('<Button-1>', self.minimum)

        median_button = Button(self.master, text='Median', width=15, height=3)
        median_button.place(x = 650, y = 360+70)
        median_button.bind('<Button-1>', self.median)

        mode_button = Button(self.master, text='Mode', width=15, height=3)
        mode_button.place(x = 650, y = 360+140)
        mode_button.bind('<Button-1>', self.mode)

        stat_button = Button(self.master,text="Statistics", width=40, height=4)
        stat_button.place(x = 850, y  = 630)
        stat_button.bind("<Button-1>", self.stat)


    def closeGUI(self, event):
        self.master.destroy()

    def authenticateEntry(self, event):
        if self.Roll_No.get() == '' or self.First_Name.get() == '' \
            or self.Last_Name.get() == '' or self.Phone_Number.get() \
            == '' or self.Department.get() == '' \
            or self.Email_Id.get() == '' or self.Python_Marks.get() \
            == '' or self.DS_Marks.get() == '' \
            or self.ADBMS_Marks.get() == '':
            messagebox.showerror('Error!','You can not leave any field empty!')
            return 0
        else:
            print('auth')
            return 1

    def search(self, event):
        if(self.Search_Roll_No.get() == ''):
            messagebox.showerror('Error!','Please Enter Roll No')
        else:
            df = pandas.DataFrame(pandas.read_csv('demo.csv'))
            abc = 'Roll_No ==' + self.Search_Roll_No.get()
            file = df.query(abc)
            if(file.empty):
                messagebox.showerror('Error!','Entry not found! Please Enter again')
            else:
                root1 = Tk()
                root1.title =('Search Record')
                root1.geometry("1200x700")
            
                lab01 = Label(root1, text='Roll No', anchor=W, font=55,
                         width=15).place(x=60, y=100)
                lab02 = Label(root1, text='First Name', anchor=W, font=55,
                         width=15).place(x=60, y=140)
                lab03 = Label(root1, text='Last Name', anchor=W, font=55,
                         width=15).place(x=60, y=180)
                lab04 = Label(root1, text='Phone Number', anchor=W,
                         font=55, width=12).place(x=60, y=220)
                lab05 = Label(root1, text='Department', anchor=W, font=55,
                         width=15).place(x=60, y=260)
                lab06 = Label(root1, text='Email Id', anchor=W, font=55,
                         width=15).place(x=60, y=300)
                lab07 = Label(root1, text='Python Marks', anchor=W,
                         font=55, width=15).place(x=60, y=340)
                lab08 = Label(root1, text='DS Marks', anchor=W, font=55,
                         width=15).place(x=60, y=380)
                lab09 = Label(root1, text='ADBMS Marks', anchor=W,
                         font=55, width=15).place(x=60, y=420)
                lab010 = Label(root1, text='Percentage', anchor=W,
                         font=55, width=15).place(x=60, y=460)
            
                file1 = list(file.values.flatten())
                temp = sum(file1[6:])/3
                percent = str(round(temp, 2)) + ' %'

                lab11 = Label(root1, text=int(file1[0]), anchor=W, font=55,
                     width=15).place(x=250, y=100)
                lab12 = Label(root1, text=file1[1], anchor=W, font=55,
                     width=15).place(x=250, y=140)
                lab13 = Label(root1, text=file1[2], anchor=W, font=55,
                     width=15).place(x=250, y=180)
                lab14 = Label(root1, text=int(file1[3]), anchor=W,
                     font=55, width=12).place(x=250, y=220)
                lab15 = Label(root1, text=file1[4], anchor=W, font=55,
                        width=15).place(x=250, y=260)
                lab16 = Label(root1, text=file1[5], anchor=W, font=55,
                     width=25).place(x=250, y=300)
                lab17 = Label(root1, text=file1[6], anchor=W,
                     font=55, width=15).place(x=250, y=340)
                lab18 = Label(root1, text=file1[7], anchor=W, font=55,
                     width=15).place(x=250, y=380)
                lab19 = Label(root1, text=file1[8], anchor=W,
                     font=55, width=15).place(x=250, y=420)
                lab010 = Label(root1, text=percent, anchor=W,
                     font=55, width=15).place(x=250, y=460)

                col_count = 3
                bar_width = .2
                
                max1 = self.stat_values('max')
                mark = file1[6:]
                avg1 = self.stat_values('average')
                
                index=np.arange(col_count)
                
                f = Figure(figsize=(6, 5), dpi=100)
                a = f.add_subplot(111)
                m1=a.bar(index,max1,bar_width,alpha=.4,label="Max")
                m2=a.bar(index+0.2,mark,bar_width,alpha=.4,label="Marks")
                m3=a.bar(index+0.4,avg1,bar_width,alpha=.4,label="Average")

                
                def CreateLabels(data):
                    for i in data:
                        height=i.get_height()
                        a.text(i.get_x() + i.get_width() / 2., height*1.05, '%d' % int(height), ha='center',va='bottom')
                        
                CreateLabels(m1)
                CreateLabels(m2)
                CreateLabels(m3)
                a.set_xticks(index + .3/2)
                a.set_xticklabels(('Python','DS','ADBMS'))
                a.legend()
                a.grid(True)
                canvas = FigureCanvasTkAgg(f, master=root1)
                canvas.get_tk_widget().place(x =500 ,y = 100)
                root1.mainloop()

    def checkForDuplicate(self, event):
        row = StringVar()
        file = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                columns=['Roll_No'])
        roll = list(file.values.T.flatten())
        for row in roll:
            if row == int(self.Roll_No.get()):
                messagebox.showerror('Error!','Redundancy   Found!')
                return 0

        print ('No')
        return 1

    def resetEntry(self):
        self.Roll_No.set('')
        self.First_Name.set('')
        self.Last_Name.set('')
        self.Phone_Number.set('')
        self.Department.set('')
        self.Email_Id.set('')
        self.Python_Marks.set('')
        self.DS_Marks.set('')
        self.ADBMS_Marks.set('')
        #self.Total_Marks.set('')

    def saveEntry(self, event):
        if self.authenticateEntry(event) == 1 \
            and self.checkForDuplicate(event) == 1:

            msg = messagebox.askyesno('Check',
                    'Do you want to save?')
            print (msg)

            data = [[
                self.Roll_No.get(),
                self.First_Name.get(),
                self.Last_Name.get(),
                self.Phone_Number.get(),
                self.Department.get(),
                self.Email_Id.get(),
                self.Python_Marks.get(),
                self.DS_Marks.get(),
                self.ADBMS_Marks.get(),
                ]]

            df = pandas.DataFrame(data, columns=[
                'Roll_No',
                'First_Name',
                'Last_Name',
                'Phone_Number',
                'Department',
                'Email_Id',
                'Python_Marks',
                'DS_Marks',
                'ADBMS_Marks',
                ])

            df.to_csv('demo.csv', mode='a', index=False, header=False)
            self.resetEntry()
        else:
            print ('No')

    

    

    def pie_graph(self, file, text):
        count1 = count2 = 0
        pass1 = fail1 = 0
        for i in file:
            if i >= 33:
                pass1 += 1
            else:
                fail1 += 1
        per1 = int(pass1 * 100 / (pass1 + fail1))
        per2 = int(fail1 * 100 / (pass1 + fail1))
        
        labels = 'Pass','Fail'
        sizes = [per1,per2]
        seperated = [.1,.1]
        f = Figure(figsize=(3, 3), dpi=100)
        a = f.add_subplot(111)
        a.set_title(text)
        a.pie(sizes,labels=labels,explode=seperated)
        return f

    def line_graph(self, file1,file2,file3):
        x=[10,20,30,40,50,60,70,80,90,100]
        u1 = pandas.unique(file1)
        u2 = pandas.unique(file2)
        u3 = pandas.unique(file3)
        s1 = pandas.Series(u1)
        s2 = pandas.Series(u2)
        s3 = pandas.Series(u3)
        top1 = s1.nlargest(10).values.flatten()
        top2 = s2.nlargest(10).values.flatten()
        top3 = s3.nlargest(10).values.flatten()
        bot1 = s1.nsmallest(10).values.flatten()
        bot2 = s2.nsmallest(10).values.flatten()
        bot3 = s3.nsmallest(10).values.flatten()
        f = Figure(figsize=(6, 4), dpi=100)
        a = f.add_subplot(111)
        a.plot(x,top1)
        a.plot(x,top2)
        a.plot(x,top3)
        a.plot(x,bot1)
        a.plot(x,bot2)
        a.plot(x,bot3)
        a.grid(True)
        a.set_title('Line Graph')
        return f
    
    def scat_plot(self):
        df = pandas.DataFrame(pandas.read_csv("demo.csv"), columns = ['Roll_No','Python_Marks','DS_Marks','ADBMS_Marks'])
        df['total']=df['Python_Marks']+df['DS_Marks']+df['ADBMS_Marks']
        
        f = Figure(figsize=(4, 3), dpi=100)
        a = f.add_subplot(111)
        a.set_title('Scatter Plot')
        a.scatter(df['Roll_No'],df['total'],alpha=0.5)
        return f
            
    def bar_mmm(self):
        col_count = 3
        bar_width = .2
        mean = self.stat_values('average')
        median = self.stat_values('median')
        mode = self.stat_values('mode')
                
        index = np.arange(col_count)
                
        f = Figure(figsize=(6, 4), dpi=100)
        a = f.add_subplot(111)
        m1 = a.bar(index, mean, bar_width, alpha=.4, label="Mean")
        m2 = a.bar(index + 0.2, median,bar_width, alpha=.4, label="Mode")
        m3 = a.bar(index + 0.4, mode,bar_width, alpha=.4, label="Median")
    
        def CreateLabels(data):
            for i in data:
                height=i.get_height()
                a.text(i.get_x() + i.get_width() / 2., height*1.05, '%d' % int(height), ha='center',va='bottom')
 
        CreateLabels(m1)
        CreateLabels(m2)
        CreateLabels(m3)
        a.set_xticks(index + .3/2)
        a.set_xticklabels(('Python','DS','ADBMS'))
        a.legend()
        a.grid(True)
        return f

    def graph_plot(self, f1, f2, f3, f4, f5, f6):
        graph = Tk()
        graph.geometry('1300x800')
        graph.configure(background='#ffffff')
        canvas = FigureCanvasTkAgg(f1, master=graph)
        canvas.get_tk_widget().place(x = 20, y = 20 )
        canvas = FigureCanvasTkAgg(f2, master=graph)
        canvas.get_tk_widget().place(x = 300, y = 20)
        canvas = FigureCanvasTkAgg(f3, master=graph)
        canvas.get_tk_widget().place(x = 580, y = 20)
        canvas = FigureCanvasTkAgg(f4, master=graph)
        canvas.get_tk_widget().place(x = 580+280, y = 20)
        canvas = FigureCanvasTkAgg(f5, master=graph)
        canvas.get_tk_widget().place(x = 20, y = 300)
        canvas = FigureCanvasTkAgg(f6, master=graph)
        canvas.get_tk_widget().place(x = 620, y = 315)
        graph.mainloop()
        

    def stat(self, event):
        file1 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['Python_Marks']).values.T.flatten()
        file2 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['DS_Marks']).values.T.flatten()
        file3 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['ADBMS_Marks']).values.T.flatten()

        f1 = self.pie_graph(file1, 'Python Pass-Fail %')
        f2 = self.pie_graph(file2, 'DS Pass-Fail %')
        f3 = self.pie_graph(file3, 'ADBMS Pass-Fail %')
        f4 = self.scat_plot()
        f5 = self.line_graph(file1, file2, file3)
        f6 = self.bar_mmm()


        self.graph_plot(f1, f2, f3, f4, f5, f6)
            

    def stat_values(self, jaggu):
        file1 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['Python_Marks'])  # .values.T.flatten()
        file2 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['DS_Marks'])  # .values.T.flatten()
        file3 = pandas.DataFrame(pandas.read_csv('demo.csv'),
                                 columns=['ADBMS_Marks'])  # .values.T.flatten()

        list1 = file1.values.T.flatten()
        list2 = file1.values.T.flatten()
        list3 = file1.values.T.flatten()

        if(jaggu == 'max'):
            max1 = file1.values.max()
            max2 = file2.values.max()
            max3 = file3.values.max()
            return [max1, max2, max3]
        
        elif(jaggu == 'min'):
            min1 = file1.values.min()
            min2 = file2.values.min()
            min3 = file3.values.min()
            return [min1, min2, min3]
        
        elif(jaggu == 'median'):
            median1 = statistics.median(list1)
            median2 = statistics.median(list1)
            median3 = statistics.median(list1)
            return [median1, median2, median3]
        
        elif(jaggu == 'mode'):
            mode1 = statistics.median(list1)
            mode2 = statistics.median(list1)
            mode3 = statistics.median(list1)
            return [mode1, mode2, mode3]
        
        elif(jaggu == 'total'):
            sum1 = file1.values.sum()
            sum2 = file2.values.sum()
            sum3 = file3.values.sum()
            return [sum1, sum2, sum3]
        
        elif(jaggu == 'average'):
            mean1 = round(file1.values.mean(), 2)
            mean2 = round(file2.values.mean(), 2)
            mean3 = round(file3.values.mean(), 2)
            return [mean1, mean2, mean3]
        
        else:
            print('No Function Found')
            

    def total(self, event):
        sum1 = self.stat_values('total')

        pyt_tot = Label(self.master, text=sum1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=150)
        ds_avg = Label(self.master, text=sum1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=150)
        adbms_max = Label(self.master, text=sum1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=150)

    def average(self, event):
        mean1 = self.stat_values('average')

        pyt_tot = Label(self.master, text=mean1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=220)
        ds_avg = Label(self.master, text=mean1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=220)
        adbms_max = Label(self.master, text=mean1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=220)


    def maximum(self, event):
        max1 = self.stat_values('max') 
        pyt_tot = Label(self.master, text=max1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=290)
        ds_avg = Label(self.master, text=max1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=290)
        adbms_max = Label(self.master, text=max1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=290)


    def minimum(self, event):
        min1 = self.stat_values('min') 

        pyt_tot = Label(self.master, text=min1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=360)
        ds_avg = Label(self.master, text=min1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=360)
        adbms_max = Label(self.master, text=min1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=360)

    def median(self, event):
        median1 = self.stat_values('median')

        pyt_tot = Label(self.master, text=median1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=360+70)
        ds_avg = Label(self.master, text=median1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=360+70)
        adbms_max = Label(self.master, text=median1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=360+70)

    def mode(self, event):
        mode1 = self.stat_values('mode')
 

        pyt_tot = Label(self.master, text=mode1[0], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=850, y=360+140)
        ds_avg = Label(self.master, text=mode1[1], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=950, y=360+140)
        adbms_max = Label(self.master, text=mode1[2], bg="#ffffff",
                     font=55, width=10, height = 2).place(x=1050, y=360+140)


root = Tk()
obj = MyInterface(root)
root.mainloop()
