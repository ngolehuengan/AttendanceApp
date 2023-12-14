DROP DATABASE IF EXISTS attendance;
CREATE DATABASE attendance;
USE attendance;

-- -- -- -- -- TABLES -- -- -- -- --
CREATE TABLE account (
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(16) NOT NULL,
    password VARCHAR(32) NOT NULL
);

CREATE TABLE department (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE subject (
    id VARCHAR(6) PRIMARY KEY,
    name VARCHAR(50),
    id_dep INT NOT NULL,
    FOREIGN KEY (id_dep) REFERENCES department (id)
);

CREATE TABLE student (
	roll INT AUTO_INCREMENT PRIMARY KEY,
	id_subject VARCHAR(6) NOT NULL,
	year VARCHAR(9),
	semester VARCHAR(10),
	id_student VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(50),
	class_name VARCHAR(2),
	gender VARCHAR(10),
	dob VARCHAR(11),
	email VARCHAR(50),
	phone VARCHAR(10),
	address VARCHAR(100),
	teacher VARCHAR(50),
	photo TEXT,
	FOREIGN KEY (id_subject) REFERENCES subject (id)
);

DELIMITER //
-- -- -- -- -- PROCEDURES -- -- -- -- --

CREATE TRIGGER password_hasher BEFORE INSERT ON account FOR EACH ROW
BEGIN
	SET NEW.password = MD5 (NEW.password);
END//

CREATE PROCEDURE login(user VARCHAR(16), pass VARCHAR(16))
BEGIN
    SELECT * FROM account WHERE username=user AND password=MD5(pass);
END//

CREATE PROCEDURE dep_insert(dep_name varchar(50))
BEGIN
	INSERT INTO department (name) VALUES (dep_name);
END//

CREATE PROCEDURE dep_select()
BEGIN
	SELECT name FROM department;
END//

CREATE PROCEDURE dep_selectById(IN subj_id VARCHAR(6))
BEGIN
	SELECT department.name FROM department,subject WHERE subj_id = subject.id AND subject.id_dep = department.id;
END//

CREATE PROCEDURE subj_insert(subj_id VARCHAR(6), subj_name varchar(50), dep_id INT)
BEGIN
	INSERT INTO subject (id,name,id_dep) VALUES (subj_id,subj_name,dep_id);
END//

CREATE PROCEDURE subj_selectId(IN dep_id INT)
BEGIN
	SELECT id FROM subject WHERE id_dep = dep_id;
END//

CREATE PROCEDURE subj_selectName(IN subj_id VARCHAR(6))
BEGIN
	SELECT name FROM subject WHERE id = subj_id LIMIT 1;
END//

CREATE PROCEDURE InsertStudent(
    in_subject_id VARCHAR(6),
    in_year VARCHAR(9),
    in_semester VARCHAR(10),
    in_class_name VARCHAR(2),
    in_id_student VARCHAR(10),
    in_name VARCHAR(50),
    in_gender VARCHAR(10),
    in_dob VARCHAR(11),
    in_email VARCHAR(50),
    in_phone VARCHAR(10),
    in_address VARCHAR(100),
    in_teacher VARCHAR(50),
    in_photo TEXT
)
BEGIN
    INSERT INTO student (
        id_subject,
        year,
        semester,
        class_name,
        id_student,
        name,
        gender,
        dob,
        email,
        phone,
        address,
        teacher,
        photo
    )
    VALUES (
        in_subject_id,
        in_year,
        in_semester,
        in_class_name,
        in_id_student,
        in_name,
        in_gender,
        in_dob,
        in_email,
        in_phone,
        in_address,
        in_teacher,
        in_photo
    );
END //

CREATE PROCEDURE UpdateStudent(
    in_subject_id VARCHAR(6),
    in_year VARCHAR(9),
    in_semester VARCHAR(10),
    in_class_name VARCHAR(2),
    in_id_student VARCHAR(10),
    in_name VARCHAR(50),
    in_gender VARCHAR(10),
    in_dob VARCHAR(11),
    in_email VARCHAR(50),
    in_phone VARCHAR(10),
    in_address VARCHAR(100),
    in_teacher VARCHAR(50),
    in_photo TEXT
)
BEGIN
    UPDATE student
    SET
        id_subject = in_subject_id,
        year = in_year,
        semester = in_semester,
        class_name = in_class_name,
        name = in_name,
        gender = in_gender,
        dob = in_dob,
        email = in_email,
        phone = in_phone,
        address = in_address,
        teacher = in_teacher,
        photo = in_photo
    WHERE
        id_student = in_id_student;
END //

CREATE PROCEDURE DeleteStudent(IN id VARCHAR(10))
BEGIN
    DELETE FROM student WHERE id=id_student;
END //

CREATE PROCEDURE info()
BEGIN
    SELECT * FROM student;
END //

CREATE PROCEDURE face_id(IN id VARCHAR(10))
BEGIN
	SELECT id_student FROM student WHERE id = roll LIMIT 1;
END//

CREATE PROCEDURE face_name(IN id VARCHAR(10))
BEGIN
	SELECT name FROM student WHERE id = roll LIMIT 1;
END//

CREATE PROCEDURE face_roll(IN id VARCHAR(10))
BEGIN
	SELECT roll FROM student WHERE id = roll LIMIT 1;
END//

DELIMITER ;

-- -- -- -- -- VALUES -- -- -- -- --
INSERT INTO account (username,password) VALUE
	('admin','admin');

CALL dep_insert('Chọn chuyên ngành');
CALL dep_insert('Hệ Thống Thông Tin');
CALL dep_insert('Kỹ Thuật Phần Mềm');
CALL dep_insert('Kỹ Thuật Máy Tính');
CALL dep_insert('Khoa Học Máy Tính');

CALL subj_insert('861301','Triết học Mác - Lênin', 1);
CALL subj_insert('861302','Kinh tế chính trị Mác - Lênin', 1);
CALL subj_insert('861303','Chủ nghĩa xã hội khoa học', 1);
CALL subj_insert('861304','Tư tưởng Hồ Chí Minh', 1);
CALL subj_insert('861305','Lịch sử Đảng Cộng sản Việt Nam', 1);
CALL subj_insert('866101','Tiếng Anh I', 1);
CALL subj_insert('866102','Tiếng Anh II', 1);
CALL subj_insert('866103','Tiếng Anh III', 1);
CALL subj_insert('865006','Pháp luật đại cương', 1);
CALL subj_insert('841405','Xác suất thống kê', 1);
CALL subj_insert('841401','Giải tích 1', 1);
CALL subj_insert('841406','Giải tích 2', 1);
CALL subj_insert('841402','Đại số tuyến tính', 1);
CALL subj_insert('862406','Giáo dục quốc phòng và an ninh I', 1);
CALL subj_insert('862407','Giáo dục quốc phòng và an ninh II', 1);
CALL subj_insert('862408','Giáo dục quốc phòng và an ninh III', 1);
CALL subj_insert('862409','Giáo dục quốc phòng và an ninh IV', 1);
CALL subj_insert('862101','Giáo dục thể chất (I)', 1);
CALL subj_insert('BOBA11','Bóng bàn 1', 1);
CALL subj_insert('BOBA12','Bóng bàn 2', 1);
CALL subj_insert('BODA11','Bóng đá 1', 1);
CALL subj_insert('BODA12','Bóng đá 2', 1);
CALL subj_insert('BOCH11','Bóng chuyền 1', 1);
CALL subj_insert('BOCH12','Bóng chuyền 2', 1);
CALL subj_insert('BORO11','Bóng rổ 1', 1);
CALL subj_insert('BORO12','Bóng rổ 2', 1);
CALL subj_insert('CALO11','Cầu lông 1', 1);
CALL subj_insert('CALO12','Cầu lông 2', 1);
CALL subj_insert('841020','Cơ sở lập trình', 1);
CALL subj_insert('841303','Kỹ thuật lập trình', 1);
CALL subj_insert('841021','Kiến trúc máy tính', 1);
CALL subj_insert('841022','Hệ điều hành', 1);
CALL subj_insert('841403','Cấu trúc rời rạc', 1);
CALL subj_insert('841108','Cấu trúc dữ liệu và giải thuật', 1);
CALL subj_insert('841404','Mạng máy tính', 1);
CALL subj_insert('841044','Phương pháp lập trình hướng đối tượng', 1);
CALL subj_insert('841109','Cơ sở dữ liệu', 1);
CALL subj_insert('841110','Cơ sở trí tuệ nhân tạo', 1);
CALL subj_insert('841310','Lý thuyết đồ thị', 1);
CALL subj_insert('841047','Công nghệ phần mềm', 1);
CALL subj_insert('841414','Thiết kế và phân tích giải thuật', 1);
CALL subj_insert('841048','Phân tích thiết kế HTTT', 1);
CALL subj_insert('841070','Thực tập tốt nghiệp', 1);
CALL subj_insert('841099','Khóa luận tốt nghiệp', 1);
CALL subj_insert('841073','Seminar chuyên đề', 1);
CALL subj_insert('841072','Các công nghệ lập trình hiện đại', 1);
CALL subj_insert('841476','Đồ án chuyên ngành', 1);
CALL subj_insert('841058','Hệ điều hành mã nguồn mở', 1);
CALL subj_insert('841324','Phương pháp luận nghiên cứu khoa học', 1);
CALL subj_insert('841417','Mỹ thuật ứng dụng trong CNTT', 1);
CALL subj_insert('841418','Mô hình tài chính', 1);
CALL subj_insert('841419','Lập trình web và ứng dụng', 1);
CALL subj_insert('841420','Lập trình trực quan', 1);
CALL subj_insert('841422','Ngôn ngữ lập trình Python', 1);
CALL subj_insert('841423','Ngôn ngữ lập trình C#', 1);
CALL subj_insert('841107','Ngôn ngữ lập trình Java', 1);
CALL subj_insert('841424','Phương pháp mô hình hóa', 1);
CALL subj_insert('841426','Quản lý và bảo mật dữ liệu', 1);
CALL subj_insert('841429','Cơ sở dữ liệu nâng cao', 2);
CALL subj_insert('841407','Các hệ quản trị cơ sở dữ liệu', 2);
CALL subj_insert('841413','Cơ sở dữ liệu phân tán', 2);
CALL subj_insert('841111','Phân tích thiết kế hướng đối tượng', 2);
CALL subj_insert('841120','An toàn và bảo mật dữ liệu trong HTTT', 2);
CALL subj_insert('841412','Nguyên lý và phương pháp lập trình', 2);
CALL subj_insert('841068','Hệ thống thông tin doanh nghiệp', 2);
CALL subj_insert('841431','Quản lý dự án phần mềm', 2);
CALL subj_insert('841432','Phân tích dữ liệu', 2);
CALL subj_insert('841433','Các hệ thống cơ sở dữ liệu', 2);
CALL subj_insert('841434','Thương mại điện tử và ứng dụng', 2);
CALL subj_insert('841435','Hệ hỗ trợ quyết định', 2);
CALL subj_insert('841480','Xây dựng phần mềm theo mô hình phân lớp', 3);
CALL subj_insert('841408','Kiểm thử phần mềm', 3);
CALL subj_insert('841481','Thiết kế giao diện', 3);
CALL subj_insert('841461','Nhập môn thiết kế ứng dụng trên thiết bị di động', 3);
CALL subj_insert('841464','Lập trình web và ứng dụng nâng cao', 3);
CALL subj_insert('841113','Phát triển phần mềm mã nguồn mở', 3);
CALL subj_insert('841320','Công nghệ Internet of Things', 3);
CALL subj_insert('841323','Điện toán đám mây', 3);
CALL subj_insert('841467','Công nghệ .NET', 3);
CALL subj_insert('841468','Chuyên đề J2EE', 3);
CALL subj_insert('841470','Tương tác người máy', 3);
CALL subj_insert('841463','Phát triển ứng dụng trên thiết bị di động nâng cao', 3);
CALL subj_insert('841409','Mạng máy tính nâng cao', 4);
CALL subj_insert('841438','Lập trình ứng dụng mạng', 4);
CALL subj_insert('841411','Quản trị mạng', 4);
CALL subj_insert('841410','An ninh mạng máy tính', 4);
CALL subj_insert('841439','Mạng không dây', 4);
CALL subj_insert('841440','Phân tích và thiết kế mạng máy tính', 4);
CALL subj_insert('841437','Các giải thuật phân tán', 4);
CALL subj_insert('841441','Đánh giá hiệu năng mạng', 4);
CALL subj_insert('841442','Mạng đa phương tiện và di động', 4);
CALL subj_insert('841443','Phân tích mạng truyền thông xã hội', 4);
CALL subj_insert('841319','An toàn mạng không dây và di động', 4);
CALL subj_insert('841444','Quản trị và bảo trì hệ thống', 4);
CALL subj_insert('841445','Hệ thống ảo và khả năng mở rộng dữ liệu', 4);
CALL subj_insert('841446','Phân tích và xử lý ảnh', 5);
CALL subj_insert('841447','Khai thác dữ liệu và ứng dụng', 5);
CALL subj_insert('841448','Xử lý ngôn ngữ tự nhiên', 5);
CALL subj_insert('841449','Nhập môn máy học', 5);
CALL subj_insert('841450','Nhập môn dữ liệu lớn', 5);
CALL subj_insert('841451','Tính toán song song', 5);
CALL subj_insert('841452','Tính toán thông minh', 5);
CALL subj_insert('841116','Đồ hoạ máy tính', 5);
CALL subj_insert('841453','Phân tích và nhận dạng mẫu', 5);
CALL subj_insert('841454','Xử lý ảnh nâng cao', 5);
CALL subj_insert('841455','Ngôn ngữ học máy tính', 5);
CALL subj_insert('841456','Công nghệ tri thức', 5);
CALL subj_insert('841457','Học sâu', 5);
CALL subj_insert('841458','Trí tuệ nhân tạo nâng cao', 5);

CALL InsertStudent('841422','2023-2024','Học kỳ 1','01','3121410339','Ngô Lê Huệ Ngân','Nữ','2003-02-17','ngolehuengan170203@gmail.com','0123456789','HCM','Mr. Khoa','No');
CALL InsertStudent('841422','2023-2024','Học kỳ 1','01','3121410361','Trần Thụy Ái Nhân','Nữ','2003-10-06','ainhan610@gmail.com','0857288009','HCM','Mr. Khoa','No');
CALL InsertStudent('841422','2023-2024','Học kỳ 1','01','3120410369','Bùi Thị Yến Nhi','Nữ','2002-01-01','abc@gmail.com','0123456789','HCM','Mr. Khoa','No');