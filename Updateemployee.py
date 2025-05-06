from tkinter import *
from tkinter import messagebox
import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Tiger",  # Replace with your MySQL password
            database="employee_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Update Employee
def update_employee():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "UPDATE employees SET name=%s, father_name=%s, address=%s, role=%s, phone=%s, salary=%s WHERE id=%s"
        values = (
            Name_entry.get(),
            Fname_entry.get(),
            Address_entry.get(),
            Role_entry.get(),
            Phone_entry.get(),
            Salary_entry.get(),
            ID_entry.get()
        )
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Employee updated successfully!")
        root.destroy()
        import Main
    except Exception as e:
        messagebox.showerror("Error", f"Error updating employee: {e}")
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
root.title("Update Employee Screen")
root.geometry("930x530")
root.configure(bg = "lightblue")

Label(root, text = "Update Employee", font = ("Arial", 20, "bold"), bg = "lightblue").pack(pady=10)

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

Label(root, text="Phone", font=("Arial",16), bg = "lightblue").place(x = 250, y = 350)

Phone_entry = Entry(root, width= 20, font=("Arial", 16))
Phone_entry.place(x = 400 , y = 350)

Label(root, text="Salary", font=("Arial",16), bg = "lightblue").place(x = 250, y = 400)

Salary_entry = Entry(root, width= 20, font=("Arial", 16))
Salary_entry.place(x = 400 , y = 400)

Button(root, text ="Update", font = ("Arial", 16),bg ="#a29bfe",command=update_employee).place(x = 300, y = 475)

Button(root, text ="Clear", font = ("Arial", 16),bg ="#a29bfe",command=clear).place(x = 450, y = 475)

Button(root, text ="Back", font = ("Arial", 16),bg ="#a29bfe",command=Main).place(x = 600, y = 475)

root.mainloop()
