from tkinter import *
import mysql.connector
from tkinter.ttk import Combobox
from tkinter import messagebox

def save():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Tiger",  # Replace with your MySQL password
            database="employee_db"
        )
        cursor = conn.cursor()
        
        # Insert data into the employees table
        query = "INSERT INTO employees (id, name, father_name, address, role, phone, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (
            ID_entry.get(),
            Name_entry.get(),
            Fname_entry.get(),
            Address_entry.get(),
            Role_entry.get(),
            Phone_entry.get(),
            Salary_entry.get()
        )
        cursor.execute(query, values)
        conn.commit()
        
        Label(root, text="Data Saved Successfully!", font=("Arial", 14), fg="green", bg="lightblue").place(x=450, y=475)
        root.destroy()
        import Main  # Import the main module after saving data
        
    except mysql.connector.Error as err:
        Label(root, text=f"Error: {err}", font=("Arial", 14), fg="red", bg="lightblue").place(x=450, y=475)
    finally:
        conn.close()

def clear():
    # Clear all entry fields
    ID_entry.delete(0, END)
    Name_entry.delete(0, END)
    Fname_entry.delete(0, END)
    Address_entry.delete(0, END)
    Role_entry.delete(0, END)
    Phone_entry.delete(0, END)
    Salary_entry.delete(0, END)
    Label(root, text="Fields Cleared!", font=("Arial", 14), fg="blue", bg="lightblue").place(x=450, y=475)
    root.destroy()
    import Main

def Main():
    root.destroy()
    import Main

root = Tk()
root.title("Add Employee Page")
root.geometry("930x530")
root.configure(bg = "lightblue")

Label(root, text = "Add Employee", font = ("Arial", 20, "bold"), bg = "lightblue").pack(pady=10)

Label(root, text = "ID", font = ("Arial", 16), bg = "lightblue").place(x = 250, y = 100)

ID_entry = Entry(root, width = 20, font = ("Arial",16))
ID_entry.place(x = 400, y = 100)

Label(root, text = "Name", font = ("Arial", 16), bg = "lightblue").place(x = 250, y = 150)

Name_entry = Entry(root, width = 20, font = ("Arial", 16))
Name_entry.place(x = 400, y =150)

Label(root, text = "Father Name", font = ("Arial",16), bg = "lightblue").place(x = 250, y = 200)

Fname_entry = Entry(root, width = 20, font = ("Arial", 16))
Fname_entry.place(x = 400, y = 200)

Label(root, text = "Address", font = ("Arial", 16), bg = "lightblue").place(x = 250, y = 250)

Address_entry = Entry(root, width = 20, font = ("Arial", 16))
Address_entry.place(x = 400, y = 250)

Label(root, text="Role", font=("Arial",16), bg = "lightblue").place(x = 250, y = 300)

Role_entry = Entry(root, width= 20, font=("Arial", 16))
Role_entry.place(x = 400 , y = 300)
# Role_options = ["Manager", "Web Developer", "Designer", "Tester" , "Java Developer", "Python Developer", "Accountant", "AI Engineer", "Machine Learning Engineer", "Data Scientist", "HR", "Sales Executive", "Marketing Executive", "Intern", "UI/UX Designer", "System Administrator", "Network Engineer", "Database Administrator", "Security Analyst", "DevOps Engineer", "Cloud Engineer", "Business Analyst", "Project Manager", "Product Manager"]
# Role_box = Combobox(root, values=Role_options, font=("Arial", 16), state="readonly")
# Role_box.place(x=400, y=300)

Label(root, text="Phone", font=("Arial",16), bg = "lightblue").place(x = 250, y = 350)

Phone_entry = Entry(root, width= 20, font=("Arial", 16))
Phone_entry.place(x = 400 , y = 350)

Label(root, text="Salary", font=("Arial",16), bg = "lightblue").place(x = 250, y = 400)

Salary_entry = Entry(root, width= 20, font=("Arial", 16))
Salary_entry.place(x = 400 , y = 400)

Button(root, text ="Save", font = ("Arial", 16),bg ="#a29bfe",command=save).place(x = 250, y = 475)

Button(root, text ="Clear", font = ("Arial", 16),bg ="#a29bfe",command=clear).place(x = 425, y = 475)

Button(root, text="Back", font=("Arial", 16), bg="#a29bfe", command=Main).place(x=600, y=475)

root.mainloop()