from tkinter import*
from PIL import Image,ImageTk   
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Reservatoion System")
        self.root.geometry("1140x510+220+192")
        #============ variables ===================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        

       #============title===================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",14,"bold"),bg="black",fg="silver",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1366,height=50)

       #================logo================

        img2=Image.open(r"C:\HOTEL RESERVATION\images\logohotel.webp")
        img2=img2.resize((120,45),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=3,width=120,height=45)

        #=====================================label frame=========================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("times new roman",11,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=380,height=445)


        #=====================================label and entry=====================================
        #cust contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=15,font=("arial",12,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)

        # =====================================fetch data button==========================

        btnFetchData=Button(labelframeleft,text="Search Data",command=self.Fetch_contact,font=("arial",9,"bold"),bg="black",fg="silver",width=10)
        btnFetchData.place(x=292,y=2)

        #check in
        check_in_date=Label(labelframeleft,text="Check_in Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=23,font=("arial",12,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #check out
        lbl_check_out=Label(labelframeleft,text="Check_out Date",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=23,font=("arial",12,"bold"))
        txt_check_out.grid(row=2,column=1)

        # Room type combo box
        label_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=22)
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available Room
        lblRoomAvailabe=Label(labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailabe.grid(row=4,column=0,sticky=W)
        #lblRoomAvailabe=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=23,font=("arial",12,"bold"))
        #lblRoomAvailabe.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=22)
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


        # Meal
        lblMeal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        lblMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=23,font=("arial",12,"bold"))
        lblMeal.grid(row=5,column=1)

        # No Of Days
        lblNoOfDays=Label(labelframeleft,text="No Of Days",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        lblNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noOfdays,width=23,font=("arial",12,"bold"))
        lblNoOfDays.grid(row=6,column=1)

        # Paid Tax
        lblNoOfDays=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        lblNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=23,font=("arial",12,"bold"))
        lblNoOfDays.grid(row=7,column=1)

        # subtotal
        lblNoOfDays=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        lblNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=23,font=("arial",12,"bold"))
        lblNoOfDays.grid(row=8,column=1)

        # Total Cost
        lblIdNumber=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        lblIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=23,font=("arial",12,"bold"))
        lblIdNumber.grid(row=9,column=1)

        #==================bill butn======================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="silver",width=7)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #===========================Button================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=3,y=384,width=367,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        #=========================  Right Image  ===================================
        img3=Image.open(r"C:\HOTEL RESERVATION\images\bedroom1.jpg")
        img3=img3.resize((400,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
            

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=735,y=55,width=400,height=220)



        #=========================tabel frame search system===================================

        Tabel_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",11,"bold"),padx=2,)
        Tabel_Frame.place(x=387,y=260,width=747,height=235)
        
        lblSearchBy=Label(Tabel_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white",padx=2,pady=3)
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Tabel_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=18,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Tabel_Frame,textvariable=self.txt_search,width=19,font=("arial",12,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Tabel_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="silver",width=7)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(Tabel_Frame,text="show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="silver",width=7)
        btnShowall.grid(row=0,column=4,padx=1)
    

     #================   show data tabel  ===============================

        details_table=Frame(Tabel_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=740,height=165)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Room_tabel=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Room_tabel.xview)
        Scroll_y.config(command=self.Room_tabel.yview)


        self.Room_tabel.heading("contact",text="Contact")
        self.Room_tabel.heading("checkin",text="Check In")
        self.Room_tabel.heading("checkout",text="Check Out")
        self.Room_tabel.heading("roomtype",text="Room Type")
        self.Room_tabel.heading("roomavailable",text="Room Available")
        self.Room_tabel.heading("meal",text="Meal")
        self.Room_tabel.heading("noOfdays",text="NoOfDays")

        self.Room_tabel["show"]="headings"

        
        self.Room_tabel.column("contact",width=130)
        self.Room_tabel.column("checkin",width=130)
        self.Room_tabel.column("checkout",width=130)
        self.Room_tabel.column("roomtype",width=130)
        self.Room_tabel.column("roomavailable",width=130)
        self.Room_tabel.column("meal",width=130)
        self.Room_tabel.column("noOfdays",width=130)
        self.Room_tabel.pack(fill=BOTH,expand=1)
        
        self.Room_tabel.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

# add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noOfdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
             except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
    
# fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
         my_cursor=conn.cursor()
         my_cursor.execute("Select * from room")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.Room_tabel.delete(*self.Room_tabel.get_children())
             for i in rows:
                 self.Room_tabel.insert("",END,values=i)
             conn.commit()
             conn.close()

# get cursor 
    def get_cuersor(self,event=""):
        cuersor_rows=self.Room_tabel.focus()
        content=self.Room_tabel.item(cuersor_rows)
        row=content["values"]
   

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdays.set(row[6])

# Update function
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
           my_cursor=conn.cursor()
           my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noOfdays.get(),self.var_contact.get()))
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

 # Delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Reservation System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
             my_cursor=conn.cursor()
             query="delete from Room where Contact=%s"
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  

# Reset fun
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")


#================================All DATA FETCH=========================================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact NUmber",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
            my_cursor=conn.cursor()
            query=("select Name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
#=========================NAME=====================
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=390,y=50,width=330,height=200)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

#=========================GENDER=====================
            conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
            my_cursor=conn.cursor()
            query=("select Gender from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=25)

            lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl2.place(x=90,y=25)

#=========================EMAIL==========================
            conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
            my_cursor=conn.cursor()
            query=("select Email from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblemail.place(x=0,y=60)

            lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl3.place(x=90,y=60)

#=========================NATIONALITY==========================
            conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
            my_cursor=conn.cursor()
            query=("select Nationality from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblNationality.place(x=0,y=90)

            lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl4.place(x=90,y=90)

#=========================ADDRESSS==========================
            conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
            my_cursor=conn.cursor()
            query=("select Address from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lblAddress.place(x=0,y=120)

            lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl5.place(x=90,y=120)

#=========================REFERENCE==========================
            conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
            my_cursor=conn.cursor()
            query=("select Ref from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblref=Label(showDataframe,text="Reference No. :",font=("arial",12,"bold"))
            lblref.place(x=0,y=155)

            lbl6=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl6.place(x=128,y=155)

# Search System 
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_tabel.delete(*self.Room_tabel.get_children())
            for i in rows:
                self.Room_tabel.insert("",END,values=i)
            conn.commit()
            conn.close()
        
        
    
#  TOTAL  AND  CALCULATION

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate-inDate).days)
     # Breakfast
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(350)
            q2=float(700)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(400)
            q2=float(1100)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

         #Lunch
        if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(390)
            q2=float(900)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(380)
            q2=float(1002)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
             
         #Dinner

        if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(450)
            q2=float(600)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(689)
            q2=float(1500)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
  
        if (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Duplex"):
            q1=float(900)
            q2=float(2500)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Duplex"):
            q1=float(890)
            q2=float(2000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Duplex"):
            q1=float(900)
            q2=float(2100)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            if __name__ =="__main__":
                root=Tk()
                obj=Roombooking(root)
                root.mainloop()
