from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
     
        

        #=============================Variable========================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()


        lbltitle = Label(self.root, text="Library Management System", bg="pink", fg="red", bd=20, relief=RIDGE, font=("Times New Roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="pink")
        frame.place(x=0,y=130,width=1530,height=400)


        #======================DataFrameLeft==============================================
        DataFrameLeft= LabelFrame(frame,text="Library membership information",bg="pink",fg="green",bd=12,relief=RIDGE,font=("times of roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=910,height=350)


        lblMember=Label(DataFrameLeft,text="Member Type",bg="pink",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin staff","student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="pink",text="Prn.No",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.prn_var,width=27)
        txtPRN_NO.grid(row=1,column=1)

        lblID_No=Label(DataFrameLeft,bg="pink",text="Id No",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblID_No.grid(row=2,column=0,sticky=W)
        txtID_NO=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.id_var,width=27)
        txtID_NO.grid(row=2,column=1)

        lblFirst_name=Label(DataFrameLeft,bg="pink",text="First Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblFirst_name.grid(row=3,column=0,sticky=W)
        txtfirst_name=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.firstname_var,width=27)
        txtfirst_name.grid(row=3,column=1)

        lblLast_name=Label(DataFrameLeft,bg="pink",text="Last Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLast_name.grid(row=4,column=0,sticky=W)
        txtLast_name=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.lastname_var,width=27)
        txtLast_name.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,bg="pink",text="Address",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.address_var,width=27)
        txtAddress.grid(row=5,column=1)
        
        lblpost_code=Label(DataFrameLeft,bg="pink",text="Post Code",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblpost_code.grid(row=6,column=0,sticky=W)
        txtpost_code=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.postcode_var,width=27)
        txtpost_code.grid(row=6,column=1)

        lblMobile_no=Label(DataFrameLeft,bg="pink",text="Mobile.NO",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMobile_no.grid(row=7,column=0,sticky=W)
        txtMobile_no=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.mobile_var,width=27)
        txtMobile_no.grid(row=7,column=1)

        lblBook_Id=Label(DataFrameLeft,bg="pink",text="Book Id",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBook_Id.grid(row=0,column=2,sticky=W)
        txtBook_Id=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.bookid_var,width=27)
        txtBook_Id.grid(row=0,column=3)

        lblBook_Tittle=Label(DataFrameLeft,bg="pink",text="Book Tittle",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBook_Tittle.grid(row=1,column=2,sticky=W)
        txtBook_Tittle=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.booktitle_var,width=27)
        txtBook_Tittle.grid(row=1,column=3)

        lblAuther_name=Label(DataFrameLeft,bg="pink",text="Auther Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAuther_name.grid(row=2,column=2,sticky=W)
        txtAuther_name=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.auther_var,width=27)
        txtAuther_name.grid(row=2,column=3)


        lblDate_borrowed=Label(DataFrameLeft,bg="pink",text="Date Borrowed",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDate_borrowed.grid(row=3,column=2,sticky=W)
        txtDate_borrowed=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.dateborrowed_var,width=27)
        txtDate_borrowed.grid(row=3,column=3)

        lblDate_due=Label(DataFrameLeft,bg="pink",text="Date due",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDate_due.grid(row=4,column=2,sticky=W)
        txtDate_due=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.datedue_var,width=27)
        txtDate_due.grid(row=4,column=3)

        lblDays_on_Book=Label(DataFrameLeft,bg="pink",text="Days on Book",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDays_on_Book.grid(row=5,column=2,sticky=W)
        txtDays_on_Book=Entry(DataFrameLeft,font=("times of roman",15,"bold"), textvariable=self.daysonbook_var,width=27)
        txtDays_on_Book.grid(row=5,column=3)

        lblLate_return_fine=Label(DataFrameLeft,bg="pink",text="Late Return fine",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLate_return_fine.grid(row=6,column=2,sticky=W)
        txtLate_return_fine=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.latereturnfine_var,width=27)
        txtLate_return_fine.grid(row=6,column=3)

        lblDate_overdue=Label(DataFrameLeft,bg="pink",text="Date over due",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDate_overdue.grid(row=7,column=2,sticky=W)
        txtDate_overdue=Entry(DataFrameLeft,font=("times of roman",15,"bold"),textvariable=self.dateoverdue_var,width=27)
        txtDate_overdue.grid(row=7,column=3)

        ##lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="ACTUAL PRICE",font=("times new roman",15,"bold"),padx=2,pady=6)
        ##lblPRN_No.grid(row=8,column=2,sticky=W)
        ##txtPRN_NO=Entry(DataFrameLeft,font=("times of roman",15,"bold"),width=27)
        ##txtPRN_NO.grid(row=8,column=3)



        #======================DataFrameRight==============================================
        DataFrameRight= LabelFrame(frame,text="Book Details",bg="pink",fg="green",bd=12,relief=RIDGE,font=("times of roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        listBoooks= ["Head First Book","Learn Python The Hard Way","Secret Rashy","Python Cookbook","Introduction to Machine Learning","Fluent Python","Machine Techno","My Python","Just Elif Guru","Elite","Jungli Python","Mumbai Python","Pune Python","Machine Python","Advanced Python","Inton Python","Redchili Python","Ishq Python"]

        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x == "Head First Book"):
             self.bookid_var.set("BKID5454")
             self.booktitle_var.set("PYTHON MANUAL")
             self.auther_var.set("paul berry")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif (x == "Learn Python The Hard Way"):
             self.bookid_var.set("BKID5455")
             self.booktitle_var.set("Learn Python")
             self.auther_var.set("Eric Matthes")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif(x == "Secret Rashy"):
             self.bookid_var.set("BKID5456")
             self.booktitle_var.set("Secret")
             self.auther_var.set("Al Sweigart")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")
             
            elif(x == "Python Cookbook"):
             self.bookid_var.set("BKID5457")
             self.booktitle_var.set("Cookbook")
             self.auther_var.set(" David Beazley and Brian K. Jones")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif(x == "Introduction to Machine Learning"):
             self.bookid_var.set("BKID5458")
             self.booktitle_var.set("Machine Learning")
             self.auther_var.set(" Allen B. Downey")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif(x == "Fluent Python"):
             self.bookid_var.set("BKID5459")
             self.booktitle_var.set("Fluent ")
             self.auther_var.set("  Wes McKinney ")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")


            elif(x == "Machine Techno"):
             self.bookid_var.set("BKID5460")
             self.booktitle_var.set("Techno")
             self.auther_var.set(" Brett Slatkin")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif(x == "My Python"):
             self.bookid_var.set("BKID5461")
             self.booktitle_var.set("Python")
             self.auther_var.set("David Beazley and Brian K. Jones")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif(x == "Just Elif Guru"):
             self.bookid_var.set("BKID5462")
             self.booktitle_var.set("Guru")
             self.auther_var.set("Allen B. Downey")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif(x == "Elite"):
             self.bookid_var.set("BKID5463")
             self.booktitle_var.set("lite")
             self.auther_var.set("William S. Vincent")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")


            elif(x == "Jungli Python"):
             self.bookid_var.set("BKID5464")
             self.booktitle_var.set("Jungli")
             self.auther_var.set(" Joel Grus")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")


            elif(x == "Mumbai Python"):
             self.bookid_var.set("BKID5465")
             self.booktitle_var.set("Mumbai")
             self.auther_var.set("Andreas C. Müller and Sarah Guido")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")



            elif(x == "Pune Python"):
             self.bookid_var.set("BKID5466")
             self.booktitle_var.set("Pune")
             self.auther_var.set(" Mark Lutz")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")


            elif(x == "Machine Python"):
             self.bookid_var.set("BKID5467")
             self.booktitle_var.set("Machine")
             self.auther_var.set("Dan Bader")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")



            elif(x == "Advanced Python"):
             self.bookid_var.set("BKID5468")
             self.booktitle_var.set("Advanced")
             self.auther_var.set(" Real Python Team")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")
            
            elif(x == "Inton Python"):
             self.bookid_var.set("BKID5469")
             self.booktitle_var.set("Inton")
             self.auther_var.set(" Ryan Mitchell")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")

            elif(x == "Redchili Python"):
             self.bookid_var.set("BKID5470")
             self.booktitle_var.set("Redchili")
             self.auther_var.set("Sebastian Raschka and Vahid Mirjalili")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")
             
        
            elif(x == "Ishq Python"):
             self.bookid_var.set("BKID5471")
             self.booktitle_var.set("Ishq")
             self.auther_var.set("François Chollet")
             d1 = datetime.datetime.today()
             d2 = datetime.timedelta(days=15)
             d3 = d1 + d2
             self.dateborrowed_var.set(d1)
             self.datedue_var.set(d3)
             self.daysonbook_var.set(15)
             self.latereturnfine_var.set("Rs.50")
             self.dateoverdue_var.set("No")


        listBox = Listbox(DataFrameRight, font=("Arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listscrollbar.config(command=listBox.yview)

         
        for item in listBoooks:
             listBox.insert(END,item)


       #======================BUTTONS FRAME=====================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="pink")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=5)

       #======================INFORMATION FRAME=====================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="pink")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="pink")
        Table_frame.place(x=0,y=2,width=1460,height=165)

        xscrool=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame, columns=("Member Type", "prnno","id","first name", "last name", "address", "postid", "Mobile no", "book id", "book title", "author", "date borrowed", "date due", "days", "late return fine", "date overdue"),xscrollcommand=xscrool.set, yscrollcommand=yscroll.set)
         
        xscrool.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscrool.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

# Define the headings
        self.library_table.heading("Member Type", text="Member Type")
        self.library_table.heading("prnno", text="PRN NO")
        self.library_table.heading("id", text="id")
        #self.library_table.heading("title", text="Title")
        self.library_table.heading("first name", text="First Name")
        self.library_table.heading("last name", text="Last Name")
        self.library_table.heading("address", text="Address")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("Mobile no", text="Mobile No")
        self.library_table.heading("book id", text="Book ID")
        self.library_table.heading("book title", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("date borrowed", text="Date Borrowed")
        self.library_table.heading("date due", text="Date Due")
        self.library_table.heading("days", text="Days on Book")
        self.library_table.heading("late return fine", text="Late Return Fine")
        self.library_table.heading("date overdue", text="Date Overdue")


        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Member Type",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("id",width=100)
        #self.library_table.column("title", width=100)
        self.library_table.column("first name", width=100)
        self.library_table.column("last name", width=100)
        self.library_table.column("address", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("Mobile no", width=100)
        self.library_table.column("book id", width=100)
        self.library_table.column("book title", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("date borrowed", width=100)
        self.library_table.column("date due", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("late return fine", width=100)
        self.library_table.column("date overdue", width=100)
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
        #conn=mysql.connector.connect(host="localhost",username="root",password="6200",database="syn")
        conn = mysql.connector.connect(host="localhost", user="root", password="6200", database="mydata")
        
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                  self.member_var.get(),
                                  self.prn_var.get(),
                                  self.id_var.get(),
                                  #self.tittle_var.get(),
                                  self.firstname_var.get(),
                                  self.lastname_var.get(),
                                  self.address_var.get(),
                                  self.postcode_var.get(),
                                  self.mobile_var.get(),
                                  self.bookid_var.get(),
                                  self.booktitle_var.get(),
                                  self.auther_var.get(),
                                  self.dateborrowed_var.get(),
                                  self.datedue_var.get(),
                                  self.daysonbook_var.get(),
                                  self.latereturnfine_var.get(),
                                  self.dateoverdue_var.get()
                                  ))
    
        conn.commit()
        self.fatch_data()
        conn.close()  
    
        messagebox.showinfo("sucess","Member has been inserted sucessfully")   
    



    ############################### UPDATE BUTTOM ########################################

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="6200", database="mydata")
        my_cursor=conn.cursor() 
        my_cursor.execute("update library set member=%s,id=%s,firstname=%s,lastname=%s,address=%s,postcode=%s,mobile=%s,bookid=%s,booktitle=%s,auther=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s where prn=%s",(
                                  self.member_var.get(),
                                  self.id_var.get(),
                                  self.firstname_var.get(),
                                  self.lastname_var.get(),
                                  self.address_var.get(),
                                  self.postcode_var.get(),
                                  self.mobile_var.get(),
                                  self.bookid_var.get(),
                                  self.booktitle_var.get(),
                                  self.auther_var.get(),
                                  self.dateborrowed_var.get(),
                                  self.datedue_var.get(),
                                  self.daysonbook_var.get(),
                                  self.latereturnfine_var.get(),
                                  self.dateoverdue_var.get(),
                                  self.prn_var.get(),
                                  ))
    
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()     

        messagebox.showinfo("sucess","Member has been Updated")               
                                                    


    ############################### ADD BUTTOM ########################################


    def fatch_data(self):     
         conn = mysql.connector.connect(host="localhost", user="root", password="6200", database="mydata")
         my_cursor=conn.cursor() 
         my_cursor.execute("Select * from library")   
         rows=my_cursor.fetchall()

         if len(rows)!=0:
             self.library_table.delete(*self.library_table.get_children()) 
             for i in rows:
                self.library_table.insert("",END,values=i)           
             conn.commit()
                
         conn.close()

     ############################### RIGHT FRAME VALUE SHOW ########################################


    def get_cursor(self,event=""):
       cursor_row=self.library_table.focus()
       content=self.library_table.item(cursor_row)
       row=content['values']


       self.member_var.set(row[0]),
       self.prn_var.set(row[1])
       self.id_var.set(row[2]),
       self.firstname_var.set(row[3]),
       self.lastname_var.set(row[4]),
       self.address_var.set(row[5]),
       self.postcode_var.set(row[6]),
       self.mobile_var.set(row[7]),
       self.bookid_var.set(row[8]),
       self.booktitle_var.set(row[9]),
       self.auther_var.set(row[10]),
       self.dateborrowed_var.set(row[11]),
       self.datedue_var.set(row[12]),
       self.daysonbook_var.set(row[13]),
       self.latereturnfine_var.set(row[14]),
       self.dateoverdue_var.set(row[15])

    ############################### SHOW BUTTOM ########################################
    def showData(self):
      self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get() + "\n")
      self.txtBox.insert(END,"PRN NO\t\t"+ self.prn_var.get() + "\n")
      self.txtBox.insert(END,"Id\t\t"+ self.id_var.get() + "\n")
      self.txtBox.insert(END,"FirstName\t\t"+ self.firstname_var.get() + "\n")
      self.txtBox.insert(END,"LastName\t\t"+ self.lastname_var.get() + "\n")
      self.txtBox.insert(END,"Address\t\t"+ self.address_var.get() + "\n")
      self.txtBox.insert(END,"PostCode\t\t"+ self.postcode_var.get() + "\n")
      self.txtBox.insert(END,"Mobile No\t\t"+ self.mobile_var.get() + "\n")
      self.txtBox.insert(END,"BookId\t\t"+ self.bookid_var.get() + "\n")
      self.txtBox.insert(END,"Booktitle\t\t"+ self.booktitle_var.get() + "\n")
      self.txtBox.insert(END,"Auther\t\t"+ self.auther_var.get() + "\n")
      self.txtBox.insert(END,"DateBorrowed\t\t"+ self.dateborrowed_var.get() + "\n")
      self.txtBox.insert(END,"DateDue\t\t"+ self.datedue_var.get() + "\n")
      self.txtBox.insert(END,"DaysonBook\t\t"+ self.daysonbook_var.get() + "\n")
      self.txtBox.insert(END,"LateReturnFine\t\t"+ self.latereturnfine_var.get() + "\n")
      self.txtBox.insert(END,"DateOverdue\t\t"+ self.dateoverdue_var.get() + "\n")

    ############################### RESET BUTTOM ########################################
    def reset(self):
       self.member_var.set(""),
       self.prn_var.set("")
       self.id_var.set(""),
       self.firstname_var.set(""),
       self.lastname_var.set(""),
       self.address_var.set(""),
       self.postcode_var.set(""),
       self.mobile_var.set(""),
       self.bookid_var.set(""),
       self.booktitle_var.set(""),
       self.auther_var.set(""),
       self.dateborrowed_var.set(""),
       self.datedue_var.set(""),
       self.daysonbook_var.set(""),
       self.latereturnfine_var.set(""),
       self.dateoverdue_var.set("")
       self.txtBox.delete("1.0",END)

    ############################### EXIT BUTTOM ########################################
    def iExit(self):
      iExit=tkinter.messagebox.askyesno("Library management System","DO you want to exit")
      if iExit>0:
        self.root.destroy()
        return

     ############################### EXIT BUTTOM ########################################

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error,Select the member")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="6200", database="mydata")
            my_cursor=conn.cursor() 
            query="delete from library where prn=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)


            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()


            messagebox.showinfo("sucess","Member has been Deleted")


                                                                             

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()