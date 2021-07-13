from tkinter import *
from typing import Counter
import time 

root = Tk()
root.title("shitty clicker 2021")
root.geometry("900x200")


count = 0
cookie = 0
jar = 0
fakecount = 0
roundedCount = 0
upgradeAmount = 1
numberOfDeath = 0
showCookies = False
showJars = False
showShop = False

def clickUpgrade():
    global upgradeAmount
    global cookie
    cookie -= 1
    if upgradeAmount == 1:
        upgradeAmount = 10
    else:
        upgradeAmount += 10

    upgrades = Label(root, text=f"you have {upgradeAmount} extra clicks!")
    upgrades.grid(row=3, column=5)

    root.update()

def clickCounter():

    global fakecount
    global numberOfDeath
    global roundedCount
    global showShop
    global showCookies
    global showJars
    global jar
    global cookie
    global count
    count = count + upgradeAmount
    fakecount = fakecount + upgradeAmount

    Clicks = Label(root, text=f"you have clicked {count} times")
    achievement1 = Label(root, text=f"congrats! you have reached {count} clicks! have this cookie 🍪")
    Cookies = Label(root, text=f"you have {cookie} cookie(s)!")
    achievement2 = Label(root, text=f"wow! you reached {cookie} cookies? you need a cookie jar for that much")
    jars = Label(root, text=f"You have {jar} jar(s)!")
    shop = Label(root, text="Welcome to the shop!", font=("Arial",20,""))
    shop_clickUpgrade = Button(root, text="+10 clicks", command=clickUpgrade, padx=30, bg="#23272A", fg="#7289DA", font=("Arial",20,""))

    if fakecount >= 100:
        fakecount = 0
        cookie += 1
        showCookies = True
        showShop = True

        if cookie % 5 == 0:

            jar += 1
            showJars = True
    
    numberOfDeath = 0
    
    if showCookies:
        Cookies.grid(row=3, column=2)
        achievement1.grid(row=3)

    if showShop:
        shop.grid(row=1, column=5)
        shop_clickUpgrade.grid(row=2, column=5)
        
    if showJars:
        achievement2.grid(row=4)
        jars.grid(row=4, column=2)

    Clicks.grid(row=2, column=2)
    

#creating a button widget
myButton = Button(root, text="button belike", padx=100, pady=30, command=clickCounter, bg="#23272A", fg="#7289DA", font=("Arial",20,""))

#putting onto screen
myButton.grid(row=2, column=0, columnspan=2)

root.mainloop()