import time
from tkinter import *
from tkinter import filedialog, messagebox
import random

#Functions

#Function Reset
def Reset():
    textReceipt.delete(1.0, END)
    #to reset quantity box
    e_polRotti.set("0")
    e_Eggrotti.set("0")
    e_VegRotti.set("0")
    e_FishRolls.set("0")
    e_ChickenRolls.set("0")
    e_SlicedPizza.set("0")
    e_chickenSandwich.set("0")
    e_hotdog.set("0")
    e_seenisambolBread.set("0")
    e_Noodles.set("0")

    e_plaintea.set("0")
    e_Milktea.set("0")
    e_Gingertea.set("0")
    e_Milk.set("0")
    e_Coffee.set("0")
    e_IcedCoffee.set("0")
    e_Milo.set("0")
    e_SoftDrinks.set("0")
    e_Faluda.set("0")
    e_FruitJuice.set("0")

    e_CupIceCream.set("0")
    e_ConeIceCream.set("0")
    e_SlicedCake.set("0")
    e_CupCake.set("0")
    e_Cookies.set("0")
    e_Pudding.set("0")
    e_Wattalappam.set("0")
    e_FruitSalad.set("0")
    e_Biscuit.set("0")
    e_Chocolate.set("0")

    #to disable quanitity box
    textpolRotti.config(state=DISABLED)
    textEggrotti.config(state=DISABLED)
    textVegRotti.config(state=DISABLED)
    textFishRolls.config(state=DISABLED)
    textChickenRolls.config(state=DISABLED)
    textSlicedPizza.config(state=DISABLED)
    textchickenSandwich.config(state=DISABLED)
    texthotdog.config(state=DISABLED)
    textseenisambolBread.config(state=DISABLED)
    textNoodles.config(state=DISABLED)

    textplaintea.config(state=DISABLED)
    textMilktea.config(state=DISABLED)
    textGingertea.config(state=DISABLED)
    textMilo.config(state=DISABLED)
    textCoffee.config(state=DISABLED)
    textIcedCoffee.config(state=DISABLED)
    textMilk.config(state=DISABLED)
    textSoftDrinks.config(state=DISABLED)
    textFaluda.config(state=DISABLED)
    textFruitJuice.config(state=DISABLED)

    textCupIceCream.config(state=DISABLED)
    textConeIceCream.config(state=DISABLED)
    textSlicedCake.config(state=DISABLED)
    textCupCake.config(state=DISABLED)
    textCookies.config(state=DISABLED)
    textPudding.config(state=DISABLED)
    textWattalappam.config(state=DISABLED)
    textFruitSalad.config(state=DISABLED)
    textBiscuit.config(state=DISABLED)
    textChocolate.config(state=DISABLED)

    #to rest checkbox
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)

#to rest cost details
    costoffoodvar.set("")
    costofdrinkvar.set("")
    costofdessertvar.set("")
    subtotalvar.set("")
    servicetaxvar.set("")
    totalcostvar.set("")


#Function Send
def Send():
    def send_msg():
        Messege=textarea.get(1.0, END)
        nember= numberfield.get()
    root2=Toplevel()

    root2.title("SEND BILL")
    root2.config(bg="cornsilk3")
    root2.geometry("485x620+50+50")

    numberLabel=Label(root2, text="Mobile Number", font=("arial", 18, "bold underline"), bg="thistle4", fg="black")
    numberLabel.pack(pady=5)

    numberfield=Entry(root2, font=("halvetica",22,"bold"), bd=2, width=24)
    numberfield.pack(pady=5)

    BillLabel = Label(root2, text="Bill Details", font=("arial", 18, "bold underline"), bg="thistle4", fg="black")
    BillLabel.pack(pady=5)

    textarea=Text(root2, font=("arial", 12, "bold"), bd=2, width=42, height=14 )
    textarea.pack(pady=5)
    textarea.insert(END, "Receipt Ref: \t\t"+billnumber+"\t\t"+date+"\n\n")

    if costoffoodvar.get() != "0 Rs":
        textarea.insert(END, f'Cost of Food\t\t\t{PriceofFood}Rs.\n')
    if costofdrinkvar.get() != "0 Rs":
        textarea.insert(END, f'Cost of Drinks\t\t\t{PriceofDrinks}Rs.\n')
    if costofdessertvar.get() != "0 Rs":
        textarea.insert(END, f'Cost of Dessert\t\t\t{PriceofDesserts}Rs.\n')

    textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs.\n')
    textarea.insert(END, f'Service tax\t\t\t{20}Rs.\n\n')
    textarea.insert(END, f'Total cost\t\t\t{subtotalofItems+20}Rs.\n')

    sendButton=Button(root2, text="Send", font=("arial", 19, "bold"), bg="black",fg="white",  bd=2, relief=GROOVE, command=send_msg)
    sendButton.pack(pady=5)

    root2.mainloop()

#Function Save
def Save():
    url= filedialog.asksaveasfile(mode="w", defaultextension=".txt")

    bill_data=textReceipt.get(1.0, END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo("Information", "Your bill is Ready!")

#functions receipt
def Receipt():
    global billnumber, date
    if costoffoodvar.get()!="" or costofdrinkvar.get()!="" or costofdessertvar.get()!="":
        textReceipt.delete(1.0, END)
        x = random.randint(100,10000)
        billnumber = "Bill"+str(x)
        date = time.strftime("%d/%m/%Y")
        textReceipt.insert(END, "Receipt Ref: \t\t" + billnumber+"\t"+date+"\n")
        textReceipt.insert(END, "***************************************************************\n")
        textReceipt.insert(END,"Items: \t\t Cost of Items(Rs.)\n")
        textReceipt.insert(END, "***************************************************************\n")

    # functions receipt Food
        if e_polRotti.get()!="0":
            textReceipt.insert(END, f'polRotti\t\t\t{int(e_polRotti.get())*40}\n\n')

        if e_Eggrotti.get()!="0":
            textReceipt.insert(END, f'Eggrotti\t\t\t{int(e_Eggrotti.get())*130}\n\n')

        if e_VegRotti.get()!="0":
            textReceipt.insert(END, f'VegRotti\t\t\t{int(e_VegRotti.get())*80}\n\n')

        if e_FishRolls.get()!="0":
            textReceipt.insert(END, f'FishRolls\t\t\t{int(e_FishRolls.get())*80}\n\n')

        if e_ChickenRolls.get()!="0":
            textReceipt.insert(END, f'ChickenRolls\t\t\t{int(e_ChickenRolls.get())*100}\n\n')

        if e_SlicedPizza.get()!="0":
            textReceipt.insert(END, f'SlicedPizza\t\t\t{int(e_SlicedPizza.get())*150}\n\n')

        if e_chickenSandwich.get()!="0":
            textReceipt.insert(END, f'chickenSandwich\t\t\t{int(e_chickenSandwich.get())*120}\n\n')

        if e_hotdog.get()!="0":
            textReceipt.insert(END, f'hotdog\t\t\t{int(e_hotdog.get())*150}\n\n')

        if e_seenisambolBread.get()!="0":
            textReceipt.insert(END, f'seenisambolBread\t\t\t{int(e_seenisambolBread.get())*130}\n\n')

        if e_Noodles.get()!="0":
            textReceipt.insert(END, f'Noodles\t\t\t{int(e_Noodles.get())*120}\n\n')

    # functions receipt Drinks
        if e_plaintea.get()!="0":
            textReceipt.insert(END, f'plaintea\t\t\t{int(e_plaintea.get())*30}\n\n')

        if e_Milktea.get()!="0":
            textReceipt.insert(END, f'Milktea\t\t\t{int(e_Milktea.get())*70}\n\n')

        if e_Gingertea.get()!="0":
            textReceipt.insert(END, f'Gingertea\t\t\t{int(e_Gingertea.get())*50}\n\n')

        if e_Milk.get()!="0":
            textReceipt.insert(END, f'Milk\t\t\t{int(e_Milk.get())*100}\n\n')

        if e_Coffee.get()!="0":
            textReceipt.insert(END, f'Coffee\t\t\t{int(e_Coffee.get())*90}\n\n')

        if e_IcedCoffee.get()!="0":
            textReceipt.insert(END, f'IcedCoffee\t\t\t{int(e_IcedCoffee.get())*130}\n\n')

        if e_Milo.get()!="0":
            textReceipt.insert(END, f'Milo\t\t\t{int(e_Milo.get())*130}\n\n')

        if e_SoftDrinks.get()!="0":
            textReceipt.insert(END, f'SoftDrinks\t\t\t{int(e_SoftDrinks.get())*80}\n\n')

        if e_Faluda.get()!="0":
            textReceipt.insert(END, f'Faluda\t\t\t{int(e_Faluda.get())*150}\n\n')

        if e_FruitJuice.get()!="0":
            textReceipt.insert(END, f'FruitJuice\t\t\t{int(e_FruitJuice.get())*120}\n\n')

    # functions receipt Desserts
        if e_CupIceCream.get()!="0":
            textReceipt.insert(END, f'CupIceCream\t\t\t{int(e_CupIceCream.get())*80}\n\n')

        if e_ConeIceCream.get()!="0":
            textReceipt.insert(END, f'ConeIceCream\t\t\t{int(e_ConeIceCream.get())*150}\n\n')

        if e_SlicedCake.get()!="0":
            textReceipt.insert(END, f'SlicedCake\t\t\t{int(e_SlicedCake.get())*100}\n\n')

        if e_CupCake.get()!="0":
            textReceipt.insert(END, f'CupCake\t\t\t{int(e_CupCake.get())*80}\n\n')

        if e_Cookies.get()!="0":
            textReceipt.insert(END, f'Cookies\t\t\t{int(e_Cookies.get())*80}\n\n')

        if e_Pudding.get()!="0":
            textReceipt.insert(END, f'Pudding\t\t\t{int(e_Pudding.get())*80}\n\n')

        if e_Wattalappam.get()!="0":
            textReceipt.insert(END, f'Wattalappam\t\t\t{int(e_Wattalappam.get())*120}\n\n')

        if e_FruitSalad.get()!="0":
            textReceipt.insert(END, f'FruitSalad\t\t\t{int(e_FruitSalad.get())*120}\n\n')

        if e_Biscuit.get()!="0":
            textReceipt.insert(END, f'Biscuit\t\t\t{int(e_Biscuit.get())*80}\n\n')

        if e_Chocolate.get()!="0":
            textReceipt.insert(END, f'Chocolate\t\t\t{int(e_Chocolate.get())*150}\n\n')

        textReceipt.insert(END, "***************************************************************\n")
        if costoffoodvar.get()!= "0 Rs":
            textReceipt.insert(END,f'Cost of Food\t\t\t{PriceofFood}Rs.\n\n')
        if costofdrinkvar.get() != "0 Rs":
            textReceipt.insert(END, f'Cost of Drinks\t\t\t{PriceofDrinks}Rs.\n\n')
        if costofdessertvar.get() != "0 Rs":
            textReceipt.insert(END, f'Cost of Dessert\t\t\t{PriceofDesserts}Rs.\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs.\n\n')
        textReceipt.insert(END, f'Service tax\t\t\t{20}Rs.\n\n')
        textReceipt.insert(END, f'Total cost\t\t\t{subtotalofItems+20}Rs.\n\n')
        textReceipt.insert(END, "***************************************************************\n")
    else:
        messagebox.showerror("Error")

#functions Total
def Totalcost():
    global PriceofFood, PriceofDrinks, PriceofDesserts, subtotalofItems, servicetax, totalcost
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or \
        var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or \
        var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or \
        var16.get()!=0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
        var25.get() != 0 or var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or \
        var29.get() != 0 or var30.get() != 0 or var31.get() != 0:

        item1 = int(e_polRotti.get())
        item2 = int(e_Eggrotti.get())
        item3 = int(e_VegRotti.get())
        item4 = int(e_FishRolls.get())
        item5 = int(e_ChickenRolls.get())
        item6 = int(e_SlicedPizza.get())
        item7 = int(e_chickenSandwich.get())
        item8 = int(e_hotdog.get())
        item9 = int(e_seenisambolBread.get())
        item10 = int(e_Noodles.get())

        item11 = int(e_plaintea.get())
        item12 = int(e_Milktea.get())
        item13 = int(e_Gingertea.get())
        item14 = int(e_Milk.get())
        item15 = int(e_Coffee.get())
        item16 = int(e_IcedCoffee.get())
        item17 = int(e_Milo.get())
        item18 = int(e_SoftDrinks.get())
        item19 = int(e_Faluda.get())
        item20 = int(e_FruitJuice.get())

        item21 = int(e_CupIceCream.get())
        item22 = int(e_ConeIceCream.get())
        item23 = int(e_SlicedCake.get())
        item24 = int(e_CupCake.get())
        item25 = int(e_Cookies.get())
        item26 = int(e_Pudding.get())
        item27 = int(e_Wattalappam.get())
        item28 = int(e_FruitSalad.get())
        item29 = int(e_Biscuit.get())
        item30 = int(e_Chocolate.get())

        PriceofFood=(item1*40)+(item2*130)+(item3*80)+(item4*80)+(item5*100)+(item6*150)+(item7*120)+(item8*150)\
                    + (item9*130)+(item10*120)

        PriceofDrinks=(item11 * 30) + (item12 * 70) + (item13 * 50) + (item14 * 100) + (item15 * 90) + (item16 * 130)\
                      + (item17 * 130) + (item18 * 80) + (item19 * 150) + (item20 * 120)

        PriceofDesserts=(item21*80)+(item22*150)+(item23*100)+(item24*80)+ (item25*80)+(item26*80)+(item27*120)\
                        + (item28*120)+(item29*80)+(item30*150)

        costoffoodvar.set(str(PriceofFood)+ "Rs.")
        costofdrinkvar.set(str(PriceofDrinks)+ "Rs.")
        costofdessertvar.set(str(PriceofDesserts)+ "Rs.")

        subtotalofItems=PriceofFood+PriceofDrinks+PriceofDesserts
        subtotalvar.set(str(subtotalofItems)+ "Rs.")

        servicetaxvar.set("20 Rs.")

        totalcost=subtotalofItems+20
        totalcostvar.set(str(totalcost)+ "Rs.")

    else:
        messagebox.showerror("Error", "No item is selected")


#functions Food

def polRotti():
    if var1.get()==1:
        textpolRotti.config(state=NORMAL)  #to become editable when we click
        textpolRotti.delete(0,END) #to remove 0, when we click
        textpolRotti.focus()
    else:
        textpolRotti.config(state=DISABLED)
        e_polRotti.set("0")

def Eggrotti():
    if var2.get()==1:
        textEggrotti.config(state=NORMAL)  #to become editable when we click
        textEggrotti.delete(0,END) #to remove 0, when we click
        textEggrotti.focus()
    else:
        textEggrotti.config(state=DISABLED)
        e_Eggrotti.set("0")

def VegRotti():
    if var3.get()==1:
        textVegRotti.config(state=NORMAL)  #to become editable when we click
        textVegRotti.delete(0,END) #to remove 0, when we click
        textVegRotti.focus()
    else:
        textVegRotti.config(state=DISABLED)
        e_VegRotti.set("0")

def FishRolls():
    if var4.get()==1:
        textFishRolls.config(state=NORMAL)  #to become editable when we click
        textFishRolls.delete(0,END) #to remove 0, when we click
        textFishRolls.focus()
    else:
        textFishRolls.config(state=DISABLED)
        e_FishRolls.set("0")

def ChickenRolls():
    if var5.get()==1:
        textChickenRolls.config(state=NORMAL)  #to become editable when we click
        textChickenRolls.delete(0,END) #to remove 0, when we click
        textChickenRolls.focus()
    else:
        textChickenRolls.config(state=DISABLED)
        e_ChickenRolls.set("0")

def SlicedPizza():
    if var6.get()==1:
        textSlicedPizza.config(state=NORMAL)  #to become editable when we click
        textSlicedPizza.delete(0,END) #to remove 0, when we click
        textSlicedPizza.focus()
    else:
        textSlicedPizza.config(state=DISABLED)
        e_SlicedPizza.set("0")

def chickenSandwich():
    if var7.get() == 1:
        textchickenSandwich.config(state=NORMAL)  # to become editable when we click
        textchickenSandwich.delete(0, END)  # to remove 0, when we click
        textchickenSandwich.focus()
    else:
        textchickenSandwich.config(state=DISABLED)
        e_chickenSandwich.set("0")

def hotdog():
    if var8.get() == 1:
        texthotdog.config(state=NORMAL)  # to become editable when we click
        texthotdog.delete(0, END)  # to remove 0, when we click
        texthotdog.focus()
    else:
        texthotdog.config(state=DISABLED)
        e_hotdog.set("0")

def seenisambolBread():
    if var9.get() == 1:
        textseenisambolBread.config(state=NORMAL)  # to become editable when we click
        textseenisambolBread.delete(0, END)  # to remove 0, when we click
        textseenisambolBread.focus()
    else:
        textseenisambolBread.config(state=DISABLED)
        e_seenisambolBread.set("0")

def Noodles():
    if var10.get()==1:
        textNoodles.config(state=NORMAL)  #to become editable when we click
        textNoodles.delete(0,END) #to remove 0, when we click
        textNoodles.focus()
    else:
        textNoodles.config(state=DISABLED)
        e_Noodles.set("0")


#functions Drinks
def plaintea():
    if var12.get()==1:
        textplaintea.config(state=NORMAL)  #to become editable when we click
        textplaintea.delete(0,END) #to remove 0, when we click
        textplaintea.focus()
    else:
        textplaintea.config(state=DISABLED)
        e_plaintea.set("0")

def Milktea():
    if var13.get() == 1:
        textMilktea.config(state=NORMAL)  # to become editable when we click
        textMilktea.delete(0, END)  # to remove 0, when we click
        textMilktea.focus()
    else:
        textMilktea.config(state=DISABLED)
        e_Milktea.set("0")

def Gingertea():
    if var14.get() == 1:
        textGingertea.config(state=NORMAL)  # to become editable when we click
        textGingertea.delete(0, END)  # to remove 0, when we click
        textGingertea.focus()
    else:
        textGingertea.config(state=DISABLED)
        e_Gingertea.set("0")

def Milk():
    if var15.get() == 1:
        textMilk.config(state=NORMAL)  # to become editable when we click
        textMilk.delete(0, END)  # to remove 0, when we click
        textMilk.focus()
    else:
        textMilk.config(state=DISABLED)
        e_Milk.set("0")

def Coffee():
    if var16.get() == 1:
        textCoffee.config(state=NORMAL)  # to become editable when we click
        textCoffee.delete(0, END)  # to remove 0, when we click
        textCoffee.focus()
    else:
        textCoffee.config(state=DISABLED)
        e_Coffee.set("0")

def IcedCoffee():
    if var17.get() == 1:
        textIcedCoffee.config(state=NORMAL)  # to become editable when we click
        textIcedCoffee.delete(0, END)  # to remove 0, when we click
        textIcedCoffee.focus()
    else:
        textIcedCoffee.config(state=DISABLED)
        e_IcedCoffee.set("0")

def Milo():
    if var18.get() == 1:
        textMilo.config(state=NORMAL)  # to become editable when we click
        textMilo.delete(0, END)  # to remove 0, when we click
        textMilo.focus()
    else:
        textMilo.config(state=DISABLED)
        e_Milo.set("0")

def SoftDrinks():
    if var19.get() == 1:
        textSoftDrinks.config(state=NORMAL)  # to become editable when we click
        textSoftDrinks.delete(0, END)  # to remove 0, when we click
        textSoftDrinks.focus()
    else:
        textSoftDrinks.config(state=DISABLED)
        e_SoftDrinks.set("0")

def Faluda():
    if var20.get() == 1:
        textFaluda.config(state=NORMAL)  # to become editable when we click
        textFaluda.delete(0, END)  # to remove 0, when we click
        textFaluda.focus()
    else:
        textFaluda.config(state=DISABLED)
        e_Faluda.set("0")

def FruitJuice():
    if var21.get() == 1:
        textFruitJuice.config(state=NORMAL)  # to become editable when we click
        textFruitJuice.delete(0, END)  # to remove 0, when we click
        textFruitJuice.focus()
    else:
        textFruitJuice.config(state=DISABLED)
        e_FruitJuice.set("0")


#functions Desserts
def CupIceCream():
    if var22.get() == 1:
        textCupIceCream.config(state=NORMAL)  # to become editable when we click
        textCupIceCream.delete(0, END)  # to remove 0, when we click
        textCupIceCream.focus()
    else:
        textCupIceCream.config(state=DISABLED)
        e_CupIceCream.set("0")

def ConeIceCream():
    if var23.get() == 1:
        textConeIceCream.config(state=NORMAL)  # to become editable when we click
        textConeIceCream.delete(0, END)  # to remove 0, when we click
        textConeIceCream.focus()
    else:
        textConeIceCream.config(state=DISABLED)
        e_ConeIceCream.set("0")

def SlicedCake():
    if var24.get() == 1:
        textSlicedCake.config(state=NORMAL)  # to become editable when we click
        textSlicedCake.delete(0, END)  # to remove 0, when we click
        textSlicedCake.focus()
    else:
        textSlicedCake.config(state=DISABLED)
        e_SlicedCake.set("0")

def CupCake():
    if var25.get() == 1:
        textCupCake.config(state=NORMAL)  # to become editable when we click
        textCupCake.delete(0, END)  # to remove 0, when we click
        textCupCake.focus()
    else:
        textCupCake.config(state=DISABLED)
        e_CupCake.set("0")

def Cookies():
    if var26.get() == 1:
        textCookies.config(state=NORMAL)  # to become editable when we click
        textCookies.delete(0, END)  # to remove 0, when we click
        textCookies.focus()
    else:
        textCookies.config(state=DISABLED)
        e_Cookies.set("0")

def Pudding():
    if var27.get() == 1:
        textPudding.config(state=NORMAL)  # to become editable when we click
        textPudding.delete(0, END)  # to remove 0, when we click
        textPudding.focus()
    else:
        textPudding.config(state=DISABLED)
        e_Pudding.set("0")

def Wattalappam():
    if var28.get() == 1:
        textWattalappam.config(state=NORMAL)  # to become editable when we click
        textWattalappam.delete(0, END)  # to remove 0, when we click
        textWattalappam.focus()
    else:
        textWattalappam.config(state=DISABLED)
        e_Wattalappam.set("0")

def FruitSalad():
    if var29.get() == 1:
        textFruitSalad.config(state=NORMAL)  # to become editable when we click
        textFruitSalad.delete(0, END)  # to remove 0, when we click
        textFruitSalad.focus()
    else:
        textFruitSalad.config(state=DISABLED)
        e_FruitSalad.set("0")

def Biscuit():
    if var30.get() == 1:
        textBiscuit.config(state=NORMAL)  # to become editable when we click
        textBiscuit.delete(0, END)  # to remove 0, when we click
        textBiscuit.focus()
    else:
        textBiscuit.config(state=DISABLED)
        e_Biscuit.set("0")

def Chocolate():
    if var31.get() == 1:
        textChocolate.config(state=NORMAL)  # to become editable when we click
        textChocolate.delete(0, END)  # to remove 0, when we click
        textChocolate.focus()
    else:
        textChocolate.config(state=DISABLED)
        e_Chocolate.set("0")



root = Tk()

root.geometry("1480x700+0+0")
root.resizable(0, 0)

#Frame.Title

root.title("Taste Trove")
root.config(bg="cornsilk3")

topFrame=Frame(root, bd=1, relief=GROOVE, bg="bisque3")
topFrame.pack(side="top")

labelTitle = Label(topFrame, text="Taste Trove", font=("Times", 50, "bold italic"), fg="black",
                   bd=1, bg="bisque3", width=20)
labelTitle.grid(row=0, column=0)

labelTitle1 = Label(topFrame, text="Place your orders here!", font=("Times", 25, "bold italic"), fg="black",
                   bd=1, bg="bisque3", width=20)
labelTitle1.grid(row=1, column=0)


#Frame.Menu

menuFrame=Frame(root, bd=2, relief=GROOVE, bg="cornsilk3")
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame, bd=2, relief=GROOVE, bg="darkgray", pady=10)
costFrame.pack(side=BOTTOM)

foodframe=LabelFrame(menuFrame, text="Food", font=("times", 19, "bold"), bd=2, relief=GROOVE, fg="blue4")
foodframe.pack(side=LEFT)

drinksframe=LabelFrame(menuFrame, text="Beverage", font=("times", 19, "bold"), bd=2, relief=GROOVE, fg="blue4")
drinksframe.pack(side=LEFT)

cakesframe=LabelFrame(menuFrame, text="Desserts", font=("times", 19, "bold"), bd=2, relief=GROOVE, fg="blue4")
cakesframe.pack(side=LEFT)

#Frame.Right

rightFrame=Frame(root, bd=2, relief=GROOVE, bg="cornsilk3")
rightFrame.pack(side=RIGHT)

recieptFrame=Frame(rightFrame, bd=2, relief=GROOVE, bg="cornsilk3")
recieptFrame.pack()

buttonFrame=Frame(rightFrame, bd=2, relief=GROOVE, bg="cornsilk3")
buttonFrame.pack()

##Variable
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()
var17= IntVar()
var18= IntVar()
var19= IntVar()
var20= IntVar()
var21= IntVar()
var22= IntVar()
var23= IntVar()
var24= IntVar()
var25= IntVar()
var26= IntVar()
var27= IntVar()
var28= IntVar()
var29= IntVar()
var30= IntVar()
var31= IntVar()


e_polRotti= StringVar()
e_Eggrotti= StringVar()
e_VegRotti= StringVar()
e_FishRolls= StringVar()
e_ChickenRolls= StringVar()
e_SlicedPizza= StringVar()
e_chickenSandwich= StringVar()
e_hotdog= StringVar()
e_seenisambolBread= StringVar()
e_Noodles= StringVar()

e_plaintea= StringVar()
e_Milktea = StringVar()
e_Gingertea = StringVar()
e_Milk = StringVar()
e_Coffee = StringVar()
e_IcedCoffee = StringVar()
e_Milo = StringVar()
e_SoftDrinks = StringVar()
e_Faluda = StringVar()
e_FruitJuice = StringVar()

e_CupIceCream = StringVar()
e_ConeIceCream = StringVar()
e_SlicedCake = StringVar()
e_CupCake = StringVar()
e_Cookies = StringVar()
e_Pudding = StringVar()
e_Wattalappam = StringVar()
e_FruitSalad = StringVar()
e_Biscuit = StringVar()
e_Chocolate = StringVar()

costoffoodvar=StringVar()
costofdrinkvar=StringVar()
costofdessertvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

#setting zero

e_polRotti.set("0")
e_Eggrotti.set("0")
e_VegRotti.set("0")
e_FishRolls.set("0")
e_ChickenRolls.set("0")
e_SlicedPizza.set("0")
e_chickenSandwich.set("0")
e_hotdog.set("0")
e_seenisambolBread.set("0")
e_Noodles.set("0")

e_plaintea.set("0")
e_Milktea .set("0")
e_Gingertea .set("0")
e_Milk .set("0")
e_Coffee .set("0")
e_IcedCoffee .set("0")
e_Milo .set("0")
e_SoftDrinks .set("0")
e_Faluda .set("0")
e_FruitJuice .set("0")

e_CupIceCream.set("0")
e_ConeIceCream.set("0")
e_SlicedCake.set("0")
e_CupCake.set("0")
e_Cookies.set("0")
e_Pudding.set("0")
e_Wattalappam.set("0")
e_FruitSalad.set("0")
e_Biscuit.set("0")
e_Chocolate.set("0")




##Food

polRotti=Checkbutton(foodframe, text="Pol Rotti", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var1, command=polRotti)
polRotti.grid(row=0, column=0, sticky=W)
#W=West
polRotti=Label(foodframe, text="Rs.40", font=("arial",18, "bold"))
polRotti.grid(row=0, column=1, sticky=W)

Eggrotti=Checkbutton(foodframe, text="Egg Rotti", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var2, command=Eggrotti)
Eggrotti.grid(row=1, column=0, sticky=W)
Eggrotti=Label(foodframe, text="Rs.130", font=("arial",18, "bold"))
Eggrotti.grid(row=1, column=1, sticky=W)

VegRotti=Checkbutton(foodframe, text="Veg Rotti", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var3, command=VegRotti)
VegRotti.grid(row=2, column=0, sticky=W)
Vegrotti=Label(foodframe, text="Rs.80", font=("arial",18, "bold"))
Vegrotti.grid(row=2, column=1, sticky=W)

FishRolls=Checkbutton(foodframe, text="Fish Rolls", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var4, command=FishRolls)
FishRolls.grid(row=3, column=0, sticky=W)
FishRolls=Label(foodframe, text="Rs.80", font=("arial",18, "bold"))
FishRolls.grid(row=3, column=1, sticky=W)

ChickenRolls=Checkbutton(foodframe, text="Chicken Rolls", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var5, command=ChickenRolls)
ChickenRolls.grid(row=4, column=0, sticky=W)
ChickenRolls=Label(foodframe, text="Rs.100", font=("arial",18, "bold"))
ChickenRolls.grid(row=4, column=1, sticky=W)

SlicedPizza=Checkbutton(foodframe, text="Sliced Pizza", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var6, command=SlicedPizza)
SlicedPizza.grid(row=5, column=0, sticky=W)
SlicedPizza=Label(foodframe, text="Rs.150", font=("arial",18, "bold"))
SlicedPizza.grid(row=5, column=1, sticky=W)

chickenSandwich=Checkbutton(foodframe, text="chic Sandwich", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var7, command=chickenSandwich)
chickenSandwich.grid(row=6, column=0, sticky=W)
chickenSandwich=Label(foodframe, text="Rs.120", font=("arial",18, "bold"))
chickenSandwich.grid(row=6, column=1, sticky=W)

hotdog=Checkbutton(foodframe, text="Hot dog", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var8, command=hotdog)
hotdog.grid(row=7, column=0, sticky=W)
hotdog=Label(foodframe, text="Rs.150", font=("arial",18, "bold"))
hotdog.grid(row=7, column=1, sticky=W)

seenisambolBread=Checkbutton(foodframe, text="Bread", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var9, command=seenisambolBread)
seenisambolBread.grid(row=8, column=0, sticky=W)
seenisambolBread=Label(foodframe, text="Rs.130", font=("arial",18, "bold"))
seenisambolBread.grid(row=8, column=1, sticky=W)

Noodles=Checkbutton(foodframe, text="Noodles", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var10, command=Noodles)
Noodles.grid(row=9, column=0, sticky=W)
Noodles=Label(foodframe, text="Rs.120", font=("arial",18, "bold"))
Noodles.grid(row=9, column=1, sticky=W)

#Entry fields for food item

textpolRotti=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_polRotti)
textpolRotti.grid(row=0, column=2)

textEggrotti=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Eggrotti)
textEggrotti.grid(row=1, column=2)

textVegRotti=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_VegRotti)
textVegRotti.grid(row=2, column=2)

textFishRolls=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_FishRolls)
textFishRolls.grid(row=3, column=2)

textChickenRolls=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_ChickenRolls)
textChickenRolls.grid(row=4, column=2)

textSlicedPizza=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_SlicedPizza)
textSlicedPizza.grid(row=5, column=2)

textchickenSandwich=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_chickenSandwich)
textchickenSandwich.grid(row=6, column=2)

texthotdog=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_hotdog)
texthotdog.grid(row=7, column=2)

textseenisambolBread=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_seenisambolBread)
textseenisambolBread.grid(row=8, column=2)

textNoodles=Entry(foodframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Noodles)
textNoodles.grid(row=9, column=2)


#Drinks

plaintea=Checkbutton(drinksframe, text="Plain tea", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var12, command=plaintea)
plaintea.grid(row=0, column=0, sticky=W)
plaintea=Label(drinksframe, text="Rs.30 ", font=("arial",18, "bold"))
plaintea.grid(row=0, column=1, sticky=W)

Milktea=Checkbutton(drinksframe, text="Milk tea", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var13, command=Milktea)
Milktea.grid(row=1, column=0, sticky=W)
Milktea=Label(drinksframe, text="Rs.70 ", font=("arial",18, "bold"))
Milktea.grid(row=1, column=1, sticky=W)

Gingertea=Checkbutton(drinksframe, text="Ginger tea", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var14, command=Gingertea)
Gingertea.grid(row=2, column=0, sticky=W)
Gingertea=Label(drinksframe, text="Rs.50 ", font=("arial",18, "bold"))
Gingertea.grid(row=2, column=1, sticky=W)

Milk=Checkbutton(drinksframe, text="Milk", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var15, command=Milk)
Milk.grid(row=3, column=0, sticky=W)
Milk=Label(drinksframe, text="Rs.100 ", font=("arial",18, "bold"))
Milk.grid(row=3, column=1, sticky=W)

Coffee=Checkbutton(drinksframe, text="Coffee", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var16, command=Coffee)
Coffee.grid(row=4, column=0, sticky=W)
Coffee=Label(drinksframe, text="Rs.90 ", font=("arial",18, "bold"))
Coffee.grid(row=4, column=1, sticky=W)

IcedCoffee=Checkbutton(drinksframe, text="Iced Coffee", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var17, command=IcedCoffee)
IcedCoffee.grid(row=5, column=0, sticky=W)
IcedCoffee=Label(drinksframe, text="Rs.130 ", font=("arial",18, "bold"))
IcedCoffee.grid(row=5, column=1, sticky=W)

Milo=Checkbutton(drinksframe, text="Milo", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var18, command=Milo)
Milo.grid(row=6, column=0, sticky=W)
Milo=Label(drinksframe, text="Rs.130 ", font=("arial",18, "bold"))
Milo.grid(row=6, column=1, sticky=W)

SoftDrinks=Checkbutton(drinksframe, text="Soft Drinks", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var19, command=SoftDrinks)
SoftDrinks.grid(row=7, column=0, sticky=W)
SoftDrinks=Label(drinksframe, text="Rs.80 ", font=("arial",18, "bold"))
SoftDrinks.grid(row=7, column=1, sticky=W)

Faluda=Checkbutton(drinksframe, text="Faluda", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var20, command=Faluda)
Faluda.grid(row=8, column=0, sticky=W)
Faluda=Label(drinksframe, text="Rs.150 ", font=("arial",18, "bold"))
Faluda.grid(row=8, column=1, sticky=W)

FruitJuice=Checkbutton(drinksframe, text="Fruit Juice", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var21, command=FruitJuice)
FruitJuice.grid(row=9, column=0, sticky=W)
FruitJuice=Label(drinksframe, text="Rs.120 ", font=("arial",18, "bold"))
FruitJuice.grid(row=9, column=1, sticky=W)

#Entry fields for drink item

textplaintea=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_plaintea)
textplaintea.grid(row=0, column=2)

textMilktea=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Milktea)
textMilktea.grid(row=1, column=2)

textGingertea=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Gingertea)
textGingertea.grid(row=2, column=2)

textMilk=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Milk)
textMilk.grid(row=3, column=2)

textCoffee=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Coffee)
textCoffee.grid(row=4, column=2)

textIcedCoffee=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_IcedCoffee)
textIcedCoffee.grid(row=5, column=2)

textMilo=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Milo)
textMilo.grid(row=6, column=2)

textSoftDrinks=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_SoftDrinks)
textSoftDrinks.grid(row=7, column=2)

textFaluda=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Faluda)
textFaluda.grid(row=8, column=2)

textFruitJuice=Entry(drinksframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_FruitJuice)
textFruitJuice.grid(row=9, column=2)


#Desserts

CupIceCream=Checkbutton(cakesframe, text="Cup IceCream", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var22, command=CupIceCream)
CupIceCream.grid(row=0, column=0, sticky=W)
CupIceCream=Label(cakesframe, text="Rs.80", font=("arial",18, "bold"))
CupIceCream.grid(row=0, column=1, sticky=W)

ConeIceCream=Checkbutton(cakesframe, text="Cone IceCream", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var23, command=ConeIceCream)
ConeIceCream.grid(row=1, column=0, sticky=W)
ConeIceCream=Label(cakesframe, text="Rs.150", font=("arial",18, "bold"))
ConeIceCream.grid(row=1, column=1, sticky=W)

SlicedCake=Checkbutton(cakesframe, text="Sliced Cake", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var24, command=SlicedCake)
SlicedCake.grid(row=2, column=0, sticky=W)
SlicedCake=Label(cakesframe, text="Rs.100", font=("arial",18, "bold"))
SlicedCake.grid(row=2, column=1, sticky=W)

CupCake=Checkbutton(cakesframe, text="Cup Cake", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var25, command=CupCake)
CupCake.grid(row=3, column=0, sticky=W)
CupCake=Label(cakesframe, text="Rs.80", font=("arial",18, "bold"))
CupCake.grid(row=3, column=1, sticky=W)

Cookies=Checkbutton(cakesframe, text="Cookies", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var26, command=Cookies)
Cookies.grid(row=4, column=0, sticky=W)
Cookies=Label(cakesframe, text="Rs.80", font=("arial",18, "bold"))
Cookies.grid(row=4, column=1, sticky=W)

Pudding=Checkbutton(cakesframe, text="Pudding", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var27, command=Pudding)
Pudding.grid(row=5, column=0, sticky=W)
Pudding=Label(cakesframe, text="Rs.80", font=("arial",18, "bold"))
Pudding.grid(row=5, column=1, sticky=W)

Wattalappam=Checkbutton(cakesframe, text="Wattalappam", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var28, command=Wattalappam)
Wattalappam.grid(row=6, column=0, sticky=W)
Wattalappam=Label(cakesframe, text="Rs.120", font=("arial",18, "bold"))
Wattalappam.grid(row=6, column=1, sticky=W)

FruitSalad=Checkbutton(cakesframe, text="Fruit Salad", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var29, command=FruitSalad)
FruitSalad.grid(row=7, column=0, sticky=W)
FruitSalad=Label(cakesframe, text="Rs.120", font=("arial",18, "bold"))
FruitSalad.grid(row=7, column=1, sticky=W)

Biscuit=Checkbutton(cakesframe, text="Biscuit", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var30, command=Biscuit)
Biscuit.grid(row=8, column=0, sticky=W)
Biscuit=Label(cakesframe, text="Rs.80", font=("arial",18, "bold"))
Biscuit.grid(row=8, column=1, sticky=W)

Chocolate=Checkbutton(cakesframe, text="Chocolate", font=("arial",18, "bold"), onvalue=1, offvalue=0, variable=var31, command=Chocolate)
Chocolate.grid(row=9, column=0, sticky=W)
Chocolate=Label(cakesframe, text="Rs.150", font=("arial",18, "bold"))
Chocolate.grid(row=9, column=1, sticky=W)

#Entry fields for desserts

textCupIceCream=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_CupIceCream)
textCupIceCream.grid(row=0, column=2)

textConeIceCream=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_ConeIceCream)
textConeIceCream.grid(row=1, column=2)

textSlicedCake=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_SlicedCake)
textSlicedCake.grid(row=2, column=2)

textCupCake=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_CupCake)
textCupCake.grid(row=3, column=2)

textCookies=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Cookies)
textCookies.grid(row=4, column=2)

textPudding=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Pudding)
textPudding.grid(row=5, column=2)

textWattalappam=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Wattalappam)
textWattalappam.grid(row=6, column=2)

textFruitSalad=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_FruitSalad)
textFruitSalad.grid(row=7, column=2)

textBiscuit=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Biscuit)
textBiscuit.grid(row=8, column=2)

textChocolate=Entry(cakesframe, font=("arial",18, "bold"), bd=1, width=6,
                   state=DISABLED, textvariable=e_Chocolate)
textChocolate.grid(row=9, column=2)


#Cost lables & entry fields
labelCostofFood=Label(costFrame, text="Cost of Foods", font=("arial", 16, "bold"), bg="cornsilk3")
labelCostofFood.grid(row=0, column=0, sticky=W)

textCostofFood=Entry(costFrame, font=("arial",16, "bold"), bd=2, width=14, state="readonly", textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1, padx=41)

labelCostofDrinks=Label(costFrame, text="Cost of Drinks", font=("arial", 16, "bold"), bg="cornsilk3")
labelCostofDrinks.grid(row=1, column=0, sticky=W)

textCostofDrinks=Entry(costFrame, font=("arial",16, "bold"), bd=2, width=14, state="readonly", textvariable=costofdrinkvar)
textCostofDrinks.grid(row=1, column=1, padx=41)

labelCostofDesserts=Label(costFrame, text="Cost of Desserts", font=("arial", 16, "bold"), bg="cornsilk3")
labelCostofDesserts.grid(row=2, column=0, sticky=W)

textCostofDesserts=Entry(costFrame, font=("arial",16, "bold"), bd=2, width=14, state="readonly", textvariable=costofdessertvar)
textCostofDesserts.grid(row=2, column=1, padx=41)


#entry fields of sub total
labelSubTotal=Label(costFrame, text="Sub Total", font=("arial", 16, "bold"), bg="cornsilk3")
labelSubTotal.grid(row=0, column=2, sticky=E)

textSubTotal=Entry(costFrame, font=("arial",16, "bold"), bd=2, width=14, state="readonly", textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=41)

#entry fields of Service Tax
labelServiceTax=Label(costFrame, text="Service Tax", font=("arial", 16, "bold"), bg="cornsilk3")
labelServiceTax.grid(row=1, column=2, sticky=E)

textServiceTax=Entry(costFrame, font=("arial", 16, "bold"), bd=2, width=14, state="readonly",textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=41)

#entry fields of Total Cost
labelTotalCost=Label(costFrame, text="Total Cost", font=("arial", 16, "bold"), bg="cornsilk3")
labelTotalCost.grid(row=2, column=2, sticky=E)

textTotalCost=Entry(costFrame, font=("arial",16, "bold"), bd=2, width=14,state="readonly", textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=41)


#Buttons
buttonTotal=Button(buttonFrame, text="Total", font=("arial", 14, "bold"), fg="black", bg="cornsilk3", bd=3, padx=3, command=Totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt=Button(buttonFrame, text="Receipt", font=("arial", 14, "bold"), fg="black", bg="cornsilk3", bd=3, padx=3, command=Receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave=Button(buttonFrame, text="Save", font=("arial", 14, "bold"), fg="black", bg="cornsilk3", bd=3, padx=3, command=Save)
buttonSave.grid(row=0, column=2)

buttonSend=Button(buttonFrame, text="Send", font=("arial", 14, "bold"), fg="black", bg="cornsilk3", bd=3, padx=3, command=Send)
buttonSend.grid(row=0, column=3)

buttonReset=Button(buttonFrame, text="Reset", font=("arial", 14, "bold"), fg="black", bg="cornsilk3", bd=3, padx=3, command=Reset)
buttonReset.grid(row=0, column=4)

#textarea for receipt
textReceipt=Text(recieptFrame, font=("arial",12, "bold"), bd=3, width=42, height=27)
textReceipt.grid(row=0, column=0)

root.mainloop()