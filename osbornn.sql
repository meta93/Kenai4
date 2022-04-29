CREATE DATABASE kenai4

CREATE TABLE shelbys(
	ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT
	Sfname text,
	Slname text,
	Gender text,
	Phone text,
	Role text
);

INSERT INTO shelbys(Sfname,Slname,Gender,Phone,Role)
VALUES ('Hilda','Ogambe','F','+254 546 252 320','TeachOp'),
	   ('Sonia','Twum', 'F', '+233 520 565 212' , 'Saviour'),
       ('David','Mutinda', 'M', '+254 895 147 258', 'Presenter'),
       ('Patrick','Toworfe','M', '+233 897 456 123', 'Discussions Lead'),
       ('Hillary', 'Onyedika', 'M', '+234 258 369 741', 'Champion'); 

SELECT * FROM shelbys;