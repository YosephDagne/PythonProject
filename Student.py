import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")

tittle_label = tk.Label(win, text="Student Management System", font=("Areal", 25), border=12, relief=tk.GROOVE,
                        bg="lightgrey")
tittle_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Areal", 30, "bold"), bd=12, relief=tk.GROOVE,
                             bg="lightgrey")
detail_frame.place(x=20, y=80, width=420, height=550)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=475, y=80, width=780, height=550)

# ==================variable=========#
rollno = tk.StringVar()
studname = tk.StringVar()
fname = tk.StringVar()
class_var = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()
search_by = tk.StringVar()

# ====================================#

# =========ENTRY======#

rollno_lbl = tk.Label(detail_frame, text="Roll No", font=("Areal", 15), bg="lightgrey")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno_entry = tk.Entry(detail_frame, bd=5, font=("Areal", 15), textvariable=rollno)
rollno_entry.grid(row=0, column=1, padx=2, pady=2)

studname_lbl = tk.Label(detail_frame, text="Student Name", font=("Areal", 15), bg="lightgrey")
studname_lbl.grid(row=1, column=0, padx=2, pady=2)

studname_entry = tk.Entry(detail_frame, bd=7, font=("Areal", 15), textvariable=studname)
studname_entry.grid(row=1, column=1, padx=2, pady=2)

lname_lbl = tk.Label(detail_frame, text="Father's Name", font=("Areal", 15), bg="lightgrey")
lname_lbl.grid(row=2, column=0, padx=2, pady=2)

lname_entry = tk.Entry(detail_frame, bd=5, font=("Areal", 15), textvariable=fname)
lname_entry.grid(row=2, column=1, padx=2, pady=2)

class_lbl = tk.Label(detail_frame, text="Class", font=("Areal", 15), bg="lightgrey")
class_lbl.grid(row=3, column=0, padx=2, pady=2)

class_entry = tk.Entry(detail_frame, bd=7, font=("Areal", 15), textvariable=class_var)
class_entry.grid(row=3, column=1, padx=2, pady=2)

section_lbl = tk.Label(detail_frame, text="Section", font=("Areal", 15), bg="lightgrey")
section_lbl.grid(row=4, column=0, padx=2, pady=2)

section_entry = tk.Entry(detail_frame, bd=5, font=("Areal", 15), textvariable=section)
section_entry.grid(row=4, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact", font=("Areal", 15), bg="lightgrey")
contact_lbl.grid(row=5, column=0, padx=2, pady=2)

contact_entry = tk.Entry(detail_frame, bd=7, font=("Areal", 15), textvariable=contact)
contact_entry.grid(row=5, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_frame, text="Address", font=("Areal", 15), bg="lightgrey")
address_lbl.grid(row=6, column=0, padx=2, pady=2)

address_entry = tk.Entry(detail_frame, bd=7, font=("Areal", 15), textvariable=address)
address_entry.grid(row=6, column=1, padx=2, pady=2)

gender_lbl = tk.Label(detail_frame, text="Gender", font=("Areal", 15), bg="lightgrey")
gender_lbl.grid(row=7, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_frame, font=("Areal", 15), state="readonly", textvariable=gender)
gender_ent["values"] = ("Male", "Female", "Others")
gender_ent.grid(row=7, column=1, padx=2, pady=2)

dob_lbl = tk.Label(detail_frame, text="Date of Birth", font=("Areal", 15), bg="lightgrey")
dob_lbl.grid(row=8, column=0, padx=2, pady=2)

dob_entry = tk.Entry(detail_frame, bd=7, font=("Areal", 15), textvariable=dob)
dob_entry.grid(row=8, column=1, padx=2, pady=2)


# =========================================#

# ============functions==================#

def fetch_data():
    global conn, curr
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="student_management")
        curr = conn.cursor()
        curr.execute("SELECT * FROM student")
        rows = curr.fetchall()

        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        try:
            curr.close()
        except NameError:
            pass

        try:
            conn.close()
        except NameError:
            pass


def add_function():
    if (rollno.get() == "" or studname.get() == "" or
            fname.get() == "" or class_var.get() == "" or
            section.get() == "" or contact.get() == "" or
            address.get() == "" or gender.get() == "" or dob.get() == ""):
        messagebox.showerror("Error!", "Please fill all the fields")
    else:
        conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="student_management")
        curr = conn.cursor()
        curr.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
        rollno.get(), studname.get(), fname.get(), class_var.get(), section.get(), contact.get(), address.get(),
        gender.get(), dob.get()))
        conn.commit()
        conn.close()
        fetch_data()


def get_cursor(event):
    '''This function will fetch data of the selected row'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content["values"]
    rollno.set(row[0])
    studname.set(row[1])
    fname.set(row[2])
    class_var.set(row[3])
    section.set(row[4])
    contact.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8])


def clear_function():
    rollno.set("")
    studname.set("")
    fname.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    address.set("")
    gender.set("")
    dob.set("")


def update_function():
    conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="student_management")
    curr = conn.cursor()
    curr.execute("update student set studname=%s,"
                 "fname=%s,"
                 "class_var=%s,"
                 "section=%s,"
                 "contact=%s,"
                 "address=%s,"  # Removed the extra comma here
                 "gender=%s,"
                 "dob=%s where rollno=%s",
                 (studname.get(),
                  fname.get(),
                  class_var.get(),
                  section.get(),
                  contact.get(),
                  address.get(),
                  gender.get(),
                  dob.get(), rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear_function()

def delete_function():
    global curr, conn
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="student_management")
        curr = conn.cursor()

        if not rollno.get():
            messagebox.showerror("Error!", "Please select a record to delete.")
        else:
            curr.execute("DELETE FROM student WHERE rollno=%s", (rollno.get(),))
            conn.commit()
            fetch_data()
            clear_function()
            messagebox.showinfo("Success", "Record deleted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        try:
            curr.close()
        except NameError:
            pass

        try:
            conn.close()
        except NameError:
            pass

# =======================================#

# +====================#Buttons============#

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=22, y=370, width=352, height=120)

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Areal", 13), width=15, command=add_function)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Areal", 13), width=15,
                       command=update_function)
update_btn.grid(row=0, column=1, padx=3, pady=2)

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Areal", 13), width=15)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Areal", 13), width=15,
                      command=clear_function)
clear_btn.grid(row=1, column=1, padx=3, pady=2)

# =========================================#

# ===========Search========================#
search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("areal", 14))
search_lbl.grid(row=0, column=0, padx=2, pady=2)

search_in = ttk.Combobox(search_frame, font=("Areal", 14), state="readonly", textvariable=search_by)
search_in["value"] = (
"Roll No", "Student Name", "Father's Name", "Class", "Section", "Contact", "Address", "Gender", "Date of Birth")
search_in.grid(row=0, column=1, padx=2, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("Areal", 13), bd=9, width=14, bg="lightgrey")
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show All", font=("Areal", 13), bd=9, width=14, bg="lightgrey")
showall_btn.grid(row=0, column=3, padx=12, pady=2)

# ==========================================#

# ==========Database frame==============#

main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=(
"RollNo", "StudentName", "FatherName", "Class", "Section", "Contact", "Address", "Gender", "DateOfBirth"),
                             yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("RollNo", text="Roll No")
student_table.heading("StudentName", text="Student Name")
student_table.heading("FatherName", text="Father's Name")
student_table.heading("Class", text="Class")
student_table.heading("Section", text="Section")
student_table.heading("Contact", text="Contact")
student_table.heading("Address", text="Address")
student_table.heading("Gender", text="Gender")
student_table.heading("DateOfBirth", text="Date Of Birth")

student_table['show'] = "headings"

student_table.column("RollNo", width=100)
student_table.column("StudentName", width=100)
student_table.column("FatherName", width=100)
student_table.column("Class", width=100)
student_table.column("Section", width=100)
student_table.column("Contact", width=100)
student_table.column("Address", width=100)
student_table.column("Gender", width=100)
student_table.column("DateOfBirth", width=100)

student_table.pack(fill=tk.BOTH, expand=True)
fetch_data()
student_table.bind("<ButtonRelease-1>", get_cursor)

# ======================================#

win.mainloop()
