#Possibly Normallotto with 6 numbers and 1 superzahl (maybe a menu beforehand to choose which mode to choose)
#DONE: Remove random junk
#DONE, global variable countnum that counts how many numbers were already pressed
#DONE: Compare the lottery ticket to the current one and do the same for the superzahlen
#DONE: check if the user finished submitting the normal numbers and the superzahlen and only then the generate_Number works, disable textboxes

#The GUI
import tkinter as tk
#RNG
import random
#for showing up errors and win/lose outcome
from tkinter import messagebox

#Global vars

button_values = []
sup_values = []
lotto_values = []
lottosup_values = []

button6a49_values = []
sup6a49 = 0
lotto6a49_values = []
lotto6a49sup = 0
countnum = 0
countsup = 0
countlot = 0
countlotsup = 0


countnum6 = 0
countsup6 = 0
count6a49 = 0
count6a49sup = 0
wonnum = 0
wonsup = 0
lottoOK = False
supOK = False
l6a49OK = False
lsupOK = False
won6a49 = 0
wonsup6a49 = 0


#function of generating the numbers for lotto and showing the outcome
def playLottery():
    global button_values, sup_values, lotto_values, lottosup_values, countlot, countsup, countlotsup, lottoOK, supOK, wonnum, wonsup
    textbox3.config(state='normal')
    textbox4.config(state='normal')
    if lottoOK == True and supOK == True:
        while countlot < 5:
            rng = random.randrange(1, 51)
            if (rng not in lotto_values):
                lotto_values.append(rng)
                textbox3.insert(tk.END, f"{rng}    ")
                countlot = countlot + 1
        while countlotsup < 2:
            rng = random.randrange(1, 13)
            if (rng not in lottosup_values):
                lottosup_values.append(rng)
                textbox4.insert(tk.END, f"{rng}    ")
                countlotsup = countlotsup + 1
        for element in button_values:
            if element in lotto_values:
                wonnum = wonnum + 1
        for element in sup_values:
            if element in lottosup_values:
                wonsup = wonsup + 1
        if wonnum >= 2 and wonsup >= 1:
            messagebox.showinfo("GEWONNEN!",f"Herzlichhen Glückwünsch, Sie haben gewonnen! {wonnum} Zahlen und {wonsup} Superzahlen stimmen überein!")
        else:
            messagebox.showinfo("VERLOREN!",f"Leider stimmen nur {wonnum} Zahl/en und {wonsup} Superzahl/en überein, Sie haben verloren!")
        buttonGenerate.config(state='disabled')
    elif lottoOK == False:
        messagebox.showerror(title="Error!", message=f"Sie haben nicht vollständig die 5 Lottozahlen eingegeben!")
    elif supOK == False:
        messagebox.showerror(title="Error!", message=f"Sie haben nicht vollständig die 2 Superzahlen eingegeben!")
    textbox3.config(state='disabled')
    textbox4.config(state='disabled')

    print(f"{lotto_values}")

def generate6aus49():
    global button6a49_values, sup6a49, lotto6a49_values, lotto6a49sup, countnum6, countsup6, count6a49sup, countlotsup, l6a49OK, lsupOK, won6a49, wonsup6a49
    textbox5_.config(state='normal')
    textbox6_.config(state='normal')
    if lsupOK == True:
        while countnum6 < 6:
            rng = random.randrange(1, 50)
            if (rng not in lotto6a49_values):
                lotto6a49_values.append(rng)
                textbox5_.insert(tk.END, f"{rng}    ")
                countnum6 = countnum6 + 1
        while count6a49sup  < 1:
            rng = random.randrange(0, 10)
            lottosup6a49 = rng
            textbox6_.insert(tk.END, f"{rng}    ")
            count6a49sup  = count6a49sup  + 1
        for element in button6a49_values:
            if element in button6a49_values:
                won6a49 = wonsup6a49 + 1
            if lottosup6a49 == sup6a49:
                wonsup6a49 = 1
        if won6a49 + wonsup6a49 >= 3:
            messagebox.showinfo("GEWONNEN!",
                                f"Herzlichhen Glückwünsch, Sie haben gewonnen! {won6a49} Zahlen und {wonsup6a49} Superzahlen stimmen überein!")
        else:
            messagebox.showinfo("VERLOREN!",
                                f"Leider stimmen nur {won6a49} Zahl/en und {wonsup6a49} Superzahl/en überein, Sie haben verloren!")
        buttonGenerate.config(state='disabled')
    elif l6a49OK == False:
        messagebox.showerror(title="Error!", message=f"Sie haben nicht vollständig die 6 Lottozahlen eingegeben!")
    elif lsupOK == False:
        messagebox.showerror(title="Error!", message=f"Sie haben nicht vollständig die 2 Superzahlen eingegeben!")
    textbox3.config(state='disabled')
    textbox4.config(state='disabled')



#GUI Elements placement
root = tk.Tk()
root.title("Lottozahlen")
root.geometry("1600x600")
labellot = tk.Label(root, text="Euroticket eingeben (5 Zahlen):", height=1, font=("Arial", 14))
labellot.place(x=20, y=20)
label = tk.Label(root, text="Ihren Lottoticket:", height=1, font=("Arial", 14))
label.place(x=420, y=20)
textbox1 = tk.Text(root, height=1, width=18, font=("Arial", 14))
textbox1.place(x=420, y=50)
textbox1.config(state='disabled')
textbox2 = tk.Text(root, height=1, width=8, font=("Arial", 14))
textbox2.place(x=420, y=270)
textbox2.config(state='disabled')
check_state = tk.IntVar()
labelsup = tk.Label(root, text="2 Superzahlen eingeben:", height=1, font=("Arial", 14))
labelsup.place(x=10, y=240)
labelsup2 = tk.Label(root, text="Ihren 2 Superzahlen", height=1, font=("Arial", 14))
labelsup2.place(x=420, y=240)
labellot2 = tk.Label(root, text="Die Lottozahlen:", height=1, font=("Arial", 14))
labellot2.place(x=60, y=420)
labellot3 = tk.Label(root, text="Die Superzahlen:", height=1, font=("Arial", 14))
labellot3.place(x= 60, y=460)
textbox3 = tk.Text(root, height=1, width=20, font=("Arial", 14))
textbox3.place(x=210, y=420)
textbox3.config(state='disabled')
textbox4 = tk.Text(root, height=1, width=20, font=("Arial", 14))
textbox4.place(x=210, y=460)
textbox4.config(state='disabled')

#for normal lotto:
labellot = tk.Label(root, text="Euroticket eingeben (5 Zahlen):", height=1, font=("Arial", 14))
labellot.place(x=20, y=20)
label_ = tk.Label(root, text="Ihren Lottoticket:", height=1, font=("Arial", 14))
label_.place(x= 1200, y=20)
textbox1_ = tk.Text(root, height=1, width=24, font=("Arial", 14))
textbox1_.place(x=1200, y=50)
textbox1_.config(state='disabled')
textbox2_ = tk.Text(root, height=1, width=8, font=("Arial", 14))
textbox2_.place(x=1200, y=270)
textbox2_.config(state='disabled')
check_state = tk.IntVar()
labellot_ = tk.Label(root, text="6AUS49 Ticket eingeben (6 Zahlen):", height=1, font=("Arial", 14))
labellot_.place(x= 750, y = 20)
labelsup_ = tk.Label(root, text="2 Superzahlen eingeben:", height=1, font=("Arial", 14))
labelsup_.place(x=10, y=240)
labelsup2_ = tk.Label(root, text="Ihren Superzahl eingeben:", height=1, font=("Arial", 14))
labelsup2_.place(x=750, y=240)
labellot3 = tk.Label(root, text="Ihren Superzahl:", height=1, font=("Arial", 14))
labellot3.place(x= 1200, y=240)
labellot2_ = tk.Label(root, text="Die Lottozahlen:", height=1, font=("Arial", 14))
labellot2_.place(x=800, y=420)
labellot3_ = tk.Label(root, text="Der Superzahl:", height=1, font=("Arial", 14))
labellot3_.place(x= 800, y=460)
textbox5_ = tk.Text(root, height=1, width=24, font=("Arial",14))
textbox5_.place(x=1000, y= 420)
textbox5_.config(state='disabled')
textbox6_ = tk.Text(root, height=1, width=24, font=("Arial",14))
textbox6_.place(x=1000, y= 460)
textbox6_.config(state='disabled')


buttonframe = tk.Frame(root)
buttonframe2 = tk.Frame(root)
buttonframe3 = tk.Frame(root)
buttonframe4 = tk.Frame(root)

#This creates the upper-left buttongrid with the numbers from 1 to 50
rows = 5
columns = 10
for i in range(rows):
    for j in range(columns):
        value = i * columns + j
        button_text = f"{i * columns + j + 1}"
        button = tk.Button(buttonframe, text=button_text)
        button.config(command=lambda b=button, v=value +1: on_button_click(b,v))
        button.grid(row=i, column=j, padx=5, pady=5)
buttonframe.place(x=10, y=50)


#This is the same but for Superzahlen
rows = 2
columns = 6
for i in range(rows):
    for j in range(columns):
        value = i * columns + j
        button_text = f"{i * columns + j + 1}"
        button = tk.Button(buttonframe2, text=button_text)
        button.config(command=lambda b=button, v=value + 1: on_supbutton_click(b,v))
        button.grid(row=i, column=j, padx=5, pady=5)
buttonframe2.place(x=10, y=270)

#For 6aus49 lotto:

rows = 5
columns = 10
for i in range(rows):
    for j in range(columns):
        value = i * columns + j
        button_text = f"{i * columns + j}"
        button = tk.Button(buttonframe3, text=button_text)
        button.config(command=lambda b=button, v=value : on_6button_click(b,v))
        button.grid(row=i, column=j, padx=5, pady=5)

buttonframe3.place(x=750, y=50)
# 6aus49 superzahl
rows = 2
columns = 6
for j in range(10):
    value = j
    button_text = f"{j}"
    button = tk.Button(buttonframe4, text=button_text)
    button.config(command=lambda b=button, v=value: on_sub6button_click(b,v))
    button.grid(row=i, column=j, padx=5, pady=5)
buttonframe4.place(x=750, y=270)

buttonGenerate = tk.Button(root, bg='#34ebe1', text="Euroticket generieren!", font=("Arial", 16), command=playLottery)
buttonGenerate.place(x=210, y=350)
button6aus49 = tk.Button(root, bg='#34ebe1', text="6AUS49 generieren!", font=("Arial", 16), command=generate6aus49)
button6aus49.place(x=1000, y=350)

#This saves the value of the buttons pressed in the lottery array and shows it inside a textbox
def on_button_click(button, value):
    global countnum
    global lottoOK
    textbox1.config(state='normal')
    if value not in button_values and countnum < 5:
        button.config(text="X")
        button_values.append(value)
        print(button_values)
        textbox1.insert(tk.END, f"{value}    ")
        countnum = countnum + 1
        if countnum == 5:
            lottoOK = True
        
    elif countnum > 4:
        messagebox.showerror(title="Error!", message=f"Sie haben schon 5 Zahlen eingegeben!")

    elif value in button_values:
        messagebox.showerror(title="Error!",
                             message=f"Sie haben schon die Zahl {value} eingegeben!. Versuchen Sie es nochmal!")
    textbox1.config(state='disabled')


#Same as on_button_click, but for the "Superzahlen"
def on_supbutton_click(button, value):
    global countsup
    global supOK
    textbox2.config(state='normal')
    if value not in sup_values and countsup < 2:
        button.config(text="X")
        sup_values.append(value)
        print(sup_values)
        textbox2.insert(tk.END, f"{value}   ")
        countsup = countsup + 1
        if countsup == 2:
            supOK = True
    elif countsup > 1:
        messagebox.showerror(title="Error!", message=f"Sie haben schon die 2 Superzahlen eingegeben!")
    elif value in sup_values:
        messagebox.showerror(title="Error!",
                             message=f"Sie haben schon die Zahl {value} eingegeben!. Versuchen Sie es nochmal!")
    textbox2.config(state='disabled')


def on_6button_click(button, value):
    global count6a49
    global l6a49OK
    textbox1_.config(state='normal')
    if value not in lotto6a49_values and count6a49 < 6:
        button.config(text="X")
        button6a49_values.append(value)
        print(button6a49_values)
        textbox1_.insert(tk.END, f"{value}    ")
        count6a49 = count6a49 + 1
        if count6a49sup == 5:
            l6a49OK = True

    elif count6a49 > 5:
        messagebox.showerror(title="Error!", message=f"Sie haben schon 6 Zahlen eingegeben!")

    elif value in button_values:
        messagebox.showerror(title="Error!",
                             message=f"Sie haben schon die Zahl {value} eingegeben!. Versuchen Sie es nochmal!")
    textbox1.config(state='disabled')

def on_sub6button_click(button, value):
    global count6a49sup
    global sup6a49
    global lsupOK
    textbox2_.config(state='normal')
    if count6a49sup < 1:
        button.config(text="X")
        sup6a49 = value
        print(sup6a49)
        textbox2_.insert(tk.END, f"{value}   ")
        count6a49sup = count6a49sup + 1
        lsupOK = True
    elif count6a49sup > 0:
        messagebox.showerror(title="Error!", message=f"Sie haben schon den Superzahl eingegeben!")
    textbox2_.config(state='disabled')

root.mainloop()
