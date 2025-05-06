from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from tkinter.ttk import Treeview

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
    
# View All Employees
def view_all_employees():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        # messagebox.showinfo("All Employees", f"{rows}")
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching employees: {e}")
    finally:
        cursor.close()
        conn.close()

def Main():
    root.destroy()
    import Main

root = Tk()
root.title("All Employee Screen")
root.geometry("930x530")
root.configure(bg = "lightblue")

Label(root, text = "All Employees", font = ("Arial", 20, "bold"), bg = "lightblue").pack(pady=10)
Button(root, text="View All Employees", command=view_all_employees, bg="#a29bfe", fg="white", font=("Arial", 15)).place(x=300, y=100)
Button(root, text="Back", command=Main, bg="#a29bfe", fg="white", font=("Arial", 15)).place(x=550, y=100)

tree = Treeview(root, columns=("ID", "Name", "Father Name", "Address", "Role", "Phone", "Salary"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Father Name", text="Father Name")
tree.heading("Address", text="Address")
tree.heading("Role", text="Role")
tree.heading("Phone", text="Phone")
tree.heading("Salary", text="Salary")
tree.pack(pady=100)

tree.column("ID", width=75, anchor="center")
tree.column("Name", width=100, anchor="center")
tree.column("Father Name", width=150, anchor="center")
tree.column("Address", width=200, anchor="center")
tree.column("Role", width=200, anchor="center")
tree.column("Phone", width=100, anchor="center")
tree.column("Salary", width=125, anchor="center")

style = ttk.Style()
style.configure("Treeview", font=("Arial", 12), rowheight=30, background="lightblue")
style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#a29bfe")

root.mainloop()