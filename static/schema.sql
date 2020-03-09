DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id integer primary key autoincrement,
    task_title text not null,
     task_desc text not null,
    done boolean not null,
    date_t datetime not null
);


INSERT INTO tasks (id, task_title, task_desc,done, date_t)
VALUES (null, 'task',"description", 0, datetime(current_timestamp));
