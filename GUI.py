from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""Stroke Prediction algorithm using ML"""

# Importing the dataset
dataset1 = pd.read_csv('train_2v.csv')
X = dataset1.iloc[1:, 1:-3].values
Y = dataset1.iloc[1:, 11].values
df = pd.DataFrame(X)

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder#to convert catogorical data to encoded values
labelencoder_X = LabelEncoder()
X[:, 0] =labelencoder_X.fit_transform(X[:, 0])
X[:, 4] =labelencoder_X.fit_transform(X[:, 4])
X[:, 5] =labelencoder_X.fit_transform(X[:, 5])
X[:, 6] =labelencoder_X.fit_transform(X[:, 6])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


""" User Interface"""
Database = {}
temp_Database = {}



def first_page():
    root = Tk()
    root.state('zoomed')
    root.configure(background="grey")

    def start():
        temp_Database["ever_married"] = m_status.get()
        temp_Database["work_type"] = w_status.get()
        temp_Database["gender"] = g_status.get()
        temp_Database["name"] = entry_name.get()
        temp_Database["age"] = entry_age.get()

        if (temp_Database["name"] == "" or temp_Database["age"] == ""):
            messagebox.showwarning('warning', "Kindly enter your Name and Age")

        elif ("".join(temp_Database["name"].split(" "))).isalpha() == False:
            messagebox.showwarning('warning', "Name should contain only alphabets")
            entry_name.delete(0, END)

        elif ("".join(temp_Database["age"].split(" "))).isdigit() == False:
            messagebox.showwarning('warning', "Age should contain only numbers")
            entry_age.delete(0, END)

        else:
            entry_name.delete(0, END)
            entry_age.delete(0, END)
            sec_page(root)

    gap_size = font.Font(size=1, weight='bold')
    heading = font.Font(size=60, weight='bold')
    heading1 = font.Font(size=30, weight='bold')
    entry = font.Font(size=25)
    entryfontname = ('verdana', 15)
    entryfontage = ('verdana', 8)

    gap = Label(root, bg='grey')
    gap.config(font=(10))
    gap.pack(fill=X)

    head1 = Label(root, text="Health Kiosk", fg="red", bg='grey')
    head1.config(font=('verdana', 50, 'bold'))
    head1.pack()

    gap1 = Label(root, bg='grey')
    gap1.config(font=('bold', 1))
    gap1.pack(fill=X)

    labelname = Label(root, text='Enter your name', bg="grey")
    labelname.config(font=('verdana', 20, 'bold'))
    labelname.pack()

    gap2 = Label(root, bg='grey')
    gap2.config(font=('bold', 1))
    gap2.pack(fill=X)

    entry_name = Entry(root, font=entryfontname)
    entry_name.pack()

    gap3 = Label(root, bg='grey')
    gap3.config(font=('bold', 1))
    gap3.pack(fill=X)

    gap4 = Label(root, bg='grey')
    gap4.config(font=('bold', 1))
    gap4.pack(fill=X)

    labelage = Label(root, text="Enter your Age", bg="grey")
    labelage.config(font=('verdana', 20, 'bold'))
    labelage.pack()

    gap5 = Label(root, bg='grey')
    gap5.config(font=('bold', 1))
    gap5.pack(fill=X)

    entry_age = Entry(root, font=entryfontage)
    entry_age.pack(ipady=8)

    gap6 = Label(root, bg='grey')
    gap6.config(font=('bold', 1))

    gap6.pack(fill=X)

    labelgender = Label(root, text="Select your Gender", bg="grey")
    labelgender.config(font=('verdana', 20, 'bold'))
    labelgender.pack()

    gap7 = Label(root, bg='grey')
    gap7.config(font=('bold', 1))

    gap7.pack(fill=X)

    g_status = StringVar(root)
    g_status.set("Select")  # default value
    g = OptionMenu(root, g_status, "Male", "Female", "Rather not say")
    g.pack(ipady=1)

    gap8 = Label(root, bg='grey')
    gap8.config(font=('bold', 1))
    gap8.pack(fill=X)

    labelmaritalstatus = Label(root, text="Select your Marital status", bg="grey")
    labelmaritalstatus.config(font=('verdana', 20, 'bold'))
    labelmaritalstatus.pack()

    gap9 = Label(root, bg='grey')
    gap9.config(font=('bold', 1))
    gap9.pack(fill=X)

    m_status = StringVar(root)
    m_status.set("Select")  # default value
    w = OptionMenu(root, m_status, "Yes", "No")
    w.pack(ipady=1)

    gap10 = Label(root, bg='grey')
    gap10.config(font=('bold', 1))
    gap10.pack(fill=X)

    labelworkingstatus = Label(root, text="Select your professional status", bg="grey")
    labelworkingstatus.config(font=('verdana', 20, 'bold'))
    labelworkingstatus.pack()

    gap11 = Label(root, bg='grey')
    gap11.config(font=('bold', 1))
    gap11.pack(fill=X)

    w_status = StringVar(root)
    w_status.set("Select")  # default value
    w_down = OptionMenu(root, w_status, "children", "Private", 'Self-employed', 'Govt_job')
    w_down.pack(ipady=1)

    gap12 = Label(root, bg='grey')
    gap12.config(font=('bold', 1))
    gap12.pack(fill=X)

    labelarea = Label(root, text="Living Area", bg="grey")
    labelarea.config(font=('verdana', 20, 'bold'))
    labelarea.pack()

    gap13 = Label(root, bg='grey')
    gap13.config(font=('bold', 1))
    gap13.pack(fill=X)

    living_status = StringVar(root)
    living_status.set("Select")  # default value
    l_down = OptionMenu(root, living_status, "Rural", "Urban")
    l_down.pack(ipady=1)

    gap14 = Label(root, bg='grey')
    gap14.config(font=('bold', 1))
    gap14.pack(fill=X)

    gap15 = Label(root, bg='grey')
    gap15.config(font=('bold', 1))
    gap15.pack(fill=X)

    but = Button(root, text="next", font=entry_age, bg="blue", command=start)
    but.pack()

    gap16 = Label(root, bg='grey')
    gap16.config(font=('bold', 1))
    gap16.pack(fill=X)

    gap17 = Label(root, bg='grey')
    gap17.config(font=('bold', 1))
    gap17.pack(fill=X)

    root.mainloop()


def sec_page(root):
    root.destroy()
    # font sizes
    font_pro = ('verdana', 15)

    def fun_height():
        height_status = messagebox.askquestion("Confirm", "Click YES and please stand straight for 2-5 seconds")
        if height_status == "yes":
            temp_Database['height'] = 150

    def fun_weight():
        weight_status = messagebox.askquestion("Confirm", "Click YES and please stand on load cell for 2-5 seconds")
        if weight_status == "yes":
            temp_Database['weight'] = 60
            bmi = temp_Database['weight'] / (temp_Database['height'] / 100) ** 2
            bmi_print = str(bmi)
            temp_Database["bmi"] = bmi_print[:5]
            if bmi < 18.5:
                temp_Database["bmi_status"] = "underweight"
            elif (bmi >= 18.5 and bmi <= 24.9):
                temp_Database["bmi_status"] = "Healthyweight"
            elif (bmi >= 25 and bmi <= 29.9):
                temp_Database["bmi_status"] = "overweight"
            else:
                temp_Database["bmi_status"] = "obese"

    def fun_temp():
        temp_status = messagebox.askquestion("Confirm",
                                             "Click YES and place your finger on the tip of temperature sensor ")
        if temp_status == "yes":
            temp_Database['temp'] = 34

    def fun_heart():
        heart_status = messagebox.askquestion("Confirm", "Click YES and place your thumb on heart rate sensor")
        if heart_status == "yes":
            temp_Database['heart_rate'] = 78
            temp_Database['blood_oxygen_level'] = 80

    sec_root = Tk()
    sec_root.state("zoomed")
    sec_root.configure(background="grey")

    def results():
        temp_Database['poss_stroke'] = "No"

        if temp_Database.get('height') == None:
            temp_Database['height'] = "Not Taken"
            temp_Database["bmi"] = "Can't Calculate without height and weight"
            temp_Database["bmi_status"] = "Can't Calculate without height and weight"
        else:
            temp_Database['height'] = str(temp_Database['height']) + " cm"

        if temp_Database.get('weight') == None:
            temp_Database['weight'] = "Not Taken"
            temp_Database["bmi"] = "Can't Calculate"
            temp_Database["bmi_status"] = "Can't Calculate"
        else:
            temp_Database['weight'] = str(temp_Database['weight']) + " kg"

        if temp_Database.get('temp') == None:
            temp_Database['temp'] = "Not Taken"
        else:
            temp_Database['temp'] = str(temp_Database['temp']) + " C"

        if temp_Database.get('heart_rate') == None:
            temp_Database['heart_rate'] = "Not Taken"
            temp_Database['blood_oxygen_level'] = "Not Taken"
        else:
            temp_Database['heart_rate'] = str(temp_Database['heart_rate']) + " bpm"
            temp_Database['blood_oxygen_level'] = str(temp_Database['blood_oxygen_level']) + " %"


        third_page(sec_root)

    gaps1 = Label(sec_root, bg='grey')
    gaps1.config(font=(10))
    gaps1.pack(fill=X)

    sec_head1 = Label(sec_root, text="Health Kiosk", fg="red", bg='grey')
    sec_head1.config(font=('verdana', 50, 'bold'))
    sec_head1.pack()

    gaps1 = Label(sec_root, bg='grey')
    gaps1.config(font=(35))
    gaps1.pack(fill=X)

    labelheight = Label(sec_root, text='Click proceed if you want to check you height', bg="grey")
    labelheight.config(font=('verdana', 20, 'bold'))
    labelheight.pack()

    gaps2 = Label(sec_root, bg='grey')
    gaps2.config(font=(35))
    gaps2.pack(fill=X)

    but_height = Button(sec_root, text="Proceed", font=font_pro, bg="blue", command=fun_height)
    but_height.pack()

    gaps3 = Label(sec_root, bg='grey')
    gaps3.config(font=(35))
    gaps3.pack(fill=X)

    labelweight = Label(sec_root, text='Click proceed if you want to check you weight', bg="grey")
    labelweight.config(font=('verdana', 20, 'bold'))
    labelweight.pack()

    gaps4 = Label(sec_root, bg='grey')
    gaps4.config(font=(35))
    gaps4.pack(fill=X)

    but_weight = Button(sec_root, text="Proceed", font=font_pro, bg="blue", command=fun_weight)
    but_weight.pack()

    gaps5 = Label(sec_root, bg='grey')
    gaps5.config(font=(35))
    gaps5.pack(fill=X)

    labeltemp = Label(sec_root, text='Click proceed if you want to check you body temperature', bg="grey")
    labeltemp.config(font=('verdana', 20, 'bold'))
    labeltemp.pack()

    gaps6 = Label(sec_root, bg='grey')
    gaps6.config(font=(35))
    gaps6.pack(fill=X)

    but_temp = Button(sec_root, text="Proceed", font=font_pro, bg="blue", command=fun_temp)
    but_temp.pack()

    gaps7 = Label(sec_root, bg='grey')
    gaps7.config(font=(35))
    gaps7.pack(fill=X)

    labelheart = Label(sec_root, text='Click proceed if you want to check you Heart rate', bg="grey")
    labelheart.config(font=('verdana', 20, 'bold'))
    labelheart.pack()

    gaps8 = Label(sec_root, bg='grey')
    gaps8.config(font=(35))
    gaps8.pack(fill=X)

    but_heart = Button(sec_root, text="Proceed", font=font_pro, bg="blue", command=fun_heart)
    but_heart.pack()

    gaps9 = Label(sec_root, bg='grey')
    gaps9.config(font=(35))
    gaps9.pack(fill=X)

    results = Button(sec_root, text="Results", font=('verdana', 18), bg="green", command=results)
    results.pack()
    sec_root.mainloop()


def third_page(sec_root):
    sec_root.destroy()

    def restart():
        third_root.destroy()
        unique_id = "".join(temp_Database["name"].split(" ")) + temp_Database["age"]
        Database[unique_id] = {}
        Database[unique_id].update(temp_Database)
        temp_Database.clear()
        print(Database)
        first_page()

    third_root = Tk()
    third_root.state("zoomed")
    third_root.configure(background="grey")

    tframe = Frame(third_root, bg="grey")
    tframe.config()
    tframe.pack()

    name_gap = Label(tframe, bg='grey')
    name_gap.config(font=(25))
    name_gap.grid(rowspan=1)

    namelabel = Label(tframe, text="Name : ", bg='grey')
    namelabel.config(font=('verdana', 25))
    namelabel.grid(row=0, column=0)

    namelabel_val = Label(tframe, text=temp_Database['name'], bg='grey')
    namelabel_val.config(font=('verdana', 25))
    namelabel_val.grid(row=0, column=1)

    agelabel = Label(tframe, text="Age : ", bg='grey')
    agelabel.config(font=('verdana', 25))
    agelabel.grid(row=2, column=0)

    agelabel_val = Label(tframe, text=temp_Database['age'], bg='grey')
    agelabel_val.config(font=('verdana', 25))
    agelabel_val.grid(row=2, column=1)

    height_gap = Label(tframe, bg='grey')
    height_gap.config(font=(25))
    height_gap.grid(rowspan=3)

    heightlabel = Label(tframe, text="Height : ", bg='grey')
    heightlabel.config(font=('verdana', 25))
    heightlabel.grid(row=4, column=0)

    heightlabel_val = Label(tframe, text=temp_Database['height'], bg='grey')
    heightlabel_val.config(font=('verdana', 25))
    heightlabel_val.grid(row=4, column=1)

    weight_gap = Label(tframe, bg='grey')
    weight_gap.config(font=(25))
    weight_gap.grid(rowspan=5)

    weightlabel = Label(tframe, text="Weight : ", bg='grey')
    weightlabel.config(font=('verdana', 25))
    weightlabel.grid(row=6, column=0)

    weightlabel_val = Label(tframe, text=temp_Database['weight'], bg='grey')
    weightlabel_val.config(font=('verdana', 25))
    weightlabel_val.grid(row=6, column=1)

    bmi_gap = Label(tframe, bg='grey')
    bmi_gap.config(font=(25))
    bmi_gap.grid(rowspan=7)

    bmilabel = Label(tframe, text="BMI : ", bg='grey')
    bmilabel.config(font=('verdana', 25))
    bmilabel.grid(row=8, column=0)

    bmilabel_val = Label(tframe, text=temp_Database['bmi'], bg='grey')
    bmilabel_val.config(font=('verdana', 25))
    bmilabel_val.grid(row=8, column=1)

    bmicat_gap = Label(tframe, bg='grey')
    bmicat_gap.config(font=(25))
    bmicat_gap.grid(rowspan=9)

    bmicatlabel = Label(tframe, text="BMI Catagory: ", bg='grey')
    bmicatlabel.config(font=('verdana', 25))
    bmicatlabel.grid(row=10, column=0)

    bmicatlabel_val = Label(tframe, text=temp_Database['bmi_status'], bg='grey')
    bmicatlabel_val.config(font=('verdana', 25))
    bmicatlabel_val.grid(row=10, column=1)

    heartrate_gap = Label(tframe, bg='grey')
    heartrate_gap.config(font=(25))
    heartrate_gap.grid(rowspan=11)

    heartratelabel = Label(tframe, text="Heart Rate : ", bg='grey')
    heartratelabel.config(font=('verdana', 25))
    heartratelabel.grid(row=12, column=0)

    heartratelabel_val = Label(tframe, text=temp_Database['heart_rate'], bg='grey')
    heartratelabel_val.config(font=('verdana', 25))
    heartratelabel_val.grid(row=12, column=1)

    temp_gap = Label(tframe, bg='grey')
    temp_gap.config(font=(25))
    temp_gap.grid(rowspan=13)

    templabel = Label(tframe, text="Temperature : ", bg='grey')
    templabel.config(font=('verdana', 25))
    templabel.grid(row=14, column=0)

    templabel_val = Label(tframe, text=temp_Database['temp'], bg='grey')
    templabel_val.config(font=('verdana', 25))
    templabel_val.grid(row=14, column=1)

    oxygen_gap = Label(tframe, bg='grey')
    oxygen_gap.config(font=(25))
    oxygen_gap.grid(rowspan=15)

    oxygenlabel = Label(tframe, text="Blood Oxygen Percentage : ", bg='grey')
    oxygenlabel.config(font=('verdana', 25))
    oxygenlabel.grid(row=16, column=0)

    oxygenlabel_val = Label(tframe, text=temp_Database['blood_oxygen_level'], bg='grey')
    oxygenlabel_val.config(font=('verdana', 25))
    oxygenlabel_val.grid(row=16, column=1)

    stroke_gap = Label(tframe, bg='grey')
    stroke_gap.config(font=(25))
    stroke_gap.grid(rowspan=17)

    strokelabel = Label(tframe, text="Possiblity of stroke : ", bg='grey')
    strokelabel.config(font=('verdana', 25))
    strokelabel.grid(row=18, column=0)

    strokelabel_val = Label(tframe, text=temp_Database['poss_stroke'], bg='grey')
    strokelabel_val.config(font=('verdana', 25))
    strokelabel_val.grid(row=18, column=1)

    button_gap = Label(tframe, bg='grey')
    button_gap.config(font=(25))
    button_gap.grid(rowspan=19)

    but_to_start = Button(tframe, text="    Ok    ", bg="blue", command=restart)
    but_to_start.grid(columnspan=3)

    third_root.mainloop()


first_page()

