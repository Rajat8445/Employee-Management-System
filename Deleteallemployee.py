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
    
# Delete All Employees
def delete_all_employees():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "DELETE FROM employees"
        cursor.execute(query)
        conn.commit()
        messagebox.showinfo("Success", "All employees deleted successfully!")
        import Main
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting all employees: {e}")
    finally:
        conn.close()

def Main():
    root.destroy()
    import Main

root = Tk()
root.title("Delete All Employee Screen")
root.geometry("930x530")
root.configure(bg = "lightblue")

Label(root, text = "Delete All Employees", font = ("Arial", 20, "bold"), bg = "lightblue").pack(pady=10)


Button(root, text="Delete All", command=delete_all_employees, bg="red", fg="white", font=("Arial", 15)).place(x=300, y=150)

Button(root, text="Back", command=Main, bg="blue", fg="white", font=("Arial", 15)).place(x=500, y=150)

root.mainloop()