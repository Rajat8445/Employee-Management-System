from tkinter import *
from tkinter import messagebox
import mysql.connector
import bcrypt

# ---------------- Database Connection ----------------
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # Change if needed
            password="Tiger",   # Change to your MySQL password
            database="LoginDB"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# ---------------- Login Function ----------------
def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter username and password")
        return

    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            cursor.close()
            connection.close()

            if result:
                stored_hash = result[0]
                if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                    messagebox.showinfo("Success", "Login successful!")
                    root.destroy()
                    import Main  # Assuming Main.py is the main application file
                else:
                    messagebox.showerror("Error", "Invalid username or password")
            else:
                messagebox.showerror("Error", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    else:
        messagebox.showerror("Error", "Database connection failed")

# ---------------- Registration Function ----------------
def account():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter username and password")
        return

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Account created successfully!")
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    else:
        messagebox.showerror("Error", "Database connection failed")
    
root = Tk()
root.title("Login Page")
root.geometry("930x530")
root.configure(bg="lightblue")

Label(root, text="Login", font=("Arial", 20, "bold"), bg="lightblue").pack(pady=10)

Label(root, text="Username", font=("Arial", 12), bg="lightblue").place(x=300, y=100)

username_entry = Entry(root, width=30, font=("Arial", 12))
username_entry.place(x=400, y=100)

Label(root, text="Password", font=("Arial", 12), bg="lightblue").place(x=300, y=150)

password_entry = Entry(root, width=30, font=("Arial", 12), show="*")
password_entry.place(x=400, y=150)

Button(root, text="Login", font=("Arial", 12), bg="#a29bfe", command=login).place(x=375, y=200)

Button(root, text="Exit", font=("Arial", 12), bg="red", command=root.quit).place(x=550, y=200)

Button(root, text = "Create an account", font=("Arial", 12), command=account).place(x=400, y=250)

root.mainloop()