from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Treeview
from tkinter import ttk

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
    
# Search Employee
def search_employee():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT * FROM employees WHERE id=%s"
        values = (ID_entry.get(),)
        cursor.execute(query, values)
        employee = cursor.fetchone()
        if employee:
            tree.insert("", "end", values=employee)
        else:
            messagebox.showinfo("Search Result", "Employee not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error searching for employee: {e}")
    finally:
        cursor.close()
        conn.close()

def Main():
    root.destroy()
    import Main

root = Tk()
root.title("Search Employee Screen")
root.geometry("930x530")
root.configure(bg = "lightblue")

Label(root, text = "Search Employee", font = ("Arial", 20, "bold"), bg = "lightblue").pack(pady=10)
Label(root, text="ID", font=("Arial", 16), bg="lightblue").place(x=300, y=100)

ID_entry = Entry(root, width=20, font=("Arial", 16))
ID_entry.place(x=400, y=100)

Button(root, text="Search", command=search_employee, bg="#a29bfe", fg="white", font=("Arial", 15)).place(x=325, y=150)

Button(root, text="Back", command=Main, bg="#a29bfe", fg="white", font=("Arial", 15)).place(x=500, y=150)

tree = Treeview(root, columns=("ID", "Name", "Father Name", "Address", "Role", "Phone", "Salary"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Father Name", text="Father Name")
tree.heading("Address", text="Address")
tree.heading("Role", text="Role")
tree.heading("Phone", text="Phone")
tree.heading("Salary", text="Salary")
tree.pack(pady=150)

tree.column("ID", width=75, anchor="center")
tree.column("Name", width=100, anchor="center") 
tree.column("Father Name", width=150, anchor="center")
tree.column("Address", width=200, anchor="center")
tree.column("Role", width=200, anchor="center")
tree.column("Phone", width=100, anchor="center")
tree.column("Salary", width=125, anchor="center")

style = ttk.Style()
style.configure("Treeview", font=("Arial", 12), rowheight=20, background="lightblue")
style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#a29bfe")

root.mainloop()