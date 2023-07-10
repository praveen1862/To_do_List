import tkinter as tk                  
from tkinter import ttk                  
from tkinter import messagebox         
import sqlite3 as sql                 
  

def add_task():  
 
    task_string = task_field.get()  

    if len(task_string) == 0:  
  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
       
        tasks.append(task_string)  
        
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
         
        list_update()  
      
        task_field.delete(0, 'end')  
  

def list_update():  
   
    clear_list()  
    
    for task in tasks:  
       
        task_listbox.insert('end', task)  
  

def delete_task():  

    try:  
       
        the_value = task_listbox.get(task_listbox.curselection())  
        
        if the_value in tasks:  
          
            tasks.remove(the_value)  
          
            list_update()  
          
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  

def delete_all_tasks():  
  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
   
    if message_box == True:  
      
        while(len(tasks) != 0):  
           
            tasks.pop()  
  
        the_cursor.execute('Delete from tasks')  
         
        list_update()  
  

def clear_list():  
   
    task_listbox.delete(0, 'end')  
  
 
def close():  
    
    print(tasks)  
   
    guiWindow.destroy()  
 
def retrieve_database():  
    
    while(len(tasks) != 0):  
       
        tasks.pop()  
    
    for row in the_cursor.execute('Select title from tasks'):  
       
        tasks.append(row[0])  
  

if __name__ == "__main__":  

    guiWindow = tk.Tk()  
    
    guiWindow.title("To-Do List Manager - JAVATPOINT")  
 
    guiWindow.geometry("500x450+750+250")  

    guiWindow.resizable(0, 0)  
   
    guiWindow.configure(bg = "black")  
  

    the_connection = sql.connect('listOfTasks.db')  
 
    the_cursor = the_connection.cursor()  
   
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    # defining an empty list  
    tasks = []  
      
    # defining frames using the tk.Frame() widget  
    header_frame = tk.Frame(guiWindow, bg = "black") 
    functions_frame = tk.Frame(guiWindow, bg = "#28282B")  
    listbox_frame = tk.Frame(guiWindow, bg = "#28282B")  
  
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    # defining a label using the ttk.Label() widget  
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Verdana", "25", "bold"),  
        background = "black",  
        foreground = "white"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#28282B",  
        foreground = "white"  
    )  
  
    task_label.place(x = 30, y = 40)  
      
    # defining an entry field using the ttk.Entry() widget  
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "11"),  
        width = 19,  
        background = "#FFF8DC",  
        foreground = "black"  
    )  
    # using the place() method to place the entry field in the application  
    task_field.place(x = 30, y = 80)  
  
    # adding buttons to the application using the ttk.Button() widget  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
  
    # defining a list box using the tk.Listbox() widget  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 30,  
        height = 15,  
        selectmode = 'SINGLE',  
        background = "white", 
        foreground = "#000000",  
        selectbackground = "black",  
        selectforeground = "white"  
    )  
    # using the place() method to place the list box in the application  
    task_listbox.place(x = 5, y = 60)  
  
    # calling some functions  
    retrieve_database()  
    list_update()  
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor.close() 