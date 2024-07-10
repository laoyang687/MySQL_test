mysql -h -loacalhost -u -root -p

show databases;  查看数据库
create database testdb;   创建数据库，testdb是库名
drop database testdb;  删除数据库
use laoyang  show tables; 查看数据库laoyang下面有多少表格，注意：use laoyang没有分号 show tables;有分号
desc city; 查看表的结构


增、删、改、查语句(1.insert into xx xx  values xx、 2.delete from xx where xx、update set where、select *from )
增(insert)
1.插入单行数据
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
示例：
INSERT INTO users (name, age, email)
VALUES ('John Doe', 30, 'john.doe@example.com');

2.插入多行数据
INSERT INTO table_name (column1, column2, ...)
VALUES
    (value1, value2, ...),
    (value1, value2, ...),
    ...;
示例：
INSERT INTO users (name, age, email)
VALUES
    ('John Doe', 30, 'john.doe@example.com'),
    ('Jane Smith', 25, 'jane.smith@example.com');

删除(delete)
1.删除特定行
DELETE FROM table_name
WHERE condition;
示例：
DELETE FROM users
WHERE id = 1;
2.清空表中所有数据;
DELETE FROM table_name;
示例：
DELETE FROM users;

修改(update)
1.更新特定行的数据;
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
示例：
UPDATE users
SET age = 31
WHERE name = 'John Doe';

查询(select)
1.查询所有数据
SELECT * FROM table_name;
示例：
SELECT * FROM users;
2.查询特定的数据
SELECT column1, column2, ...
FROM table_name;
示例：
SELECT name, email
FROM users;
3.带条件的查询
SELECT * FROM table_name
WHERE condition;
示例：
SELECT * FROM users
WHERE age > 25;

