from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Mad_lib_generator")
Label(root,text = "Enter data to see how mad_lib works", font = "arial 10 bold").pack()
Label(root,text ="Choose any one").pack()


def madlib_1():
    name = input("Enter name of the person :")
    place = input("Enter a location name :")
    animal = input("Enter an animal :")
    thing = input("Enter a material/non living object :")
    print("Yesterday " +name+ " visited a zoo near " +place+ " . At zoo " +name+ " saw the " +animal+ " which was hitten by " +thing)

def madlib_2():
    name = input("Enter name of the person :")
    apple_pdt = input("Enter ay apple pdt: ")
    android = input ("Enter any android pdt: ")
    print(name+" thinks apple device "+apple_pdt+ "is better than android devices like "+android)

Button(root,text="At zoo",command = madlib_1 ,bg="blue",font = "arial 10").place(x=190, y=150)
Button(root,text="Mobiles",command = madlib_2 ,bg="violet",font = "arial 10").place(x=190, y=200)

root.mainloop()

