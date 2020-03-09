from flask import Flask, g, flash, request, redirect, url_for
from flask import render_template
import os
import sqlite3
from datetime import datetime


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='secretkete',
    DATABASE=os.path.join(app.root_path, 'db/todo.db'),
    SITE_NAME='ToDo'
))

def db_connection():
    if not g.get('db'):
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con
    return g.db

@app.teardown_appcontext
def close_db(error):
    if g.get('db'):
        g.db.close()


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/mytasks", methods=['GET','POST'])
def mytasks():
    error = None
    if request.method == "POST":
        task_title = request.form["task_title"].strip()
        task_desc = request.form["task_desc"].strip()
        if len(task_title) > 0 and len(task_desc)>0:
            done = 0
            date = datetime.now()
            db = db_connection()
            db.execute("INSERT INTO tasks (id, task_title, task_desc,done, date_t)VALUES (?, ?,?, ?, ?);",
                       [None, task_title,task_desc,done,date])
            db.commit()
            flash("Added new task!")
            return redirect(url_for("mytasks"))

        else:
            error = "no title or description, cant add task"
    else:
        db = db_connection()
        cursor = db.execute("select * from tasks")
        tasks = cursor.fetchall()
        return render_template('mytasks.html', tasks=tasks, error= error)


if __name__ == '__main__':
    app.run()
