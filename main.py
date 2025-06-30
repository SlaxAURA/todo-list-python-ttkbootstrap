import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox

# Task list
tasks = []

# Add task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"description": task, "completed": False})
        task_entry.delete(0, END)
        update_tasks()
    else:
        messagebox.showwarning("Oops!", "Please enter a task.")

# Delete task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_tasks()
    else:
        messagebox.showwarning("No Selection", "Select a task to delete.")

# Mark as complete
def mark_completed():
    selected = task_listbox.curselection()
    if selected:
        tasks[selected[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("No Selection", "Select a task to complete.")

# Update listbox
def update_tasks():
    task_listbox.delete(0, END)
    for task in tasks:
        status = "✅" if task["completed"] else "🔘"
        task_listbox.insert(END, f"{status} {task['description']}")

# === UI Window ===
app = ttk.Window(title="🌟 Fancy To-Do App", themename="morph", size=(500, 600))
app.resizable(False, False)

# Header
ttk.Label(app, text="📝 My To-Do List", font=("Segoe UI", 20, "bold")).pack(pady=20)

# Entry
task_entry = ttk.Entry(app, width=40, font=("Segoe UI", 12))
task_entry.pack(pady=10, ipady=6)

# Listbox
task_listbox = tk.Listbox(app, width=45, height=10, font=("Segoe UI", 12),
                          bg="#f0f4f8", bd=0, highlightthickness=1, selectbackground="#c7d2fe")
task_listbox.pack(pady=20)

# Buttons Frame
btn_frame = ttk.Frame(app)
btn_frame.pack(pady=10)

# ➕ Add Button
add_btn = ttk.Button(btn_frame, text="➕ Add", bootstyle="primary-outline", width=14, command=add_task, cursor="hand2")
add_btn.grid(row=0, column=0, padx=10)
add_btn.bind("<Enter>", lambda e: add_btn.config(bootstyle="primary"))
add_btn.bind("<Leave>", lambda e: add_btn.config(bootstyle="primary-outline"))

# 🗑️ Delete Button
del_btn = ttk.Button(btn_frame, text="🗑️ Delete", bootstyle="danger-outline", width=14, command=delete_task, cursor="hand2")
del_btn.grid(row=0, column=1, padx=10)
del_btn.bind("<Enter>", lambda e: del_btn.config(bootstyle="danger"))
del_btn.bind("<Leave>", lambda e: del_btn.config(bootstyle="danger-outline"))

# ✅ Complete Button
done_btn = ttk.Button(btn_frame, text="✅ Complete", bootstyle="success-outline", width=14, command=mark_completed, cursor="hand2")
done_btn.grid(row=0, column=2, padx=10)
done_btn.bind("<Enter>", lambda e: done_btn.config(bootstyle="success"))
done_btn.bind("<Leave>", lambda e: done_btn.config(bootstyle="success-outline"))

# Footer
ttk.Label(app, text="Made by Aditya Mendhe", font=("Segoe UI", 10)).pack(pady=10)

# Run app
app.mainloop()
