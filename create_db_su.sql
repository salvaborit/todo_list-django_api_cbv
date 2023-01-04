-- creates a django db 'todo_dev_db' with utf8 charset
-- creates superuser 'todo_dev' + grants

CREATE DATABASE IF NOT EXISTS todo_cbv_db CHARACTER SET utf8;

CREATE USER IF NOT EXISTS 'todo_dev'@'localhost' IDENTIFIED BY 'dev_pwd';
GRANT ALL PRIVILEGES ON todo_cbv_db.* TO 'todo_dev'@'localhost';
FLUSH PRIVILEGES;
