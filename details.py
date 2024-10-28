from tkinter import*
from PIL import Image,ImageTk   
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1140x510+220+192")


#============title===================
        lbl_title=Label(self.root,text="DETAILS",font=("times new roman",14,"bold"),bg="black",fg="silver",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1366,height=50)

#================logo================

        img2=Image.open(r"C:\HOTEL RESERVATION\images\logohotel.webp")
        img2=img2.resize((120,45),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=3,width=120,height=45)

#=====================================label frame=========================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Rooms Add",font=("times new roman",11,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=480,height=340)

        #Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
 
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=15,font=("arial",12,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)

       #Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
 
        self.var_roomNo=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=15,font=("arial",12,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType=Label(labelframeleft,text="RoomType",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
 
        self.var_RoomType=StringVar()
        enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=15,font=("arial",12,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)


 #===========================Button================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=3,y=190,width=367,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="silver",width=8)
        btnReset.grid(row=0,column=3,padx=1)

 #=========================tabel frame ===================================

        Tabel_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",11,"bold"),padx=2,)
        Tabel_Frame.place(x=525,y=55,width=550,height=336)

        Scroll_x=ttk.Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Tabel_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Tabel_Frame,column=("floor","roomno","roomType"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
       
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()


# add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_RoomType.get()
                                                                           
                                                                  ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
             except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)

# fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
         my_cursor=conn.cursor()
         my_cursor.execute("Select * from details")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                 self.room_table.insert("",END,values=i)
             conn.commit()
             conn.close()

# get cursor 
    def get_cuersor(self,event=""):
        cuersor_rows=self.room_table.focus()
        content=self.room_table.item(cuersor_rows)
        row=content["values"]


        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])


# Update function
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor number",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
           my_cursor=conn.cursor()
           my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(self.var_floor.get(),self.var_RoomType.get(),self.var_roomNo.get(),))
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Update"," New Room details has been updated successfully",parent=self.root)

# Delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Reservation System","Do you want to delete this Room Details",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.connect(host="localhost",username="root",password="renuka7798511235",database="mydata")
             my_cursor=conn.cursor()
             query="delete from details where RoomNo=%s"
             value=(self.var_roomNo.get(),)
             my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  
    
    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")
        if __name__ =="__main__":
            root=Tk()
            obj=DetailsRoom(root)
            root.mainloop()