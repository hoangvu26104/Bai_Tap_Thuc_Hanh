CREATE TABLE Student (
    Student_Id   INTEGER PRIMARY KEY,
    Name         TEXT,
    Surrname     TEXT,
    DateOfBirth  TEXT,
    YearEnrolled INTEGER
);


Create table Course (
    Course_Id Text,
    Name Text,
    CreditPoints Integer,
    YearCommenced Integer
);

Create table Staff (
    Employee_Id Text,
    Name Text,
    SureName Text,
    JobTitle Text
);

Create Table Program(
    Program_Id Text,
    Name Text,
    CreditsPoints Integer,
    YearCommenced Integer
);

Insert Into Student (Student_Id, Name, Surrname, DateOfBirth, YearEnrolled)
Values (1, 'Nguyễn', 'Văn A', '1999-03-15', 2017),
(2, 'Trần', 'Thị B', '2000-11-25', 2018),
(3, 'Lê', 'Minh C', '1998-07-10', 2016),
(4, 'Phạm', 'Quốc D', '2001-02-20', 2019),
(5, 'Đỗ', 'Thị E', '1997-05-22', 2015),
(6, 'Vũ', 'Văn F', '2000-09-12', 2018),
(7, 'Bùi', 'Thị G', '1999-04-30', 2017),
(8, 'Hoàng', 'Văn H', '1998-06-05', 2016),
(9, 'Phan', 'Thị I', '2001-12-01', 2019),
(10, 'Đinh', 'Văn J', '2000-08-14', 2018);

INSERT INTO Course (Course_Id, Name, CreditPoints, YearCommenced) VALUES
(101, 'Toán học', 3, 2015),
(102, 'Vật lý', 4, 2016),
(103, 'Hóa học', 3, 2017),
(104, 'Sinh học', 4, 2018),
(105, 'Khoa học máy tính', 6, 2015),
(106, 'Kinh tế học', 3, 2016),
(107, 'Tâm lý học', 4, 2017),
(108, 'Kỹ thuật', 5, 2018),
(109, 'Lịch sử', 3, 2015),
(110, 'Ngôn ngữ Anh', 3, 2016);

INSERT INTO staff (Employee_Id, Name, Surename, JobTitle) VALUES
(101, 'Nguyễn', 'Anh', 'Giáo sư'),
(102, 'Trần', 'Bình', 'Phó Giáo sư'),
(103, 'Lê', 'Chiến', 'Giảng viên'),
(104, 'Phạm', 'Dũng', 'Giảng viên chính'),
(105, 'Đỗ', 'Hoàng', 'Giáo sư'),
(106, 'Vũ', 'Kiên', 'Giảng viên'),
(107, 'Bùi', 'Lan', 'Trợ lý Giáo sư'),
(108, 'Hoàng', 'Mạnh', 'Giáo sư'),
(109, 'Phan', 'Ngọc', 'Giảng viên chính'),
(110, 'Đinh', 'Phong', 'Phó Giáo sư');


INSERT INTO Program (Program_Id, Name, CreditsPoints, YearCommenced) VALUES
(201, 'Chương trình Toán học', 120, 2015),
(202, 'Chương trình Vật lý', 130, 2016),
(203, 'Chương trình Hóa học', 125, 2017),
(204, 'Chương trình Sinh học', 135, 2018),
(205, 'Chương trình Khoa học máy tính', 150, 2015),
(206, 'Chương trình Kinh tế học', 120, 2016),
(207, 'Chương trình Tâm lý học', 130, 2017),
(208, 'Chương trình Kỹ thuật', 140, 2018),
(209, 'Chương trình Lịch sử', 125, 2015),
(210, 'Chương trình Ngôn ngữ Anh', 120, 2016);


--Hien thi ten sinh vien bang chu H
Select SurrName 
From Student
Where SurrName Like '%H';

--Hien thi sinh vien nam 4
Select SurrName 
From Student
Where 2023 - YearEnrolled = 4;


--Hiển thị tất cả các khóa học từ bảng course bắt đầu với những khóa học có số điểm tín chỉ cao nhất.
Select Name ,
    Max(CreditPoints)as SoTinChi
From Course
Order By CreditPoints Desc;

--Đổi tên sinh viên có student_id thấp nhất thành Adam.
Update Student
Set Surrname = "Adam"
Where Student_Id = 1;

--Đổi tất cả giá trị trong cột name của bảng course thành chữ hoa.
Select Upper(c.Name)
From Course c;


--Xóa sinh viên lớn tuổi nhất trong bảng student.
Delete From Student 
Where Student.YearEnrolled = (
    Select Min(Student.YearEnrolled)
    From Student
);


--Loại bỏ cột yearCommenced khỏi bảng course.
Alter Table Course 
Drop Column YearCommenced;

--Đổi tên bảng staff thành employee.
Alter Table Staff
Rename To Employee