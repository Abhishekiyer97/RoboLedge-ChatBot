BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `expenditure1` (
	`SpentID`	INTEGER,
	`userID`	TEXT,
	`amount`	INTEGER,
	`date`	TEXT,
	`item`	TEXT,
	PRIMARY KEY(`SpentID`)
);
INSERT INTO `expenditure1` VALUES (1,'aditya',800,'2018-06-04','food');
INSERT INTO `expenditure1` VALUES (2,'arjun',500,'2018-07-03','');
INSERT INTO `expenditure1` VALUES (3,'aditya',550,'2018-06-04','');
INSERT INTO `expenditure1` VALUES (4,'aditya',1500,'2018-07-03','');
INSERT INTO `expenditure1` VALUES (5,'aditya',899,'2018-07-06',NULL);
INSERT INTO `expenditure1` VALUES (6,'arjun',5000,'2018-06-23','');
INSERT INTO `expenditure1` VALUES (7,'arjun',50,'2018-06-02','');
INSERT INTO `expenditure1` VALUES (8,'aditya',700,'2018-07-30','');
INSERT INTO `expenditure1` VALUES (9,'arjun',2000,'2018-05-02','');
INSERT INTO `expenditure1` VALUES (10,'arjun',990,'2018-06-05','');
INSERT INTO `expenditure1` VALUES (11,'abhi',90000,'2018-06-05','');
INSERT INTO `expenditure1` VALUES (12,'abhi',95000,'2018-06-02','');
INSERT INTO `expenditure1` VALUES (13,'abhi',60000,'2018-06-08','');
INSERT INTO `expenditure1` VALUES (14,'abhi',75000,'2018-06-20','');
INSERT INTO `expenditure1` VALUES (15,'abhi',90000,'2018-06-18','');
INSERT INTO `expenditure1` VALUES (16,'abhi',95500,'2018-06-26','');
INSERT INTO `expenditure1` VALUES (17,'abhi',50000,'2018-06-30','');
INSERT INTO `expenditure1` VALUES (18,'aditya',10000,'2018-07-12',NULL);
CREATE VIEW temp2 as
select * from expenditure1
where strftime('%m', date) = '07' and userID = 'aditya';
CREATE VIEW temp1 as
select * from expenditure1
where strftime('%m', date) = '07' and userID = 'aditya';
CREATE VIEW tempo as
select * from expenditure1
where strftime('%m', date) = '07' and userID = 'aditya';
COMMIT;
