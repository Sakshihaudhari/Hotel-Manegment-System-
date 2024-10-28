from tkinter import*
from PIL import Image,ImageTk   
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

 


class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1140x510+220+192")


#=====================variabels=======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


 #============title===================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",14,"bold"),bg="black",fg="silver",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1366,height=50)

#================logo================

        img2=Image.open(r"C:\HOTEL RESERVATION\images\logohotel.webp")
        img2=img2.resize((120,45),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=3,width=120,height=45)

#=====================================label frame=========================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",11,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=380,height=445)

#=====================================label and entry=====================================
        #custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=25,state="readonly",font=("arial",12,"bold"))
        enty_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=25,font=("arial",12,"bold"))
        txtcname.grid(row=1,column=1)
        
        #mother name
        lblmname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=25,font=("arial",12,"bold"))
        txtmname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=23,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        # postcode
        lblPostCode=Label(labelframeleft,text="PostCode",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)

        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=25,font=("arial",12,"bold"))
        txtPostCode.grid(row=4,column=1)

        # mobilenumber
        lblMobile=Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=25,font=("arial",12,"bold"))
        txtMobile.grid(row=5,column=1)

        # email
        lblEmail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)

        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=25,font=("arial",12,"bold"))
        txtEmail.grid(row=6,column=1)

        # nationality combobox
        lblNationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=23,state="readonly")
        combo_Nationality["value"]=("Indian","America","New York","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

       # idproof type combobox
        lblIdProof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)
        
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=23,state="readonly")
        combo_id["value"]=("Adhar card","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # id number
        lblIdNumber=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=25,font=("arial",12,"bold"))
        txtIdNumber.grid(row=9,column=1)


        # address
        lblAddress=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=25,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)



   #===========================Button================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=3,y=384,width=367,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnAdd.grid(row=0,column=0,padx=1,)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnUpdate.grid(row=0,column=1,padx=1,)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnDelete.grid(row=0,column=2,padx=1,)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnReset.grid(row=0,column=3,padx=1,)

     
     #=========================tabel frame search system===================================
        Tabel_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",11,"bold"),padx=2,)
        Tabel_Frame.place(x=387,y=50,width=747,height=445)
        
        lblSearchBy=Label(Tabel_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white",padx=2,pady=3)
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Tabel_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=18,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Tabel_Frame,textvariable=self.txt_search,width=19,font=("arial",12,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Tabel_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="silver",width=7)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(Tabel_Frame,text="show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="silver",width=7)
        btnShowall.grid(row=0,column=4,padx=1)


  #================show data tabel===============================

        details_table=Frame(Tabel_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=740,height=309)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Tabel=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile",
                                            "email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_Details_Tabel.xview)
        Scroll_y.config(command=self.Cust_Details_Tabel.yview)

        self.Cust_Details_Tabel.heading("ref",text="Refer No")
        self.Cust_Details_Tabel.heading("name",text="Name")
        self.Cust_Details_Tabel.heading("mother",text="Mother Name")
        self.Cust_Details_Tabel.heading("gender",text="Gender")
        self.Cust_Details_Tabel.heading("post",text="PosteCode")
        self.Cust_Details_Tabel.heading("mobile",text="Mobile")
        self.Cust_Details_Tabel.heading("email",text="Email")
        self.Cust_Details_Tabel.heading("nationality",text="Nationality")
        self.Cust_Details_Tabel.heading("idproof",text="Id Proof")
        self.Cust_Details_Tabel.heading("idnumber",text="Id Number")
        self.Cust_Details_Tabel.heading("address",text="Address")

        self.Cust_Details_Tabel["show"]="headings"

        self.Cust_Details_Tabel.column("ref",width=100)
        self.Cust_Details_Tabel.column("name",width=100)
        self.Cust_Details_Tabel.column("mother",width=100)
        self.Cust_Details_Tabel.column("gender",width=100)
        self.Cust_Details_Tabel.column("post",width=100)
        self.Cust_Details_Tabel.column("mobile",width=100)
        self.Cust_Details_Tabel.column("email",width=100)
        self.Cust_Details_Tabel.column("nationality",width=100)
        self.Cust_Details_Tabel.column("idproof",width=100)
        self.Cust_Details_Tabel.column("idnumber",width=100)
        self.Cust_Details_Tabel.column("address",width=100)

        self.Cust_Details_Tabel.pack(fill=BOTH,expand=1)
        self.Cust_Details_Tabel.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_cust_name.get(), self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
             except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
         my_cursor=conn.cursor()
         my_cursor.execute("Select * from customer")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.Cust_Details_Tabel.delete(*self.Cust_Details_Tabel.get_children())
             for i in rows:
                 self.Cust_Details_Tabel.insert("",END,values=i)
             conn.commit()
             conn.close()

    def get_cuersor(self,event=""):
        cuersor_rows=self.Cust_Details_Tabel.focus()
        content=self.Cust_Details_Tabel.item(cuersor_rows)
        row=content["values"]
   

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
           my_cursor=conn.cursor()
           my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get(),self.var_ref.get()))
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Reservation System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
             my_cursor=conn.cursor()
             query="delete from customer where ref=%s"
             value=(self.var_ref.get(),)
             my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
       # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
       # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    
    # Search System 
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Tabel.delete(*self.Cust_Details_Tabel.get_children())
            for i in rows:
                self.Cust_Details_Tabel.insert("",END,values=i)
            conn.commit()
            conn.close()
            if __name__ =="__main__":
                root=Tk()
                obj=cust_win(root)
                root.mainloop()
