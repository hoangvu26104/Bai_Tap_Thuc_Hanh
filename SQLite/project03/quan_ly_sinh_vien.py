import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("600x800")
# conn = sqlite3.connect('information_student.db')
# c = conn.cursor()
# c.execute('''
#     CREATE TABLE information_student(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name text,
#         last_name text,
#         information_student text,
#         city text,
#         state text,
#         zipcode interger
#     )
# '''
# )

def add():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('information_student.db')
    c = conn.cursor()
    # Lấy dữ liệu đã nhập
    name_value =f_name.get()
    lastName_value = l_name.get()
    class_id_value = class_id.get()
    year_enroll_value = year_enroll.get()
    avg_value = avg.get()
    # Thực hiện câu lệnh để thêm
    c.execute('''
        INSERT INTO 
        information_student (name, last_name, class_id, year_enroll, avg)
        VALUES 
        (:name, :last_name, :class_id,:year_enroll, :avg)
    ''',{
        'name' : name_value,
        'last_name' : lastName_value,
        'class_id': class_id_value,
        'year_enroll': year_enroll_value,
        'avg': avg_value,
      }
    )
    conn.commit()
    conn.close()

    # Reset form
    f_name.delete(0, END)
    l_name.delete(0, END)
    class_id.delete(0, END)
    year_enroll.delete(0, END)
    avg.delete(0, END)
    # Hien thi lai du lieu
    excute()
def delete():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('information_student.db')
    c = conn.cursor()
    c.execute(''' DELETE FROM
              information_student
                  WHERE student_id=:id''',
                  {'id':delete_box.get()})
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    messagebox.showinfo("Thông báo", "Đã xóa!")
    excute()

def excute():
    # Xóa đi các dữ liệu trong TreeView
    for row in tree.get_children():
        tree.delete(row)

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('information_student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM information_student")
    records = c.fetchall()

    # Hien thi du lieu
    for r in records:
        tree.insert("", END, values=(r[0],  r[1], r[2]))

    # Ngat ket noi
    conn.close()
    print()
def edit():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x300")

    conn = sqlite3.connect('information_student.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM information_student WHERE student_id=:id", {'id':record_id})
    records = c.fetchall()
    if records:
        global id_editor, f_name_editor, l_name_editor, class_id_editor, year_enroll_editor, avg_editor
    else:
        messagebox.showinfo("Thông báo", "Không tìm thấy thông tin!")

    

    


    id_editor = Entry(editor, width=30)
    id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=1, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=2, column=1)
    class_id_editor = Entry(editor, width=30)
    class_id_editor.grid(row=3, column=1)
    year_enroll_editor = Entry(editor, width=30)
    year_enroll_editor.grid(row=4, column=1)
    avg_editor = Entry(editor, width=30)
    avg_editor.grid(row=5, column=1)
   

    id_label = Label(editor, text="ID")
    id_label.grid(row=0, column=0, pady=(10, 0))
    f_name_label = Label(editor, text="Họ")
    f_name_label.grid(row=1, column=0)
    l_name_label = Label(editor, text="Tên")
    l_name_label.grid(row=2, column=0)
    class_id_label = Label(editor, text="Mã lớp")
    class_id_label.grid(row=3, column=0)
    year_enroll_label = Label(editor, text="Năm nhập học")
    year_enroll_label.grid(row=4, column=0)
    avg_label = Label(editor, text="Điểm trung bình")
    avg_label.grid(row=5, column=0)
    

    for record in records:
        id_editor.insert(0, record[0])
        f_name_editor.insert(0, record[1])
        l_name_editor.insert(0, record[2])
        class_id_editor.insert(0, record[3])
        year_enroll_editor.insert(0, record[4])
        avg_editor.insert(0, record[5])
        

    edit_btn = Button(editor, text="Lưu bản ghi", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

def update():
    conn = sqlite3.connect('information_student.db')
    c = conn.cursor()
    record_id = id_editor.get()

    c.execute("""UPDATE information_student SET
           name = :first,
           last_name = :last,
           class_id = :class_id,
           year_enroll = :year_enroll,
           avg = :avg,
           WHERE id = :id""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'class_id': class_id_editor.get(),
                  'year_enroll': year_enroll_editor.get(),
                  'avg': avg_editor.get(),
                  'id': record_id
              })

    conn.commit()
    conn.close()
    editor.destroy()

    # Cập nhật lại danh sách bản ghi sau khi chỉnh sửa
    excute()
    
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
f_name = Entry(input_frame, width=30)
f_name.grid(row=1, column=1, padx=20, pady=(10, 0))
l_name = Entry(input_frame, width=30)
l_name.grid(row=2, column=1)
class_id = Entry(input_frame, width=30)
class_id.grid(row=3, column=1)
year_enroll = Entry(input_frame, width=30)
year_enroll.grid(row=4, column=1)
avg = Entry(input_frame, width=30)
avg.grid(row=5, column=1)


# Các nhãn
id_label = Label(input_frame, text="Mã Sinh Viên")
id_label.grid(row=0, column=0, pady=(10, 0))
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=1, column=0)
l_name_label = Label(input_frame, text="Tên")
l_name_label.grid(row=2, column=0)
class_id_label = Label(input_frame, text="Mã lớp")
class_id_label.grid(row=3, column=0)
year_enroll_label = Label(input_frame, text="Năm nhập học")
year_enroll_label.grid(row=4, column=0)
avg_label = Label(input_frame, text="Điểm trung bình")
avg_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=add)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị bản ghi", command=excute)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn ID để xóa")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa bản ghi", command=delete)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=edit)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)
def select_record(event):
    # Lấy dữ liệu của dòng được chọn
    selected = tree.focus()
    values = tree.item(selected, 'values')

    # Hiển thị ID của dòng được chọn trong ô delete_box
    delete_box.delete(0, END)  # Xóa nội dung cũ trong ô delete_box
    delete_box.insert(0, values[0])  # Hiển thị ID mới

# Treeview để hiển thị bản ghi
columns = ("ID", "Họ", "Tên", "Địa Chỉ", "Thành Phố")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
tree.pack()

# Định nghĩa tiêu đề cho các cột
for col in columns:     
    tree.column(col, anchor=CENTER)
    tree.heading(col, text=col)
    
tree.bind("<<TreeviewSelect>>", select_record)

# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
excute()

root.mainloop()


