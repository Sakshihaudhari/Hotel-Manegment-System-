from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from customer import cust_win
from room import Roombooking
from details import DetailsRoom




class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1366x768+0+0")


           #================1st image===============
        img1=Image.open(r"C:\HOTEL RESERVATION\images\hotel1.jpg")
        img1=img1.resize((1366,768),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1366,height=140)

        #================logo================

        img2=Image.open(r"C:\HOTEL RESERVATION\images\logohotel.webp")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #============title===================
        lbl_title=Label(self.root,text="LUXURIOUS CROWN HOTEL",font=("times new roman",40,"bold"),bg="black",fg="silver",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1366,height=50)

        #===========main frame==============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #============== menu =================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="#9C661F",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230,)

        #===========main frame==============
        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=228,height=190)

        cust_button=Button(button_frame,text="CUSTOMER",command=self.cust_details,width=22,height=1,font=("times new roman",14,"bold"),bg="black",fg="silver",bd=0,cursor="hand1")
        cust_button.grid(row=0,column=0,pady=1)

        room_button=Button(button_frame,text="ROOM BOOKING",command=self.roombooking,width=22,height=1,font=("times new roman",14,"bold"),bg="black",fg="silver",bd=0,cursor="hand1")
        room_button.grid(row=1,column=0,pady=1)

        details_button=Button(button_frame,text="DETAILS",command=self.details_room,width=22,height=1,font=("times new roman",14,"bold"),bg="black",fg="silver",bd=0,cursor="hand1")
        details_button.grid(row=2,column=0,pady=1)


        logout_button=Button(button_frame,text="LOGOUT",command=self.logout,width=22,height=1,font=("times new roman",14,"bold"),bg="black",fg="silver",bd=0,cursor="hand1")
        logout_button.grid(row=3,column=0,pady=1)


        #===========right side image==============
        img3=Image.open(r"C:\HOTEL RESERVATION\images\slide3.jpg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)


        #===========down side image==============

        img4=Image.open(r"C:\HOTEL RESERVATION\images\food1.jpg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        
        img5=Image.open(r"C:\HOTEL RESERVATION\images\food2.jpg")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.customer=Toplevel(self.root)
        self.app=cust_win(self.customer)

    def roombooking(self):
        self.customer=Toplevel(self.root)
        self.app=Roombooking(self.customer)

    def details_room(self):
        self.customer=Toplevel(self.root)
        self.app=DetailsRoom(self.customer)

    
    def logout(self):
         self.root.destroy()
         if __name__ == "__main__":
            root=Tk()
            obj=HotelManagementSystem(root)
            root.mainloop()
