from tkinter import*
import random
import os
from tkinter import messagebox

#=================main================
class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        self.root.configure(bg = "#c3c3c3")
        title = Label ( self.root, text="Billing Software", font=('Goudy Stout', 30, 'bold'), pady=2,bd=12, bg="#02075d", fg="#f0ffff", relief=FLAT)
        title.pack(fill=X)
#================variables=================
        self.sanitizer = IntVar()
        self.facemask = IntVar()
        self.hand_gloves = IntVar()
        self.disinfectant = IntVar()
        self.penicillin = IntVar()
        self.thermometer = IntVar()
#======================grocery==================
        self.food_stuffs = IntVar()
        self.cooking_oil = IntVar()
        self.fruits = IntVar()
        self.vegetables = IntVar()
        self.meat= IntVar()
        self.seasonings = IntVar()
        self.canned_foods = IntVar()
#==================Beverages============
        self.soft_drinks = IntVar()
        self.malt_drinks = IntVar()
        self.wine = IntVar()
        self.yogurt = IntVar()
        self.fruit_juice = IntVar()
        self.beer = IntVar()
#================total product price===============
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.beverages_price = StringVar()
#===================customer==================
        self.c_name =StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.c_tax = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

#=========================tax================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.beverages_tax = StringVar()
#==============customer retail details================
        F1 = LabelFrame(self.root, text="Customer Details", font=('agency fb', 15, 'bold'),bd=10, fg="#010b13", bg="#8ba8b7")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg="#f0ffff", font=('Constantia', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='Constantia 15', bd=7, relief= RIDGE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#f0ffff", font=('Constantia', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='Constantia 15', bd=7, relief=RIDGE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#f0ffff", font=('Constantia', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='Constantia 15', bd=7, relief=RIDGE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command= self.find_bill, width=10, bd=7, font=('Constantia', 12, 'bold'), relief=RAISED)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

#=========Medical=====================
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="#8ba8b7", bg="#02075d")
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('helvetica', 16, 'bold'), bg= "#02075d", fg="#8ba8b7")
        sanitizer_lbl.grid( row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font='helvetica 15', bd=5, relief=RIDGE)
        sanitizer_txt.grid(row=0, column=1, pady=10, padx=10)

        facemask_lbl = Label(F2, text="Face Mask", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7")
        facemask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W' )
        facemask_txt = Entry(F2, width=10, textvariable=self.facemask, font='helvetica 15', bd=5, relief=RIDGE)
        facemask_txt.grid(row=1, column=1, pady=10, padx=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font='helvetica 15', bd=5, relief=RIDGE)
        hand_gloves_txt.grid( row=2, column=1, pady=10, padx=10)

        disinfectant_lbl = Label(F2, text="Disinfectant", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7")
        disinfectant_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        disinfectant_txt = Entry(F2, width=10, textvariable=self.disinfectant, font='helvetica 15', bd=5, relief=RIDGE)
        disinfectant_txt.grid(row=3, column=1, pady=10, padx=10)

        penicillin_lbl = Label(F2, text="Penicillin", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7")
        penicillin_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        penicillin_txt = Entry(F2, width=10, textvariable=self.penicillin, font='helvetica 15', bd=5, relief=RIDGE)
        penicillin_txt.grid(row=4, column=1, pady=10, padx=10)

        thermometer_lbl = Label(F2, text="Thermometer", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7")
        thermometer_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermometer_txt = Entry(F2, width=10, textvariable=self.thermometer, font='helvetica 15', bd=5, relief=RIDGE)
        thermometer_txt.grid(row=5, column=1, pady=10, padx=10)
#===============Groceryitems=======================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 16, 'bold'), bd=10, fg="#02075d", bg="#8ba8b7")
        F3.place(x=340, y=180, width=325, height=380)

        food_stuffs_lbl = Label(F3, text="Food stuffs", font=('helvetica', 16, 'bold'), fg="#02075d", bg="#8ba8b7")
        food_stuffs_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        food_stuffs_txt = Entry(F3, width=10, textvariable=self.food_stuffs, font=('helvetica', 15), bd=5, relief=RIDGE)
        food_stuffs_txt.grid(row=0, column=1, padx=10, pady=10)

        cooking_oil_lbl = Label(F3, text="Cooking Oil", font=('helvetica', 16, 'bold'), fg="#02075d", bg="#8ba8b7" )
        cooking_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W" )
        cooking_oil_txt = Entry(F3, width=10, textvariable=self.cooking_oil, font=('hevetica', 15), bd=5,relief=RIDGE)
        cooking_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        fruits_lbl = Label ( F3, text="Fruits", font=('helvetica', 16, 'bold'), fg="#02075d", bg="#8ba8b7" )
        fruits_lbl.grid ( row=2, column=0, padx=10, pady=10, sticky="W" )
        fruits_txt = Entry ( F3, width=10, textvariable=self.fruits, font=('helvetica', 15), bd=5,relief=RIDGE )
        fruits_txt.grid ( row=2, column=1, padx=10, pady=10)

        meat_lbl = Label ( F3, text="Meat", font=('helvetica', 16, 'bold'), fg="#02075d", bg="#8ba8b7" )
        meat_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="W" )
        meat_txt = Entry( F3, width=10, textvariable=self.meat, font=('helvetica', 15), bd=5, relief=RIDGE )
        meat_txt.grid(row=3, column=1, padx=10, pady=10)

        seasonings_lbl = Label(F3, text="Seasonings", font=('helvetica', 16, 'bold'), fg="#02075d", bg="#8ba8b7")
        seasonings_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="W")
        seasonings_txt = Entry(F3, width=10, textvariable=self.seasonings, font=('helvetica', 15), bd=5, relief=RIDGE)
        seasonings_txt.grid(row=4, column=1, padx=10, pady=10)

        canned_foods_lbl = Label ( F3, text="Canned foods", font=('helvetica', 16, 'bold'), fg="#02075d", bg="#8ba8b7" )
        canned_foods_lbl.grid ( row=5, column=0, padx=10, pady=10, sticky="W")
        canned_foods_txt = Entry ( F3, width=10, textvariable=self.canned_foods, font=('helvetica', 15), bd=5, relief=RIDGE )
        canned_foods_txt.grid(row=5, column=1, padx=10, pady=10)
#=======================Beverages==========================
        F4 = LabelFrame(self.root, text="Beverages", font=('times new roman', 15, 'bold'), bd=10, fg="#8ba8b7", bg="#02075d")
        F4.place(x=670, y=180, width=325, height=380)

        soft_drinks_lbl = Label ( F4, text="Soft Drinks", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7" )
        soft_drinks_lbl.grid ( row=0, column=0, padx=10, pady=10, sticky='W' )
        soft_drinks_txt = Entry ( F4, width=10, textvariable=self.soft_drinks, font='helvetica 15', bd=5, relief=RIDGE )
        soft_drinks_txt.grid ( row=0, column=1, pady=10, padx=10 )

        malt_drinks_lbl = Label(F4, text="Malt Drinks", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7" )
        malt_drinks_lbl.grid( row=1, column=0, padx=10, pady=10, sticky='W' )
        malt_drinks_txt = Entry(F4, width=10, textvariable=self.malt_drinks, font='helvetica 15', bd=5, relief=RIDGE )
        malt_drinks_txt.grid( row=1, column=1, pady=10, padx=10 )

        wine_lbl = Label(F4, text="Wine", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7" )
        wine_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W' )
        wine_txt = Entry(F4, width=10, textvariable=self.wine, font='helvetica 15', bd=5, relief=RIDGE )
        wine_txt.grid(row=2, column=1, pady=10, padx=10)

        yogurt_lbl = Label(F4, text="Yogurt", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7" )
        yogurt_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W' )
        yogurt_txt = Entry(F4, width=10, textvariable=self.yogurt, font='helvetica 15', bd=5, relief=RIDGE )
        yogurt_txt.grid(row=3, column=1, pady=10, padx=10)

        fruit_juice_lbl = Label ( F4, text="Fruit Juice", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7" )
        fruit_juice_lbl.grid ( row=4, column=0, padx=10, pady=10, sticky='W' )
        fruit_juice_txt = Entry ( F4, width=10, textvariable=self.fruit_juice, font='helvetica 15', bd=5, relief=RIDGE )
        fruit_juice_txt.grid ( row=4, column=1, pady=10, padx=10 )

        beer_lbl = Label ( F4, text="Beer", font=('helvetica', 16, 'bold'), bg="#02075d", fg="#8ba8b7")
        beer_lbl.grid ( row=5, column=0, padx=10, pady=10, sticky='W' )
        beer_txt = Entry ( F4, width=10, textvariable=self.beer, font='helvetica 15', bd=5, relief=RIDGE )
        beer_txt.grid ( row=5, column=1, pady=10, padx=10 )

#========================BillArea====================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width= 350, height=380)

        bill_title = Label(F5, text="Bill Area", font=('helvetica', 15, 'bold'), bd=7, relief= FLAT)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient= VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side= RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

#================ButtonFrame========================
        F6 = LabelFrame(self.root, text= "Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="#02075d", bg="#8ba8b7")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('helvetica', 14, 'bold'), fg="#02075d", bg="#8ba8b7")
        m1_lbl.grid ( row=0, column=0, padx=20, pady=1, sticky='W' )
        m1_txt = Entry ( F6, width=18, textvariable=self.medical_price, font='helvetica 10 bold', bd=7, relief=RIDGE)
        m1_txt.grid ( row=0, column=1, padx=18, pady=1 )

        m1_lbl = Label ( F6, text="Total Grocery Price", font=('helvetica', 14, 'bold'), fg="#02075d", bg="#8ba8b7" )
        m1_lbl.grid ( row=1, column=0, padx=20, pady=1, sticky='W' )
        m1_txt = Entry ( F6, width=18, textvariable=self.grocery_price, font='helvetica 10 bold', bd=7, relief=RIDGE )
        m1_txt.grid ( row=1, column=1, padx=18, pady=1 )

        m1_lbl = Label ( F6, text="Total Beverages Price", font=('helvetica', 14, 'bold'), fg="#02075d", bg="#8ba8b7" )
        m1_lbl.grid ( row=2, column=0, padx=20, pady=1, sticky='W' )
        m1_txt = Entry ( F6, width=18, textvariable=self.beverages_price, font='helvetica 10 bold', bd=7, relief=RIDGE )
        m1_txt.grid ( row=2, column=1, padx=18, pady=1 )

        m1_lbl = Label ( F6, text="Medical Tax", font=('helvetica', 14, 'bold'), fg="#02075d", bg="#8ba8b7" )
        m1_lbl.grid ( row=0, column=2, padx=20, pady=1, sticky='W' )
        m1_txt = Entry ( F6, width=18, textvariable=self.medical_tax, font='helvetica 10 bold', bd=7, relief=RIDGE )
        m1_txt.grid ( row=0, column=3, padx=18, pady=1 )

        m1_lbl = Label ( F6, text="Grocery Tax", font=('helvetica', 14, 'bold'), fg="#02075d", bg="#8ba8b7" )
        m1_lbl.grid ( row=1, column=2, padx=20, pady=1, sticky='W' )
        m1_txt = Entry ( F6, width=18, textvariable=self.grocery_tax, font='helvetica 10 bold', bd=7, relief=RIDGE )
        m1_txt.grid ( row=1, column=3, padx=18, pady=1 )

        m1_lbl = Label ( F6, text="Beverages Tax", font=('helvetica', 14, 'bold'), fg="#02075d", bg="#8ba8b7" )
        m1_lbl.grid ( row=2, column=2, padx=20, pady=1, sticky='W' )
        m1_txt = Entry ( F6, width=18, textvariable=self.beverages_tax, font='helvetica 10 bold', bd=7, relief=RIDGE )
        m1_txt.grid ( row=2, column=3, padx=18, pady=1 )

#======================buttons=====================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x= 760, width=580, height=105)

        total_btn = Button(btn_f, command= self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button ( btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold' )
        generateBill_btn.grid ( row=0, column=1, padx=5, pady=5 )

        clear_btn = Button ( btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold' )
        clear_btn.grid ( row=0, column=2, padx=5, pady=5)

        exit_btn = Button( btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold' )
        exit_btn.grid(row=0, column=3, padx=5, pady=5 )
        self.welcome_bill()
#===================total bill====================
    def total(self):
        self.m_s_p = self.sanitizer.get()*50
        self.m_h_g_p = self.hand_gloves.get()*100
        self.m_f_m_p = self.facemask.get()*50
        self.m_d_p = self.disinfectant.get()*50
        self.m_p_p = self.penicillin.get()*20
        self.m_t_p = self.thermometer.get()*100
        self.total_medical_price = float(self.m_s_p+self.m_h_g_p+self.m_f_m_p+self.m_d_p+self.m_p_p+self.m_t_p)

        self.medical_price.set("$ " + str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax.set("$ " + str(self.c_tax))

        self.g_f_s_p = self.food_stuffs.get()*300
        self.g_c_o_p_ = self.cooking_oil.get()*100
        self.g_f_p = self.fruits.get()*100
        self.g_m_p = self.meat.get()*500
        self.g_s_p = self.seasonings()*500
        self.g_c_f_p = self.canned_foods()*100
        self.total_grocery_price = float(self.g_f_s_p+self.g_c_o_p_+self.g_f_p+self.g_m_p+self.g_s_p+self.g_c_f_p)

        self.grocery_price.set("$ " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax.set("$ " + str(self.g_tax))

        self.b_s_d_p = self.soft_drinks.get()*10
        self.b_m_d_p = self.malt_drinks.get()*20
        self.b_w_p = self.wine.get()*100
        self.b_y_p = self.yogurt.get()*50
        self.b_f_j_p = self.fruit_juice.get()*50
        self.b_b_p = self.beer.get()*50
        self.total_beverages_price = float(self.b_s_d_p+self.b_m_d_p+self.b_w_p+self.b_y_p+self.b_f_j_p+self.b_b_p)

        self.beverages_price.set("$ " + str(self.total_beverages_price))
        self.b_tax = round((self.total_beverages_price*0.1),2)
        self.beverages_tax.set("$ " + str(self.b_tax))

        self.total_bill = float(self.total_medical_price + self.total_grocery_price + self.total_beverages_price + self.c_tax + self.g_tax + self.b_tax)

#===================welcomebill===========
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to L-STRWEB Retail")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Bill Number:{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=================================")
        self.txtarea.insert(END, f"\nProducts\tQTY\t\tPrice")


#===============billArea==================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer's detail is required")
        elif self.medical_price.get() == "# 0.0" and self.grocery_price.get() == "# 0.0" and self.beverages_price.get() == "# 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
#===============medical=================
        if self.sanitizer.get()!= 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.facemask.get() != 0:
            self.txtarea.insert(END, f"\n Face Mask\t\t{self.facemask.get()}\t\t{self.m_f_m_p}")
        if self.disinfectant.get() != 0:
            self.txtarea.insert(END, f"\n Disinfectant\t\t{self.disinfectant.get()}\t\t{self.m_d_p}")
        if self.penicillin.get() != 0:
            self.txtarea.insert ( END, f"\n Penicillin\t\t{self.penicillin.get()}\t\t{self.m_p_p}")
        if self.thermometer.get ( ) != 0:                self.txtarea.insert ( END, f"\n Thermometer\t\t{self.thermometer.get()}\t\t{self.m_t_p}")
#===============grocery=========================
        if self.food_stuffs.get() != 0:
             self.txtarea.insert(END, f"\n Food Stuffs\t\t{self.food_stuffs.get()}\t\t{self.g_f_s_p}")
        if self.cooking_oil.get() != 0:
            self.txtarea.insert(END, f"\n Cooking Oil\t\t{self.cooking_oil.get()}\t\t{self.g_c_o_p}")
        if self.fruits.get() != 0:
            self.txtarea.insert(END, f"\n Fruits\t\t{self.fruits.get()}\t\t{self.g_f_p}")
        if self.meat.get() != 0:
            self.txtarea.insert(END, f"\n Meat\t\t{self.meat.get()}\t\t{self.g_m_p}")
        if self.seasonings.get() != 0:
            self.txtarea.insert(END, f"\n Seasonings\t\t{self.seasonings.get()}\t\t{self.g_s_p}")
        if self.sanitizer.get() != 0:
            self.txtarea.insert( END, f"\nSanitizer\t\t{self.sanitizer.get ( )}\t\t{self.m_s_p}")
#==============beverages=================
        if self.soft_drinks.get() != 0:
            self.txtarea.insert(END, f"\n Soft Drinks\t\t{self.soft_drinks.get()}\t\t{self.b_s_d_p}")
        if self.malt_drinks.get() != 0:
            self.txtarea.insert(END, f"\n Malt Drinks\t\t{self.malt_drinks.get()}\t\t{self.b_m_d_p}")
        if self.wine.get() != 0:
            self.txtarea.insert(END, f"\n Wine\t\t{self.wine.get()}\t\t{self.b_w_p}")
        if self.yogurt.get() != 0:
            self.txtarea.inser (END, f"\n Yogurt\t\t{self.yogurt.get()}\t\t{self.b_y_p}")
        if self.fruit_juice.get() != 0:
            self.txtarea.insert(END, f"\n Fruit Juice\t\t{self.fruit_juice.get()}\t\t{self.b_f_j_p}")
        if self.beer.get() != 0:
            self.txtarea.insert(END, f"\n Beer\t\t{self.soft_drinks.get()}\t\t{self.b_b_p}")

#===============taxes=====================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.groveery_tax.get()}")
        if self.beverages_tax.get() != '0.0':
            self.txtarea.insert ( END, f"\n Beverages Tax\t\t\t{self.beverages_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bill:\t\t\t #(self.total_bill)")
        self.txtarea.insert(END, f"\n-----------------------")
        self.save_bill()

#+===================savebill==================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
            return


#==========================find_bill====================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")
#================================clear bill==================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do ypu really want to clear?")
        if op > 0:
            self.hand_gloves.set(0)
            self.sanitizer.set(0)
            self.facemask.set(0)
            self.disinfectant.set(0)
            self.penicillin.set(0)
            self.thermometer.set(0)
#==========grocery================
            self.food_stuffs.set(0)
            self.cooking_oil.set(0)
            self.fruits.set(0)
            self.meat.set(0)
            self.seasonings.set(0)
            self.canned_foods.set(0)
#===========beverages====================
            self.soft_drinks.set(0)
            self.malt_drinks.set(0)
            self.wine.set(0)
            self.yogurt.set(0)
            self.fruit_juice.set(0)
            self.beer.set(0)

#====================taxes================================
        self.medical_price.set("")
        self.grocery_price.set("")
        self.beverages_price.set("")

        self.medical_tax.set("")
        self.grocery_tax.set("")
        self.cold_drinks_tax.set("")

        self.c_name.set( "" )
        self.c_phone.set("")

        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill.set("")
        self.welcome_bill()

#====================== exit=================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()




root = Tk()
obj = Bill_app(root)
root.mainloop()
