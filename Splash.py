from tkinter import *
from tkinter import messagebox

def continueApp():    
    user_choice = messagebox.askokcancel("Continue", "Do you want to continue to the main application?")
    if user_choice:
        root.destroy()
        import Login  # Assuming Login.py is the main application file
    else:
        root.quit()
   
root = Tk()
root.title("Splash Screen")
root.geometry("930x530")
root.configure(bg="lightblue")

Label(root, text="Welcome to the Application", font=("Arial", 20), bg="lightblue").pack(pady=10)

Label(root, text="Employee", font=("Arial", 16), bg="lightblue").place(x=400, y=100)

Label(root, text="Management System", font=("Arial", 16), bg="lightblue").place(x=350, y=150)

Label(root, text="Version 1.0", font=("Arial", 12), bg="lightblue").place(x=400, y=200)

Label(root, text="Developed by : Rajat Kumar & Abhishek Sharma", font=("Arial", 14), bg="lightblue").place(x=260, y=250)

Button(root, text="Continue", font=("Arial", 12), bg="#a29bfe", command = continueApp).place(x=375, y=300)

Button(root, text="Exit", font=("Arial", 12), bg="red", command=root.quit).place(x=500, y=300)

root.mainloop()