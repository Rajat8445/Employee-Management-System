from tkinter import *
from tkinter import messagebox

def addemployee():
    user_choice = messagebox.askokcancel("Add","Add new employee")
    if user_choice:
        root.destroy()
        import Addemployee
    else:
        root.quit()
    
def updateemployee():
    user_choice = messagebox.askokcancel("Update", "Update an employee")
    if user_choice:
        root.destroy()
        import Updateemployee
    else:
        root.quit()
    
def deleteemployee():
    user_choice = messagebox.askokcancel("Delete","Delete an employee")
    if user_choice:
        root.destroy()
        import Deleteemployee
    else:
        root.quit()    

def deleteall():
    user_choice = messagebox.askokcancel("Delete","Delete all employee")
    if user_choice:
        root.destroy()
        import Deleteallemployee
    else:
        root.quit()    

def allemployee():
    user_choice = messagebox.askokcancel("All", "Show all employee")
    if user_choice:
        root.destroy()
        import Allemployee
    else:
        root.quit()   

def searchemployee():
    user_choice = messagebox.askokcancel("Search", "Search an employee")
    if user_choice:
        root.destroy()
        import Searchemployee
    else:
        root.quit()
    
def logout():
    user_choice = messagebox.askokcancel("Log out", "Logout from this page")
    if user_choice:
        root.destroy()
        import Login
    else:
        root.quit()    
    
root = Tk()
root.title("Main Screen")
root.geometry("930x530")
root.configure(bg = "lightblue")

Label(root, text="Employee Management System", font=("Arial", 20), bg="lightblue").pack(pady=10)

Button(root, text="Add Employee", font=("Arial", 16), bg="#a29bfe", command=addemployee).place(x=300, y=100)

Button(root, text = "Update Employee", font = ("Arial", 16), bg = "#a29bfe", command = updateemployee).place(x = 300, y = 150)

Button(root, text = "Delete Employee", font = ("Arial",16), bg = "#a29bfe", command = deleteemployee).place(x = 300, y = 200 )

Button(root, text ="Delete all Employee", font = ("Arial", 16), bg = "#a29bfe", command = deleteall ).place(x = 300, y = 250)

Button(root, text = "View All Employee", font = ("Arial", 16), bg = "#a29bfe", command = allemployee).place(x = 300, y = 300)

Button(root, text = "Search Employee", font = ("Arial", 16), bg = "#a29bfe", command = searchemployee).place(x = 300, y = 350)

Button(root, text = "Log Out", font = ("Arial", 16), bg = "#a29bfe", command = logout).place(x = 350, y = 450)

Button(root, text = "Exit", font = ("Arial", 16), bg = "red", command = root.quit).place(x = 500, y = 450)

root.mainloop()