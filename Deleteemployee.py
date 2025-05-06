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
    
# Delete Employee
def delete_employee():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "DELETE FROM employees WHERE id=%s"
        values = (ID_entry.get(),)
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Employee deleted successfully!")
        root.destroy()
        import Main
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting employee: {e}")
    finally:
        conn.close()

def Main():
    root.destroy()
    import Main

root = Tk()
root.title("Delete Employee Screen")
root.geometry("930x530")
root.configure(bg = "lightblue")

Label(root, text = "Delete Employee", font = ("Arial", 20, "bold"), bg = "lightblue").pack(pady=10)
    
ID_label = Label(root, text="Employee ID:", font = ("Arial", 12), bg="lightblue")
ID_label.place(x=250, y=100)

ID_entry = Entry(root)
ID_entry.place(x=400, y=100)
ID_entry.config(width=20, font=("Arial", 12))

Button(root, text="Delete Employee", bg ="#a29bfe" ,font=("Arial", 12), command=delete_employee).place(x=300, y=150)

Button(root, text="Back", bg ="#a29bfe" ,font=("Arial", 12), command=Main).place(x=500, y=150)

root.mainloop()