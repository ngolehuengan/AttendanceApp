DROP DATABASE IF EXISTS attendance;
CREATE DATABASE attendance;
USE attendance;

-- -- -- -- -- TABLES -- -- -- -- --
CREATE TABLE account (
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(16) NOT NULL,
    password VARCHAR(32) NOT NULL
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

DELIMITER ;

-- -- -- -- -- VALUES -- -- -- -- --
INSERT INTO account (username,password) VALUE
	('admin','admin')